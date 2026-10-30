"""Competitor-coverage sections for the twelve money pages.

Built from the H2/H3 outlines of the top-ranking competitor pages for each
keyword (fetched 30 October 2026; see research/COMPETITOR-HEADINGS.md). Each
page gets the headings and step-by-step guides those pages share, written in
our own words, plus "opportunity" sections none of them have. Operator
examples come from ops_data.py, so they stay in step with the reviews.
"""
from lib import BY, OPS, CASINOS, SPORTS, steps, table, note, review_url, esc


def link(slug):
    o = BY[slug]
    return f'<a href="{review_url(o)}">{esc(o["name"])}</a>'


EUR_NZD = 1.95   # approximate rate used for euro limits; rounded, for illustration only


def weeks_to_pay(op, amount_nzd):
    """Weeks to withdraw amount_nzd under the published weekly limit, NZD limits only."""
    for lim in op["limits"]:
        if lim.startswith("NZ$") and "week" in lim:
            per = int(lim[3:].split(" ")[0].replace(",", ""))
            return -(-amount_nzd // per), lim
    return None, None


def _win_schedule(amount):
    rows = []
    for o in OPS:
        n, lim = weeks_to_pay(o, amount)
        if n:
            rows.append([link(o["slug"]), lim, f"{n} week{'s' if n > 1 else ''}"])
    for slug, eur in (("smash", 2000), ("lucky-circus", 2500)):
        n = -(-round(amount / EUR_NZD) // eur)
        rows.append([link(slug), f"€{eur:,} a week", f"About {n} weeks at NZ${EUR_NZD} to the euro"])
    rows.append([link("crownslots"), "Not published", "Unknown: ask support in writing before you deposit"])
    return table(["Casino", "Published weekly limit", f"Time to receive a NZ${amount:,} win"], rows,
                 caption="Worked from each casino's published limits as recorded in our reviews. Euro conversions are approximate.")


GROUPS = table(["Group", "Casinos on our list", "What it means for you"], [
    ["Hollycorn N.V.", f'{link("spinjo")}, {link("lucky7even")}, {link("lucky-vibe")}',
     "Same limits (NZ$3,000 a day, NZ$7,500 a week), similar cashier and support. A welcome bonus at one may rule out another."],
    ["Novatrix S.R.L.", f'{link("gunsbet")}, {link("rooster-bet")}, {link("fortune-play")}, {link("lucky-circus")}, {link("betandplay")}',
     "Shared payments team and terms. A dispute or account closure at one brand can follow you to its sisters."],
    ["Softon Ltd", link("smash"), "Euro-only limits of €1,000 a day and a €100,000 daily win cap."],
    ["Exceptiosoft Ltd", link("rivo"), "Euro-only limits, 2026 Anjouan licence."],
    ["Owner not confirmed", f'{link("crownslots")}, {link("kingdom")}, {link("trixino")}, {link("madcasino")}, {link("spino")}',
     "No confirmed company to hold to account. Read the licence section of each review first."],
], caption="From the owner field in each review. Groups change; check the footer of the site you use.")


COMPLAIN_STEPS = [
    ("Put it in writing", "Use live chat or email and ask for a ticket or reference number. Screenshot your balance, bet history and every reply."),
    ("Follow the casino's own complaints process", "Most terms give a set number of days for a reply. Note the deadline and escalate to a manager or the complaints address if it passes."),
    ("Go to the regulator named on the licence", "Anjouan, Tobique and Curaçao each publish a complaints route. Quote the licence number from the casino's footer."),
    ("Use an independent mediator", "Casino Guru's complaint resolution centre and similar services handle disputes for free. They cannot force payment, but many cases settle."),
    ("Know where the road ends", "No New Zealand body can order an offshore casino to pay. That is the main reason to keep balances small and withdraw often."),
]


# ---------------------------------------------------------------------------
# Homepage
# ---------------------------------------------------------------------------
def home():
    return (
        '<h2 id="by-category">Best online casino sites NZ by category</h2>'
        "<p>Most ranking pages pick a 'best' casino for each type of player. Here is ours, based on the facts in each review rather than the size of the bonus:</p>"
        + table(["If you want…", "Look at", "Why"], [
            ["The strongest public record", link("spinjo"), "Named owner, two verified licences, NZD balance, Safety Index 8.9"],
            ["Casino and sport on one NZD account", f'{link("fortune-play")} or {link("lucky-vibe")}', "Both hold NZD and publish NZ$7,500 weekly limits"],
            ["The deepest licensing", link("rooster-bet"), "Three licences including an EU one (Estonia)"],
            ["Low wagering", f'{link("smash")} (10x deposit + bonus)', "Far below the 35x to 40x norm, but euro-only limits"],
            ["Crypto only", link("spino"), "Coins only, 20% cashback with no wagering reported, clean complaint record"],
            ["The biggest headline package", link("lucky-circus"), "100% up to NZ$10,000 + 450 free spins reported, at 40x"],
        ])
        + '<h2 id="win-real-money">Can you win real money at online casinos in NZ?</h2>'
        "<p>Yes. Every casino on this page pays real money, and winnings are not taxed for casual players in New Zealand. Three things decide whether you actually receive a win: the game's return to player (RTP), the casino's withdrawal limits, and whether your account is verified. A NZ$50,000 pokie win at a casino with a NZ$7,500 weekly limit arrives over seven weeks, not in one payment.</p>"
        + '<h3 id="big-win">What a big win looks like at each casino</h3>' + _win_schedule(50000)
        + '<h2 id="bonus-types">Online casino bonus types explained</h2>'
        + table(["Bonus", "How it works", "Example on our list"], [
            ["Welcome package", "Matches your first few deposits, often with free spins", f'{link("spinjo")}: up to NZ$5,000 + 300 free spins over four deposits (reported)'],
            ["Low-wager bonus", "Smaller multiple, so more of it can be withdrawn", f'{link("smash")}: 600% up to €10,000 at 10x deposit + bonus'],
            ["Multi-stage package", "Different match on each deposit", f'{link("trixino")}: 777% over six deposits at 7x (supplied)'],
            ["Cashback", "A share of losses returned, sometimes with no wagering", f'{link("spino")}: 20% cashback up to 2,000 USDT (reported)'],
            ["Sports welcome", "Bonus for the sportsbook instead of the casino", f'{link("madcasino")}: 250% up to €3,500 (supplied)'],
        ])
        + '<h2 id="vip">Loyalty and VIP programmes</h2>'
        "<p>Most casinos here run a points-based loyalty scheme: you earn points per bet, move up levels and unlock cashback, faster withdrawals or higher limits. Read the level table before chasing it. A VIP tier that raises your weekly limit is worth more than one that only adds free spins, and points earned while a bonus is active often do not count.</p>"
        + '<h2 id="providers">Casino software providers</h2>'
        "<p>The games at offshore casinos come from the same studios you will find worldwide: Pragmatic Play, Evolution (live dealer), Play'n GO, NetEnt, Relax Gaming, Hacksaw and BGaming among them. The studio sets each game's maths, but many let the casino choose between several RTP settings. A well-known studio is a good sign for fairness; it does not tell you which RTP version the casino runs.</p>"
        + '<h2 id="pros-cons">Pros and cons of offshore casinos for Kiwis</h2>'
        + table(["Pros", "Cons"], [
            ["Large game lobbies, often 5,000+ titles", "No New Zealand regulator to complain to"],
            ["NZD balances at the Hollycorn and Novatrix brands", "Withdrawal limits can stretch a big win over months"],
            ["Crypto and e-wallet withdrawals can be quick", "Advertising them to New Zealanders is unlawful; you will not see them promoted legitimately"],
            ["Low-wager offers exist (Smash 10x, Trixino 7x supplied)", "Expected to stop serving New Zealand from 1 December 2026"],
        ])
        + '<h2 id="complain">How to make a complaint at an online casino</h2>' + steps(COMPLAIN_STEPS)
        + '<h2 id="exit-plan">Your 1 December exit plan, step by step</h2>'
        "<p>No other ranking page covers this, but it matters more than any bonus right now. None of the companies behind these casinos won a place in the DIA's October 2026 licence auction.</p>"
        + steps([
            ("List every casino where you hold an account", "Include ones you have not used for months. Balances, bonus funds and loyalty points can all be lost when an operator exits."),
            ("Finish or cancel active bonuses", "An active bonus blocks withdrawal. Forfeit it if the wagering cannot be finished in time."),
            ("Complete verification now", "Upload ID and proof of address before the rush. Verification queues get longer near a market exit."),
            ("Withdraw in limit-sized amounts", "At NZ$3,000 a day, a NZ$12,000 balance needs four working days. Start early."),
            ("Save your records", "Download your transaction history and keep every email. You will need them if a payment goes missing."),
        ])
    )


# ---------------------------------------------------------------------------
# Online pokies
# ---------------------------------------------------------------------------
def pokies():
    return (
        '<h2 id="paytable">Pokie symbols and how to read a paytable</h2>'
        "<p>Every pokie has an information screen, usually behind an 'i' or menu icon. It is the only reliable place to find the game's RTP and rules.</p>"
        + steps([
            ("Open the paytable before you spin", "Look for the i, ? or menu icon in the game. It works the same in demo and real-money mode."),
            ("Find the RTP figure", "Usually in the rules text. If it shows several values, the casino chose one; if none is shown, assume the lowest."),
            ("Learn the special symbols", "Wilds substitute for other symbols, scatters trigger features regardless of position, and bonus symbols start free spins or pick games."),
            ("Check paylines or ways to win", "Fixed paylines pay left to right on set lines; 'ways' games pay matching symbols on adjacent reels, up to 117,649 ways on Megaways."),
            ("Note the max win", "Shown as a multiple of your stake, such as 5,000x. Once reached, the round ends even if more wins were due."),
        ])
        + '<h2 id="popular">Best online pokies for real money: popular titles and their RTP</h2>'
        + table(["Pokie", "Studio", "Published top RTP", "Volatility"], [
            ["Book of 99", "Relax Gaming", "99%", "High"],
            ["Mega Joker", "NetEnt", "Up to 99% (with supermeter)", "High"],
            ["Blood Suckers", "NetEnt", "98%", "Low"],
            ["Sweet Bonanza", "Pragmatic Play", "96.48%", "High"],
            ["Book of Dead", "Play'n GO", "96.21%", "High"],
            ["Starburst", "NetEnt", "96.09%", "Low"],
            ["Gonzo's Quest", "NetEnt", "95.97%", "Medium"],
            ["Mega Moolah", "Games Global", "About 88% (progressive)", "High"],
        ], caption="Top RTP as published by each studio. Casinos may run lower settings; check the paytable.")
        + '<h2 id="max-win">What do max win caps mean on a pokie?</h2>'
        "<p>A max win cap is the most a single round can pay, set as a multiple of your stake. A 5,000x cap at NZ$1 a spin means NZ$5,000. Casinos can add their own caps on top: "
        + link("lucky-circus") + " and " + link("betandplay") + " do not pay net daily winnings above US$50,000, and " + link("smash") + " and " + link("rivo") + " cap daily wins at €100,000.</p>"
        + '<h2 id="free-spins-vs-bonus">In-game free spins vs bonus spins</h2>'
        "<p>In-game free spins are a feature of the pokie, triggered by scatters and paid as normal winnings. Bonus spins come from the casino's promotion, are tied to one game and a fixed stake, and their winnings usually carry wagering. "
        + link("lucky-circus") + "'s reported 450 free spins are bonus spins at 40x; a scatter-triggered round in Book of Dead is not.</p>"
        + '<h2 id="tournaments">Pokies tournaments</h2>'
        "<p>Tournaments rank players by points, biggest multiplier or total wins over a set period, with a prize pool shared among the leaders. Entry is usually free with real-money spins on the listed games. Read the scoring rule: 'biggest multiplier' tournaments reward small stakes, while 'total wagered' ones reward volume and can push you to spend more than you planned.</p>"
        + '<h2 id="glossary">Real money pokie terms you need to know</h2>'
        + table(["Term", "Meaning"], [
            ["RTP", "Long-run share of stakes returned to players, such as 96%"],
            ["Volatility", "How often and how big wins come; high volatility means rarer, larger wins"],
            ["Hit frequency", "Share of spins that return anything at all"],
            ["Bonus buy", "Paying a fixed price to trigger the feature; often banned while a bonus is active"],
            ["Megaways", "Reels change height each spin, giving up to 117,649 ways to win"],
            ["Hold and win", "Feature where money symbols lock in place while respins reset"],
            ["Max win", "The highest multiple a single round can pay"],
        ])
        + '<h2 id="tips">Tips for real money pokies in NZ</h2>'
        + steps([
            ("Pick an NZD casino", f'{link("spinjo")}, {link("lucky7even")} and {link("lucky-vibe")} all hold NZD, so your bank does not convert every spin.'),
            ("Prefer 96% RTP or higher", "On NZ$1,000 of spins, 96% costs about NZ$40 on average; 94% costs NZ$60."),
            ("Match volatility to your budget", "Low volatility stretches a small budget; high volatility needs a bigger one to reach the features."),
            ("Decide on the bonus first", "A bonus at 40x on pokies means betting 40 times the bonus before it is yours."),
            ("Set a time and money limit", "Pokies are fast. At 10 spins a minute, an hour is 600 spins."),
        ])
        + '<h2 id="budget">How long does NZ$100 last on the pokies?</h2>'
        "<p>None of the ranking pages answer this, but it is the most useful number on the page. On average, the cost per hour is spins per hour × stake × (1 − RTP):</p>"
        + table(["Stake", "Spins an hour", "RTP", "Average cost an hour"], [
            ["NZ$0.20", "600", "96%", "NZ$4.80"],
            ["NZ$1.00", "600", "96%", "NZ$24.00"],
            ["NZ$1.00", "600", "94%", "NZ$36.00"],
            ["NZ$5.00", "600", "96%", "NZ$120.00"],
        ], caption="Averages only. Real sessions swing far above and below these figures, especially on high-volatility pokies.")
    )


# ---------------------------------------------------------------------------
# New online casinos
# ---------------------------------------------------------------------------
def new():
    return (
        '<h2 id="newest">Newest brands on our list, by licence date</h2>'
        + table(["Casino", "Licence", "Launched", "What to check"], [
            [link("trixino"), "Not confirmed", "2026 (reported)", "No independent profile yet; licence and owner unconfirmed"],
            [link("rivo"), "Anjouan, 2026", "Not published", "Euro-only limits of €1,000 a day"],
            [link("spino"), "Anjouan, 2025", "2025 (reported)", "Crypto only; no NZD"],
            [link("smash"), "Anjouan, 2024", "2024 (reported)", "Safety Index 3.9; €2,000 weekly limit"],
            [link("crownslots"), "Curaçao (reported)", "2024 (reported)", "Owner and licence number not published"],
            [link("gunsbet"), "Anjouan + Tobique, 2025", "2016 (reported)", "An older brand on new licences: not new, just relicensed"],
        ])
        + '<h2 id="new-vs-established">Are brand new online casinos better than established ones?</h2>'
        + table(["New casinos", "Established casinos"], [
            ["Bigger, more unusual offers (Trixino 777% at 7x, Rivo 1000% up to €10,000)", "Smaller offers, but a track record you can check"],
            ["Modern cashiers, more coins (Smash takes USDC and Solana)", "NZD balances and NZ$ limits (Gunsbet, Rooster Bet)"],
            ["No complaint history, good or bad", "Years of complaints showing how disputes end"],
            ["Often no independent safety profile", "Safety Index scores, such as Lucky7even's 8.9"],
        ])
        + '<h2 id="trends">What trends are shaping new online casinos in 2026?</h2>'
        "<ul><li><b>Low-wager headline offers.</b> " + link("smash") + " (10x deposit + bonus) and " + link("trixino") + " (7x, supplied) compete on wagering rather than size.</li>"
        "<li><b>Long multi-deposit packages.</b> " + link("rivo") + "'s offer runs across eight deposits.</li>"
        "<li><b>Crypto-first cashiers.</b> " + link("spino") + " takes only coins; stablecoins like USDT and USDC are now standard.</li>"
        "<li><b>Euro-only limits.</b> Several new brands publish limits in euros, so your bank converts every withdrawal.</li></ul>"
        + '<h2 id="red-flags">What are the red flags at a brand new casino?</h2>'
        + steps([
            ("No licence number in the footer", "A logo alone is not a licence. Trixino and Kingdom are examples where we could not confirm one."),
            ("No company name", "If the terms do not name the operator, you have no one to hold to account."),
            ("A bonus far above the market with no terms page", "Big percentages with hidden wagering or caps are the commonest trap."),
            ("Withdrawal limits missing from the terms", "If you cannot find them before depositing, ask support in writing."),
            ("A launch date after 1 May 2026 aimed at New Zealand", "Under the 2026 Act no new provider may enter the New Zealand market."),
        ])
        + '<h2 id="rebrands">Are new casinos just rebrands of older sites?</h2>'
        "<p>Often, yes. Groups launch new brands on the same platform, terms and payments team. That is not bad in itself, and it lets you judge a new brand by its sisters' record:</p>" + GROUPS
        + '<h2 id="new-payments">Which payment methods do new casinos support?</h2>'
        "<p>Expect cards, e-wallets and a long crypto list. " + link("rivo") + " lists 34 payment options including Apple Pay and American Express; " + link("smash") + " adds Solana and USDC. What new brands often lack is an NZD balance, so check the currency list before you sign up.</p>"
    )


# ---------------------------------------------------------------------------
# High payout
# ---------------------------------------------------------------------------
def high_payout():
    return (
        '<h2 id="audited">How RTP is calculated and audited</h2>'
        "<p>A game's RTP comes from its maths model: every possible outcome multiplied by its probability and payout. Independent labs such as GLI, iTech Labs and BMM test the random number generator and confirm the published RTP over millions of simulated rounds. The audit covers the game, not the casino, which is why the casino's chosen RTP setting matters.</p>"
        + '<h2 id="rtp-pokies">Highest RTP pokies</h2>'
        + table(["Pokie", "Studio", "Published top RTP"], [
            ["Book of 99", "Relax Gaming", "99%"], ["Mega Joker", "NetEnt", "Up to 99%"],
            ["1429 Uncharted Seas", "Thunderkick", "98.6%"], ["Blood Suckers", "NetEnt", "98%"],
            ["Starmania", "NextGen", "97.87%"],
        ], caption="Studio-published maximums. Open the paytable to see which version a casino runs.")
        + '<h2 id="blackjack-rules">Which blackjack rules raise or lower the payout?</h2>'
        + table(["Rule", "Effect on the house edge"], [
            ["Blackjack pays 6:5 instead of 3:2", "Adds about 1.4%: avoid"],
            ["Dealer hits soft 17", "Adds about 0.2%"],
            ["Double after split allowed", "Cuts about 0.14%"],
            ["Single deck instead of eight", "Cuts about 0.5%"],
            ["Late surrender allowed", "Cuts about 0.08%"],
        ], caption="Approximate effects with basic strategy, from standard blackjack rule calculations.")
        + '<h2 id="video-poker">Video poker</h2>'
        "<p>Full-pay Jacks or Better (9/6) returns about 99.5% with perfect strategy, and some Deuces Wild versions exceed 100%. The catch is the paytable: a 8/5 Jacks or Better drops to about 97.3%. Check the payout for a full house and a flush before you play.</p>"
        + '<h2 id="live-payout">Which live casino games pay out the most?</h2>'
        "<p>Live blackjack with basic strategy (about 99.5%) and baccarat on the banker bet (98.94%) lead. Live game shows such as Crazy Time return roughly 94% to 96% depending on the bet, well below the tables.</p>"
        + '<h2 id="bonus-payout">Which casino bonuses actually improve your payout?</h2>'
        "<p>Only low-wager ones. A bonus at 10x, like " + link("smash") + "'s, can add value on average; at 40x, like the reported " + link("lucky-circus") + " offer, the expected cost of clearing it usually exceeds the bonus. Many casinos also count high-RTP games at a reduced rate or exclude them from wagering, so check the game weighting list.</p>"
        + '<h2 id="high-rollers">Can high rollers cash out more?</h2>'
        "<p>Sometimes. VIP levels at the Hollycorn and Novatrix brands may lift the standard NZ$7,500 weekly limit, usually only by agreement. If you play at high stakes, ask for the VIP limit in writing before you deposit, and note that progressive jackpot wins are usually exempt from limits while normal wins are not.</p>"
        + '<h2 id="payout-schedule">How long a NZ$20,000 win takes to reach you</h2>'
        "<p>No ranking page converts limits into time. Here is the schedule at each casino on our list:</p>" + _win_schedule(20000)
        + '<h2 id="nz-tax">Do you pay tax on high payouts in New Zealand?</h2>'
        "<p>Not as a casual player: Inland Revenue does not treat gambling winnings as income. If gambling is your business, or you hold crypto that rises in value, tax can apply. See our <a href=\"/gambling-winnings-tax-nz/\">gambling winnings tax guide</a>.</p>"
    )


# ---------------------------------------------------------------------------
# Fast payout
# ---------------------------------------------------------------------------
def fast_payout():
    return (
        '<h2 id="types">Instant, under one hour and same-day withdrawals: what the labels mean</h2>'
        + table(["Label", "What it usually means", "Realistic method"], [
            ["Instant", "Automated approval for verified accounts under a set amount", "Crypto, some e-wallets"],
            ["Under 1 hour", "Approval within the hour, then the payment network's own time", "Crypto, Skrill, Neteller, MiFinity"],
            ["Same day", "Processed the same business day", "E-wallets; cards rarely"],
            ["Standard", "One to five working days after approval", "Cards and bank transfer"],
        ])
        + '<h2 id="stages">How a casino withdrawal is processed, step by step</h2>'
        + steps([
            ("You request the withdrawal", "From the cashier, using the method you deposited with where possible."),
            ("The casino's pending period", "Often 24 to 72 hours. Many casinos let you reverse the request here; do not."),
            ("Verification and review", "First withdrawals and large amounts trigger KYC or source-of-funds checks."),
            ("The payment provider processes it", "Minutes for crypto, hours for e-wallets, days for cards and bank transfers."),
            ("The money reaches your account", "If it has not arrived within the stated time, contact support with the transaction ID."),
        ])
        + '<h2 id="timing">Timing your withdrawal: NZ business hours, weekends and holidays</h2>'
        "<p>Offshore casinos usually run payments on European business hours, which are New Zealand's evenings and nights. A request made on a New Zealand Saturday or Sunday falls on the European weekend and may wait until Monday morning in Europe, which is Monday evening in New Zealand. Requests made on New Zealand weekday evenings (European mornings) tend to be processed fastest. Bank transfers also wait for New Zealand banking days, so public holidays add a day.</p>"
        + '<h2 id="first-withdrawal">Why your first withdrawal is always the slowest</h2>'
        "<p>It is the one that triggers full verification. Upload ID and proof of address straight after sign-up and make a small first withdrawal, such as NZ$50, to clear the checks before a large one is waiting.</p>"
        + '<h2 id="poli">Can you withdraw with POLi?</h2>'
        "<p>No. POLi is a deposit-only bank payment service. One 2026 review reports it as a deposit option at " + link("spinjo") + " and " + link("lucky-vibe") + ", but withdrawals go back by bank transfer or another method.</p>"
        + '<h2 id="limits-speed">Speed means little without limits: how much each casino pays per week</h2>'
        "<p>A fast cashier still cannot pay more than the limit. This is the comparison the ranking pages skip:</p>"
        + table(["Casino", "Daily", "Weekly", "Monthly"], [
            [link(s), *(BY[s]["limits"] + ["—"] * 3)[:3]] for s in
            ("spinjo", "lucky7even", "lucky-vibe", "rooster-bet", "fortune-play", "gunsbet", "madcasino")
        ] + [[link("smash"), "€1,000", "€2,000", "—"], [link("rivo"), "€1,000", "—", "€10,000"],
             [link("lucky-circus"), "—", "€2,500", "€10,000"]])
        + '<h2 id="slow-signs">Red flags of a slow-paying casino</h2>'
        + steps([
            ("Repeated document requests", "Asking again for documents you already supplied is a common stalling tactic."),
            ("Pending periods longer than the terms", "If the terms say 48 hours and it has been five days, escalate in writing."),
            ("Withdrawals reversed into your balance", "Some sites push you to keep playing. Turn off reversals if the setting exists."),
            ("Limits that appear only after a win", "Check the limits page before depositing and screenshot it."),
        ])
        + '<h2 id="fast-bonus">Bonuses at fast payout casinos</h2>'
        "<p>An active bonus is the biggest single cause of slow payouts, because nothing can be withdrawn until wagering is complete. If speed matters most, decline the welcome offer or choose a low-wager one such as " + link("smash") + "'s at 10x.</p>"
    )


# ---------------------------------------------------------------------------
# Crypto
# ---------------------------------------------------------------------------
def crypto():
    return (
        '<h2 id="vs-traditional">Crypto casinos vs traditional online casinos</h2>'
        + table(["", "Crypto casino", "Traditional casino"], [
            ["Deposit", "Minutes, after network confirmations", "Instant by card"],
            ["Withdrawal", "Often within hours once approved", "One to five working days by card or bank"],
            ["Fees", "Network fee, from cents (TRC-20 USDT, Litecoin) to dollars (Bitcoin, Ethereum)", "Usually none, plus conversion if not NZD"],
            ["Price risk", "Yes, unless you use a stablecoin", "None in NZD"],
            ["ID checks", "Still required at licensed casinos", "Required"],
        ])
        + '<h2 id="coins-by-casino">Which coins each casino on our list accepts</h2>'
        "<p>Ranking pages list coins in general. Here is what each casino's cashier actually shows in our records:</p>"
        + table(["Casino", "Coins listed", "NZD balance too?"], [
            [link(o["slug"]), ", ".join(p for p in o["payments"] if p in ("Bitcoin", "Ethereum", "Litecoin", "USDT", "USDC", "Solana", "Dogecoin", "XRP")) or "Crypto (coins not itemised)",
             {True: "Yes", False: "No", None: "Not confirmed"}[o["nzd"]]]
            for o in OPS if o["crypto"]
        ])
        + '<h2 id="hybrid">Crypto-only vs hybrid casinos</h2>'
        "<p>" + link("spino") + " is crypto-only: no NZD, and USD is the only fiat option. The Hollycorn and Novatrix brands are hybrids: you can hold NZD and still deposit with Bitcoin or Ethereum. For most Kiwis a hybrid is simpler, because winnings can go straight back to a New Zealand bank.</p>"
        + '<h2 id="provably-fair">What is provably fair?</h2>'
        "<p>Provably fair games publish a cryptographic hash of each round's result before you bet, plus a seed you can change. Afterwards you can check that the result matched the hash. It proves the round was not altered; it does not change the house edge.</p>"
        + '<h2 id="kyc">Do crypto casinos require KYC verification?</h2>'
        "<p>Licensed ones do, usually before your first withdrawal or above a set amount. 'No KYC' marketing usually means checks are delayed, not skipped, and that is a risk when you try to withdraw a large win.</p>"
        + '<h2 id="crypto-bonuses">Crypto casino bonuses</h2>'
        "<p>Crypto offers are often quoted in coins rather than dollars. " + link("spino") + "'s reported offer is 20% cashback up to 2,000 USDT with no wagering, which is easier to value than a large match bonus. Check whether the bonus is credited in the coin you deposited and whether wagering is counted in its dollar value.</p>"
        + '<h2 id="to-bank">Can a crypto casino pay out to my bank account?</h2>'
        "<p>Not directly from a crypto-only site. Withdraw to your own wallet, sell on a New Zealand exchange and withdraw NZD to your bank. Hybrid casinos can pay NZD by bank transfer instead.</p>"
        + '<h2 id="wrong-network">What if I send crypto on the wrong network?</h2>'
        + steps([
            ("Stop and do not send more", "Check the transaction hash on a block explorer to see where the funds went."),
            ("Contact the casino's support", "Give the hash, coin, network and amount. Some casinos can recover funds sent on a compatible network, for a fee."),
            ("Expect the worst on incompatible networks", "Funds sent on a network the casino's wallet does not support are usually lost."),
            ("Prevent it next time", "Always send a small test amount first and match the network name exactly."),
        ])
        + '<h2 id="crypto-pros-cons">Should you sign up at a crypto casino?</h2>'
        + table(["Why it might suit you", "Why it might not"], [
            ["You already hold crypto and know wallets", "You have never bought crypto before"],
            ["You want fast withdrawals once verified", "You want your balance to stay fixed in NZD"],
            ["You use stablecoins to avoid price swings", "You do not want to keep records for Inland Revenue"],
        ])
    )


# ---------------------------------------------------------------------------
# Live casinos
# ---------------------------------------------------------------------------
def live():
    return (
        '<h2 id="how-to-play">How to play live dealer casino games, step by step</h2>'
        + steps([
            ("Open the live lobby", "Filter by game and by minimum bet; tables show the stake range before you join."),
            ("Pick a table within your budget", "A NZ$5 minimum blackjack table needs a bigger bankroll than NZ$0.20 roulette."),
            ("Place your chips in the betting window", "A timer shows how long is left. Late bets are not accepted."),
            ("Watch the round and the result", "The dealer deals or spins in real time; results are read by cameras and sensors."),
            ("Collect, then decide", "Winnings are credited automatically. Use the history panel to track your session."),
        ])
        + '<h2 id="poker-craps">Live poker and live craps</h2>'
        "<p>Live casino poker, such as Casino Hold'em and Three Card Poker, is played against the dealer, not other players, with house edges of about 2% to 3.5% on the main bet. Live craps follows standard rules; the pass line edge is 1.41% and odds bets carry none.</p>"
        + '<h2 id="stakes">Low stakes vs high stakes live casino games</h2>'
        + table(["Game", "Typical minimum", "Typical maximum"], [
            ["Live roulette", "NZ$0.20 to NZ$1", "NZ$5,000+"], ["Live blackjack", "NZ$1 to NZ$5", "NZ$5,000+ (VIP tables more)"],
            ["Live baccarat", "NZ$1", "NZ$10,000+"], ["Game shows", "NZ$0.10", "NZ$1,000 to NZ$5,000"],
        ], caption="Typical ranges at Evolution and Pragmatic Play Live lobbies; each casino sets its own.")
        + '<h2 id="providers">Live casino software providers</h2>'
        "<p>Evolution runs most live lobbies worldwide, including Lightning Roulette and Crazy Time. Pragmatic Play Live, Playtech Live and Ezugi are the main alternatives. A lobby with several providers gives more table limits and more tables open at New Zealand hours.</p>"
        + '<h2 id="live-vs-rng">Live dealer games vs regular online table games</h2>'
        + table(["", "Live dealer", "RNG (computer) version"], [
            ["Speed", "About 50 to 60 hands or spins an hour", "Several hundred an hour"],
            ["Minimum bet", "Higher", "Often NZ$0.10"],
            ["House edge", "Same rules, same edge", "Same rules, same edge"],
            ["Bonus wagering", "Often 0% to 10%", "Often 10% to 20%"],
        ])
        + '<h2 id="live-bonus">Live casino bonuses: do they work on live games?</h2>'
        "<p>Mostly not. Welcome bonuses usually weight live games at 0% to 10% towards wagering, so a 40x bonus would take ten times longer to clear. Look for live cashback instead, or play live games with your own money and leave bonuses for pokies.</p>"
        + '<h2 id="live-bankroll">How much do you need for a live session?</h2>'
        "<p>A simple rule from blackjack players: bring 20 to 40 times the table minimum. At a NZ$5 table that is NZ$100 to NZ$200. At 60 hands an hour and a 0.5% edge with basic strategy, the average cost is about NZ$1.50 an hour at NZ$5 a hand; the swings are far larger than that average.</p>"
        + '<h2 id="live-pros-cons">Pros and cons of live casinos</h2>'
        + table(["Pros", "Cons"], [
            ["Real cards and wheels, visible on camera", "Higher minimum bets"], ["Chat with dealers", "Slower, so less play per dollar of bonus"],
            ["Same low edges as land-based tables", "Needs a stable connection"],
        ])
    )


# ---------------------------------------------------------------------------
# Bonuses
# ---------------------------------------------------------------------------
def bonuses():
    return (
        '<h2 id="claim">How to claim a casino bonus, step by step</h2>'
        + steps([
            ("Read the full bonus terms first", "Wagering, max bet, game weighting, expiry and any cap on winnings. If you cannot find them, do not claim."),
            ("Register with your real details", "Mismatched details are the usual reason bonus winnings are confiscated."),
            ("Verify your account", "Some casinos only release bonus winnings to verified accounts."),
            ("Opt in or enter the code", "Tick the bonus box or enter the code before you pay. Most bonuses cannot be added afterwards."),
            ("Deposit the qualifying amount by an eligible method", "Check the minimum and that your payment method is not excluded."),
            ("Play eligible games within the max bet", "Track wagering progress in your account. Stop if you hit your own limit."),
            ("Withdraw once wagering is complete", "Then request a withdrawal before claiming another offer."),
        ])
        + '<h2 id="compare-dollars">Bonus wagering compared, in dollars</h2>'
        "<p>Ranking pages list wagering multiples. This table turns the multiples on our list into what you must bet on a NZ$100 bonus:</p>"
        + table(["Wagering", "Example on our list", "Bet needed on a NZ$100 bonus", "Average cost at 96% RTP"], [
            ["7x bonus", f'{link("trixino")} (supplied)', "NZ$700", "NZ$28"],
            ["10x deposit + bonus", f'{link("smash")}', "NZ$2,000 (on NZ$100 + NZ$100)", "NZ$80"],
            ["30x bonus", f'{link("madcasino")} (reported)', "NZ$3,000", "NZ$120"],
            ["40x bonus", f'{link("lucky-circus")}, {link("rooster-bet")} (reported)', "NZ$4,000", "NZ$160"],
        ], caption="Average cost = amount wagered × 4%. If the average cost is more than the bonus, the bonus is worth less than nothing on average.")
        + '<h2 id="codes">What are casino bonus codes?</h2>'
        "<p>A code tells the cashier which offer to apply. Some casinos need a code for every stage of a welcome package; others apply the first stage automatically. A code found on a third-party site is no guarantee the offer exists: if the cashier rejects it, the published terms on the casino's own site are what count.</p>"
        + '<h2 id="clearing">Which games are best for clearing a bonus?</h2>'
        "<p>Pokies usually count 100%; table and live games 0% to 20%. Within pokies, low-volatility games give steadier progress through wagering, while high-volatility games are more likely to bust the balance early or produce one large win. Many terms ban bonus buys and certain high-RTP games during wagering.</p>"
        + '<h2 id="excluded-methods">Payment methods that can void a bonus</h2>'
        "<p>Skrill and Neteller deposits are excluded from welcome offers at many casinos, and some exclude prepaid vouchers or crypto. Check the bonus terms for 'excluded payment methods' before you deposit.</p>"
        + '<h2 id="special">High roller, live casino and crypto bonuses</h2>'
        "<p>High roller bonuses need a large first deposit for a higher cap. Live casino bonuses are rare because live games count little towards wagering; cashback is the usual alternative. Crypto bonuses may be quoted in coins, like " + link("spino") + "'s reported 20% cashback up to 2,000 USDT.</p>"
        + '<h2 id="sports-alt">Casino or sports welcome: choose one</h2>'
        "<p>Combined accounts usually let you take one welcome offer, not both. " + link("madcasino") + " offers 777% up to €7,500 on the casino or 250% up to €3,500 on sport (supplied); " + link("smash") + " 600% up to €10,000 at 10x or 250% up to €5,000 at 15x on odds of 1.80+. If you mainly bet on sport, the sports offer usually has the easier rollover.</p>"
        + '<h2 id="bonus-pros-cons">Are casino bonuses worth claiming?</h2>'
        + table(["Advantages", "Disadvantages"], [
            ["More play for the same deposit", "Locks your balance until wagering is done"],
            ["Low-wager offers can add real value", "Max bet rules are easy to break by accident"],
            ["Free spins let you try new pokies", "Winnings may be capped"],
        ])
    )


# ---------------------------------------------------------------------------
# No deposit
# ---------------------------------------------------------------------------
def no_deposit():
    return (
        '<h2 id="claim-steps">How to claim a no deposit bonus in five steps</h2>'
        + steps([
            ("Choose a casino you have checked", "A free offer at an unlicensed site is still a risk to your details."),
            ("Create your account with accurate details", "Name, date of birth and address must match your ID."),
            ("Verify your email or mobile number", "Most casinos only credit the bonus after the confirmation link or code."),
            ("Enter the bonus code if one is required", "In the cashier or promotions page, before you play."),
            ("Open the eligible game", "Free spins only work on the named pokie at a fixed stake."),
        ])
        + '<h2 id="real-money">Turning a no deposit bonus into real money: four rules</h2>'
        + steps([
            ("Complete the wagering", "Usually 40x to 60x the winnings from free spins."),
            ("Stay within the max bet", "Often NZ$5 or less per spin; one bigger bet can void everything."),
            ("Respect the max cashout", "Typically NZ$50 to NZ$100, whatever you win."),
            ("Verify before withdrawing", "And expect to make a small deposit first at many casinos, to confirm a payment method."),
        ])
        + '<h2 id="nd-types">Types of no deposit bonus</h2>'
        + table(["Type", "What you get", "Watch for"], [
            ["Free spins", "A set number of spins on one pokie", "Fixed stake, wagering on winnings"],
            ["Bonus credit", "A small cash balance", "Game restrictions, max bet"],
            ["No wagering spins", "Winnings paid as cash", "Usually very few spins"],
            ["Cashback for existing players", "A share of losses back", f'{link("spino")}: 20% up to 2,000 USDT, no wagering (reported)'],
        ])
        + '<h2 id="best-games">Best games to use a no deposit bonus on</h2>'
        "<p>You rarely get to choose: free spins are tied to one pokie. For bonus credit, low-volatility pokies such as Starburst or Blood Suckers stretch a small balance through wagering further than high-volatility games.</p>"
        + '<h2 id="existing">No deposit offers for existing players</h2>'
        "<p>Loyalty programmes, birthday spins and cashback are the realistic 'no deposit' offers once you have an account. Cashback with no wagering is the cleanest, because what you receive is real money.</p>"
        + '<h2 id="terms">Key terms: expiry, excluded games and withdrawal amounts</h2>'
        "<p>No deposit bonuses often expire within 24 hours to 7 days if unused, and winnings may need wagering within a few days more. Excluded games and the max cashout sit in the bonus terms, not the banner.</p>"
        + '<h2 id="nd-alternatives">Low-risk alternatives on our list</h2>'
        "<p>We have no confirmed no deposit offer on record for any casino here. The closest alternatives are low-wager deposit offers, such as " + link("smash") + "'s at 10x, and free demo play, which every pokie studio offers without an account.</p>"
        + '<h2 id="nd-pros-cons">Pros and cons of a no deposit bonus</h2>'
        + table(["Pros", "Cons"], [
            ["Try a casino without risking money", "Small max cashout"], ["Learn a pokie's features", "High wagering on winnings"],
            ["Test verification and support", "Often needs a deposit before withdrawal"],
        ])
    )


# ---------------------------------------------------------------------------
# Betting pages
# ---------------------------------------------------------------------------
def online_betting():
    return (
        '<h2 id="delays">Why live bets are delayed and markets suspend</h2>'
        "<p>In-play bets carry a delay of a few seconds so the bookmaker can check that the price has not moved. Markets suspend whenever something significant may happen, such as a try, a wicket or a penalty. If your bet is rejected, the price changed during the delay.</p>"
        + '<h2 id="football-markets">Football betting markets explained</h2>'
        + table(["Market", "What you are betting on"], [
            ["Match result (1X2)", "Home win, draw or away win"], ["Both teams to score (BTTS)", "Each side scores at least once"],
            ["Over/under goals", "Total goals above or below a line, such as 2.5"], ["Asian handicap", "A head start that removes the draw, with half or quarter lines"],
            ["Bet builder", "Several outcomes in one match combined into one bet"], ["Futures", "Long-term results such as a league winner"],
        ])
        + '<h2 id="rugby-cricket">Rugby, league and cricket in-play</h2>'
        "<p>Rugby markets move most after tries and cards; line (handicap) betting is the main market. In league, momentum swings after sin-bins. In cricket, prices move ball by ball, so in-play delays are longest and suspensions most frequent.</p>"
        + '<h2 id="apps">Betting apps in New Zealand</h2>'
        "<p>TAB NZ's app covers sport and streams New Zealand racing; Betcha runs its own app under the same framework. Offshore apps are not authorised to take bets from New Zealanders since 28 June 2025.</p>"
        + '<h2 id="how-we-review-bet">How we review a betting site, step by step</h2>' + _bet_review_steps()
        + '<h2 id="win-caps">Win caps on combined casino and sports accounts</h2>'
        "<p>No ranking page mentions this, but it decides what a big multi actually pays: " + link("betandplay") + " does not pay net daily winnings above US$50,000, and " + link("smash") + " and " + link("rivo") + " cap daily wins at €100,000.</p>"
    )


def _bet_review_steps():
    return steps([
        ("Legal status and licence", "Is the operator allowed to take bets from New Zealanders? Since 2025, only TAB NZ and Betcha are."),
        ("Markets and coverage", "Rugby, league, cricket, netball, football and racing depth."),
        ("Odds and margin", "We calculate the bookmaker margin on main markets."),
        ("Apps and platform", "Speed, bet slip, cash-out and streaming."),
        ("Payments and payouts", "NZD support, withdrawal limits and win caps."),
        ("Safety tools", "Deposit limits, time-outs and self-exclusion."),
        ("Support", "Response times and complaint routes."),
        ("Ongoing checks", "We recheck licences and limits monthly."),
    ])


def sports_sites():
    return (
        '<h2 id="how-we-review-bet">How we review betting sites, step by step</h2>' + _bet_review_steps()
        + '<h2 id="nzd-books">Betting sites that accept New Zealand dollars</h2>'
        + table(["Sportsbook", "NZD balance", "Withdrawal limits", "Daily win cap"], [
            [link(o["slug"]), {True: "Yes", False: "No", None: "Not confirmed"}[o["nzd"]],
             ", ".join(o["limits"]) or "Not published", o["win_cap"] or "None published"] for o in SPORTS
        ])
        + '<h2 id="sports-bonuses">Sports welcome bonuses compared</h2>'
        + table(["Sportsbook", "Sports offer on record", "Rollover"], [
            [link("madcasino"), "250% up to €3,500 (supplied)", "Not confirmed"],
            [link("smash"), "250% up to €5,000 (supplied)", "15x at odds of 1.80+"],
            [link("rivo"), "100% up to €500 (supplied)", "Not confirmed"],
            [link("betandplay"), "100% up to NZ$500 (reported)", "5x at odds of 1.80+"],
            [link("gunsbet"), "285% up to €7,500 + 285 free spins (supplied, same headline as casino)", "Not confirmed"],
        ])
        + '<h2 id="bet-payments">Depositing and withdrawing at betting sites</h2>'
        "<p>The same rules as casinos apply: verify early, withdraw by the method you deposited with, and settle open bets first. Win caps matter more for punters, because one big multi can exceed them: " + link("betandplay") + " caps net daily winnings at US$50,000.</p>"
        + '<h2 id="why-offshore">Why punters compared offshore sites with TAB NZ</h2>'
        "<p>Before 2025, offshore books advertised bigger bonuses, more markets and sharper prices on some sports. Since 28 June 2025 they may not take bets from New Zealanders, so those comparisons no longer lead anywhere lawful. TAB NZ and Betcha are the options; compare their prices with the margin method on our <a href=\"/online-betting/\">online betting guide</a>.</p>"
        + '<h2 id="best-for">Best betting sites for rugby, football and cricket</h2>'
        "<p>For New Zealand punters the lawful answer for all three is TAB NZ or Betcha. TAB NZ has the deepest racing and domestic rugby coverage; Betcha runs on the same licence with a newer app. For international football, both offer markets on the Premier League, A-League (including Wellington Phoenix) and Champions League.</p>"
    )


# ---------------------------------------------------------------------------
# Casino reviews hub
# ---------------------------------------------------------------------------
def reviews():
    return (
        '<h2 id="review-steps">How we review a casino, step by step</h2>'
        + steps([
            ("Confirm the licence", "We look the number up on the regulator's register, not the casino's footer."),
            ("Identify the owner", "A named company, cross-checked against independent databases."),
            ("Read the full terms", "Withdrawal limits, win caps, bonus rules and account closure terms."),
            ("Check banking for Kiwis", "NZD balance, number of payment methods and crypto."),
            ("Record independent safety data", "Casino Guru's Safety Index and complaint count."),
            ("Read player reviews", "Trustpilot scores and the pattern of complaints, not single stories."),
            ("Score and date it", "Five weighted inputs, published with the date we checked."),
            ("Recheck monthly", "Licences and owners change; so do our scores."),
        ])
        + '<h2 id="types">Types of casino we review</h2>'
        + table(["Type", "Examples on our list"], [
            ["Casino only", f'{link("crownslots")}, {link("spinjo")}, {link("lucky7even")}, {link("lucky-circus")}'],
            ["Casino and sportsbook", f'{link("madcasino")}, {link("lucky-vibe")}, {link("rooster-bet")}, {link("fortune-play")}, {link("kingdom")}, {link("smash")}, {link("trixino")}, {link("rivo")}'],
            ["Sportsbook listings", f'{link("gunsbet")}, {link("betandplay")}'],
            ["Crypto first", link("spino")],
        ])
        + '<h2 id="own-research">Do your own research in five steps</h2>'
        + steps([
            ("Find the licence number", "In the footer of the casino site."),
            ("Look it up on the register", "Anjouan, Tobique, Curaçao and Estonia all publish online registers."),
            ("Check the owner and sister sites", "A group with a clean record is a lower risk than an anonymous brand."),
            ("Read recent complaints", "Look for patterns: withdrawals refused, accounts closed after wins."),
            ("Test with a small withdrawal", "Before you deposit more."),
        ])
        + '<h2 id="red-terms">Red-flag terms in casino T&amp;Cs</h2>'
        "<ul><li><b>Discretionary account closure</b> with 'confiscation of winnings'.</li>"
        "<li><b>Withdrawal limits</b> that are low or missing.</li>"
        "<li><b>Daily win caps</b>, such as US$50,000 net at " + link("lucky-circus") + " and " + link("betandplay") + ".</li>"
        "<li><b>'Irregular play'</b> clauses without a definition.</li>"
        "<li><b>Dormant account fees</b> that eat inactive balances.</li></ul>"
        + '<h2 id="groups">Sister sites: who owns which casino</h2>'
        "<p>No other review hub maps ownership like this. A dispute with one brand often involves the same team as its sisters:</p>" + GROUPS
        + '<h2 id="complain">How to make a complaint, step by step</h2>' + steps(COMPLAIN_STEPS)
        + '<h2 id="caution">Casinos to approach with caution</h2>'
        "<p>" + link("kingdom") + ", " + link("trixino") + " and " + link("crownslots") + " score below 5 mainly because we could not confirm a licence or an owner. That does not prove they are unsafe; it means there is nobody we can confirm you could hold to account.</p>"
    )


SECTIONS = {
    "/": home, "/online-pokies/": pokies, "/new-online-casinos/": new, "/high-payout-casinos/": high_payout,
    "/fast-payout-casinos/": fast_payout, "/best-crypto-casinos/": crypto, "/live-casinos/": live,
    "/online-casinos/bonuses/": bonuses, "/no-deposit-casinos/": no_deposit, "/online-betting/": online_betting,
    "/best-sports-betting-sites/": sports_sites, "/casino-reviews/": reviews,
}


def extra(path):
    f = SECTIONS.get(path)
    return f() if f else ""


# Extra FAQs: competitor questions our pages did not already answer.
FAQS = {
    "/": [
        ("Can you win real money on online casinos in New Zealand?",
         "<p>Yes. Winnings are paid in real money, and casual winnings are not taxed in New Zealand. How fast you receive a large win depends on the casino's withdrawal limits.</p>"),
        ("What is the legal gambling age in New Zealand?",
         "<p>18 for online casinos and Lotto, and 20 to enter a land-based casino.</p>"),
    ],
    "/online-pokies/": [
        ("What is the difference between pokies and slots?",
         "<p>None. 'Pokies' is the Australian and New Zealand name for slot machines, from 'poker machine'.</p>"),
        ("Do pokies pay out more at certain times of day?",
         "<p>No. Each spin is decided by a random number generator, independent of the time and of previous spins.</p>"),
        ("What changes for NZ pokies players on 1 December 2026?",
         "<p>Offshore casinos without a pending licence application must stop serving New Zealand. None of the companies behind the casinos on this page won a place in the October 2026 licence auction.</p>"),
    ],
    "/new-online-casinos/": [
        ("What happens to my balance if a new casino closes?",
         "<p>Offshore casinos do not have to hold player money separately, and no New Zealand scheme covers it. Keep balances small and withdraw regularly.</p>"),
        ("Do new casinos really pay out faster?",
         "<p>Not necessarily. Payout speed depends on verification, the payment method and the casino's staffing, not its age.</p>"),
    ],
    "/high-payout-casinos/": [
        ("Who sets the RTP on casino games?",
         "<p>The game studio sets the available RTP versions; the casino chooses which one to run.</p>"),
        ("Is the RTP lower when playing with bonus funds?",
         "<p>No, the game's RTP is the same, but wagering requirements raise the total you must bet and so the expected cost.</p>"),
    ],
    "/fast-payout-casinos/": [
        ("Do casinos process withdrawals on weekends?",
         "<p>Some do, many do not. Requests made over the New Zealand weekend often wait until Monday evening New Zealand time, when the European working week starts.</p>"),
        ("Can I split a large win into smaller withdrawals?",
         "<p>Yes, and with daily limits you usually have to. Several smaller requests within the limit can also avoid manual review.</p>"),
    ],
    "/best-crypto-casinos/": [
        ("Does crypto price volatility affect my casino balance?",
         "<p>Yes, if the casino holds your balance in that coin. Stablecoins such as USDT avoid it.</p>"),
        ("Can I use Bitcoin anonymously at online casinos?",
         "<p>Not at licensed casinos, which verify identity before withdrawals. The blockchain itself is public, not anonymous.</p>"),
    ],
    "/live-casinos/": [
        ("Are live casino dealers real?",
         "<p>Yes. They work in studios run by providers such as Evolution and are filmed in real time.</p>"),
        ("Are live dealer games available 24/7 in NZ?",
         "<p>Most popular games run around the clock, but the number of open tables is lower in European night hours, which fall in the New Zealand afternoon.</p>"),
    ],
    "/online-casinos/bonuses/": [
        ("Can I have more than one active bonus at a time?",
         "<p>Usually not. Most casinos queue a second bonus until the first is cleared or forfeited.</p>"),
        ("Can I use bonus buy on a pokie while wagering is active?",
         "<p>Usually not. Bonus buys are commonly banned during wagering and using one can void the bonus.</p>"),
        ("Are casino bonus winnings taxable in NZ?",
         "<p>Not for casual players. Inland Revenue does not treat gambling winnings as income.</p>"),
    ],
    "/no-deposit-casinos/": [
        ("Can I get multiple no deposit bonuses from the same casino?",
         "<p>One per person, household and payment method is the usual rule. Sister sites may also count as the same casino.</p>"),
        ("Are no deposit bonuses really free?",
         "<p>They cost no money to claim, but wagering, caps and the usual need to deposit before withdrawing mean the value is small.</p>"),
    ],
    "/online-betting/": [
        ("Why are live bets delayed?",
         "<p>A delay of a few seconds lets the bookmaker confirm the price has not changed. If it has, the bet is rejected or re-priced.</p>"),
        ("Is cash out guaranteed on live bets?",
         "<p>No. Cash out can be suspended at any time, especially during key moments of a match.</p>"),
    ],
    "/best-sports-betting-sites/": [
        ("Is Betcha better than TAB?",
         "<p>They run on the same licence. Betcha is a newer online brand with a different app; TAB NZ has the deepest racing coverage. Compare prices on the events you bet on.</p>"),
        ("Can I get in trouble for using an overseas betting site?",
         "<p>The 2025 law targets the bookmakers and anyone promoting them, not individual punters, but offshore books may not take your bets and you have no New Zealand complaint route.</p>"),
    ],
    "/casino-reviews/": [
        ("How do I know if a casino review is honest?",
         "<p>Look for sources and dates on every fact, a published scoring method and negative findings as well as positive ones.</p>"),
        ("Why do some reviews score a casino highly while yours does not?",
         "<p>Many rankings weight bonus size heavily. Ours weights independent safety, licence and ownership, which is why unconfirmed brands score low here.</p>"),
    ],
}


def extra_faqs(path):
    return FAQS.get(path, [])
