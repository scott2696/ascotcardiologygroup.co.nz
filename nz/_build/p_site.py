"""Company and legal pages: About, Contact, Authors, Terms, Privacy, Cookies."""
from lib import *


def simple(P, crumb, lead, content, author="hana-mcallister", kind="WebPage", extra=None, facts=None, priority=0.4):
    t, d, h1 = META[P]
    trail = [(crumb, P)]
    body = (hero(h1, lead, None, None, facts) + crumbs(trail)
            + f'<section class="sec"><div class="wrap prose">{content}</div></section>')
    schema = [schema_webpage(P, kind), schema_crumbs(P, trail)] + (extra or [])
    write(P, body, schema, priority=priority, freq="yearly", author=author)


def about():
    P = "/about/"
    content = (
        '<h2 id="who">Who we are</h2>'
        f"<p>{NAME} is an independent New Zealand guide to the online casino and betting sites that New Zealanders ask "
        "about. We started it because most casino 'review' sites are advertising in disguise: they rank casinos by what they "
        "pay the publisher, print payout times nobody measured, and say little about New Zealand law. We wanted a record that "
        "a reader could check line by line.</p>"
        '<h2 id="different">What makes us different</h2>'
        + cards([("No casino links", "Nothing on this site sends you to a casino or bookmaker, and we carry no sign-up offers or bonus codes."),
                 ("Every fact sourced", "Each review lists its sources and the date we checked them. If we could not confirm something, we say so."),
                 ("A score you can rebuild", "The Ledger score uses five published inputs and fixed rules, set out on how we review."),
                 ("The law, stated plainly", "Every relevant page explains the 2026 Act, the advertising ban and the 1 December cut-off.")], 2)
        + '<h2 id="standards">Editorial standards</h2>'
          "<ul><li><b>Accuracy.</b> Facts come from operators' own terms, regulators' registers, independent databases and New "
          "Zealand government sources. One-source facts are marked 'reported'.</li>"
          "<li><b>Independence.</b> No operator can pay for a review, a score or a change to either. Scores follow the published "
          "formula.</li>"
          "<li><b>No invented testing.</b> We do not claim deposits, withdrawals or measurements we did not make.</li>"
          "<li><b>Corrections.</b> Confirmed errors are corrected within two working days.</li>"
          "<li><b>Responsible gambling.</b> We never present gambling as a way to make money, and every page carries the "
          "Gambling Helpline number.</li></ul>"
          '<h2 id="funding">How the site is funded</h2>'
          f"<p>{NAME} is funded by its publisher. Because the site contains no links to casinos or bookmakers, we earn no referral "
          "commission when anyone opens an account. The order of operator lists is "
          "an editorial choice and is not a ranking; our assessment is the Ledger score.</p>"
          '<h2 id="team">The team</h2>'
          "<p>Five writers and editors cover casinos, payments, games, law and betting. Each page names its author and the "
          'person who checked it. <a href="/authors/">Meet the team</a>.</p>'
          '<h2 id="contact">Get in touch</h2>'
          f'<p>Corrections, questions and complaints: <a href="/contact/">Contact Us</a>, or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'
    )
    simple(P, "About Us", f"Who runs {NAME}, why there are no casino links here, how the site is funded and the editorial "
           "standards behind every page.", content, kind="AboutPage", priority=0.5)


def contact():
    P = "/contact/"
    content = (
        '<h2 id="email">Email us</h2>'
        + table(["Reason", "Address", "What to include"], [
            ["General questions", f'<a href="mailto:{EMAIL}">{EMAIL}</a>', "Your question and the page it relates to"],
            ["Corrections", f'<a href="mailto:{EMAIL_EDITOR}">{EMAIL_EDITOR}</a>', "The page, the fact, and a source for the correct information"],
            ["Complaints about our content", f'<a href="mailto:{EMAIL_COMPLAINTS}">{EMAIL_COMPLAINTS}</a>', "What you are unhappy with and what you would like us to do"],
            ["Privacy requests", f'<a href="mailto:{EMAIL}">{EMAIL}</a>', "Mark the subject 'Privacy request'"],
        ])
        + '<h2 id="corrections">Corrections</h2>'
          "<p>If a fact on this site is wrong or out of date, tell us which page and which fact, and if you can, point us to a "
          "source. We check every correction against the source, update the page within two working days if it is confirmed, "
          "and recalculate any score it affects.</p>"
          '<h2 id="casino-disputes">Problems with a casino</h2>'
          "<p>We are not connected to any casino or bookmaker and cannot resolve disputes with them. Contact the operator first, "
          "then the regulator named on its licence. Keep screenshots and transaction records. Our reviews list each operator's "
          "licence so you know which regulator to approach.</p>"
          '<h2 id="help">If you need help with gambling</h2>'
          '<p>Call the Gambling Helpline on <a href="tel:0800654655">0800 654 655</a> or text 8006, free and confidential, 24/7.</p>'
          '<h2 id="reply">When we reply</h2><p>We aim to reply to every message within two working days.</p>'
    )
    simple(P, "Contact Us", "Corrections, questions about a casino we cover, complaints and privacy requests. We aim to reply "
           "within two working days.", content, kind="ContactPage", priority=0.5)


def authors():
    P = "/authors/"
    blocks = []
    for k in AUTHOR_ORDER:
        a = AUTHORS[k]
        owns = "".join(f"<li>{x}</li>" for x in a["owns"])
        blocks.append(f'<section class="abox" id="{k}"><span class="av av--lg" aria-hidden="true">{a["initials"]}</span><div>'
                      f'<h2 style="margin:0 0 .2em">{a["name"]}</h2><p class="abox-r">{a["role"]} &middot; {a["focus"]}</p>'
                      f'<p>{a["bio"]}</p><p><b>Responsible for:</b></p><ul>{owns}</ul></div></section>')
    content = ("<p>Every page names the person who wrote it and the person who checked it. Here is who does what.</p>"
               + "".join(blocks)
               + "<h2>How we work together</h2><p>Each page has one author and one checker. The checker confirms every fact "
                 'against its source before publication. Our scoring rules are set out on <a href="/how-we-review/">how we '
                 "review</a>.</p>")
    simple(P, "Authors", "The writers and editors behind every page, what each of them covers, and how pages are checked.",
           content, kind="ProfilePage", extra=[schema_person(k) for k in AUTHOR_ORDER], priority=0.5)


def terms():
    P = "/terms/"
    content = (
        f"<p>These terms apply to your use of {NAME} at {SITE}. By using the site you agree to them.</p>"
        "<h2>1. Who the site is for</h2><p>The site is for adults aged 18 or over. It provides general information about online "
        "gambling and New Zealand law. It is not legal, financial or tax advice.</p>"
        "<h2>2. No links to gambling operators</h2><p>We do not link to, advertise for, or accept referral payments from online "
        "casinos or bookmakers in respect of New Zealand readers. Nothing on this site is an invitation to gamble.</p>"
        "<h2>3. Accuracy</h2><p>We check facts against named sources and show the date we checked them. Operators change their "
        "terms, licences and offers without notice, so information may be out of date when you read it. Always check the "
        "operator's own terms and the regulator's register before you act.</p>"
        "<h2>4. Your responsibility</h2><p>You are responsible for complying with the law that applies to you. Under New "
        "Zealand law, offshore online casinos may not advertise to you and only TAB NZ may offer you online betting.</p>"
        "<h2>5. Liability</h2><p>To the extent permitted by law, we are not liable for any loss arising from your use of the site "
        "or of any gambling service it describes. Nothing in these terms limits rights you have under the Consumer Guarantees "
        "Act 1993 or the Fair Trading Act 1986 that cannot be excluded.</p>"
        f"<h2>6. Copyright</h2><p>The text, data and design of this site are owned by {NAME}. You may quote short extracts with a "
        "link to the source page. Operator names and logos belong to their owners and are used to identify the brands reviewed.</p>"
        '<h2>7. Privacy and cookies</h2><p>See our <a href="/privacy/">Privacy Policy</a> and <a href="/cookie-policy/">Cookie Policy</a>.</p>'
        "<h2>8. Changes</h2><p>We may update these terms. The version on this page applies from the date shown in the page's update line.</p>"
        "<h2>9. Law</h2><p>These terms are governed by the law of New Zealand, and the New Zealand courts have jurisdiction.</p>"
        f'<h2>10. Contact</h2><p><a href="mailto:{EMAIL}">{EMAIL}</a></p>'
    )
    simple(P, "Terms and Conditions", f"The rules for using {NAME}: who it is for, accuracy, our no-links policy, liability, "
           "copyright and the law that applies.", content)


def privacy():
    P = "/privacy/"
    content = (
        f"<p>This policy explains how {NAME} handles personal information under the New Zealand <b>Privacy Act 2020</b> and its "
        "Information Privacy Principles.</p>"
        "<h2>What we collect</h2><ul><li><b>Messages you send us</b> by email: your name, address and what you write.</li>"
        "<li><b>Basic server logs</b> kept by our hosting provider, such as IP address, browser type and pages requested, used "
        "to keep the site secure and working.</li></ul>"
        "<p>We do not run accounts, newsletters, analytics or advertising on this site, and we do not collect payment details.</p>"
        "<h2>Third-party services</h2><p>The site loads its fonts from Google Fonts. When your browser requests them, Google "
        "receives your IP address and browser details under its own privacy policy. We do not embed social media, video or "
        "advertising scripts.</p>"
        "<h2>How we use it</h2><p>Only to reply to you, act on corrections and complaints, and keep the site secure. We do not "
        "sell or share personal information, and we never pass it to gambling operators.</p>"
        "<h2>Storage and security</h2><p>Emails are held in our mail provider's systems, which may be outside New Zealand. We keep "
        "correspondence only as long as needed to deal with it, normally no more than two years.</p>"
        f'<h2>Your rights</h2><p>You can ask to see or correct the personal information we hold about you by emailing <a href="mailto:{EMAIL}">{EMAIL}</a> '
        "with the subject 'Privacy request'. We will respond within 20 working days, as the Act requires. If you are not happy "
        "with our response, you can complain to the Office of the Privacy Commissioner.</p>"
        "<h2>Changes</h2><p>We will update this page if our practices change.</p>"
    )
    simple(P, "Privacy Policy", "What personal information we collect, why, how we protect it, and how to access or correct "
           "it under the Privacy Act 2020.", content)


def cookies():
    P = "/cookie-policy/"
    content = (
        f"<h2>The short version</h2><p>{NAME} does not set any cookies. There are no analytics, advertising, affiliate or "
        "tracking cookies on this site.</p>"
        "<h2>Why there are no affiliate cookies</h2><p>Many casino sites set affiliate cookies that track you to a casino so the "
        "publisher is paid when you sign up. We have no casino links, so there is nothing to track.</p>"
        "<h2>Third parties</h2><p>Fonts are loaded from Google Fonts, which does not set cookies for font requests but does "
        "receive your IP address. If we ever add a service that sets cookies, we will update this page first and ask for your "
        "consent where the law requires it.</p>"
        "<h2>Controlling cookies</h2><p>You can block or delete cookies in your browser settings: in Chrome under Settings, "
        "Privacy and security; in Safari under Settings, Privacy; in Firefox under Settings, Privacy and Security; in Edge under "
        "Settings, Cookies and site permissions.</p>"
        f'<h2>Questions</h2><p><a href="mailto:{EMAIL}">{EMAIL}</a></p>'
    )
    simple(P, "Cookie Policy", f"{NAME} sets no cookies. Here is why there are no affiliate or tracking cookies, what third "
           "parties receive, and how to control cookies in your browser.", content)


def build():
    about(); contact(); authors(); terms(); privacy(); cookies()
