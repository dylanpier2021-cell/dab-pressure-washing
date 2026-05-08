# docs/launch-checklist.md — Pre-Launch QA

Walk this checklist on every site before handoff. Do not skip steps. If a step fails, fix it and restart from that section.

---

## Performance

- [ ] Lighthouse mobile ≥ 95 on home, top service page, and a city page
- [ ] LCP < 2.5s, INP < 200ms, CLS < 0.1 (mobile, throttled 4G)
- [ ] Total page weight < 500KB compressed on every template
- [ ] Hero image preloaded, all other images lazy-loaded
- [ ] All images WebP or AVIF, with `width` and `height` attributes
- [ ] No render-blocking JS in `<head>`
- [ ] All third-party scripts have `defer` or `async`
- [ ] CSS is minified, unused Tailwind classes purged
- [ ] No CDN Tailwind (`cdn.tailwindcss.com`) anywhere

## SEO Foundation

- [ ] Every page has a unique `<title>` (50–60 chars)
- [ ] Every page has a unique meta description (140–160 chars)
- [ ] Every page has a `<link rel="canonical">`
- [ ] Every page has exactly one `<h1>`
- [ ] Heading hierarchy is logical (no h2 → h4 jumps)
- [ ] All images have descriptive alt text
- [ ] OG and Twitter card tags present and valid
- [ ] Favicon and apple-touch-icon present
- [ ] `lang="en"` on `<html>`
- [ ] Viewport meta tag present

## Schema

- [ ] LocalBusiness schema on home and contact, validates in Rich Results Test
- [ ] Service schema on every service page, validates
- [ ] FAQ schema only where FAQs are visible on the page
- [ ] BreadcrumbList schema on inner pages
- [ ] No fabricated `aggregateRating` data
- [ ] `@id` references resolve correctly across schema blocks

## Index Safety

- [ ] No keyword stuffing in copy, alt text, or meta tags
- [ ] City pages have 500+ unique words each with local references
- [ ] No hidden text, no `display:none` for SEO content
- [ ] No Lorem Ipsum, no placeholder testimonials in production
- [ ] No mass-duplicate content across geo pages
- [ ] All external links: `rel="noopener"`
- [ ] No intrusive mobile interstitials

## GHL Integration

- [ ] All lead forms are GHL embeds (no native HTML POST forms)
- [ ] Form ID and Calendar ID match the live GHL sub-account
- [ ] Test submission lands in the GHL pipeline correctly
- [ ] Calendar bookings hit the right calendar
- [ ] Tracking number is the GHL number, not the personal/business cell
- [ ] Click-to-call links use `tel:+1XXXXXXXXXX` format
- [ ] Chat widget loads and accepts a test message
- [ ] GHL tracking pixel fires on page load (verify in GHL reporting)

## Indexability

- [ ] `robots.txt` allows crawl and points to sitemap
- [ ] `sitemap.xml` lists every indexable page with `lastmod`
- [ ] No `noindex` tags left over from staging
- [ ] No `Disallow: /` left over from staging
- [ ] Submitted to Google Search Console
- [ ] Sitemap submitted in Search Console
- [ ] Live URL inspection passes for home + 1 service + 1 city page

## Browser & Device QA

- [ ] Renders correctly at 375px width (iPhone SE)
- [ ] Renders correctly at 768px (tablet)
- [ ] Renders correctly at 1280px+ (desktop)
- [ ] Tested in Chrome, Safari, Firefox
- [ ] Tested on at least one real iOS device
- [ ] Tested on at least one real Android device
- [ ] No horizontal scroll on any breakpoint

## Accessibility

- [ ] All interactive elements keyboard-navigable
- [ ] Focus states visible
- [ ] Color contrast ≥ 4.5:1 for body text
- [ ] All form fields have labels
- [ ] All images have alt text (decorative ones use `alt=""`)
- [ ] No autoplaying audio or video

## Security

- [ ] HTTPS forced (HTTP redirects to HTTPS)
- [ ] No mixed content warnings
- [ ] No exposed `.env`, `.git`, or admin paths
- [ ] All forms use HTTPS endpoints

## Final

- [ ] DNS pointed correctly, propagated globally
- [ ] WWW and apex both resolve to the same canonical
- [ ] 404 page exists and is styled
- [ ] Google Analytics 4 / GTM installed and firing
- [ ] Microsoft Clarity or Hotjar installed if requested
- [ ] Client has been walked through the GHL pipeline
- [ ] Backup of the codebase committed to Git
