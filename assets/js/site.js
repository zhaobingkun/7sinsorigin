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
})();
