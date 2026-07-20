(function () {
  var GA_ID = 'G-CP46SFNL6W';
  var analyticsLoaded = false;

  function loadAnalytics() {
    if (analyticsLoaded || !GA_ID || !document.head) {
      return;
    }

    analyticsLoaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () {
      window.dataLayer.push(arguments);
    };

    window.gtag('js', new Date());
    window.gtag('config', GA_ID);

    var gaScript = document.createElement('script');
    gaScript.async = true;
    gaScript.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(GA_ID);
    document.head.appendChild(gaScript);

    removeAnalyticsListeners();
  }

  var analyticsEvents = ['pointerdown', 'scroll', 'keydown', 'touchstart'];

  function removeAnalyticsListeners() {
    analyticsEvents.forEach(function (eventName) {
      window.removeEventListener(eventName, loadAnalytics, listenerOptions);
    });
  }

  var listenerOptions = { passive: true };

  analyticsEvents.forEach(function (eventName) {
    window.addEventListener(eventName, loadAnalytics, listenerOptions);
  });

  if ('requestIdleCallback' in window) {
    window.requestIdleCallback(loadAnalytics, { timeout: 3500 });
  } else {
    window.setTimeout(loadAnalytics, 3500);
  }

  var yearEl = document.querySelector('[data-year]');
  if (yearEl) {
    yearEl.textContent = String(new Date().getFullYear());
  }

  var menuBtn = document.querySelector('[data-menu-btn]');
  var nav = document.querySelector('.nav');
  if (menuBtn && nav) {
    menuBtn.addEventListener('click', function () {
      nav.classList.toggle('open');
    });
  }

  var revealNodes = document.querySelectorAll('[data-reveal]');
  if (revealNodes.length) {
    if ('IntersectionObserver' in window) {
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.15, rootMargin: '0px 0px -30px 0px' });

      revealNodes.forEach(function (node) {
        observer.observe(node);
      });
    } else {
      revealNodes.forEach(function (node) {
        node.classList.add('is-visible');
      });
    }
  }

  var liteFrames = document.querySelectorAll('.video-frame-lite[data-youtube-id]');
  liteFrames.forEach(function (frame) {
    var btn = frame.querySelector('.video-load-btn');
    if (!btn) return;
    btn.addEventListener('click', function () {
      if (frame.dataset.loaded === '1') return;
      var videoId = frame.dataset.youtubeId;
      var title = frame.dataset.youtubeTitle || 'YouTube video';
      if (!videoId) return;

      var iframe = document.createElement('iframe');
      iframe.src = 'https://www.youtube-nocookie.com/embed/' + videoId + '?autoplay=1&rel=0';
      iframe.title = title;
      iframe.loading = 'lazy';
      iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
      iframe.referrerPolicy = 'strict-origin-when-cross-origin';
      iframe.allowFullscreen = true;

      frame.innerHTML = '';
      frame.appendChild(iframe);
      frame.dataset.loaded = '1';
    });
  });

  var homePlanner = document.querySelector('[data-home-planner]');
  if (homePlanner) {
    var plannerData = {
      banner: {
        title: 'Current Banner Worth It?',
        copy: 'Start with the current banner page if your main Seven Deadly Sins Origin question is whether Gowther is worth spending on before the next maintenance window.',
        href: '/banners/current/',
        label: 'Open Current Banner Guide'
      },
      build: {
        title: 'Current Tier List and Build Priorities',
        copy: 'Open the tier list route when you need to decide which Seven Deadly Sins Origin characters, beginner teams, and raid teams deserve scarce materials first.',
        href: '/tier-list/',
        label: 'Open Tier List Hub'
      },
      growth: {
        title: 'Daily Growth and Diamond Farming',
        copy: 'Use the growth route when your 7DS Origin account needs a better daily checklist, weekly reset plan, diamond path, or shop-spending order.',
        href: '/daily-checklist/',
        label: 'Open Daily Checklist'
      },
      fix: {
        title: 'Bugs, Errors, and Performance Fixes',
        copy: 'Start with troubleshooting when login, install, update, crash, controller, or mobile performance problems block normal play.',
        href: '/bugs-errors/',
        label: 'Open Bugs and Errors Hub'
      }
    };
    var plannerTitle = homePlanner.querySelector('[data-planner-title]');
    var plannerCopy = homePlanner.querySelector('[data-planner-copy]');
    var plannerLink = homePlanner.querySelector('[data-planner-link]');
    var plannerChoices = homePlanner.querySelectorAll('input[name="home-planner"]');

    function updatePlanner(value) {
      var next = plannerData[value];
      if (!next || !plannerTitle || !plannerCopy || !plannerLink) return;
      plannerTitle.textContent = next.title;
      plannerCopy.textContent = next.copy;
      plannerLink.href = next.href;
      plannerLink.textContent = next.label;
    }

    plannerChoices.forEach(function (choice) {
      choice.addEventListener('change', function () {
        updatePlanner(choice.value);
      });
    });
  }
})();
