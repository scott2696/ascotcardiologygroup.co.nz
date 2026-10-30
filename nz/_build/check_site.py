#!/usr/bin/env python3
"""QA: every page parses, has one H1, a self-referencing canonical, valid
JSON-LD, unique title/description within length budgets, and every internal
link and image resolves. Nav and footer carry About and Contact; footer carries
every legal page."""
import os, re, json, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib

ROOT = lib.ROOT
err, warn = [], []
BANNED = {"rooster.bet", "spinjo.com", "luckyvibe.com", "fortuneplay.com", "luckycircus.com", "lucky7even.com",
          "gunsbet.com", "betandplay.com", "robycasino.com", "hellspin.com", "slotsgem.com", "ivibet.com",
          "smash.casino", "trixino.com", "madcasino.com", "rivo.casino", "kingdom.casino"}
ALLOWED = {lib.DOMAIN, "pokiesrealmoney.co.com", "dia.govt.nz", "legislation.govt.nz", "ird.govt.nz", "gamblinghelpline.co.nz", "pgf.nz", "tab.co.nz",
           "privacy.org.nz", "casino.guru", "health.govt.nz", "asianfamilyservices.nz", "fonts.googleapis.com",
           "fonts.gstatic.com", "anjouangaming.com", "tobiquegaming.ca", "gamingcommission.ca", "gaming-curacao.com",
           "cga.cw", "emta.ee", "consumer.org.nz", "depression.org.nz", "1737.org.nz", "beehive.govt.nz",
           "lotto.co.nz", "mygambling.co.nz", "chooseyourlimits.nz", "raptor.co.nz", "betcha.co.nz", "harmreduction.co.nz"}
pages = {}
for dp, ds, fs in os.walk(ROOT):
    ds[:] = [d for d in ds if not d.startswith((".", "_"))]
    for f in fs:
        if f == "index.html":
            rel = os.path.relpath(dp, ROOT)
            path = "/" if rel == "." else "/" + rel + "/"
            raw = open(os.path.join(dp, f), encoding="utf-8").read()
            # Every site-relative link must sit under BASE; then check them as site paths.
            for a in re.findall(r'\s(?:href|src|action)="(/[^"]*)"', raw):
                if not a.startswith(lib.BASE + "/"): err.append(f"{path}: link outside {lib.BASE}/: {a}")
            pages[path] = re.sub(r'(\s(?:href|src|action)=")' + lib.BASE + "/", r"\1/", raw)

titles, descs = {}, {}
TITLE_ROWS = []
for p, h in pages.items():
    h1 = re.findall(r"<h1[\s>]", h)
    if len(h1) != 1: err.append(f"{p}: {len(h1)} H1s")
    c = re.search(r'<link rel="canonical" href="([^"]+)"', h)
    if not c or c.group(1) != lib.SITE + p: err.append(f"{p}: canonical {c and c.group(1)}")
    t = html.unescape(re.search(r"<title>(.*?)</title>", h).group(1))
    d = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', h).group(1))
    titles.setdefault(t, []).append(p); descs.setdefault(d, []).append(p)
    # Pixel budget measured with the month forced to September, the widest, so a
    # title that passes now passes in every month of the year.
    tw = lib.px(re.sub(r"\[\w+ (\d{4})\]", r"[September \1]", t))
    if tw > 580: err.append(f"{p}: title {tw}px > 580px: {t}")
    if f"[{lib.MY}]" not in t: err.append(f"{p}: title missing [{lib.MY}]: {t}")
    h1t = re.sub(r"<[^>]+>", "", re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S).group(1))
    if f"[{lib.MY}]" not in html.unescape(h1t): err.append(f"{p}: H1 missing [{lib.MY}]")
    TITLE_ROWS.append((tw, p, t, html.unescape(h1t)))
    if not 110 <= len(d) <= 170: warn.append(f"{p}: description {len(d)} chars")
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try: json.loads(m)
        except Exception as e: err.append(f"{p}: bad JSON-LD {e}")
    for a in re.findall(r'href="(/[^"#?]*)', h):
        if a.endswith(".html"): err.append(f"{p}: .html link {a}")
        if a in ("/sitemap.xml", "/site.webmanifest", "/favicon.ico", "/favicon.svg") or a.startswith(("/assets/", "/images/", "/logos/", "/favicon", "/apple")):
            if not os.path.exists(os.path.join(ROOT, a.lstrip("/"))): err.append(f"{p}: missing file {a}")
            continue
        if a not in pages: err.append(f"{p}: broken link {a}")
    for a in re.findall(r'href="(/[^"?]*#[^"]+)"', h):
        u, frag = a.split("#", 1)
        tgt = pages.get(u or p, "")
        if tgt and f'id="{frag}"' not in tgt: err.append(f"{p}: missing anchor {a}")
    for s in re.findall(r'src="(/[^"]+)"', h):
        if not os.path.exists(os.path.join(ROOT, s.lstrip("/"))): err.append(f"{p}: missing img {s}")
    nav = re.search(r'<nav class="nav".*?</nav>', h, re.S).group(0)
    foot = re.search(r'<footer.*?</footer>', h, re.S).group(0)
    for u in ("/about/", "/contact/"):
        if f'href="{u}"' not in nav: err.append(f"{p}: {u} not in main nav")
    for u in ("/about/", "/contact/", "/terms/", "/authors/", "/privacy/", "/cookie-policy/", "/responsible-gambling/", "/sitemap.xml"):
        if f'href="{u}"' not in foot: err.append(f"{p}: {u} not in footer")
    # Editorial rule: no outbound link to any casino, bookmaker or affiliate network.
    for ext in ([] if lib.AFF_ON else re.findall(r'href="(https?://[^"]+)"', h)):
        host = re.sub(r"^https?://(www\.)?", "", ext).split("/")[0].lower()
        if host in BANNED or any(b in ext for b in ("afftrack", "partners", "roosters", "mediaroosters", "novarao", "myloric", "zaplypulse", "crownslotslink", "gunsbetlink")):
            err.append(f"{p}: outbound casino/affiliate link {ext}")
        elif host not in ALLOWED:
            warn.append(f"{p}: external link {ext}")
    if ".html\"" in h and "index.html" in h: warn.append(f"{p}: mentions index.html")
for t, ps in titles.items():
    if len(ps) > 1: err.append(f"duplicate title {t}: {ps}")
for d, ps in descs.items():
    if len(ps) > 1: err.append(f"duplicate description: {ps}")
sm = open(os.path.join(ROOT, "sitemap.xml")).read()
locs = set(re.findall(r"<loc>" + re.escape(lib.SITE) + r"(/[^<]*)</loc>", sm))
if locs != set(pages): err.append(f"sitemap mismatch: {sorted(set(pages) ^ locs)}")
rb = open(os.path.join(lib.DOMAIN_ROOT, "robots.txt")).read()
if f"Sitemap: {lib.SITE}/sitemap.xml" not in rb: err.append("robots missing sitemap")
for ua in ["AhrefsBot", "SemrushBot", "MJ12bot", "DotBot", "Rogerbot", "serpstatbot", "SistrixBot"]:
    if f"User-agent: {ua}\nDisallow: /" not in rb: err.append(f"robots missing {ua}")
from PIL import Image
for s in (48, 96, 144, 192):
    im = Image.open(os.path.join(ROOT, f"favicon-{s}x{s}.png"))
    if im.size != (s, s): err.append(f"favicon {s} wrong size {im.size}")
if "--titles" in sys.argv:
    for tw, p, t, h in sorted(TITLE_ROWS, key=lambda r: r[1]):
        print(f"{tw:4d}px  {p:38s} {t}\n        H1: {h}")
print(f"{len(pages)} pages checked · {len(err)} errors · {len(warn)} warnings")
for e in err: print("  ERR ", e)
for w in warn: print("  warn", w)
sys.exit(1 if err else 0)
