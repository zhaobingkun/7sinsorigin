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
})();
