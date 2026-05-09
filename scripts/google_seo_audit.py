from __future__ import annotations

import csv
import json
import os
from datetime import date, timedelta
from pathlib import Path


ROOT = Path("/Users/zhaobingkun/dev/7sinsorigin.com/7sinsorigin")
REPORTS = ROOT / "reports"
CONFIG_PATH = ROOT / "scripts" / "google_api_config.json"


def load_local_config() -> dict:
    if not CONFIG_PATH.exists():
        return {}
    try:
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in config file: {CONFIG_PATH}") from exc


def require_setting(name: str, config: dict) -> str:
    value = str(config.get(name, "")).strip() or os.getenv(name, "").strip()
    if not value:
        raise SystemExit(f"Missing required setting: {name}")
    return value


def require_google_libs():
    try:
        import httplib2  # noqa: F401
        from google.oauth2 import service_account  # noqa: F401
        from googleapiclient.discovery import build  # noqa: F401
        import google_auth_httplib2  # noqa: F401
    except Exception as exc:  # pragma: no cover
        raise SystemExit(
            "Missing Google API libraries. Install with:\n"
            "pip install google-api-python-client google-auth google-auth-httplib2"
        ) from exc


def resolve_path(path_str: str) -> Path:
    path = Path(path_str)
    if path.is_absolute():
        return path
    return (CONFIG_PATH.parent / path).resolve()


def build_clients(config: dict):
    import google_auth_httplib2
    import httplib2
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    creds_path = require_setting("GOOGLE_APPLICATION_CREDENTIALS", config)
    creds_file = resolve_path(creds_path)
    if not creds_file.exists():
        raise SystemExit(f"Service account file not found: {creds_file}")
    credentials = service_account.Credentials.from_service_account_file(
        str(creds_file),
        scopes=[
            "https://www.googleapis.com/auth/webmasters.readonly",
            "https://www.googleapis.com/auth/analytics.readonly",
        ],
    )
    timeout = int(str(config.get("HTTP_TIMEOUT_SECS", "")).strip() or os.getenv("HTTP_TIMEOUT_SECS", "120"))
    proxy_host = str(config.get("PROXY_HOST", "")).strip() or os.getenv("PROXY_HOST", "").strip()
    proxy_port = str(config.get("PROXY_PORT", "")).strip() or os.getenv("PROXY_PORT", "").strip()
    proxy_info = None
    if proxy_host and proxy_port:
        proxy_info = httplib2.ProxyInfo(
            proxy_type=httplib2.socks.PROXY_TYPE_HTTP,
            proxy_host=proxy_host,
            proxy_port=int(proxy_port),
        )
    http = google_auth_httplib2.AuthorizedHttp(
        credentials,
        http=httplib2.Http(timeout=timeout, proxy_info=proxy_info),
    )
    run_gsc = str(config.get("RUN_GSC", "")).strip().lower() or os.getenv("RUN_GSC", "true")
    run_gsc = run_gsc in {"1", "true", "yes", "on"}
    run_ga4 = str(config.get("RUN_GA4", "")).strip().lower() or os.getenv("RUN_GA4", "true")
    run_ga4 = run_ga4 in {"1", "true", "yes", "on"}
    run_admin = str(config.get("RUN_GA4_ADMIN", "")).strip().lower() or os.getenv("RUN_GA4_ADMIN", "false")
    run_admin = run_admin in {"1", "true", "yes", "on"}

    search_console = build("searchconsole", "v1", http=http, cache_discovery=False) if run_gsc else None
    analytics_data = build("analyticsdata", "v1beta", http=http, cache_discovery=False) if run_ga4 else None
    analytics_admin = build("analyticsadmin", "v1alpha", http=http, cache_discovery=False) if run_admin else None
    return search_console, analytics_data, analytics_admin


def last_n_days(days: int) -> tuple[str, str]:
    end = date.today() - timedelta(days=1)
    start = end - timedelta(days=days - 1)
    return start.isoformat(), end.isoformat()


def fetch_search_console(search_console, site_url: str, start_date: str, end_date: str, row_limit: int) -> dict:
    def query(dimensions: list[str]):
        body = {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": dimensions,
            "rowLimit": row_limit,
        }
        return (
            search_console.searchanalytics()
            .query(siteUrl=site_url, body=body)
            .execute()
            .get("rows", [])
        )

    return {
        "query_page": query(["query", "page"]),
        "page": query(["page"]),
        "query": query(["query"]),
        "country": query(["country"]),
        "device": query(["device"]),
    }


def fetch_ga4(analytics_data, property_id: str, start_date: str, end_date: str) -> dict:
    property_name = f"properties/{property_id}"

    def run_report(dimensions: list[str], metrics: list[str], limit: int = 10000):
        body = {
            "dateRanges": [{"startDate": start_date, "endDate": end_date}],
            "dimensions": [{"name": item} for item in dimensions],
            "metrics": [{"name": item} for item in metrics],
            "limit": str(limit),
        }
        return analytics_data.properties().runReport(property=property_name, body=body).execute()

    return {
        "pages": run_report(
            ["pagePath", "deviceCategory"],
            ["sessions", "screenPageViews", "engagementRate", "averageSessionDuration"],
        ),
        "sources": run_report(
            ["sessionSource", "sessionMedium"],
            ["sessions", "engagementRate", "averageSessionDuration"],
        ),
    }


def fetch_admin(analytics_admin, property_id: str) -> dict:
    property_name = f"properties/{property_id}"
    streams = analytics_admin.properties().dataStreams().list(parent=property_name).execute().get("dataStreams", [])
    return {"property": property_name, "streams": streams}


def rows_to_csv(path: Path, header: list[str], rows: list[list[object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(header)
        writer.writerows(rows)


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def summarize_search_console(data: dict) -> list[str]:
    lines: list[str] = []
    query_page = data["query_page"]
    high_impression_low_ctr = [
        row for row in query_page
        if row.get("impressions", 0) >= 50 and row.get("ctr", 0) < 0.03
    ]
    near_page_one = [
        row for row in query_page
        if row.get("impressions", 0) >= 30 and 8 <= row.get("position", 0) <= 20
    ]
    lines.append(f"- Search Console query/page rows: {len(query_page)}")
    lines.append(f"- High-impression low-CTR opportunities: {len(high_impression_low_ctr)}")
    lines.append(f"- Rank 8-20 opportunities: {len(near_page_one)}")
    for row in sorted(high_impression_low_ctr, key=lambda item: item.get("impressions", 0), reverse=True)[:10]:
        query, page = row["keys"]
        lines.append(
            f"  - CTR fix: `{query}` -> `{page}` | impressions {row['impressions']:.0f}, ctr {row['ctr']:.2%}, pos {row['position']:.1f}"
        )
    for row in sorted(near_page_one, key=lambda item: item.get("impressions", 0), reverse=True)[:10]:
        query, page = row["keys"]
        lines.append(
            f"  - Content/internal-link candidate: `{query}` -> `{page}` | impressions {row['impressions']:.0f}, ctr {row['ctr']:.2%}, pos {row['position']:.1f}"
        )
    return lines


def summarize_ga4(report: dict) -> list[str]:
    lines: list[str] = []
    page_rows = report["pages"].get("rows", [])
    weak_engagement = []
    for row in page_rows:
        dims = [item["value"] for item in row.get("dimensionValues", [])]
        metrics = [item["value"] for item in row.get("metricValues", [])]
        page = dims[0] if dims else ""
        sessions = float(metrics[0]) if metrics else 0.0
        engagement = float(metrics[2]) if len(metrics) > 2 else 0.0
        if sessions >= 20 and engagement < 0.45:
            weak_engagement.append((page, sessions, engagement))
    lines.append(f"- GA4 page/device rows: {len(page_rows)}")
    lines.append(f"- Pages with sessions >= 20 and engagementRate < 45%: {len(weak_engagement)}")
    for page, sessions, engagement in sorted(weak_engagement, key=lambda item: item[1], reverse=True)[:10]:
        lines.append(f"  - UX/content review: `{page}` | sessions {sessions:.0f}, engagement {engagement:.2%}")
    return lines


def export_search_console(data: dict) -> None:
    query_page_rows = []
    for row in data["query_page"]:
        query, page = row["keys"]
        query_page_rows.append([query, page, row.get("clicks", 0), row.get("impressions", 0), row.get("ctr", 0), row.get("position", 0)])
    rows_to_csv(
        REPORTS / "gsc-query-page.csv",
        ["query", "page", "clicks", "impressions", "ctr", "position"],
        query_page_rows,
    )

    page_rows = []
    for row in data["page"]:
        page_rows.append([row["keys"][0], row.get("clicks", 0), row.get("impressions", 0), row.get("ctr", 0), row.get("position", 0)])
    rows_to_csv(
        REPORTS / "gsc-pages.csv",
        ["page", "clicks", "impressions", "ctr", "position"],
        page_rows,
    )

    query_rows = []
    for row in data["query"]:
        query_rows.append([row["keys"][0], row.get("clicks", 0), row.get("impressions", 0), row.get("ctr", 0), row.get("position", 0)])
    rows_to_csv(
        REPORTS / "gsc-queries.csv",
        ["query", "clicks", "impressions", "ctr", "position"],
        query_rows,
    )


def export_ga4(report: dict) -> None:
    page_rows = []
    for row in report["pages"].get("rows", []):
        dims = [item["value"] for item in row.get("dimensionValues", [])]
        metrics = [item["value"] for item in row.get("metricValues", [])]
        page_rows.append(dims + metrics)
    rows_to_csv(
        REPORTS / "ga4-pages.csv",
        ["pagePath", "deviceCategory", "sessions", "screenPageViews", "engagementRate", "averageSessionDuration"],
        page_rows,
    )

    source_rows = []
    for row in report["sources"].get("rows", []):
        dims = [item["value"] for item in row.get("dimensionValues", [])]
        metrics = [item["value"] for item in row.get("metricValues", [])]
        source_rows.append(dims + metrics)
    rows_to_csv(
        REPORTS / "ga4-sources.csv",
        ["sessionSource", "sessionMedium", "sessions", "engagementRate", "averageSessionDuration"],
        source_rows,
    )


def main() -> None:
    require_google_libs()
    config = load_local_config()
    run_gsc = str(config.get("RUN_GSC", "")).strip().lower() or os.getenv("RUN_GSC", "true")
    run_gsc = run_gsc in {"1", "true", "yes", "on"}
    run_ga4 = str(config.get("RUN_GA4", "")).strip().lower() or os.getenv("RUN_GA4", "true")
    run_ga4 = run_ga4 in {"1", "true", "yes", "on"}
    if not run_gsc and not run_ga4:
        raise SystemExit("At least one of RUN_GSC or RUN_GA4 must be true.")
    site_url = require_setting("GSC_SITE_URL", config) if run_gsc else ""
    property_id = require_setting("GA4_PROPERTY_ID", config) if run_ga4 else ""
    days = int(str(config.get("SEO_AUDIT_DAYS", "")).strip() or os.getenv("SEO_AUDIT_DAYS", "90"))
    gsc_row_limit = int(str(config.get("GSC_ROW_LIMIT", "")).strip() or os.getenv("GSC_ROW_LIMIT", "5000"))
    start_date, end_date = last_n_days(days)

    search_console, analytics_data, analytics_admin = build_clients(config)
    gsc = fetch_search_console(search_console, site_url, start_date, end_date, gsc_row_limit) if run_gsc else None
    ga4 = fetch_ga4(analytics_data, property_id, start_date, end_date) if run_ga4 else None
    admin = fetch_admin(analytics_admin, property_id) if analytics_admin else {"property": f"properties/{property_id}" if property_id else "", "streams": [], "skipped": True}

    if gsc:
        export_search_console(gsc)
    if ga4:
        export_ga4(ga4)
    if analytics_admin or property_id:
        write_json(REPORTS / "ga4-admin.json", admin)

    summary_lines = [
        f"# SEO Audit Summary",
        "",
        f"- Site: `{site_url or 'disabled'}`",
        f"- GA4 property: `{property_id or 'disabled'}`",
        f"- Date range: `{start_date}` to `{end_date}`",
        "",
    ]
    if gsc:
        summary_lines.extend(["## Search Console", *summarize_search_console(gsc), ""])
    if ga4:
        summary_lines.extend(["## GA4", *summarize_ga4(ga4), ""])
    summary_lines.extend([
        "## Files",
    ])
    if gsc:
        summary_lines.extend([
            "- `reports/gsc-query-page.csv`",
            "- `reports/gsc-pages.csv`",
            "- `reports/gsc-queries.csv`",
        ])
    if ga4:
        summary_lines.extend([
            "- `reports/ga4-pages.csv`",
            "- `reports/ga4-sources.csv`",
        ])
    if analytics_admin or property_id:
        summary_lines.append("- `reports/ga4-admin.json`")
    summary_path = REPORTS / "seo-audit-summary.md"
    summary_path.write_text("\n".join(summary_lines), encoding="utf-8")
    print(summary_path)


if __name__ == "__main__":
    main()
