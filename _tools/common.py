"""Shared building blocks for the generated pages (service pages, blog, privacy).

`pre` is the relative path back to the site root: "" for the homepage, "../" one level down, "../../" two.
"""
import html, re

SITE = "https://saturn369.github.io/max-return-taxes"
PHONE_TEL, PHONE = "+18609939904", "(860) 993-9904"
EMAIL = "freedomenka@gmail.com"
WEB3FORMS_KEY = "2ea0597a-db8d-4862-8478-9f10b581dc0f"  # public by design; only delivers to EMAIL
FONTS_URL = "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Inter:wght@400;500;600;700&display=swap"
FAVICON = ("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 64 64%27%3E%3Crect width=%2764%27 height=%2764%27 rx=%2712%27 fill=%27%23080808%27/%3E"
           "%3Ctext x=%2732%27 y=%2746%27 font-family=%27Georgia,serif%27 font-size=%2740%27 font-weight=%27700%27 text-anchor=%27middle%27 fill=%27%23C9A84C%27%3EM%3C/text%3E%3C/svg%3E")

# Service pages: slug -> label (order = footer/related order)
SERVICES = {"business-tax-returns": "Business Tax Returns", "late-tax-returns": "Late &amp; Unfiled Returns",
            "amended-tax-returns": "Amended Returns", "connecticut-tax-preparer": "Hartford County, CT"}
SERVICE_OPTIONS = ["Business Tax Return", "Late Filing (1+ years behind)", "Amendment / Correction",
                   "Individual Tax Return", "Multiple Services"]
STATES = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
          "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts",
          "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
          "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island",
          "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
          "Wisconsin", "Wyoming"]

ARROW = '<svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>'
SEND = '<svg width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M6 12L3.269 3.126A59.768 59.768 0 0121.485 12 59.77 59.77 0 013.269 20.876L5.999 12zm0 0h7.5"/></svg>'
ICON = {
    "loc": '<path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z"/>',
    "phone": '<path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z"/>',
    "mail": '<path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75"/>',
    "clock": '<path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"/>',
}

def strip(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()

def fonts_head():
    return ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            f'  <link href="{FONTS_URL}" rel="stylesheet">')

def nav(pre):
    links = [("Services", f"{pre}#services"), ("Why Us", f"{pre}#why"), ("Process", f"{pre}#process"), ("Blog", f"{pre}blog/"), ("Contact", f"{pre}#contact")]
    li = "".join(f'<li><a href="{h}">{t}</a></li>' for t, h in links)
    return f'''<nav class="nav" id="nav">
    <div class="container nav-inner">
      <a href="{pre or './'}" class="logo">Max Return<span class="logo-sep"></span><span class="logo-accent">Taxes</span></a>
      <ul class="nav-links" id="navLinks">{li}</ul>
      <div class="nav-cta">
        <a href="tel:{PHONE_TEL}" class="btn btn-ghost">Call Now</a>
        <a href="{pre}#contact" class="btn btn-primary">Get Started</a>
      </div>
      <button class="hamburger" id="hbg" aria-label="Open menu" aria-expanded="false" aria-controls="navLinks"><span></span><span></span><span></span></button>
    </div>
  </nav>'''

def footer(pre):
    svc = "".join(f'<li><a href="{pre}{s}/">{t}</a></li>' for s, t in SERVICES.items())
    return f'''<footer class="footer">
    <div class="container">
      <div class="footer-top">
        <div>
          <a href="{pre or './'}" class="logo">Max Return<span class="logo-sep"></span><span class="logo-accent">Taxes</span></a>
          <p class="footer-tagline">Hartford County's premier tax specialists — serving every client across all 50 states with expertise and integrity.</p>
        </div>
        <div>
          <div class="f-col-ttl">Services</div>
          <ul class="f-links">{svc}</ul>
        </div>
        <div>
          <div class="f-col-ttl">Company</div>
          <ul class="f-links"><li><a href="{pre}#why">About Us</a></li><li><a href="{pre}#process">How It Works</a></li><li><a href="{pre}blog/">Blog</a></li><li><a href="{pre}#contact">Contact</a></li></ul>
        </div>
        <div>
          <div class="f-col-ttl">Contact</div>
          <ul class="f-links" style="gap:14px">
            <li style="color:var(--text-secondary);font-size:.875rem">Hartford County, CT</li>
            <li style="color:var(--text-secondary);font-size:.875rem">All 50 States Served</li>
            <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <div class="f-copy">© 2026 Max Return Taxes · Hartford County, CT · All rights reserved. · <a href="{pre}privacy/">Privacy Policy</a></div>
        <div class="f-credit">Motion effects derived from <a href="https://github.com/DavidHDev/vue-bits" target="_blank" rel="noopener">vue-bits</a> by DavidHDev (MIT)</div>
      </div>
    </div>
  </footer>'''

def _ci(icon, label, val):
    return (f'<div class="ci"><div class="ci-icon"><svg width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">{ICON[icon]}</svg></div>'
            f'<div><div class="ci-label">{label}</div><div class="ci-val">{val}</div></div></div>')

def contact_form(page, default_service="", id_prefix="c"):
    """Lead form handled by assets/site.js (Web3Forms). `page` is reported in the email and in analytics."""
    st = "".join(f"<option>{s}</option>" for s in STATES)
    sv = "".join(f'<option{" selected" if o == default_service else ""}>{o}</option>' for o in SERVICE_OPTIONS)
    i = id_prefix
    return f'''<form class="contact-form" action="https://api.web3forms.com/submit" method="POST" data-page="{html.escape(page, quote=True)}">
          <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
          <input type="hidden" name="subject" value="New inquiry — {html.escape(page, quote=True)}">
          <input type="hidden" name="from_name" value="Max Return Taxes Website">
          <input type="hidden" name="page" value="{html.escape(page, quote=True)}">
          <input type="checkbox" name="botcheck" style="display:none" tabindex="-1" autocomplete="off">
          <div class="form-row">
            <div class="fg"><label class="flabel" for="{i}fn">First Name</label><input class="fi" type="text" id="{i}fn" name="first_name" autocomplete="given-name" required></div>
            <div class="fg"><label class="flabel" for="{i}ln">Last Name</label><input class="fi" type="text" id="{i}ln" name="last_name" autocomplete="family-name" required></div>
          </div>
          <div class="fg"><label class="flabel" for="{i}em">Email Address</label><input class="fi" type="email" id="{i}em" name="email" autocomplete="email" required></div>
          <div class="form-row">
            <div class="fg"><label class="flabel" for="{i}ph">Phone</label><input class="fi" type="tel" id="{i}ph" name="phone" autocomplete="tel"></div>
            <div class="fg"><label class="flabel" for="{i}st">Your State</label><select class="fs" id="{i}st" name="state"><option value="">Select state...</option>{st}</select></div>
          </div>
          <div class="fg"><label class="flabel" for="{i}sv">Service Needed</label><select class="fs" id="{i}sv" name="service"><option value="">Select a service...</option>{sv}</select></div>
          <div class="fg"><label class="flabel" for="{i}msg">Tell Us More</label><textarea class="fta" id="{i}msg" name="message" placeholder="Briefly describe your tax situation..."></textarea></div>
          <button type="submit" class="btn btn-primary btn-lg" style="justify-content:center">Send Message {SEND}</button>
          <p class="form-note">We reply within 24 hours. See our <a href="PRIVACY_HREF">privacy policy</a>.</p>
        </form>'''

def contact_section(pre, page, title, sub, default_service=""):
    info = (_ci("phone", "Phone", f'<a href="tel:{PHONE_TEL}" style="color:inherit">{PHONE}</a>')
            + _ci("mail", "Email", f'<a href="mailto:{EMAIL}" style="color:inherit">{EMAIL}</a>')
            + _ci("clock", "Hours", 'Mon–Fri: 9am–7pm ET<br><span class="ci-sub">Sat: 10am–4pm · Extended during tax season</span>')
            + _ci("loc", "Location", 'Hartford County, Connecticut<br><span class="ci-sub">Serving All 50 States</span>'))
    form = contact_form(page, default_service).replace("PRIVACY_HREF", f"{pre}privacy/")
    return f'''<section class="contact-section" id="contact">
    <div class="container">
      <div class="section-eye">Free Consultation</div>
      <h2 class="section-title">{title}</h2>
      <div class="contact-grid" style="margin-top:40px">
        <div>
          <p class="contact-lead">{sub}</p>
          <div class="contact-info">{info}</div>
        </div>
        {form}
      </div>
    </div>
  </section>'''
