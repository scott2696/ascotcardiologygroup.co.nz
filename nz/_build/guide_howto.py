"""Step-by-step account, deposit and withdrawal guide shown under the ranked
list on every money page. Three variants (casino, crypto, sports) so the
pages do not repeat each other word for word; each page sets its own heading
and opening line for its keyword."""
from lib import steps, note, esc

OPEN = [
    ("Check the site before you sign up",
     "Find the licence number in the site's footer and look it up on the regulator's public register, then read our "
     "review for the owner, limits and complaint record. If the footer has no licence number, stop there."),
    ("Register with your real details",
     "Use your legal name, date of birth, home address and an email you check, exactly as they appear on your ID. You "
     "must be 18 or over. Wrong or made-up details are the most common reason a withdrawal is refused later."),
    ("Choose your currency carefully",
     "If NZD is offered, pick it at sign-up. Most sites will not let you change the account currency afterwards, and a "
     "non-NZD account means your bank converts every deposit and withdrawal."),
    ("Set your limits first",
     "Before you deposit, open the account or responsible gambling settings and set a deposit limit, a loss limit and a "
     "session reminder. Lowering a limit takes effect straight away; raising one usually has a cooling-off delay."),
    ("Verify your identity straight away",
     "Upload photo ID (passport or driver licence) and proof of address dated in the last three months, such as a bank "
     "statement or power bill. Doing it now means your first withdrawal is not held up waiting for checks."),
]

DEPOSIT = [
    ("Open the cashier",
     "Log in and choose Deposit or Cashier. Check the minimum deposit, usually around NZ$20 to NZ$30 or the euro "
     "equivalent, and whether the method you want carries a fee."),
    ("Pick a method you can also withdraw to",
     "Cards, e-wallets such as Skrill, bank transfer and crypto all work both ways. Prepaid vouchers such as Neosurf are "
     "deposit-only, so you would need a second method to get money out."),
    ("Decide on the bonus before you pay",
     "Tick or untick the bonus box, or leave the code field empty if you do not want it. Once a bonus is active, its "
     "wagering, maximum-bet and game rules apply to your balance until you clear or forfeit it."),
    ("Enter the amount and confirm",
     "Stay inside the limit you set. Your bank may ask you to approve a card payment in its app. If a New Zealand bank "
     "declines the payment, it may block offshore gambling transactions; do not try to get around a block you set yourself."),
    ("Check the balance and keep a record",
     "Card and e-wallet deposits usually show within a minute. Screenshot or note the transaction ID, the amount and the "
     "time, in case you need to raise a dispute."),
]

WITHDRAW = [
    ("Clear or cancel any bonus first",
     "Withdrawing while a bonus is active usually voids the bonus and anything won with it. Check your wagering progress "
     "in the account area, or forfeit the bonus if you would rather cash out what is yours."),
    ("Request the withdrawal",
     "Open the cashier, choose Withdraw and enter the amount. Most sites send money back by the method you deposited with, "
     "so expect to use the same card, e-wallet or wallet address."),
    ("Leave it pending",
     "Many sites hold withdrawals for 24 to 72 hours before processing them. Do not reverse the request to keep playing; "
     "turn off 'reverse withdrawal' if the site offers it."),
    ("Answer verification requests quickly",
     "For larger amounts the site may ask for a recent bank statement or proof of where the money came from. Reply from "
     "the email on your account and keep copies of everything you send."),
    ("Watch the limits",
     "Daily, weekly and monthly withdrawal limits mean a big win can be paid in instalments. The limit for each site is in "
     "its row above and in its review."),
    ("Track the payment to your account",
     "Once approved, e-wallet and crypto withdrawals usually arrive the same day; cards and bank transfers take one to "
     "five working days. If nothing arrives, contact support with the transaction ID, then the regulator named on the licence."),
]

CRYPTO_DEPOSIT = [
    ("Buy crypto on a New Zealand exchange",
     "Use an exchange registered on New Zealand's Financial Service Providers Register, verify your account and buy with "
     "NZD by bank transfer. USDT avoids price swings; Litecoin and Tron-network USDT keep network fees low."),
    ("Copy the casino's deposit address and network",
     "In the cashier, choose the coin and the network (for example USDT on TRC-20). Copy the address exactly. Sending on "
     "the wrong network usually loses the money for good."),
    ("Send a small test amount first",
     "Send a few dollars' worth and wait for it to arrive before sending the rest. Check the casino's minimum, as amounts "
     "below it may not be credited."),
    ("Wait for confirmations",
     "The deposit shows once the network confirms it: minutes for most coins, longer for Bitcoin when the network is busy."),
    ("Record the price and the transaction hash",
     "Note the NZD value on the day and the transaction hash. Inland Revenue can tax gains on crypto you hold, so you need "
     "these records whether or not you win."),
]

CRYPTO_WITHDRAW = [
    ("Clear or cancel any bonus first",
     "An active bonus usually has to be wagered or forfeited before crypto can be withdrawn."),
    ("Paste your own wallet address and pick the same network",
     "Use a wallet or exchange address in your name. Double-check the network matches; a mismatch can lose the funds."),
    ("Wait for approval and confirmations",
     "Crypto withdrawals are often approved within hours, then arrive once the network confirms them."),
    ("Convert to NZD and withdraw to your bank",
     "Sell on your New Zealand exchange and withdraw to your bank account. Keep the records for Inland Revenue."),
]

SPORTS_DEPOSIT = DEPOSIT[:2] + [
    ("Check the free bet or bonus terms",
     "Sports bonuses usually need the bonus to be rolled over several times at minimum odds, such as 1.80. Decide whether "
     "you want it before you deposit, and untick it if not."),
] + DEPOSIT[3:]

SPORTS_WITHDRAW = [
    ("Wait for open bets to settle",
     "Funds in unsettled bets cannot be withdrawn. Check the bet history and any rollover still needed on a bonus."),
] + WITHDRAW[1:]

PAGES = {
    "/": ("How to open an account, deposit and withdraw at an online casino", "casino",
          "The same steps apply at every casino on this list. Doing them in this order avoids the problems readers report most often: refused withdrawals and long verification holds."),
    "/online-pokies/": ("How to start playing pokies for real money, step by step", "casino",
          "Open an account, fund it and cash out in the right order, so your first pokies win is not stuck behind verification."),
    "/new-online-casinos/": ("How to sign up at a new casino safely", "casino",
          "A new brand has no track record, so the checks in the first steps matter more here than anywhere."),
    "/high-payout-casinos/": ("How to sign up, deposit and cash out a big win", "casino",
          "Large withdrawals are where limits and source-of-funds checks bite. Set up the account so a big win can be paid."),
    "/fast-payout-casinos/": ("How to get your withdrawal paid quickly, step by step", "casino",
          "Most slow withdrawals are caused by unfinished verification or an active bonus, not by the payment method. These steps remove both."),
    "/best-crypto-casinos/": ("How to open an account and deposit or withdraw with crypto", "crypto",
          "Crypto is fast, but mistakes with addresses and networks cannot be reversed. Follow these steps in order."),
    "/live-casinos/": ("How to sign up and fund a live casino account", "casino",
          "Live tables often have higher minimum bets than pokies, so set your limits before your first deposit."),
    "/online-casinos/bonuses/": ("How to sign up, claim a bonus and withdraw", "casino",
          "The bonus decision happens at the deposit step. Make it deliberately, then follow the withdrawal steps once wagering is done."),
    "/no-deposit-casinos/": ("How to register, claim free spins and withdraw winnings", "casino",
          "Even with no deposit, you will need a verified account and usually a deposit method before free spin winnings can be withdrawn."),
    "/online-betting/": ("How to open a betting account, deposit and withdraw", "sports",
          "The steps are the same at any bookmaker. In New Zealand, only TAB NZ and Betcha may lawfully take your bets."),
    "/best-sports-betting-sites/": ("How to join a betting site, deposit and withdraw", "sports",
          "Set up the account properly once and every later withdrawal is quicker. In New Zealand, only TAB NZ and Betcha may lawfully take your bets."),
    "/casino-reviews/": ("How to open an account, deposit and withdraw at any site we review", "casino",
          "Use each review for the licence, limits and payment methods, then follow these steps."),
}


def account_guide(path):
    h2, kind, lead = PAGES[path]
    dep, wd = {"casino": (DEPOSIT, WITHDRAW), "crypto": (CRYPTO_DEPOSIT, CRYPTO_WITHDRAW),
               "sports": (SPORTS_DEPOSIT, SPORTS_WITHDRAW)}[kind]
    acct = "betting account" if kind == "sports" else "account"
    return ('<div class="prose how" id="how-to">'
            f'<h2>{esc(h2)}</h2><p class="intro">{lead}</p>'
            f'<h3 id="open-account">Step 1: open your {acct}</h3>' + steps(OPEN, "h4")
            + f'<h3 id="deposit">Step 2: make a deposit</h3>' + steps(dep, "h4")
            + f'<h3 id="withdraw">Step 3: make a withdrawal</h3>' + steps(wd, "h4")
            + note("<p>The offshore sites on this page are expected to stop serving New Zealand from 1 December 2026. If you "
                   "hold a balance at one, complete verification and withdraw it now.</p>", "warn", "Withdraw before 1 December")
            + "</div>")
