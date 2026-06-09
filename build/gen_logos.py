# -*- coding: utf-8 -*-
import os, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
G = json.load(open(os.path.join(os.path.dirname(__file__), "glyphs.json")))
UPM = G["upm"]
D = G["glyphs"]["Д"]
N9 = G["glyphs"]["9"]

DEFS = '''  <defs>
    <linearGradient id="navy" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#1d3252"/><stop offset="1" stop-color="#091322"/>
    </linearGradient>
    <linearGradient id="brass" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f0d79b"/><stop offset=".28" stop-color="#caa766"/>
      <stop offset=".55" stop-color="#a87f3c"/><stop offset=".78" stop-color="#e6c98a"/>
      <stop offset="1" stop-color="#9a702f"/>
    </linearGradient>
    <radialGradient id="sheen" cx=".34" cy=".28" r=".75">
      <stop offset="0" stop-color="#fff" stop-opacity=".5"/>
      <stop offset=".4" stop-color="#fff" stop-opacity="0"/>
    </radialGradient>
  </defs>'''

def place(g, s, tx, ty, fill="url(#brass)"):
    return '<path transform="translate(%.2f %.2f) scale(%.5f %.5f)" fill="%s" d="%s"/>' % (
        tx, ty, s, -s, fill, g["d"])

def svg(inner, size=64):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" aria-label="ДИС 99">\n%s\n%s\n</svg>\n'
            % (size, size, DEFS, inner))

# ---------- Concept A: Wax-seal medallion ----------
def concept_a():
    cx = 32
    # decorative ticks around ring
    ticks = ""
    import math
    for i in range(24):
        a = math.radians(i * 15)
        r1, r2 = 29.5, 31
        x1, y1 = cx + r1 * math.cos(a), cx + r1 * math.sin(a)
        x2, y2 = cx + r2 * math.cos(a), cx + r2 * math.sin(a)
        ticks += '<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" stroke="url(#brass)" stroke-width="%.2f" stroke-linecap="round" opacity=".9"/>' % (x1, y1, x2, y2, 1.4 if i % 6 == 0 else 0.7)
    d = place(D, 0.0360, 20.3, 41.2)
    n9a = place(N9, 0.0145, 25.6, 51.0)
    n9b = place(N9, 0.0145, 30.4, 51.0)
    inner = '''  <circle cx="32" cy="32" r="31.2" fill="none" stroke="url(#brass)" stroke-width="1.6"/>
  %s
  <circle cx="32" cy="32" r="26.2" fill="url(#navy)" stroke="url(#brass)" stroke-width="1"/>
  <circle cx="32" cy="32" r="26.2" fill="url(#sheen)"/>
  %s
  <path d="M22 45.5 Q32 49 42 45.5" fill="none" stroke="url(#brass)" stroke-width="1" stroke-linecap="round" opacity=".75"/>
  %s%s''' % (ticks, d, n9a, n9b)
    return svg(inner)

# ---------- Concept B: Crest / shield ----------
def concept_b():
    shield = 'M10 7 H54 V33 Q54 49 32 59 Q10 49 10 33 Z'
    d = place(D, 0.0330, 21.0, 36.0)
    n9a = place(N9, 0.0150, 25.4, 52.5)
    n9b = place(N9, 0.0150, 30.4, 52.5)
    inner = '''  <path d="%s" fill="url(#navy)"/>
  <path d="%s" fill="url(#sheen)"/>
  <path d="%s" fill="none" stroke="url(#brass)" stroke-width="1.6"/>
  <path d="M14 11 H50" stroke="url(#brass)" stroke-width="1" opacity=".5"/>
  %s
  <path d="M19 41 H45" stroke="url(#brass)" stroke-width="1" opacity=".8"/>
  %s%s''' % (shield, shield, shield, d, n9a, n9b)
    return svg(inner)

# ---------- Concept C: Modern squircle + signature swash ----------
def concept_c():
    d = place(D, 0.0380, 16.5, 42.5)
    n9a = place(N9, 0.0150, 40.0, 30.0)
    n9b = place(N9, 0.0150, 44.6, 30.0)
    inner = '''  <rect x="1.5" y="1.5" width="61" height="61" rx="20" fill="url(#navy)"/>
  <rect x="1.5" y="1.5" width="61" height="61" rx="20" fill="url(#sheen)"/>
  <rect x="4.5" y="4.5" width="55" height="55" rx="17" fill="none" stroke="url(#brass)" stroke-width="1" stroke-opacity=".55"/>
  %s
  <path d="M12 47 C22 53 42 53 52 45" fill="none" stroke="url(#brass)" stroke-width="1.6" stroke-linecap="round"/>
  %s%s''' % (d, n9a, n9b)
    return svg(inner)

os.makedirs(os.path.join(ROOT, "img"), exist_ok=True)
for name, fn in [("logo-a", concept_a), ("logo-b", concept_b), ("logo-c", concept_c)]:
    open(os.path.join(ROOT, "img", name + ".svg"), "w", encoding="utf-8").write(fn())
    print("wrote img/%s.svg" % name)

# Preview gallery
gallery = '''<!doctype html><html><head><meta charset="utf-8"><style>
body{margin:0;background:#fbf8f2;font-family:Inter,system-ui,sans-serif;padding:40px;}
.row{display:flex;gap:50px;flex-wrap:wrap;justify-content:center;align-items:flex-end;}
.item{text-align:center;}
.big{width:150px;height:150px;}
.dark{background:#0a1422;padding:24px;border-radius:20px;margin-top:16px;display:flex;gap:16px;align-items:center;justify-content:center;}
.sm{width:54px;height:54px;}
.hdr{background:#fff;border:1px solid #e7ddca;border-radius:14px;padding:12px 18px;margin-top:12px;display:flex;gap:12px;align-items:center;justify-content:center;}
h3{color:#16202e;font-family:Georgia,serif;}
.wm{font-family:"Playfair Display",Georgia,serif;font-weight:700;font-size:22px;color:#243043;}
.wm i{color:#8a6630;}
</style></head><body>
<div class="row">
'''
for label, name in [("A · Медальон (seal)", "logo-a"), ("B · Герб (crest)", "logo-b"), ("C · Модерен (squircle)", "logo-c")]:
    gallery += '''<div class="item"><h3>%s</h3>
      <img class="big" src="../../img/%s.svg">
      <div class="hdr"><img class="sm" src="../../img/%s.svg"><span class="wm">ДИС&nbsp;<i>99</i></span></div>
      <div class="dark"><img class="sm" src="../../img/%s.svg"><span class="wm" style="color:#fff">ДИС&nbsp;<i style="color:#cda969">99</i></span></div>
    </div>''' % (label, name, name, name)
gallery += "</div></body></html>"
os.makedirs(os.path.join(ROOT, "build", "_preview"), exist_ok=True)
open(os.path.join(ROOT, "build", "_preview", "logos.html"), "w", encoding="utf-8").write(gallery)
print("wrote build/_preview/logos.html")
