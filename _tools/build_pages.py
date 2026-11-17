"""Generate Max Return Taxes service pages. Usage: python -I build_pages.py <repo_dir>"""
import json, re, sys, pathlib, html

ROOT = pathlib.Path(sys.argv[1])
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from common import SITE, PHONE_TEL, PHONE, EMAIL, FAVICON, ARROW, SERVICES, strip, fonts_head, nav, footer, contact_section
CHECK = '<svg width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>'

PAGES = {}  # slug -> dict

def cards(items, cls=""):
    out = []
    for c in items:
        tag = f'<span class="svc-tag">{c["tag"]}</span>' if c.get("tag") else ""
        out.append(f'<div class="bc {c.get("cls","")}">{tag}<h3 class="bc-title">{c["t"]}</h3><p class="bc-body">{c["b"]}</p></div>')
    return f'<div class="card-grid {cls}">' + "".join(out) + "</div>"

def checklist(items):
    return '<ul class="checklist">' + "".join(f"<li>{CHECK}<span>{i}</span></li>" for i in items) + "</ul>"

def table(head, rows, note=""):
    th = "".join(f"<th>{h}</th>" for h in head)
    tr = "".join("<tr>" + "".join(f'<td data-label="{strip(h)}">{c}</td>' for h, c in zip(head, r)) + "</tr>" for r in rows)
    n = f'<p class="table-note">{note}</p>' if note else ""
    return f'<div class="table-wrap"><table class="dl-table"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>{n}'

def steps(items):
    return '<div class="process-grid">' + "".join(
        f'<div class="p-step"><div class="p-num">0{i}</div><h3 class="p-title">{t}</h3><p class="p-body">{b}</p></div>'
        for i, (t, b) in enumerate(items, 1)) + "</div>"

def section(eye, title, sub, body, alt=False, id_=None):
    s = f'<p class="section-sub">{sub}</p>' if sub else ""
    i = f' id="{id_}"' if id_ else ""
    return (f'<section class="page-section{" page-section-alt" if alt else ""}"{i}><div class="container">'
            f'<div class="section-eye">{eye}</div><h2 class="section-title">{title}</h2>{s}{body}</div></section>')

def faq_html(faqs):
    return '<div class="faq-list">' + "".join(
        f'<details class="faq"><summary>{q}</summary><div class="faq-a">{a}</div></details>' for q, a in faqs) + "</div>"

SERVICE_LINKS = list(SERVICES.items())
DEFAULT_SERVICE = {"business-tax-returns": "Business Tax Return", "late-tax-returns": "Late Filing (1+ years behind)", "amended-tax-returns": "Amendment / Correction"}

def related(slug):
    items = [(s, t) for s, t in SERVICE_LINKS if s != slug]
    links = "".join(f'<a class="related-link" href="../{s}/"><span>{t}</span>{ARROW}</a>' for s, t in items)
    return f'<section class="page-section page-section-alt"><div class="container"><div class="section-eye">More Services</div><div class="related-grid">{links}</div></div></section>'

def page(slug, p):
    url = f"{SITE}/{slug}/"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "@id": url + "#service", "name": p["service_name"], "serviceType": p["service_name"],
         "description": p["desc"], "url": url, "areaServed": {"@type": "Country", "name": "United States"},
         "provider": {"@id": f"{SITE}/#business"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": strip(p["crumb"]), "item": url}]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in p["faqs"]]},
    ]}
    title = html.escape(p["title"], quote=True); desc = html.escape(p["desc"], quote=True)
    body = "\n  ".join(p["sections"])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="icon" href="{FAVICON}">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{SITE}/og-image.jpg">
  <meta property="og:site_name" content="Max Return Taxes">
  <meta property="og:locale" content="en_US">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{SITE}/og-image.jpg">
  {fonts_head()}
  <link rel="stylesheet" href="../assets/site.css">
  <script type="application/ld+json">
{json.dumps(ld, indent=2, ensure_ascii=False)}
  </script>
</head>
<body>
  <div class="scroll-progress" id="sp"></div>
  {nav("../")}

  <header class="page-hero">
    <div class="hero-bg"></div><div class="hero-grid"></div><div class="hero-vignette"></div>
    <div class="container page-hero-content">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="../">Home</a><span aria-hidden="true">/</span><span>{p["crumb"]}</span></nav>
      <div class="hero-eyebrow">{p["eyebrow"]}</div>
      <h1 class="page-title">{p["h1"]}</h1>
      <p class="page-sub">{p["sub"]}</p>
      <div class="page-actions">
        <a href="../#contact" class="btn btn-primary btn-lg">{p["cta_btn"]}</a>
        <a href="tel:{PHONE_TEL}" class="btn btn-ghost btn-lg">Call {PHONE}</a>
      </div>
    </div>
  </header>

  <main>
  {body}
  {section("Questions", "Frequently Asked Questions", "", faq_html(p["faqs"]), id_="faq")}
  {related(slug)}
  {contact_section("../", strip(p["crumb"]) + " page", p["cta_title"], p["cta_sub"], DEFAULT_SERVICE.get(slug, ""))}
  </main>

  {footer("../")}
  <script src="../assets/site.js" defer></script>
</body>
</html>
'''

# ---------------------------------------------------------------- CONTENT
PAGES["business-tax-returns"] = dict(
    title="Business Tax Return Preparation — S-Corp, LLC & Partnership | Max Return Taxes",
    desc="Business tax preparation for S-Corps, C-Corps, partnerships, LLCs and sole proprietors. Based in Hartford County, CT and serving business owners in all 50 states.",
    service_name="Business Tax Return Preparation", crumb="Business Tax Returns",
    eyebrow="Core Specialty · All 50 States",
    h1='Business Tax Returns, <span class="text-gold">Prepared Right.</span>',
    sub="S-Corps, C-Corps, partnerships, LLCs and sole proprietors — federal and state returns prepared accurately, filed on time, with every legitimate deduction claimed.",
    cta_btn="Get a Free Consultation",
    cta_title="Let's Get Your Business Return Done Right",
    cta_sub="Tell us about your business and what you need filed. We'll reply within 24 hours with next steps.",
    sections=[
        section("Who We Serve", "Every Business Structure", "Business returns are our core work, not a side service. Here's what we prepare:",
            cards([
                dict(tag="Form 1120-S", t="S Corporations", b="The 1120-S and a Schedule K-1 for every shareholder. We review owner compensation for reasonableness, track shareholder basis, and catch the errors that flow through to your personal return."),
                dict(tag="Form 1065", t="Partnerships &amp; Multi-Member LLCs", b="The 1065 with partner K-1s, capital account and basis reporting, guaranteed payments, and the allocation details partnerships get wrong most often."),
                dict(tag="Form 1120", t="C Corporations", b="Corporate returns, estimated tax planning, and the state corporate returns that go with them — including Connecticut's CT-1120."),
                dict(tag="Schedule C", t="Sole Proprietors &amp; Single-Member LLCs", b="Schedule C with your 1040, self-employment tax, home office, vehicle and equipment deductions, and a plan for next year's quarterly estimates."),
            ])),
        section("Deadlines", "Business Tax Deadlines", "For calendar-year businesses. Missing these triggers penalties — for S-Corps and partnerships, even when no tax is owed.",
            table(["Return", "Business type", "Due date", "Extended deadline"], [
                ["Form 1120-S", "S Corporation", "March 15", "September 15 (Form 7004)"],
                ["Form 1065", "Partnership / multi-member LLC", "March 15", "September 15 (Form 7004)"],
                ["Form 1120", "C Corporation", "April 15", "October 15 (Form 7004)"],
                ["Schedule C (Form 1040)", "Sole proprietor / single-member LLC", "April 15", "October 15 (Form 4868)"],
            ], "An extension gives you more time to <em>file</em>, not more time to <em>pay</em> — tax owed is still due by the original deadline. When a deadline falls on a weekend or holiday, it moves to the next business day."), alt=True),
        section("Maximize Your Return", "Deductions We Make Sure You Don't Miss", "Small businesses leave money on the table every year. We look for every one of these that applies to you:",
            '<div class="two-col">' + checklist([
                "Home office deduction for space used regularly and exclusively for business",
                "Vehicle expenses — standard mileage or actual costs, whichever is better",
                "Equipment and property depreciation, including Section 179 expensing",
                "Self-employed health insurance premiums",
                "Retirement contributions — SEP-IRA, Solo 401(k) and SIMPLE plans",
            ]) + checklist([
                "The qualified business income (QBI) deduction for pass-through owners",
                "Startup and organizational costs for new businesses",
                "Business use of your phone, internet and software",
                "Professional fees, insurance, and business interest",
                "Connecticut's elective pass-through entity tax, where it helps",
            ]) + "</div>"),
        section("Getting Started", "What to Have Ready", "Don't have everything? Send what you have — we'll tell you exactly what's missing.",
            '<div class="two-col">' + checklist([
                "Last year's business and personal tax returns",
                "Profit &amp; loss statement and balance sheet (a QuickBooks or Xero export works)",
                "Bank and credit card statements for the year",
                "1099-NEC, 1099-K and 1099-MISC forms you received",
            ]) + checklist([
                "Payroll reports — W-2s, W-3 and quarterly Form 941s",
                "Records of equipment, vehicles or property bought or sold",
                "Loan statements and any changes in ownership",
                "Estimated tax payments made during the year",
            ]) + "</div>", alt=True),
        section("How It Works", "Three Steps to a Filed Return", "",
            steps([
                ("Share Your Records", "Upload your documents securely or send them over — from anywhere in the country. We'll review and follow up on anything missing."),
                ("We Prepare &amp; Optimize", "We build your federal and state returns, check them against prior years, and find every legitimate deduction and credit."),
                ("Review &amp; File", "We walk you through the finished return and answer your questions. Once you approve, we e-file and confirm acceptance."),
            ])),
    ],
    faqs=[
        ("When is my S-Corp tax return due?", "For calendar-year S-Corps, Form 1120-S is due March 15. Filing Form 7004 extends the deadline six months, to September 15. A late S-Corp return is penalized per shareholder, per month — even if the business owes no tax."),
        ("Can you prepare my state return if my business isn't in Connecticut?", "Yes. We prepare your federal return along with the state returns for every state where your business is required to file."),
        ("My bookkeeping is behind. Can you still help?", "Yes. Send what you have — bank statements, receipts, any reports from your accounting software — and we'll tell you what's missing and how to get your records in shape to file."),
        ("Should my LLC elect to be taxed as an S-Corp?", "It depends on your profit, what a reasonable salary for your role would be, and your state. For some owners it lowers self-employment tax; for others the added payroll costs outweigh the savings. We can run the numbers for your situation."),
        ("Do I have to meet with you in person?", "No. Most clients work with us entirely remotely — documents are exchanged securely online and we talk by phone or video."),
    ])

PAGES["late-tax-returns"] = dict(
    title="Late & Unfiled Tax Returns Help — Get Current With the IRS | Max Return Taxes",
    desc="Behind on your taxes? We prepare past-due individual and business returns, help limit IRS penalties, and get you back in good standing. No judgment. Serving all 50 states.",
    service_name="Late and Unfiled Tax Return Preparation", crumb="Late &amp; Unfiled Returns",
    eyebrow="No Judgment · All 50 States",
    h1='Behind on Your Taxes? <span class="text-gold">Let\'s Get You Current.</span>',
    sub="Whether it's one missed year or several, we prepare your past-due returns, work out what you actually owe — or are owed — and get you back in good standing with the IRS.",
    cta_btn="Get Back on Track",
    cta_title="The Hardest Part Is Making the Call",
    cta_sub="Tell us how many years you're behind. We'll reply within 24 hours with a plan — no lectures, no judgment.",
    sections=[
        section("Why Act Now", "Waiting Makes It More Expensive", "Unfiled returns don't go away on their own. Here's what happens while they sit:",
            cards([
                dict(cls="bc-scarlett", t="Penalties keep growing", b="The failure-to-file penalty is 5% of the unpaid tax for each month a return is late, up to 25%. A separate failure-to-pay penalty and interest also build up. Filing — even if you can't pay yet — stops the larger penalty from growing."),
                dict(cls="bc-gold", t="Refunds expire", b="If you were owed a refund, you generally have three years from the original due date to claim it. After that, the money is gone for good."),
                dict(t="The IRS can file for you", b="The IRS can prepare a \"substitute for return\" using the income reported to it — without your deductions, credits, or business expenses. That usually means a much bigger bill than if you had filed yourself."),
                dict(t="Business returns are penalized even with no tax due", b="Late S-Corp and partnership returns are penalized per owner, per month — even when the business owes nothing."),
            ])),
        section("How We Help", "How We Get You Current", "",
            steps([
                ("Find Out Where You Stand", "With your authorization, we pull your IRS wage and income transcripts — so missing W-2s and 1099s aren't a problem — and see which years are open."),
                ("Prepare Every Missing Year", "We prepare each past-due federal and state return, claiming the deductions and credits a substitute return would leave out."),
                ("File &amp; Make a Plan", "We file the returns and, if there's a balance, walk you through your options — IRS payment plans and whether you may qualify for penalty relief."),
            ]), alt=True),
        section("Good to Know", "How Far Back Do You Need to Go?", "",
            '<div class="prose"><p>The IRS generally expects the <strong>last six years</strong> of returns to be filed for you to be considered in good standing. That\'s often the place to start — though every situation is different, and we\'ll look at what makes sense for yours.</p>'
            '<p>If you have a balance you can\'t pay all at once, the IRS offers <strong>payment plans</strong>. And if you have a clean history, you may qualify for <strong>First-Time Abatement</strong>, which can remove certain penalties for a single tax year. We\'ll tell you which options apply to you.</p>'
            '<p>State returns matter too. Connecticut and most other states charge their own late-filing penalties and interest, so we prepare your state returns for the same years.</p></div>'),
        section("Who We Help", "Common Situations We Handle", "",
            '<div class="two-col">' + checklist([
                "One or more years of unfiled personal returns",
                "Business returns that fell behind — S-Corp, partnership or Schedule C",
                "Missing or lost W-2s, 1099s and other records",
            ]) + checklist([
                "IRS notices about returns you haven't filed",
                "A substitute return the IRS prepared for you",
                "Self-employed income with no estimated payments made",
            ]) + "</div>", alt=True),
    ],
    faqs=[
        ("I can't afford to pay what I owe. Should I still file?", "Yes. The failure-to-file penalty is ten times larger per month than the failure-to-pay penalty, so filing on its own cuts how fast your balance grows. The IRS offers payment plans for balances you can't pay right away."),
        ("How many years of back taxes do I need to file?", "The IRS generally looks for the last six years to be filed for you to be in good standing. We'll review your transcripts and recommend what makes sense for your situation."),
        ("I lost my W-2s and 1099s. Can you still file my returns?", "Usually, yes. With your authorization we can get your IRS wage and income transcripts, which show the income reported to the IRS for each year."),
        ("Can IRS penalties be removed?", "Sometimes. First-Time Abatement can remove certain penalties for one tax year if you have a clean compliance history. Penalties can also be reduced for reasonable cause, such as a serious illness. We'll tell you whether you may qualify."),
        ("Do I need to file my state returns too?", "Usually. Connecticut and most other states have their own filing requirements, penalties and interest. We prepare the state returns alongside your federal returns."),
    ])

PAGES["amended-tax-returns"] = dict(
    title="Amended Tax Returns — Fix Errors & Claim Missed Refunds | Max Return Taxes",
    desc="Missed a deduction or had a return filed wrong? We review prior-year returns and file amendments for individuals and businesses to correct mistakes and recover refunds.",
    service_name="Amended Tax Return Preparation", crumb="Amended Returns",
    eyebrow="Fix &amp; Recover · All 50 States",
    h1='Fix a Past Return. <span class="text-gold">Recover What You\'re Owed.</span>',
    sub="Missed a deduction, received a corrected 1099, or had a return prepared wrong? We review prior-year returns and file amendments to correct the record and claim refunds you're entitled to.",
    cta_btn="Have Us Review a Return",
    cta_title="Think a Past Return Was Wrong?",
    cta_sub="Send us the return and tell us what you're worried about. We'll reply within 24 hours and let you know if an amendment makes sense.",
    sections=[
        section("When to Amend", "Common Reasons to Amend a Return", "If any of these apply to you, it may be worth a second look:",
            cards([
                dict(cls="bc-gold", t="Missed deductions or credits", b="Business expenses, education credits, retirement contributions, or other deductions you qualified for but didn't claim."),
                dict(t="Corrected tax forms", b="A corrected W-2, 1099 or K-1 that arrived after you filed — common with brokerage statements and partnership K-1s."),
                dict(t="Wrong filing status or dependents", b="Filing status or dependents that should have been claimed differently, changing your tax or your credits."),
                dict(t="Business return errors", b="Mistakes on an S-Corp or partnership return that flowed through to the owners' personal returns."),
                dict(cls="bc-scarlett", t="Income that was left off", b="Correcting unreported income yourself — before the IRS finds it — generally means less in penalties and interest."),
                dict(t="A preparer's mistake", b="Errors made by a previous preparer. We review the full return, not just the line in question."),
            ])),
        section("Time Limits", "Don't Wait Too Long", "",
            '<div class="prose"><p>To claim a refund, you generally must file an amended return within <strong>three years</strong> of the date you filed the original return, or within <strong>two years</strong> of the date you paid the tax — whichever is later. A return filed before the April deadline is treated as filed on the deadline.</p>'
            '<p>After that window closes, the refund is lost even if you were entitled to it. That\'s why it pays to review recent returns sooner rather than later.</p>'
            '<p>Not every mistake needs an amendment. The IRS fixes simple math errors on its own and will usually write to you if a form was missing. We\'ll tell you when an amendment is actually worth filing.</p></div>', alt=True),
        section("What Gets Filed", "How Amendments Work", "Different returns are corrected in different ways. We handle each one:",
            table(["Return", "How it's corrected"], [
                ["Individual (Form 1040)", "Form 1040-X, with the changed schedules"],
                ["S Corporation (Form 1120-S)", "An amended 1120-S, with corrected K-1s for shareholders"],
                ["C Corporation (Form 1120)", "Form 1120-X"],
                ["Partnership (Form 1065)", "Usually an Administrative Adjustment Request, with corrected K-1 information for partners"],
                ["Connecticut (Form CT-1040)", "Form CT-1040X, when a change affects your Connecticut tax"],
            ], "The IRS says amended returns usually take 8 to 12 weeks to process, and sometimes up to 16. You can track the status with the IRS's \"Where's My Amended Return?\" tool.")),
        section("How It Works", "From Review to Refund", "",
            steps([
                ("Send Us the Return", "Share the return you want reviewed, plus any new or corrected forms. Tell us what you think went wrong."),
                ("We Review &amp; Calculate", "We go through the full return, confirm what needs to change, and show you the effect on your refund or balance before anything is filed."),
                ("We File the Amendment", "Once you approve, we file the federal amendment and any state amendments that go with it."),
            ]), alt=True),
    ],
    faqs=[
        ("How far back can I amend a tax return?", "To claim a refund, you generally have three years from when you filed the original return, or two years from when you paid the tax, whichever is later."),
        ("Will filing an amended return trigger an audit?", "Amending a return doesn't by itself mean you'll be audited. Amended returns are routine, and an accurate amendment with supporting documents is the right way to correct a mistake."),
        ("What if I owe more tax after amending?", "Then it's best to file and pay as soon as possible. Interest runs from the original due date, so correcting it sooner keeps the cost down."),
        ("Do I need to amend my state return too?", "Usually. If a federal change affects your state tax, most states — including Connecticut — expect you to file a state amendment as well. We prepare both."),
        ("My previous preparer made the mistake. Can you still fix it?", "Yes. We'll review the whole return, correct what's wrong, and make sure the same issue isn't repeated in the years since."),
    ])

TOWNS = ["Hartford", "West Hartford", "East Hartford", "Manchester", "New Britain", "Bristol", "Glastonbury", "Wethersfield",
         "Newington", "Farmington", "Southington", "Enfield", "Windsor", "Bloomfield", "Simsbury", "Avon", "Rocky Hill", "Berlin"]

PAGES["connecticut-tax-preparer"] = dict(
    title="Hartford County, CT Tax Preparer — Business & Individual Returns | Max Return Taxes",
    desc="Hartford County, Connecticut tax preparation for business owners and individuals. Federal and Connecticut returns, late filings and amendments — with clients in all 50 states.",
    service_name="Tax Preparation in Hartford County, Connecticut", crumb="Hartford County, CT",
    eyebrow="Hartford County, Connecticut",
    h1='Your Hartford County <span class="text-gold">Tax Preparer.</span>',
    sub="Local Connecticut expertise with nationwide reach. We prepare federal and Connecticut returns for business owners and individuals across Hartford County — and for clients in every state.",
    cta_btn="Get a Free Consultation",
    cta_title="Connecticut Taxes, Handled",
    cta_sub="Tell us what you need filed. We'll reply within 24 hours — whether you're in Hartford or anywhere else in the country.",
    sections=[
        section("What We Do", "Tax Services for Connecticut", "",
            cards([
                dict(tag="Core Specialty", t="Business Tax Returns", b='S-Corps, partnerships, LLCs, C-Corps and sole proprietors — federal returns and Connecticut returns like the CT-1120. <a class="inline-link" href="../business-tax-returns/">Business returns →</a>'),
                dict(tag="Don't Wait", t="Late &amp; Unfiled Returns", b='Behind on federal or Connecticut returns? We prepare the missing years and help limit penalties. <a class="inline-link" href="../late-tax-returns/">Late filings →</a>'),
                dict(tag="Fix &amp; Recover", t="Amended Returns", b='Correct a prior federal or Connecticut return and claim refunds you missed. <a class="inline-link" href="../amended-tax-returns/">Amendments →</a>'),
            ])),
        section("Connecticut Know-How", "Connecticut Taxes We Handle", "Connecticut has rules of its own. These come up often for our clients:",
            '<div class="two-col">' + checklist([
                "<strong>CT-1040</strong> resident income tax returns",
                "<strong>CT-1040NR/PY</strong> for part-year residents and people who moved in or out of state",
                "<strong>CT-1040X</strong> amended Connecticut returns",
            ]) + checklist([
                "<strong>CT-1120</strong> corporation business tax returns",
                "Connecticut's <strong>elective pass-through entity tax</strong> for S-Corps and partnerships — and whether electing it helps you",
                "Multi-state returns for Connecticut businesses with customers or owners in other states",
            ]) + "</div>", alt=True),
        section("Service Area", "Serving All of Hartford County", "We work with clients throughout Hartford County, including:",
            '<ul class="town-list">' + "".join(f"<li>{t}</li>" for t in TOWNS) + '</ul>'
            '<p class="table-note">Not in Hartford County? We work with clients in all 50 states — documents are exchanged securely online and we meet by phone or video.</p>'),
        section("How It Works", "Simple, From Start to Finish", "",
            steps([
                ("Reach Out", "Send a message or call. Tell us what you need filed and for which years."),
                ("Share Your Documents", "Upload your documents securely. We'll let you know if anything is missing."),
                ("Review &amp; File", "We walk you through your finished returns, then e-file once you approve."),
            ]), alt=True),
    ],
    faqs=[
        ("Do you only work with Connecticut clients?", "No. We're based in Hartford County, but we work with clients in all 50 states and prepare returns for whichever states you need to file in."),
        ("I moved into or out of Connecticut this year. What do I file?", "Part-year residents generally file Form CT-1040NR/PY, which splits your income between the time you lived in Connecticut and the time you didn't. You may also need a return in the other state."),
        ("Should my business elect Connecticut's pass-through entity tax?", "Connecticut's pass-through entity tax is elective. For some S-Corp and partnership owners, paying state tax at the business level produces federal tax savings; for others it doesn't. We can look at the numbers for your business."),
        ("Can we meet in person?", "Most of our clients work with us remotely — by phone, video and secure document upload — which is often the fastest way to get your return done."),
        ("What does it cost?", "It depends on the type of return and how many years are involved. Reach out for a free consultation and we'll give you a quote."),
    ])

# ---------------------------------------------------------------- WRITE
for slug, p in PAGES.items():
    d = ROOT / slug; d.mkdir(exist_ok=True)
    (d / "index.html").write_text(page(slug, p), encoding="utf-8")
print("pages:", ", ".join(PAGES))

# ---------------------------------------------------------------- PRIVACY POLICY
PRIVACY_UPDATED = "November 17, 2026"
PRIVACY_BODY = f'''
<p>This policy explains what information Max Return Taxes collects through this website, how we use it, and the choices you have. Questions? Email <a href="mailto:{EMAIL}">{EMAIL}</a> or call <a href="tel:{PHONE_TEL}">{PHONE}</a>.</p>

<h2>Information you give us</h2>
<p>When you use a contact form on this site, we collect what you enter: your name, email address, phone number, state, the service you're interested in and your message. We also receive whatever you share with us directly by email or phone.</p>
<p>If you become a client, we collect the tax documents and information needed to prepare your returns. That information is handled separately from this website.</p>
<p><strong>Please don't send Social Security numbers, tax documents or bank details through the website form.</strong> Once we're working together, we'll give you a secure way to share them.</p>

<h2>How contact form submissions are delivered</h2>
<p>Our contact forms are processed by <a href="https://web3forms.com/privacy" rel="noopener" target="_blank">Web3Forms</a>, a form delivery service that sends your message to our email inbox. Web3Forms handles the data only to deliver it to us.</p>

<h2>How we use your information</h2>
<ul>
<li>To respond to your inquiry and give you a quote</li>
<li>To provide tax preparation and related services if you become a client</li>
<li>To meet our legal and professional obligations</li>
</ul>
<p>We do <strong>not</strong> sell your personal information, and we don't share it with advertisers.</p>

<h2>Tax return information</h2>
<p>As tax return preparers, we're subject to federal rules that restrict how we use and disclose tax return information. We don't use or disclose your tax return information for any purpose other than preparing your returns without your consent, except as the law permits or requires.</p>

<h2>Website analytics</h2>
<p>We use <a href="https://www.goatcounter.com/help/privacy" rel="noopener" target="_blank">GoatCounter</a>, a privacy-friendly analytics service, to count page views and clicks on our phone number, email and contact form. GoatCounter doesn't use cookies, doesn't track you across other websites, and doesn't identify individual visitors. We see only totals, like how many people viewed a page, which site they came from, and their general browser, device type and country.</p>

<h2>Other services this site uses</h2>
<ul>
<li><strong>Hosting:</strong> this site is hosted on GitHub Pages, which may log technical information such as IP addresses for security and operations. See <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener" target="_blank">GitHub's privacy statement</a>.</li>
<li><strong>Fonts:</strong> our fonts are loaded from Google Fonts, so your browser connects to Google's servers. See <a href="https://policies.google.com/privacy" rel="noopener" target="_blank">Google's privacy policy</a>.</li>
</ul>

<h2>How long we keep information</h2>
<p>We keep inquiries for as long as needed to respond and follow up, and client records for as long as required by law and professional standards.</p>

<h2>Your choices</h2>
<p>You can ask us what information we have about you, ask us to correct it, or ask us to delete your inquiry, subject to any records we're legally required to keep. Just email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2>Security</h2>
<p>We take reasonable steps to protect the information you give us. No method of sending information over the internet is completely secure, which is why we ask you not to send sensitive tax documents through the website form.</p>

<h2>Children</h2>
<p>This website isn't directed at children under 13, and we don't knowingly collect their information through it.</p>

<h2>Changes to this policy</h2>
<p>If we change this policy, we'll update the date below.</p>
<p class="article-disclaimer">Last updated: {PRIVACY_UPDATED}</p>
'''

def simple_page(slug, title, desc, crumb, h1, sub, body):
    url = f"{SITE}/{slug}/"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title, "isPartOf": {"@id": f"{SITE}/#webpage"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": crumb, "item": url}]}]}
    t = html.escape(title, quote=True); d = html.escape(desc, quote=True)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{t}</title>
  <meta name="description" content="{d}">
  <link rel="icon" href="{FAVICON}">
  <link rel="canonical" href="{url}">
  {fonts_head()}
  <link rel="stylesheet" href="../assets/site.css">
  <script type="application/ld+json">
{json.dumps(ld, indent=2, ensure_ascii=False)}
  </script>
</head>
<body>
  <div class="scroll-progress" id="sp"></div>
  {nav("../")}
  <header class="page-hero article-hero">
    <div class="hero-bg"></div><div class="hero-grid"></div><div class="hero-vignette"></div>
    <div class="container page-hero-content">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="../">Home</a><span aria-hidden="true">/</span><span>{crumb}</span></nav>
      <h1 class="page-title article-title">{h1}</h1>
      <p class="page-sub">{sub}</p>
    </div>
  </header>
  <main>
    <section class="page-section"><div class="container"><article class="article-body">{body}</article></div></section>
  </main>
  {footer("../")}
  <script src="../assets/site.js" defer></script>
</body>
</html>
'''

(ROOT / "privacy").mkdir(exist_ok=True)
(ROOT / "privacy" / "index.html").write_text(simple_page(
    "privacy", "Privacy Policy | Max Return Taxes",
    "How Max Return Taxes collects, uses and protects information submitted through this website.",
    "Privacy Policy", "Privacy Policy", "What we collect through this website, how we use it, and your choices."
    , PRIVACY_BODY), encoding="utf-8")
print("privacy page written")
