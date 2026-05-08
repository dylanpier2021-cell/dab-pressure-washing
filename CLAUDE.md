# CLAUDE.md — Contractor & Home Service Website Builder

You are building marketing websites for contractors and home service businesses (HVAC, plumbing, roofing, landscaping, painting, electrical, pest control, garage doors, etc.) sold through **Pierson Digital Marketing LLC**.

Every site you build must hit four bars, in this order:
1. **Fast** — Lighthouse mobile ≥ 95, all Core Web Vitals green
2. **Convert** — GoHighLevel (GHL) is the only lead destination
3. **Rank** — Local SEO foundation done right on day one
4. **Safe for index** — Zero practices that risk a Google penalty

If any decision conflicts with one of these, ask before proceeding.

---

## Tech Stack (default)

- **HTML5 + Tailwind CSS** (compiled via CLI for production, never the CDN script)
- **Vanilla JS only** — no jQuery, no React, no Next.js, no WordPress
- **Astro** is acceptable if a multi-page content system is needed (city/blog pages)
- **Hosting**: Cloudflare Pages (preferred) or Netlify
- **DNS**: Cloudflare for CDN + free SSL
- All forms, calendars, chat, and tracking → **GHL**

Do not introduce a framework, CMS, or build tool that wasn't already in the project unless the user asks.

---

## File Structure

```
site/
├── index.html
├── about.html
├── contact.html
├── 404.html
├── robots.txt
├── sitemap.xml
├── services/
│   └── [service-slug]/index.html
├── service-areas/
│   └── [city-slug]/index.html
├── blog/                       (only if requested)
└── assets/
    ├── css/styles.css          (compiled Tailwind, minified)
    ├── js/main.js              (< 5KB)
    └── img/                    (WebP/AVIF only, originals in img/src/)
```

URLs are lowercase, hyphenated, trailing slash on directories. Never use `.html` in internal links if the host serves clean URLs.

---

## Performance — non-negotiable

- LCP < 2.5s, INP < 200ms, CLS < 0.1
- Total page weight < 500KB compressed
- Hero image: `loading="eager"`, `fetchpriority="high"`, `<link rel="preload">` in head
- All other images: `loading="lazy"`, explicit `width` and `height`, WebP or AVIF
- Below-the-fold iframes (GHL forms, maps, YouTube): `loading="lazy"`
- YouTube: use a facade pattern or `lite-youtube-embed`, never raw iframe above the fold
- Inline critical CSS for above-the-fold; load full stylesheet async
- All third-party scripts: `defer` or `async`, never blocking
- Fonts: prefer system stack. If using a web font, self-host, `font-display: swap`, preload one weight only
- No render-blocking resources in `<head>` except the critical CSS

Run `npx @lhci/cli autorun` or Lighthouse before declaring a page done.

---

## SEO Foundation — every page

- One `<h1>` per page, then logical `h2`/`h3`
- Unique `<title>` 50–60 chars
- Unique meta description 140–160 chars
- `<link rel="canonical">` on every page
- Open Graph + Twitter card tags
- `<meta name="viewport" content="width=device-width, initial-scale=1">`
- `<html lang="en">`
- Schema (see `docs/snippets.md`):
  - `LocalBusiness` on home + contact
  - `Service` on each service page
  - `FAQPage` wherever FAQs appear
  - `BreadcrumbList` on inner pages
- `robots.txt` allows crawl + points to sitemap
- `sitemap.xml` lists every indexable page with `lastmod`
- Internal linking: every page reachable in ≤ 3 clicks from home
- External links: `rel="noopener"`, `target="_blank"` only when leaving site
- All images: descriptive `alt` (not keyword-stuffed, not "image")

---

## Safe for Index — never do these

- Keyword stuffing in copy, alt text, or meta tags
- Duplicate content across city/service pages — each must have **500+ unique words** with specific local references (neighborhoods, landmarks, zip codes)
- Doorway pages (thin city pages with only a name swap)
- Hidden text, white-on-white, `display:none` for SEO
- Cloaking (different content for bots vs users)
- AI-generated content that reads as templated — vary sentence structure, add specifics
- Mass-generating 50+ city pages on day one — start with the priority cities and expand
- Lorem Ipsum, placeholder testimonials, or fake reviews in delivered pages
- Stock photos that scream stock — use real job photos when available
- More than one `<h1>` per page
- Linking out to spammy or unrelated sites
- Intrusive mobile interstitials (full-screen popups on load)

---

## GoHighLevel Integration

Every site connects to a GHL sub-account. Before building any lead-capture surface, ask the user for:
- GHL Form ID
- GHL Calendar ID
- GHL Chat Widget snippet
- GHL tracking number (for click-to-call)
- Sub-account location ID (if needed for API)

**Never build native HTML forms that POST to a PHP endpoint or `mailto:`.** All leads go through GHL embeds. See `docs/snippets.md` for embed patterns.

Phone numbers everywhere should be the GHL tracking number, formatted as `tel:+1XXXXXXXXXX`. Display format: `(555) 123-4567`.

---

## City + Service Pages (the local SEO play)

The money pages are `service × city` combinations. Build them carefully:

1. Start with **5–10 priority cities × top 3 services**, not the full matrix
2. Each city page needs:
   - Unique 3–5 sentence intro mentioning real neighborhoods, landmarks, or zip codes
   - Service-specific FAQ (3–5 questions minimum)
   - Embedded Google Map iframe of the service area (lazy-loaded)
   - Unique title + meta description with city + service
   - At least one local-specific paragraph (climate, common issues in that area, local regs)
3. Link all city pages from a `/service-areas/` hub
4. Link all service pages from the main nav
5. Cross-link related services within service pages

If the user asks for "100 city pages," push back and recommend a phased rollout.

---

## Content Guidelines

- Headlines: benefit-focused, not keyword-stuffed
- Show pricing or "starting at" ranges where possible (trust + SEO win)
- Trust signals on home: license #, insurance, years in business, jobs completed, Google rating, BBB
- Real testimonials with first name + last initial + city, or clearly labeled placeholders during build
- Specific service descriptions, not "we do everything"
- Every page has one clear primary CTA (call or quote form) repeated 2–3 times

---

## Reference Docs

When you need details, pull from:
- `docs/snippets.md` — copy-paste schema, GHL embeds, robots.txt, sitemap, head boilerplate
- `docs/launch-checklist.md` — pre-launch QA checklist

---

## Workflow for a New Site

1. Confirm intake: business name, NAP, services, service area, GHL IDs, brand colors, logo, photos
2. Scaffold file structure
3. Build **home page first** — get layout/design approved before continuing
4. Build services pages
5. Build about + contact
6. Build city pages (phased)
7. Run Lighthouse on every template
8. Validate every schema block in Google's Rich Results Test
9. Generate `sitemap.xml` and `robots.txt` last
10. Walk the launch checklist before handoff

---

## Things to Ask Before Generating

If any of these are missing, ask first:
- GHL Form ID and Calendar ID
- Business NAP (name, address, phone) — exact format must match Google Business Profile
- Primary service vs upsells
- Photo library availability
- Brand colors and fonts (or permission to choose)
- Service area cities, in priority order
- Competitors to study for positioning

## Never

- Ship Lorem Ipsum
- Ship without alt text on every image
- Ship a page without unique title + meta description
- Add tracking scripts to `<head>` without `defer`
- Build a contact form that isn't GHL
- Use `<h1>` more than once per page
- Skip the `viewport` meta tag
- Mass-duplicate content across geo pages
