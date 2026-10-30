#!/usr/bin/env python3
"""Source of truth for the 15 operators, in the order supplied by the publisher.

Run this file to regenerate _build/operators.json.

Editorial rules for this dataset
--------------------------------
* No affiliate links are stored or published. Reviews link only to pages on
  this site. (The New Zealand Online Casino Gambling Act 2026 bans advertising
  unlicensed online casino gambling to people in New Zealand; see README.)
* Every licence, owner, limit and payment fact below was read on 8 October 2026
  from the source named in `sources`. Where sources disagree, the copy says so.
* Welcome offers appear only where the publisher supplied them (CrownSlots,
  Gunsbet, Trixino) or where a 2026 source reported one (Kingdom, marked as
  reported). Nothing is invented. Offers change; re-check before publishing.
* `safety` is the Casino Guru Safety Index (0-10) as published on 8 Oct 2026.
  It is an independent third-party score and is attributed wherever shown.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

HERE = os.path.dirname(os.path.abspath(__file__))
CHECKED = "8 October 2026"

CG = "https://casino.guru/"

OPS = [
 dict(slug="crownslots", name="CrownSlots", logo="/logos/crownslots.png",
      casino=True, sports=False, crypto=True,
      owner="Not consistently published", owner_note=(
          "Review sites disagree on who runs CrownSlots: AboutSlots names Hollycorn N.V. in one place and Dama N.V. in "
          "another. We could not confirm the operating company from an independent register."),
      licences=[("Curaçao Gaming Control Board (reported)", "number not published in the sources we checked")],
      licence_short="Curaçao (reported)", licence_year=None, launched="2024 (reported)",
      safety=None, complaints=None, nzd=None,
      limits=[], win_cap=None,
      payments=["Visa", "Mastercard", "Siru Mobile", "Bitcoin", "other crypto"],
      n_pay=None,
      offer="390% up to €3,700 + 175 free spins across the first deposits",
      offer_detail=("The publisher-supplied headline is 390% up to €3,700 plus 175 free spins. AboutSlots describes the "
                    "package as four deposit-matched stages, each needing a deposit of at least €20 and each carrying 40x "
                    "wagering, with free spins valid for seven days. A separate high-roller option matches a first deposit "
                    "of €500 or more at 100% up to €5,000, also at 40x within seven days. Thursday promotions include "
                    "cashback of up to 20% and a 50% reload up to €500."),
      wagering="40x (reported)",
      sources=[("AboutSlots CrownSlots review", "https://www.aboutslots.com/reviews/crownslots-casino")],
      flags=["Owner not confirmed", "Licence number not published"],
      ),

 dict(slug="spinjo", name="Spinjo", logo="/logos/spinjo.png",
      casino=True, sports=False, crypto=True,
      owner="Hollycorn N.V.", owner_note="Casino Guru lists Hollycorn N.V. as the owner, the same group behind Lucky Vibe and Lucky7even.",
      licences=[("Anjouan Gaming (Comoros)", "ALSI-202509073-FI2"), ("Tobique Gaming Commission (New Brunswick)", "0000064")],
      licence_short="Anjouan + Tobique", licence_year=2025, launched="2024 (reported)",
      safety=8.9, complaints=None, nzd=True,
      limits=["NZ$3,000 a day", "NZ$7,500 a week", "NZ$30,000 a month"], win_cap=None,
      payments=["Visa", "Mastercard", "Skrill", "Neteller", "Paysafecard", "Neosurf", "MiFinity", "Revolut", "bank transfer", "Bitcoin", "Ethereum", "USDT"],
      n_pay=26, offer='up to NZ$5,000 + 300 free spins over four deposits (reported)', offer_detail='Reported by Gambling.com NZ in 2026: a four-part welcome package worth up to NZ$5,000 and 300 free spins, starting with 100% up to NZ$1,000 plus 100 free spins on the first deposit. Wagering was not confirmed for New Zealand; a Canadian review reports 29x on the bonus. Check the cashier terms before depositing.', wagering=None,
      sources=[("Casino Guru Spinjo review", CG + "spinjo-casino-review"), ('Gambling.com NZ Spinjo review', 'https://www.gambling.com/nz/online-casinos/reviews/spinjo')], flags=[]),

 dict(slug="madcasino", name="MadCasino", logo="/logos/madcasino.png",
      casino=True, sports=True, crypto=True,
      owner="Not published", owner_note=(
          "Casino Guru does not name an owner. CasinoCanada attributes the brand to Softon Ltd, the company Casino Guru "
          "lists behind Smash; we could not confirm the link."),
      licences=[("Curaçao Gaming Authority", "OGL/2024/129/0131")],
      licence_short="Curaçao (CGA)", licence_year=2024, launched=None,
      safety=6.7, complaints=0, nzd=True,
      limits=["NZ$1,400 a day", "NZ$4,500 a week", "NZ$18,000 a month"], win_cap=None,
      payments=["Visa", "Mastercard", "Apple Pay", "Google Pay", "Skrill", "Neteller", "Paysafecard", "Jeton", "MiFinity", "Revolut", "bank transfer", "Bitcoin", "Ethereum", "USDT", "Solana"],
      n_pay=38, offer=None, offer_detail=None, wagering=None,
      sources=[("Casino Guru MadCasino review", CG + "madcasino-review"), ("CasinoCanada MadCasino review", "https://casinocanada.com/casinos/madcasino/")],
      flags=["Owner not published", "Lower withdrawal limits than most"]),

 dict(slug="gunsbet", name="Gunsbet", logo="/logos/gunsbet.png", logo_dark=True,
      casino=False, sports=True, crypto=False,
      owner="Novatrix S.R.L.", owner_note="Casino Guru lists Novatrix S.R.L. (Costa Rica), which also runs Rooster Bet, Fortune Play, Lucky Circus and Bet&Play.",
      licences=[("Anjouan Gaming (Comoros)", "ALSI-202508056-FI2"), ("Tobique Gaming Commission (New Brunswick)", "0000002")],
      licence_short="Anjouan + Tobique", licence_year=2025, launched="2016 (reported)",
      safety=6.8, complaints=3, nzd=True,
      limits=["NZ$3,000 a day", "NZ$7,500 a week", "NZ$30,000 a month"], win_cap=None,
      payments=["Visa", "Mastercard", "Skrill", "Neteller", "Paysafecard", "Neosurf", "AstroPay", "MiFinity", "bank transfer"],
      n_pay=43,
      offer="285% up to €7,500 + 285 free spins",
      offer_detail=("The publisher supplied the same headline for both products: 285% up to €7,500 plus 285 free spins. "
                    "Wagering and stage-by-stage caps were not supplied, so read the offer page before you deposit."),
      wagering=None,
      sources=[("Casino Guru Gunsbet review", CG + "gunsbet-casino-review")],
      flags=["3 complaints logged with Casino Guru"]),

 dict(slug="lucky7even", name="Lucky7even", logo="/logos/lucky7even.jpg",
      casino=True, sports=False, crypto=True,
      owner="Hollycorn N.V. (reported)", owner_note="Legit.casino and CasinoBee name Hollycorn N.V.; the licence numbers match Spinjo and Lucky Vibe.",
      licences=[("Tobique Gaming Commission (New Brunswick)", "0000064"), ("Anjouan Gaming (Comoros)", "ALSI-202509073-FI2")],
      licence_short="Tobique + Anjouan", licence_year=2025, launched="2022 (reported)",
      safety=8.9, complaints=None, nzd=True,
      limits=["NZ$3,000 a day", "NZ$7,500 a week", "NZ$30,000 a month"], win_cap=None,
      payments=["Visa", "Mastercard", "Skrill", "Neteller", "Paysafecard", "Neosurf", "AstroPay", "Flexepin", "Jeton", "bank transfer", "Bitcoin", "Ethereum", "USDT"],
      n_pay=29, offer=None, offer_detail=None, wagering=None,
      sources=[("Casino Guru Lucky7even review", CG + "lucky7even-casino-review"), ("Legit.casino Lucky7even review", "https://legit.casino/reviews/lucky7even-casino/")],
      flags=[]),

 dict(slug="lucky-vibe", name="Lucky Vibe", logo="/logos/lucky-vibe.jpg",
      casino=True, sports=True, crypto=True,
      owner="Hollycorn N.V.", owner_note="Casino Guru lists Hollycorn N.V. as the owner.",
      licences=[("Tobique Gaming Commission (New Brunswick)", "0000064"), ("Anjouan Gaming (Comoros)", "ALSI-202509073-FI2")],
      licence_short="Tobique + Anjouan", licence_year=2025, launched="2024 (reported)",
      safety=8.5, complaints=None, nzd=True,
      limits=["NZ$3,000 a day", "NZ$7,500 a week", "NZ$30,000 a month"], win_cap=None,
      payments=["Visa", "Mastercard", "Skrill", "Neteller", "Paysafecard", "Neosurf", "MiFinity", "Jeton", "Revolut", "bank transfer", "Bitcoin", "Ethereum", "USDT"],
      n_pay=22, offer='up to $5,000 + 300 free spins (reported)', offer_detail="Reported by several 2026 casino listings: up to $5,000 plus 300 free spins, with 100% up to $1,000 plus 100 free spins on the first deposit. We could not find the operator's own terms or a confirmed wagering requirement, so treat the figure as unconfirmed.", wagering=None,
      sources=[("Casino Guru LuckyVibe review", CG + "luckyvibe-casino-review"), ('Muddy River News 2026 casino listing', 'https://muddyrivernews.com/tag/lucky-vibe/')], flags=[]),

 dict(slug="rooster-bet", name="Rooster Bet", logo="/logos/rooster-bet.png",
      casino=True, sports=True, crypto=True,
      owner="Novatrix S.R.L.", owner_note="Rooster.bet's own About page names Novatrix SRL, a Costa Rica company (registration 3-102-893958).",
      licences=[("Tobique Gaming Commission (New Brunswick)", "0000002"), ("Anjouan Gaming (Comoros)", "ALSI-202508056-FI2"), ("Estonian Tax and Customs Board", "HKT000017")],
      licence_short="Tobique + Anjouan + Estonia", licence_year=2025, launched="2023 (reported)",
      safety=8.5, complaints=None, nzd=True,
      limits=["NZ$3,000 a day", "NZ$7,500 a week", "NZ$30,000 a month"], win_cap=None,
      payments=["Visa", "Mastercard", "Skrill", "Neteller", "Neosurf", "MiFinity", "bank transfer", "Bitcoin", "Ethereum", "USDT"],
      n_pay=None, offer='up to $5,000 + 300 free spins over four deposits (reported)', offer_detail='Reported by Casinos.com NZ and Casino.org in 2026: a package across the first four deposits, each with its own match and free spins, totalling up to $5,000 and 300 free spins. One listing reports 40x wagering and a $30 minimum deposit; we could not confirm these.', wagering='40x (reported)',
      sources=[("Rooster.bet About us", "https://www.rooster.bet/about-us"), ("Casino Guru Rooster Bet review", CG + "rooster-bet-casino-review"), ('Casinos.com NZ Rooster Bet review', 'https://www.casinos.com/nz/rooster-bet-casino')],
      flags=[]),

 dict(slug="fortune-play", name="Fortune Play", logo="/logos/fortune-play.png",
      casino=True, sports=True, crypto=True,
      owner="Novatrix S.R.L.", owner_note="Casino Guru lists Novatrix S.R.L.; earlier reviews name Dama N.V., the previous operator of this group of brands.",
      licences=[("Tobique Gaming Commission (New Brunswick)", "0000002"), ("Anjouan Gaming (Comoros)", "ALSI-202508056-FI2")],
      licence_short="Tobique + Anjouan", licence_year=2025, launched="2024 (reported)",
      safety=8.4, complaints=None, nzd=True,
      limits=["NZ$3,000 a day", "NZ$7,500 a week", "NZ$30,000 a month"], win_cap=None,
      payments=["Visa", "Mastercard", "Skrill", "Neteller", "Paysafecard", "Neosurf", "MiFinity", "Revolut", "MuchBetter", "bank transfer", "Bitcoin", "Ethereum", "USDT"],
      n_pay=25, offer='up to $5,000 + 300 free spins over four deposits (reported)', offer_detail='Reported by Casino.org and other 2026 reviews: up to $5,000 plus 300 free spins spread across the first four deposits, followed by weekly reloads. Wagering was not confirmed.', wagering=None,
      sources=[("Casino Guru Fortune Play review", CG + "fortune-play-casino-review"), ('Gamerules FortunePlay review', 'https://gamerules.com/online-casinos/fortuneplay-casino/')], flags=[]),

 dict(slug="lucky-circus", name="Lucky Circus", logo="/logos/lucky-circus.jpg",
      casino=True, sports=False, crypto=True,
      owner="Novatrix S.R.L.", owner_note="Casino Guru lists Novatrix S.R.L.",
      licences=[("Anjouan Gaming (Comoros)", "ALSI-202508056-FI2"), ("Tobique Gaming Commission (New Brunswick)", "0000002")],
      licence_short="Anjouan + Tobique", licence_year=2025, launched="2024 (reported)",
      safety=6.8, complaints=1, nzd=True,
      limits=["€2,500 a week", "€10,000 a month"], win_cap="US$50,000 a day (net win)",
      payments=["Visa", "Mastercard", "Skrill", "Neteller", "Neosurf", "MiFinity", "MuchBetter", "CashtoCode", "bank transfer", "Bitcoin", "Ethereum", "USDT"],
      n_pay=21, offer='100% up to NZ$10,000 + 450 free spins over four deposits (reported)', offer_detail='Reported by Casino.org NZ and Gambling.com NZ in 2026: up to NZ$10,000 plus 450 free spins across the first four deposits, with 40x wagering and a NZ$30 minimum deposit.', wagering='40x (reported)',
      sources=[("Casino Guru Lucky Circus review", CG + "lucky-circus-casino-review"), ('Casino.org NZ LuckyCircus review', 'https://www.casino.org/new-zealand/reviews/luckycircus/')],
      flags=["Daily win cap", "Low weekly withdrawal limit"]),

 dict(slug="kingdom", name="Kingdom", logo="/logos/kingdom.png",
      casino=True, sports=True, crypto=True,
      owner="Not confirmed", owner_note=(
          "Casino Guru lists a Dama N.V. brand called Kingdom Casino as closed. 2026 reviews describe an active Kingdom "
          "Casino with a crypto-first cashier, which appears to be a separate brand. We could not confirm which company runs it."),
      licences=[("Not confirmed", "check the site footer before depositing")],
      licence_short="Not confirmed", licence_year=None, launched=None,
      safety=None, complaints=None, nzd=None, limits=[], win_cap=None,
      payments=["Visa", "Mastercard", "Bitcoin", "other crypto"], n_pay=None,
      offer="600% up to €9,500 + 20% cashback (reported)",
      offer_detail=("We did not receive a confirmed offer for Kingdom. Several 2026 listings report a welcome package of 600% "
                    "up to €9,500 with 20% cashback. Treat this as unconfirmed until you see it on the site itself."),
      wagering=None,
      sources=[("Casino Guru Kingdom Casino (closed listing)", CG + "kingdom-casino-review"), ("UK Bitcoin Casino listing", "https://www.ukbitcoincasino.co.uk/casinos")],
      flags=["Licence not confirmed", "Name shared with a closed casino"]),

 dict(slug="smash", name="Smash", logo="/logos/smash.png",
      casino=True, sports=True, crypto=True,
      owner="Softon Ltd", owner_note="Casino Guru lists Softon Ltd as the owner.",
      licences=[("Anjouan Gaming (Comoros)", "ALSI-202409012-FI1")],
      licence_short="Anjouan", licence_year=2024, launched="2024 (reported)",
      safety=3.9, complaints=None, nzd=False,
      limits=["€1,000 a day", "€2,000 a week"], win_cap="€100,000 a day",
      payments=["Visa", "Mastercard", "American Express", "Apple Pay", "Bitcoin", "Ethereum", "Litecoin", "USDT", "USDC", "Solana"],
      n_pay=21, offer=None, offer_detail=None, wagering=None,
      sources=[("Casino Guru Smash review", CG + "smash-casino-review")],
      flags=["Low Safety Index (3.9)", "No NZD balance", "€2,000 weekly withdrawal limit"]),

 dict(slug="trixino", name="Trixino", logo="/logos/trixino.png",
      casino=True, sports=True, crypto=True,
      owner="Not confirmed", owner_note="We found no independent profile naming Trixino's operator. Listings describe it as offshore-licensed without a verifiable number.",
      licences=[("Not confirmed", "listings variously cite Curaçao or Anjouan")],
      licence_short="Not confirmed", licence_year=None, launched="2026 (reported)",
      safety=None, complaints=None, nzd=None, limits=[], win_cap=None,
      payments=["Cards", "crypto"], n_pay=None,
      offer="777% across six deposits, up to €7,777 in total, at 7x wagering",
      offer_detail=("Supplied by the publisher. The package is split over six deposits: 200% up to €500, 100% up to €2,000, "
                    "177% up to €1,777, 50% up to €1,500, 150% up to €1,000 and 100% up to €1,000. That adds up to 777% and "
                    "€7,777. The 7x wagering is far below the 35x to 40x that is normal offshore, which is the part worth "
                    "checking in the full terms (what counts towards it, the maximum bet and any cap on winnings)."),
      wagering="7x",
      sources=[("Publisher-supplied offer", ""), ("Casino listings citing 777% up to €7,777", "https://e-playonline.com/crypto-casinos-8134/")],
      flags=["Licence not confirmed", "Owner not confirmed"]),

 dict(slug="rivo", name="Rivo", logo="/logos/rivo.png",
      casino=True, sports=True, crypto=True,
      owner="Exceptiosoft Ltd", owner_note="Casino Guru lists Exceptiosoft Ltd as the owner.",
      licences=[("Anjouan Gaming (Comoros)", "ALSI-202606020-FI1")],
      licence_short="Anjouan", licence_year=2026, launched=None,
      safety=6.2, complaints=None, nzd=False,
      limits=["€1,000 a day", "€10,000 a month"], win_cap="€100,000 a day",
      payments=["Visa", "Mastercard", "American Express", "Apple Pay", "Skrill", "Neteller", "bank transfer", "Bitcoin", "Litecoin", "USDT", "USDC"],
      n_pay=34, offer=None, offer_detail=None, wagering=None,
      sources=[("Casino Guru Rivo review", CG + "rivo-casino-review")],
      flags=["No NZD balance", "Daily win cap"]),

 dict(slug="betandplay", name="Bet&Play", logo="/logos/betandplay.png",
      casino=False, sports=True, crypto=True,
      owner="Novatrix S.R.L.", owner_note="Casino Guru lists Novatrix S.R.L.",
      licences=[("Anjouan Gaming (Comoros)", "ALSI-202508056-FI2"), ("Tobique Gaming Commission (New Brunswick)", "0000002")],
      licence_short="Anjouan + Tobique", licence_year=2025, launched="2022 (reported)",
      safety=6.8, complaints=0, nzd=True,
      limits=["€5,000 a week", "€20,000 a month"], win_cap="US$50,000 a day (net win)",
      payments=["Visa", "Mastercard", "Skrill", "Neteller", "Paysafecard", "MiFinity", "MuchBetter", "Revolut", "bank transfer", "Bitcoin", "Ethereum", "USDT"],
      n_pay=19, offer=None, offer_detail=None, wagering=None,
      sources=[("Casino Guru Bet&Play review", CG + "betandplay-casino-review")],
      flags=["Daily win cap"]),


 dict(slug="spino", name="Spino", logo="/logos/spino.jpg",
      casino=True, sports=True, crypto=True,
      owner="Not published", owner_note="Casino Guru does not name an owner.",
      licences=[("Anjouan Gaming (Comoros)", "ALSI-202506006-FI1")],
      licence_short="Anjouan", licence_year=2025, launched="2025 (reported)",
      safety=7.2, complaints=0, nzd=False,
      limits=[], win_cap=None,
      payments=["Bitcoin", "Ethereum", "Litecoin", "USDT", "Solana", "Dogecoin", "XRP"],
      n_pay=None, offer=None, offer_detail=None, wagering=None,
      sources=[("Casino Guru Casino Spino review", CG + "casino-spino-review")],
      flags=["Crypto-first cashier", "Owner not published"]),




]

# ---------------------------------------------------------------------------
# Trustpilot, read 8 October 2026 at trustpilot.com/review/<domain>.
# (score, number of reviews, note). None = no profile found for the brand.
# ---------------------------------------------------------------------------
TRUSTPILOT = {
    "crownslots": (3.6, 7, "crown-slots.net; very few reviews"),
    "spinjo": (None, 56, "Rating unavailable: Trustpilot says the company breached its guidelines"),
    "madcasino": (None, None, "No profile found"),
    "gunsbet": (None, None, "Profile removed by Trustpilot"),
    "lucky7even": (2.4, 137, ""),
    "lucky-vibe": (1.8, 49, ""),
    "rooster-bet": (2.0, 205, ""),
    "fortune-play": (3.4, 161, ""),
    "lucky-circus": (2.4, 38, ""),
    "kingdom": (None, None, "No profile found"),
    "smash": (3.3, 242, ""),
    "trixino": (None, None, "Profile removed by Trustpilot"),
    "rivo": (None, None, "Profile removed by Trustpilot"),
    "betandplay": (1.9, 112, ""),
    "spino": (None, None, "No profile found"),
}

# ---------------------------------------------------------------------------
# The Ledger score. Five inputs, all taken from public information, so anyone
# can reproduce the number. Weights are published on /how-we-review/.
# ---------------------------------------------------------------------------
WEIGHTS = {"safety": 0.40, "licence": 0.20, "owner": 0.15, "terms": 0.15, "banking": 0.10}


def _licence_pts(o):
    s = o["licence_short"]
    if s.startswith(("Not", "None")):
        return 2.0
    pts = {"Kahnawake": 7.0, "Curaçao (CGA)": 6.0, "Anjouan": 5.0}.get(s)
    if pts is None:
        pts = 6.5 if ("+" in s) else 5.5
    if "Estonia" in s:
        pts = 7.0
    return pts


def _owner_pts(o):
    w = o["owner"]
    if w.startswith("Not"):
        return 3.0
    if "reported" in w:
        return 6.0
    return 8.0


def _terms_pts(o):
    p = 8.0
    if o.get("win_cap"):
        p -= 2.0
    if any("below the stated" in f for f in o["flags"]):
        p -= 3.0
    lims = " ".join(o["limits"])
    if "€2,000 a week" in lims or "€2,500 a week" in lims:
        p -= 1.5
    if not o["limits"]:
        p -= 1.0
    return max(p, 1.0)


def _banking_pts(o):
    p = 5.0
    if o.get("nzd"):
        p += 2.5
    n = o.get("n_pay") or 0
    p += 1.5 if n >= 25 else (1.0 if n >= 19 else 0)
    if o.get("crypto"):
        p += 1.0
    return min(p, 10.0)


def score(o):
    parts = {
        "safety": o["safety"] if o["safety"] is not None else 4.0,
        "licence": _licence_pts(o), "owner": _owner_pts(o),
        "terms": _terms_pts(o), "banking": _banking_pts(o)}
    total = sum(parts[k] * w for k, w in WEIGHTS.items())
    return round(total, 1), {k: round(v, 1) for k, v in parts.items()}


def main():
    from copy_ops import COPY
    out = []
    for i, o in enumerate(OPS, 1):
        o = dict(o)
        o.update(COPY[o["slug"]])
        o["order"] = i
        o["rating"], o["parts"] = score(o)
        o.setdefault("logo_dark", False)
        o["checked"] = CHECKED
        o["tp_score"], o["tp_reviews"], o["tp_note"] = TRUSTPILOT[o["slug"]]
        out.append(o)
    json.dump(out, open(os.path.join(HERE, "operators.json"), "w"), indent=1, ensure_ascii=False)
    for o in out:
        print(f'{o["order"]:2d} {o["name"]:18s} {o["rating"]:4.1f}  {o["parts"]}')


if __name__ == "__main__":
    main()
