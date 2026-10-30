#!/usr/bin/env python3
"""Favicons at 48/96/144/192/512 px (all multiples of 48) plus 16/32 for old
browsers, favicon.ico, favicon.svg, apple-touch-icon, the Open Graph card, and
web-sized copies of the operator logos. The mark matches BRAND_MARK in lib.py."""
import os, glob
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FOREST, KOWHAI, MINT, PAPER, INK = (15, 59, 48), (242, 193, 78), (127, 214, 181), (247, 245, 239), (24, 34, 31)


def mark(size):
    s = size * 8; u = s / 48
    im = Image.new("RGBA", (s, s), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([u, u, 47*u, 47*u], radius=11*u, fill=FOREST)
    for y, w, a in ((12, 26, 255), (22, 18, 191), (32, 11, 128)):
        d.rounded_rectangle([11*u, y*u, (11+w)*u, (y+4)*u], radius=2*u, fill=KOWHAI + (a,))
    d.line([(27*u, 33.5*u), (31*u, 37.5*u), (38.5*u, 28.5*u)], fill=MINT, width=int(3.4*u), joint="curve")
    return im.resize((size, size), Image.LANCZOS)


def font(sz, bold=True):
    for p in ([ "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"] if bold else []) + ["/System/Library/Fonts/Supplemental/Arial.ttf"]:
        if os.path.exists(p):
            return ImageFont.truetype(p, sz)
    return ImageFont.load_default()


def logos():
    """Trim flat background borders from the master logos, then downsize for the
    web (max 360 x 160). Run on fresh copies from MY_SITES/logos."""
    from PIL import ImageChops
    for f in glob.glob(os.path.join(ROOT, "logos", "*")):
        im = Image.open(f); fmt = im.format
        rgb = im.convert("RGBA")
        bg = Image.new("RGBA", rgb.size, rgb.getpixel((0, 0)))
        diff = ImageChops.difference(rgb, bg).convert("L").point(lambda v: 255 if v > 24 else 0)
        box = diff.getbbox()
        if box:
            pad = max(4, round(min(rgb.size) * 0.03))
            box = (max(box[0] - pad, 0), max(box[1] - pad, 0), min(box[2] + pad, rgb.width), min(box[3] + pad, rgb.height))
            im = im.crop(box)
        im.thumbnail((360, 160), Image.LANCZOS)
        if fmt == "JPEG":
            im.convert("RGB").save(f, quality=88, optimize=True)
        else:
            im.save(f, optimize=True)


def main():
    for s in (16, 32, 48, 96, 144, 192, 512):
        mark(s).save(os.path.join(ROOT, f"favicon-{s}x{s}.png"))
    mark(48).save(os.path.join(ROOT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    at = Image.new("RGBA", (180, 180), FOREST + (255,)); at.alpha_composite(mark(156), (12, 12))
    at.convert("RGB").save(os.path.join(ROOT, "apple-touch-icon.png"))
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect x="1" y="1" width="46" height="46" rx="11" fill="#0F3B30"/>'
           '<rect x="11" y="12" width="26" height="4" rx="2" fill="#F2C14E"/><rect x="11" y="22" width="18" height="4" rx="2" fill="#F2C14E" opacity=".75"/>'
           '<rect x="11" y="32" width="11" height="4" rx="2" fill="#F2C14E" opacity=".5"/>'
           '<path d="M27 33.5l4 4 7.5-9" fill="none" stroke="#7FD6B5" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    open(os.path.join(ROOT, "favicon.svg"), "w").write(svg)
    os.makedirs(os.path.join(ROOT, "images"), exist_ok=True)
    og = Image.new("RGB", (1200, 630), FOREST); d = ImageDraw.Draw(og)
    d.rectangle([0, 556, 1200, 630], fill=INK)
    m = mark(210); og.paste(m, (84, 190), m)
    d.text((340, 196), "Kiwi Casino Ledger", font=font(76), fill=(255, 255, 255))
    d.text((342, 300), "Online casino sites, checked and sourced", font=font(38, False), fill=KOWHAI)
    d.text((342, 360), "Licence · owner · NZD banking · limits · NZ law", font=font(29, False), fill=(205, 225, 216))
    d.text((84, 578), "R18 · Gambling can cause harm · 0800 654 655 · No casino links", font=font(24, False), fill=(205, 225, 216))
    og.save(os.path.join(ROOT, "images", "og.png"), optimize=True)
    logos()
    print("icons, og image and logos written")


if __name__ == "__main__":
    main()
