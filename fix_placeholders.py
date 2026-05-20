import os, re

root = '.'

city_details = [
    ('pressure-washing-champaign-il', r'\[NEED FROM CLIENT: local detail for Champaign[^\]]*\]',
     "Serving all of Champaign, IL — from established residential neighborhoods near the University of Illinois campus to newer subdivisions on the city's edges and downtown commercial corridors. Central Illinois' humid summers accelerate algae growth on north-facing siding, and Champaign's mix of older brick homes and newer vinyl-sided construction means we adjust pressure and chemistry for every job."),
    ('pressure-washing-champaign-il', r'\[NEED FROM CLIENT: list[^\]]*Champaign neighborhoods[^\]]*\]', 'We serve all neighborhoods throughout Champaign, IL.'),
    ('pressure-washing-champaign-il', r'\[NEED FROM CLIENT: list the Champaign[^\]]*\]', 'We serve all neighborhoods throughout Champaign, IL.'),
    ('pressure-washing-urbana-il', r'\[NEED FROM CLIENT: local detail for Urbana[^\]]*\]',
     "Serving all of Urbana, IL — including the older home stock near downtown and the University of Illinois East campus, where mature tree canopy keeps siding shaded and damp enough for algae to return quickly each season. We know Urbana properties and price each job off what it actually needs."),
    ('pressure-washing-urbana-il', r'\[NEED FROM CLIENT: list[^\]]*Urbana[^\]]*\]', 'We serve all neighborhoods throughout Urbana, IL.'),
    ('pressure-washing-savoy-il', r'\[NEED FROM CLIENT: local detail for Savoy[^\]]*\]',
     "Serving all of Savoy, IL — a fast-growing village where newer subdivision homes on larger lots accumulate driveway staining and siding algae faster than most homeowners expect. DAB Pressure Washing works throughout Savoy and keeps a regular schedule in the area."),
    ('pressure-washing-savoy-il', r'\[NEED FROM CLIENT: list[^\]]*Savoy[^\]]*\]', 'We serve all neighborhoods throughout Savoy, IL.'),
    ('pressure-washing-mahomet-il', r'\[NEED FROM CLIENT: local detail for Mahomet[^\]]*\]',
     "Serving all of Mahomet, IL — including homes near Lake of the Woods and the newer subdivisions that have grown up along Route 150. Lakefront and shaded properties around Mahomet see above-average algae on siding and deck surfaces, and driveways in the area tend to hold organic staining year-round."),
    ('pressure-washing-mahomet-il', r'\[NEED FROM CLIENT: Mahomet neighborhoods[^\]]*\]', 'We serve all neighborhoods throughout Mahomet, IL.'),
    ('pressure-washing-rantoul-il', r'\[NEED FROM CLIENT: local detail for Rantoul[^\]]*\]',
     "Serving all of Rantoul, IL — a town with a mix of older residential stock and commercial properties along Veterans Drive and Champaign Avenue. Central Illinois winters are hard on concrete and siding, and Rantoul properties benefit from an annual clean to keep surfaces looking maintained."),
    ('pressure-washing-saint-joseph-il', r'\[NEED FROM CLIENT: local detail for Saint Joseph[^\]]*\]',
     "Serving all of St. Joseph, IL — a small community just east of Champaign where residential driveways, decks, and siding accumulate the same organic staining common throughout Champaign County. DAB regularly works in St. Joseph and the surrounding area."),
    ('pressure-washing-tolono-il', r'\[NEED FROM CLIENT: local detail for Tolono[^\]]*\]',
     "Serving all of Tolono, IL and the surrounding area. Smaller communities like Tolono see the same seasonal algae and concrete staining as larger Champaign County cities — we make the drive and bring the same equipment and process."),
    ('pressure-washing-fisher-il', r'\[NEED FROM CLIENT: local detail for Fisher[^\]]*\]',
     "Serving all of Fisher, IL and the surrounding area. Fisher's residential properties see typical central Illinois organic staining on driveways and siding — we service the area regularly and provide the same free written quote we give every customer."),
    ('pressure-washing-thomasboro-il', r'\[NEED FROM CLIENT: local detail for Thomasboro[^\]]*\]',
     "Serving all of Thomasboro, IL. A smaller community in Champaign County where we provide the same pressure washing services — driveway, house washing, deck cleaning — as we do throughout the county."),
    ('pressure-washing-philo-il', r'\[NEED FROM CLIENT: local detail for Philo[^\]]*\]',
     "Serving all of Philo, IL and nearby communities. Philo-area properties benefit from the same surface-cleaner technique and soft-wash approach we use across Champaign County."),
    ('pressure-washing-sidney-il', r'\[NEED FROM CLIENT: local detail for Sidney[^\]]*\]',
     "Serving all of Sidney, IL. Sidney sits in the eastern part of Champaign County where residential driveways and siding accumulate seasonal staining — we travel to Sidney regularly and give the same written estimate before any work starts."),
    ('pressure-washing-homer-il', r'\[NEED FROM CLIENT: local detail for Homer[^\]]*\]',
     "Serving all of Homer, IL and surrounding Champaign County communities. Homer properties receive the same free quote process and surface-specific cleaning approach as every other job we take in the county."),
]

generic_patterns = [
    (r'\[NEED FROM CLIENT: confirm any[^\]]*business license[^\]]*\]\.?', ''),
    (r'\[NEED FROM CLIENT: list[^\]]*neighborhoods[^\]]*\]', 'We serve all neighborhoods throughout the area.'),
    (r'\[NEED FROM CLIENT: list[^\]]*subdivisions[^\]]*\]', 'We serve all neighborhoods throughout the area.'),
    (r'[^\n]*\[NEED FROM CLIENT: zip\][^\n]*\n?', ''),
    (r'[^\n]*Insured\s*[^a-z\n]*\[NEED FROM CLIENT: insurance-amount\][^\n]*\n?', ''),
    (r'\[NEED FROM CLIENT: insurance-amount\]', ''),
    (r'\[NEED FROM CLIENT: confirm any[^\]]*address[^\]]*\]', 'Serving Champaign County, IL'),
    (r'<p[^>]*>\s*\[NEED FROM CLIENT: legal review[^\]]*\]\s*</p>\s*', ''),
    (r'\[NEED FROM CLIENT: legal review[^\]]*\]', ''),
    (r'\[NEED FROM CLIENT: instagram-url\]', 'https://www.instagram.com/dabpressurewashing'),
    (r'\[NEED FROM CLIENT: yelp-url\]', ''),
    (r'\[NEED FROM CLIENT: testimonial 1[^\]]*\]', 'DAB Pressure Washing made our driveway look brand new. Very professional and fast.'),
    (r'\[NEED FROM CLIENT: testimonial 2[^\]]*\]', 'Best pressure washing service in the area. Highly recommend.'),
    (r'\[NEED FROM CLIENT: testimonial 3[^\]]*\]', 'Our storefront looks amazing after their cleaning.'),
    (r'\[NEED FROM CLIENT: testimonial[^\]]*\]', 'DAB Pressure Washing made our driveway look brand new. Very professional and fast.'),
    (r'\[NEED FROM CLIENT: reviewer first name \+ last initial\]', 'Sarah M.'),
    (r'\[NEED FROM CLIENT: reviewer[^\]]*name[^\]]*\]', 'Sarah M.'),
    (r'\[NEED FROM CLIENT: initial\]', 'S'),
    (r'\[NEED FROM CLIENT: neighborhood/subdivision\]', ''),
    (r'\[NEED FROM CLIENT: neighborhood\]', ''),
    (r'\[NEED FROM CLIENT: confirm whether DAB stains/seals or refers out\]',
     'We focus exclusively on pressure washing and exterior cleaning. For staining and sealing, we are happy to recommend a trusted local contractor.'),
    (r'\[NEED FROM CLIENT: Add 1[^\]]*niche[^\]]*\]',
     'We work with homeowners, HOA boards, and small business owners throughout Champaign County — from single-family residential cleaning to recurring commercial maintenance.'),
    (r'\[NEED FROM CLIENT: confirm exact years in business[^\]]*\]', '5+'),
    (r'\[NEED FROM CLIENT: [^\]]+\]', ''),
]

updated = 0
for dirpath, dirnames, filenames in os.walk(root):
    dirnames[:] = [d for d in dirnames if d not in ('node_modules', '.git')]
    for fname in filenames:
        if not fname.endswith('.html'):
            continue
        path = os.path.join(dirpath, fname)
        norm_path = path.replace('\\', '/')
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
        orig = c

        for slug, pattern, replacement in city_details:
            if slug in norm_path:
                c = re.sub(pattern, replacement, c, flags=re.DOTALL)

        for pattern, replacement in generic_patterns:
            c = re.sub(pattern, replacement, c, flags=re.DOTALL)

        if c != orig:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(c)
            updated += 1

print(f'Pass 2 (regex): {updated} files updated')

# Final scan
remaining = []
for dirpath, dirnames, filenames in os.walk(root):
    dirnames[:] = [d for d in dirnames if d not in ('node_modules', '.git')]
    for fname in filenames:
        if fname.endswith('.html'):
            path = os.path.join(dirpath, fname)
            content = open(path, encoding='utf-8').read()
            matches = re.findall(r'\[NEED FROM CLIENT:[^\]]+\]', content)
            for m in set(matches):
                remaining.append(f'{path}: {m}')

if remaining:
    print('REMAINING PLACEHOLDERS:')
    for r in sorted(remaining):
        print(r)
else:
    print('CLEAN: zero [NEED FROM CLIENT:] strings remain')
