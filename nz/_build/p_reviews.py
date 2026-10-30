"""The reviews hub and one review per operator."""
from lib import *
from guide_howto import account_guide

AUTH, CHECK = "hana-mcallister", "wiremu-salter"


def _meta(op):
    # "is <brand> legit" is the dominant brand-review query in NZ autocomplete.
    t = f"{op['name']} Review NZ {DATE}: Is It Legit?"
    h1 = f"{op['name']} Review NZ {DATE}: Is It Legit? Licence, Owner, NZD Banking and Limits"
    lic = op["licence_short"]
    d = (f"Is {op['name']} safe for Kiwis? Our review checks its "
         f"{lic.lower() if lic.startswith('Not') else lic} licence, {'NZD balance' if op['nzd'] else 'currency'}, payout limits "
         f"and safety score, and what 1 December means for NZ.")
    return t, d, h1


def _facts(op):
    lic = "".join(f"<li>{esc(a)}: <b>{esc(n)}</b></li>" for a, n in op["licences"])
    prods = " and ".join(x for x, f in (("Online casino", op["casino"]), ("sportsbook", op["sports"])) if f)
    rows = [
        ("Products", prods + (" (crypto accepted)" if op["crypto"] else "")),
        ("Owner", f'{esc(op["owner"])}<br><small>{esc(op["owner_note"])}</small>'),
        ("Licences", f"<ul>{lic}</ul>"),
        ("Launched", esc(op["launched"] or "Not confirmed")),
        ("NZD balance", nzd_txt(op)),
        ("Withdrawal limits", esc(", ".join(op["limits"]) or "Not published in the sources we checked")),
        ("Daily win cap", esc(op["win_cap"] or "None recorded")),
        ("Payment options", (f'{op["n_pay"]} listed, including ' if op["n_pay"] else "Including ") + esc(", ".join(op["payments"][:8]))),
        ("Casino Guru Safety Index", (f'<b>{op["safety"]:.1f}</b> / 10' if op["safety"] is not None else "No independent profile found")),
        ("Trustpilot", esc(tp_txt(op, True))),
        ("Complaints (Casino Guru)", str(op["complaints"]) + " logged directly" if op["complaints"] is not None else "No figure published"),
        ("Offer on record", esc(op["offer"] or "None confirmed")),
        ("Facts checked", CHECKED),
    ]
    return '<dl class="facts">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows) + "</dl>"


def _licence_section(op):
    names = [a for a, _ in op["licences"]]
    s = " ".join(names)
    out = [f'<h2 id="licence">Licence and ownership</h2><p>{esc(op["owner_note"])}</p>']
    if op["licence_short"].startswith(("Not", "None")):
        out.append("<p>We could not find a licence number for this brand that an independent source had checked. That "
                   "matters because the licence is the only route to an outside body if the casino refuses a withdrawal. "
                   "Before depositing anywhere, scroll to the footer of the casino's own site, copy the licence number and "
                   "look it up on the regulator's public register.</p>")
    else:
        if "Anjouan" in s:
            out.append("<p><b>Anjouan</b> (the Anjouan Offshore Finance Authority, in the Comoros) became a common licence "
                       "for offshore casinos after Curaçao tightened its rules in 2023. Its numbers follow the pattern "
                       "ALSI-YYYYMM…, so you can read roughly when the licence was issued. It is a light-touch regulator: "
                       "there is a complaints route, but nothing like the protections of a European or New Zealand licence.</p>")
        if "Tobique" in s:
            out.append("<p><b>Tobique Gaming Commission</b> licenses online gambling from the Tobique First Nation in New "
                       "Brunswick, Canada. Like Anjouan, it is an offshore licence; it does not make a site legal in New Zealand.</p>")
        if "Kahnawake" in s:
            out.append("<p><b>The Kahnawake Gaming Commission</b>, near Montreal, is one of the longest-running online "
                       "gambling regulators, operating since the late 1990s, and runs a formal player complaints process.</p>")
        if "Curaçao" in s:
            out.append("<p><b>Curaçao</b> replaced its old master-licence system with direct licensing by the Curaçao Gaming "
                       "Authority from 2023. Licences under the new regime carry numbers that start with OGL/.</p>")
        if "Estonia" in s:
            out.append("<p><b>Estonia's Tax and Customs Board</b> is a European Union regulator. An Estonian licence "
                       "covers the operator's business in Estonia; it does not extend to New Zealand.</p>")
    out.append('<p>None of these licences is a New Zealand licence. See <a href="/nz-online-casino-law/">NZ online casino '
               'law</a> for what that means and what changes on 1 December 2026.</p>')
    return "".join(out)


def _banking(op):
    p = [f'<h2 id="banking">Banking for New Zealand players</h2>']
    if op["nzd"]:
        p.append(f"<p>{op['name']} lets you hold your balance in New Zealand dollars, so a deposit from a New Zealand bank "
                 "card or account is not converted. That saves the spread a bank charges on every foreign-currency "
                 "transaction, which is often 2% to 3% each way.</p>")
    elif op["nzd"] is False:
        p.append(f"<p>{op['name']} does not list New Zealand dollars as a balance currency, so your bank converts every "
                 "deposit and withdrawal. On a card, the conversion fee and exchange spread commonly add 2% to 3% each "
                 "way, which comes off your money before you place a bet.</p>")
    else:
        p.append(f"<p>We could not confirm whether {op['name']} offers a New Zealand dollar balance. Check the currency "
                 "drop-down at sign-up; if NZD is not there, every deposit will be converted.</p>")
    if op["limits"]:
        p.append(f"<p>Published withdrawal limits: <b>{esc(', '.join(op['limits']))}</b>. Limits decide how quickly a "
                 "big win reaches you; a site that caps withdrawals at a few thousand a week can take months to pay out a "
                 "large jackpot.</p>")
    else:
        p.append("<p>We did not find published withdrawal limits for this brand. Ask support for the daily, weekly and "
                 "monthly limits in writing before you deposit.</p>")
    if op["win_cap"]:
        p.append(f"<p><b>Win cap:</b> {esc(op['win_cap'])}. Any amount above this in a single day is not paid, regardless "
                 "of how it was won. This is set out in the terms and is easy to miss.</p>")
    p.append(f"<p>Payment options listed for this brand include {esc(', '.join(op['payments']))}. Availability varies by "
             'country, so check the cashier after sign-up. Our <a href="/payment-methods/">payment methods guide</a> '
             "explains fees and speeds for each method from New Zealand.</p>")
    return "".join(p)


def _offer(op):
    if op.get("offer"):
        return (f'<h2 id="offer">Offer on record</h2><p><b>{esc(op["offer"])}</b></p><p>{esc(op["offer_detail"])}</p>'
                '<p>We do not publish sign-up links or bonus codes. To understand what any welcome offer really costs, see '
                '<a href="/online-casinos/bonuses/">casino bonuses explained</a>, which turns wagering into dollars.</p>')
    return ('<h2 id="offer">Offers</h2><p>We have no confirmed welcome offer on record for this brand. Offshore offers change '
            'often and differ by country, and we only quote offers we have been supplied or can source. Our '
            '<a href="/online-casinos/bonuses/">bonus guide</a> shows how to read any offer you find.</p>')


def _faqs(op):
    lic = ", ".join(f"{a} ({n})" for a, n in op["licences"])
    q = [
        (f"Is {op['name']} licensed?",
         f"<p>{'We could not confirm a licence for ' + op['name'] + '.' if op['licence_short'].startswith(('Not','None')) else op['name'] + ' holds: ' + esc(lic) + '.'} "
         "None of these is a New Zealand licence from the Department of Internal Affairs.</p>"),
        (f"Does {op['name']} accept New Zealand dollars?",
         f"<p>{ {True: 'Yes. NZD is listed as a balance currency.', False: 'No. NZD is not listed as a balance currency, so deposits are converted.', None: 'We could not confirm it. Check the currency list when you register.'}[op['nzd']] }</p>"),
        (f"What are {op['name']}'s withdrawal limits?",
         f"<p>{esc(', '.join(op['limits'])) + '.' if op['limits'] else 'We did not find published limits; ask support before depositing.'}"
         f"{' There is also a daily win cap of ' + esc(op['win_cap']) + '.' if op['win_cap'] else ''}</p>"),
        (f"Is it legal for New Zealanders to use {op['name']}?",
         "<p>New Zealand law targets operators and advertisers, not players, and playing at an offshore site is not an offence "
         "for the individual. But the site is not licensed in New Zealand, it cannot lawfully advertise to you, and from 1 December "
         "2026 unlicensed casinos without a pending application must stop serving New Zealand players. Its operator is not "
         "among the 11 companies that won the right to apply in the DIA's October 2026 auction, so expect it to close New "
         "Zealand accounts. You also have no New "
         "Zealand regulator to complain to.</p>"),
    ]
    return q


def build_review(op):
    P = review_url(op)
    t, d, h1 = _meta(op)
    PAGE_EXTRA[P] = (t, d, h1)
    trail = [("Casino reviews", "/casino-reviews/"), (op["name"], P)]
    offer = f'<p class="rv-offer"><span>Offer on record</span>{esc(op["offer"])}</p>' if op.get("offer") else ""
    head = (f'<header class="hero hero--rv"><div class="wrap rv-grid">'
            f'<div class="rv-copy"><p class="kicker">Facts checked {CHECKED}</p><h1>{stamp(h1)}</h1>'
            f'<p class="lead">{op["tagline"]}</p>{byline(AUTH, CHECK)}</div>'
            f'<aside class="rv-card" aria-label="{attr(op["name"])} scorecard">'
            f'<div class="rv-logo{" logo--dark" if op.get("logo_dark") else ""}">{logo_img(op, 200, 96, True)}</div>'
            f'<p class="rv-score"><b>{op["rating"]:.1f}</b><span>out of 10<br>Ledger score</span></p>'
            f'<div class="rv-bar" aria-hidden="true"><i style="width:{op["rating"] * 10:.0f}%"></i></div>'
            f'{offer}{visit_btn(op, "casino" if op["casino"] else "sports", "btn btn--block")}'
            f'<a class="rv-jump" href="#facts">See the key facts</a>'
            f'<p class="rv-rg">18+ only. Free help: <a href="tel:0800654655">0800 654 655</a></p></aside>'
            f'</div></header>')
    faq_html, ents = faq(_faqs(op), heading=f"{op['name']}: common questions")
    srcs = "".join(f'<li>{esc(n)}{": " + esc(u) if u else ""}</li>' for n, u in op["sources"])
    body = (head + crumbs(trail)
            + '<section class="sec"><div class="wrap prose">'
            + law_note()
            + toc([("Key facts", "facts"), ("Overview", "overview"), ("Licence and ownership", "licence"),
                   ("Banking for New Zealand players", "banking"), ("Offers", "offer"), ("Ledger score", "score"),
                   ("Verdict", "verdict"), ("Common questions", "faq")])
            + f'<h2 id="facts">Key facts</h2>{_facts(op)}'
            + f'<h2 id="overview">Overview</h2><p>{op["intro"]}</p>' + proscons(op["pros"], op["cons"])
            + _licence_section(op) + _banking(op) + _offer(op)
            + f'<h2 id="score">Ledger score: {op["rating"]:.1f} out of 10</h2>'
            + '<p>The score is built from five inputs, each taken from public information, so you can check it yourself. '
              'Independent safety is the Casino Guru Safety Index; brands without one are given a neutral 4.0. Full weights '
              'and rules are on <a href="/how-we-review/">how we review</a>.</p>'
            + scorebars(op["parts"])
            + f'<h2 id="verdict">Verdict</h2><p>{op["verdict"]}</p>'
            + faq_html
            + f'<div class="src"><b>Sources</b> (read {CHECKED})<ul>{srcs}</ul>'
              '<p style="margin:.6em 0 0">Something out of date? <a href="/contact/#corrections">Send a correction</a>.</p></div>'
            + rg_line() + authorbox(AUTH)
            + "</div></section>")
    schema = [schema_webpage(P), schema_crumbs(P, trail), schema_review(op, AUTH), schema_faq(P, ents),
              schema_person(AUTH), schema_person(CHECK)]
    write(P, body, schema, priority=0.6, author=AUTH)


def build_hub():
    P = "/casino-reviews/"
    t, d, h1 = META[P]
    trail = [("Casino reviews", P)]
    faqs = [
        ("How are these reviews different from other casino review sites?",
         "<p>We do not link to any casino, we take no referral fees for New Zealand sign-ups, and every fact in a review is "
         "dated and sourced. Where we could not confirm something, such as a licence number or an owner, we say so instead "
         "of filling the gap.</p>"),
        ("Why is the list order different from the score order?",
         "<p>The list order is set by our editor. The Ledger score is calculated from five published inputs. If you want our "
         "assessment, use the table sorted by score below.</p>"),
        ("Have you played at these casinos?",
         "<p>These reviews are built from public records: licence registers, the operators' own terms, and independent "
         "databases such as Casino Guru. We do not claim test deposits or timed withdrawals we have not made, and we do not "
         "publish invented payout times.</p>"),
        ("How often are reviews updated?",
         f"<p>Every fact is rechecked at least monthly. The current check was on {CHECKED}; the next is due by {NEXT_CHECK}. "
         "If you see something out of date, tell us through the contact page.</p>"),
    ]
    faq_html, ents = faq(faqs)
    rows_score = compare(BY_SCORE, ["products", "licence", "nzd", "limit", "safety", "score"])
    body = (hero(h1, "Fifteen casino and betting sites that New Zealanders ask about, each checked against public licence "
                 "records, the operator's own terms and independent safety data. No links, no sign-up offers, sources on "
                 "every page.", AUTH, CHECK,
                 [(str(len(OPS)), "sites reviewed"), (str(sum(1 for o in OPS if o["nzd"])), "with an NZD balance"), ("8.9", "highest Safety Index"), ("0", "casino links")])
            + crumbs(trail)
            + f'<section class="sec"><div class="wrap"><h2>All 15 reviews</h2>'
              '<p class="intro">Listed in our editor\'s order. Each row links to the full review.</p>'
            + toplist(OPS) + account_guide("/casino-reviews/") + law_note() + rg_line() + "</div></section>"
            + '<section class="sec sec--alt"><div class="wrap">'
            + '<h2 id="by-score">Every site sorted by Ledger score</h2><p class="intro">Highest first. The score weights '
              'independent safety (40%), licence (20%), ownership (15%), terms and limits (15%) and banking for Kiwis (10%).</p>'
            + rows_score
            + '<div class="prose">'
            + "<h2>What the scores tell you</h2>"
            + "<p>Five brands score 8 or more: Spinjo, Lucky7even, Lucky Vibe, Rooster Bet and Fortune Play. They share "
              "three traits: a named owner, two or more licences that an independent database has verified, and an NZD balance "
              "with published NZD withdrawal limits. All five belong to two groups, Hollycorn N.V. and Novatrix S.R.L., "
              "which is worth knowing: a dispute with one brand often involves the same support and payments team as its "
              "sister sites.</p>"
            + "<p>At the other end, Kingdom, Trixino and CrownSlots score below 5 mainly because we could not "
              "confirm a licence or an owner. Smash has a licence, but "
              "its independent Safety Index is below 4.</p>"
            + "<h2>How to read a review</h2>"
            + steps([("Start with the key facts box", "Licence numbers, owner, NZD support and limits are at the top of every review, with the date we checked them."),
                     ("Check the licence yourself", "Copy the licence number into the regulator's public register. If the casino's footer shows a different number from ours, trust the register."),
                     ("Look at the limits, not the bonus", "Withdrawal limits and win caps decide whether you can actually receive a big win. They matter more than the size of a welcome offer."),
                     ("Read the legal note", "None of these sites is licensed in New Zealand. Our law guide explains what that means for you.")])
            + faq_html + authorbox(AUTH) + "</div></div></section>")
    schema = [schema_webpage(P, "CollectionPage"), schema_crumbs(P, trail), schema_itemlist(P, OPS, "Casino reviews"),
              schema_faq(P, ents), schema_person(AUTH), schema_person(CHECK)]
    write(P, body, schema, priority=0.8, freq="weekly", author=AUTH)


def build():
    build_hub()
    for op in OPS:
        build_review(op)
