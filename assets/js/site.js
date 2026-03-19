(function () {
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
})();
