"""Generate the Max Return Taxes blog. Usage: python -I build_blog.py <repo_dir>"""
import json, re, sys, pathlib, html, datetime

ROOT = pathlib.Path(sys.argv[1])
SITE = "https://saturn369.github.io/max-return-taxes"
PHONE_TEL, PHONE = "+18609939904", "(860) 993-9904"
EMAIL = "freedomenka@gmail.com"
PUBLISHED = "2026-11-17"
ARROW = '<svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>'
FAVICON = ("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 64 64%27%3E%3Crect width=%2764%27 height=%2764%27 rx=%2712%27 fill=%27%23080808%27/%3E"
           "%3Ctext x=%2732%27 y=%2746%27 font-family=%27Georgia,serif%27 font-size=%2740%27 font-weight=%27700%27 text-anchor=%27middle%27 fill=%27%23C9A84C%27%3EM%3C/text%3E%3C/svg%3E")
SERVICES = {"business-tax-returns": "Business Tax Returns", "late-tax-returns": "Late &amp; Unfiled Returns",
            "amended-tax-returns": "Amended Returns", "connecticut-tax-preparer": "Hartford County, CT"}

def strip(s): return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()
def human_date(s): d = datetime.date.fromisoformat(s); return d.strftime("%B ") + str(d.day) + d.strftime(", %Y")

def nav(pre):
    links = [("Services", f"{pre}#services"), ("Why Us", f"{pre}#why"), ("Process", f"{pre}#process"), ("Blog", f"{pre}blog/"), ("Contact", f"{pre}#contact")]
    li = "".join(f'<li><a href="{h}">{t}</a></li>' for t, h in links)
    return f'''<nav class="nav" id="nav">
    <div class="container nav-inner">
      <a href="{pre}" class="logo">Max Return<span class="logo-sep"></span><span class="logo-accent">Taxes</span></a>
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
          <a href="{pre}" class="logo">Max Return<span class="logo-sep"></span><span class="logo-accent">Taxes</span></a>
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
        <div class="f-copy">© 2026 Max Return Taxes · Hartford County, CT · All rights reserved.</div>
        <div class="f-credit">Motion effects derived from <a href="https://github.com/DavidHDev/vue-bits" target="_blank" rel="noopener">vue-bits</a> by DavidHDev (MIT)</div>
      </div>
    </div>
  </footer>'''

def head(pre, title, desc, url, ld, og_type="website"):
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
  <meta property="og:type" content="{og_type}">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{t}">
  <meta property="og:description" content="{d}">
  <meta property="og:image" content="{SITE}/og-image.jpg">
  <meta property="og:site_name" content="Max Return Taxes">
  <meta property="og:locale" content="en_US">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{t}">
  <meta name="twitter:description" content="{d}">
  <meta name="twitter:image" content="{SITE}/og-image.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{pre}assets/site.css">
  <script type="application/ld+json">
{json.dumps(ld, indent=2, ensure_ascii=False)}
  </script>
</head>'''

def cta(pre, title, sub):
    return f'''<section class="cta-section">
    <div class="container">
      <div class="cta-eye">Free Consultation</div>
      <h2 class="cta-title">{title}</h2>
      <p class="cta-sub">{sub}</p>
      <div class="cta-actions">
        <a href="{pre}#contact" class="btn btn-gold btn-lg">Send Us a Message</a>
        <a href="tel:{PHONE_TEL}" class="btn btn-ghost btn-lg">Call {PHONE}</a>
      </div>
      <p class="cta-note">Free consultation · No obligation · We respond within 24 hours</p>
    </div>
  </section>'''

def callout(pre, slug, text):
    return (f'<aside class="callout"><p>{text}</p><a class="svc-link" href="{pre}{slug}/">{strip(SERVICES[slug])} {ARROW}</a></aside>')

def table(head_, rows):
    th = "".join(f"<th>{h}</th>" for h in head_)
    tr = "".join("<tr>" + "".join(f'<td data-label="{strip(h)}">{c}</td>' for h, c in zip(head_, r)) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="dl-table"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'

# ---------------------------------------------------------------- POSTS
# Each body is HTML using {pre} for the path back to site root ("../../").
POSTS = []

def post(slug, title, h1, desc, tag, service, excerpt, body, cta_title, cta_sub):
    POSTS.append(dict(slug=slug, title=title, h1=h1, desc=desc, tag=tag, service=service, excerpt=excerpt,
                      body=body, cta_title=cta_title, cta_sub=cta_sub))

P = "../../"

post("havent-filed-taxes-in-years",
     "Haven't Filed Taxes in Years? Here's What Happens — and What to Do | Max Return Taxes",
     "Haven't Filed Taxes in Years? Here's What Happens — and What to Do",
     "What happens when you don't file taxes for several years: penalties, lost refunds, IRS substitute returns — and the step-by-step way to get current.",
     "Late Filing", "late-tax-returns",
     "Penalties, lost refunds, and IRS substitute returns — plus the step-by-step way to get back in good standing.",
     f'''<p>If you've gone a year or more without filing, you're far from alone — and the situation is almost always more fixable than it feels. But unfiled returns don't resolve themselves, and waiting usually makes them more expensive. Here's what's actually happening behind the scenes, and how to get current.</p>

<h2>What happens when you don't file</h2>
<h3>Penalties and interest keep growing</h3>
<p>If you owe tax, the IRS charges a <strong>failure-to-file penalty</strong> of 5% of the unpaid tax for each month (or part of a month) the return is late, up to 25%. There's also a smaller <strong>failure-to-pay penalty</strong> and interest on the balance. The longer a return sits, the more those add up. (We break down the two penalties in <a href="{P}blog/failure-to-file-vs-failure-to-pay-penalty/">this guide</a>.)</p>
<h3>Refunds can expire</h3>
<p>Plenty of people who don't file are actually owed money. But you generally have <strong>three years from the original due date</strong> to claim a refund. After that, it's gone — the money stays with the Treasury.</p>
<h3>The IRS may file for you — badly</h3>
<p>The IRS receives copies of your W-2s, 1099s and other income documents. If you don't file, it can prepare a <strong>substitute for return</strong> based on that income — without your deductions, credits, dependents, or business expenses. The result is usually a much larger bill than you'd owe on a return you filed yourself. A substitute return doesn't stop you from filing your own; filing your own return is usually how you bring the bill back down.</p>
<h3>Collection can follow</h3>
<p>Once tax is assessed and notices go unanswered, the IRS can move to collection, including liens and levies on wages or bank accounts. Responding early keeps far more options open.</p>
<h3>Self-employed? Your Social Security record is affected too</h3>
<p>If you're self-employed, your tax return is how your earnings get reported for Social Security. Years you don't file may not count toward your future benefits.</p>

{callout(P, "late-tax-returns", "Behind on one year or several? We prepare past-due federal and state returns and help you get back in good standing — no judgment.")}

<h2>How to get current, step by step</h2>
<ol>
<li><strong>Find out what the IRS has on file.</strong> Your IRS wage and income transcripts show the W-2, 1099 and other income reported for each year — so lost paperwork isn't a dead end. (Here's <a href="{P}blog/lost-w2-1099-irs-transcript/">how to get them</a>.)</li>
<li><strong>Figure out which years to file.</strong> The IRS generally expects the last six years of returns to be filed for you to be considered in good standing. That's often the starting point.</li>
<li><strong>Prepare each return properly.</strong> Claim every deduction and credit you're entitled to — especially business expenses, which substitute returns leave out.</li>
<li><strong>Don't forget your state.</strong> Connecticut and most other states have their own filing requirements, penalties and interest.</li>
<li><strong>Make a plan for any balance.</strong> If you can't pay in full, the IRS offers payment plans. And you may qualify for penalty relief, such as First-Time Abatement or reasonable cause.</li>
</ol>

<h2>Should you file even if you can't pay?</h2>
<p>Yes. The failure-to-file penalty grows far faster than the failure-to-pay penalty, so filing on its own slows how quickly your balance grows. It also starts the clock on your refund rights and lets you set up a payment plan.</p>

<h2>The bottom line</h2>
<p>Unfiled returns get more expensive the longer they sit, but they're a solvable problem. The right first step is finding out where you stand — then filing the missing years correctly.</p>''',
     "Ready to Get Current?", "Tell us how many years you're behind. We'll reply within 24 hours with a plan — no lectures, no judgment.")

post("how-far-back-can-you-amend-a-tax-return",
     "How Far Back Can You Amend a Tax Return? | Max Return Taxes",
     "How Far Back Can You Amend a Tax Return?",
     "The time limits for amending a tax return to claim a refund, which form to use, when you don't need to amend, and how long amended returns take.",
     "Amendments", "amended-tax-returns",
     "The refund deadline for amended returns, which form to file, and when you don't need to amend at all.",
     f'''<p>Found a mistake on a past return — or realized you missed a deduction? You may be able to fix it and get money back. But there's a deadline, and once it passes, a refund you were entitled to is gone for good.</p>

<h2>The time limit for claiming a refund</h2>
<p>To claim a refund, you generally must file an amended return within <strong>three years</strong> of the date you filed the original return, or within <strong>two years</strong> of the date you paid the tax — whichever is later.</p>
<p>One detail matters a lot: a return filed <em>before</em> the April deadline is treated as if it were filed on the deadline. So for a return filed early, the three years run from the April due date, not the day you actually filed.</p>
<p>If an amendment means you owe <em>more</em> tax, there's no reason to wait. Interest runs from the original due date, so the sooner you correct it, the less it costs.</p>

<h2>Which form do you use?</h2>
{table(["Original return", "How it's amended"], [
    ["Individual (Form 1040)", "Form 1040-X"],
    ["S Corporation (Form 1120-S)", "An amended 1120-S, with corrected K-1s for shareholders"],
    ["C Corporation (Form 1120)", "Form 1120-X"],
    ["Partnership (Form 1065)", "Usually an Administrative Adjustment Request, with corrected K-1 information"],
    ["Connecticut (Form CT-1040)", "Form CT-1040X"],
])}
<p>Form 1040-X can be filed electronically for recent tax years, which is faster and easier to track than paper.</p>

{callout(P, "amended-tax-returns", "Think a past return was wrong? We review prior-year returns and file federal and state amendments to fix the record and claim refunds you're owed.")}

<h2>Good reasons to amend</h2>
<ul>
<li>You missed deductions or credits you qualified for</li>
<li>You received a corrected W-2, 1099 or K-1 after filing</li>
<li>Your filing status or dependents were wrong</li>
<li>Income was left off the return</li>
<li>An error on an S-Corp or partnership return flowed through to your personal return</li>
</ul>

<h2>When you don't need to amend</h2>
<p>The IRS corrects simple math errors on its own, and if you forgot to attach a form or schedule, it will usually write and ask for it. In those cases, an amended return isn't needed.</p>

<h2>How long does an amended return take?</h2>
<p>The IRS says amended returns generally take 8 to 12 weeks to process, and sometimes up to 16. You can follow the status with the IRS's "Where's My Amended Return?" tool, though it can take a few weeks after filing for a return to show up there.</p>

<h2>Don't forget your state return</h2>
<p>If a federal change affects your state tax, most states — including Connecticut — expect you to amend your state return too.</p>''',
     "Think a Past Return Was Wrong?", "Send it over and tell us what you're worried about. We'll reply within 24 hours and tell you whether an amendment makes sense.")

post("failure-to-file-vs-failure-to-pay-penalty",
     "Failure-to-File vs. Failure-to-Pay Penalty: What's the Difference? | Max Return Taxes",
     "Failure-to-File vs. Failure-to-Pay Penalty: What's the Difference?",
     "How the IRS failure-to-file and failure-to-pay penalties work, how they combine, how interest is added, and how penalty relief like First-Time Abatement works.",
     "IRS Penalties", "late-tax-returns",
     "Why the penalty for not filing is ten times bigger than the penalty for not paying — and how to get penalties reduced.",
     f'''<p>The IRS charges two different penalties when a return is late or tax goes unpaid — and one is much bigger than the other. Knowing the difference explains the most important rule for anyone who's behind: <strong>file on time, even if you can't pay</strong>.</p>

<h2>The two penalties at a glance</h2>
{table(["", "Failure to file", "Failure to pay"], [
    ["When it applies", "Your return is filed late", "Tax shown on your return isn't paid by the due date"],
    ["Monthly rate", "5% of unpaid tax per month or part of a month", "0.5% of unpaid tax per month or part of a month"],
    ["Maximum", "25% of unpaid tax", "25% of unpaid tax"],
])}

<h2>Failure-to-file: the big one</h2>
<p>The failure-to-file penalty is 5% of the unpaid tax for each month or part of a month your return is late, up to 25%. If your return is more than 60 days late, there's also a minimum penalty — the lesser of a set dollar amount (adjusted each year for inflation) or 100% of the tax owed.</p>
<p>An extension avoids this penalty, because it pushes back your filing deadline. But an extension doesn't extend the time to pay.</p>

<h2>Failure-to-pay: smaller, but it lasts longer</h2>
<p>The failure-to-pay penalty is 0.5% of the unpaid tax per month, up to 25%. If you filed on time and set up an IRS payment plan, the rate drops to 0.25% a month while the plan is in effect. If the IRS issues a notice of intent to levy and the balance still isn't paid, it goes up to 1% a month.</p>

<h2>When both penalties apply</h2>
<p>If you both file and pay late, the failure-to-file penalty is reduced by the failure-to-pay penalty for any month both apply — so the combined charge is 5% a month, not 5.5%.</p>

<h2>Interest is added on top</h2>
<p>Interest is charged on unpaid tax from the original due date, and on penalties as well. The rate is set every quarter (the federal short-term rate plus 3%) and compounds daily. Unlike penalties, interest generally can't be waived — though if a penalty is removed, the interest on that penalty goes with it.</p>

{callout(P, "late-tax-returns", "Behind on filing? We prepare past-due returns, figure out your real balance, and look at whether you qualify for penalty relief.")}

<h2>Can penalties be removed?</h2>
<p>Often, yes. The two most common forms of relief:</p>
<ul>
<li><strong>First-Time Abatement.</strong> If you have a clean record — generally no significant penalties in the prior three years, and all required returns filed — the IRS may remove failure-to-file and failure-to-pay penalties for a single tax year.</li>
<li><strong>Reasonable cause.</strong> If you couldn't file or pay on time despite ordinary care — because of a serious illness, a disaster, or similar circumstances — penalties may be reduced or removed.</li>
</ul>

<h2>The takeaway</h2>
<p>Because the failure-to-file penalty is ten times larger per month, filing on time — even if you can't pay — is almost always the right move. Then set up a payment plan and look into penalty relief.</p>''',
     "Facing IRS Penalties?", "Tell us what's going on. We'll reply within 24 hours and help you understand what you owe and what can be reduced.")

post("2027-business-tax-deadlines",
     "2027 Business Tax Deadlines: Calendar for S-Corps, LLCs & Sole Proprietors | Max Return Taxes",
     "2027 Business Tax Deadlines: What's Due and When",
     "Key 2027 federal tax deadlines for small businesses: W-2s and 1099s, S-Corp and partnership returns, C-Corp and Schedule C returns, extensions and quarterly estimates.",
     "Deadlines", "business-tax-returns",
     "Every key federal date for S-Corps, partnerships, C-Corps and sole proprietors in 2027 — in one calendar.",
     f'''<p>Missing a business tax deadline is one of the most avoidable ways to pay a penalty — and for S-Corps and partnerships, a late return is penalized even if the business owes no tax. Here are the key federal dates for calendar-year businesses in 2027, covering tax year 2026 returns and 2027 estimated payments.</p>

<h2>2027 federal deadline calendar</h2>
{table(["Date", "What's due"], [
    ["Friday, January 15", "4th-quarter 2026 estimated tax payment"],
    ["Monday, February 1", "W-2s to employees and the SSA; 1099-NEC to contractors and the IRS (moved from January 31, a Sunday)"],
    ["Monday, March 15", "S-Corp (Form 1120-S) and partnership (Form 1065) returns, or Form 7004 extension; K-1s to owners"],
    ["Thursday, April 15", "Individual returns including Schedule C (Form 1040), or Form 4868 extension; C-Corp returns (Form 1120), or Form 7004 extension; 1st-quarter 2027 estimated tax; last day for most 2026 IRA and HSA contributions"],
    ["Tuesday, June 15", "2nd-quarter 2027 estimated tax payment"],
    ["Wednesday, September 15", "Extended S-Corp and partnership returns; 3rd-quarter 2027 estimated tax payment"],
    ["Friday, October 15", "Extended individual and C-Corp returns"],
    ["Tuesday, January 18, 2028", "4th-quarter 2027 estimated tax payment (moved from January 15, a Saturday; January 17 is a federal holiday)"],
])}
<p>These are for businesses on a calendar year. Fiscal-year businesses have different dates. The IRS also regularly postpones deadlines for areas hit by federally declared disasters, so check for relief if you're affected.</p>

<h2>Extensions: more time to file, not to pay</h2>
<p>Form 7004 gives businesses an automatic six-month extension to file, and Form 4868 does the same for individuals, including sole proprietors. But tax owed is still due by the original deadline. Interest and the failure-to-pay penalty apply to anything paid late.</p>

<h2>Why S-Corp and partnership deadlines matter so much</h2>
<p>A late 1120-S or 1065 is penalized <strong>per shareholder or partner, per month</strong>, for up to 12 months — even when the business owes nothing. Those returns also produce the K-1s owners need for their personal returns, so filing late can hold up everyone's taxes.</p>

{callout(P, "business-tax-returns", "We prepare S-Corp, partnership, C-Corp and Schedule C returns — on time, with every legitimate deduction claimed.")}

<h2>Don't forget state deadlines</h2>
<p>State due dates often follow the federal ones, but not always. Connecticut and other states have their own returns, extension rules and estimated payment schedules, so check every state where your business files.</p>''',
     "Don't Wait for March 15", "Get your business return on our calendar now. We'll reply within 24 hours with what we need from you.")

post("should-my-llc-elect-s-corp-status",
     "Should Your LLC Elect S-Corp Status? Pros, Cons & Deadlines | Max Return Taxes",
     "Should Your LLC Elect S-Corp Status?",
     "How an S-Corp election can lower self-employment tax for LLC owners, what it costs, the reasonable-salary rule, and the deadline for filing Form 2553.",
     "Business Taxes", "business-tax-returns",
     "How the S-Corp election can cut self-employment tax, what it really costs, and when it doesn't pay off.",
     f'''<p>It's one of the most common questions profitable small-business owners ask: "Should my LLC be an S-Corp?" Sometimes the answer is a clear yes that saves real money every year. Sometimes the extra cost and paperwork outweigh the savings. Here's how to think it through.</p>

<h2>How an LLC is taxed by default</h2>
<p>A single-member LLC is taxed like a sole proprietorship, and a multi-member LLC like a partnership. Either way, the owners generally pay <strong>self-employment tax</strong> — 15.3% for Social Security and Medicare, with the Social Security part capped each year — on their share of the business's net earnings, on top of income tax.</p>

<h2>What changes with an S-Corp election</h2>
<p>An LLC can elect to be taxed as an S Corporation. The business still passes its income through to the owners, but owners who work in the business are paid in two ways:</p>
<ul>
<li><strong>A salary,</strong> run through payroll, which is subject to Social Security and Medicare taxes, just like any employee's wages.</li>
<li><strong>Distributions</strong> of the remaining profit, which are not subject to self-employment tax.</li>
</ul>
<p>The potential savings come from that second part: profit taken as distributions avoids the 15.3% tax that would otherwise apply.</p>

<h2>The catch: a reasonable salary</h2>
<p>The IRS requires S-Corp owner-employees to pay themselves <strong>reasonable compensation</strong> — roughly what you'd have to pay someone else to do your job. You can't take a token salary and call everything else a distribution. That rule is what decides how much an election can actually save.</p>

<h2>The costs of being an S-Corp</h2>
<ul>
<li>Running payroll, with quarterly payroll tax filings and year-end W-2s</li>
<li>A separate business return (Form 1120-S) every year, due March 15</li>
<li>More bookkeeping and accountability for owner pay and distributions</li>
<li>Possible state-level costs or filing requirements, depending on your state</li>
<li>Health insurance for more-than-2% owners has to be handled through payroll</li>
</ul>
<p>There can also be effects on other parts of your taxes, like the qualified business income deduction and retirement plan contribution limits. Those should be part of the math.</p>

<h2>When it tends to make sense</h2>
<p>An S-Corp election generally starts to pay off once your profit is comfortably more than a reasonable salary for your role — enough that the self-employment tax saved on distributions clearly outweighs the added costs. If your profit is modest or swings a lot from year to year, the default treatment may be the better choice.</p>

{callout(P, "business-tax-returns", "We can run the numbers for your business — salary, distributions, payroll costs and state rules — and tell you whether an election makes sense.")}

<h2>How and when to elect</h2>
<p>The election is made on <strong>Form 2553</strong>. To take effect for a given year, it generally must be filed no later than two months and 15 days after the start of that tax year — <strong>March 15</strong> for a calendar-year business — or any time during the year before. If you miss the deadline, the IRS has procedures for late-election relief in many cases.</p>''',
     "Is an S-Corp Right for You?", "Tell us about your business and profit. We'll reply within 24 hours and help you decide with real numbers.")

post("lost-w2-1099-irs-transcript",
     "Lost Your W-2 or 1099? How to Get Your Income Records From the IRS | Max Return Taxes",
     "Lost Your W-2 or 1099? How to Get Your Income Records From the IRS",
     "How to get missing W-2 and 1099 information with an IRS wage and income transcript, what transcripts show and don't show, and what to do if a form never arrived.",
     "How-To", "late-tax-returns",
     "How to use an IRS wage and income transcript to file — even for years when the paperwork is long gone.",
     f'''<p>Missing tax forms are one of the biggest reasons people put off filing — especially when they're catching up on past years. The good news is that the IRS already has copies of most of them, and you can get that information yourself.</p>

<h2>Use an IRS wage and income transcript</h2>
<p>Employers, banks, brokers and other payers send copies of your W-2s, 1099s and similar forms to the IRS. A <strong>wage and income transcript</strong> shows the data from those forms for a given tax year, and it's available for up to ten years back.</p>
<p>Ways to get one:</p>
<ul>
<li><strong>Online:</strong> through your IRS Individual Online Account at irs.gov, where you can view and download transcripts right away after verifying your identity.</li>
<li><strong>By mail:</strong> by requesting a transcript with Form 4506-T.</li>
<li><strong>Through a tax professional:</strong> with your written authorization, your preparer can request transcripts for you.</li>
</ul>

<h2>What a transcript shows — and what it doesn't</h2>
<p>Transcripts list the income, withholding and payment information that was reported to the IRS. But they have limits:</p>
<ul>
<li>They don't include <strong>state</strong> wage or withholding information. For that, check old pay stubs, contact the employer, or ask your state tax agency.</li>
<li>They only show what was reported. <strong>Cash income</strong> or work paid without a 1099 won't appear, but it still has to be reported.</li>
<li>Information for the most recent tax year may not be complete until later in the year.</li>
<li>They don't show your <strong>deductions and expenses</strong>. Business owners should rebuild those from bank statements, receipts and other records.</li>
</ul>

{callout(P, "late-tax-returns", "Catching up on past years? We pull your transcripts with your authorization and prepare every missing return.")}

<h2>If this year's W-2 never arrived</h2>
<ol>
<li><strong>Ask the employer first.</strong> W-2s are due by the end of January. If yours hasn't arrived by mid-February, contact the employer and confirm your address.</li>
<li><strong>Contact the IRS</strong> if the employer doesn't respond by the end of February.</li>
<li><strong>File on time anyway.</strong> If the form still doesn't come, you can file using Form 4852, a substitute W-2, based on your final pay stub. If the real form later shows different numbers, you may need to amend.</li>
</ol>

<h2>The bottom line</h2>
<p>Lost paperwork shouldn't stop you from filing. Between IRS transcripts and your own records, you can almost always rebuild what you need — and the sooner you file, the less penalties and interest add up.</p>''',
     "Missing Paperwork? We Can Help", "Tell us which years you need to file. We'll reply within 24 hours and help track down what's missing.")

# ---------------------------------------------------------------- RENDER
def words(s): return len(strip(s).split())

def render_post(p, others):
    url = f"{SITE}/blog/{p['slug']}/"
    mins = max(3, round(words(p["body"]) / 230))
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BlogPosting", "@id": url + "#article", "headline": strip(p["h1"]), "description": p["desc"],
         "datePublished": PUBLISHED, "dateModified": PUBLISHED, "mainEntityOfPage": url, "image": f"{SITE}/og-image.jpg",
         "author": {"@type": "Organization", "name": "Max Return Taxes", "url": f"{SITE}/"},
         "publisher": {"@id": f"{SITE}/#business"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{SITE}/blog/"},
            {"@type": "ListItem", "position": 3, "name": strip(p["h1"]), "item": url}]}]}
    rel = "".join(post_card(P, o) for o in others[:3])
    return f'''{head(P, p["title"], p["desc"], url, ld, "article")}
<body>
  <div class="scroll-progress" id="sp"></div>
  {nav(P)}

  <header class="page-hero article-hero">
    <div class="hero-bg"></div><div class="hero-grid"></div><div class="hero-vignette"></div>
    <div class="container page-hero-content">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="{P}">Home</a><span aria-hidden="true">/</span><a href="{P}blog/">Blog</a><span aria-hidden="true">/</span><span>{p["tag"]}</span></nav>
      <div class="hero-eyebrow">{p["tag"]}</div>
      <h1 class="page-title article-title">{p["h1"]}</h1>
      <p class="article-meta"><time datetime="{PUBLISHED}">{human_date(PUBLISHED)}</time><span aria-hidden="true">·</span>{mins} min read<span aria-hidden="true">·</span>Max Return Taxes</p>
    </div>
  </header>

  <main>
    <section class="page-section"><div class="container">
      <article class="article-body">
{p["body"]}
        <p class="article-disclaimer">This article is general information, not tax or legal advice for your specific situation. Tax rules change and have exceptions — talk with a tax professional before acting on it.</p>
      </article>
    </div></section>
    <section class="page-section page-section-alt"><div class="container">
      <div class="section-eye">Keep Reading</div>
      <div class="post-grid">{rel}</div>
    </div></section>
    {cta(P, p["cta_title"], p["cta_sub"])}
  </main>

  {footer(P)}
  <script src="{P}assets/site.js" defer></script>
</body>
</html>
'''

def post_card(pre, p):
    return (f'<a class="post-card" href="{pre}blog/{p["slug"]}/"><span class="svc-tag">{p["tag"]}</span>'
            f'<h3 class="post-card-title">{p["h1"]}</h3><p class="post-card-ex">{p["excerpt"]}</p>'
            f'<span class="svc-link">Read article {ARROW}</span></a>')

def render_index():
    pre = "../"; url = f"{SITE}/blog/"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Blog", "@id": url + "#blog", "name": "Max Return Taxes Blog", "url": url,
         "publisher": {"@id": f"{SITE}/#business"},
         "blogPost": [{"@type": "BlogPosting", "headline": strip(p["h1"]), "url": f"{url}{p['slug']}/", "datePublished": PUBLISHED} for p in POSTS]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": url}]}]}
    cards = "".join(post_card(pre, p) for p in POSTS)
    return f'''{head(pre, "Tax Tips & Guides for Business Owners | Max Return Taxes Blog",
        "Plain-English guides to business taxes, late and unfiled returns, amended returns, IRS penalties and deadlines — from Max Return Taxes in Hartford County, CT.", url, ld)}
<body>
  <div class="scroll-progress" id="sp"></div>
  {nav(pre)}

  <header class="page-hero">
    <div class="hero-bg"></div><div class="hero-grid"></div><div class="hero-vignette"></div>
    <div class="container page-hero-content">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="{pre}">Home</a><span aria-hidden="true">/</span><span>Blog</span></nav>
      <div class="hero-eyebrow">Tax Guides</div>
      <h1 class="page-title">Straight Answers on <span class="text-gold">Taxes.</span></h1>
      <p class="page-sub">Plain-English guides to business taxes, late returns, amendments, IRS penalties and deadlines — written for business owners and individuals, not accountants.</p>
    </div>
  </header>

  <main>
    <section class="page-section"><div class="container">
      <div class="post-grid">{cards}</div>
    </div></section>
    {cta(pre, "Have a Question That's Not Answered Here?", "Send us a message. We'll reply within 24 hours with a straight answer.")}
  </main>

  {footer(pre)}
  <script src="{pre}assets/site.js" defer></script>
</body>
</html>
'''

blog = ROOT / "blog"; blog.mkdir(exist_ok=True)
(blog / "index.html").write_text(render_index(), encoding="utf-8")
for i, p in enumerate(POSTS):
    others = [o for o in POSTS if o["service"] == p["service"] and o is not p] + [o for o in POSTS if o["service"] != p["service"]]
    d = blog / p["slug"]; d.mkdir(exist_ok=True)
    (d / "index.html").write_text(render_post(p, others), encoding="utf-8")
print("posts:", len(POSTS), "| words:", [words(p["body"]) for p in POSTS])
