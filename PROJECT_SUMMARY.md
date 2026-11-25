# Max Return Taxes — Project Summary

**Date:** November 15, 2025
**Project:** Max Return Taxes Website
**Location:** `/home/dominique/max-return-taxes/`

---

## Business Details

| Field | Info |
|-------|------|
| Business Name | Max Return Taxes |
| Location | Hartford County, Connecticut |
| Service Area | All 50 States (fully remote-capable) |
| Specialties | Business Tax Returns, Late Filings, Amendments |
| Entity Types Served | S-Corps, C-Corps, LLCs, Partnerships, Sole Proprietors |
| Phone | (860) 993-9904 *(placeholder — update before launch)* |
| Email | freedomenka@gmail.com *(placeholder — update before launch)* |

---

## Design Decisions

### Color Scheme
| Color | Hex | Role |
|-------|-----|------|
| Black | `#080808` | Page background |
| Surface | `#0F0F0F` | Cards, containers |
| Scarlett | `#B91C3A` | Primary buttons, urgency, tags |
| Gold | `#C9A84C` | CTAs, stats, accents, wealth signal |
| Chrome | `#9BAAB8` | Borders, secondary UI, icons |
| Text | `#F2EDE4` | Warm white — never pure #FFF |

### Typography
- **Headings:** Cormorant Garamond (serif, 600–700) — prestige and authority
- **Body/UI:** Inter (sans, 400–600) — clean readability
- **Source:** Google Fonts

### Style Seed
Dark Editorial Luxury — closest match to seed #2 (Dark Tech) but with gold/scarlett replacing cyan/purple. Interaction tier: **L2 Fluid** (no GSAP — pure CSS + IntersectionObserver).

---

## Files Created

### `/home/dominique/max-return-taxes/DESIGN.md`
Full 9-chapter design specification:
1. Visual Theme & Atmosphere
2. Color Palette & Roles (all CSS variables)
3. Typography Rules
4. Component Stylings (buttons, cards, nav, links, forms — all states)
5. Layout Principles (grid, spacing, containers)
6. Depth & Elevation
7. Animation & Interaction
8. Do's and Don'ts (10 rules)
9. Responsive Behavior (Desktop / Tablet / Mobile / Small)

### `/home/dominique/max-return-taxes/index.html`
Complete single-file website. No build tools, no dependencies — open directly in a browser.

---

## Website Sections

| # | Section | Key Features |
|---|---------|-------------|
| 1 | **Nav** | Fixed, transparent → glass on scroll, hamburger mobile menu |
| 2 | **Hero** | Animated silk-style background (scarlett + gold blobs), word-by-word title entrance, Hartford County + 50 States eyebrow |
| 3 | **Marquee** | Infinite scrolling trust bar: Business Returns · Late Filings · Amendments · All 50 States · IRS Enrolled |
| 4 | **Stats** | Count-up animation: 1,000+ Returns · 50 States · 98% Satisfaction |
| 5 | **Services** | 3-card SpotlightCard grid (mouse-tracking radial glow): Business Returns, Late Filings, Amendments |
| 6 | **Why Us** | Bento grid with GlareHover sweep: Nationwide, Every Deduction Reviewed, Business Specialists, No Judgment, Fast Turnaround |
| 7 | **Process** | 3-step with connecting gold/scarlett line: Share Docs → We Prepare → Review & File |
| 8 | **Testimonials** | Auto-scrolling carousel (pauses on hover), 4 client stories from TX, FL, CA, NY |
| 9 | **CTA Banner** | "Stop Leaving Money on the Table" with scarlett radial glow |
| 10 | **Contact** | Split layout: contact info (location, phone, email, hours) + lead form (name, email, phone, state dropdown all 50, service selector, message) |
| 11 | **Footer** | 4-column: brand + tagline + socials, Services links, Company links, Contact info |

---

## Animations & Interactions

| Effect | Implementation | Where Used |
|--------|---------------|------------|
| Silk background | CSS `radial-gradient` blobs + `@keyframes` | Hero |
| Word entrance | CSS `@keyframes wordIn` staggered per word | Hero H1 |
| SpotlightCard | `--mx/--my` CSS vars via JS `mousemove` → `radial-gradient` | Services cards |
| GlareHover | CSS `translateX` sweep on `::before` | Bento cards |
| Scroll reveal | `IntersectionObserver` → `.in-view` class | All sections |
| Stagger reveal | nth-child transition delays on `.stagger` containers | Stats, services, bento, process |
| Count-up | RAF eased counter triggered by IntersectionObserver | Stats numbers |
| Marquee | Pure CSS `translateX` keyframes | Trust bar |
| Testimonial scroll | Pure CSS `translateX` keyframes, pauses on hover | Reviews |
| Scroll progress bar | `scaleX` from 0→1 based on scroll position | Top of page (gold→scarlett) |
| Nav glass | `backdrop-filter: blur(12px)` on `.scrolled` class | Navigation |
| Magnetic buttons | `mousemove` → `translate(x*0.28, y*0.28)` on `(hover:hover)` only | All `.magnetic` CTAs |
| Cursor glow | 500px radial-gradient div follows mouse via RAF | Desktop only |
| Rotating badge | CSS `conic-gradient` border + `@keyframes` rotation | Hero |
| Gold shimmer text | `background-position` animation on gradient clip-text | Section headlines |

---

## Things to Update Before Launch

- [ ] Replace placeholder phone `(860) 993-9904` with real number
- [ ] Replace placeholder email `freedomenka@gmail.com` with real email
- [ ] Update social media links (Facebook, Instagram, LinkedIn) in footer
- [ ] Connect contact form to a backend / form service (Formspree, Netlify Forms, etc.)
- [x] Stat numbers confirmed by owner 2026-11-25 (1,000+ returns, 98% satisfaction)
- [ ] Add real Google reviews / testimonials with actual client names (with permission)
- [ ] Add a favicon (`<link rel="icon">` in `<head>`)
- [ ] Consider adding a privacy policy and terms page links in the footer
- [ ] Add Google Analytics or similar tracking
- [ ] Test on real mobile devices before going live

---

## Credits

- Motion effects derived from [vue-bits](https://github.com/DavidHDev/vue-bits) by DavidHDev (MIT)
- Fonts: [Cormorant Garamond](https://fonts.google.com/specimen/Cormorant+Garamond) + [Inter](https://fonts.google.com/specimen/Inter) via Google Fonts
- Icons: Heroicons (inline SVG, MIT)
