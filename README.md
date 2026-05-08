# Contractor Site Template — Pierson Digital Marketing

A fast, GHL-ready, SEO-optimized starter for contractor and home service websites.

**Stack:** HTML5 + Tailwind CSS (CLI build) + minimal vanilla JS. No frameworks. No CMS. Deploy anywhere.

---

## Quick start

```bash
npm install            # one time
npm run dev            # watch mode — rebuilds CSS as you edit HTML
# in another terminal:
npm run serve          # local server at http://localhost:3000

# When ready to ship:
npm run build          # minified production CSS
```

Open `index.html` in your browser to see the site.

---

## What's in here

```
.
├── CLAUDE.md                    # rules Claude Code follows when building sites
├── docs/
│   ├── snippets.md              # copy-paste schemas, GHL embeds, head boilerplate
│   └── launch-checklist.md      # pre-launch QA
├── src/input.css                # Tailwind source — edit theme tokens here
├── tailwind.config.js
├── package.json
├── index.html                   # home page template
├── contact.html
├── 404.html
├── services/
│   └── example-service/index.html
├── service-areas/
│   └── example-city/index.html
├── assets/
│   ├── css/styles.css           # compiled — don't edit by hand
│   ├── js/main.js               # tracking, smooth scroll, mobile menu
│   └── img/                     # drop client photos here as .webp
├── robots.txt
└── sitemap.xml
```

---

## Per-client setup checklist

1. **Theme tokens** — edit `src/input.css`, update the `:root` color variables. The accent color is the one you'll change most:
   ```css
   --color-accent: 217 119 6;   /* RGB triplet — amber default */
   ```
   Trade-by-trade suggestions:
   - Plumber: `30 110 200` (steady blue)
   - HVAC: `220 50 60` (warm red) or `30 110 200`
   - Roofer: `170 35 35` (deep red)
   - Electrician: `230 180 30` (amber-yellow)
   - Painter: client's actual brand color
   - Landscaper: `60 130 70` (forest green)

2. **Find/replace tokens** — every template file uses `{{TOKEN}}` placeholders. Hit them all:

   | Token | Example |
   |---|---|
   | `{{BUSINESS_NAME}}` | Acme Plumbing |
   | `{{DOMAIN}}` | acmeplumbing.com (no protocol, no trailing slash) |
   | `{{PHONE_DIGITS}}` | 5551234567 (digits only, used in `tel:` links) |
   | `{{FORMATTED_PHONE}}` | (555) 123-4567 |
   | `{{STREET}}` `{{CITY}}` `{{STATE}}` `{{STATE_CODE}}` `{{ZIP}}` | NAP for schema |
   | `{{LAT}}` `{{LNG}}` | Geo coords for LocalBusiness schema |
   | `{{LICENSE_NUMBER}}` | Trade license # |
   | `{{SCHEMA_TYPE}}` | `Plumber`, `HVACBusiness`, `RoofingContractor`, etc. |
   | `{{GHL_FORM_ID}}` | UUID from your GHL sub-account |
   | `{{YEAR_FOUNDED}}` `{{YEARS_IN_BUSINESS}}` `{{JOBS_COMPLETED}}` `{{RATING}}` `{{REVIEW_COUNT}}` | Trust numbers |

3. **Hero image** — drop a real job photo at `assets/img/hero.webp`. Convert with:
   ```bash
   cwebp -q 80 hero-original.jpg -o assets/img/hero.webp
   ```
   Same for any other photo. Always WebP. Always with explicit width/height in the HTML.

4. **GHL form embed** — replace `{{GHL_FORM_ID}}` everywhere it appears. The form ID is the UUID after `/widget/form/` in the GHL embed code.

5. **Schema** — pick the most specific type:
   - `Plumber`, `HVACBusiness`, `RoofingContractor`, `ElectricalBusiness`, `HousePainter`, `Locksmith`, `MovingCompany`, `PestControl`
   - Fall back to `LocalBusiness` only if there's no specific subtype.
   - Validate at https://search.google.com/test/rich-results

6. **Service pages** — duplicate `services/example-service/` per service. Update slug, all `{{TOKENS}}`, hero image, FAQ.

7. **City pages** — duplicate `service-areas/example-city/` per priority city. **Do not skip the unique local content.** Each page needs real references to neighborhoods, landmarks, or zip codes. 500+ unique words minimum.

8. **Sitemap** — add every indexable URL to `sitemap.xml` with current `<lastmod>`.

9. **Tracking** — uncomment GA4 block in `index.html` and replace `G-XXXXXXXXXX`. Add the GHL chat snippet before `</body>`.

10. **Run the launch checklist** at `docs/launch-checklist.md` before shipping.

---

## Design system at a glance

- **Display font:** Fraunces (serif with character)
- **Body font:** DM Sans (clean, distinctive)
- **Aesthetic:** Editorial confidence + trade professionalism
- **Color discipline:** Dark ink + warm cream + single accent
- **Hero pattern:** asymmetric, form-prominent, big confident type
- **Section transitions:** dark/light alternation for editorial rhythm
- **Trust signals:** big numbers in display font, italic accent for emphasis

The italic-accent pattern (`<em class="italic text-accent">`) is the design DNA — use it for the emphasized word in any section heading.

---

## Performance budget

| Metric | Target |
|---|---|
| Lighthouse mobile | ≥ 95 |
| LCP | < 2.5s |
| INP | < 200ms |
| CLS | < 0.1 |
| Page weight | < 500KB compressed |
| Total CSS | < 50KB minified ✓ (41KB current) |
| Total JS | < 5KB |

If you add a feature that breaks any of these, push back or restructure.

---

## Deploy

**Cloudflare Pages (recommended):**
1. Push to GitHub.
2. Cloudflare Pages → Connect → select repo.
3. Build command: `npm run build`. Output dir: `/`.
4. Done. Free SSL, free CDN, instant deploys.

**Netlify:** identical workflow. Use `netlify.toml` if needed.

**Important:** point DNS at the host *before* indexing. Keep `noindex` until DNS is live and you've smoke-tested.
