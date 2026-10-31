export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.hostname === "www.7sinsorigin.com") {
      url.hostname = "7sinsorigin.com";
      return Response.redirect(url.toString(), 308);
    }

    return env.ASSETS.fetch(request);
  },
};
