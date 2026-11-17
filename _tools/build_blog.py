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

post("do-i-need-to-send-1099s-to-contractors",
     "Do You Need to Send 1099s to Contractors? 2027 Rules & the New $2,000 Threshold | Max Return Taxes",
     "Do You Need to Send 1099s to Contractors? The 2027 Rules",
     "Who gets a 1099-NEC, the new $2,000 reporting threshold for 2026 payments, exceptions for corporations and card payments, W-9s, deadlines and penalties.",
     "Business Taxes", "business-tax-returns",
     "The threshold just jumped from $600 to $2,000. Here's who still needs a 1099-NEC, and when it's due.",
     f'''<p>If your business paid freelancers, contractors or other self-employed people this year, you may need to send them a Form 1099-NEC by early 2027. The rules changed recently, so even if you've done this for years, they're worth a fresh look.</p>

<h2>The big change: $600 is now $2,000</h2>
<p>For years, you had to file a 1099-NEC for any contractor you paid <strong>$600 or more</strong> during the year. A 2025 federal tax law raised that threshold to <strong>$2,000</strong> for payments made in 2026 and later, with inflation adjustments starting after that. The same change applies to many payments reported on Form 1099-MISC, such as rent.</p>
<p>That means the forms due in early 2027, covering what you paid in 2026, are the first ones under the higher threshold. Paid a contractor $1,500 in 2026? You generally no longer need to send that person a 1099-NEC.</p>
<p>The contractor still has to report that income on their own return, whether or not they get a form.</p>

<h2>Who gets a 1099-NEC</h2>
<p>Generally, you need to file a 1099-NEC when all of these are true:</p>
<ul>
<li>You paid someone who <strong>isn't your employee</strong>, such as a freelancer, independent contractor or consultant</li>
<li>You paid them for <strong>services</strong> in the course of your trade or business, not personal expenses</li>
<li>The person is an <strong>individual, partnership or LLC</strong> that isn't taxed as a corporation</li>
<li>You paid them <strong>at least the threshold amount</strong> during the year: $2,000 for 2026 payments</li>
</ul>

<h2>Common exceptions</h2>
<ul>
<li><strong>Corporations.</strong> Payments to C-Corps and S-Corps generally don't need a 1099. Payments for legal services are the big exception: attorneys get a 1099 even if their firm is incorporated.</li>
<li><strong>Card and app payments.</strong> If you paid by credit card, debit card or a payment app's business payment option, the payment company handles the reporting on Form 1099-K. Don't also send a 1099-NEC for those payments.</li>
<li><strong>Employees.</strong> People on your payroll get a W-2, not a 1099.</li>
<li><strong>Personal payments.</strong> Hiring someone to paint your own house isn't a business payment.</li>
</ul>

{callout(P, "business-tax-returns", "Not sure who needs a 1099 this year? We sort out your contractor payments and file your 1099s alongside your business return.")}

<h2>Get a W-9 before you pay</h2>
<p>The easiest way to stay on top of 1099s is to collect a <strong>Form W-9</strong> from every contractor before you pay them. It gives you their legal name, tax classification and taxpayer identification number. That tells you whether they need a 1099 and gives you everything you need to file one.</p>
<p>If a contractor won't give you a valid taxpayer ID, you may be required to withhold <strong>24% backup withholding</strong> from their payments and send it to the IRS.</p>

<h2>Deadlines and how to file</h2>
<p>Form 1099-NEC is due to <strong>both the contractor and the IRS by January 31</strong>. In 2027, January 31 falls on a Sunday, so the deadline is <strong>Monday, February 1, 2027</strong>. Unlike most tax forms, there's no automatic extension.</p>
<p>If you're filing 10 or more information returns in total, including W-2s and other 1099s, you must file them electronically. The IRS's free IRIS portal lets businesses e-file 1099s directly.</p>
<p>Some states have their own 1099 filing requirements, and Connecticut is one of them in many cases. Check your state's rules too.</p>

<h2>Penalties for late or missing 1099s</h2>
<p>The IRS charges a penalty for each 1099 that's filed late, filed with wrong information or never filed. The amount grows the later you file, and it's much steeper if the IRS finds you intentionally ignored the requirement. The penalty dollar amounts are adjusted for inflation every year. Filing on time, even if you need to correct a form later, is always cheaper.</p>

<h2>Contractor or employee?</h2>
<p>A 1099 only works if the person really is an independent contractor. If you control how, when and where someone does the work, they may legally be an employee. In that case, payroll taxes and a W-2 apply instead. Misclassification can be expensive, so if you're unsure, it's worth getting advice before year-end.</p>''',
     "Get Your 1099s Done Right", "Send us your list of contractors and payments. We'll reply within 24 hours and tell you exactly who needs a form.")

post("home-office-deduction",
     "Home Office Deduction: Who Qualifies & How to Calculate It | Max Return Taxes",
     "The Home Office Deduction: Who Qualifies and How to Claim It",
     "Who qualifies for the home office deduction, the simplified vs. regular method, what expenses count, how S-Corp owners should handle it, and the depreciation catch when you sell.",
     "Deductions", "business-tax-returns",
     "The two tests you have to pass, the simplified vs. regular method, and the catch S-Corp owners often miss.",
     f'''<p>If you run a business from home, part of what you spend on your home may be deductible. But the rules are strict, and the right way to claim it depends on how your business is set up. Here's how it works.</p>

<h2>First: who can take it</h2>
<p>The home office deduction is for <strong>self-employed people and business owners</strong>. If you're a W-2 employee who works from home for someone else's company, you generally can't deduct home office expenses on your federal return, even if your employer requires you to work remotely.</p>

<h2>The two tests your space has to pass</h2>
<h3>1. Regular and exclusive use</h3>
<p>The space must be used <strong>regularly</strong> for your business, and <strong>only</strong> for your business. A spare room that's purely an office qualifies. A kitchen table where you also eat dinner doesn't. The space doesn't have to be a full room, but it does need to be a clearly separate area. There are limited exceptions for daycare providers and for storing inventory or product samples.</p>
<h3>2. It's your principal place of business, or another qualifying use</h3>
<p>The space must meet one of these:</p>
<ul>
<li>It's your <strong>principal place of business</strong>. This includes a home office where you do your administrative or management work, like billing, scheduling and bookkeeping, if you have no other fixed location where you do that work. So a contractor who works on job sites can still qualify.</li>
<li>You <strong>meet clients or customers</strong> there in the normal course of business.</li>
<li>It's a <strong>separate structure</strong>, like a detached garage or studio, used for your business.</li>
</ul>

<h2>Two ways to calculate it</h2>
{table(["", "Simplified method", "Regular method"], [
    ["How it works", "$5 per square foot of office space", "The business percentage of your actual home expenses"],
    ["Maximum", "300 sq ft, which is a $1,500 deduction", "No set cap, but it can't exceed your business income"],
    ["Expenses included", "Covered by the flat rate", "Mortgage interest or rent, property tax, insurance, utilities, repairs, depreciation"],
    ["Paperwork", "Minimal", "Form 8829 and detailed records"],
    ["Depreciation", "None", "Yes, which affects you when you sell"],
])}
<p>To find your business percentage for the regular method, divide the office's square footage by your home's total square footage. A 200 sq ft office in a 2,000 sq ft home is 10%. Expenses that apply only to the office, like painting it, are fully deductible.</p>
<p>You can choose either method each year. The regular method often produces a bigger deduction, especially for renters and people in high-cost homes. The simplified method is far less work.</p>

{callout(P, "business-tax-returns", "We'll figure out whether you qualify, compare both methods and claim the one that saves you more.")}

<h2>The catch: depreciation when you sell</h2>
<p>Under the regular method, homeowners deduct depreciation on the office portion of the home. When you later sell the home, the depreciation you claimed, or could have claimed, after May 6, 1997 is generally taxable, even if the rest of your gain is tax-free under the home sale exclusion. That's not a reason to skip the deduction, but it should be part of the decision. The simplified method avoids it entirely.</p>

<h2>Own an S-Corp? It works differently</h2>
<p>If your business is an S-Corp, you're technically an employee of your own company, so you can't claim a home office deduction on Schedule C. Instead, the corporation can <strong>reimburse you</strong> for the business share of your home expenses under a written <strong>accountable plan</strong>. The business deducts the reimbursement, and it isn't taxable income to you. Partners in a partnership may have a similar option, depending on the partnership agreement. (Thinking about becoming an S-Corp? <a href="{P}blog/should-my-llc-elect-s-corp-status/">Here's how to decide</a>.)</p>

<h2>Keep good records</h2>
<ul>
<li>Measurements of the office and your whole home</li>
<li>Photos showing the space is set up only for business</li>
<li>A year of utility bills, insurance, property tax and mortgage interest or rent statements</li>
<li>Receipts for repairs or improvements to the office</li>
</ul>''',
     "Working From Home?", "Tell us about your setup. We'll reply within 24 hours and help you claim the deduction the right way.")

post("quarterly-estimated-taxes-self-employed",
     "Quarterly Estimated Taxes for the Self-Employed: Who Pays, When & How Much | Max Return Taxes",
     "Quarterly Estimated Taxes: Who Has to Pay, When, and How Much",
     "Who has to make quarterly estimated tax payments, the 2027 due dates, the safe harbor rules that avoid the underpayment penalty, and how to pay.",
     "Self-Employed", "business-tax-returns",
     "The 2027 due dates, the safe-harbor rules that keep you penalty-free, and a payroll trick for S-Corp owners.",
     f'''<p>When you work for an employer, tax comes out of every paycheck. When you work for yourself, nobody withholds it for you. The IRS still expects to be paid during the year, not all at once in April. That's what quarterly estimated taxes are for.</p>

<h2>Who has to pay estimated taxes</h2>
<p>You generally need to make estimated payments if you expect to owe <strong>$1,000 or more</strong> when you file your return, after subtracting withholding and refundable credits. That usually includes:</p>
<ul>
<li>Sole proprietors, freelancers and independent contractors</li>
<li>Partners and LLC members who receive business income</li>
<li>S-Corp owners whose payroll withholding doesn't cover their taxes on business profit</li>
<li>Anyone with significant investment, rental or other income that has no withholding</li>
</ul>
<p>Corporations have their own estimated tax rules and generally must pay if they expect to owe $500 or more.</p>

<h2>2027 due dates</h2>
{table(["Payment", "Covers income earned", "Due date"], [
    ["1st quarter", "January 1 – March 31", "Thursday, April 15, 2027"],
    ["2nd quarter", "April 1 – May 31", "Tuesday, June 15, 2027"],
    ["3rd quarter", "June 1 – August 31", "Wednesday, September 15, 2027"],
    ["4th quarter", "September 1 – December 31", "Tuesday, January 18, 2028"],
])}
<p>Despite the name, the "quarters" aren't equal: the second covers only two months and the fourth covers four. (See all the year's business dates in our <a href="{P}blog/2027-business-tax-deadlines/">2027 deadline calendar</a>.)</p>

<h2>How much to pay: the safe harbor rules</h2>
<p>You avoid the underpayment penalty if your withholding and estimated payments, paid on time, add up to at least the <strong>smaller</strong> of:</p>
<ul>
<li><strong>90% of this year's tax</strong>, or</li>
<li><strong>100% of last year's tax</strong>, or <strong>110%</strong> if last year's adjusted gross income was over $150,000 ($75,000 if married filing separately)</li>
</ul>
<p>The prior-year rule is the easiest to plan around. Take last year's total tax, divide it by four, and pay that each quarter. Even if your income jumps, you won't owe a penalty, though you'll still owe the difference when you file.</p>

{callout(P, "business-tax-returns", "We'll calculate your quarterly payments when we prepare your return, so you know exactly what to pay and when.")}

<h2>What happens if you underpay</h2>
<p>If you pay too little or too late, the IRS charges an underpayment penalty, figured on Form 2210. It works like interest: it's based on how much was short and for how long, at the IRS underpayment rate. Catching up with a bigger payment later in the year reduces the penalty from that point on.</p>
<p>If your income is uneven, such as a business that earns most of its money late in the year, the <strong>annualized income method</strong> can lower or eliminate the penalty for earlier quarters.</p>

<h2>A tip for S-Corp owners and side-gig workers</h2>
<p>Federal income tax <strong>withholding</strong> is treated as if it were paid evenly throughout the year, no matter when it was actually withheld. So if you're behind on estimates, raising the withholding on your S-Corp salary, or on a W-2 job, late in the year can fill the gap and avoid the penalty in a way a late estimated payment can't.</p>

<h2>How to pay</h2>
<ul>
<li><strong>IRS Direct Pay</strong>, free from your bank account at irs.gov</li>
<li>Your <strong>IRS Online Account</strong>, where you can also see payments you've already made</li>
<li><strong>EFTPS</strong>, the Treasury's free electronic payment system</li>
<li>Debit or credit card, through approved processors that charge a fee</li>
<li>A check with a Form 1040-ES payment voucher</li>
</ul>

<h2>Don't forget your state</h2>
<p>Most states with an income tax, including Connecticut, have their own estimated payment requirements. Connecticut residents use Form CT-1040ES.</p>''',
     "Want Your Quarterly Payments Figured Out?", "Tell us about your income. We'll reply within 24 hours and help you set up a payment plan that keeps you penalty-free.")

post("irs-notice-what-to-do",
     "Got a Letter From the IRS? What Common Notices Mean & What to Do | Max Return Taxes",
     "Got a Letter From the IRS? What It Means and What to Do",
     "What common IRS notices like the CP2000, CP14, CP59, CP504 and final notice of intent to levy mean, how to respond, deadlines that matter, and how to spot scams.",
     "IRS Notices", "late-tax-returns",
     "How to read the notice number, which letters are urgent, and the deadlines you really can't miss.",
     f'''<p>An envelope from the IRS is enough to ruin anyone's day. But most IRS letters are routine, and almost all of them can be resolved if you respond on time. The worst thing you can do is put it in a drawer.</p>

<h2>Step 1: Make sure it's real</h2>
<p>The IRS generally starts contact <strong>by mail</strong>. It doesn't open conversations by text message, email or social media, and it never demands payment by gift card, cryptocurrency or wire transfer. If you're unsure whether a letter is real, don't call the number on the letter. Look up the IRS's contact information on irs.gov, or check for the notice in your IRS Online Account.</p>

<h2>Step 2: Find the notice number and the deadline</h2>
<p>Look in the top or bottom right corner for a code like <strong>CP2000</strong> or <strong>LT11</strong>. That number tells you exactly what kind of letter it is. Then find the response date. Many deadlines are firm, and missing one can cost you rights you can't get back.</p>

<h2>Common notices and what they mean</h2>
{table(["Notice", "What it means", "What to do"], [
    ["CP2000", "Income reported to the IRS doesn't match your return, so the IRS is proposing a change. It's not a bill yet.", "Agree, or disagree with documents, by the response date"],
    ["CP14", "You have a balance due.", "Pay, or set up a payment plan if you can't pay in full"],
    ["CP59", "The IRS has no record of a return it expected from you.", "File the return, or show that you already filed or didn't need to"],
    ["CP501 / CP503", "Reminders that a balance is still unpaid.", "Pay or arrange a plan before it escalates"],
    ["CP504", "Notice of intent to levy. The IRS can take your state tax refund and move toward other collection.", "Act now: pay, set up a plan or get help"],
    ["LT11 / Letter 1058", "Final notice of intent to levy, with your right to a hearing.", "You generally have 30 days to request a Collection Due Process hearing"],
    ["Notice of Deficiency", "The IRS's formal determination that you owe more tax.", "You generally have 90 days to petition the U.S. Tax Court, a deadline that can't be extended"],
])}

{callout(P, "late-tax-returns", "Got a notice about unfiled returns or a balance due? Send it to us. We'll explain it in plain English and help you respond.")}

<h2>Step 3: Respond, even if you disagree</h2>
<ul>
<li><strong>If the IRS is right,</strong> pay what you can by the deadline. If you can't pay in full, ask for a payment plan. That stops more serious collection action.</li>
<li><strong>If the IRS is wrong,</strong> say so in writing with copies of supporting documents, not originals, by the response date. Proposed changes like a CP2000 are often reduced or dropped once the IRS sees the full picture, like the cost basis of stock you sold.</li>
<li><strong>If you need more time,</strong> contact the IRS before the deadline. Short extensions are often available for routine notices, but not for court deadlines.</li>
</ul>

<h2>Step 4: Keep a paper trail</h2>
<p>Keep a copy of the notice, everything you send back and proof of when you sent it, such as certified mail. Write down the date, name and ID number of anyone you speak with at the IRS.</p>

<h2>Notices about unfiled returns</h2>
<p>If a notice says the IRS has no record of a return, or that it prepared one for you, filing your own accurate return is usually the best response. A return the IRS prepares often leaves out deductions and credits you're entitled to. (Read <a href="{P}blog/havent-filed-taxes-in-years/">what happens when you haven't filed</a>.)</p>''',
     "Don't Face an IRS Letter Alone", "Send us a copy of your notice. We'll reply within 24 hours, explain what it means and walk you through your options.")

post("s-corp-reasonable-salary",
     "S-Corp Reasonable Salary: How Much Should You Pay Yourself? | Max Return Taxes",
     "S-Corp Reasonable Salary: How Much Should You Pay Yourself?",
     "How the IRS reasonable compensation rule works for S-Corp owners, factors that determine a reasonable salary, risks of paying too little, and how salary affects QBI and retirement.",
     "Business Taxes", "business-tax-returns",
     "Why a $0 salary is a red flag, what the IRS looks at, and how your salary ripples through the rest of your taxes.",
     f'''<p>The main tax benefit of an S-Corp is that profits paid out as distributions aren't subject to self-employment tax. Your salary is. So every S-Corp owner faces the same question: how much salary do I have to pay myself? The IRS's answer is "reasonable compensation," and getting it wrong can erase the benefit of the S-Corp.</p>

<h2>The rule</h2>
<p>If you're a shareholder who works in your S-Corp, the IRS expects you to pay yourself a <strong>reasonable salary</strong> through payroll, with taxes withheld, <strong>before</strong> taking distributions. Reasonable generally means roughly what the business would have to pay someone else to do the work you do.</p>
<p>There's no fixed formula or percentage in the tax code. You may have heard of a "60/40 rule," splitting profit 60% salary and 40% distributions. It's a rule of thumb, not an IRS rule, and it doesn't protect you if your salary is too low for the work you actually do.</p>

<h2>What the IRS looks at</h2>
<p>Factors the IRS and the courts have used include:</p>
<ul>
<li>Your <strong>training and experience</strong></li>
<li>Your <strong>duties and responsibilities</strong> in the business</li>
<li>The <strong>time and effort</strong> you put into the business</li>
<li>What <strong>comparable businesses pay</strong> for similar services</li>
<li>What the business pays <strong>non-owner employees</strong></li>
<li>The history of your <strong>salary compared with distributions</strong></li>
<li>How and when bonuses are paid</li>
</ul>

<h2>The risk of paying too little</h2>
<p>Paying yourself nothing, or a token salary while taking large distributions, is a classic audit red flag. If the IRS decides your salary was unreasonably low, it can <strong>reclassify distributions as wages</strong>. The business then owes the payroll taxes that should have been paid, plus penalties and interest.</p>
<p>There's also no need to overpay. Salary above what's reasonable just adds payroll taxes you didn't need to pay. The goal is a figure you can defend.</p>

{callout(P, "business-tax-returns", "We help S-Corp owners set a salary they can defend, and we prepare the 1120-S and K-1s that go with it.")}

<h2>How to set a salary you can defend</h2>
<ol>
<li><strong>List what you actually do.</strong> Many owners wear several hats, like manager, salesperson and technician. Each role has a market rate.</li>
<li><strong>Research comparable pay.</strong> Government wage data, such as the Bureau of Labor Statistics occupational surveys, and industry salary surveys are good starting points.</li>
<li><strong>Factor in time.</strong> A part-time owner can reasonably earn less than a full-time one.</li>
<li><strong>Write it down.</strong> Keep notes on how you arrived at the number and update them as the business changes.</li>
</ol>

<h2>How your salary affects the rest of your taxes</h2>
<ul>
<li><strong>Qualified business income (QBI) deduction.</strong> Your salary reduces the business income that qualifies for the deduction. At higher incomes, though, the deduction can be limited by the W-2 wages the business pays. A salary that's too low or too high can cost you here.</li>
<li><strong>Retirement contributions.</strong> Contributions to a Solo 401(k) or SEP for an S-Corp owner are based on <strong>W-2 salary</strong>, not distributions. A very low salary limits how much you can put away.</li>
<li><strong>Social Security.</strong> Your future Social Security benefit is based on earnings you paid Social Security tax on. Distributions don't count.</li>
</ul>

<h2>The bottom line</h2>
<p>A reasonable salary is part of the cost of having an S-Corp. Set it based on your real role and market pay, document why, and revisit it every year. (Still deciding whether an S-Corp is right for you? Read <a href="{P}blog/should-my-llc-elect-s-corp-status/">should your LLC elect S-Corp status</a>.)</p>''',
     "Not Sure What to Pay Yourself?", "Tell us about your role and your business's profit. We'll reply within 24 hours and help you find a defensible number.")

post("moving-in-or-out-of-connecticut-taxes",
     "Moving In or Out of Connecticut? How Part-Year Resident Taxes Work | Max Return Taxes",
     "Moving In or Out of Connecticut? How Your Taxes Work the Year You Move",
     "How Connecticut taxes part-year residents and nonresidents, which return to file, how income is split, credits for other states, and how to show you changed residency.",
     "Connecticut", "connecticut-tax-preparer",
     "Which Connecticut return to file, how your income gets split, and how to avoid paying two states on the same money.",
     f'''<p>Moving to or from Connecticut makes the year's taxes more complicated. You'll often need to file in two states, split your income between them, and make sure you're not taxed twice on the same money. Here's how it works.</p>

<h2>Which Connecticut return do you file?</h2>
{table(["Your situation", "Connecticut return"], [
    ["Lived in Connecticut all year", "Form CT-1040, resident return"],
    ["Moved into or out of Connecticut during the year", "Form CT-1040NR/PY, part-year resident return"],
    ["Lived elsewhere all year but had Connecticut income", "Form CT-1040NR/PY, nonresident return"],
])}

<h2>How a part-year resident's income is split</h2>
<p>As a part-year resident, Connecticut generally taxes:</p>
<ul>
<li><strong>All your income</strong> from the period you lived in Connecticut, wherever it came from, and</li>
<li><strong>Only Connecticut-source income</strong> from the period you lived elsewhere, such as wages for work done in Connecticut, Connecticut rental property, or a business operating in Connecticut</li>
</ul>
<p>Your other state will usually tax the rest the same way. Getting the split right, like which paychecks, bonuses, interest or capital gains fall into which period, is where most part-year mistakes happen.</p>

<h2>Avoiding double taxation</h2>
<p>When two states could tax the same income, the state where you live generally gives you a <strong>credit for tax paid to the other state</strong>. That's common for Connecticut residents who commute to work in New York. New York taxes the wages earned there as a nonresident, and Connecticut gives a credit on the resident return. The credit has limits, so you may still owe some tax to Connecticut, but it prevents paying full tax twice.</p>
<p>Remote work makes this trickier. Where your wages are taxed can depend on where you physically did the work and, in some cases, where your employer is located. New York and Connecticut in particular have rules that can surprise people. If you work remotely across state lines, it's worth having someone check.</p>

{callout(P, "connecticut-tax-preparer", "Moved in or out of Connecticut? We prepare part-year and nonresident returns for both states, and make sure you get credit for tax paid to the other state.")}

<h2>Changing your residency for real</h2>
<p>Your tax residency follows your <strong>domicile</strong>, your true, permanent home. It's not just your mailing address. If you leave Connecticut, especially for a state with no income tax, make sure the move is clear on paper:</p>
<ul>
<li>Get a driver's license and register your car in your new state</li>
<li>Register to vote in your new state</li>
<li>Update your address with banks, employers, doctors and the IRS</li>
<li>Keep records of your move date, lease or home purchase, and where you spend your time</li>
</ul>
<p>Keeping a home in Connecticut and spending a lot of time here can still make you a Connecticut resident for tax purposes. Under Connecticut's rules, that can happen even if you've technically moved.</p>

<h2>Don't forget the rest of the year's details</h2>
<ul>
<li><strong>Withholding:</strong> make sure your employer updates your state withholding when you move.</li>
<li><strong>Estimated payments:</strong> self-employed people may need to make estimated payments to both states for part of the year.</li>
<li><strong>Business owners:</strong> moving yourself doesn't move your business. A Connecticut business can still create Connecticut-source income after you leave.</li>
</ul>''',
     "Moving This Year?", "Tell us where you're moving from and to. We'll reply within 24 hours and help you file correctly in both states.")

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
