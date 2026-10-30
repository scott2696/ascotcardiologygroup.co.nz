#!/usr/bin/env python3
"""Export every built page body to _pages/<slug>.md with front matter, so the
content can be pasted into any CMS. Called at the end of build.py."""
import os, re, html
from html.parser import HTMLParser
import lib

OUT = os.path.join(lib.ROOT, "_pages")


class MD(HTMLParser):
    SKIP = {"script", "style", "svg", "nav", "summary-skip"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.o, self.href, self.skip, self.lst, self.row, self.rows, self.cell = [], [], 0, [], None, None, None
        self.inpre = False

    def w(self, s):
        if self.cell is not None:
            self.cell.append(s)
        else:
            self.o.append(s)

    def handle_starttag(self, t, a):
        a = dict(a)
        if t in ("nav", "svg", "script", "style") or "tl-tc" in (a.get("class") or ""):
            self.skip += 1
        if self.skip:
            return
        if t in ("h1", "h2", "h3", "h4"):
            self.w("\n\n" + "#" * int(t[1]) + " ")
        elif t == "p":
            self.w("\n\n")
        elif t in ("ul", "ol"):
            self.lst.append([t, 0])
            self.w("\n")
        elif t == "li":
            if self.lst:
                self.lst[-1][1] += 1
                m = f"{self.lst[-1][1]}." if self.lst[-1][0] == "ol" else "-"
            else:
                m = "-"
            self.w("\n" + "  " * (len(self.lst) - 1) + m + " ")
        elif t in ("b", "strong"):
            self.w("**")
        elif t in ("em", "i") and not a.get("style"):
            self.w("*")
        elif t == "a":
            self.href.append(a.get("href", ""))
            self.w("[")
        elif t == "br":
            self.w("  \n")
        elif t == "table":
            self.rows = []
        elif t == "tr":
            self.row = []
        elif t in ("td", "th"):
            self.cell = []
        elif t == "img" and a.get("alt"):
            self.w(f"![{a['alt']}]({a.get('src','')})")
        elif t == "summary":
            self.w("\n\n")
        elif t == "div" and "tl-offer" in (a.get("class") or ""):
            self.w("\n")

    def handle_endtag(self, t):
        if t in ("nav", "svg", "script", "style"):
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            if t == "p":
                self.skip = max(0, self.skip - 1)
            return
        if t in ("b", "strong"):
            self.w("**")
        elif t in ("em", "i"):
            self.w("*")
        elif t == "a":
            h = self.href.pop() if self.href else ""
            if h.startswith("/"):
                h = lib.SITE + h
            self.w(f"]({h})")
        elif t in ("ul", "ol"):
            if self.lst:
                self.lst.pop()
            self.w("\n")
        elif t in ("td", "th"):
            if self.row is not None:
                self.row.append(re.sub(r"\s+", " ", "".join(self.cell or [])).strip().replace("|", "/"))
            self.cell = None
        elif t == "tr":
            if self.rows is not None and self.row is not None:
                self.rows.append(self.row)
            self.row = None
        elif t == "table":
            if self.rows:
                n = max(len(r) for r in self.rows)
                lines = ["| " + " | ".join(r + [""] * (n - len(r))) + " |" for r in self.rows]
                lines.insert(1, "|" + "---|" * n)
                self.o.append("\n\n" + "\n".join(lines) + "\n")
            self.rows = None
        elif t in ("h1", "h2", "h3", "h4"):
            self.w("\n")

    def handle_data(self, d):
        if self.skip:
            return
        d = re.sub(r"\s+", " ", d)
        self.w(d)


TL = re.compile(r'<ol class="tl"[^>]*>.*?</ol>', re.S)
ROW = re.compile(r'<li class="tl-row.*?</li></ul>.*?</li>', re.S)


def _tl_table(m):
    rows = []
    for r in ROW.findall(m.group(0)):
        name = re.search(r'class="tl-name"><a href="([^"]+)">(.*?)</a>', r)
        offer = re.search(r'class="tl-offer"><span>.*?</span>(.*?)</p>', r)
        score = re.search(r'class="tl-score"><b>(.*?)</b>', r)
        facts = re.findall(r'<li><span>(.*?)</span><b>(.*?)</b></li>', r)
        f = "; ".join(f"{k}: {v}" for k, v in facts)
        rows.append(f'<tr><td><a href="{name.group(1)}">{name.group(2)}</a></td><td>{offer.group(1).strip() if offer else "None on record"}</td>'
                    f'<td>{f}</td><td>{score.group(1) if score else ""}/10</td></tr>')
    return ('<table><tr><th>Site</th><th>Offer on record</th><th>Key facts</th><th>Ledger score</th></tr>'
            + "".join(rows) + '</table>')


def to_md(body):
    body = TL.sub(_tl_table, body)
    body = re.sub(r'<span class="av[^"]*"[^>]*>.*?</span>', "", body)
    body = re.sub(r'</(span|b|div|time)>', r'</\1> ', body)
    p = MD()
    p.feed(body)
    s = "".join(p.o)
    s = re.sub(r"\n[ \t]+", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    s = re.sub(r"\[\]\([^)]*\)", "", s)
    return s.strip() + "\n"


def run():
    os.makedirs(OUT, exist_ok=True)
    for f in os.listdir(OUT):
        if f.endswith(".md"):
            os.remove(os.path.join(OUT, f))
    rows = []
    for path, (author, body) in lib.SOURCES.items():
        if path in lib.META:
            t, d, h1 = lib.META[path]
        else:
            t, d, h1 = lib.PAGE_EXTRA[path]
        md = to_md(body)
        words = len(re.findall(r"[A-Za-z0-9$€%'’-]+", re.sub(r"\(https?://[^)]*\)", "", md)))
        name = "home" if path == "/" else path.strip("/").replace("/", "--")
        a = lib.AUTHORS[author]["name"] if author else ""
        fm = (f"---\nurl: {lib.SITE}{path}\ntitle: \"{html.unescape(lib.strip_tags(t))}\"\n"
              f"meta_description: \"{html.unescape(lib.strip_tags(d))}\"\nh1: \"{html.unescape(lib.strip_tags(h1))}\"\n"
              f"author: {a}\nwords: {words}\n---\n\n")
        open(os.path.join(OUT, name + ".md"), "w").write(fm + md)
        rows.append((words, path, name))
    rows.sort(reverse=True)
    json_rows = "\n".join(f"| {w:,} | `{p}` | `_pages/{n}.md` |" for w, p, n in rows)
    open(os.path.join(OUT, "_INDEX.md"), "w").write(
        f"# Page index\n\n{len(rows)} pages, {sum(r[0] for r in rows):,} words.\n\n| Words | URL | File |\n|---:|---|---|\n{json_rows}\n")
    print(f"  exported {len(rows)} pages, {sum(r[0] for r in rows):,} words")
