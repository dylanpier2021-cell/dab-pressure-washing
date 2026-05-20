(function () {
  // Year
  document.querySelectorAll('#year').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  // Mobile menu
  var MENU_HTML = '<div id="mobile-menu" class="fixed inset-0 z-30 bg-paper flex flex-col pt-20 pb-10 px-6 transform -translate-x-full transition-transform duration-300 ease-in-out lg:hidden" aria-hidden="true"><nav class="flex flex-col gap-6 mt-8 text-2xl font-display" aria-label="Mobile"><a href="/services/" class="py-2 border-b border-line hover:text-accent transition-colors">Services</a><a href="/service-locations/" class="py-2 border-b border-line hover:text-accent transition-colors">Service Locations</a><a href="/portfolio/" class="py-2 border-b border-line hover:text-accent transition-colors">Portfolio</a><a href="/blog/" class="py-2 border-b border-line hover:text-accent transition-colors">Blog</a><a href="/about.html" class="py-2 border-b border-line hover:text-accent transition-colors">About</a><a href="/contact.html" class="py-2 border-b border-line hover:text-accent transition-colors">Contact</a></nav><div class="mt-auto space-y-4"><a href="tel:+12176892050" class="btn-accent w-full flex items-center justify-center gap-2 text-lg"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>(217) 689-2050</a><a href="/contact.html#quote" class="btn-outline w-full flex items-center justify-center">Get Free Quote</a></div></div>';

  var ICON_MENU = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg>';
  var ICON_CLOSE = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M18 6L6 18M6 6l12 12"/></svg>';

  function initMobileMenu() {
    var btn = document.querySelector('[data-mobile-menu-toggle]');
    if (!btn) return;

    if (!document.getElementById('mobile-menu')) {
      var header = document.querySelector('header');
      if (header) header.insertAdjacentHTML('afterend', MENU_HTML);
    }

    var menu = document.getElementById('mobile-menu');
    if (!menu) return;

    var isOpen = false;

    function openMenu() {
      isOpen = true;
      menu.classList.remove('-translate-x-full');
      menu.setAttribute('aria-hidden', 'false');
      btn.setAttribute('aria-expanded', 'true');
      btn.innerHTML = ICON_CLOSE;
      document.body.style.overflow = 'hidden';
    }

    function closeMenu() {
      isOpen = false;
      menu.classList.add('-translate-x-full');
      menu.setAttribute('aria-hidden', 'true');
      btn.setAttribute('aria-expanded', 'false');
      btn.innerHTML = ICON_MENU;
      document.body.style.overflow = '';
    }

    btn.addEventListener('click', function () {
      if (isOpen) { closeMenu(); } else { openMenu(); }
    });

    menu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', closeMenu);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && isOpen) { closeMenu(); }
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth >= 1024 && isOpen) { closeMenu(); }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMobileMenu);
  } else {
    initMobileMenu();
  }

  // Phone-click tracking (GA4 + dataLayer)
  document.querySelectorAll('a[href^="tel:"]').forEach(function (link) {
    link.addEventListener('click', function () {
      var location = link.getAttribute('data-track') || 'phone-click';
      if (typeof gtag === 'function') {
        gtag('event', 'phone_click', { event_category: 'engagement', event_label: location });
      }
      if (window.dataLayer) {
        window.dataLayer.push({ event: 'phone_click', location: location });
      }
    });
  });

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var href = link.getAttribute('href');
      if (href === '#' || href.length < 2) return;
      var target = document.querySelector(href);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  // Intersection observer for fade-up animations
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -10% 0px' });
    document.querySelectorAll('[data-animate]').forEach(function (el) { io.observe(el); });
  }

})();
