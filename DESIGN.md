# DESIGN.md

> Dark luxury tax authority — gold and scarlett on black, every dollar earned and shown.

## 1. Visual Theme & Atmosphere

**Style**: Dark Editorial Luxury
**Keywords**: Authority, trust, premium, scarlett power, gold wealth, chrome precision, serious, results-driven
**Tone**: Commanding and professional — NOT casual, playful, or clinical
**Feel**: Like walking into a high-end financial firm in Manhattan — dark walls, gold accents, nothing wasted

**Interaction Tier**: L2 Fluid Interaction
**Dependencies**: CSS only + IntersectionObserver (no GSAP required)

## 2. Color Palette & Roles

```css
:root {
  /* Backgrounds */
  --bg: #080808;
  --surface: #0F0F0F;
  --surface-alt: #141414;
  --surface-hover: #1A1A1A;

  /* Borders */
  --border: rgba(201, 168, 76, 0.12);
  --border-hover: rgba(201, 168, 76, 0.35);
  --border-chrome: rgba(155, 170, 184, 0.15);

  /* Text */
  --text: #F2EDE4;
  --text-secondary: #A8A09A;
  --text-tertiary: #6B6560;

  /* Accent — Gold */
  --gold: #C9A84C;
  --gold-light: #E8C96A;
  --gold-dim: #9A7E3A;

  /* Accent — Scarlett */
  --scarlett: #B91C3A;
  --scarlett-light: #E0243F;

  /* Accent — Chrome */
  --chrome: #9BAAB8;
  --chrome-light: #BFC9D4;

  /* RGB variants for rgba() */
  --bg-rgb: 8, 8, 8;
  --gold-rgb: 201, 168, 76;
  --scarlett-rgb: 185, 28, 58;
  --chrome-rgb: 155, 170, 184;

  /* Semantic */
  --success: #3D9A6E;
  --error: #E53935;
  --warning: #F4A261;
}
```

**Color Rules:**
- All colors via CSS variables — zero hardcoded hex in components
- Gold = value, achievement, wealth (CTAs, stats, accents)
- Scarlett = urgency, action, power (primary buttons, tags, alerts)
- Chrome = precision, neutrality (borders, secondary UI, icons)
- Never use gold and scarlett on the same interactive element

## 3. Typography Rules

**Font Stack:**
```css
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Inter:wght@300;400;500;600;700&display=swap');
```

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Hero H1 | Cormorant Garamond | clamp(3.5rem, 7vw, 6.5rem) | 600 | 1.08 | -0.02em |
| Section H2 | Cormorant Garamond | clamp(2.2rem, 4vw, 3.25rem) | 600 | 1.12 | -0.02em |
| H3 / Card Title | Cormorant Garamond | 1.375–1.5rem | 600 | 1.25 | 0 |
| Body | Inter | 0.9375–1rem | 400 | 1.65–1.7 | 0 |
| Label / Eyebrow | Inter | 0.6875–0.75rem | 600 | 1 | 0.14–0.18em |
| Button | Inter | 0.8125rem | 600 | 1 | 0.06em |

**Typography Rules:**
- Cormorant Garamond for all display text — it carries the wealth/prestige signal
- Inter for all functional text — clean readability
- **NEVER use**: Arial, Helvetica alone, any system-ui for headings, Roboto, Open Sans

**Text Decoration:**
- Hero H1: Gold gradient on key word (`.text-gold`) — dark background + 72px+ qualifies
- Hero H1 shadow: `text-shadow: 0 0 60px rgba(201,168,76,0.15)` subtle glow on gold word
- Section H2: shimmer gradient animation on highlight spans only
- Body p: no decoration

## 4. Component Stylings

### Buttons
```css
/* Primary (Scarlett) */
.btn-primary {
  background: linear-gradient(135deg, var(--scarlett) 0%, #8B1127 100%);
  color: var(--text);
  border: 1px solid rgba(var(--scarlett-rgb), 0.4);
  box-shadow: 0 2px 12px rgba(var(--scarlett-rgb), 0.25), inset 0 1px 0 rgba(255,255,255,0.08);
  padding: 12px 28px; border-radius: 8px;
  font-size: 0.8125rem; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase;
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 24px rgba(var(--scarlett-rgb), 0.4);
}
.btn-primary:active { transform: scale(0.97); box-shadow: none; }
.btn-primary:focus-visible { outline: 2px solid var(--scarlett); outline-offset: 3px; }
.btn-primary:disabled { opacity: 0.5; cursor: not-allowed; transform: none; }

/* Gold CTA */
.btn-gold {
  background: linear-gradient(135deg, var(--gold) 0%, var(--gold-dim) 100%);
  color: #0A0808; border: 1px solid var(--gold);
  box-shadow: 0 2px 12px rgba(var(--gold-rgb), 0.2);
}
.btn-gold:hover { transform: translateY(-2px); box-shadow: 0 6px 24px rgba(var(--gold-rgb), 0.35); }
.btn-gold:active { transform: scale(0.97); }
.btn-gold:focus-visible { outline: 2px solid var(--gold); outline-offset: 3px; }
.btn-gold:disabled { opacity: 0.5; }

/* Ghost */
.btn-ghost {
  background: transparent; color: var(--text-secondary);
  border: 1px solid var(--border-chrome);
}
.btn-ghost:hover { color: var(--text); border-color: rgba(var(--chrome-rgb), 0.4); transform: translateY(-1px); }
.btn-ghost:focus-visible { outline: 2px solid var(--chrome); outline-offset: 3px; }
```

### Cards
```css
.spotlight-card {
  background: var(--surface);
  border-right: 1px solid var(--border);
  padding: 40px 36px;
  position: relative; overflow: hidden;
  transition: background 0.3s;
}
/* SpotlightCard: mouse-tracking radial glow via --mouse-x/--mouse-y CSS vars */
.spotlight-card::before {
  content: ''; position: absolute; inset: 0;
  background: radial-gradient(300px circle at var(--mouse-x,50%) var(--mouse-y,50%), rgba(var(--gold-rgb),0.07) 0%, transparent 70%);
  opacity: 0; transition: opacity 0.4s;
}
.spotlight-card:hover::before { opacity: 1; }
.spotlight-card:hover { background: var(--surface-hover); }
.spotlight-card:focus-visible { outline: 2px solid var(--gold); outline-offset: -2px; }

.bento-card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 16px; padding: 36px;
  transition: border-color 0.3s, box-shadow 0.3s;
}
.bento-card:hover { border-color: rgba(var(--gold-rgb), 0.25); box-shadow: 0 4px 24px rgba(0,0,0,0.3); }
```

### Navigation
```css
.nav {
  position: fixed; top: 0; width: 100%; height: 76px; z-index: 100;
  background: transparent; border-bottom: 1px solid transparent;
  transition: background 0.4s, border-color 0.4s, box-shadow 0.4s;
}
.nav.scrolled {
  background: rgba(var(--bg-rgb), 0.88);
  backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
  border-bottom-color: var(--border);
  box-shadow: 0 1px 20px rgba(0,0,0,0.4);
}
```

### Links
```css
.nav-links a {
  color: var(--text-secondary); position: relative;
  transition: color 0.2s;
}
.nav-links a::after {
  content: ''; position: absolute; bottom: -4px; left: 0;
  width: 0; height: 1px; background: var(--gold);
  transition: width 0.3s cubic-bezier(0.16,1,0.3,1);
}
.nav-links a:hover { color: var(--text); }
.nav-links a:hover::after { width: 100%; }
```

### Tags / Badges
```css
.service-tag {
  font-size: 0.6rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--scarlett); background: rgba(var(--scarlett-rgb), 0.1);
  border: 1px solid rgba(var(--scarlett-rgb), 0.2);
  border-radius: 4px; padding: 3px 8px;
}
```

### Form Inputs
```css
.form-input, .form-select, .form-textarea {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 8px; padding: 12px 16px;
  color: var(--text); transition: border-color 0.2s, box-shadow 0.2s;
}
.form-input:focus, .form-select:focus, .form-textarea:focus {
  border-color: rgba(var(--gold-rgb), 0.5);
  box-shadow: 0 0 0 3px rgba(var(--gold-rgb), 0.08);
  outline: none;
}
```

## 5. Layout Principles

**Container:**
- Max width: 1200px
- Padding: 0 24px
- Narrow variant (text-only): 720px

**Spacing Scale:**
- Section padding: 80–120px vertical
- Component gap: 48–56px
- Card internal padding: 36–40px
- Grid gap: 1px (seamless borders) or 12px (bento)

**Grid:**
```css
.services-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px; }
.bento-grid { display: grid; grid-template-columns: repeat(12, 1fr); gap: 12px; }
.stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 2px; }
.contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 80px; }
.process-steps { display: grid; grid-template-columns: repeat(3, 1fr); gap: 48px; }
```

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | No shadow | Cards at rest, sections |
| Subtle | `0 2px 12px rgba(0,0,0,0.3)` | Nav scrolled |
| Elevated | `0 6px 24px rgba(scarlett-rgb,0.4)` | CTA button hover |
| Gold Glow | `0 0 0 1px var(--gold), 0 0 20px rgba(gold-rgb,0.15)` | Active/featured states |
| Deep | `0 1px 20px rgba(0,0,0,0.4)` | Nav on scroll |

## 7. Animation & Interaction

**Motion Philosophy**: Authority through restraint — movement signals weight, not whimsy
**Tier**: L2

### Dependencies
No external JS libraries — CSS + native IntersectionObserver only.

### Entrance Animation
```css
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
@keyframes heroWordIn {
  from { opacity: 0; transform: translateY(100%); }
  to { opacity: 1; transform: translateY(0); }
}
.reveal {
  opacity: 0; transform: translateY(28px);
  transition: opacity 0.7s cubic-bezier(0.16,1,0.3,1), transform 0.7s cubic-bezier(0.16,1,0.3,1);
}
.reveal.in-view { opacity: 1; transform: translateY(0); }
.stagger-reveal > * { opacity: 0; transform: translateY(24px); transition: opacity 0.6s, transform 0.6s; }
.stagger-reveal.in-view > *:nth-child(n) { opacity: 1; transform: none; /* delay via nth-child */ }
```

### Scroll Behavior
```js
// IntersectionObserver for .reveal and .stagger-reveal
const obs = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in-view'); obs.unobserve(e.target); } });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal, .stagger-reveal').forEach(el => obs.observe(el));
```

### Hover & Focus States
```css
/* Nav scroll progress */
.scroll-progress { position: fixed; top: 0; left: 0; height: 2px; background: linear-gradient(90deg, var(--scarlett), var(--gold)); transform-origin: left; transform: scaleX(0); z-index: 1001; }
/* Card glow on hover */
.glow-card:hover { box-shadow: 0 0 0 1px var(--gold), 0 0 20px rgba(var(--gold-rgb), 0.15); }
/* Button press */
.btn:active { transform: scale(0.97); }
```

### Special Effects
- **Silk-style hero background**: CSS `radial-gradient` blobs animated via `@keyframes` — scarlett and gold orbs drifting on `#080808`
- **SpotlightCard**: `--mouse-x/--mouse-y` CSS vars updated via JS `mousemove`, drives `radial-gradient` on `::before`
- **Shimmer text**: `background-position` animation on gradient text (`background-size: 200%`)
- **CountUp**: RAF-based number animation triggered by IntersectionObserver
- **Marquee + Testimonials scroll**: pure CSS `translateX` keyframes, infinite loop
- **Magnetic buttons**: `mousemove` → `translate(x*0.25, y*0.25)` only on `(hover: hover)` devices
- **Cursor glow**: 500px radial-gradient div follows mouse via RAF (desktop only)

### Reduced Motion
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
  html { scroll-behavior: auto; }
  .reveal, .stagger-reveal > * { opacity: 1; transform: none; }
}
```

## 8. Do's and Don'ts

### Do
- Use Cormorant Garamond for all display headings — the serif carries prestige
- Keep gold for value/achievement moments (stats, CTAs, decorative highlights)
- Use scarlett for urgency and action (primary CTA, service tags, error states)
- Keep backgrounds near-black (#080808–#141414) — the dark field makes gold pop
- Use subtle 1px gold-tinted borders on all cards and containers
- Keep eyebrow labels uppercase, wide letter-spacing, in `var(--gold)`
- Ensure every section has clear visual rhythm: eyebrow → title → subtitle → content

### Don't
- ❌ Never use pure white (#FFFFFF) — use `var(--text)` (#F2EDE4) for all foreground text
- ❌ Never hardcode hex colors in component styles — only CSS variables
- ❌ Never put gold text on a gold or light background — only on near-black surfaces
- ❌ Never use `filter: blur()` on moving/animated elements — kills performance
- ❌ Never use more than 1 animated background effect per section
- ❌ Never use sans-serif fonts for headings — Cormorant is non-negotiable
- ❌ Never use more than 2 accent colors in a single component (pick gold OR scarlett)
- ❌ Never let `backdrop-filter: blur()` exceed 14px or cover large scroll areas
- ❌ Never use emoji as decorative elements — use inline SVG icons only
- ❌ Never break the dark theme with bright white sections — use `--surface-alt` (#141414) for alternating sections

## 9. Responsive Behavior

**Breakpoints:**
| Name | Width | Key Changes |
|------|-------|-------------|
| Desktop | > 1024px | Full 3-col services, 12-col bento, side-by-side contact |
| Tablet | 768–1024px | Bento collapses to 2-col, hero badge hidden |
| Mobile | < 768px | Single-col everything, hamburger nav, stacked CTAs |
| Small | < 480px | Reduced padding (16px), stats go single column |

**Touch Targets:** minimum 44×44px on all interactive elements
**Collapsing Strategy:** Grid → single column; nav links → hamburger drawer; side-by-side → stacked

```css
@media (max-width: 768px) {
  .services-grid { grid-template-columns: 1fr; }
  .stats-grid { grid-template-columns: repeat(2, 1fr); }
  .process-steps { grid-template-columns: 1fr; gap: 32px; }
  .contact-grid { grid-template-columns: 1fr; }
  .hero-actions { flex-direction: column; align-items: flex-start; }
  .bento-grid [class*="bento-span"] { grid-column: span 12; }
}
@media (max-width: 480px) {
  .container { padding: 0 16px; }
  .stats-grid { grid-template-columns: 1fr; }
}
```
