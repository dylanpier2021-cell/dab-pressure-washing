# docs/snippets.md — Copy-Paste Reference

This file is the source of truth for boilerplate. Copy from here, swap the placeholders, do not invent variations.

---

## `<head>` boilerplate (every page)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>{{PAGE_TITLE}} | {{BUSINESS_NAME}}</title>
  <meta name="description" content="{{PAGE_DESCRIPTION_140_160_CHARS}}">
  <link rel="canonical" href="https://{{DOMAIN}}{{PATH}}">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="{{PAGE_TITLE}}">
  <meta property="og:description" content="{{PAGE_DESCRIPTION}}">
  <meta property="og:url" content="https://{{DOMAIN}}{{PATH}}">
  <meta property="og:image" content="https://{{DOMAIN}}/assets/img/og-image.jpg">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">

  <!-- Favicons -->
  <link rel="icon" href="/favicon.ico">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">

  <!-- Preload hero -->
  <link rel="preload" as="image" href="/assets/img/hero.webp" fetchpriority="high">

  <!-- Stylesheet -->
  <link rel="stylesheet" href="/assets/css/styles.css">
</head>
```

---

## LocalBusiness schema (home page + contact page)

Use the most specific subtype available (`Plumber`, `HVACBusiness`, `RoofingContractor`, `ElectricalBusiness`, `HousePainter`, `LocalBusiness` as fallback).

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Plumber",
  "@id": "https://{{DOMAIN}}/#business",
  "name": "{{BUSINESS_NAME}}",
  "image": "https://{{DOMAIN}}/assets/img/storefront.jpg",
  "logo": "https://{{DOMAIN}}/assets/img/logo.png",
  "url": "https://{{DOMAIN}}/",
  "telephone": "+1{{PHONE_DIGITS}}",
  "priceRange": "$$",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "{{STREET}}",
    "addressLocality": "{{CITY}}",
    "addressRegion": "{{STATE_CODE}}",
    "postalCode": "{{ZIP}}",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": {{LAT}},
    "longitude": {{LNG}}
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
      "opens": "08:00",
      "closes": "17:00"
    }
  ],
  "areaServed": [
    { "@type": "City", "name": "{{CITY_1}}" },
    { "@type": "City", "name": "{{CITY_2}}" }
  ],
  "sameAs": [
    "{{GOOGLE_BUSINESS_PROFILE_URL}}",
    "{{FACEBOOK_URL}}"
  ],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "{{RATING}}",
    "reviewCount": "{{REVIEW_COUNT}}"
  }
}
</script>
```

Only include `aggregateRating` if you have real review data. Never fabricate.

---

## Service schema (each service page)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "{{SERVICE_NAME}}",
  "provider": { "@id": "https://{{DOMAIN}}/#business" },
  "areaServed": [
    { "@type": "City", "name": "{{CITY_1}}" }
  ],
  "description": "{{1_2_SENTENCE_DESCRIPTION}}",
  "offers": {
    "@type": "Offer",
    "priceSpecification": {
      "@type": "PriceSpecification",
      "priceCurrency": "USD",
      "price": "{{STARTING_PRICE}}"
    }
  }
}
</script>
```

---

## FAQPage schema

Only include FAQs that are actually visible on the page.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "{{QUESTION}}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{{ANSWER}}"
      }
    }
  ]
}
</script>
```

---

## BreadcrumbList schema (inner pages)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://{{DOMAIN}}/" },
    { "@type": "ListItem", "position": 2, "name": "Services", "item": "https://{{DOMAIN}}/services/" },
    { "@type": "ListItem", "position": 3, "name": "{{SERVICE}}", "item": "https://{{DOMAIN}}/services/{{slug}}/" }
  ]
}
</script>
```

---

## GHL Form embed (inline)

```html
<iframe
  src="https://api.leadconnectorhq.com/widget/form/{{FORM_ID}}"
  style="width:100%;height:600px;border:none;border-radius:8px"
  id="inline-{{FORM_ID}}"
  data-layout='{"id":"INLINE"}'
  data-trigger-type="alwaysShow"
  data-form-id="{{FORM_ID}}"
  title="Quote Request Form"
  loading="lazy">
</iframe>
<script src="https://link.msgsndr.com/js/form_embed.js" defer></script>
```

If the form is above the fold, remove `loading="lazy"`.

---

## GHL Calendar embed

```html
<iframe
  src="https://api.leadconnectorhq.com/widget/booking/{{CALENDAR_ID}}"
  style="width:100%;border:none;overflow:hidden"
  scrolling="no"
  id="{{CALENDAR_ID}}"
  loading="lazy">
</iframe>
<script src="https://link.msgsndr.com/js/form_embed.js" defer></script>
```

---

## GHL Chat widget

Paste the snippet GHL gives you just before `</body>`. Always add `defer`.

---

## Click-to-call button (mobile-first)

```html
<a href="tel:+1{{PHONE_DIGITS}}"
   class="cta-call"
   aria-label="Call {{BUSINESS_NAME}} at {{FORMATTED_PHONE}}"
   data-track="phone-click">
  Call (555) 123-4567
</a>
```

Wire `data-track` to GA4 + GHL via a tiny vanilla JS listener in `main.js`.

---

## Google Map embed (city pages)

```html
<iframe
  src="https://www.google.com/maps?q={{ENCODED_ADDRESS}}&output=embed"
  width="100%" height="350"
  style="border:0;border-radius:8px"
  loading="lazy"
  referrerpolicy="no-referrer-when-downgrade"
  title="Service area map"></iframe>
```

---

## robots.txt

```
User-agent: *
Allow: /

Sitemap: https://{{DOMAIN}}/sitemap.xml
```

If the site is in dev/staging, change to:
```
User-agent: *
Disallow: /
```
…and add `<meta name="robots" content="noindex">` to every page until launch.

---

## sitemap.xml (generate at build time)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://{{DOMAIN}}/</loc>
    <lastmod>{{YYYY-MM-DD}}</lastmod>
    <priority>1.0</priority>
  </url>
  <!-- repeat for every indexable page -->
</urlset>
```

Exclude: `/thank-you/`, any utility pages, anything `noindex`.

---

## Tailwind production build (no CDN)

```bash
npx tailwindcss -i ./src/input.css -o ./assets/css/styles.css --minify
```

`tailwind.config.js` content array must include every HTML file path so unused classes get purged.
