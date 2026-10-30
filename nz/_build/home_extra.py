"""Homepage sections added from the SERP, Reddit, Trustpilot, Trends and statistics research (8 October 2026)."""
from lib import *

TP_THEMES = [("Withdrawals delayed or refused", 52, "148 of 285"), ("Customer support", 36, "102"), ("Verification documents", 33, "94"),
             ("Bonus terms", 24, "68"), ("Claims the games are rigged", 19, "55"), ("Winnings confiscated or voided", 11, "30"),
             ("Praise for fast payouts", 5, "13"), ("Limits and caps", 4, "11"), ("Account closed or blocked", 3, "9")]


def numbers():
    return (
        '<h2 id="numbers">New Zealand online gambling in numbers</h2>'
        + "<p>Context helps when you weigh up any casino. Here is what the official and independent data says about how much "
          "New Zealanders gamble, where the money goes, and how many people are affected.</p>"
        + '<div class="stat-grid">'
          '<div class="stat"><b>NZ$1.36bn</b><span>New Zealand online gambling market, 12 months to September 2025</span><small>Dot Loves Data analysis for the DIA, reported by Newsroom</small></div>'
          '<div class="stat"><b>80%+</b><span>of online spend goes to the top 15 providers</span><small>Same analysis</small></div>'
          '<div class="stat"><b>NZ$342m–500m</b><span>estimated yearly spend with offshore online operators</span><small>Ministry of Health economic costing of gambling, 2025</small></div>'
          '<div class="stat"><b>22%</b><span>of adults affected at some point by their own or someone else\'s gambling</span><small>Problem Gambling Foundation</small></div>'
          "</div>"
        + "<h3>Where New Zealanders' gambling losses go (regulated sector)</h3>"
        + barchart([("Pokie machines in pubs and clubs", 1037), ("Lotto NZ products", 792), ("Land-based casinos", 592), ("TAB NZ betting", 371)],
                   unit="NZ$", caption="Amount lost by gamblers (operators' profit), NZ$ million, 2023/24. Total NZ$2,792 million. "
                   "Source: Department of Internal Affairs gambling expenditure statistics. Offshore online casinos are not included.")
        + "<h3>Five-year trend in regulated gambling losses</h3>"
        + barchart([("2019/20", 2252), ("2020/21", 2625), ("2021/22", 2254, "year of Delta lockdowns"), ("2022/23", 2761), ("2023/24", 2792)],
                   unit="NZ$", caption="Total lost by gamblers across TAB NZ, Lotto NZ, pub and club pokies and casinos, NZ$ million. Source: DIA.")
        + "<p>Losses in the regulated sector rose from NZ$2,252 million in 2019/20 to NZ$2,792 million in 2023/24, an increase of "
          "about 24% in four years. Pokie machines outside casinos remain the largest single source of losses and, according to "
          "the Problem Gambling Foundation, of people seeking help. Online is growing fastest: Lotto NZ's online products now make "
          "up 44% of its sales, according to the Ministry of Health's 2025 gambling harm strategy.</p>"
        + table(["Measure", "Figure", "Source"], [
            ["Adults who gambled in the past year", "About 69%", "Health and Lifestyles Survey 2020, via PGF"],
            ["Adults who gambled online", "Nearly 30%", "Health and Lifestyles Survey 2020, via PGF"],
            ["Adults who gambled on overseas websites", "2.6%", "Health and Lifestyles Survey 2020, via PGF"],
            ["Offshore spend identified in tax records, year to June 2023", "NZ$342.5 million", "Offshore gambling duty data, reported by The Modern Regulator"],
            ["Maximum new online casino licences", "15", "Online Casino Gambling Act 2026"],
        ], caption="Survey figures predate the 2026 law; newer national survey results are published by the Ministry of Health.")
    )


def complaints():
    ops = [o for o in OPS if o.get("tp_score") is not None]
    ops_sorted = sorted(ops, key=lambda o: -o["tp_score"])
    gone = [o["name"] for o in OPS if "removed" in (o.get("tp_note") or "")]
    return (
        '<h2 id="complaints">What players actually complain about</h2>'
        + "<p>We read the most recent Trustpilot reviews shown for 13 of the brands on this page, 285 reviews in all, and "
          "tagged what each one was about. A review can mention several things, so the percentages add up to more than 100.</p>"
        + barchart([(t, v, f"{n} reviews") for t, v, n in TP_THEMES], suffix="%", cls="chart--warn",
                   caption=f"Share of 285 recent Trustpilot reviews mentioning each topic, read {CHECKED}. Trustpilot does not verify "
                   "reviews, and unhappy customers are more likely to post.")
        + "<p>Two lessons stand out. First, more than half of all complaints are about getting money out, not about games or "
          "bonuses, which is why our scores weight limits, licences and ownership so heavily. Second, a third mention "
          "verification: most delays happen because ID checks start only when a player first asks to withdraw.</p>"
        + "<h3>Trustpilot scores for the brands on this page</h3>"
        + table(["Site", "TrustScore", "Reviews", "Ledger score"], [
            [op_cell(o), f'{o["tp_score"]:.1f} / 5', str(o["tp_reviews"]), f'{o["rating"]:.1f}'] for o in ops_sorted
        ], caption=f"Read {CHECKED}.")
        + note(f"<p>Trustpilot has <b>suspended Spinjo's rating</b> for a breach of its guidelines, and has <b>removed the profiles</b> "
               f"of {', '.join(gone[:-1])} and {gone[-1]}. MadCasino, Kingdom and Spino have no profile we could find. A missing or suspended profile "
               "is not proof of wrongdoing, but it removes one of the few public signals players have.</p>", "warn",
               "Suspended and removed profiles")
        + "<p>Why don't we simply rank by Trustpilot? Because the scores are thin (CrownSlots has seven reviews), unverified, and "
          "skewed towards people with a problem. We show them so you can see the pattern, and we keep our own score on facts "
          "that can be checked.</p>"
    )


def trending():
    return (
        '<h3 id="leak">October 2026: what the Curaçao leak revealed</h3>'
        + "<p>In late September 2026 more than 84,000 internal documents from the Curaçao Gaming Authority were leaked. Reporting by "
          "Newsroom on 5 October showed that SpinBet, which describes itself as New Zealand's number one online casino, planned its "
          "growth around gambling streamers and influencers, including New Zealand creators, and that its owner reported revenue of "
          "€83 million in 2024. SpinBet and four influencers had already been fined by the DIA in 2025 for promoting gambling. "
          "SpinBet is not on our list, but the story shows why influencer and affiliate promotion is now a target for enforcement, "
          "and why a casino's marketing tells you little about how it treats players.</p>"
        + '<h3 id="searches">Why searches for online casinos fell in 2026</h3>'
        + "<p>Google Trends shows New Zealand searches for \"online casino\" averaging about 36 on its relative scale from October "
          "2025 to March 2026, and about 11 from May to October 2026, a drop of roughly 70%. The fall came in one step in early "
          "April, straight after a spike in late March. Many of the 'rising' searches over the period were for spam casino-list "
          "domains, which suggests part of the earlier volume was automated search manipulation rather than real interest. "
          "Genuine rising searches include \"best paying online casino\", \"live casino online\" and \"nz online casino real "
          "money\". Interest in TAB NZ peaks around November, during the spring racing carnival.</p>"
        + '<h3 id="auction">Who will get a licence?</h3>'
        + f"<p>{AUCTION_SUMMARY} They include SkyCity, TAB New Zealand and Stake New Zealand; the full list is on our "
          f'<a href="/nz-online-casino-law/#auction">NZ online casino law</a> page. {NOT_IN_AUCTION}</p>'
    )


QUESTIONS = [
 ("Can an online casino refuse to pay out or hold my winnings?", "refuse",
  "<p>Yes, within its terms, and that is the most common complaint we see. A casino can delay or refuse a withdrawal if "
  "verification is incomplete, if a bonus term was broken (most often the maximum bet while a bonus is active), if the "
  "withdrawal exceeds its limits, or if it suspects duplicate accounts or 'irregular play'. Some go further than their "
  "terms allow. Your protection depends on the licence: the operator's complaints process first, then the regulator named "
  "on the licence. An offshore licence offers far less than a New Zealand one will, which is why this site leads with "
  "licence and owner details. Keep screenshots of your balance, bets and every message.</p>"),
 ("Can online casinos ban you for winning or close your account?", "ban",
  "<p>Offshore casinos usually reserve the right to close accounts at their discretion. A legitimate casino should still pay a "
  "balance that was won within the terms. Closures after a big win are often justified by bonus abuse, multiple accounts or "
  "'advantage play' clauses, so read those terms before you take a bonus. Bookmakers restricting consistently winning "
  "customers is a separate, long-standing practice, and New Zealand punters on Reddit report it at both offshore books and "
  "TAB NZ.</p>"),
 ("Can online casinos change the RTP or rig the games?", "rtp",
  "<p>A casino cannot change how a certified game behaves spin by spin, but it can choose which RTP version of a game to run, "
  "and many popular pokies are sold at several settings. The difference between 96% and 91% is about NZ$5 more lost per "
  "NZ$100 wagered on average. Check the RTP in the game's information panel and compare it with the studio's published "
  "figure. One in five recent Trustpilot complaints we read claimed games were rigged; most describe ordinary losing runs, "
  "which high-volatility pokies produce often.</p>"),
 ("Why is my withdrawal taking so long, and does the weekend matter?", "slow",
  "<p>A withdrawal has three stages: the casino's own pending period, verification, and the payment method. Many casinos "
  "approve withdrawals manually and work reduced hours at weekends, and international transfers generally do not settle "
  "on weekends or public holidays, so a request made on Friday night can easily take until Tuesday. Verify your "
  "account straight after sign-up, withdraw by the method you deposited with, and avoid having an active bonus. See "
  '<a href="/fast-payout-casinos/">fast payout casinos</a>.</p>'),
 ("What is a 'no verification' casino, and should I use one?", "kyc",
  "<p>'No verification' or 'no KYC' casinos let you play and sometimes withdraw without ID checks, usually with crypto. They "
  "are the lightest-regulated end of the market. Licensed casinos must check identity under anti-money-laundering rules, and "
  "licensed New Zealand casinos will have to verify that players are 18 or over. A casino that never checks who you are is "
  "also one that can more easily refuse a large withdrawal by asking for documents at the last minute.</p>"),
 ("My bank is asking about a big win from an overseas casino. What now?", "bank",
  "<p>Banks must monitor large or unusual international payments under anti-money-laundering law, so a large deposit from an "
  "offshore gambling company can trigger questions. Answer them: keep the casino's transaction history, withdrawal "
  "confirmations and your ID documents, and explain the source. Winnings from casual gambling are not taxable income in New "
  "Zealand, so there is normally nothing to declare to Inland Revenue, but your bank still needs to understand where the "
  "money came from.</p>"),
 ("Do online casinos take tax off my winnings?", "tax",
  "<p>No casino on this list deducts New Zealand tax, and New Zealand does not tax casual gambling winnings. The '30% "
  "withholding' figure you may see online applies to non-residents winning at US-based operators. Beware of scams: anyone "
  "asking you to pay a 'tax' or 'release fee' before receiving a prize or withdrawal is trying to defraud you. See "
  '<a href="/gambling-winnings-tax-nz/">gambling winnings tax</a>.</p>'),
 ("Can I use PayPal, Apple Pay, a Prezzy card or POLi?", "payments",
  "<p><b>PayPal</b>: none of the payment lists we checked for these 17 brands includes it. <b>Apple Pay</b>: listed at "
  "MadCasino, Smash, Rivo and Ivibet. <b>Prezzy card</b>: a prepaid Visa, so it may work where Visa does, but it "
  "cannot receive withdrawals. <b>POLi</b>: still running in New Zealand, but rare offshore; one 2026 review reports it at "
  "Spinjo and Lucky Vibe. Full details: <a href=\"/payment-methods/\">payment methods</a>.</p>"),
 ("Are NZ$1, NZ$5 and NZ$10 deposit casinos worth it?", "low-deposit",
  "<p>A low minimum deposit is good for trying a site cheaply, but check two other numbers: the minimum deposit needed to "
  "qualify for any bonus (often NZ$20 to NZ$35 or the euro equivalent), and the minimum withdrawal. Some payment methods "
  "also have their own minimums. A NZ$10 deposit that cannot be withdrawn until it grows past a NZ$50 minimum is not really "
  "a NZ$10 casino.</p>"),
 ("Is SkyCity online or Lotto NZ a safer option?", "local",
  "<p>Lotto NZ is the lawful national lottery operator and sells lottery and instant games online through MyLotto, under "
  "New Zealand rules. SkyCity Online Casino is a different case: it is run by Gaming Innovation Group on behalf of SkyCity "
  "Malta Limited and licensed by the Malta Gaming Authority (MGA/B2C/880/2021), so, like the brands on this page, it is an "
  "offshore-licensed casino until New Zealand licences are issued. In March 2026 RNZ reported that a US-funded group is suing "
  "SkyCity over the Malta arrangement. Reddit users report the same verification delays there as at other casinos. The "
  "advantage of both is a New Zealand-based parent company that is accountable here.</p>"),
 ("What happens to my money if a casino closes or leaves New Zealand?", "closing",
  "<p>Offshore casinos are not required to hold player balances separately from their own money, and no New Zealand "
  "compensation scheme covers them. If a casino closes, or stops serving New Zealand on 1 December 2026 as every casino on this site is expected to, your balance is "
  "only as safe as the operator's willingness to pay it. Withdraw before any deadline, do not leave large balances sitting "
  "in an account, complete verification early so a withdrawal is not held up, and save your full transaction history.</p>"),
 ("How do I complain about an online casino?", "complain",
  "<p>Start with the casino's own complaints process and ask for a written reference. If that fails, go to the regulator "
  "named on its licence: Anjouan, Tobique, Kahnawake and Curaçao all publish complaint routes, and independent mediation "
  "services such as Casino Guru's complaint resolution centre also handle disputes. The DIA cannot resolve disputes with "
  "unlicensed offshore casinos, but you can report unlawful advertising to it at onlinegambling@dia.govt.nz. Once licensing "
  "starts in 2027, complaints about licensed casinos can go to the operator and then the DIA.</p>"),
 ("Can I trust Reddit and review sites?", "trust",
  "<p>Be careful. Many 'Reddit' posts that rank for New Zealand casino searches are promotional posts in unrelated "
  "communities, written to look like personal experience and pointing to casino-list sites. Trustpilot is more useful but "
  "unverified, and several brands here have suspended or removed profiles. Treat any review that recommends a casino and "
  "links to it as advertising. Use facts you can check: the licence number, the owner and the withdrawal terms.</p>"),
]


def caution():
    low = [o for o in CASINOS if o["rating"] < 5.5]
    rows = [[op_cell(o), f'{o["rating"]:.1f}', esc("; ".join(o["flags"][:2]) or "Low independent safety rating")] for o in low]
    return ('<h3 id="caution">Casinos to approach with caution</h3><p>These casinos score below 5.5 on the public record. '
            'That is not an accusation of wrongdoing; it means key facts are missing or independent signals are weak.</p>'
            + table(["Site", "Ledger score", "Main reasons"], rows))


def questions():
    out = ['<h2 id="questions">Real questions New Zealanders ask about online casinos</h2>'
           '<p>These come from the searches New Zealanders actually type, from New Zealand Reddit threads and from Trustpilot '
           'complaints, answered in full.</p>']
    for q, ident, a in QUESTIONS:
        out.append(f'<h3 id="q-{ident}">{q}</h3>{a}')
    out.append(caution())
    return "".join(out)
