#!/usr/bin/env python3
"""Build everything: pages, sitemap.xml, robots.txt, web manifest and the
Markdown export in _pages/.   Run:  python3 _build/build.py"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib
from lib import ROOT, SITE, NAME, PAGES, save_lastmod

MODULES = ["p_home", "p_cat", "p_betting", "p_guides", "p_reviews", "p_site"]

# The seven crawlers named in the brief, each blocked site-wide.
BLOCKED = ["AhrefsBot", "SemrushBot", "MJ12bot", "DotBot", "Rogerbot", "serpstatbot", "SistrixBot"]


def _images(path):
    """Images worth listing for a page: the share card on the homepage, the
    operator logo on its review, writer photos on the authors page."""
    if path == "/":
        return ["/images/og.png"]
    if path == "/authors/":
        return [a["photo"] for a in lib.AUTHORS.values() if a.get("photo")]
    if path.startswith("/casino-reviews/") and path.count("/") == 3:
        op = lib.BY.get(path.split("/")[2])
        return [op["logo"]] if op else []
    return []


def sitemap():
    rows = []
    for path, date, pri, freq in sorted(PAGES, key=lambda p: (-p[2], p[0])):
        imgs = "".join(f"\n    <image:image><image:loc>{SITE}{u}</image:loc></image:image>" for u in _images(path))
        rows.append(f"  <url>\n    <loc>{SITE}{path}</loc>\n    <lastmod>{date}</lastmod>\n"
                    f"    <changefreq>{freq}</changefreq>\n    <priority>{pri:.1f}</priority>{imgs}\n  </url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(xml)
    return len(rows)


def robots():
    # The domain-wide robots.txt. The group games at the root stay out of search
    # (they are noindex too); only the NZ guide under BASE is crawlable.
    out = [f"# robots.txt for https://{lib.DOMAIN}", "", "User-agent: *", f"Allow: {lib.BASE}/", f"Disallow: {lib.BASE}/*?",
           "Disallow: /", "", f"Sitemap: {SITE}/sitemap.xml", ""]
    for ua in BLOCKED:
        out += [f"User-agent: {ua}", "Disallow: /", ""]
    open(os.path.join(lib.DOMAIN_ROOT, "robots.txt"), "w").write("\n".join(out))


def manifest():
    m = {"name": NAME, "short_name": lib.SHORT, "start_url": f"{lib.BASE}/", "display": "standalone",
         "background_color": "#F7F5EF", "theme_color": "#0F3B30", "lang": "en-NZ",
         "icons": [{"src": f"{lib.BASE}/favicon-{s}x{s}.png", "sizes": f"{s}x{s}", "type": "image/png"} for s in (48, 96, 144, 192, 512)]}
    json.dump(m, open(os.path.join(ROOT, "site.webmanifest"), "w"), indent=1)


def main():
    for name in MODULES:
        __import__(name).build()
        print(f"  ok {name}")
    n = sitemap(); robots(); manifest(); save_lastmod()
    import export; export.run()
    print(f"\n{n} pages written. sitemap.xml, robots.txt, site.webmanifest, _pages/*.md updated.")


if __name__ == "__main__":
    main()
