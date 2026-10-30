#!/usr/bin/env python3
"""Favicons at 48/96/144/192/512 px (all multiples of 48) plus 16/32 for old
browsers, favicon.ico, favicon.svg, apple-touch-icon, the Open Graph card, and
web-sized copies of the operator logos. The mark matches BRAND_MARK in lib.py."""
import os, glob
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FOREST, KOWHAI, MINT, PAPER, INK = (15, 59, 48), (242, 193, 78), (127, 214, 181), (247, 245, 239), (24, 34, 31)


RED, CREAM, SOOT, ASH = (196, 56, 35), (243, 237, 221), (32, 27, 18), (43, 37, 25)


def mark(size):
    """A red casino chip with a kiwi at its centre; matches BRAND_MARK in lib.py."""
    import math
    s = size * 8; u = s / 48
    im = Image.new("RGBA", (s, s), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse([u, u, 47*u, 47*u], fill=RED)
    for k in range(8):                       # edge notches
        a = math.radians(k * 45)
        cx, cy = 24 + 19.55 * math.sin(a), 24 - 19.55 * math.cos(a)
        notch = Image.new("RGBA", (int(5*u), int(6.5*u)), CREAM + (255,))
        notch = notch.rotate(-k * 45, expand=True, resample=Image.BICUBIC)
        im.alpha_composite(notch, (int(cx*u - notch.width/2), int(cy*u - notch.height/2)))
    d = ImageDraw.Draw(im)
    d.ellipse([8.5*u, 8.5*u, 39.5*u, 39.5*u], fill=SOOT, outline=CREAM, width=max(1, int(1.4*u)))
    d.ellipse([19.3*u, 20*u, 33.7*u, 31.2*u], fill=CREAM)      # body
    d.ellipse([17*u, 19*u, 23*u, 25*u], fill=CREAM)            # head
    w = max(1, int(1.4*u))
    d.line([(17.6*u, 23.4*u), (14.5*u, 26.5*u), (11.8*u, 31*u)], fill=CREAM, width=w, joint="curve")   # beak
    for x in (25, 28.6):
        d.line([(x*u, 30.6*u), (x*u, 34.8*u)], fill=CREAM, width=w)
        d.line([((x-1.4)*u, 34.8*u), ((x+1.2)*u, 34.8*u)], fill=CREAM, width=w)
    d.ellipse([20.05*u, 20.65*u, 21.35*u, 21.95*u], fill=SOOT)  # eye
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
    at = Image.new("RGBA", (180, 180), ASH + (255,)); at.alpha_composite(mark(156), (12, 12))
    at.convert("RGB").save(os.path.join(ROOT, "apple-touch-icon.png"))
    import re, sys
    sys.path.insert(0, HERE)
    from lib import BRAND_MARK
    svg = re.sub(r'<svg class="mark"[^>]*>', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">', BRAND_MARK)
    open(os.path.join(ROOT, "favicon.svg"), "w").write(svg)
    os.makedirs(os.path.join(ROOT, "images"), exist_ok=True)
    og = Image.new("RGB", (1200, 630), ASH); d = ImageDraw.Draw(og)
    d.rectangle([0, 556, 1200, 630], fill=SOOT); d.rectangle([0, 548, 1200, 556], fill=RED)
    m = mark(210); og.paste(m, (84, 190), m)
    d.text((340, 196), "Kiwi Stakes", font=font(76), fill=(255, 255, 255))
    d.text((342, 300), "Online casino sites, checked and sourced", font=font(38, False), fill=(224, 80, 50))
    d.text((342, 360), "Licence · owner · NZD banking · limits · NZ law", font=font(29, False), fill=(224, 217, 198))
    d.text((84, 578), "R18 · Gambling can cause harm · 0800 654 655 · No casino links", font=font(24, False), fill=(224, 217, 198))
    og.save(os.path.join(ROOT, "images", "og.png"), optimize=True)
    # logos() trims fresh copies from MY_SITES/logos; already done for this set
    print("icons, og image and logos written")


if __name__ == "__main__":
    main()
