"""Guide pages: payments, law, tax, method, responsible gambling."""
from lib import *
from ops_data import WEIGHTS


def guide(P, crumb, author, checker, lead, facts, content, faqs, extra_schema=None, trail=None, kind="Article", priority=0.7):
    t, d, h1 = META[P]
    faq_html, ents = faq(faqs) if faqs else ("", [])
    trail = trail or [(crumb, P)]
    rel = [r for r in RELATED if r[2] != P][:6]
    body = (hero(h1, lead, author, checker, facts, f"Checked {CHECKED}") + crumbs(trail)
            + '<section class="sec"><div class="wrap prose">' + content + faq_html
            + "<h2>Related guides</h2>" + cards(rel, 3) + authorbox(author) + "</div></section>")
    schema = [schema_webpage(P), schema_crumbs(P, trail), schema_article(P, h1, author, checker), schema_person(author)]
    if checker:
        schema.append(schema_person(checker))
    if ents:
        schema.append(schema_faq(P, ents))
    schema += extra_schema or []
    write(P, body, schema, priority=priority, author=author)


# ---------------------------------------------------------------------------
def payments():
    P = "/payment-methods/"
    methods = [
        ("cards", "Visa and Mastercard debit and credit cards", (
            "<p>Cards are accepted almost everywhere and deposits are instant. Two things trip New Zealanders up. First, some "
            "banks decline card payments to offshore gambling merchants, and if you have switched on a gambling block they will "
            "always be declined. Second, if the casino holds your balance in euros or US dollars, your bank applies a foreign "
            "currency fee and its own exchange rate on every transaction, commonly 2% to 3% combined. Not every card can "
            "receive withdrawals; casinos often pay card deposits back by bank transfer instead. Using a credit card to gamble "
            "means paying interest on losses, which is a good reason not to.</p>")),
        ("ewallets", "E-wallets: Skrill, Neteller, MiFinity, Jeton, MuchBetter", (
            "<p>E-wallets sit between your bank and the casino. Deposits are instant and withdrawals are usually the quickest "
            "fiat option once approved. They also keep gambling money in a separate place, which helps with budgeting. "
            "Watch for two catches: some casinos exclude Skrill and Neteller deposits from bonuses, and the e-wallet itself "
            "may charge for currency conversion and for withdrawing to your New Zealand bank.</p>")),
        ("vouchers", "Prepaid vouchers: Neosurf, Paysafecard, Flexepin, CashtoCode", (
            "<p>Vouchers are bought for cash or by card from a retailer or online, then entered as a code at the casino. They "
            "cap what you can spend and keep your bank details away from the casino. They are deposit only, so you will need a "
            "bank transfer, e-wallet or crypto to withdraw.</p>")),
        ("bank", "Bank transfer", (
            "<p>Direct bank transfers work at many casinos but are the slowest route, commonly two to seven business days, and "
            "international transfers can carry fees at both ends. New Zealand banks may ask questions about transfers to "
            "offshore gambling companies, and if you have a gambling block in place they may stop them.</p>")),
        ("crypto", "Cryptocurrency: Bitcoin, Ethereum, USDT, Litecoin and others", (
            "<p>Most casinos on our list accept several coins. Crypto is often the most direct withdrawal route offshore, but "
            "it brings its own costs and risks: exchange fees in New Zealand, network fees, price swings while you hold the "
            'coins, irreversible transfers, and possible tax on crypto gains. See <a href="/best-crypto-casinos/">crypto casinos</a>.</p>')),
        ("poli", "POLi and Apple Pay", (
            "<p>POLi, the bank-to-bank payment service, closed in Australia in 2023 but still operates in New Zealand. It is rare "
            "at offshore casinos and does not appear in Casino Guru's payment lists for any brand here, though one 2026 review "
            "reports it at Spinjo and Lucky Vibe. Apple Pay appears at a few brands on our list, including MadCasino, Smash "
            "and Rivo, usually as a way of paying by card.</p>")),
    ]
    content = (
        toc([(t_, i) for i, t_, _ in methods] + [("Currency conversion costs", "fx"), ("Bank gambling blocks", "blocks"),
                                                 ("Payment options by casino", "by-casino"), ("FAQ", "faq")])
        + "<p>Choosing how to pay is about more than speed. It decides what conversion fees you pay, how easily you can stop, "
          "and how quickly money comes back. Here is every common method from a New Zealand point of view.</p>"
        + "".join(f'<h2 id="{i}">{t_}</h2>{b}' for i, t_, b in methods)
        + '<h2 id="fx">What currency conversion really costs</h2>'
        + "<p>If a casino has no NZD balance, each deposit and each withdrawal is converted. Suppose your bank's combined fee "
          "and exchange spread is 2.5% each way. Depositing NZ$200 a month for a year means NZ$2,400 converted on the way in, "
          "costing about NZ$60, before you have placed a bet, and the same again on anything you withdraw.</p>"
        + table(["Monthly deposits", "Converted in a year", "Cost at 2.5% each way (deposits only)"], [
            ["NZ$50", "NZ$600", "NZ$15"], ["NZ$200", "NZ$2,400", "NZ$60"], ["NZ$500", "NZ$6,000", "NZ$150"]])
        + f"<p>{sum(1 for o in CASINOS if o['nzd'])} of the {len(CASINOS)} casinos we checked list NZD as a balance currency.</p>"
        + '<h2 id="blocks">Bank gambling blocks</h2>'
        + "<p>Most major New Zealand banks let customers block gambling transactions on their cards, often with a switch in "
          "the banking app and a cooling-off period before it can be turned off. If you want a firm limit, this is one of the "
          "most effective tools there is, because it works at every gambling site at once. Check your bank's app, or call "
          'them. More tools: <a href="/responsible-gambling/">responsible gambling</a>.</p>'
        + '<h2 id="by-casino">Payment options by casino</h2>'
        + table(["Site", "Options listed", "NZD balance", "Examples"], [
            [op_cell(o), str(o["n_pay"] or "n/a"), nzd_txt(o), esc(", ".join(o["payments"][:7]))] for o in OPS],
            caption=f"Payment lists from each brand's Casino Guru profile or other named source, read {CHECKED}. Availability varies by country.")
    )
    faqs = [
        ("What is the best payment method for online casinos in NZ?",
         "<p>It depends on what you value. E-wallets balance speed and separation from your main account; vouchers cap your "
         "spending; crypto is often the most direct withdrawal route but carries price and tax risk. Paying into a casino that "
         "holds NZD avoids conversion fees whichever you choose.</p>"),
        ("Why was my card declined at an online casino?",
         "<p>Many New Zealand banks decline payments to offshore gambling merchants, and a gambling block will always decline "
         "them. Your card provider may also flag the payment for fraud checks.</p>"),
        ("Is POLi still available in New Zealand?",
         "<p>Yes, POLi still operates in New Zealand; it closed in Australia in 2023. It is rarely offered by offshore casinos.</p>"),
        ("Can I use PayPal at online casinos in NZ?",
         "<p>None of the payment lists we checked for the brands on this site includes PayPal.</p>"),
        ("Are casino deposits charged fees?",
         "<p>Casinos rarely charge deposit fees themselves, but your bank or e-wallet may charge for currency conversion, and "
         "crypto carries network and exchange fees.</p>"),
    ]
    guide(P, "Payment methods", "tama-rewiti", "hana-mcallister",
          "Cards, e-wallets, vouchers, bank transfer and crypto compared from a New Zealand point of view: what each costs, how "
          "fast it is, what goes wrong, and how a bank gambling block works.",
          [("2–3%", "typical conversion cost each way"), (str(sum(1 for o in CASINOS if o["nzd"])), "casinos with NZD"), ("6", "method types compared"), ("0", "casino links")],
          content, faqs)


# ---------------------------------------------------------------------------
def law():
    P = "/nz-online-casino-law/"
    content = (
        toc([("The short answer", "short"), ("Before 2026: the Gambling Act 2003", "before"), ("The Online Casino Gambling Act 2026", "act"),
             ("The advertising ban", "ads"), ("Licensing timeline", "timeline"), ("The October 2026 auction result", "auction"), ("What licensed casinos must do", "rules"),
             ("What 1 December 2026 means for you", "dec"), ("Sports and racing betting", "betting"), ("Lotto and land-based gambling", "other"),
             ("FAQ", "faq")])
        + '<h2 id="short">The short answer</h2>'
        + "<p>It is not an offence for a New Zealander to play at an online casino based overseas. It is unlawful for an "
          "unlicensed online casino, or anyone acting for it, to advertise to people in New Zealand, and from 1 December 2026 "
          "unlicensed casinos that have not applied for a New Zealand licence must stop serving New Zealand. Eleven companies won "
          "the right to apply in the DIA's October 2026 auction, and the first New Zealand licences are expected in 2027.</p>"
        + '<h2 id="before">Before 2026: the Gambling Act 2003</h2>'
        + "<p>The Gambling Act 2003 banned 'remote interactive gambling' from being run inside New Zealand, with exceptions for "
          "the TAB and the Lotteries Commission (Lotto NZ). It did not stop New Zealanders using casinos based overseas, and it "
          "already prohibited advertising overseas gambling here. In practice that advertising ban was hard to enforce, and "
          "offshore casinos built a large New Zealand customer base.</p>"
        + '<h2 id="act">The Online Casino Gambling Act 2026</h2>'
        + "<p>The Online Casino Gambling Act 2026 received royal assent and came into force on 1 May 2026. It creates a "
          "licensed online casino market regulated by the Department of Internal Affairs. Its main features:</p>"
        + "<ul><li>Up to <b>15 licences</b>, allocated by auction, each for one brand and valid for up to three years.</li>"
          "<li>No company may hold more than three licences.</li>"
          "<li>Licensed operators must take reasonable steps to verify that players are at least <b>18</b>.</li>"
          "<li>Regulations covering harm prevention and minimisation, consumer protection and record-keeping, advertising and "
          "marketing, and fees and levies.</li>"
          "<li>A public register of licensed operators maintained by the DIA.</li></ul>"
        + '<h2 id="ads">The advertising ban</h2>'
        + "<p>Advertising online casino gambling to people in New Zealand has been prohibited for years, but the 2026 Act gave "
          "the DIA new enforcement powers from 1 May 2026: takedown notices and pecuniary penalties of up to <b>NZ$5 million</b> "
          "for unlawful advertising. According to the DIA, these can be issued to anyone who publishes an unlawful "
          "advertisement or arranges to publish one on behalf of an online casino provider, which includes influencers, "
          "content creators and affiliate sites.</p>"
        + "<p>After licensing, licensed operators will be allowed to advertise with restrictions. Cabinet's initial regulatory "
          "decisions, released in late 2025, include prohibiting affiliate marketing and paid endorsements. This is why "
          f"{NAME} carries no links to casinos and no sign-up offers.</p>"
        + note('<p>You can report unlawful online casino advertising to the DIA at onlinegambling@dia.govt.nz.</p>', "info", "Reporting advertising")
        + '<h2 id="timeline">Licensing timeline</h2>'
        + table(["Date", "Step"], [
            ["1 May 2026", "Act in force. Advertising prohibition enforceable. No new online casino providers may enter the New Zealand market"],
            ["July 2026", "Stage 1: expressions of interest"],
            ["29 Sep to 12 Oct 2026", "Stage 2: auction. 32 bidders, 10 rounds, closing price NZ$15 million per licence; 11 companies win the right to apply"],
            ["October 2026", "Stage 3: successful bidders submit full licence applications"],
            ["1 December 2026", "Providers that have not applied must stop offering online casino gambling in New Zealand"],
            ["2027", "Licence decisions and DIA register; regulated market fully operational"],
            ["1 June 2027", "End of the exemption that lets pending applicants keep operating"],
        ], caption="Source: Department of Internal Affairs, Online Gambling for Providers (updated 13 October 2026) and for Players pages.")
        + '<h2 id="auction">The October 2026 auction result</h2>'
        + f"<p>{AUCTION_SUMMARY} Winning at auction is not a licence: each company must pay the auction price and pass a "
          "full suitability assessment before the DIA grants one. The successful companies are:</p>"
        + auction_table()
        + f"<p>{NOT_IN_AUCTION}</p>"
        + '<h2 id="rules">What licensed casinos will have to do</h2>'
        + "<p>Licensed operators will be held to the same standards, set in regulations covering harm minimisation, consumer "
          "protection and advertising. Expect identity and age checks, harm-prevention tools, rules on inducements, and a "
          "complaints route through the operator and then the DIA. Applicants must submit detailed plans for advertising and "
          "marketing, consumer protection, harm prevention and compliance before a licence is granted.</p>"
        + '<h2 id="dec">What 1 December 2026 means for you</h2>'
        + steps([("Find out whether your casino has applied", "Only the 11 companies above could apply. Casinos with a pending application may keep operating without advertising; others must stop serving New Zealand."),
                 ("Withdraw your balance", "If your casino is leaving New Zealand, withdraw before 1 December. Complete any verification now."),
                 ("Keep records", "Save your transaction history and correspondence in case of a dispute."),
                 ("Check the DIA register from 2027", "Once licences are issued, the register will show which casinos are licensed.")])
        + '<h2 id="betting">Sports and racing betting</h2>'
        + "<p>Betting is covered by different law. The Racing Industry Amendment Act 2025, in force from 28 June 2025, made TAB NZ "
          "the only operator allowed to offer online racing and sports betting to people in New Zealand. Offshore bookmakers "
          'may not take bets from New Zealanders. See <a href="/online-betting/">online betting NZ</a>.</p>'
        + '<h2 id="other">Lotto and land-based gambling</h2>'
        + "<p>Lotto NZ remains the lawful operator of national lotteries, including online through MyLotto. Land-based casinos "
          "operate under the Gambling Act 2003, with their own licensing and venue rules, and class 4 gaming machines (pokies "
          "in pubs and clubs) are run by licensed societies that return funds to the community.</p>"
    )
    faqs = [
        ("Is online gambling legal in New Zealand?",
         "<p>Playing at an offshore online casino is not an offence for individuals. Running online casino gambling in New Zealand "
         "without a licence, and advertising unlicensed online casinos here, are unlawful. Online betting is lawful only with TAB "
         "NZ, and lotteries with Lotto NZ.</p>"),
        ("When will licensed online casinos be available in New Zealand?",
         "<p>The auction closed on 12 October 2026 and full applications followed. The DIA expects the licensed market to be "
         "fully operational during 2027, and the exemption for pending applicants ends on 1 June 2027.</p>"),
        ("How many online casino licences will New Zealand issue?",
         "<p>Up to 15, each for a single brand and valid for up to three years. No company may hold more than three.</p>"),
        ("What is the minimum age for online casinos in New Zealand?",
         "<p>Licensed online casinos must take reasonable steps to verify that players are at least 18.</p>"),
        ("Can I be fined for playing at an offshore casino?",
         "<p>The penalties in the 2026 Act are aimed at operators and advertisers, not at individual players.</p>"),
        ("What happens to offshore casinos after 1 December 2026?",
         "<p>Those that have not applied for a licence must stop offering online casino gambling in New Zealand. Applicants may "
         "continue without advertising until their application is decided. Only the 11 companies that won at auction could apply.</p>"),
        ("Who won New Zealand's online casino licence auction?",
         "<p>Eleven companies won the right to apply: Baytree Interactive (3 rights), Playvia Gaming (NZ) (2), Rock Swift Group "
         "(2), Christchurch Online NZ, One Casino, Rush Entertainment, Skill On Net, SkyCity NZ Online NO1 and NO2, Stake New "
         "Zealand and TAB New Zealand. The price reached NZ$15 million per licence.</p>"),
        ("Will affiliate casino sites be allowed?",
         "<p>Cabinet's initial regulatory decisions include prohibiting affiliate marketing and paid endorsements, even for licensed operators.</p>"),
    ]
    guide(P, "NZ online casino law", "wiremu-salter", "hana-mcallister",
          "The Online Casino Gambling Act 2026 in plain English: what is legal now, the advertising ban and its NZ$5 million "
          "penalties, who won the DIA licence auction, the 1 December 2026 cut-off and what it means for your account.",
          [("1 May 2026", "Act in force"), ("15", "maximum licences"), ("NZ$5m", "maximum advertising penalty"), ("1 Dec 2026", "unlicensed casinos must exit")],
          content, faqs, priority=0.8)


# ---------------------------------------------------------------------------
def tax():
    P = "/gambling-winnings-tax-nz/"
    content = (
        toc([("The general rule", "rule"), ("Professional gamblers", "pro"), ("Crypto", "crypto"), ("Interest and investment returns", "interest"),
             ("Worked examples", "examples"), ("Duty paid by operators", "duty"), ("FAQ", "faq")])
        + note("<p>This is general information, not tax advice. If gambling is a significant part of your income, talk to a "
               "tax adviser or Inland Revenue.</p>", "info", "General information only")
        + '<h2 id="rule">The general rule: casual winnings are not income</h2>'
        + "<p>Inland Revenue does not generally treat gambling winnings as taxable income for people who gamble for fun. That "
          "covers casino wins, pokie jackpots, betting wins and Lotto prizes. There is no gambling winnings tax to pay, and "
          "losses cannot be claimed against other income.</p>"
        + '<h2 id="pro">When winnings can be taxable: professional gambling</h2>'
        + "<p>The position changes if gambling is a business. Inland Revenue looks at the whole picture: how regularly you "
          "gamble, how organised and systematic it is, the scale, and whether you depend on it for a living. Professional "
          "poker players and some professional punters fall into this category. If you are in business, winnings are income "
          "and expenses, including losses, may be deductible.</p>"
        + '<h2 id="crypto">Crypto: the trap most guides miss</h2>'
        + "<p>Inland Revenue treats crypto-assets as property. If you buy crypto mainly to sell or exchange it, gains on "
          "disposal are generally taxable. Using crypto at a casino does not change that: if your Bitcoin rose in value "
          "between buying it and spending or selling it, the gain can be taxable even though gambling winnings are not. Keep "
          "dated records of every purchase, transfer and sale.</p>"
        + '<h2 id="interest">Interest and investment returns on winnings</h2>'
        + "<p>Once winnings are in your bank account, any interest they earn, or returns from investing them, are taxed in the "
          "normal way.</p>"
        + '<h2 id="examples">Worked examples</h2>'
        + table(["Situation", "Usually taxable?", "Why"], [
            ["You win NZ$8,000 on a pokie playing for fun", "No", "Casual gambling winnings are not income"],
            ["You win NZ$1 million on Lotto", "No", "Lottery prizes are not income; interest earned on them is"],
            ["You bet on rugby every weekend for fun and finish the year up", "No", "Recreational betting"],
            ["You play poker full-time and it is your main income", "Likely yes", "Gambling as a business"],
            ["You buy Bitcoin, it rises, you deposit it at a casino", "The crypto gain may be", "Crypto disposal rules, separate from gambling"],
        ])
        + '<h2 id="duty">Duty paid by operators</h2>'
        + "<p>Some taxes on gambling are paid by operators, not players. Offshore gambling operators have been liable for "
          "offshore gambling duty and GST on services to New Zealanders since 2023, and licensed operators will pay duties and "
          "levies under the new regime. None of these is deducted from your winnings by law.</p>"
    )
    faqs = [
        ("Do you pay tax on casino winnings in NZ?",
         "<p>Not if you gamble for fun. Inland Revenue does not generally treat casual gambling winnings as income.</p>"),
        ("Is Lotto taxed in New Zealand?",
         "<p>No. Lotto prizes are not taxable income, but interest or investment returns earned on the prize are.</p>"),
        ("Do I need to declare gambling winnings to Inland Revenue?",
         "<p>Casual winnings do not need to be declared as income. Professional gamblers must declare gambling income.</p>"),
        ("Can I claim gambling losses on tax?",
         "<p>Only if gambling is a business. Recreational losses cannot be deducted.</p>"),
        ("Is crypto gambling taxed differently?",
         "<p>The winnings are treated the same, but gains on the crypto itself may be taxable under Inland Revenue's crypto-asset rules.</p>"),
    ]
    guide(P, "Gambling winnings tax", "wiremu-salter", "tama-rewiti",
          "Casual gambling wins are not income in New Zealand, whether from a pokie, a bet or Lotto. The exceptions are "
          "professional gambling and gains on crypto. Here is Inland Revenue's position with worked examples.",
          [("0%", "tax on casual winnings"), ("Pro", "gamblers can be taxed"), ("Crypto", "gains may be taxable"), ("Lotto", "prizes not taxed")],
          content, faqs)


# ---------------------------------------------------------------------------
def method():
    P = "/how-we-review/"
    lic_rows = [["Kahnawake Gaming Commission", "7.0"], ["Two or more licences (e.g. Anjouan + Tobique)", "6.5"],
                ["Three licences including Estonia", "7.0"], ["Curaçao Gaming Authority (post-2023 regime)", "6.0"],
                ["Single Anjouan licence", "5.0"], ["Licence not confirmed or not verified", "2.0"]]
    content = (
        toc([("What we do and do not do", "rules"), ("The Ledger score", "score"), ("Input 1: independent safety", "safety"),
             ("Input 2: licence", "licence"), ("Input 3: ownership", "owner"), ("Input 4: terms and limits", "terms"),
             ("Input 5: banking for Kiwis", "banking"), ("Our sources", "sources"), ("Updates and corrections", "updates")])
        + '<h2 id="rules">What we do, and what we do not do</h2>'
        + table(["We do", "We do not"], [
            ["Source every fact and show the date we checked it", "Link to casinos or bookmakers"],
            ["Say 'reported' or 'not confirmed' when a fact has only one source", "Publish sign-up offers, bonus codes or referral links"],
            ["Show independent ratings and attribute them", "Claim test deposits, timed withdrawals or game counts we did not do"],
            ["Explain the New Zealand law on every relevant page", "Let operators buy a review, a score or a change to one"],
        ])
        + '<h2 id="score">The Ledger score</h2>'
        + "<p>Every site gets a score out of 10, built from five inputs. Each input is scored from public information, so "
          "anyone can repeat the calculation from the facts in a review.</p>"
        + table(["Input", "Weight"], [[k.title() if k != "banking" else "Banking for Kiwis", f"{int(w*100)}%"] for k, w in WEIGHTS.items()])
        + "<p>Score = 0.40 × safety + 0.20 × licence + 0.15 × ownership + 0.15 × terms + 0.10 × banking, rounded to one decimal.</p>"
        + '<h2 id="safety">Input 1: independent safety (40%)</h2>'
        + "<p>We use the Casino Guru Safety Index, a 0 to 10 rating built from a casino's terms and conditions, estimated "
          "size, links to related casinos and its complaint record. It is the most widely published independent measure that "
          "covers almost every brand here. Where a brand has no profile, it gets a neutral 4.0, so missing information never "
          "raises a score.</p>"
        + '<h2 id="licence">Input 2: licence (20%)</h2>'
        + table(["Licence situation", "Points"], lic_rows)
        + '<h2 id="owner">Input 3: ownership (15%)</h2>'
        + table(["Ownership", "Points"], [["Named owner confirmed by an independent database or the operator's own site", "8.0"],
                                          ["Owner named by review sites only (reported)", "6.0"], ["Owner not published or not confirmed", "3.0"]])
        + '<h2 id="terms">Input 4: terms and limits (15%)</h2>'
        + "<p>Starts at 8.0. We deduct 2.0 for a daily win cap, 3.0 where players report payouts below the stated limits, 1.5 "
          "for a weekly withdrawal limit of €2,500 or less, and 1.0 where no withdrawal limits are published. Minimum 1.0.</p>"
        + '<h2 id="banking">Input 5: banking for Kiwis (10%)</h2>'
        + "<p>Starts at 5.0. We add 2.5 for an NZD balance, 1.5 for 25 or more payment options (1.0 for 19 to 24), and 1.0 "
          "for crypto support. Maximum 10.</p>"
        + '<h2 id="sources">Our sources</h2>'
        + "<ul><li>Operators' own terms, About pages and site footers.</li>"
          "<li>Regulators' public licence registers (Anjouan, Tobique, Kahnawake, Curaçao).</li>"
          "<li>Casino Guru casino profiles, for the Safety Index, licence verification, owners, limits, payment lists and complaints.</li>"
          "<li>Other review sites, only where they add a fact, and marked 'reported'.</li>"
          "<li>Department of Internal Affairs, New Zealand legislation and Inland Revenue for law and tax.</li></ul>"
        + '<h2 id="updates">Updates and corrections</h2>'
        + f"<p>Every fact is rechecked at least monthly. The current check was completed on {CHECKED}; the next is due by "
          f"{NEXT_CHECK}. When a fact changes, the review is updated and the score recalculated. If you spot an error, "
          '<a href="/contact/#corrections">tell us</a>; we correct confirmed errors within two working days and note the change.</p>'
        + "<p>The order of operator lists on this site is set by our editor and is not a ranking. Where you want our assessment, "
          'use the Ledger score, or the <a href="/casino-reviews/#by-score">table sorted by score</a>.</p>'
    )
    guide(P, "How we review", "hana-mcallister", "wiremu-salter",
          "Every number on this site can be traced back to a public source. Here is exactly how the Ledger score is "
          "calculated, the sources we use, how often we recheck, and the rules we never break.",
          [("5", "weighted inputs"), ("40%", "independent safety"), ("Monthly", "recheck cycle"), ("0", "paid scores")],
          content, None, priority=0.6)


# ---------------------------------------------------------------------------
def responsible():
    P = "/responsible-gambling/"
    content = (
        toc([("Free help, 24/7", "help"), ("Warning signs", "signs"), ("Tools that work", "tools"), ("Bank gambling blocks", "blocks"),
             ("Self-exclusion", "exclusion"), ("Blocking software", "software"), ("Helping someone else", "whanau"), ("Our commitments", "ours")])
        + '<h2 id="help">Free, confidential help, 24/7</h2>'
        + table(["Service", "Contact", "What they offer"], [
            ["Gambling Helpline", '<a href="tel:0800654655">0800 654 655</a> · text 8006', "Free, confidential support any time, and referral to counselling"],
            ["Problem Gambling Foundation", '<a href="tel:0800664262">0800 664 262</a>', "Free counselling and support, including Māori and Pacific services"],
            ["Asian Family Services", '<a href="tel:0800862342">0800 862 342</a>', "Gambling support in several Asian languages"],
            ["Need to talk?", "Call or text 1737", "Free counselling for anything that is weighing on you"],
            ["Lifeline", '<a href="tel:0800543354">0800 543 354</a>', "24/7 crisis support"],
        ])
        + note("<p>If you or someone you know is in immediate danger, call 111.</p>", "warn", "In an emergency")
        + '<h2 id="signs">Warning signs</h2>'
        + "<ul><li>Spending more time or money than you meant to, more often.</li>"
          "<li>Chasing losses, or gambling to win back money you need.</li>"
          "<li>Borrowing, using credit, or selling things to gamble.</li>"
          "<li>Hiding gambling from your partner or whānau, or lying about it.</li>"
          "<li>Feeling restless, anxious or low when you are not gambling.</li>"
          "<li>Gambling to escape stress, loneliness or problems.</li></ul>"
        + "<p>Two or more of these is a reason to pause and talk to someone. The Gambling Helpline is a good first call.</p>"
        + '<h2 id="tools">Tools that work</h2>'
        + table(["Tool", "How it helps", "Where to find it"], [
            ["Deposit limit", "Caps what you can deposit per day, week or month", "Account settings at most casinos and betting sites"],
            ["Loss and session limits", "Stops play after a set loss or time", "Account settings, where offered"],
            ["Reality checks", "Pop-ups showing how long you have played", "Account settings"],
            ["Time-out", "Locks your account for a short period", "Account settings or support"],
            ["Self-exclusion", "Closes your account for months or years", "Support or account settings"],
            ["Bank gambling block", "Blocks gambling payments on your cards", "Your bank's app or phone line"],
        ])
        + '<h2 id="blocks">Bank gambling blocks</h2>'
        + "<p>Most major New Zealand banks offer a way to block gambling transactions on your cards, usually with a delay "
          "before the block can be lifted. It is one of the strongest tools available because it applies to every gambling "
          "site at once, offshore or local. Look in your banking app's card settings, or ask your bank.</p>"
        + '<h2 id="exclusion">Self-exclusion</h2>'
        + "<p>Each casino or betting site handles its own self-exclusion, so excluding from one does not exclude you from "
          "others, including sister sites from the same group. If you exclude, do it with every site you use, and combine it "
          "with a bank block. For land-based venues in New Zealand, venue exclusion orders are available, and the Gambling "
          "Helpline can help you arrange multi-venue exclusion.</p>"
        + '<h2 id="software">Blocking software</h2>'
        + "<p>Gambling-blocking apps and browser tools can stop gambling sites loading on your devices. Some are free. Set them "
          "up on every device you use and, if possible, ask someone you trust to hold the password.</p>"
        + '<h2 id="whanau">If someone you care about is gambling too much</h2>'
        + "<p>Talk when you are both calm, focus on how it is affecting you rather than on blame, and do not lend money to cover "
          "losses. Support services help family and whānau as well as gamblers: you can call the Gambling Helpline or the "
          "Problem Gambling Foundation for yourself.</p>"
        + '<h2 id="ours">Our commitments</h2>'
        + "<ul><li>This site is for adults 18 and over.</li><li>We publish no links to casinos and no sign-up offers.</li>"
          "<li>We do not present gambling as a way to make money.</li>"
          "<li>Every page carries the Gambling Helpline number.</li></ul>"
    )
    faqs = [
        ("How do I know if I have a gambling problem?",
         "<p>If gambling is costing more money or time than you can afford, if you chase losses, borrow to gamble or hide it, it is "
         "worth talking to someone. The Gambling Helpline on 0800 654 655 is free and confidential.</p>"),
        ("Can I block gambling on my bank card in New Zealand?",
         "<p>Yes, most major New Zealand banks let you block gambling transactions on your cards, usually in the banking app.</p>"),
        ("How do I self-exclude from online casinos?",
         "<p>Contact each casino's support or use the self-exclusion option in your account. Exclusion at one site does not cover "
         "others, so repeat it everywhere you have an account and add a bank block.</p>"),
        ("Is help free in New Zealand?",
         "<p>Yes. The Gambling Helpline, the Problem Gambling Foundation and Asian Family Services provide free, confidential support.</p>"),
    ]
    guide(P, "Responsible gambling", "wiremu-salter", "hana-mcallister",
          "Free, confidential help is available 24/7. Here are the warning signs, the tools that actually work, including bank "
          "gambling blocks and self-exclusion, and how to support someone in your whānau.",
          [("0800 654 655", "Gambling Helpline"), ("8006", "free text"), ("24/7", "always open"), ("18+", "this site is R18")],
          content, faqs, priority=0.6)


def build():
    payments(); law(); tax(); method(); responsible()
