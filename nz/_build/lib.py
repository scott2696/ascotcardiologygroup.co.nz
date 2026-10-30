#!/usr/bin/env python3
"""Kiwi Casino Ledger: shared identity, components, schema and page shell.

Standard library only (Pillow for title pixel widths). Every page module builds
a body string and hands it to write(), which emits <slug>/index.html so every
public URL is clean (no .html) and every canonical is self-referencing.

Editorial rule built into the components: there is no outbound link to any
casino or bookmaker anywhere on the site. Operator rows link to our own review.
"""
import os, re, json, html, hashlib, datetime

BUILD = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BUILD)              # the /nz/ folder of the domain repo
DOMAIN_ROOT = os.path.dirname(ROOT)        # the domain repo root (group games live here)

# ---------------------------------------------------------------------------
# Identity
# ---------------------------------------------------------------------------
DOMAIN = "ascotcardiologygroup.co.nz"
# The guide lives in a sub-folder; the domain homepage is the group games hub.
BASE = "/nz"
SITE = f"https://{DOMAIN}{BASE}"
NAME = "Kiwi Casino Ledger"
SHORT = "Casino Ledger"
EMAIL = f"hello@{DOMAIN}"
EMAIL_EDITOR = f"editor@{DOMAIN}"
EMAIL_COMPLAINTS = f"complaints@{DOMAIN}"
PUBLISHED = "2026-10-08"

MONTH, YEAR = "October", "2026"
MY = f"{MONTH} {YEAR}"
CHECKED = "8 October 2026"
NEXT_CHECK = "8 November 2026"

UPDATED = "@@LASTMOD@@"
UPDATED_NZ = "@@LASTMOD_NZ@@"

# ---------------------------------------------------------------------------
# Operators, in the order supplied by the publisher.
# ---------------------------------------------------------------------------
OPS = json.load(open(os.path.join(BUILD, "operators.json")))
BY = {o["slug"]: o for o in OPS}
CASINOS = [o for o in OPS if o["casino"]]
SPORTS = [o for o in OPS if o["sports"]]
CRYPTO = [o for o in OPS if o["crypto"]]
BY_SCORE = sorted(OPS, key=lambda o: -o["rating"])


def pick(slugs, kind="casino"):
    want = set(slugs)
    bad = want - set(BY)
    if bad:
        raise KeyError(f"unknown operator slug(s): {sorted(bad)}")
    return [o for o in OPS if o["slug"] in want and o[kind]]


def review_url(op):
    return f"/casino-reviews/{op['slug']}/"


def safety_txt(op):
    return f'{op["safety"]:.1f}' if op["safety"] is not None else "No profile"


def nzd_txt(op):
    return {True: "Yes", False: "No", None: "Not confirmed"}[op["nzd"]]


def tp_txt(op, long=False):
    if op.get("tp_score") is not None:
        return f'{op["tp_score"]:.1f} ({op["tp_reviews"]} reviews)' if long else f'{op["tp_score"]:.1f}'
    if long:
        return op.get("tp_note") or "No profile found"
    return "Suspended" if "breach" in (op.get("tp_note") or "") else ("Removed" if "removed" in (op.get("tp_note") or "") else "None")


def limit_txt(op):
    """The weekly limit where published, else the first limit we have."""
    week = [x for x in op["limits"] if "week" in x]
    return week[0] if week else (op["limits"][0] if op["limits"] else "Not published")


# ---------------------------------------------------------------------------
# Authors. PLACEHOLDER PROFILES (see README): replace with the real people who
# write and check this site before it goes live. Bios state each person's job
# on this site only. No degrees, employers or years of experience are claimed.
# ---------------------------------------------------------------------------
AUTHORS = {
    "hana-mcallister": {
        "name": "Hana McAllister", "initials": "HM", "role": "Editor",
        "focus": "Rankings, scoring and editorial standards",
        "bio": ("Hana edits every ranking and review on Kiwi Casino Ledger. Hana checks that each score can be traced back "
                "to the public sources listed under it, that offers are quoted exactly as supplied or reported, and that "
                "every page says plainly what New Zealand law currently allows."),
        "owns": ["Homepage", "Casino reviews", "How we review"],
    },
    "tama-rewiti": {
        "name": "Tama Rewiti", "initials": "TR", "role": "Payments Writer",
        "focus": "NZD banking, withdrawal limits and crypto",
        "bio": ("Tama covers the money side: which casinos hold an NZD balance, what the published withdrawal limits are in "
                "dollars, which deposit methods work from a New Zealand bank, and what currency conversion costs. Tama "
                "reads the cashier terms so readers do not have to."),
        "owns": ["Payment methods", "Fast payout casinos", "Crypto casinos"],
    },
    "olivia-brandt": {
        "name": "Olivia Brandt", "initials": "OB", "role": "Games Writer",
        "focus": "Pokies, RTP, volatility and live dealer games",
        "bio": ("Olivia writes about the games themselves: how return to player works, why the same pokie can run at "
                "different RTP settings, how volatility changes a session, and how live dealer tables differ from the "
                "computer-run versions."),
        "owns": ["Online pokies", "High payout casinos", "Live casinos"],
    },
    "wiremu-salter": {
        "name": "Wiremu Salter", "initials": "WS", "role": "Law and Safety Writer",
        "focus": "NZ gambling law, DIA licensing, harm reduction",
        "bio": ("Wiremu writes the legal, tax and responsible gambling pages from primary sources: the Online Casino "
                "Gambling Act 2026, the Racing Industry Amendment Act 2025, the Gambling Act 2003, Inland Revenue guidance "
                "and the Department of Internal Affairs' published material. Wiremu also checks every legal claim on the site."),
        "owns": ["NZ online casino law", "Gambling winnings tax", "Responsible gambling"],
    },
    "jess-tuilagi": {
        "name": "Jess Tuilagi", "initials": "JT", "role": "Sport Writer",
        "focus": "Sports betting markets, odds and TAB NZ",
        "bio": ("Jess covers sports betting: how odds and bookmaker margins work, which markets matter for rugby, league, "
                "netball and cricket, and what the 2025 law change that gave TAB NZ the only legal online sports book "
                "means for New Zealand punters."),
        "owns": ["Online betting NZ", "Best sports betting sites"],
    },
}
AUTHOR_ORDER = list(AUTHORS)

# ---------------------------------------------------------------------------
# Navigation. About Us and Contact Us are in the main nav AND the footer.
# ---------------------------------------------------------------------------
NAV = [
    ("Casinos", "/", [
        ("Best online casino sites NZ", "/"),
        ("Online pokies NZ", "/online-pokies/"),
        ("New online casinos", "/new-online-casinos/"),
        ("High payout casinos", "/high-payout-casinos/"),
        ("Fast payout casinos", "/fast-payout-casinos/"),
        ("Live casinos", "/live-casinos/"),
        ("Crypto casinos", "/best-crypto-casinos/"),
    ]),
    ("Bonuses", "/online-casinos/bonuses/", [
        ("Casino bonuses explained", "/online-casinos/bonuses/"),
        ("No deposit bonuses", "/no-deposit-casinos/"),
    ]),
    ("Betting", "/online-betting/", [
        ("Online betting NZ", "/online-betting/"),
        ("Sports betting sites", "/best-sports-betting-sites/"),
    ]),
    ("Reviews", "/casino-reviews/", None),
    ("Guides", "/nz-online-casino-law/", [
        ("NZ online casino law", "/nz-online-casino-law/"),
        ("Payment methods", "/payment-methods/"),
        ("Tax on gambling winnings", "/gambling-winnings-tax-nz/"),
        ("How we review", "/how-we-review/"),
        ("Responsible gambling", "/responsible-gambling/"),
    ]),
    ("About Us", "/about/", None),
    ("Contact Us", "/contact/", None),
]

FOOTER = [
    ("Casino guides", [
        ("Best online casino sites NZ", "/"),
        ("Online pokies NZ", "/online-pokies/"),
        ("New online casinos", "/new-online-casinos/"),
        ("High payout casinos", "/high-payout-casinos/"),
        ("Fast payout casinos", "/fast-payout-casinos/"),
        ("Live casinos NZ", "/live-casinos/"),
        ("Crypto casinos NZ", "/best-crypto-casinos/"),
        ("Casino reviews", "/casino-reviews/"),
    ]),
    ("Bonuses, betting &amp; guides", [
        ("Casino bonuses explained", "/online-casinos/bonuses/"),
        ("No deposit bonuses", "/no-deposit-casinos/"),
        ("Online betting NZ", "/online-betting/"),
        ("Sports betting sites", "/best-sports-betting-sites/"),
        ("Payment methods", "/payment-methods/"),
        ("NZ online casino law", "/nz-online-casino-law/"),
        ("Gambling winnings tax", "/gambling-winnings-tax-nz/"),
    ]),
    ("Company", [
        ("About Us", "/about/"),
        ("Contact Us", "/contact/"),
        ("Authors", "/authors/"),
        ("How we review", "/how-we-review/"),
        ("Responsible Gambling", "/responsible-gambling/"),
    ]),
    ("Legal", [
        ("Terms and Conditions", "/terms/"),
        ("Privacy Policy", "/privacy/"),
        ("Cookie Policy", "/cookie-policy/"),
        ("Sitemap", "/sitemap.xml"),
    ]),
]

# ---------------------------------------------------------------------------
# Titles, descriptions, H1s. Each page targets a different variant of the head
# term so titles never compete. Formula: Primary [Month Year]: Secondary.
# Titles are budgeted at <= 580px (Arial 20px, measured with 'September').
# (primary, title secondary, h1 secondary, description)
# ---------------------------------------------------------------------------
PAGE_META = {
 "/": ("Best Online Casino Sites NZ", "Top Rated", "Real Money Casinos Checked on Licence, NZD Banking and Payout Limits",
   "Top online casinos in New Zealand rated for Kiwis: licences, real money NZD banking, payout limits and safety scores, plus which casinos must leave NZ on 1 December."),
 "/online-pokies/": ("Online Pokies NZ", "Real Money Pokies", "Best Pokies Sites, Real Money Slots, RTP and Jackpots Explained",
   "Real money pokies NZ guide: how pokie RTP and volatility work, Megaways, hold-and-win and progressive jackpots explained, and the pokies casinos Kiwis ask about most."),
 "/new-online-casinos/": ("New Online Casinos NZ", "Newest Casino Sites", "Best New Casino Sites, Dated by Licence and Checked Before You Join",
   "Newest online casino sites in NZ for 2026, dated by licence rather than launch hype, why no new casino may enter NZ under the 2026 Act, and what the DIA auction means."),
 "/high-payout-casinos/": ("Best Payout Casinos NZ", "Best Paying Casinos", "Highest RTP and High Payout Casinos, With the House Edge by Game",
   "Best paying online casinos for NZ players: the highest RTP games, house edge on blackjack, roulette and baccarat, and which casinos' withdrawal limits can pay a big win."),
 "/fast-payout-casinos/": ("Fastest Payout Casinos NZ", "Fast Cashouts", "Fast Withdrawal Casinos, Payout Limits and Why Cashouts Stall",
   "Fast withdrawal casinos for Kiwis: the quickest NZ casino payout methods, published NZD withdrawal limits, ID checks and why an 'instant withdrawal' casino still stalls."),
 "/best-crypto-casinos/": ("Best Crypto Casinos NZ", "Bitcoin &amp; USDT Sites", "Bitcoin, USDT and Ethereum Casinos, With Fees and Tax for Kiwis",
   "Bitcoin casino NZ guide: crypto casinos taking BTC, USDT and ETH, network fees, buying crypto on an NZ exchange, price risk and how IRD taxes crypto gains."),
 "/live-casinos/": ("Live Casino NZ", "Live Dealer Games", "Best Live Dealer Casinos for Blackjack, Roulette, Baccarat and Game Shows",
   "Live dealer casino NZ guide: live blackjack, live roulette, baccarat and game shows explained, with the house edge, table limits and the live casinos Kiwis ask about."),
 "/online-casinos/bonuses/": ("Best Casino Bonuses NZ", "Welcome Offers", "Sign Up and Welcome Bonuses, With the Real Cost of Wagering",
   "Casino welcome bonus NZ guide: wagering requirements worked through in NZD, max-bet rules, win caps, free spins, reloads and cashback, so you know the real cost first."),
 "/no-deposit-casinos/": ("No Deposit Bonus NZ", "No Deposit Free Spins", "Free Spins and No Deposit Offers, and the Win Caps Behind Them",
   "No deposit free spins and bonus cash for NZ players: how no deposit offers work, typical NZ$50 to NZ$100 max cashouts, wagering, and how to spot a fake bonus code."),
 "/online-betting/": ("Online Betting NZ", "Legal Betting Sites", "Racing and Sports Betting, TAB NZ and the Offshore Ban Explained",
   "Is online betting legal in NZ? TAB NZ and Betcha are the only legal betting sites. Rugby, racing and sports betting odds, margins, bet types and safer betting tools."),
 "/best-sports-betting-sites/": ("Best Sports Betting Sites NZ", "Bookmakers", "Top Bookies Compared on Licence, Limits and the 2025 Law",
   "Best betting sites NZ punters search for: TAB NZ against offshore bookmakers on licence, NZD banking, limits and odds, and what the 2025 offshore betting ban changed."),
 "/casino-reviews/": ("Online Casino Reviews NZ", "Trusted or Not?", "17 Casinos and Betting Sites Rated on Licence, Owner and Limits",
   "Honest NZ casino reviews: 17 online casinos and betting sites checked on licence, owner, NZD banking, withdrawal limits and safety, and whether each can be trusted."),
 "/payment-methods/": ("Casino Payment Methods NZ", "NZD Deposits", "Deposits and Withdrawals by Card, E-Wallet, Bank Transfer and Crypto",
   "Online casino deposit and withdrawal methods in NZ: Visa, Mastercard, Apple Pay, Skrill, Neosurf, POLi, bank transfer and crypto, NZD conversion fees and bank blocks."),
 "/nz-online-casino-law/": ("Is Online Gambling Legal in NZ", "Licences", "The Online Casino Gambling Act 2026 in Plain English",
   "Online casino law NZ: the Online Casino Gambling Act 2026, who won the DIA licence auction, the NZ$5m advertising ban and what the 1 December 2026 cut-off means for you."),
 "/gambling-winnings-tax-nz/": ("Gambling Winnings Tax NZ", "IRD Rules", "Is Gambling Taxed on Casino, Betting and Lotto Wins?",
   "Are gambling winnings taxable in NZ? IRD treats casual casino, pokies, betting and Lotto wins as tax-free, but professional gambling and crypto gains can be taxed."),
 "/how-we-review/": ("How We Rate Online Casinos", "Ledger Score", "Our Review Method, the Ledger Score and Our Sources",
   "How we rate online casinos in NZ: the five weighted inputs in the Ledger score (safety, licence, owner, terms, banking), our public sources and how often we recheck."),
 "/responsible-gambling/": ("Responsible Gambling NZ", "Gambling Helpline", "Free Help, Tools, Bank Blocks and Self-Exclusion",
   "Problem gambling help in NZ: the Gambling Helpline on 0800 654 655 (free, 24/7), bank gambling blocks, deposit limits, self-exclusion and the warning signs to watch for."),
 "/about/": ("About Kiwi Casino Ledger", "Who We Are", "Who We Are and Why There Are No Casino Links Here",
   "About Kiwi Casino Ledger: who we are, why we publish no casino links or sign-up offers, how we choose what to cover and the editorial standards behind every page."),
 "/contact/": ("Contact Kiwi Casino Ledger", "Get in Touch", "Corrections, Complaints and Questions",
   "Contact Kiwi Casino Ledger for corrections, questions about a casino we cover, privacy requests or media enquiries. We aim to reply within two working days."),
 "/authors/": ("Our Writers and Editors", "Kiwi Casino Ledger", "Who Writes and Checks Every Page",
   "Meet the writers and editors behind Kiwi Casino Ledger: who covers casinos, payments, games, law and betting, and which pages each person is responsible for."),
 "/terms/": ("Terms and Conditions", "Kiwi Casino Ledger", "The Rules for Using This Site",
   "The terms and conditions for using Kiwi Casino Ledger: who the site is for, accuracy of information, no casino links, liability, copyright and the law that applies."),
 "/privacy/": ("Privacy Policy", "NZ Privacy Act 2020", "How We Handle Personal Information",
   "How Kiwi Casino Ledger collects, uses, stores and protects personal information under the New Zealand Privacy Act 2020, and how to access or correct what we hold."),
 "/cookie-policy/": ("Cookie Policy", "Kiwi Casino Ledger", "The Cookies We Use and How to Control Them",
   "Which cookies Kiwi Casino Ledger sets, why there are no affiliate or advertising cookies here, and how to block or delete cookies in every major browser."),
}

DATE = f"[{MY}]"
META = {p: (f"{a} {DATE}: {b}", d, f"{a} {DATE}: {h}") for p, (a, b, h, d) in PAGE_META.items()}
PRIMARY = {p: v[0] for p, v in PAGE_META.items()}
PAGE_EXTRA = {}       # review pages register their meta here

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def esc(s):
    return html.escape(str(s), quote=False)


def attr(s):
    return html.escape(str(s), quote=True)


def strip_tags(s):
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


_ARIAL = None


def px(s):
    global _ARIAL
    if _ARIAL is None:
        from PIL import ImageFont
        for f in ("/System/Library/Fonts/Supplemental/Arial.ttf", "/Library/Fonts/Arial.ttf"):
            if os.path.exists(f):
                _ARIAL = ImageFont.truetype(f, 20)
                break
    return round(_ARIAL.getlength(html.unescape(s)))


def stamp(h1):
    return re.sub(r"\[([^\]]+)\]", r'<span class="h1-date">[\1]</span>', h1, count=1)


# ---------------------------------------------------------------------------
# Components
# ---------------------------------------------------------------------------
def byline(author, checker=None):
    a = AUTHORS[author]
    out = [f'<div class="byline"><span class="av" aria-hidden="true">{a["initials"]}</span><div>',
           f'<span>Written by <a href="/authors/#{author}"><b>{a["name"]}</b></a>, {a["role"]}</span>']
    if checker:
        c = AUTHORS[checker]
        out.append(f'<span>Checked by <a href="/authors/#{checker}">{c["name"]}</a></span>')
    out.append(f'<span>Updated <time datetime="{UPDATED}">{UPDATED_NZ}</time></span>')
    out.append("</div></div>")
    return "".join(out)


def hero(h1, lead, author=None, checker=None, facts=None, kicker=None):
    k = f'<p class="kicker">{kicker}</p>' if kicker else ""
    f = ""
    if facts:
        f = '<ul class="hero-facts">' + "".join(f"<li><b>{b}</b><span>{s}</span></li>" for b, s in facts) + "</ul>"
    b = byline(author, checker) if author else ""
    return (f'<header class="hero"><div class="wrap">{k}<h1>{stamp(h1)}</h1>'
            f'<p class="lead">{lead}</p>{b}{f}</div></header>')


def crumbs(trail):
    items = [("Home", "/")] + trail
    li = []
    for i, (label, u) in enumerate(items):
        if i == len(items) - 1:
            li.append(f'<li aria-current="page">{label}</li>')
        else:
            li.append(f'<li><a href="{u}">{label}</a></li>')
    return f'<nav class="crumbs" aria-label="Breadcrumb"><div class="wrap"><ol>{"".join(li)}</ol></div></nav>'


def toc(items):
    li = "".join(f'<li><a href="#{i}">{l}</a></li>' for l, i in items)
    return f'<nav class="toc" aria-label="On this page"><p class="toc-h">On this page</p><ol>{li}</ol></nav>'


def note(body, kind="info", title=None):
    t = f'<p class="note-t">{title}</p>' if title else ""
    return f'<div class="note note--{kind}">{t}{body}</div>'


def table(headers, rows, caption=None, cls=""):
    th = "".join(f'<th scope="col">{h}</th>' for h in headers)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    cap = f"<caption>{caption}</caption>" if caption else ""
    return f'<figure class="tw {cls}"><table>{cap}<thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>'


def logo_img(op, w=140, h=70, eager=False):
    dark = " logo--dark" if op.get("logo_dark") else ""
    return (f'<img class="logo{dark}" src="{op["logo"]}" alt="{attr(op["name"])} logo" width="{w}" height="{h}" '
            f'loading="{"eager" if eager else "lazy"}">')


def op_cell(op):
    return (f'<span class="opc"><span class="opc-l{" logo--dark" if op.get("logo_dark") else ""}">'
            f'<img src="{op["logo"]}" alt="" width="44" height="28" loading="lazy"></span>'
            f'<a href="{review_url(op)}">{esc(op["name"])}</a></span>')


def proscons(pros, cons):
    p = "".join(f"<li>{x}</li>" for x in pros)
    c = "".join(f"<li>{x}</li>" for x in cons)
    return (f'<div class="pc"><div class="pc-p"><p class="pc-h">Strengths</p><ul>{p}</ul></div>'
            f'<div class="pc-c"><p class="pc-h">Watch out for</p><ul>{c}</ul></div></div>')


def cards(items, cols=3):
    out = [f'<div class="grid g{cols}">']
    for it in items:
        t, body = it[0], it[1]
        href = it[2] if len(it) > 2 else None
        if href:
            out.append(f'<a class="card" href="{href}"><h3>{t}</h3><p>{body}</p><span class="more">Read the guide</span></a>')
        else:
            out.append(f'<div class="card"><h3>{t}</h3><p>{body}</p></div>')
    out.append("</div>")
    return "".join(out)


def steps(items):
    li = "".join(f"<li><h3>{t}</h3><p>{b}</p></li>" for t, b in items)
    return f'<ol class="steps">{li}</ol>'


def faq(items, heading="Frequently asked questions", ident="faq"):
    """Returns (html, schema entities) so markup and FAQPage schema never drift."""
    out = [f'<h2 id="{ident}">{heading}</h2><div class="faq">']
    ents = []
    for q, a in items:
        out.append(f'<details><summary><h3>{q}</h3></summary><div class="faq-a">{a}</div></details>')
        ents.append({"@type": "Question", "name": strip_tags(q),
                     "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}})
    out.append("</div>")
    return "".join(out), ents


def authorbox(key):
    a = AUTHORS[key]
    return (f'<aside class="abox"><span class="av av--lg" aria-hidden="true">{a["initials"]}</span><div>'
            f'<p class="abox-n"><a href="/authors/#{key}">{a["name"]}</a></p>'
            f'<p class="abox-r">{a["role"]} &middot; {a["focus"]}</p><p>{a["bio"]}</p>'
            f'<p class="abox-m"><a href="/how-we-review/">How we review</a> &middot; <a href="/authors/">All authors</a></p></div></aside>')


def scorebars(parts):
    labels = [("safety", "Independent safety"), ("licence", "Licence"), ("owner", "Ownership"),
              ("terms", "Terms and limits"), ("banking", "Banking for Kiwis")]
    out = ['<div class="bars">']
    for k, label in labels:
        v = parts[k]
        out.append(f'<div class="bar"><span>{label}</span><span class="trk"><i style="width:{round(v*10)}%"></i></span><b>{v:.1f}</b></div>')
    out.append("</div>")
    return "".join(out)


def barchart(rows, unit="", caption=None, maxv=None, cls="", suffix=""):
    """Accessible horizontal bar chart: a real table for screen readers and
    the export, styled as bars. rows = [(label, value, note)]."""
    maxv = maxv or max(v for _, v, *_ in rows) or 1
    out = [f'<figure class="chart {cls}"><table><tbody>']
    for r in rows:
        label, v = r[0], r[1]
        nt = f'<small>{r[2]}</small>' if len(r) > 2 and r[2] else ""
        out.append(f'<tr><th scope="row">{label}{nt}</th><td><span class="cb"><i style="width:{max(2, round(100 * v / maxv))}%"></i></span>'
                   f'<b>{unit}{v:,}{suffix}</b></td></tr>' if isinstance(v, int) else
                   f'<tr><th scope="row">{label}{nt}</th><td><span class="cb"><i style="width:{max(2, round(100 * v / maxv))}%"></i></span>'
                   f'<b>{v}{unit}</b></td></tr>')
    out.append("</tbody></table>")
    if caption:
        out.append(f"<figcaption>{caption}</figcaption>")
    out.append("</figure>")
    return "".join(out)


def rg_line():
    return ('<p class="rg">R18. Gambling can cause harm. Free, confidential help 24/7: Gambling Helpline '
            '<a href="tel:0800654655">0800 654 655</a> or text 8006. '
            '<a href="/responsible-gambling/">Tools and support</a>.</p>')


def law_note():
    return note('<p>The casinos and bookmakers on this site are licensed overseas, not by New Zealand\'s Department of Internal '
                'Affairs. Under the <a href="/nz-online-casino-law/">Online Casino Gambling Act 2026</a> it is unlawful to advertise '
                'unlicensed online casino gambling to people in New Zealand, so we publish no links to these sites and no sign-up '
                'offers on their behalf. From 1 December 2026, casinos that have not applied for a New Zealand licence must stop '
                'serving New Zealand players, and none of the companies behind these casinos won a place in the DIA\'s October 2026 licence auction. This page is information, not a recommendation to gamble.</p>',
                "law", "The legal position, in short")


ORDER_NOTE = ('<p class="tl-note"><b>About this list.</b> Sites are shown in the order set by our editor, which is not the '
              'score order. The <b>Ledger score</b> comes from five published inputs and is the number to compare; '
              '<a href="/casino-reviews/#by-score">see every site sorted by score</a>. We do not link to any casino '
              'or carry sign-up offers. <a href="/how-we-review/">How we score</a>.</p>')


def badge(op):
    if op["rating"] >= 8:
        return '<span class="tag tag--good">Strong public record</span>'
    if op["rating"] < 5.5:
        return '<span class="tag tag--warn">Caution</span>'
    return ""


def toplist(ops, kind="casino", start=1, note_=True, eager=2):
    """The ranked list. Every row is a set of checkable facts and a link to our
    own review. There is no outbound link."""
    out = [f'<ol class="tl" start="{start}">']
    for i, op in enumerate(ops, start):
        facts = [("Licence", op["licence_short"]), ("NZD balance", nzd_txt(op)),
                 ("Withdrawal limit", limit_txt(op)), ("Safety Index", safety_txt(op))]
        fl = "".join(f"<li><span>{k}</span><b>{esc(v)}</b></li>" for k, v in facts)
        chips = []
        if op["casino"]:
            chips.append('<span class="chip">Casino</span>')
        if op["sports"]:
            chips.append('<span class="chip">Sportsbook</span>')
        if op["crypto"]:
            chips.append('<span class="chip">Crypto</span>')
        for fl_ in op["flags"][:2]:
            chips.append(f'<span class="chip chip--warn">{esc(fl_)}</span>')
        offer = (f'<p class="tl-offer"><span>Offer on record:</span> {esc(op["offer"])}</p>' if op.get("offer") else "")
        out.append(
            f'<li class="tl-row">'
            f'<div class="tl-rank" aria-hidden="true">{i}</div>'
            f'<div class="tl-logo{" logo--dark" if op.get("logo_dark") else ""}">{logo_img(op, eager=(i - start) < eager)}</div>'
            f'<div class="tl-main"><div class="tl-head"><h3 class="tl-name"><a href="{review_url(op)}">{esc(op["name"])}</a></h3>{badge(op)}</div>'
            f'<p class="tl-why">{op["tagline"]}</p>{offer}'
            f'<ul class="tl-facts">{fl}</ul><div class="tl-chips">{"".join(chips)}</div></div>'
            f'<div class="tl-side"><p class="tl-score"><b>{op["rating"]:.1f}</b><span>Ledger score</span></p>'
            f'<a class="btn" href="{review_url(op)}">Read the review</a>'
            f'<p class="tl-tc">Facts checked {CHECKED}</p></div></li>')
    out.append("</ol>")
    if note_:
        out.append(ORDER_NOTE)
    return "".join(out)


def compare(ops, cols=None, caption=None):
    cols = cols or ["licence", "owner", "nzd", "limit", "safety", "score"]
    heads = {"licence": "Licence", "owner": "Owner", "nzd": "NZD balance", "limit": "Withdrawal limit",
             "safety": "Safety Index*", "score": "Ledger score", "pay": "Payment options", "cap": "Daily win cap",
             "crypto": "Crypto", "offer": "Offer on record", "lyear": "Licence issued", "products": "Products", "tp": "Trustpilot"}
    get = {"licence": lambda o: esc(o["licence_short"]), "owner": lambda o: esc(o["owner"]),
           "nzd": lambda o: nzd_txt(o), "limit": lambda o: esc(limit_txt(o)), "safety": lambda o: safety_txt(o),
           "score": lambda o: f'<b>{o["rating"]:.1f}</b>', "pay": lambda o: str(o["n_pay"] or "n/a"),
           "cap": lambda o: esc(o["win_cap"] or "None published"), "crypto": lambda o: "Yes" if o["crypto"] else "No",
           "offer": lambda o: esc(o["offer"] or "None on record"),
           "lyear": lambda o: str(o["licence_year"] or "Not confirmed"), "tp": lambda o: tp_txt(o),
           "products": lambda o: " + ".join(x for x, f in (("Casino", o["casino"]), ("Sport", o["sports"])) if f)}
    rows = [[op_cell(o)] + [get[c](o) for c in cols] for o in ops]
    cap = caption or ("*Casino Guru Safety Index, read " + CHECKED + ". Ledger score: our five-input score.")
    return table(["Site"] + [heads[c] for c in cols], rows, caption=cap, cls="tw--cmp")


# ---------------------------------------------------------------------------
# Schema. Organization + WebSite on every page; page entities appended.
# ---------------------------------------------------------------------------
def schema_org():
    return {"@type": "Organization", "@id": f"{SITE}/#org", "name": NAME, "url": SITE + "/",
            "logo": {"@type": "ImageObject", "url": f"{SITE}/favicon-192x192.png", "width": 192, "height": 192},
            "email": EMAIL, "areaServed": {"@type": "Country", "name": "New Zealand"},
            "publishingPrinciples": f"{SITE}/how-we-review/", "ethicsPolicy": f"{SITE}/about/#standards",
            "correctionsPolicy": f"{SITE}/contact/#corrections",
            "contactPoint": {"@type": "ContactPoint", "contactType": "editorial", "email": EMAIL_EDITOR,
                             "areaServed": "NZ", "availableLanguage": "en-NZ"}}


def schema_site():
    return {"@type": "WebSite", "@id": f"{SITE}/#website", "url": SITE + "/", "name": NAME,
            "inLanguage": "en-NZ", "publisher": {"@id": f"{SITE}/#org"}}


def schema_person(key):
    a = AUTHORS[key]
    return {"@type": "Person", "@id": f"{SITE}/authors/#{key}", "name": a["name"],
            "jobTitle": strip_tags(a["role"]), "description": strip_tags(a["bio"]),
            "knowsAbout": strip_tags(a["focus"]), "worksFor": {"@id": f"{SITE}/#org"},
            "url": f"{SITE}/authors/#{key}"}


def schema_crumbs(path, trail):
    items = [("Home", "/")] + trail
    return {"@type": "BreadcrumbList", "@id": f"{SITE}{path}#crumbs",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": strip_tags(n),
                                 "item": f"{SITE}{u}"} for i, (n, u) in enumerate(items)]}


def _meta(path):
    return META[path] if path in META else PAGE_EXTRA[path]


def schema_webpage(path, kind="WebPage"):
    t, d = _meta(path)[:2]
    return {"@type": kind, "@id": f"{SITE}{path}#webpage", "url": f"{SITE}{path}",
            "name": strip_tags(t), "description": strip_tags(d), "inLanguage": "en-NZ",
            "isPartOf": {"@id": f"{SITE}/#website"}, "datePublished": PUBLISHED,
            "dateModified": UPDATED, "breadcrumb": {"@id": f"{SITE}{path}#crumbs"}}


def schema_article(path, headline, author, checker=None):
    a = {"@type": "Article", "@id": f"{SITE}{path}#article", "headline": strip_tags(headline)[:110],
         "inLanguage": "en-NZ", "mainEntityOfPage": {"@id": f"{SITE}{path}#webpage"},
         "datePublished": PUBLISHED, "dateModified": UPDATED,
         "author": {"@id": f"{SITE}/authors/#{author}"}, "publisher": {"@id": f"{SITE}/#org"},
         "image": f"{SITE}/images/og.png"}
    if checker:
        a["reviewedBy"] = {"@id": f"{SITE}/authors/#{checker}"}
    return a


def schema_itemlist(path, ops, name):
    return {"@type": "ItemList", "@id": f"{SITE}{path}#list", "name": name,
            "numberOfItems": len(ops), "itemListOrder": "https://schema.org/ItemListUnordered",
            "itemListElement": [{"@type": "ListItem", "position": i, "name": o["name"],
                                 "url": f"{SITE}{review_url(o)}"} for i, o in enumerate(ops, 1)]}


def schema_review(op, author):
    return {"@type": "Review", "@id": f"{SITE}{review_url(op)}#review",
            "itemReviewed": {"@type": "Organization", "name": op["name"], "image": SITE + op["logo"]},
            "reviewRating": {"@type": "Rating", "ratingValue": op["rating"], "bestRating": 10, "worstRating": 0},
            "author": {"@id": f"{SITE}/authors/#{author}"}, "publisher": {"@id": f"{SITE}/#org"},
            "datePublished": PUBLISHED, "dateModified": UPDATED,
            "reviewBody": strip_tags(op["verdict"])[:500], "inLanguage": "en-NZ"}


def schema_faq(path, ents):
    return {"@type": "FAQPage", "@id": f"{SITE}{path}#faq", "mainEntity": ents}


def schema_howto(path, name, items):
    return {"@type": "HowTo", "@id": f"{SITE}{path}#howto", "name": name,
            "step": [{"@type": "HowToStep", "position": i, "name": strip_tags(t), "text": strip_tags(b)}
                     for i, (t, b) in enumerate(items, 1)]}


# ---------------------------------------------------------------------------
# Shell
# ---------------------------------------------------------------------------
BRAND_MARK = ('<svg class="mark" viewBox="0 0 48 48" width="36" height="36" aria-hidden="true">'
              '<rect x="1" y="1" width="46" height="46" rx="11" fill="#0F3B30"/>'
              '<rect x="11" y="12" width="26" height="4" rx="2" fill="#F2C14E"/>'
              '<rect x="11" y="22" width="18" height="4" rx="2" fill="#F2C14E" opacity=".75"/>'
              '<rect x="11" y="32" width="11" height="4" rx="2" fill="#F2C14E" opacity=".5"/>'
              '<path d="M27 33.5l4 4 7.5-9" fill="none" stroke="#7FD6B5" stroke-width="3.4" '
              'stroke-linecap="round" stroke-linejoin="round"/></svg>')


def _nav(path):
    out = []
    for label, href, sub in NAV:
        cur = ' aria-current="page"' if href == path else ""
        if not sub:
            out.append(f'<li><a class="nl" href="{href}"{cur}>{label}</a></li>')
            continue
        ac = ' aria-current="page"'
        items = "".join(f'<li><a href="{u}"{ac if u == path else ""}>{l}</a></li>' for l, u in sub)
        out.append(f'<li class="has"><a class="nl" href="{href}"{cur}>{label}</a><ul class="drop">{items}</ul></li>')
    return "".join(out)


def _mobile():
    cols = []
    for label, href, sub in NAV:
        links = sub or [(label, href)]
        cols.append(f'<div><p>{label}</p><ul>' + "".join(f'<li><a href="{u}">{l}</a></li>' for l, u in links) + "</ul></div>")
    return ('<details class="mnav"><summary aria-label="Open menu"><span class="burger" aria-hidden="true"></span>'
            f'<span>Menu</span></summary><div class="mnav-p">{"".join(cols)}</div></details>')


def _footer():
    cols = "".join(f'<div class="fcol"><p class="fh">{t}</p><ul>' +
                   "".join(f'<li><a href="{u}">{l}</a></li>' for l, u in links) + "</ul></div>"
                   for t, links in FOOTER)
    return f"""<footer class="foot"><div class="wrap">
<div class="foot-top">
<div class="fabout"><a class="brand brand--foot" href="/">{BRAND_MARK}<span>Kiwi Casino <em>Ledger</em></span></a>
<p>An independent record of the online casino and betting sites New Zealanders ask about. Every fact is sourced and
dated. We publish no casino links, carry no sign-up offers and say plainly what the law allows.</p>
<p class="fbadges"><span>R18</span><span>No casino links</span><span>Sources on every review</span></p></div>
{cols}
</div>
<div class="foot-legal">
<p><b>R18. Gambling can cause harm.</b> Treat it as entertainment you pay for, never as income. If gambling is
affecting you or your whānau, call the Gambling Helpline on <a href="tel:0800654655">0800 654 655</a>, text 8006, or see
<a href="/responsible-gambling/">responsible gambling</a>. Free, confidential, 24/7.</p>
<p><b>No advertising.</b> {NAME} does not link to, take referrals for, or publish offers on behalf of any online
casino or bookmaker. The operators covered here are licensed offshore, not by the Department of Internal Affairs.
Advertising unlicensed online casino gambling in New Zealand has been unlawful since 1 May 2026, and TAB NZ is the
only lawful online bookmaker. See <a href="/nz-online-casino-law/">NZ online casino law</a>.</p>
</div>
<div class="foot-bot"><span>&copy; {YEAR} {NAME}</span>
<span><a href="/about/">About Us</a> &middot; <a href="/contact/">Contact Us</a> &middot; <a href="/authors/">Authors</a> &middot;
<a href="/terms/">Terms and Conditions</a> &middot; <a href="/privacy/">Privacy Policy</a> &middot; <a href="/cookie-policy/">Cookie Policy</a> &middot;
<a href="/responsible-gambling/">Responsible Gambling</a> &middot; <a href="/sitemap.xml">Sitemap</a></span></div>
</div></footer>"""


def page(path, body, schema=None):
    t, d = _meta(path)[:2]
    canon = f"{SITE}{path}"
    graph = [schema_org(), schema_site()] + (schema or [])
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, separators=(",", ":"), ensure_ascii=False)
    tt, dd = attr(strip_tags(t)), attr(strip_tags(d))
    return f"""<!doctype html>
<html lang="en-NZ">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{tt}</title>
<meta name="description" content="{dd}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<meta name="theme-color" content="#0F3B30">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME}">
<meta property="og:locale" content="en_NZ">
<meta property="og:title" content="{tt}">
<meta property="og:description" content="{dd}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/images/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">
<link rel="icon" type="image/png" sizes="144x144" href="/favicon-144x144.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192x192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,650&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/site.css?v={CSS_V}">
<script type="application/ld+json">{ld}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="strip"><div class="wrap"><span><b>R18</b> &middot; Gambling can cause harm. Free help 24/7:
<a href="tel:0800654655">0800 654 655</a></span><span class="strip-r">Independent &middot; No casino links &middot;
<a href="/about/#standards">Our standards</a></span></div></div>
<header class="hdr"><div class="wrap hdr-in">
<a class="brand" href="/" aria-label="{NAME} home">{BRAND_MARK}<span>Kiwi Casino <em>Ledger</em></span></a>
<nav class="nav" aria-label="Main"><ul>{_nav(path)}</ul></nav>
{_mobile()}
</div></header>
<main id="main">
{body}
</main>
{_footer()}
</body>
</html>
"""


try:
    CSS_V = hashlib.sha256(open(os.path.join(ROOT, "assets", "css", "site.css"), "rb").read()).hexdigest()[:8]
except OSError:
    CSS_V = "1"

# ---------------------------------------------------------------------------
# Writer. lastmod follows a content hash so sitemap dates mean something.
# ---------------------------------------------------------------------------
_LM = os.path.join(BUILD, "lastmod.json")
try:
    LASTMOD = json.load(open(_LM))
except Exception:
    LASTMOD = {}
TODAY = datetime.date.today().isoformat()
_MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August",
           "September", "October", "November", "December"]
PAGES = []
SOURCES = {}


def nzdate(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{d} {_MONTHS[m-1]} {y}"


def write(path, body, schema=None, priority=0.7, freq="monthly", author=None):
    doc = page(path, body, schema)
    h = hashlib.sha256(doc.replace(UPDATED, "").replace(UPDATED_NZ, "").encode()).hexdigest()[:16]
    rec = LASTMOD.get(path)
    if not rec or rec.get("hash") != h:
        rec = {"hash": h, "date": TODAY}
        LASTMOD[path] = rec
    doc = doc.replace(UPDATED_NZ, nzdate(rec["date"])).replace(UPDATED, rec["date"])
    # Pages are written with site-relative links; prefix every one with BASE.
    doc = re.sub(r'(\s(?:href|src|action)=")/(?!/)', r"\1" + BASE + "/", doc)
    out = os.path.join(ROOT, "index.html") if path == "/" else os.path.join(ROOT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(doc)
    PAGES.append((path, rec["date"], priority, freq))
    SOURCES[path] = (author, body.replace(UPDATED_NZ, nzdate(rec["date"])).replace(UPDATED, rec["date"]))
    return path


def save_lastmod():
    json.dump(LASTMOD, open(_LM, "w"), indent=1, sort_keys=True)


# ---------------------------------------------------------------------------
# Landing template shared by every category page, so all of them follow the
# homepage layout: hero > breadcrumb > law note > list > comparison > guide >
# FAQ > related guides > author box.
# ---------------------------------------------------------------------------
RELATED = [
    ("Best online casino sites NZ", "All 17 sites in one list, with licence, NZD banking and limits side by side.", "/"),
    ("NZ online casino law", "The 2026 Act, the advertising ban and the 1 December cut-off, explained.", "/nz-online-casino-law/"),
    ("Online pokies NZ", "RTP, variable RTP settings, volatility and jackpots, in plain English.", "/online-pokies/"),
    ("Fast payout casinos", "Published withdrawal limits in NZD and why cashouts stall.", "/fast-payout-casinos/"),
    ("Casino bonuses explained", "How wagering really works, with worked examples in dollars.", "/online-casinos/bonuses/"),
    ("Payment methods", "Cards, e-wallets, bank transfer, vouchers and crypto from NZ.", "/payment-methods/"),
    ("High payout casinos", "The house edge on every main game, and what 'best paying' means.", "/high-payout-casinos/"),
    ("Online betting NZ", "TAB NZ, the offshore ban and how betting odds work.", "/online-betting/"),
    ("Responsible gambling", "Free help, bank blocks, limits and self-exclusion.", "/responsible-gambling/"),
]


def landing(P, crumb, author, checker, lead, facts, ops, list_h2, list_intro, content, faqs,
            kind="casino", cols=None, extra_schema=None, kicker=None, trail=None, priority=0.9, related=None):
    t, d, h1 = META[P]
    faq_html, ents = faq(faqs)
    trail = trail or [(crumb, P)]
    rel = related or [r for r in RELATED if r[2] != P][:6]
    body = (hero(h1, lead, author, checker, facts, kicker or f"Facts checked {CHECKED}")
            + crumbs(trail)
            + f'<section class="sec" id="the-list"><div class="wrap">{law_note()}<h2>{list_h2}</h2><p class="intro">{list_intro}</p>'
            + toplist(ops, kind)
            + compare(ops, cols)
            + rg_line() + "</div></section>"
            + '<section class="sec sec--alt"><div class="wrap prose">'
            + content + faq_html
            + "<h2>Related guides</h2>" + cards(rel, 3)
            + authorbox(author)
            + "</div></section>")
    schema = [schema_webpage(P, "CollectionPage"), schema_crumbs(P, trail),
              schema_article(P, h1, author, checker), schema_itemlist(P, ops, strip_tags(list_h2)),
              schema_faq(P, ents), schema_person(author)]
    if checker:
        schema.append(schema_person(checker))
    schema += extra_schema or []
    write(P, body, schema, priority=priority, freq="weekly", author=author)


# ---------------------------------------------------------------------------
# DIA licence auction result (dia.govt.nz/Online-Gambling-for-Providers,
# updated 13 October 2026). Brands are not published until licences are granted.
# ---------------------------------------------------------------------------
AUCTION_WINNERS = [
    ("Baytree Interactive Limited", 3), ("Christchurch Online NZ Limited", 1), ("One Casino Limited", 1),
    ("Playvia Gaming (NZ) Limited", 2), ("Rock Swift Group Limited", 2), ("Rush Entertainment Limited", 1),
    ("Skill On Net Limited", 1), ("SkyCity NZ Online NO1 Limited", 1), ("SkyCity NZ Online NO2 Limited", 1),
    ("Stake New Zealand Limited", 1), ("TAB New Zealand", 1),
]
AUCTION_SUMMARY = ("The DIA's licence auction ran from 29 September to 12 October 2026. It drew 32 bidders, went to 10 "
                   "rounds and closed at NZ$15 million per licence. Eleven companies won the right to apply for the 15 "
                   "licences.")
NOT_IN_AUCTION = ("None of the companies named as owners of the casinos on this site (Hollycorn N.V., Novatrix S.R.L., "
                  "Softon Ltd and Exceptiosoft Ltd) is among them. The DIA has not yet published which brands will run "
                  "under each licence, but on the public record none of these casinos has a route to a New Zealand "
                  "licence in this round. Expect them to stop serving New Zealand from 1 December 2026.")


def auction_table():
    return table(["Company", "Rights to apply"], [[c, str(n)] for c, n in AUCTION_WINNERS],
                 caption="Source: Department of Internal Affairs, Online Gambling for Providers, updated 13 October 2026.")
