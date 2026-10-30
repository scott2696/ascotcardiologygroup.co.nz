"""Homepage: best online casino sites NZ."""
from lib import *
from home_extra import numbers, complaints, trending, questions

P = "/"
AUTH, CHECK = "hana-mcallister", "wiremu-salter"


def _limits_table():
    rows = []
    for o in CASINOS:
        rows.append([op_cell(o), esc(o["limits"][0] if o["limits"] else "Not published"),
                     esc(o["limits"][1] if len(o["limits"]) > 1 else "Not published"),
                     esc(o["win_cap"] or "None recorded"), nzd_txt(o)])
    return table(["Site", "Daily or first limit", "Weekly or monthly limit", "Daily win cap", "NZD balance"], rows,
                 caption=f"Withdrawal limits as published in each brand's Casino Guru profile, read {CHECKED}. Euro limits are not converted.")


def _picks():
    s = BY
    return cards([
        ("Best documented overall: Spinjo", f"Named owner, two verified licences, NZD balance and a Safety Index of {s['spinjo']['safety']}. The easiest brand here to check up on.", review_url(s["spinjo"])),
        ("Deepest licensing: Rooster Bet", "Three verified licences including an EU one (Estonia), an owner named on its own site, and casino plus sport.", review_url(s["rooster-bet"])),
        ("Casino and sport, NZD: Fortune Play", "Novatrix-run, verified licences, Safety Index 8.4, NZD limits of $7,500 a week.", review_url(s["fortune-play"])),
        ("Lowest wagering on record: Trixino", "7x on a 777% six-stage package, far below the 35x to 40x norm. Licence and owner not yet confirmed, so read the review first.", review_url(s["trixino"])),
        ("Crypto first: Spino", "Anjouan licence, Safety Index 7.2, no complaints logged. No NZD balance; only for people already comfortable with crypto.", review_url(s["spino"])),
        ("Highest NZD limits: Gunsbet", "NZ$3,000 a day and NZ$7,500 a week, the same as the Hollycorn and Novatrix casinos, with a Safety Index of 6.8.", "/fast-payout-casinos/"),
    ], 3)


def build():
    t, d, h1 = META[P]
    n_nzd = sum(1 for o in CASINOS if o["nzd"])
    strong = [o for o in CASINOS if o["rating"] >= 8]
    lead = (f"We checked {len(CASINOS)} online casinos that New Zealanders ask about against the things that decide whether "
            "you get paid: who owns the site, which licence it holds, whether it keeps your money in NZ dollars, and how much "
            "it lets you withdraw. Every fact is sourced and dated. There are no casino links on this site, and the "
            "2026 change in New Zealand law is explained below.")
    facts = [(str(len(CASINOS)), "casinos checked"), (str(n_nzd), "with an NZD balance"),
             ("52%", "of Trustpilot complaints are about withdrawals"), ("0", "casino links or paid offers")]

    sections = [("The list", "the-list"), ("Comparison table", "compare"), ("Quick picks", "picks"),
                ("What makes a casino site 'best' in 2026", "best"), ("What players complain about", "complaints"),
                ("NZ online gambling in numbers", "numbers"), ("NZ law in 2026", "law"),
                ("Real questions Kiwis ask", "questions"),
                ("Check any casino in five minutes", "check"), ("NZD banking and payments", "banking"),
                ("Withdrawal limits compared", "limits"), ("Bonuses and wagering", "bonuses"),
                ("Games: pokies, live and table", "games"), ("Playing on mobile", "mobile"),
                ("Red flags", "red-flags"), ("Gambling safely", "safer"), ("FAQ", "faq")]

    check_steps = [
        ("Find the licence number", "Scroll to the very bottom of the casino's home page. A real offshore licence shows a regulator's name and a number, for example ALSI-202509073-FI2 for Anjouan or OGL/2024/… for Curaçao."),
        ("Look it up on the register", "Search the number on the regulator's own website. If it is missing, expired or belongs to a different brand, stop there."),
        ("Find the company", "The terms and conditions should name the operating company and where it is registered. 'Not stated' is a warning sign, not a detail."),
        ("Read the withdrawal limits", "Search the terms for 'withdrawal', 'limit' and 'maximum win'. Note the daily, weekly and monthly amounts, and any daily win cap."),
        ("Check the currency list", "At sign-up, see whether NZD is offered as a balance currency. If not, every deposit and withdrawal is converted by your bank."),
        ("Read recent complaints", "Check the casino's complaint history on an independent database and its recent reviews, looking for patterns around withdrawals and confiscated winnings."),
    ]

    faqs = [
        ("What are the best online casino sites in NZ?",
         "<p>On the public record, Spinjo, Lucky7even, Lucky Vibe, Rooster Bet and Fortune Play score highest on this site, each "
         "8.0 or above. They have named owners, two or more licences verified by an independent database, an NZD balance and "
         "published NZD withdrawal limits. None of them is licensed in New Zealand.</p>"),
        ("Is it legal to gamble at online casinos in New Zealand?",
         "<p>Playing at an offshore online casino is not an offence for an individual New Zealander. What is restricted is the "
         "operator and anyone advertising for it: since 1 May 2026 it has been unlawful to advertise unlicensed online casino "
         "gambling to people in New Zealand, and from 1 December 2026 unlicensed casinos without a pending licence application "
         "must stop serving New Zealand. Licensed sites are expected from early 2027.</p>"),
        ("Are there any New Zealand licensed online casinos yet?",
         "<p>Not yet. The DIA's auction closed on 12 October 2026: 11 companies, including SkyCity, TAB New Zealand and Stake New "
         "Zealand, won the right to apply for the 15 licences at NZ$15 million each. The first licences are expected in 2027, "
         "and the DIA will then publish a register of licensed operators and their brands.</p>"),
        ("Which online casinos accept New Zealand dollars?",
         f"<p>{n_nzd} of the {len(CASINOS)} casinos we checked list NZD as a balance currency, including Spinjo, Lucky7even, Lucky "
         "Vibe, Rooster Bet, Fortune Play, Lucky Circus, and MadCasino. Smash, Rivo and "
         "Spino do not. For CrownSlots, Kingdom and Trixino we could not confirm it.</p>"),
        ("Which online casino pays out the most?",
         "<p>No casino 'pays out more' in the sense of better odds across the board; the return depends on the game and its RTP "
         "setting. What differs is how much a casino lets you withdraw. The NZD sites in the Hollycorn and Novatrix "
         "groups publish the highest limits here: NZ$3,000 a day and NZ$7,500 a week. See "
         '<a href="/high-payout-casinos/">high payout casinos</a>.</p>'),
        ("Do I pay tax on online casino winnings in New Zealand?",
         "<p>Usually not. Inland Revenue does not treat casual gambling winnings as income. It can be different if gambling is "
         "your business, and gains on crypto you hold can be taxable. See our "
         '<a href="/gambling-winnings-tax-nz/">gambling winnings tax guide</a>.</p>'),
        ("How do I know an online casino is safe?",
         "<p>No offshore casino is 'safe' in the way a New Zealand regulated business is. You can reduce the risk by checking that "
         "the licence number is real, the owner is named, the withdrawal limits suit you and the complaint history is clean. "
         "Our five-minute check above walks through it.</p>"),
        ("Why are there no links to the casinos on this site?",
         "<p>Because New Zealand law bans advertising unlicensed online casino gambling to people here, and because we want our "
         "scores to be read as information, not as sales. We name the casinos so you can research them; we do not send you "
         "to them.</p>"),
        ("What happens to my account after 1 December 2026?",
         "<p>Casinos that have not applied for a New Zealand licence must stop providing online casino gambling to people in "
         "New Zealand from that date. None of the companies behind the casinos on this site won a place in the October 2026 "
         "auction, so expect all of them to close New Zealand accounts. If you hold a balance at one of them, withdraw it before then and keep records of your "
         "deposits, withdrawals and any correspondence.</p>"),
        ("Where can I get help if gambling is becoming a problem?",
         '<p>Call the Gambling Helpline on <a href="tel:0800654655">0800 654 655</a> or text 8006, free and 24/7. Most New Zealand '
         "banks also let you block gambling transactions on your card. See our "
         '<a href="/responsible-gambling/">responsible gambling page</a>.</p>'),
    ]
    faq_html, ents = faq(faqs)

    law_rows = [
        ["27 June 2025", "Racing Industry Amendment Act passes, making TAB NZ the only lawful online sports and racing bookmaker"],
        ["Late 2025", "Cabinet's initial decisions for the new regime, including a ban on affiliate marketing and paid endorsements for licensed casinos"],
        ["1 May 2026", "Online Casino Gambling Act 2026 in force; advertising unlicensed online casino gambling to New Zealanders becomes enforceable with penalties up to NZ$5 million"],
        ["July 2026", "Stage 1: expressions of interest open for licences"],
        ["29 Sep to 12 Oct 2026", "Stage 2: auction. 32 bidders; 11 companies win the right to apply for 15 licences at NZ$15 million each"],
        ["October 2026", "Stage 3: successful bidders submit full applications"],
        ["1 December 2026", "Casinos without a licence application must stop serving New Zealand; applicants may continue without advertising"],
        ["2027", "First licences expected; DIA register of licensed operators published. Exemption for pending applicants ends 1 June 2027"],
    ]

    pay_rows = [
        ["Visa and Mastercard", "Almost all", "Some NZ banks decline offshore gambling transactions; a bank gambling block stops them entirely", "Conversion fee applies if the casino has no NZD balance"],
        ["Skrill and Neteller", "Most", "Good for keeping gambling money separate from your main account", "Some casinos exclude e-wallet deposits from bonuses"],
        ["Neosurf, Paysafecard, Flexepin", "Many", "Prepaid vouchers bought with cash or card: deposit only", "You need another method to withdraw"],
        ["Bank transfer", "Many", "Slowest route, but direct", "Your bank may query transfers to offshore companies"],
        ["Crypto (BTC, ETH, USDT, LTC)", "Most", "Usually the most direct withdrawal route offshore", "Price swings, exchange fees and tax on crypto gains"],
        ["POLi", "A few, reportedly", "Bank-to-bank payment that still runs in New Zealand. One 2026 review reports it at Spinjo and Lucky Vibe; it is not in Casino Guru's payment lists for any brand here", "Closed in Australia in 2023, which is why many guides wrongly say it has gone"],
    ]

    body = (hero(h1, lead, AUTH, CHECK, facts, kicker=f"Facts checked {CHECKED}")
            + f'<section class="sec" id="the-list"><div class="wrap">'
            + f'<h2>The {len(CASINOS)} online casino sites New Zealanders ask about most</h2>'
            + '<p class="intro">Each row shows the four facts that matter most for a New Zealand player: the licence, whether '
              'there is an NZD balance, the published withdrawal limit and the independent Casino Guru Safety Index. The '
              '<b>Ledger score</b> combines them; it is explained under <a href="#best">what makes a casino site best</a>.</p>'
            + toplist(CASINOS)
            + f'<h2 id="compare">Side-by-side comparison</h2>'
            + compare(CASINOS, ["licence", "nzd", "limit", "safety", "tp", "score"])
            + law_note() + rg_line() + "</div></section>"

            + '<section class="sec sec--alt"><div class="wrap"><h2 id="picks">Quick picks by what you need</h2>'
              '<p class="intro">Shortcuts based on the public record. Every pick links to the full review with sources.</p>'
            + _picks() + "</div></section>"

            + '<section class="sec"><div class="wrap prose">'
            + toc(sections)

            + '<h2 id="best">What makes an online casino site "best" in 2026</h2>'
            + "<p>Most rankings sort casinos by the size of their welcome bonus, because that is what earns the ranking site the "
              "most money. A bonus tells you very little about whether you will be paid. For a New Zealander using an offshore "
              "casino, five things decide that, and they are the five inputs to our Ledger score:</p>"
            + table(["Input", "Weight", "What we look at", "Why it matters"], [
                ["Independent safety", "40%", "The Casino Guru Safety Index, built from terms, size, related casinos and complaints", "The best single outside measure of how a casino treats players"],
                ["Licence", "20%", "Which regulator, whether the number is verified, how many licences", "The licence is your only route to an outside complaint"],
                ["Ownership", "15%", "Whether a real company is named and confirmed", "An unnamed operator can disappear without trace"],
                ["Terms and limits", "15%", "Withdrawal limits, daily win caps, reported payout problems", "Limits decide whether a big win reaches you"],
                ["Banking for Kiwis", "10%", "NZD balance, number of payment options, crypto", "Currency conversion quietly costs 2% to 3% each way"],
            ], caption="Full method and rules: how we review.")
            + "<p>Brands with no independent safety profile get a neutral 4.0 for that input, which is why CrownSlots, Kingdom and "
              "Trixino score low despite large offers: we cannot see their track record, so we will not guess it.</p>"
            + note("<p>We publish a number only when we have a source for it. You will not find invented payout times, test "
                   "deposits we never made, or game counts we did not count. Where a fact is reported by one source but not "
                   "confirmed, the review says <em>reported</em>.</p>", "tip", "Our rule on facts")

            + complaints() + numbers()
            + '<h2 id="law">New Zealand online casino law in 2026</h2>'
            + "<p>For twenty years, New Zealand law said that online casino gambling could not be run from inside the country, "
              "but did not stop New Zealanders playing at casinos based overseas. That gap is closing. The Online Casino "
              "Gambling Act 2026 came into force on <b>1 May 2026</b>. It sets up a licensed market of up to 15 online casinos, "
              "regulated by the Department of Internal Affairs (DIA), and gives the DIA new powers against unlicensed operators "
              "and anyone who advertises for them.</p>"
            + table(["Date", "What happens"], law_rows, caption="Sources: Department of Internal Affairs, Racing Industry Amendment Act 2025.")
            + "<p>Three points matter most for players. First, playing offshore is still not an offence for you. Second, the "
              "casinos on this page cannot lawfully advertise to you, which is why this site carries no links or offers. Third, "
              "these casinos must stop serving New Zealand from 1 December 2026 unless they have applied for a licence, and none of "
              "the companies behind them won a place in the DIA's October auction. If you hold a balance at one, withdraw it now. "
              'Auction result and full detail: <a href="/nz-online-casino-law/">NZ online casino law</a>.</p>'
            + trending() + questions()

            + '<h2 id="check">How to check any online casino in five minutes</h2>'
            + "<p>You do not need to trust us or any other site. These six checks take about five minutes and catch most of the "
              "casinos that cause problems:</p>"
            + steps(check_steps)

            + '<h2 id="banking">NZD banking and payment methods</h2>'
            + f"<p>Of the {len(CASINOS)} casinos here, {n_nzd} let you hold a balance in New Zealand dollars. That is worth more "
              "than most welcome bonuses. When a casino only holds euros or US dollars, your bank converts each deposit and "
              "each withdrawal, and the combined fee and exchange spread is commonly 2% to 3% each way. Over a year of regular "
              "deposits that adds up to real money, and none of it appears in the casino's offer.</p>"
            + table(["Method", "Offered by", "Good to know", "Watch for"], pay_rows)
            + '<p>Before you deposit anywhere, consider turning on your bank\'s gambling block if you want a hard stop. Our '
              '<a href="/payment-methods/">payment methods guide</a> covers each method in detail.</p>'

            + '<h2 id="limits">Withdrawal limits compared</h2>'
            + "<p>The limit is the most underrated number in online gambling. A casino with a NZ$1,000 daily limit and a NZ$13,000 "
              "monthly limit would need months to pay a NZ$50,000 jackpot. Daily win caps are stricter "
              "still: at Lucky Circus and Bet&Play, net winnings above US$50,000 in a day are not paid at all.</p>"
            + _limits_table()
            + '<p>For the payout methods that move money fastest, see <a href="/fast-payout-casinos/">fast payout casinos</a>.</p>'

            + '<h2 id="bonuses">Bonuses and wagering, in dollars</h2>'
            + "<p>A welcome bonus is a loan of play money with a condition: you must bet a multiple of it, the wagering "
              "requirement, before any winnings become withdrawable. The headline percentage is far less important than that "
              "multiple. Two offers on our records show the difference:</p>"
            + table(["Offer on record", "Wagering", "Bonus of NZ$100 means betting", "At NZ$1 a spin"], [
                ["CrownSlots: 390% up to €3,700 + 175 free spins", "40x (reported)", "NZ$4,000", "about 4,000 spins"],
                ["Trixino: 777% up to €7,777 over six deposits", "7x", "NZ$700", "about 700 spins"],
            ], caption="Worked on a NZ$100 bonus for clarity. Pokies with a 96% RTP lose, on average, about 4% of every dollar wagered.")
            + "<p>On a 96% RTP pokie, wagering NZ$4,000 costs about NZ$160 on average; wagering NZ$700 costs about NZ$28. That is "
              "why a lower multiple usually beats a bigger percentage. Also check the maximum bet allowed while a bonus is "
              "active, which games count towards wagering, and whether winnings from the bonus are capped. Full guide: "
              '<a href="/online-casinos/bonuses/">casino bonuses explained</a>.</p>'

            + '<h2 id="games">Games: pokies, live dealer and table games</h2>'
            + "<p>Pokies make up most of every lobby on this list. The number to understand is return to player (RTP): the share "
              "of all money staked that a game pays back over millions of spins. Many popular pokies are released at several "
              "RTP settings, for example 96%, 94% and 92%, and the casino chooses which to run. You can usually see the setting "
              "in the game's information panel.</p>"
            + table(["Game", "Typical house edge", "Notes"], [
                ["Blackjack (basic strategy)", "About 0.5%", "Depends on the rules; your decisions matter"],
                ["European roulette", "2.7%", "Single zero. Avoid double-zero American wheels (5.26%)"],
                ["Baccarat, banker bet", "About 1.06%", "Player bet about 1.24%; tie bet much higher"],
                ["Pokies", "About 3% to 8%", "Set by the RTP version the casino runs"],
                ["Live game shows", "About 3% to 5% or more", "Varies by segment and bet"],
            ], caption="House edge figures are standard published game maths, not casino-specific.")
            + '<p>Guides: <a href="/online-pokies/">online pokies NZ</a>, <a href="/live-casinos/">live casino NZ</a> and '
              '<a href="/high-payout-casinos/">high payout casinos</a>.</p>'

            + '<h2 id="mobile">Playing on mobile</h2>'
            + "<p>Every casino on this list runs in a mobile browser, so you do not need to install anything. Be wary of any "
              "'casino app' offered as a download file outside the official app stores. A browser site is also easier to "
              "walk away from: you can delete the bookmark and clear your saved logins. If you play on your phone, set your "
              "deposit limit in the account settings first, because it applies on every device.</p>"

            + '<h2 id="red-flags">Red flags that should stop you depositing</h2>'
            + "<ul>"
              "<li><b>No licence number</b>, or a number that does not appear on the regulator's register.</li>"
              "<li><b>No company name</b> in the terms and conditions.</li>"
              "<li><b>Daily win caps</b> or weekly withdrawal limits that are low compared with the bonus on offer.</li>"
              "<li><b>Bonus terms that let the casino void winnings</b> for 'irregular play' without defining it.</li>"
              "<li><b>A cluster of complaints</b> about withdrawals being delayed after big wins, or accounts being closed.</li>"
              "<li><b>Pressure</b>: countdown timers, VIP managers who contact you to deposit, or offers to 'unlock' a withdrawal for a fee.</li>"
              "</ul>"
            + note("<p>Any request to pay a fee, tax or 'unlock charge' before a withdrawal is a scam. Legitimate casinos deduct any "
                   "fees from the withdrawal itself.</p>", "warn", "Never pay to withdraw")

            + '<h2 id="safer">Gambling safely</h2>'
            + "<p>Treat gambling as entertainment you pay for. Decide your budget before you play, set a deposit limit in your "
              "account, and stop when it is gone. Signs that it is time to step back include chasing losses, borrowing to "
              "gamble, hiding it from whānau, or feeling anxious when you are not playing.</p>"
            + table(["Support", "Contact", "What they offer"], [
                ["Gambling Helpline", '<a href="tel:0800654655">0800 654 655</a> or text 8006', "Free, confidential, 24/7 support and counselling referrals"],
                ["Problem Gambling Foundation", '<a href="tel:0800664262">0800 664 262</a>', "Free counselling, including Māori and Pacific services"],
                ["Asian Family Services", '<a href="tel:0800862342">0800 862 342</a>', "Support in several Asian languages"],
            ])
            + '<p>More tools, including bank gambling blocks and self-exclusion: <a href="/responsible-gambling/">responsible gambling</a>.</p>'

            + faq_html
            + "<h2>More guides</h2>" + cards([r for r in RELATED if r[2] != "/"][:6], 3)
            + authorbox(AUTH)
            + "</div></section>")

    schema = [schema_webpage(P, "CollectionPage"), schema_crumbs(P, []),
              schema_article(P, h1, AUTH, CHECK), schema_itemlist(P, CASINOS, "Online casino sites checked for NZ readers"),
              schema_howto(P, "How to check an online casino in five minutes", check_steps),
              schema_faq(P, ents), schema_person(AUTH), schema_person(CHECK)]
    write(P, body, schema, priority=1.0, freq="weekly", author=AUTH)
