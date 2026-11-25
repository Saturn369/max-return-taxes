# Max Return Taxes — Website

Single-page marketing site for Max Return Taxes, a Hartford County, CT tax services firm serving clients across all 50 states.

## Stack

- Pure HTML/CSS/JS — no frameworks, no build step
- Fonts: Cormorant Garamond + Inter via Google Fonts
- Icons: inline SVG

## File Structure

```
max-return-taxes/
├── index.html      # Main site (single page)
├── og-image.jpg    # Social share preview (1200×630)
├── robots.txt      # Crawler policy + sitemap reference
├── sitemap.xml     # XML sitemap
└── README.md       # This file
```

## SEO Improvements Made

### Meta & Discoverability
- Added `<link rel="canonical">` to prevent duplicate-URL penalties
- Added full Open Graph tags (`og:title`, `og:description`, `og:image`, `og:url`, `og:type`, `og:site_name`, `og:locale`)
- Added Twitter Card tags (`summary_large_image`)
- Created `og-image.jpg` (1200×630) matching the site's dark gold aesthetic
- Created `robots.txt` with sitemap reference
- Created `sitemap.xml` with homepage URL, lastmod, and change frequency

### Structured Data (JSON-LD)
- `AccountingService` schema with name, phone, email, address, geo coordinates, hours, and area served
- `OfferCatalog` with three `Service` nodes (Business Tax Returns, Late Filings, Amendments)
- `AggregateRating` (5★, 4 reviews) + four individual `Review` nodes
- `sameAs` social profile links for Knowledge Graph entity disambiguation
- `WebPage` node linking the page to the business entity

### On-Page SEO
- Rewrote H1 from "Maximize Your Return." → "Maximize Your Business Tax Return." to include primary keyword
- Updated hero badge and marquee from "IRS Enrolled Agents" to "CT Licensed & Federally Authorized" (accurate)

### E-E-A-T (Experience, Expertise, Authoritativeness, Trust)
- Added "Licensed & Federally Authorized" bento card explaining CT + federal practitioner status
- Added "Lead Practitioner" bento card: **Joseph E. Smith**, CT Licensed Tax Practitioner, Federally Authorized
- Removed fabricated physical address — site correctly lists Hartford County, CT

## Before Going Live

- [ ] Replace `og-image.jpg` social links in JSON-LD `sameAs` with real profile URLs
- [ ] Submit sitemap at `https://saturn369.github.io/max-return-taxes/sitemap.xml` in Google Search Console
- [ ] Update `sitemap.xml` `<lastmod>` date on each publish
- [ ] Create a real `og-image.jpg` using your brand assets (or keep the generated one)
- [ ] Add Google Analytics or similar tracking
- [ ] Consider adding a blog for topical authority (business tax, late filings, amendments)

## Practitioner

**Joseph E. Smith**  
CT Licensed Tax Practitioner · Federally Authorized  
Hartford County, Connecticut · freedomenka@gmail.com · (860) 993-9904
