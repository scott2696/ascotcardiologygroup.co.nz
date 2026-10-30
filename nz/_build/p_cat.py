"""Casino category pages. All share the homepage layout through lib.landing()."""
from lib import *


# ---------------------------------------------------------------------------
def pokies():
    P = "/online-pokies/"
    content = (
        toc([("How pokies work", "how"), ("RTP and variable RTP", "rtp"), ("Volatility", "vol"), ("Types of pokie", "types"),
             ("Jackpots", "jackpots"), ("Choosing where to play", "where"), ("Free demo play", "demo"), ("FAQ", "faq")])
        + '<h2 id="how">How online pokies work</h2>'
        + "<p>Every online pokie is run by a random number generator (RNG): a program that picks a result for each spin the "
          "moment you press the button. The reels you see are an animation of a result that has already been decided. Spins "
          "are independent, so a machine is never 'due' a win and a run of losses does not make the next spin any more likely "
          "to pay. Games from the major studios are tested by independent labs that check the RNG and the published maths.</p>"
        + "<p>What you can control is which game you play, at what stake, for how long, and at which RTP setting. Those choices "
          "change your expected cost far more than any strategy on the reels.</p>"
        + '<h2 id="rtp">RTP, and why the same pokie can pay differently</h2>'
        + "<p>Return to player (RTP) is the share of all money staked on a game that it pays back over a very large number of "
          "spins. A 96% RTP pokie returns NZ$96 for every NZ$100 staked on average, so the expected cost is about 4 cents per "
          "dollar wagered. Over one session, results swing wildly; RTP only describes the long run.</p>"
        + "<p>The detail most guides leave out: many popular pokies are sold to casinos at several RTP settings, for example "
          "96.5%, 94% and 91%. The game looks identical. The casino chooses the version. On NZ$2,000 of spins, the difference "
          "between 96% and 91% is about NZ$100 in expected losses.</p>"
        + table(["RTP setting", "Expected cost per NZ$100 wagered", "On NZ$2,000 of spins"], [
            ["97%", "NZ$3", "NZ$60"], ["96%", "NZ$4", "NZ$80"], ["94%", "NZ$6", "NZ$120"], ["91%", "NZ$9", "NZ$180"]],
            caption="Averages over the long run. Any single session can be far better or worse.")
        + note("<p>Open the game's information or paytable screen (often an 'i' or menu icon) and look for 'RTP' or 'theoretical "
               "return'. If the figure shown is lower than the one on the studio's own website, the casino is running a lower "
               "setting.</p>", "tip", "How to check the RTP a casino is running")
        + '<h2 id="vol">Volatility: how a pokie spends your money</h2>'
        + "<p>Volatility (or variance) describes how results are spread. Low-volatility pokies pay small amounts often, so a "
          "budget lasts longer. High-volatility pokies pay rarely but can pay big, so long losing runs are normal. Two games "
          "with the same 96% RTP can feel completely different: one drip-feeds wins, the other can take your whole session "
          "budget before a bonus round lands. Choose volatility to match your budget, not your hopes.</p>"
        + '<h2 id="types">The main types of online pokie</h2>'
        + table(["Type", "How it works", "Good to know"], [
            ["Classic and video pokies", "Fixed paylines, usually 3 to 5 reels", "Simplest to understand; often lower volatility"],
            ["Megaways", "Reel heights change each spin, giving up to 117,649 ways to win", "Usually high volatility"],
            ["Hold and win", "Collect cash symbols that lock in place during respins", "Popular with Asian-themed and 'Lightning'-style games"],
            ["Cluster pays", "Wins form from groups of matching symbols rather than lines", "Cascading wins are common"],
            ["Bonus buy", "Pay a multiple of your stake to go straight to the feature", "Raises the cost and the volatility of each session"],
            ["Progressive jackpots", "Part of every stake feeds a growing prize", "Base game RTP is often lower to fund the jackpot"],
        ])
        + '<h2 id="jackpots">Progressive jackpots</h2>'
        + "<p>A progressive jackpot grows with every bet placed on the game across all the casinos linked to it, until one "
          "player wins it. The headline can run into millions, but the chance of hitting it on any spin is tiny and the base "
          "game usually has a lower RTP to pay for the pot. If you play jackpot pokies, check the casino's withdrawal limits "
          "first: several sites on this list cap withdrawals at a few thousand dollars a week, and some exempt progressive "
          "jackpots from those limits while others do not.</p>"
        + '<h2 id="where">Choosing where to play pokies</h2>'
        + "<p>The pokies themselves come from the same studios at almost every casino here. What differs between casinos is "
          "the RTP version they run, the currency you play in, the withdrawal limits and how disputes are handled. That is why "
          "the list above shows licence, NZD support, limits and independent safety rather than game counts.</p>"
        + '<h2 id="demo">Free demo play</h2>'
        + "<p>Most studios offer a free demo mode, either on the casino site or on the studio's own website. Demo play is the "
          "best way to learn a game's volatility and features without spending anything. Remember that some demo versions run "
          "at the highest RTP setting, which may be higher than the real-money version a casino offers.</p>"
    )
    faqs = [
        ("Which online pokies pay out the most in NZ?",
         "<p>Look for games with an RTP of 96% or more, and check the setting in the game's information panel, because the same "
         "title can run at a lower RTP at some casinos. No pokie 'pays more' in the short term; RTP is a long-run average.</p>"),
        ("Can you win real money on online pokies?",
         "<p>Yes, but on average every pokie returns less than you stake. Wins are random, and over time the house edge means "
         "most players lose more than they win. Play with money you are happy to spend on entertainment.</p>"),
        ("Are online pokies rigged?",
         "<p>Games from the major studios are tested by independent labs and use certified random number generators. The real "
         "risk is less the game than the casino: which RTP version it runs and whether it pays out. That is what our reviews check.</p>"),
        ("What is the difference between RTP and volatility?",
         "<p>RTP tells you how much a pokie pays back on average over the long run. Volatility tells you how unevenly it pays: "
         "often and small, or rarely and big.</p>"),
        ("Do I pay tax on pokie winnings in New Zealand?",
         '<p>Not if you play for fun. Casual gambling winnings are not treated as income by Inland Revenue. See <a href="/gambling-winnings-tax-nz/">gambling winnings tax</a>.</p>'),
        ("Are free pokies the same as real-money pokies?",
         "<p>The game and features are the same, but the demo may run at a different RTP setting from the real-money version a "
         "casino offers, and demo wins cannot be withdrawn.</p>"),
    ]
    landing(P, "Online pokies NZ", "olivia-brandt", "hana-mcallister",
            "How online pokies really pay: return to player, the variable RTP settings casinos can choose, volatility, Megaways, "
            "hold-and-win and jackpots. Plus the casinos New Zealanders ask about, checked on licence, NZD banking and limits.",
            [("96%", "typical RTP to look for"), ("4c", "expected cost per $1 at 96%"), (str(len(CASINOS)), "casinos checked"), ("0", "casino links")],
            CASINOS, "Casinos for online pokies, checked for New Zealand players",
            "The pokies come from the same studios almost everywhere. What differs is the casino: its licence, its currency and "
            "how much it lets you withdraw.", content, faqs)


# ---------------------------------------------------------------------------
def new_casinos():
    P = "/new-online-casinos/"
    ops = pick(["crownslots", "spinjo", "lucky-vibe", "fortune-play", "lucky-circus", "smash", "trixino", "rivo", "spino"])
    lic_rows = sorted([o for o in ops if o["licence_year"] or o["launched"]], key=lambda o: o["name"])
    content = (
        toc([("What counts as new", "new"), ("Dating a casino by its licence", "dating"), ("Checks for any new casino", "checks"),
             ("New casinos and the 1 December cut-off", "cutoff"), ("New casino bonuses", "bonus"), ("FAQ", "faq")])
        + '<h2 id="new">What counts as a new online casino</h2>'
        + "<p>New casino brands launch every month, but most are not new businesses. They are new websites from existing "
          "operating groups, built on the same platform with a different name, theme and bonus. Several brands on this page "
          "share owners and licence numbers: Spinjo and Lucky Vibe both sit under Hollycorn N.V., and Fortune Play and Lucky "
          "Circus under Novatrix S.R.L. That is not a bad thing, since an established group usually means working payments and "
          "support, but it does mean a 'new' brand inherits its sister sites' complaint history.</p>"
        + '<h2 id="dating">How to date a casino by its licence number</h2>'
        + "<p>Anjouan licence numbers follow the pattern ALSI-YYYYMM…, so the number itself shows roughly when the licence was "
          "issued. Rivo's ALSI-202606020-FI1 dates from June 2026; Spino's ALSI-202506006-FI1 from June 2025. A licence date is "
          "not a launch date, because brands move between regulators, but it is a checkable fact, unlike the 'launched' dates "
          "many review sites print.</p>"
        + table(["Brand", "Launched (reported)", "Licence issued", "Licence"], [
            [op_cell(o), esc(o["launched"] or "Not confirmed"), str(o["licence_year"] or "Not confirmed"), esc(o["licence_short"])]
            for o in lic_rows], caption="Licence year read from the licence number where the format allows.")
        + '<h2 id="checks">Six checks before joining any new casino</h2>'
        + steps([
            ("Licence number on a real register", "A new brand should show a licence number in its footer that you can find on the regulator's site."),
            ("A named operating company", "The terms should say which company runs the site and where it is registered."),
            ("Sister sites", "Search the company name. If its other brands have a poor complaint record, expect the same."),
            ("Withdrawal limits and win caps", "New brands often launch with low limits. Find them in the terms before you deposit."),
            ("Real terms, not just a banner", "Read the full bonus terms: wagering, maximum bet, game weighting and any cap on bonus winnings."),
            ("Small first withdrawal", "Withdraw a small amount early to test verification and payout before you deposit more."),
        ])
        + '<h2 id="cutoff">New casinos and the 1 December 2026 cut-off</h2>'
        + "<p>The Online Casino Gambling Act 2026 closed the door to new entrants. Since it came into force on 1 May 2026, no "
          "new online casino provider may enter the New Zealand market, and only providers already serving New Zealand before "
          "then may continue, until 1 December 2026, unless they apply for a licence. A brand that launched for New Zealand "
          "after 1 May 2026 is, on the DIA's guidance, not permitted to be operating here at all. From early 2027 the only "
          f"genuinely new casinos for New Zealanders will be the licensed ones on the DIA's register. {NOT_IN_AUCTION}</p>"
        + '<h2 id="bonus">New casino bonuses</h2>'
        + "<p>New brands compete on bonus size. Trixino's six-stage 777% package at 7x wagering is an example of a genuinely "
          "unusual offer; CrownSlots' 390% at a reported 40x is more typical. The bigger and newer the offer, the more it pays "
          'to read the terms. Our <a href="/online-casinos/bonuses/">bonus guide</a> shows how to work out what an offer will '
          "really cost you.</p>"
    )
    faqs = [
        ("What is the newest online casino in NZ?",
         "<p>Going by licence numbers, Rivo's Anjouan licence (June 2026) is the most recent on our list. Note that under the 2026 "
         "Act, no new online casino provider may lawfully enter the New Zealand market until licensing is complete.</p>"),
        ("Are new online casinos safe?",
         "<p>A new brand has no track record of its own. Check its licence, its owner and the record of its sister sites. A brand "
         "from a group with a long, clean history is a lower risk than an anonymous one.</p>"),
        ("Why do new casinos offer such big bonuses?",
         "<p>To attract players quickly. Large bonuses usually come with high wagering, low maximum bets and capped bonus "
         "winnings, so the headline is rarely what it seems.</p>"),
        ("Will there be new licensed online casinos in New Zealand?",
         "<p>Yes. Eleven companies won the right to apply for the 15 licences at the DIA's October 2026 auction, including SkyCity, "
         "TAB New Zealand and Stake New Zealand. Licences are expected in 2027, and licensed brands will be listed on a DIA register.</p>"),
        ("Can a casino that launched in 2026 serve New Zealand players?",
         "<p>On the DIA's guidance, no new online casino provider may enter the New Zealand market until the licensing regime is "
         "in place. Only providers already operating here before 1 May 2026 may continue, and only until 1 December 2026 unless "
         "they have applied for a licence.</p>"),
    ]
    landing(P, "New online casinos", "hana-mcallister", "wiremu-salter",
            "Ten newer casino brands that New Zealanders ask about, dated by their licence numbers rather than marketing claims. "
            "Plus the six checks for any new casino and why the 2026 Act stopped new brands entering New Zealand.",
            [(str(len(ops)), "newer brands checked"), ("June 2026", "newest licence on our list"), ("1 May 2026", "no new entrants from"), ("0", "casino links")],
            ops, "Newer casino brands, checked", "Brands reported as launched since 2024 or licensed since 2025, in our editor's order.",
            content, faqs, cols=["licence", "lyear", "owner", "nzd", "safety", "score"])


# ---------------------------------------------------------------------------
def high_payout():
    P = "/high-payout-casinos/"
    big = sorted(CASINOS, key=lambda o: -o["rating"])
    content = (
        toc([("What 'best paying' means", "meaning"), ("House edge by game", "edge"), ("RTP settings", "rtp"),
             ("Limits: the other half of paying out", "limits"), ("How to get the best return", "tips"), ("FAQ", "faq")])
        + '<h2 id="meaning">What "best paying casino" actually means</h2>'
        + "<p>Casinos do not set one payout rate for the whole site. Every game has its own return to player, so a site's "
          "'payout percentage' is just an average of whatever its customers happened to play. Two things genuinely make one "
          "casino pay better than another: the <b>RTP versions</b> it chooses to run, and the <b>limits</b> it puts on how much "
          "you can withdraw. A casino running high-RTP versions but capping withdrawals at NZ$1,000 a day is not a high payout "
          "casino for anyone who wins big.</p>"
        + '<h2 id="edge">The house edge on every main game</h2>'
        + table(["Game", "RTP", "House edge", "What changes it"], [
            ["Blackjack, basic strategy", "about 99.5%", "about 0.5%", "Rules (dealer stands on soft 17, 3:2 payouts) and your decisions"],
            ["Baccarat, banker bet", "98.94%", "1.06%", "5% commission on banker wins"],
            ["Baccarat, player bet", "98.76%", "1.24%", "Nothing"],
            ["European roulette", "97.30%", "2.70%", "Single zero; French 'La Partage' rules halve it on even-money bets"],
            ["American roulette", "94.74%", "5.26%", "Double zero; avoid"],
            ["Video poker (full pay)", "99%+", "under 1%", "Paytable and perfect strategy"],
            ["Pokies", "88% to 97%", "3% to 12%", "The RTP version the casino runs"],
            ["Baccarat, tie bet", "about 85.6%", "about 14.4%", "Avoid"],
        ], caption="Standard published game maths. Live dealer versions use the same rules as their RNG equivalents.")
        + "<p>Expected cost is house edge times the amount you wager. NZ$1,000 wagered on European roulette costs about NZ$27 "
          "on average; the same NZ$1,000 on a 94% pokie costs about NZ$60, and on basic-strategy blackjack about NZ$5.</p>"
        + '<h2 id="rtp">Why RTP settings matter more than the casino</h2>'
        + "<p>Studios commonly offer the same pokie at several RTP levels. The casino picks one. You can check which is running "
          "by opening the game's paytable or information screen and comparing the RTP with the figure on the studio's website. "
          "If a casino consistently runs the lower settings, its pokies are a worse deal everywhere in the lobby, however "
          "generous its bonus looks.</p>"
        + '<h2 id="limits">Limits: the other half of paying out</h2>'
        + "<p>The highest published limits on our list belong to the NZD-balance sites in the Hollycorn and Novatrix "
          "groups: NZ$3,000 a day, NZ$7,500 a week and NZ$30,000 a month. At the low end, Smash and Rivo publish €1,000 "
          "a day, Smash €2,000 a week and Lucky Circus €2,500 a week. Lucky Circus, Bet&Play, Rivo and Smash also have daily "
          "win caps.</p>"
        + '<h2 id="tips">How to get the best return</h2>'
        + "<ul><li>Choose games with a low house edge: blackjack with basic strategy, baccarat banker, European roulette.</li>"
          "<li>On pokies, check the RTP setting and prefer 96% or more.</li>"
          "<li>Skip side bets and tie bets, which carry far higher edges.</li>"
          "<li>Avoid bonuses whose wagering would force you to bet many times your deposit.</li>"
          "<li>Pick a casino whose withdrawal limits match the size of win you could realistically land.</li></ul>"
    )
    faqs = [
        ("Which online casino has the highest payout in NZ?",
         "<p>No casino has a single payout rate. What you can compare is the RTP of the games and the withdrawal limits. The "
         "best-documented NZD sites publish the highest limits on our list, at NZ$3,000 a day and NZ$7,500 a week.</p>"),
        ("What casino game has the best odds?",
         "<p>Blackjack played with basic strategy, at about 0.5% house edge, followed by baccarat on the banker bet (1.06%) and "
         "European roulette (2.7%).</p>"),
        ("Is a 98% RTP pokie better than a 96% one?",
         "<p>Over the long run, yes: it costs about 2 cents per dollar wagered instead of 4. In a single session, volatility "
         "matters far more than that difference.</p>"),
        ("Why do some casinos have different RTP for the same game?",
         "<p>Studios sell many games at several RTP settings and the casino chooses which one to run. The game looks the same; "
         "only the paytable information shows the difference.</p>"),
        ("Do withdrawal limits affect payouts?",
         "<p>Yes. A big win is paid in instalments up to the limit, so a low weekly limit can turn a large win into months of "
         "payments. A daily win cap means winnings above it are not paid at all.</p>"),
    ]
    landing(P, "High payout casinos", "olivia-brandt", "tama-rewiti",
            "What 'best paying' really means: the house edge on every main game, the RTP settings casinos choose, and the "
            "withdrawal limits that decide whether a big win reaches you. Casinos listed highest Ledger score first.",
            [("0.5%", "house edge, basic blackjack"), ("2.7%", "European roulette"), ("€4,000", "highest daily limit here"), ("0", "casino links")],
            big, "Casinos ranked by Ledger score", "This page is the exception to our editor's order: here the casinos are sorted "
            "by Ledger score, highest first, because the score already reflects limits and payout reliability.",
            content, faqs, cols=["limit", "cap", "nzd", "safety", "score"])


# ---------------------------------------------------------------------------
def fast_payout():
    P = "/fast-payout-casinos/"
    ops = [o for o in CASINOS if o["limits"]]
    content = (
        toc([("What makes a payout fast", "fast"), ("Typical times by method", "methods"), ("Why withdrawals stall", "stall"),
             ("Verification (KYC)", "kyc"), ("Speeding up your first withdrawal", "speed"), ("FAQ", "faq")])
        + note("<p>Many sites publish precise payout times for each casino. We have not timed withdrawals ourselves, so we "
               "do not. The ranges below are typical for each payment method industry-wide. What we do publish are each "
               "casino's own withdrawal limits.</p>", "tip", "Why there are no 'payout in 1 hour' claims here")
        + '<h2 id="fast">What makes a casino payout fast</h2>'
        + "<p>A withdrawal passes through three stages: the casino's own processing (often called the pending period), any "
          "verification checks, and the payment method's transfer time. Casinos control the first two. The third depends on the "
          "method you choose. A 'fast payout casino' is one that processes quickly, verifies you early and offers a fast "
          "method; a high withdrawal limit means big wins do not get split into many slow instalments.</p>"
        + '<h2 id="methods">Typical withdrawal times by method</h2>'
        + table(["Method", "Typical time after approval", "Notes for NZ players"], [
            ["Crypto (BTC, LTC, USDT)", "Minutes to a few hours", "Network congestion and fees vary; you then sell on a NZ exchange"],
            ["E-wallets (Skrill, Neteller, MiFinity, Jeton)", "Same day to 24 hours", "Then a further transfer to your NZ bank"],
            ["Visa and Mastercard", "1 to 5 business days", "Not all cards accept withdrawals; some NZ banks block offshore gambling"],
            ["Bank transfer", "2 to 7 business days", "Slowest; international transfer fees may apply"],
            ["Vouchers (Neosurf, Paysafecard)", "Not available", "Deposit only"],
        ], caption="Typical industry ranges, not measured at any specific casino.")
        + '<h2 id="stall">Why casino withdrawals stall</h2>'
        + "<ul><li><b>Unfinished verification.</b> The most common cause. Many casinos only ask for ID at your first withdrawal.</li>"
          "<li><b>Bonus still active.</b> Withdrawing before wagering is complete usually forfeits the bonus and its winnings.</li>"
          "<li><b>Method mismatch.</b> Casinos usually pay back to the method you deposited with, or ask you to prove ownership of a new one.</li>"
          "<li><b>Limits.</b> A win above the daily or weekly limit is paid in instalments.</li>"
          "<li><b>Weekends and public holidays.</b> Manual approval teams may work reduced hours.</li>"
          "<li><b>Reversing a withdrawal.</b> Some casinos let you cancel a pending withdrawal and play it back; turn that off if offered.</li></ul>"
        + '<h2 id="kyc">Verification (KYC): what to expect</h2>'
        + "<p>Licensed offshore casinos must check who you are before paying out, to meet anti-money-laundering rules. Expect "
          "to provide photo ID (passport or New Zealand driver licence), proof of address dated within three months (a bank "
          "statement or utility bill), and sometimes proof that you own the card or wallet you used. Send clear colour images "
          "with all four corners visible.</p>"
        + '<h2 id="speed">How to speed up your first withdrawal</h2>'
        + steps([("Verify straight after sign-up", "Upload ID and proof of address before your first deposit, not when you want to withdraw."),
                 ("Deposit and withdraw with the same method", "It avoids extra ownership checks."),
                 ("Clear or decline the bonus", "Either finish the wagering or play without a bonus."),
                 ("Withdraw within the limits", "Split large amounts to match the daily limit."),
                 ("Keep records", "Screenshot your withdrawal request and any chat transcripts.")])
    )
    faqs = [
        ("Which online casino pays out fastest in NZ?",
         "<p>Speed depends mostly on the method: crypto and e-wallets are usually quickest, cards and bank transfers slower. We "
         "have not timed withdrawals, so we do not rank casinos on speed. We do publish each casino's withdrawal limits, which "
         "decide how long a large win takes.</p>"),
        ("Why is my casino withdrawal pending?",
         "<p>Usually because verification is not complete, a bonus is still active, or the casino has a manual approval period. "
         "Contact support and ask exactly what is outstanding.</p>"),
        ("Can I withdraw to a different method than I deposited with?",
         "<p>Sometimes, but most casinos pay back to the deposit method first and ask you to prove ownership of any new one.</p>"),
        ("Are instant withdrawal casinos real?",
         "<p>Some casinos approve crypto withdrawals automatically, so the money can arrive within minutes. 'Instant' rarely "
         "applies to a first withdrawal, which usually needs verification.</p>"),
        ("What is a withdrawal limit?",
         "<p>The most a casino will pay you in a day, week or month. Wins above it are paid in instalments. A daily win cap is "
         "different: amounts above it are not paid at all.</p>"),
    ]
    landing(P, "Fast payout casinos", "tama-rewiti", "hana-mcallister",
            "Fast payouts come down to three things: the casino's processing, verification and the payment method. Here are "
            "typical times by method, the reasons withdrawals stall, and every casino's published withdrawal limits.",
            [("3", "stages in every withdrawal"), ("NZ$7,500", "weekly limit at the NZD sites"), ("€4,000", "highest daily limit here"), ("0", "casino links")],
            ops, "Casinos with published withdrawal limits", "Only casinos whose limits we could source are listed, in our editor's order.",
            content, faqs, cols=["limit", "cap", "nzd", "pay", "score"])


# ---------------------------------------------------------------------------
def crypto():
    P = "/best-crypto-casinos/"
    ops = [o for o in CASINOS if o["crypto"]]
    content = (
        toc([("How crypto casinos work", "how"), ("Coins and fees", "coins"), ("From NZ dollars to crypto and back", "nz"),
             ("Risks", "risks"), ("Crypto and Inland Revenue", "tax"), ("FAQ", "faq")])
        + '<h2 id="how">How crypto casinos work</h2>'
        + "<p>A crypto casino gives you a wallet address for each coin it accepts. You send coins from your own wallet or "
          "exchange account, the casino credits your balance once the transaction is confirmed on the blockchain, and "
          "withdrawals go back to an address you supply. Most casinos here accept crypto alongside cards; Spino's cashier is "
          "built around crypto, with no NZD option. Some casinos convert your crypto into a fiat balance (euros or US dollars) for play, which adds an "
          "exchange step at both ends.</p>"
        + '<h2 id="coins">Which coins, and what they cost to move</h2>'
        + table(["Coin", "Typical network fee", "Typical confirmation", "Notes"], [
            ["Bitcoin (BTC)", "Variable, can be several dollars when busy", "10 to 60 minutes", "Most widely accepted"],
            ["Litecoin (LTC)", "Usually cents", "A few minutes", "Cheap and quick for casino transfers"],
            ["Tether (USDT)", "Depends on the network (TRC-20 and others cheaper than ERC-20)", "Minutes", "Pegged to the US dollar, so no price swings"],
            ["Ethereum (ETH)", "Variable", "Minutes", "Fees rise when the network is busy"],
            ["Solana, XRP, Dogecoin", "Usually cents", "Seconds to minutes", "Accepted at fewer casinos"],
        ], caption="Typical network behaviour, not casino-specific. Always send on the network the casino specifies.")
        + note("<p>Sending a coin on the wrong network, for example USDT on Ethereum to an address that expects TRC-20, can lose "
               "the funds permanently. Copy the address and network exactly from the casino's cashier.</p>", "warn", "Check the network")
        + '<h2 id="nz">From NZ dollars to crypto and back</h2>'
        + "<p>Most New Zealanders buy crypto on a local exchange with NZD from a bank account, then send it to the casino. To "
          "cash out, you send it back to the exchange, sell for NZD and withdraw to your bank. Each step can carry a fee: the "
          "exchange's trading fee or spread, the network fee, and any withdrawal fee. Some New Zealand banks look closely at "
          "transfers to and from exchanges, so use a registered exchange and keep records.</p>"
        + '<h2 id="risks">Risks of gambling with crypto</h2>'
        + "<ul><li><b>Price swings.</b> A Bitcoin balance can lose value while you play, separate from any gambling loss. USDT avoids this.</li>"
          "<li><b>Irreversible transfers.</b> There is no chargeback if something goes wrong.</li>"
          "<li><b>Less oversight.</b> Crypto-only casinos often have the lightest licensing.</li>"
          "<li><b>Faster spending.</b> Quick deposits make it easier to spend more than you planned; set a limit first.</li></ul>"
        + '<h2 id="tax">Crypto and Inland Revenue</h2>'
        + "<p>Casual gambling winnings are not taxable in New Zealand, but crypto is treated as property by Inland Revenue. If "
          "you buy crypto and it rises in value before you sell it, that gain can be taxable, whether or not you gambled with it. "
          'Keep records of what you bought and sold, and when. See <a href="/gambling-winnings-tax-nz/">gambling winnings tax</a>.</p>'
    )
    faqs = [
        ("Are crypto casinos legal in New Zealand?",
         "<p>Crypto casinos are offshore online casinos like any other. Playing is not an offence for individuals, but they are "
         "not licensed in New Zealand, cannot lawfully advertise here, and must stop serving New Zealand from 1 December 2026 "
         "unless they have applied for a licence. None of the crypto casinos on this page is run by a company that won a place "
         "in the October 2026 licence auction.</p>"),
        ("Which crypto is best for online casinos?",
         "<p>For low fees and no price risk, USDT on a low-fee network; for speed and low cost, Litecoin. Bitcoin is accepted "
         "most widely but can be slow and expensive when the network is busy.</p>"),
        ("Are crypto casino withdrawals faster?",
         "<p>Often, once a withdrawal is approved, because blockchain transfers settle in minutes. Verification still applies at "
         "most casinos on this list.</p>"),
        ("Do I pay tax on crypto casino winnings in NZ?",
         "<p>The gambling winnings themselves are generally not taxable, but gains on crypto you hold can be. Keep records.</p>"),
        ("Can I deposit NZD and withdraw crypto?",
         "<p>At many casinos, yes, but you may be asked to withdraw by your deposit method first. Check the cashier rules.</p>"),
    ]
    landing(P, "Crypto casinos NZ", "tama-rewiti", "wiremu-salter",
            "How Bitcoin, USDT, Litecoin and Ethereum casinos work, what moving each coin costs, the route from NZ dollars to "
            "crypto and back, the risks, and how Inland Revenue treats crypto. Every casino here accepts crypto.",
            [(str(len(ops)), "casinos accepting crypto"), ("Spino", "crypto-first, no NZD"), ("USDT", "no price swings"), ("0", "casino links")],
            ops, "Casinos that accept crypto, checked", "All accept crypto deposits according to their payment lists. In our editor's order.",
            content, faqs, cols=["licence", "nzd", "limit", "safety", "score"])


# ---------------------------------------------------------------------------
def live():
    P = "/live-casinos/"
    content = (
        toc([("How live casino works", "how"), ("Live blackjack", "bj"), ("Live roulette", "roulette"), ("Live baccarat", "bac"),
             ("Game shows", "shows"), ("Playing at New Zealand hours", "hours"), ("Etiquette and connection", "tips"), ("FAQ", "faq")])
        + '<h2 id="how">How live dealer casino games work</h2>'
        + "<p>A live casino streams a real dealer, real cards and a real wheel from a studio, usually in Europe, Asia or "
          "Latin America. You place bets on an on-screen overlay during a betting window, then watch the result. Optical "
          "character recognition reads the cards and wheel results so the game can settle your bets automatically. Most "
          "casinos on this list carry tables from the large live studios, so the same games appear in many lobbies.</p>"
        + '<h2 id="bj">Live blackjack</h2>'
        + "<p>Live blackjack uses the same rules as computer blackjack, so basic strategy keeps the house edge around 0.5%. "
          "Check two rules before you sit down: whether blackjack pays 3:2 (good) or 6:5 (much worse), and whether the dealer "
          "hits or stands on soft 17. Many live tables have a fixed number of seats; 'infinite' versions let any number of "
          "players play the same hand. Side bets such as Perfect Pairs and 21+3 carry much higher edges.</p>"
        + '<h2 id="roulette">Live roulette</h2>'
        + "<p>Choose European (single zero, 2.7% edge) or French (single zero, with La Partage on even-money bets, about 1.35%) "
          "over American (double zero, 5.26%). Multiplier variants such as Lightning Roulette add random multipliers on "
          "straight-up numbers but pay less on standard straight-up wins to fund them.</p>"
        + '<h2 id="bac">Live baccarat</h2>'
        + "<p>Baccarat is a game of pure chance with three bets: banker (1.06% edge after commission), player (1.24%) and tie "
          "(about 14.4%). 'No commission' tables usually pay less on certain banker wins instead. Speed baccarat deals faster "
          "rounds, which means more bets per hour and more expected cost per hour.</p>"
        + '<h2 id="shows">Live game shows</h2>'
        + "<p>Game shows such as money wheels with bonus rounds are entertainment-first. Their RTP varies by bet, often between "
          "about 95% and 97%, and the top multipliers are rare by design. They move fast, so set a time limit as well as a "
          "money limit.</p>"
        + '<h2 id="hours">Playing at New Zealand hours</h2>'
        + "<p>Because most studios are in Europe, the busiest tables are often New Zealand early mornings, and New Zealand "
          "evenings line up with European mornings when fewer tables may be open. Studios in Asia are closer to New Zealand "
          "time. Stake ranges are set per table, commonly from NZ$1 to NZ$5 minimum on mainstream tables, with VIP tables much "
          "higher.</p>"
        + '<h2 id="tips">Etiquette, chat and connection</h2>'
        + "<ul><li>Use a stable connection; if you drop out mid-hand, the table's rules decide what happens to your bet.</li>"
          "<li>Chat is moderated; dealers will not respond to abuse.</li>"
          "<li>Take screenshots of any disputed result and note the round ID shown on screen.</li></ul>"
    )
    faqs = [
        ("Is live casino better than online casino games?",
         "<p>The odds are the same for the same rules. Live games are slower, so you place fewer bets per hour, which can mean a "
         "lower expected cost per hour. They also feel more transparent because you see the cards and wheel.</p>"),
        ("Are live dealer games rigged?",
         "<p>Major studios are audited and stream continuously. The bigger risk is the casino's own terms and payout record, "
         "which is what our reviews look at.</p>"),
        ("What is the best live casino game for odds?",
         "<p>Live blackjack with basic strategy, at about 0.5% house edge, then baccarat on the banker bet.</p>"),
        ("Can I play live casino on my phone?",
         "<p>Yes. Every casino here streams live tables in a mobile browser. Use Wi-Fi for a stable stream.</p>"),
        ("What are the minimum bets at live casinos?",
         "<p>Usually NZ$1 to NZ$5 on mainstream tables, set per table. VIP and high-limit tables start much higher.</p>"),
    ]
    landing(P, "Live casino NZ", "olivia-brandt", "hana-mcallister",
            "How live dealer blackjack, roulette, baccarat and game shows work, the house edge on each bet, stake ranges and "
            "studio hours for New Zealand players. Plus the casinos New Zealanders ask about, checked.",
            [("0.5%", "live blackjack edge"), ("1.06%", "baccarat banker"), ("2.7%", "European roulette"), ("0", "casino links")],
            CASINOS, "Casinos with live dealer lobbies, checked", "In our editor's order. Compare licence, NZD support and limits.",
            content, faqs)


# ---------------------------------------------------------------------------
def bonuses():
    P = "/online-casinos/bonuses/"
    with_offer = [o for o in CASINOS if o.get("offer")]
    content = (
        toc([("How a casino bonus works", "how"), ("Wagering in dollars", "wagering"), ("Offers on record", "offers"),
             ("The terms that matter", "terms"), ("Types of bonus", "types"), ("When to say no", "no"), ("FAQ", "faq")])
        + '<h2 id="how">How a casino bonus works</h2>'
        + "<p>A deposit bonus adds money to your account that you cannot withdraw straight away. To convert it into cash, you "
          "must bet a set multiple of it, the wagering requirement (also called playthrough or rollover). Until then, the "
          "bonus and usually any winnings from it are locked. If you withdraw early, you normally lose both.</p>"
        + '<h2 id="wagering">Wagering, worked out in dollars</h2>'
        + "<p>The formula is simple: <b>bonus × wagering multiple = amount you must bet</b>. Some casinos apply the multiple to "
          "the deposit plus the bonus, which doubles it. Then <b>amount bet × house edge = expected cost</b>.</p>"
        + table(["Bonus", "Wagering", "You must bet", "Expected cost at 96% RTP", "Expected cost at 94% RTP"], [
            ["NZ$100", "7x", "NZ$700", "NZ$28", "NZ$42"],
            ["NZ$100", "20x", "NZ$2,000", "NZ$80", "NZ$120"],
            ["NZ$100", "35x", "NZ$3,500", "NZ$140", "NZ$210"],
            ["NZ$100", "40x", "NZ$4,000", "NZ$160", "NZ$240"],
            ["NZ$100", "40x deposit + bonus", "NZ$8,000", "NZ$320", "NZ$480"],
        ], caption="Average outcomes. If expected cost exceeds the bonus, the bonus is worth less than nothing on average.")
        + "<p>Read the last column carefully. At 40x on deposit plus bonus, a NZ$100 bonus has an average cost of NZ$320 to "
          "clear. That does not mean you will lose it, but on average the bonus costs more than it gives.</p>"
        + '<h2 id="offers">Offers on our records</h2>'
        + "<p>We only quote offers supplied to us or reported by a source we can name, in the currency that source used "
          "(NZ$, $ or €). Reported offers come from 2026 reviews, not the casino's own terms, so check the cashier before "
          "depositing. The amount you receive depends on your currency.</p>"
        + table(["Brand", "Offer on record", "Wagering", "Status"], [
            [op_cell(o), esc(offer_txt(o)), esc(o["wagering"] or "Not confirmed"),
             "Reported, unconfirmed" if "reported" in o["offer"] else "Supplied"] for o in with_offer
        ] + [[op_cell(BY["gunsbet"]), esc(offer_txt(BY["gunsbet"])), "Not confirmed", "Supplied (betting listing)"],
             [op_cell(BY["betandplay"]), esc(offer_txt(BY["betandplay"])), esc(BY["betandplay"]["wagering"]), "Reported, unconfirmed (betting listing)"]])
        + '<h2 id="terms">The terms that matter more than the headline</h2>'
        + table(["Term", "What it means", "What good looks like"], [
            ["Wagering multiple", "How many times you must bet the bonus", "Under 30x, and on the bonus only"],
            ["Game weighting", "How much each game counts towards wagering", "Pokies 100%; table games often 0% to 10%"],
            ["Maximum bet", "Largest stake allowed while a bonus is active", "Clearly stated, commonly around NZ$8 or €5"],
            ["Time limit", "Days to complete wagering", "At least 7, ideally 30"],
            ["Maximum cashout", "Cap on what bonus winnings can pay", "None, or several times the bonus"],
            ["Prompt withdrawal rule", "Winnings above a cap are voided if not withdrawn once wagering ends", "Know it exists; several brands here have it"],
            ["Excluded deposits", "Methods that do not qualify, often e-wallets", "Listed plainly"],
        ])
        + '<h2 id="types">Types of casino bonus</h2>'
        + "<ul><li><b>Welcome package</b>: matched deposits across your first few deposits, often with free spins.</li>"
          "<li><b>Free spins</b>: spins on a named pokie at a fixed stake; winnings usually carry wagering.</li>"
          "<li><b>Reload</b>: a smaller match on later deposits, often weekly.</li>"
          "<li><b>Cashback</b>: a percentage of net losses returned, sometimes as cash, sometimes as bonus money with wagering.</li>"
          "<li><b>High-roller bonus</b>: larger match for large deposits, for example CrownSlots' reported 100% up to €5,000 on €500 or more.</li>"
          "<li><b>No deposit bonus</b>: small amounts or spins without depositing; see <a href=\"/no-deposit-casinos/\">no deposit bonuses</a>.</li></ul>"
        + '<h2 id="no">When to say no to a bonus</h2>'
        + "<p>Playing without a bonus is often the better choice. Decline it if you mainly play table or live games (they rarely "
          "count), if you want to withdraw quickly, if you like to bet more than the maximum stake, or if the expected cost in "
          "the table above is higher than the bonus itself.</p>"
        + note("<p>From 2027, licensed New Zealand casinos will operate under DIA regulations covering advertising and "
               "inducements. Offers from offshore casinos are not covered by those rules.</p>", "law", "Bonuses and New Zealand rules")
    )
    faqs = [
        ("What is a good wagering requirement?",
         "<p>Under 30x on the bonus amount only is good for an offshore casino. Trixino's 7x on record is unusually low; 35x to 40x "
         "is normal.</p>"),
        ("What is the biggest casino bonus for NZ players?",
         "<p>By headline, Trixino's 777% up to €7,777 and Gunsbet's 285% up to €7,500 are the largest on our records. The size of the "
         "headline matters far less than the wagering.</p>"),
        ("Can I withdraw a casino bonus?",
         "<p>Only after you complete the wagering requirement within the time limit and follow the other terms. Withdrawing early "
         "usually cancels the bonus and its winnings.</p>"),
        ("Do table games count towards wagering?",
         "<p>Usually very little or not at all. Most casinos count pokies at 100% and table and live games at 0% to 10%.</p>"),
        ("Why was my bonus winnings cancelled?",
         "<p>Common reasons are breaking the maximum bet rule, playing excluded games, using a non-qualifying deposit method, or "
         "missing the time limit. Ask support for the exact term they relied on.</p>"),
        ("Should I take a welcome bonus?",
         "<p>Only if the expected cost of the wagering is lower than the bonus and the terms suit how you play. Otherwise, play "
         "with your own money and withdraw whenever you like.</p>"),
    ]
    landing(P, "Casino bonuses explained", "hana-mcallister", "tama-rewiti",
            "A casino bonus is only as good as its wagering. Here is the maths in dollars, the offers on our records, the terms "
            "that decide whether a bonus is worth taking, and when to say no.",
            [("7x", "lowest wagering on record"), ("40x", "typical offshore wagering"), ("NZ$160", "avg cost to clear NZ$100 at 40x"), ("0", "bonus codes or links")],
            CASINOS, "Casinos checked, with any offer on record", "Offers are shown only where supplied or sourced. In our editor's order.",
            content, faqs, cols=["offer", "licence", "nzd", "safety", "score"],
            trail=[("Online casinos", "/"), ("Bonuses", P)])


# ---------------------------------------------------------------------------
def no_deposit():
    P = "/no-deposit-casinos/"
    content = (
        toc([("What a no deposit bonus is", "what"), ("Free spins vs bonus cash", "types"), ("The catch: caps and wagering", "catch"),
             ("Worked example", "example"), ("Spotting fake offers", "fake"), ("Claiming one sensibly", "claim"), ("FAQ", "faq")])
        + note("<p>We have no confirmed no deposit offer on record for any casino on this list at the moment. Offers of this kind "
               "change weekly and are often limited by country. This page explains how they work so you can judge any offer "
               "you come across.</p>", "tip", "Current offers")
        + '<h2 id="what">What a no deposit bonus is</h2>'
        + "<p>A no deposit bonus gives a new player a small amount of play without paying in first: free spins on a named "
          "pokie, a few dollars of bonus cash, or occasionally free play for a short time. Casinos use them to get you to "
          "register and verify an account. They are genuinely free to claim, but the terms are designed so that very few "
          "players turn them into withdrawable money.</p>"
        + '<h2 id="types">Free spins vs bonus cash</h2>'
        + table(["Type", "Typical size", "Typical terms"], [
            ["No deposit free spins", "10 to 50 spins at the minimum stake", "Winnings credited as bonus money with wagering, then capped"],
            ["No deposit bonus cash", "A few dollars to NZ$20", "Wagering of 40x to 60x, game restrictions, low max cashout"],
            ["Free play", "A larger amount for a short time", "Only a small part of any profit is kept"],
        ])
        + '<h2 id="catch">The catch: win caps and wagering</h2>'
        + "<p>Almost every no deposit offer carries a maximum cashout, commonly NZ$50 to NZ$100, regardless of what you win. "
          "Winnings also usually need wagering, often at a higher multiple than deposit bonuses, and many casinos require a "
          "small deposit before you can withdraw anything at all, to verify your payment method.</p>"
        + '<h2 id="example">A worked example</h2>'
        + "<p>Take 20 free spins at NZ$0.20 on a 96% RTP pokie. The spins are worth NZ$4 of stake, and on average return about "
          "NZ$3.84. Suppose you win NZ$10. With 40x wagering on winnings, you must bet NZ$400; on a 96% game that costs about "
          "NZ$16 on average, more than the NZ$10 you won. Most players finish with nothing, a few clear the wagering, and the "
          "max cashout caps the lucky ones. That is the honest value of most no deposit offers: some entertainment and a look "
          "at the casino.</p>"
        + '<h2 id="fake">Spotting fake no deposit offers</h2>'
        + "<ul><li>Huge no deposit amounts (hundreds of dollars) with no visible terms.</li>"
          "<li>Requests to pay a 'verification fee' or 'tax' to release winnings.</li>"
          "<li>Offers sent by text message or social media from accounts that are not the casino's.</li>"
          "<li>Sites with no licence number, or a number that is not on the regulator's register.</li></ul>"
        + note("<p>No legitimate casino asks you to pay to receive a bonus or to unlock a withdrawal.</p>", "warn", "Never pay to claim")
        + '<h2 id="claim">Claiming one sensibly</h2>'
        + steps([("Read the full terms first", "Find the wagering, max cashout, eligible games and time limit."),
                 ("Check the casino, not the offer", "A free offer at a casino with no verified licence is not worth your personal details."),
                 ("Verify early", "You will need ID to withdraw anyway."),
                 ("Treat it as a trial", "Use it to judge the site's support and cashier, not as a way to make money.")])
    )
    faqs = [
        ("Are there real no deposit bonuses in NZ?",
         "<p>Offshore casinos do run them from time to time, though we have none confirmed on record right now. They are real but "
         "small, and they almost always cap what you can win.</p>"),
        ("Can you win real money with a no deposit bonus?",
         "<p>Yes, but only up to the maximum cashout, commonly NZ$50 to NZ$100, and only after completing wagering. Many casinos "
         "also require a deposit before your first withdrawal.</p>"),
        ("What is a max cashout?",
         "<p>The most you can withdraw from bonus winnings, however much you win. Anything above it is removed when you withdraw.</p>"),
        ("Do no deposit free spins have wagering?",
         "<p>Usually yes: winnings from the spins are credited as bonus money and must be wagered. Wager-free spins exist but are rare.</p>"),
        ("Why do casinos ask for ID for a free bonus?",
         "<p>Licensed offshore casinos must verify customers before paying out, and verification also stops people claiming the "
         "same offer many times.</p>"),
    ]
    landing(P, "No deposit bonuses", "hana-mcallister", "tama-rewiti",
            "No deposit bonuses are free to claim and designed so few players cash out. Here is how free spins and bonus cash "
            "really work, the maths of a typical offer, and how to tell a real offer from bait.",
            [("NZ$50–100", "typical max cashout"), ("40x+", "typical wagering"), ("NZ$3.84", "avg return on 20 x 20c spins"), ("0", "bonus codes or links")],
            CASINOS, "Casinos checked", "We have no confirmed no deposit offers on record at present. In our editor's order.",
            content, faqs, cols=["licence", "nzd", "limit", "safety", "score"],
            trail=[("Bonuses", "/online-casinos/bonuses/"), ("No deposit bonuses", P)])


def build():
    pokies(); new_casinos(); high_payout(); fast_payout(); crypto(); live(); bonuses(); no_deposit()
