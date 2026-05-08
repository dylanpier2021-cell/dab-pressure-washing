// ============================================
// main.js — keep this file under 5KB
// All non-essential JS lazy-loaded or deferred.
// ============================================

(function() {
  'use strict';

  // -- Auto-update copyright year ----------------
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // -- Mobile menu toggle ------------------------
  var menuBtn = document.querySelector('[data-mobile-menu-toggle]');
  var menu = document.querySelector('[data-mobile-menu]');
  if (menuBtn && menu) {
    menuBtn.addEventListener('click', function() {
      var isOpen = menu.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });
  }

  // -- Phone-click tracking (GA4 + dataLayer) -----
  // Sends an event whenever a tel: link is clicked.
  // Configure conversions in GA4 + GHL accordingly.
  document.querySelectorAll('a[href^="tel:"]').forEach(function(link) {
    link.addEventListener('click', function() {
      var location = link.getAttribute('data-track') || 'phone-click';
      if (typeof gtag === 'function') {
        gtag('event', 'phone_click', {
          event_category: 'engagement',
          event_label: location,
          phone_number: link.getAttribute('href').replace('tel:', '')
        });
      }
      if (window.dataLayer) {
        window.dataLayer.push({
          event: 'phone_click',
          location: location
        });
      }
    });
  });

  // -- Smooth scroll for anchor links -------------
  document.querySelectorAll('a[href^="#"]').forEach(function(link) {
    link.addEventListener('click', function(e) {
      var href = link.getAttribute('href');
      if (href === '#' || href.length < 2) return;
      var target = document.querySelector(href);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  // -- Intersection observer for fade-up animations
  // Adds .in-view to elements with [data-animate] when scrolled into view
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -10% 0px' });

    document.querySelectorAll('[data-animate]').forEach(function(el) {
      io.observe(el);
    });
  }

})();
