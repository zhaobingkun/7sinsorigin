(function () {
  var GA_ID = 'G-CP46SFNL6W';
  var privacyStorageKey = '7so_privacy_choice_v1';
  var analyticsLoaded = false;

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () {
    window.dataLayer.push(arguments);
  };
  window.gtag('consent', 'default', {
    ad_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied',
    analytics_storage: 'denied',
    wait_for_update: 500
  });

  function loadAnalytics() {
    if (analyticsLoaded || !GA_ID || !document.head) {
      return;
    }

    analyticsLoaded = true;
    window.gtag('js', new Date());
    window.gtag('config', GA_ID, { anonymize_ip: true });

    var gaScript = document.createElement('script');
    gaScript.async = true;
    gaScript.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(GA_ID);
    document.head.appendChild(gaScript);

  }

  function readPrivacyChoice() {
    try {
      return window.localStorage.getItem(privacyStorageKey);
    } catch (error) {
      return null;
    }
  }

  function savePrivacyChoice(choice) {
    try {
      window.localStorage.setItem(privacyStorageKey, choice);
    } catch (error) {
      // Consent still applies for the current page when storage is unavailable.
    }
  }

  function applyPrivacyChoice(choice) {
    var granted = choice === 'accepted';
    window.gtag('consent', 'update', {
      ad_storage: 'denied',
      ad_user_data: 'denied',
      ad_personalization: 'denied',
      analytics_storage: granted ? 'granted' : 'denied'
    });
    if (granted) loadAnalytics();
  }

  var isChinese = (document.documentElement.lang || '').toLowerCase().indexOf('zh') === 0;
  var privacyCopy = isChinese ? {
    title: '隐私选择',
    body: '本站只在你允许后加载 Google Analytics。必要存储仅用于记住这个选择。未来启用广告时，会继续按照适用地区要求征求同意。',
    accept: '允许分析 Cookie',
    reject: '拒绝可选项',
    policy: '查看隐私政策'
  } : {
    title: 'Privacy choices',
    body: 'Google Analytics loads only after you allow it. Essential storage is used only to remember this choice. Advertising consent will remain subject to applicable regional requirements.',
    accept: 'Allow analytics',
    reject: 'Reject optional',
    policy: 'Read privacy policy'
  };

  var privacyPanel = document.createElement('section');
  privacyPanel.className = 'privacy-panel';
  privacyPanel.hidden = true;
  privacyPanel.setAttribute('role', 'dialog');
  privacyPanel.setAttribute('aria-modal', 'true');
  privacyPanel.setAttribute('aria-labelledby', 'privacy-panel-title');
  privacyPanel.innerHTML = '<div class="privacy-panel-inner">' +
    '<div><h2 id="privacy-panel-title">' + privacyCopy.title + '</h2><p>' + privacyCopy.body + '</p></div>' +
    '<div class="privacy-panel-actions"><button class="btn" type="button" data-privacy-accept>' + privacyCopy.accept + '</button>' +
    '<button class="btn btn-secondary" type="button" data-privacy-reject>' + privacyCopy.reject + '</button>' +
    '<a href="' + (isChinese ? '/zh/privacy/' : '/privacy/') + '">' + privacyCopy.policy + '</a></div></div>';
  document.body.appendChild(privacyPanel);

  function openPrivacyPanel() {
    privacyPanel.hidden = false;
    var firstButton = privacyPanel.querySelector('[data-privacy-accept]');
    if (firstButton) firstButton.focus();
  }

  function closePrivacyPanel() {
    privacyPanel.hidden = true;
  }

  privacyPanel.querySelector('[data-privacy-accept]').addEventListener('click', function () {
    savePrivacyChoice('accepted');
    applyPrivacyChoice('accepted');
    closePrivacyPanel();
  });

  privacyPanel.querySelector('[data-privacy-reject]').addEventListener('click', function () {
    savePrivacyChoice('rejected');
    applyPrivacyChoice('rejected');
    closePrivacyPanel();
  });

  document.querySelectorAll('[data-privacy-settings]').forEach(function (button) {
    button.addEventListener('click', openPrivacyPanel);
  });

  var savedPrivacyChoice = readPrivacyChoice();
  if (savedPrivacyChoice === 'accepted' || savedPrivacyChoice === 'rejected') {
    applyPrivacyChoice(savedPrivacyChoice);
  } else {
    openPrivacyPanel();
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
        copy: 'Start with the current banner page to confirm whether a Hero Pick Up is active. After the August 5 maintenance, save until Netmarble publishes the next official banner notice.',
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
