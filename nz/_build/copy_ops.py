"""Hand-written review copy for each operator. Every sentence is drawn from the
sourced facts in ops_data.py (checked 8 October 2026). No test results, payout
timings or game counts are claimed, because we have not measured them."""

COPY = {
 "crownslots": dict(
  tagline="A large staged welcome package, but the operator and licence number are not clearly published.",
  intro=("CrownSlots is a casino-only brand that review sites date to 2024. Its pitch is the size of its welcome package: "
         "the publisher-supplied headline is 390% up to €3,700 plus 175 free spins, paid across the first few deposits. "
         "The weakness is transparency. The sources we checked disagree on which company runs it, and none quoted a "
         "Curaçao licence number we could look up."),
  pros=["One of the larger welcome packages on our list, spread over several deposits",
        "Weekly extras reported: Thursday cashback of up to 20% and a Thursday reload",
        "Crypto deposits accepted alongside cards"],
  cons=["Operating company not confirmed: sources name both Hollycorn N.V. and Dama N.V.",
        "No licence number published in the sources we checked",
        "No Casino Guru profile, so there is no independent safety rating to compare",
        "Bonus amounts are in euros, so every NZD deposit is converted"],
  verdict=("CrownSlots offers a big headline package, but we could not confirm who runs it or under which licence number, "
           "and those are the two facts that matter most if something goes wrong. It scores low for that reason, not "
           "because of anything we found wrong with the games or the offer.")),
 "spinjo": dict(
  tagline="The strongest public record on our list: named owner, two verified licences and an NZD balance.",
  intro=("Spinjo is a casino-only brand from Hollycorn N.V., the group behind Lucky Vibe and Lucky7even. It holds two "
         "licences that Casino Guru marks as verified, Anjouan (ALSI-202509073-FI2) and Tobique (0000064), and it has the "
         "joint-highest Casino Guru Safety Index on this site at 8.9. Balances can be held in New Zealand dollars."),
  pros=["Joint-highest independent Safety Index on our list (8.9)",
        "Named owner and two licences verified by Casino Guru",
        "NZD balance, so no conversion on deposits or withdrawals",
        "Withdrawal limits published in NZD: $3,000 a day, $7,500 a week, $30,000 a month"],
  cons=["Offshore licence: no New Zealand regulator to complain to",
        "Casino Guru flags a common bonus term: winnings must be withdrawn as soon as wagering is met or they can be capped",
        "No confirmed welcome offer on record with us",
        "Trustpilot has suspended Spinjo's rating for a breach of its review guidelines"],
  verdict=("On the licence and ownership record, Spinjo is the most transparent casino here, though Trustpilot's "
           "suspension of its rating is a reason to read recent player feedback elsewhere before depositing. If a New Zealander asks us which offshore "
           "brand is easiest to check up on, this is it, with the caveat that it still sits outside New Zealand regulation.")),
 "madcasino": dict(
  tagline="Casino and sportsbook on one account, under a verified Curaçao licence, but with low withdrawal limits.",
  intro=("MadCasino runs a casino and a sportsbook from one account. Casino Guru lists a Curaçao Gaming Authority licence, "
         "OGL/2024/129/0131, under the new Curaçao regime, and a Safety Index of 6.7 with no complaints logged directly "
         "against it. It does not name an owner, and its published withdrawal limits are among the lowest here."),
  pros=["Casino and sports betting from one wallet and one verification",
        "Licence number published and verified under Curaçao's post-2023 regime",
        "NZD balance supported",
        "Wide choice of payment options (38 listed by Casino Guru)"],
  cons=["No owner named; one review links it to Softon Ltd, which we could not confirm",
        "Low limits: NZ$1,400 a day and NZ$4,500 a week",
        "Casino Guru notes it is connected to 38 other casinos, so problems at sister sites count against it"],
  verdict=("MadCasino suits someone who wants pokies and sport in one place and plays at modest stakes. The daily limit of "
           "NZ$1,400 means a big win would take weeks to withdraw.")),
 "gunsbet": dict(
  tagline="Sportsbook listing with a very large supplied welcome headline and a named owner.",
  intro=("Gunsbet is one of the longer-running names here, reported as launched in 2016. It is now run by Novatrix S.R.L., "
         "a Costa Rica company that also runs Rooster Bet, Fortune Play, Lucky Circus and Bet&Play, and it holds Anjouan and "
         "Tobique licences that Casino Guru marks as verified. We cover it as a betting site, as supplied by the publisher."),
  pros=["Named owner and two verified licences",
        "NZD balance and NZD limits of $3,000 a day and $7,500 a week",
        "Very large supplied welcome headline: 285% up to €7,500 plus 285 free spins",
        "Wide range of payment options (43 listed)"],
  cons=["Three complaints logged with Casino Guru",
        "Its Trustpilot profile has been removed",
        "No crypto cashier in the publisher's product sheet",
        "Wagering terms were not supplied with the offer"],
  verdict=("Gunsbet has a long history and a clear owner, which counts for a lot offshore. Read the full offer terms before "
           "you rely on the headline; a 285% package means little until you see the wagering attached.")),
 "lucky7even": dict(
  tagline="Joint-highest independent safety rating here, with NZD banking from the Hollycorn group.",
  intro=("Lucky7even shares its licences with Spinjo and Lucky Vibe (Tobique 0000064 and Anjouan ALSI-202509073-FI2), and "
         "review sites name the same owner, Hollycorn N.V. Casino Guru gives it a Safety Index of 8.9, level with Spinjo. "
         "It supports an NZD balance and publishes NZD withdrawal limits."),
  pros=["Joint-highest Safety Index on our list (8.9)",
        "Two licences verified by Casino Guru",
        "NZD balance and limits of $3,000 a day, $7,500 a week",
        "29 payment options listed, including Neosurf vouchers and crypto"],
  cons=["Owner named by review sites rather than by Casino Guru",
        "Same bonus term flag as its sister sites: withdraw promptly once wagering is met",
        "No confirmed welcome offer on record with us"],
  verdict=("Lucky7even is as well documented as Spinjo and the choice between them comes down to the lobby you prefer. On "
           "the facts we can check, both are near the top of this list.")),
 "lucky-vibe": dict(
  tagline="Hollycorn-owned casino and sportsbook with an NZD balance and a strong independent rating.",
  intro=("Lucky Vibe is owned by Hollycorn N.V. and holds the same pair of verified licences as Spinjo and Lucky7even. "
         "Casino Guru gives it a Safety Index of 8.5 and lists 22 payment options. It runs a sportsbook as well as a casino."),
  pros=["Named owner and two verified licences",
        "High independent Safety Index (8.5)",
        "Casino and sportsbook in one account",
        "NZD balance with limits of $3,000 a day and $7,500 a week"],
  cons=["Trustpilot score is poor (1.8 from 49 reviews), so read recent player reviews",
        "No confirmed welcome offer on record with us"],
  verdict=("Lucky Vibe is one of the better-documented casino and sportsbook combinations here. The weak Trustpilot score "
           "is worth reading before you sign up, because it reflects how players say disputes are handled.")),
 "rooster-bet": dict(
  tagline="Three licences and an owner named on its own website, with casino and sport in one place.",
  intro=("Rooster Bet's own About page names Novatrix SRL, a Costa Rica company, as owner. Casino Guru lists three verified "
         "licences: Tobique (0000002), Anjouan (ALSI-202508056-FI2) and the Estonian Tax and Customs Board (HKT000017). "
         "That third licence, from an EU authority, is unusual among the brands on this list. Safety Index: 8.5."),
  pros=["Owner named on the operator's own website",
        "Three verified licences, including an Estonian one",
        "High independent Safety Index (8.5)",
        "NZD balance; NZD limits of $3,000 a day and $7,500 a week"],
  cons=["Older reviews still name Dama N.V. as owner, so check the current footer",
        "No confirmed welcome offer on record with us"],
  verdict=("Rooster Bet has the deepest licensing on our list and an owner that says who it is. It is among the strongest "
           "casino and sportsbook combinations we cover on the public record.")),
 "fortune-play": dict(
  tagline="Novatrix-run casino and sportsbook with an 8.4 independent rating and NZD banking.",
  intro=("Fortune Play is run by Novatrix S.R.L. under the same verified Tobique and Anjouan licences as Rooster Bet. Casino "
         "Guru gives it a Safety Index of 8.4, lists 25 payment options and records NZD limits of $3,000 a day, $7,500 a "
         "week and $30,000 a month."),
  pros=["Named owner and two verified licences",
        "Safety Index of 8.4",
        "NZD balance and published NZD limits",
        "Casino and sportsbook on one account"],
  cons=["Casino Guru flags bonus-stacking rules: claiming too many bonuses can void winnings",
        "No confirmed welcome offer on record with us"],
  verdict=("Fortune Play is a well-documented member of the Novatrix group. If you want casino and sport together with NZD "
           "banking, it belongs on the shortlist.")),
 "lucky-circus": dict(
  tagline="Novatrix casino with NZD support, but a low weekly limit and a daily win cap.",
  intro=("Lucky Circus is another Novatrix S.R.L. brand with verified Anjouan and Tobique licences. Its Safety Index is "
         "6.8, lower than its sister sites, mainly because of its limits: €2,500 a week, €10,000 a month and a daily win cap "
         "of US$50,000 on net winnings."),
  pros=["Named owner and two verified licences",
        "NZD balance supported",
        "21 payment options, including Neosurf and CashtoCode vouchers"],
  cons=["Weekly withdrawal limit of €2,500 is among the lowest here",
        "Daily win cap: you cannot win more than US$50,000 net in a day",
        "One complaint logged with Casino Guru"],
  verdict=("Lucky Circus is fine for small, casual play. Its limits make it a poor fit for anyone who hopes to land and "
           "withdraw a large win.")),
 "kingdom": dict(
  tagline="Large reported crypto package, but the licence, owner and even the brand's history are unclear.",
  intro=("There is a naming problem with Kingdom. Casino Guru's Kingdom Casino profile, a Dama N.V. brand, is marked as closed. "
         "Several 2026 casino listings describe an active Kingdom Casino with a crypto-first cashier and a reported welcome "
         "package of 600% up to €9,500. They appear to be different businesses, and we could not confirm the licence or "
         "owner of the current one."),
  pros=["Reported large welcome package with cashback (unconfirmed)",
        "Casino and sportsbook with crypto payments"],
  cons=["Licence not confirmed",
        "Owner not confirmed",
        "Shares its name with a casino listed as closed, which makes complaint history hard to trace"],
  verdict=("We cannot tell New Zealand readers who runs Kingdom or who licenses it. Until that is clear, it sits near the "
           "bottom of our scores.")),
 "smash": dict(
  tagline="Anjouan-licensed casino and sportsbook with a low safety rating and euro-only limits.",
  intro=("Smash is owned by Softon Ltd and licensed in Anjouan (ALSI-202409012-FI1). Casino Guru gives it a Safety Index of "
         "3.9, one of the lowest here. It has no NZD balance, a weekly withdrawal limit of €2,000 and a daily win cap of "
         "€100,000."),
  pros=["Named owner and a verified Anjouan licence",
        "Casino, sportsbook and a crypto-heavy cashier, including Solana and USDC"],
  cons=["Low independent Safety Index (3.9)",
        "No NZD balance: euro limits of €1,000 a day and €2,000 a week",
        "Daily win cap of €100,000",
        "Public complaints about confiscated winnings"],
  verdict=("Smash scores poorly on the public record. The combination of a low safety rating, tight euro limits and "
           "complaints about withheld winnings is enough for us to advise caution.")),
 "trixino": dict(
  tagline="Unusually low 7x wagering on a 777% six-stage package, but licence and owner unconfirmed.",
  intro=("Trixino is a newer brand with casino and sportsbook products. Its welcome package, as supplied by the publisher, "
         "is 777% across six deposits up to €7,777 in total, with 7x wagering. That wagering is far lower than the "
         "offshore norm of 35x to 40x. What we could not find is an independent profile naming its operator or a licence "
         "number we could check."),
  pros=["Wagering of 7x is a fraction of the usual 35x to 40x",
        "Six-stage package spreads the bonus over several deposits",
        "Casino, sportsbook and crypto on one account"],
  cons=["Licence not confirmed",
        "Owner not confirmed",
        "No independent safety rating to compare",
        "Its Trustpilot profile has been removed"],
  verdict=("Trixino's offer terms are genuinely player-friendly on paper. Without a confirmed licence or owner, though, "
           "there is no way to judge what happens if a withdrawal is refused.")),
 "rivo": dict(
  tagline="Exceptiosoft-run casino and sportsbook with a 2026 Anjouan licence and euro-only limits.",
  intro=("Rivo is owned by Exceptiosoft Ltd and holds an Anjouan licence (ALSI-202606020-FI1) that, going by its number, "
         "was issued in June 2026. Casino Guru gives it a Safety Index of 6.2 and lists 34 payment options. There is no "
         "NZD balance, and limits are €1,000 a day with a daily win cap of €100,000."),
  pros=["Named owner and a verified licence",
        "Wide choice of 34 payment options, including Apple Pay and crypto",
        "Casino and sportsbook on one account"],
  cons=["No NZD balance",
        "Daily withdrawal limit of €1,000",
        "Daily win cap of €100,000",
        "Very new licence, so little track record",
        "Its Trustpilot profile has been removed"],
  verdict=("Rivo is a middle-of-the-table option. The licence is real and the owner is named, but the low daily limit and "
           "short history keep its score in the sixes.")),
 "betandplay": dict(
  tagline="Novatrix sportsbook listing with verified licences, NZD support and a daily win cap.",
  intro=("Bet&Play is run by Novatrix S.R.L. and holds the group's verified Anjouan and Tobique licences. We cover it as a "
         "betting site, as supplied by the publisher. Casino Guru gives it a Safety Index of 6.8, with no complaints logged "
         "directly against it, and records a daily win cap of US$50,000."),
  pros=["Named owner and two verified licences",
        "No complaints logged directly against it with Casino Guru",
        "NZD balance supported",
        "Crypto and e-wallets accepted"],
  cons=["Daily win cap of US$50,000",
        "Weekly withdrawal limit of €5,000",
        "Casino Guru counts 11 complaints against related sites"],
  verdict=("Bet&Play is a reasonable, well-documented sportsbook option within the Novatrix group, held back by its "
           "win cap and limits.")),
 "spino": dict(
  tagline="Crypto-first casino and sportsbook with an Anjouan licence and a clean complaint record.",
  intro=("Spino is a crypto-first brand licensed in Anjouan (ALSI-202506006-FI1). Casino Guru gives it a Safety Index of "
         "7.2 with no complaints logged. Its cashier lists crypto rather than New Zealand dollars, and it does not name an "
         "owner."),
  pros=["Safety Index of 7.2 with no complaints on record",
        "Verified Anjouan licence",
        "Wide crypto support, including Solana and XRP"],
  cons=["No NZD option: you need to buy crypto first",
        "Owner not published",
        "No withdrawal limits published in the sources we checked"],
  verdict=("Spino is a reasonable choice only for someone already comfortable holding and moving crypto. For everyone "
           "else, the exchange step adds cost and risk.")),
}
