"""Online betting NZ (the money page from the second brief) and sports betting sites."""
from lib import *


def bet_law_note():
    return note('<p>Since <b>28 June 2025</b>, under the Racing Industry Amendment Act 2025, TAB NZ is the only operator allowed to '
                'offer online racing and sports betting to people in New Zealand, and offshore bookmakers may not take bets from '
                'New Zealanders. TAB NZ runs its betting through a 25-year partnership with Entain, which also operates the online '
                'brand Betcha alongside TAB. The offshore sportsbooks named on this site are covered for information only; we do '
                'not link to them or carry their offers.</p>', "law", "Betting law in New Zealand, in short")


def _odds_table():
    return table(["Decimal odds", "Fractional", "Implied probability", "NZ$10 bet returns"], [
        ["1.50", "1/2", "66.7%", "NZ$15.00"], ["1.91", "10/11", "52.4%", "NZ$19.10"], ["2.00", "evens", "50.0%", "NZ$20.00"],
        ["3.00", "2/1", "33.3%", "NZ$30.00"], ["5.00", "4/1", "20.0%", "NZ$50.00"], ["11.00", "10/1", "9.1%", "NZ$110.00"],
    ], caption="Implied probability = 1 ÷ decimal odds. Returns include your stake.")


def online_betting():
    P = "/online-betting/"
    t, d, h1 = META[P]
    A, C = "jess-tuilagi", "wiremu-salter"
    sections = [("The law since June 2025", "law"), ("TAB NZ and Betcha", "tab"), ("Offshore sportsbooks we cover", "the-list"),
                ("How betting odds work", "odds"), ("Bookmaker margins", "margin"), ("Bet types explained", "types"),
                ("New Zealand sport and racing markets", "markets"), ("Live betting and cash-out", "live"),
                ("Comparing value", "value"), ("Betting and tax", "tax"), ("Betting safely", "safer"), ("FAQ", "faq")]
    margin_rows = [
        ["Two-way market, 1.91 / 1.91", "52.36% + 52.36%", "104.7%", "4.7%"],
        ["Two-way market, 1.95 / 1.87", "51.28% + 53.48%", "104.8%", "4.8%"],
        ["Two-way market, 1.80 / 1.80", "55.56% + 55.56%", "111.1%", "11.1%"],
        ["Three-way football, 2.40 / 3.30 / 3.00", "41.7% + 30.3% + 33.3%", "105.3%", "5.3%"],
    ]
    types = [
        ["Head to head (money line)", "Pick the winner", "The simplest bet; draws may void or lose depending on the market"],
        ["Line (handicap)", "One side gets a points start, e.g. All Blacks −12.5", "Common in rugby and league; turns a mismatch into close odds"],
        ["Total (over/under)", "Combined points above or below a figure", "Weather and referee trends move rugby totals"],
        ["Margin bands", "Winning margin within a range, e.g. 1–12", "Popular in rugby and league; higher margins built in"],
        ["Multi (accumulator)", "Several legs; all must win", "Margins compound with every leg, so long multis are expensive"],
        ["Same-game multi", "Several outcomes in one game", "Legs are correlated, and bookmakers price that in heavily"],
        ["Futures", "Season winners, e.g. Super Rugby Pacific champion", "Money is tied up for months"],
        ["Racing: win, place, quinella, trifecta", "Pari-mutuel (tote) or fixed odds", "Tote dividends depend on the pool; fixed odds are set in advance"],
    ]
    markets = [
        ["Rugby union", "All Blacks tests, Super Rugby Pacific, Bunnings NPC, Rugby Championship", "Line and margin markets are the most popular"],
        ["Rugby league", "NRL including the One New Zealand Warriors, State of Origin", "Try-scorer markets; line betting"],
        ["Netball", "ANZ Premiership, Silver Ferns internationals", "Fewer markets than rugby; mainly head to head and line"],
        ["Cricket", "Black Caps tests, ODIs and T20s, Dream11 Super Smash", "Session and player markets in T20"],
        ["Football", "Wellington Phoenix and Auckland FC in the A-League, the Premier League", "Three-way result markets"],
        ["Racing", "Thoroughbred and harness meetings across New Zealand and Australia", "Commercial greyhound racing in New Zealand ended on 1 August 2026"],
        ["US sport", "NBA, NFL, MLB", "Mainly overnight or morning New Zealand time"],
    ]
    faqs = [
        ("Is online betting legal in New Zealand?",
         "<p>Yes, with TAB NZ. Since 28 June 2025, TAB NZ has been the only operator allowed to offer online racing and sports "
         "betting to people in New Zealand. Offshore bookmakers are not permitted to take bets from New Zealanders.</p>"),
        ("Can I still use offshore betting sites from New Zealand?",
         "<p>The 2025 law is aimed at the bookmakers: offshore operators may not offer betting to New Zealanders, and many now "
         "block New Zealand accounts. If you hold an offshore account, withdraw your balance, and be aware you have no New "
         "Zealand protection if a dispute arises.</p>"),
        ("What is Betcha?",
         "<p>Betcha is an online betting brand run by Entain alongside TAB NZ, under the 25-year partnership between the two that "
         "was agreed in 2023. It operates within TAB NZ's legal framework.</p>"),
        ("What are the best odds for betting in NZ?",
         "<p>Odds vary by market and change constantly. The way to judge value is the bookmaker's margin: add up the implied "
         "probabilities of every outcome. The closer to 100%, the better the value.</p>"),
        ("How do I work out implied probability from odds?",
         "<p>Divide 1 by the decimal odds. Odds of 2.50 imply 1 ÷ 2.50 = 40%. If you think the real chance is higher than 40%, "
         "the bet is good value; if lower, it is not.</p>"),
        ("Are betting winnings taxed in New Zealand?",
         "<p>Not for recreational punters. Inland Revenue generally treats casual gambling winnings, including betting, as "
         "non-taxable. Professional gambling can be different.</p>"),
        ("What is a multi, and why do they pay so much?",
         "<p>A multi combines several selections, and every one must win. The odds multiply, and so does the bookmaker's margin, "
         "so long multis carry a much larger built-in edge than single bets.</p>"),
        ("What happened to greyhound racing betting?",
         "<p>Commercial greyhound racing in New Zealand ended on 1 August 2026 under the Racing Industry (Closure of Greyhound "
         "Racing Industry) Amendment Act, passed in April 2026.</p>"),
        ("How can I limit my betting?",
         "<p>Set deposit limits in your betting account, use your bank's gambling block, and call the Gambling Helpline on "
         '<a href="tel:0800654655">0800 654 655</a> if betting is causing harm.</p>'),
    ]
    faq_html, ents = faq(faqs)
    body = (hero(h1, "Online betting in New Zealand changed in June 2025, when TAB NZ became the only lawful online "
                 "bookmaker. This guide explains the law, how odds and bookmaker margins work, every main bet type, the "
                 "rugby, league, netball, cricket and racing markets Kiwis bet on, and how to bet within your limits.",
                 A, C, [("28 Jun 2025", "offshore bookmaker ban in force"), ("1", "lawful online bookmaker: TAB NZ"),
                        ("1 Aug 2026", "greyhound racing ended"), ("0", "bookmaker links")], kicker=f"Checked {CHECKED}")
            + crumbs([("Online betting NZ", P)])
            + '<section class="sec"><div class="wrap prose">' + bet_law_note() + toc(sections)
            + '<h2 id="law">Online betting law in New Zealand since June 2025</h2>'
            + "<p>The Racing Industry Amendment Act 2025 passed on 27 June 2025 and took effect the next day. It extended TAB NZ's "
              "long-standing exclusive right to offer racing and sports betting so that it clearly covers online betting, and "
              "it closed the door on offshore bookmakers that had been taking bets from New Zealanders without paying into New "
              "Zealand racing or sport. Offshore operators are not allowed to offer betting to people in New Zealand.</p>"
            + "<p>For punters, the practical effect is that a legal online bet in New Zealand is a bet with TAB NZ or its "
              "partner brand. Offshore sportsbooks may still be visible online, but they are not authorised here, they "
              "cannot lawfully advertise to you, and you have no New Zealand regulator to turn to if one refuses to pay.</p>"
            + table(["Question", "TAB NZ (and Betcha)", "Offshore sportsbook"], [
                ["Allowed to take bets from New Zealanders?", "Yes", "No, since 28 June 2025"],
                ["Regulated in New Zealand?", "Yes, under the Racing Industry Act 2020", "No; licensed overseas, if at all"],
                ["Returns money to NZ racing and sport?", "Yes", "No"],
                ["Complaint route in New Zealand?", "Yes", "No"],
                ["NZD accounts?", "Yes", "Some"],
            ])
            + '<h2 id="tab">TAB NZ and Betcha</h2>'
            + "<p>TAB NZ is a statutory body set up under the Racing Industry Act 2020. In 2023 it agreed a 25-year partnership "
              "with Entain, a large international betting company, which now runs TAB NZ's betting products. Entain also "
              "launched Betcha, an online betting brand that operates alongside TAB NZ under the same legal framework. Both "
              "offer fixed-odds sports betting; TAB NZ also runs pari-mutuel (tote) racing pools.</p>"
            + "<p>A monopoly has trade-offs. Supporters point to funding for racing and sport and to New Zealand harm-reduction "
              "rules. Critics, including some punters, say odds and limits are less competitive than offshore books used to "
              "be. Either way, it is the legal position.</p>"
            + "</div></section>"

            + f'<section class="sec sec--alt" id="the-list"><div class="wrap"><h2>Offshore sportsbooks New Zealanders ask about</h2>'
              '<p class="intro">For information only. None of these sportsbooks is permitted to take bets from people in New '
              'Zealand under the 2025 law. Each row links to our review, with licence, owner and limits sourced.</p>'
            + toplist(SPORTS, "sports") + compare(SPORTS, ["products", "licence", "nzd", "limit", "safety", "score"])
            + rg_line() + "</div></section>"

            + '<section class="sec"><div class="wrap prose">'
            + '<h2 id="odds">How betting odds work</h2>'
            + "<p>New Zealand bookmakers use decimal odds. The number is what a winning NZ$1 bet returns, including the stake. "
              "Odds of 3.00 return NZ$3 for every NZ$1, a profit of NZ$2. The odds also tell you the probability the bookmaker "
              "is pricing in: divide 1 by the odds.</p>"
            + _odds_table()
            + '<h2 id="margin">Bookmaker margins: the number that decides value</h2>'
            + "<p>Add up the implied probabilities of every outcome in a market. In a fair market they would total 100%. They "
              "always total more, and the excess is the bookmaker's margin (also called the overround or vig). It is the "
              "built-in cost of betting, in the same way the house edge is the cost of casino games.</p>"
            + table(["Market", "Implied probabilities", "Total", "Margin"], margin_rows,
                    caption="The lower the margin, the better the value for the same outcome.")
            + "<p>Margins are usually lowest on the main markets of big events, such as a head-to-head on an All Blacks test, and "
              "highest on niche markets, same-game multis and long-range futures.</p>"
            + '<h2 id="types">Bet types explained</h2>'
            + table(["Bet", "How it works", "Good to know"], types)
            + '<h2 id="markets">New Zealand sport and racing markets</h2>'
            + table(["Sport", "Competitions", "Notes"], markets)
            + '<h2 id="live">Live (in-play) betting and cash-out</h2>'
            + "<p>Live betting lets you bet after a match starts, with odds updating every few seconds. It is the fastest form of "
              "betting and the easiest way to bet more than you planned. Cash-out lets you settle a bet early for less than "
              "its full return, or to cut a loss. The cash-out price includes a margin of its own, so cashing out regularly "
              "costs money over time.</p>"
            + '<h2 id="value">How to compare value as a punter</h2>'
            + steps([("Compare the margin, not the headline odds", "Work out the total implied probability for the market you want."),
                     ("Bet singles over long multis", "Every extra leg multiplies the bookmaker's margin."),
                     ("Keep records", "Track stakes and results. Most people underestimate their losses."),
                     ("Ignore boosts that hide margins", "A boosted price on a same-game multi can still carry a large margin."),
                     ("Set the stake before the game", "Decide your total for the day before live markets open.")])
            + '<h2 id="tax">Betting and tax</h2>'
            + "<p>Inland Revenue generally does not tax casual gambling winnings, including betting wins, because they are not "
              "income from a business. If you bet with the regularity, organisation and intention of a business, winnings can "
              'be taxable and losses may be deductible. See <a href="/gambling-winnings-tax-nz/">gambling winnings tax</a>.</p>'
            + '<h2 id="safer">Betting safely</h2>'
            + "<ul><li>Set a deposit limit in your account before your first bet.</li>"
              "<li>Turn on your bank's gambling block if you want a hard stop.</li>"
              "<li>Never chase losses with bigger bets or extra multis.</li>"
              "<li>Avoid betting on teams you support when emotions run high.</li>"
              '<li>Free, confidential help is available 24/7 from the Gambling Helpline on <a href="tel:0800654655">0800 654 655</a>.</li></ul>'
            + faq_html
            + "<h2>Related guides</h2>" + cards([("Sports betting sites compared", "TAB NZ and the offshore sportsbooks New Zealanders ask about, side by side.", "/best-sports-betting-sites/"),
                                                  ("NZ online casino law", "The 2026 Act, the advertising ban and the 1 December cut-off.", "/nz-online-casino-law/"),
                                                  ("Gambling winnings tax", "When betting and casino wins are taxable in New Zealand.", "/gambling-winnings-tax-nz/"),
                                                  ("Responsible gambling", "Bank blocks, deposit limits, self-exclusion and free help.", "/responsible-gambling/"),
                                                  ("Payment methods", "Cards, e-wallets, bank transfer and crypto from New Zealand.", "/payment-methods/"),
                                                  ("Casino reviews", "All 15 casino and betting sites, checked and scored.", "/casino-reviews/")], 3)
            + authorbox(A) + "</div></section>")
    schema = [schema_webpage(P), schema_crumbs(P, [("Online betting NZ", P)]), schema_article(P, h1, A, C),
              schema_itemlist(P, SPORTS, "Offshore sportsbooks New Zealanders ask about"), schema_faq(P, ents),
              schema_howto(P, "How to compare betting value", [("Compare the margin, not the headline odds", "Work out the total implied probability for the market you want."),
                                                              ("Bet singles over long multis", "Every extra leg multiplies the bookmaker's margin."),
                                                              ("Keep records", "Track stakes and results."),
                                                              ("Ignore boosts that hide margins", "A boosted price can still carry a large margin."),
                                                              ("Set the stake before the game", "Decide your total for the day before live markets open.")]),
              schema_person(A), schema_person(C)]
    write(P, body, schema, priority=0.9, freq="weekly", author=A)


def sports_sites():
    P = "/best-sports-betting-sites/"
    content = (
        bet_law_note()
        + toc([("TAB NZ vs offshore books", "vs"), ("What to compare", "compare-what"), ("Margins in practice", "margins"),
               ("Withdrawal limits and win caps", "limits"), ("Red flags", "flags"), ("FAQ", "faq")])
        + '<h2 id="vs">TAB NZ compared with offshore sportsbooks</h2>'
        + table(["", "TAB NZ / Betcha", "Offshore sportsbooks on this page"], [
            ["Legal to offer betting in NZ", "Yes", "No, since 28 June 2025"],
            ["Regulator", "New Zealand law (Racing Industry Act 2020)", "Anjouan, Tobique, Curaçao or Kahnawake, if confirmed"],
            ["Harm-minimisation rules", "New Zealand requirements", "Operator's own tools"],
            ["Money to NZ racing and sport", "Yes", "No"],
            ["Disputes", "New Zealand complaint routes", "Overseas regulator, if any"],
        ])
        + '<h2 id="compare-what">What to compare between betting sites</h2>'
        + "<p>Before the 2025 law, comparison sites ranked bookmakers on odds boosts and sign-up bets. For New Zealanders the "
          "first question is now legal: only TAB NZ may take your bets. For the offshore brands on this page, the facts that "
          "matter are the same as for casinos: who owns the site, which licence it holds, whether it pays in NZD, and how much "
          "it lets you withdraw.</p>"
        + '<h2 id="margins">Margins in practice</h2>'
        + "<p>A two-way market priced 1.91 and 1.91 carries a margin of about 4.7%. Priced 1.80 and 1.80, it carries about "
          "11.1%. Over a season of NZ$20 bets, that difference is the single biggest factor in what betting costs you. Our "
          '<a href="/online-betting/#margin">online betting guide</a> shows how to work it out for any market.</p>'
        + '<h2 id="limits">Withdrawal limits and win caps</h2>'
        + "<p>Several offshore books here cap what you can win or withdraw: Bet&Play has a daily win cap of US$50,000; Rivo and "
          "Smash cap daily wins at €100,000 and limit withdrawals to €1,000 a day. Combined casino and sportsbook accounts "
          "usually share one withdrawal limit across both.</p>"
        + '<h2 id="flags">Red flags at any betting site</h2>'
        + "<ul><li>Bets voided after a win for 'palpable error' without a clear explanation.</li>"
          "<li>Stake limits imposed after a few wins, then withdrawals delayed.</li>"
          "<li>Sign-up bets with rollover on odds of 1.80 or more, which forces many more bets.</li>"
          "<li>No licence number, or an owner that is not named.</li></ul>"
    )
    faqs = [
        ("What is the best sports betting site in NZ?",
         "<p>Legally, TAB NZ (including its partner brand Betcha) is the only online bookmaker allowed to take bets from people in "
         "New Zealand. The offshore sportsbooks on this page are listed for information only.</p>"),
        ("Why can't I bet with offshore bookmakers any more?",
         "<p>The Racing Industry Amendment Act 2025 made TAB NZ the only lawful provider of online racing and sports betting "
         "in New Zealand from 28 June 2025. Offshore operators are not permitted to take bets from New Zealanders.</p>"),
        ("Do offshore sportsbooks accept NZD?",
         "<p>Some list NZD as a balance currency, including Lucky Vibe, Rooster Bet, Fortune Play, Bet&Play and Gunsbet. That "
         "does not make them lawful providers in New Zealand.</p>"),
        ("Which betting site has the best odds?",
         "<p>It depends on the market and changes constantly. Compare margins: total the implied probabilities of every outcome; "
         "the lower the total above 100%, the better.</p>"),
        ("Are betting sites safe?",
         "<p>TAB NZ is regulated in New Zealand. Offshore sportsbooks are only as safe as their overseas licence and their own "
         "record, which is what our reviews check.</p>"),
    ]
    landing(P, "Sports betting sites", "jess-tuilagi", "wiremu-salter",
            "How TAB NZ compares with the offshore sportsbooks New Zealanders still ask about, checked on licence, owner, NZD "
            "banking and limits. Since June 2025 only TAB NZ may lawfully take your bets.",
            [("1", "lawful online bookmaker"), (str(len(SPORTS)), "offshore books checked"), ("4.7%", "margin at 1.91/1.91"), ("0", "bookmaker links")],
            SPORTS, "Offshore sportsbooks New Zealanders ask about", "For information only; none may take bets from New Zealanders "
            "under the 2025 law. In our editor's order.", content, faqs, kind="sports",
            cols=["products", "licence", "nzd", "limit", "safety", "score"],
            trail=[("Online betting NZ", "/online-betting/"), ("Sports betting sites", P)],
            related=[("Online betting NZ", "The law, odds, margins, bet types and NZ markets.", "/online-betting/")] + [r for r in RELATED if r[2] not in (P, "/online-betting/")][:5])


def build():
    online_betting(); sports_sites()
