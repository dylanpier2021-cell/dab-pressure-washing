# Client Intake — DAB Pressure Washing

> Filled from public sources (their site description, Yelp listing, Google search). Anything I couldn't verify is marked `TBD` — Dylan/client must fill those in before build. Don't ship the site until every TBD is resolved or intentionally dropped.

**Companion docs in this folder:**
- `dab-kickoff-questionnaire.md` — every TBD as a clean question for the client. Send before kickoff.
- `dab-about-page-draft.md` — About page copy draft, owner-facts as `[OWNER]` inserts.
- `dab-privacy-policy-draft.md` — standard privacy policy ready for owner review.

---

## 1. Business basics

- **Business name (legal):** TBD — confirm with owner (likely "DAB Pressure Washing LLC" — verify with IL Secretary of State)
- **Business name (display, what shows on the site):** DAB Pressure Washing
- **Trade / category:** Pressure Washing / Exterior Cleaning
- **Schema type:** `LocalBusiness` (fallback — Schema.org has no pressure-washing-specific type; `LocalBusiness` is correct here)
- **Year founded:** TBD
- **Years in business:** TBD
- **Owner name(s):** Artem & Barak (last names TBD — get from owner)
- **One-sentence positioning:** Locally owned, pressure-washing-only specialists serving Champaign County — commercial-grade equipment, correct PSI for every surface, upfront pricing, no upsells.

---

## 2. Contact info (NAP — has to be 100% identical everywhere)

- **Phone (formatted):** TBD (not listed publicly in search snippets — pull from their site / Google Business Profile)
- **Phone (digits only, for tel: links):** TBD
- **Email:** TBD
- **Street address:** 203 Hessel Blvd *(per Yelp listing — confirm with owner; may be a residential / mailing address they don't want public-facing)*
- **City:** Champaign
- **State (full):** Illinois
- **State code:** IL
- **Zip:** TBD (Hessel Blvd Champaign is in 61820 — confirm)
- **Latitude / longitude:** ~40.1164, -88.2434 *(rough Champaign center — replace with exact for the listed address)*
- **Hours of operation:**
  - Mon–Fri: TBD
  - Saturday: TBD
  - Sunday: TBD
  - 24/7 emergency? N (pressure washing is not an emergency trade — recommend "By appointment, free quotes anytime")
- **License number(s) and type:** TBD — Illinois does not require a state-level pressure washing license, but confirm any local Champaign / Urbana business license. Do NOT invent one.
- **Insurance:** TBD — REQUIRED to confirm before publishing. At minimum get general liability amount. Bonded? Workers comp if they have W-2 employees?

---

## 3. Domain & hosting

- **Current website URL:** https://dabpressurewashing.com
- **New domain to use:** dabpressurewashing.com (already owned)
- **Domain registrar:** TBD — ask client
- **Going to host on:** TBD (recommend Cloudflare Pages — free tier, fast, easy DNS)
- **Email already set up?** TBD — check MX records before changing nameservers

---

## 4. Services — list ALL of them

> Confirmed from public site description: concrete cleaning, driveway cleaning, house washing (soft wash), deck & fence cleaning, commercial pressure washing. Drafted full service blocks below. **Pricing, "what's included" specifics, and FAQ answers must be reviewed and corrected by the owner before launch — these are educated drafts, not facts.**

### Service 1 — House Washing (Soft Wash)
- **Name (display):** House Washing
- **URL slug:** `house-washing`
- **One-sentence description:** Low-pressure soft wash that safely removes algae, mildew, dirt, and cobwebs from siding, soffits, gutters, and trim — without damaging paint, caulk, or landscaping.
- **Starting price:** TBD (typical Midwest range: $250–$450 for a single-story home — confirm with owner)
- **What's included (5–6 items):**
  1. Pre-treatment of organic growth (algae, mildew, mold) with surfactant solution
  2. Low-pressure rinse of all siding, soffits, fascia, and trim
  3. Window exterior rinse where included in the wash
  4. Plant and landscaping protection (pre-soak + post-rinse)
  5. Walk-around with homeowner before and after
  6. *(TBD — confirm anything else they bundle in, e.g. exterior light fixtures)*
- **Signs a customer needs this (4 items):**
  1. Green or black streaks on the north-facing side of the house
  2. Black "tiger stripes" running down gutters
  3. Cobwebs and dirt buildup around eaves and porch ceilings
  4. Mildew smell or visible spotting on siding
- **Common questions (3 minimum):**
  - Q: Will this damage my siding or paint?
  - A: No — we use a low-pressure soft-wash method specifically designed for residential siding. High-pressure washing can strip paint, force water behind siding, or damage caulk; we don't do that on house exteriors.
  - Q: Do I need to be home?
  - A: No, as long as outdoor water access is available. Most homeowners prefer to be there for the walk-around at the end.
  - Q: How often should I have my house washed?
  - A: Once a year is typical in central Illinois — humidity and tree cover make organic growth come back fairly quickly.

### Service 2 — Driveway & Concrete Cleaning
- **Name (display):** Driveway & Concrete Cleaning
- **URL slug:** `driveway-concrete-cleaning`
- **One-sentence description:** Surface-cleaner pressure washing that lifts oil stains, tire marks, algae, and ground-in dirt from driveways, sidewalks, garage floors, and patios — leaving concrete looking close to new.
- **Starting price:** TBD (typical Midwest range: $0.20–$0.45/sq ft — confirm)
- **What's included (5–6 items):**
  1. Pre-treatment for oil, rust, and organic stains where present
  2. Surface-cleaner pass for even, stripe-free results
  3. Edge and crack detail with a wand
  4. Final rinse and debris removal from adjacent grass / beds
  5. Optional post-treatment to slow algae regrowth (TBD if they offer)
- **Signs a customer needs this (4 items):**
  1. Black or green algae growth, especially near downspouts or shaded areas
  2. Oil and tire stains making the driveway look patchy
  3. Concrete looks dingy compared to a neighbor's
  4. Selling the home and want curb appeal before listing photos
- **Common questions (3 minimum):**
  - Q: Will it remove all oil stains?
  - A: Most. Fresh stains usually come fully out. Old, deeply soaked stains may lighten significantly but not vanish — we'll tell you up front during the quote.
  - Q: Will pressure washing damage the concrete?
  - A: Not when done correctly. We use a surface cleaner at appropriate pressure. Aggressive wand-only cleaning by an inexperienced operator can etch concrete — that's not how we work.
  - Q: How long does it take to dry?
  - A: A few hours in summer; longer if it's overcast. You can usually walk on it within an hour.

### Service 3 — Deck & Fence Cleaning
- **Name (display):** Deck & Fence Cleaning
- **URL slug:** `deck-fence-cleaning`
- **One-sentence description:** Soft-wash and controlled-pressure cleaning that strips graying, mildew, and algae from wood and composite decks, fences, and pergolas — prepping surfaces for stain or sealer if needed.
- **Starting price:** TBD
- **What's included (5–6 items):**
  1. Inspection for rot, loose boards, and protruding nails before cleaning
  2. Wood-safe cleaning solution applied and dwelled
  3. Low-to-medium pressure rinse with the right tip for the wood type
  4. Cleanup of debris around the deck/fence
  5. Recommendations on whether the surface is ready for stain/seal
- **Signs a customer needs this (4 items):**
  1. Wood looks gray or weathered instead of its original color
  2. Black or green spots on deck boards or fence pickets
  3. Slippery feeling underfoot (algae buildup)
  4. Planning to re-stain or seal — needs to be cleaned first
- **Common questions (3 minimum):**
  - Q: Can I stain right after?
  - A: Wood typically needs 24–72 hours of dry time before staining or sealing, depending on weather. We'll let you know.
  - Q: Will pressure washing damage soft wood?
  - A: It can if done wrong. We adjust pressure and tip selection for the wood — cedar and pine get treated differently than pressure-treated lumber.
  - Q: Do you stain or seal too?
  - A: TBD — confirm with owner whether they offer this or refer out.

### Service 4 — Commercial Pressure Washing
- **Name (display):** Commercial Pressure Washing
- **URL slug:** `commercial-pressure-washing`
- **One-sentence description:** Storefront, sidewalk, dumpster pad, drive-thru, and parking-lot cleaning for Champaign-County businesses — scheduled after hours when needed, with proof-of-insurance on file.
- **Starting price:** TBD (most commercial work is quoted custom)
- **What's included (5–6 items):**
  1. Site walk and written quote
  2. Storefront and sidewalk surface cleaning (gum removal as add-on TBD)
  3. Dumpster pad degreasing
  4. Drive-thru lane / order-window area cleaning
  5. Recurring service schedules available (monthly / quarterly)
  6. Certificate of Insurance provided to property manager on request
- **Signs a customer needs this (4 items):**
  1. Black mildew streaks down stucco or EIFS exterior
  2. Sticky / stained sidewalks at the front door (gum, drink spills, food traffic)
  3. Visible algae or mildew on north-facing walls
  4. Property manager flagging exterior cleanliness in walk-throughs
- **Common questions (3 minimum):**
  - Q: Can you work after hours?
  - A: Yes — many of our commercial clients schedule overnight or before opening to avoid disrupting customers.
  - Q: Do you have insurance?
  - A: Yes — we carry general liability and can send a Certificate of Insurance to your property manager before the first visit.
  - Q: Do you offer recurring service contracts?
  - A: Yes — most commercial clients book monthly or quarterly. We'll set a schedule and price that fits.

### Service 5 — Roof Soft Wash *(OPTIONAL — confirm if they offer)*
- Drop entirely if they don't do roofs. Listed because it's a common pressure-washing service and a high-margin add-on. **Do not publish without owner confirmation.**

### Service 6 — Gutter Cleaning / Brightening *(OPTIONAL — confirm if they offer)*
- Same note as above.

---

## 5. Service area

- **Primary city:** Champaign, IL
- **All cities served (priority order, top of list = build a city page first):**
  1. Champaign
  2. Urbana
  3. Savoy
  4. Mahomet
  5. Saint Joseph
  6. Tolono
  7. Monticello
  8. Rantoul
  9. *(also serve: Thomasboro, Fisher, Philo, Sidney, Homer — build pages later if budget allows)*
- **Travel radius from HQ:** ~30 miles from Champaign (covers all of Champaign County and edges of Piatt / Vermilion) — confirm with owner
- **Zip codes covered:** 61801, 61802, 61820, 61821, 61822, 61843, 61849, 61853, 61856, 61864, 61866, 61873, 61874, 61877, 61878, 61880 *(verify with owner — these are the standard ZIPs for the listed cities)*
- **Neighborhoods explicitly covered in the primary city:** TBD — ask owner for 4–6 Champaign neighborhoods they work in often (e.g. Old Town, Cherry Hills, Ironwood, Robeson Park, Trails at Brittany, etc.). This makes the local intro paragraph specific instead of generic.

### Per-city local context

#### City: Champaign
- **Population / size:** ~89,000 (2020 census)
- **Notable neighborhoods you serve there:** TBD — get 3–5 specific ones from owner
- **Common service issue specific to this city:** Tree-heavy older neighborhoods (Old Town, West Side) get heavy north-side algae on siding from shade and humidity; concrete driveways stain fast under mature oaks. *(Confirm angle with owner before publishing.)*
- **Local landmark or detail to mention:** University of Illinois campus, downtown Champaign, Market Place Mall — pick whichever feels right for tone
- **Permits or codes specific to this city:** TBD — generally none for residential pressure washing, but confirm
- **A real customer testimonial from this city (if available):** TBD

#### City: Urbana
- **Population / size:** ~38,000
- **Notable neighborhoods you serve there:** TBD
- **Common service issue specific to this city:** Older brick homes near downtown Urbana and the U of I campus zone get heavy mildew on north-facing brick and limestone walks. *(Confirm.)*
- **Local landmark or detail to mention:** University of Illinois, Crystal Lake Park, downtown Urbana
- **Permits or codes specific to this city:** TBD
- **A real customer testimonial from this city (if available):** TBD

#### City: Savoy
- **Population / size:** ~9,000
- **Notable neighborhoods you serve there:** TBD
- **Common service issue specific to this city:** Newer subdivisions with lots of vinyl siding — common candidates for annual soft wash.
- **Local landmark or detail to mention:** Willard Airport (CMI), proximity to U of I south campus
- **Permits or codes specific to this city:** TBD
- **A real customer testimonial from this city (if available):** TBD

#### City: Mahomet
- **Population / size:** ~9,400
- **Notable neighborhoods you serve there:** TBD (Lake of the Woods area is popular)
- **Common service issue specific to this city:** Lakefront homes near Lake of the Woods get heavy algae on decks, docks, and patios from humidity and tree cover.
- **Local landmark or detail to mention:** Lake of the Woods Forest Preserve, Mahomet-Seymour schools area
- **Permits or codes specific to this city:** TBD
- **A real customer testimonial from this city (if available):** TBD

#### City: Saint Joseph
- **Population / size:** ~4,000
- **Notable neighborhoods you serve there:** TBD
- **Common service issue specific to this city:** Rural-edge homes get more pollen and field dust on siding than in-town homes.
- **Local landmark or detail to mention:** Quick I-74 access east of Champaign
- **Permits or codes specific to this city:** TBD
- **A real customer testimonial from this city (if available):** TBD

> *(If budget allows, repeat for Tolono, Monticello, Rantoul.)*

---

## 6. Trust signals & numbers

- **Total jobs completed (lifetime estimate is fine):** TBD
- **Average Google rating:** TBD — pull from Google Business Profile
- **Google review count:** TBD
- **Google Business Profile URL:** TBD — get the share URL from their GBP dashboard
- **BBB rating (if any):** TBD (likely not listed — that's fine)
- **Industry certifications / awards:** TBD — ask about PWNA / UAMCC membership, manufacturer training, etc. Don't invent any.
- **Insurance amounts to brag about:** TBD — get exact GL coverage amount
- **Response time average:** TBD — ask owner; if they reply to leads in <2 hours, that's a great trust line

---

## 7. Reviews / testimonials (need at least 5)

> **DO NOT WRITE FAKE REVIEWS.** Pull these from Google / Yelp / Facebook with names already attached, OR have the owner reach out to 5 happy customers and ask for permission to use their name + city. Public site shows one snippet ("DAB Pressure Washing made our driveway look brand new. Very professional and fast.") — confirm whether that came from a real customer with attribution and permission before reusing.

### Review 1
- **Quote (verbatim, with permission):** TBD
- **Customer name:** TBD (First + Last initial only)
- **Their city/neighborhood:** TBD
- **Date:** TBD
- **Source:** TBD
- **Star rating:** TBD

### Review 2 — TBD
### Review 3 — TBD
### Review 4 — TBD
### Review 5 — TBD

---

## 8. Photos

> **Critical for pressure washing.** Before/after photos sell this trade harder than copy ever will. Get at least 5 strong before/afters from real DAB jobs. Stock photos will look obviously fake on a local site.

- [ ] Logo (transparent PNG, ideally vector SVG) — TBD
- [ ] Team photo (Artem + Barak, ideally with a branded vehicle) — TBD
- [ ] 3–5 in-progress job photos (techs working with a wand or surface cleaner, soaped-up siding, etc.) — TBD
- [ ] **At least 5 before/after pairs** — house washing, driveway, deck, fence, commercial — TBD
- [ ] Storefront / office exterior — likely N/A for a service-based business
- [ ] Hero image (640×800, vertical) — recommend a strong before/after of a Champaign-area driveway with the team in frame
- [ ] Photos for each service page (one per service ideal) — TBD
- [ ] OG/social image (1200×630) — TBD

**Where photos are stored:** TBD (set up a Google Drive folder and share with Dylan)

---

## 9. Brand & style

- **Brand colors (hex codes):**
  - Primary: TBD — confirm from existing logo
  - Accent (this becomes `--color-accent` in the site): TBD
- **Existing logo files location:** TBD
- **Vibe / tone they want:** Recommend **utility + friendly** — pressure washing buyers want competence and fair pricing, not luxury. Confirm with owner.
- **Sites they like the look of:** TBD — ask owner for 1–3
- **Sites they hate:** TBD

---

## 10. GoHighLevel setup

- **GHL sub-account name:** TBD (suggest: `DAB Pressure Washing` under Pierson Digital Marketing's agency account)
- **GHL form ID for quote requests:** TBD — create the quote form in GHL first, then paste the UUID from `/widget/form/UUID` here
- **GHL chat widget snippet:** TBD — paste the full `<script>` after creating the widget
- **GHL booking calendar ID (if using):** TBD — recommend setting up a "Free Quote Request" calendar
- **Lead destination:**
  - Phone: TBD (which owner gets the SMS)
  - Email: TBD

---

## 11. SEO targets

- **Primary keyword (the main one to rank for):** `pressure washing Champaign IL`
- **Secondary keywords (3–5):**
  1. `house washing Champaign IL`
  2. `driveway cleaning Champaign`
  3. `soft wash Champaign County`
  4. `commercial pressure washing Champaign`
  5. `deck cleaning Urbana IL`
- **Top 3 competitors and their URLs:**
  1. https://www.2prowash.com/ (Vermilion + Champaign Counties)
  2. https://midwestexteriorsoftwash.com/
  3. https://www.atlantic217.com/pressure-washing
  *(Plus regional aggregators: Thumbtack, Angi, Yelp, Porch — don't try to outrank them on brand pages, target local intent instead.)*
- **What makes this client genuinely better than those competitors?** TBD — ask owner. Likely angles based on their public messaging: pressure-washing-only specialists (not a side service), upfront pricing, locally owned, correct-PSI methodology. Confirm in their words.

---

## 12. Legal & compliance

- **Any specific claims they CAN'T legally make?** Avoid "guaranteed" / "100% removal" / "kills all mold" — these can trigger consumer-protection issues. Use "significantly improve," "lift," "treat," "safely clean."
- **Any disclaimers required by their license board?** None known — Illinois doesn't license pressure washing at the state level. Confirm any local Champaign / Urbana requirements.
- **Privacy policy needed?** **YES** — required because the GHL form collects name, email, phone. Generate a standard privacy policy template; have client review before publishing.
- **Existing privacy policy URL:** TBD (likely none — we're creating)

---

## 13. Content the client provided

- [ ] About page bio / origin story — TBD (need 2–3 paragraphs from Artem & Barak: how they started, what they care about, why pressure washing specifically)
- [ ] Existing copy from old site (if salvageable) — pull from current dabpressurewashing.com if helpful
- [ ] Brochures or printed marketing materials — TBD
- [ ] Press mentions / media coverage — TBD

**Where stored:** TBD

---

## 14. Goals & success metrics

- **What does "this site is working" look like in 90 days?** TBD — anchor target: 15–25 quote requests/month from organic + GBP, ranking top-3 in the local pack for "pressure washing Champaign" within 60–90 days. Confirm with owner what *they* would call a win.
- **Current monthly lead volume:** TBD
- **Goal monthly lead volume:** TBD
- **Best lead source today:** TBD (ask: word of mouth? Google? Facebook? Yelp? Knowing this matters before changing anything.)

---

## 15. Anything else weird or important

- Confirm the 203 Hessel Blvd address — if it's a residential address the owners don't want public, use a service-area-only schema setup (no street address shown publicly, just city + ZIP region). This is common and Google supports it for service-area businesses.
- Pressure washing is **seasonal** in central Illinois (April–October is peak; freezing winters basically halt work). The site should acknowledge this — recommend a "Book your spring slot" CTA Feb–March and a "Last calls before winter" angle in October. Maybe a winter waitlist form.
- Last names of owners: TBD — needed for About page and potentially for legal/business name accuracy.
- Confirm whether they have any employees or it's just the two owners — affects the team page and any "our team" copy.

---

## ✅ Pre-build checklist

Before opening Claude Code, confirm:

- [ ] All `TBD` info above is filled in (or marked dropped if intentionally not used)
- [x] At least 4 services with full details — **DONE (drafts; owner must review and correct pricing/specifics)**
- [ ] At least top 3 cities have local context filled in — **partial; need owner input on neighborhoods + specific local issues**
- [ ] At least 5 real reviews captured with permission
- [ ] Hero image + at least 1 photo per service in the Drive folder
- [ ] Brand colors decided (accent color especially)
- [ ] GHL form ID is in hand
- [ ] Domain pointed somewhere (or ready to be)

---

## Summary of what's still needed from the client (one-screen version)

**Must-haves before build:**
1. Phone number, email, confirmed address (or service-area-only setup)
2. Hours of operation
3. Owner last names + short origin-story paragraph
4. Confirmed list of services + starting prices for each (or "quote-based")
5. Insurance amount + any certifications/licenses they actually hold
6. 5 real customer reviews with names + cities + permission
7. Logo files + brand colors
8. Photos: at least 5 before/afters + a hero image
9. GHL form ID + chat widget snippet
10. Where leads go (phone/email)

**Nice-to-haves:**
- Champaign neighborhoods they work in often
- Specific service issue per city (Mahomet vs. Champaign vs. Urbana, etc.)
- One competitor they want to beat and why
- 90-day success target in their words
