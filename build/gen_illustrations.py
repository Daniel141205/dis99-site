# -*- coding: utf-8 -*-
import os, math
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
W, H = 480, 360

DEFS = '''  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f7efe0"/><stop offset="1" stop-color="#efe4cf"/>
    </linearGradient>
    <linearGradient id="navy" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#1d3252"/><stop offset="1" stop-color="#0c1d33"/>
    </linearGradient>
    <linearGradient id="brass" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#e7c98c"/><stop offset=".5" stop-color="#c19a55"/><stop offset="1" stop-color="#a2762f"/>
    </linearGradient>
    <radialGradient id="blob" cx=".5" cy=".5" r=".5">
      <stop offset="0" stop-color="#caa766" stop-opacity=".35"/><stop offset="1" stop-color="#caa766" stop-opacity="0"/>
    </radialGradient>
    <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.3" fill="#bda77f" opacity=".35"/>
    </pattern>
    <filter id="sh" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#3a2c12" flood-opacity="0.18"/>
    </filter>
  </defs>'''

def frame(inner):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img">\n%s\n'
            '  <rect width="%d" height="%d" rx="18" fill="url(#bg)"/>\n'
            '  <rect width="%d" height="%d" rx="18" fill="url(#dots)"/>\n'
            '  <circle cx="400" cy="60" r="150" fill="url(#blob)"/>\n'
            '  <circle cx="70" cy="320" r="120" fill="url(#blob)"/>\n'
            '%s\n</svg>\n' % (W, H, DEFS, W, H, W, H, inner))

def card(x, y, w, h, rot=0, fill="#fffdf8", cx=None, cy=None):
    cx = x + w / 2 if cx is None else cx
    cy = y + h / 2 if cy is None else cy
    return ('<g transform="rotate(%g %g %g)" filter="url(#sh)">'
            '<rect x="%g" y="%g" width="%g" height="%g" rx="12" fill="%s" stroke="#e9dcc2"/>'
            % (rot, cx, cy, x, y, w, h, fill))

def lines(x, y, w, n=4, gap=14, first_brass=True):
    s = ""
    for i in range(n):
        ww = w if i < n - 1 else w * 0.6
        col = "url(#brass)" if (i == 0 and first_brass) else "#d7cbb6"
        s += '<rect x="%g" y="%g" width="%g" height="4.5" rx="2.25" fill="%s"/>' % (x, y + i * gap, ww, col)
    return s

def coin(cx, cy, r=26):
    R = r * 0.5
    star = ('M%g %g L%g %g L%g %g L%g %g L%g %g L%g %g L%g %g L%g %g Z' % (
        cx, cy-R, cx+R*0.2, cy-R*0.2, cx+R, cy, cx+R*0.2, cy+R*0.2,
        cx, cy+R, cx-R*0.2, cy+R*0.2, cx-R, cy, cx-R*0.2, cy-R*0.2))
    return ('<g filter="url(#sh)"><circle cx="%g" cy="%g" r="%g" fill="url(#brass)"/>'
            '<circle cx="%g" cy="%g" r="%g" fill="none" stroke="#fff5e0" stroke-opacity=".5" stroke-width="2"/>'
            '<path d="%s" fill="#7a5a26"/></g>'
            % (cx, cy, r, cx, cy, r-5, star))

def bars(x, y, heights, bw=16, gap=12):
    s = ""
    for i, hh in enumerate(heights):
        s += '<rect x="%g" y="%g" width="%g" height="%g" rx="3" fill="url(#brass)"/>' % (x + i*(bw+gap), y - hh, bw, hh)
    return s

def linechart(x, y, w, h, pts):
    coords = [(x + w*px, y + h*(1-py)) for px, py in pts]
    d = "M" + " L".join("%g %g" % c for c in coords)
    nodes = "".join('<circle cx="%g" cy="%g" r="3.2" fill="#0c1d33"/>' % c for c in coords)
    return '<path d="%s" fill="none" stroke="url(#brass)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>%s' % (d, nodes)

def checkbadge(cx, cy, r=22, col="#2f7d5b"):
    return ('<g filter="url(#sh)"><circle cx="%g" cy="%g" r="%g" fill="%s"/>'
            '<path d="M%g %g l%g %g l%g %g" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/></g>'
            % (cx, cy, r, col, cx-r*0.42, cy, r*0.32, r*0.4, r*0.62, -r*0.7))

def avatar(cx, cy, r=24, fill="url(#navy)"):
    return ('<g filter="url(#sh)"><circle cx="%g" cy="%g" r="%g" fill="#fffdf8" stroke="#e9dcc2"/>'
            '<circle cx="%g" cy="%g" r="%g" fill="%s"/>'
            '<path d="M%g %g a%g %g 0 0 1 %g 0" fill="%s"/></g>'
            % (cx, cy, r, cx, cy-r*0.22, r*0.34, fill,
               cx-r*0.5, cy+r*0.55, r*0.5, r*0.5, r*1.0, fill))

def percent(cx, cy, r=26):
    return ('<g filter="url(#sh)"><circle cx="%g" cy="%g" r="%g" fill="url(#navy)"/>'
            '<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="url(#brass)" stroke-width="3.2" stroke-linecap="round"/>'
            '<circle cx="%g" cy="%g" r="3.6" fill="url(#brass)"/><circle cx="%g" cy="%g" r="3.6" fill="url(#brass)"/></g>'
            % (cx, cy, r, cx-r*0.4, cy+r*0.4, cx+r*0.4, cy-r*0.4,
               cx-r*0.38, cy-r*0.38, cx+r*0.38, cy+r*0.38))

# ---------------- scenes ----------------
def s_bookkeeping():
    inner = (card(150, 70, 200, 230, rot=-4) + lines(176, 104, 150, 6, 20) +
             '<rect x="176" y="244" width="150" height="2" fill="#e0d4bd"/>' +
             '<rect x="176" y="256" width="92" height="6" rx="3" fill="url(#brass)"/>' + '</g>' +
             card(70, 200, 150, 96, rot=5) + linechart(86, 214, 120, 64, [(0,.15),(.3,.5),(.55,.35),(.8,.8),(1,.7)]) + '</g>' +
             coin(360, 250, 30))
    return frame(inner)

def s_vat():
    inner = (card(140, 64, 190, 236) + lines(166, 100, 140, 6, 20) +
             '<rect x="166" y="244" width="140" height="2" fill="#e0d4bd"/>' +
             '<rect x="166" y="256" width="80" height="6" rx="3" fill="url(#brass)"/>' + '</g>' +
             percent(330, 96, 30) +
             checkbadge(150, 290, 24))
    # VIES star arc
    stars = ""
    for i in range(7):
        a = math.radians(200 + i*23)
        sx, sy = 235 + 150*math.cos(a), 180 + 150*math.sin(a)
        stars += '<circle cx="%g" cy="%g" r="3" fill="url(#brass)" opacity=".7"/>' % (sx, sy)
    return frame(inner + stars)

def s_annual():
    inner = (card(130, 96, 220, 200) +
             '<path d="M150 96 h70 v-14 a8 8 0 0 0 -8 -8 h-54 a8 8 0 0 0 -8 8 z" fill="url(#brass)"/>' +
             bars(166, 268, [40, 70, 56, 96], 22, 16) +
             linechart(166, 150, 150, 0.001, []) + '</g>' +
             card(296, 60, 110, 110, rot=6) +
             '<rect x="312" y="78" width="78" height="22" rx="6" fill="url(#navy)"/>' +
             '<circle cx="324" cy="128" r="7" fill="none" stroke="url(#brass)" stroke-width="3"/>' +
             '<rect x="342" y="120" width="40" height="6" rx="3" fill="#d7cbb6"/>' +
             '<rect x="342" y="134" width="30" height="6" rx="3" fill="#d7cbb6"/>' + '</g>')
    return frame(inner)

def s_payroll():
    inner = (card(150, 78, 180, 220) + lines(176, 112, 130, 5, 20) +
             '<rect x="176" y="232" width="60" height="20" rx="6" fill="url(#brass)"/>' +
             '<rect x="246" y="236" width="60" height="6" rx="3" fill="#d7cbb6"/>' + '</g>' +
             avatar(120, 150, 30) + avatar(160, 150, 30, fill="url(#brass)") +
             coin(350, 250, 30))
    return frame(inner)

def s_defense():
    shield = ('<g filter="url(#sh)"><path d="M240 70 L320 96 V176 C320 226 284 256 240 278 '
              'C196 256 160 226 160 176 V96 Z" fill="url(#navy)"/>'
              '<path d="M240 70 L320 96 V176 C320 226 284 256 240 278 C196 256 160 226 160 176 V96 Z" '
              'fill="none" stroke="url(#brass)" stroke-width="3"/>'
              '<path d="M212 172 l20 20 l40 -52" fill="none" stroke="url(#brass)" stroke-width="6" '
              'stroke-linecap="round" stroke-linejoin="round"/></g>')
    back = card(300, 120, 120, 150, rot=8) + lines(316, 150, 84, 5, 18) + '</g>'
    return frame(back + shield)

def s_registration():
    bld = ('<g filter="url(#sh)"><rect x="170" y="150" width="140" height="148" rx="6" fill="#fffdf8" stroke="#e9dcc2"/>'
           '<path d="M160 152 L240 104 L320 152 Z" fill="url(#navy)"/>'
           '<rect x="222" y="226" width="36" height="72" rx="4" fill="url(#navy)"/>'
           '<rect x="186" y="176" width="34" height="30" rx="4" fill="#e8dcc4"/>'
           '<rect x="260" y="176" width="34" height="30" rx="4" fill="#e8dcc4"/>'
           '<rect x="232" y="84" width="6" height="26" fill="url(#brass)"/>'
           '<path d="M238 86 h26 v16 h-26 z" fill="url(#brass)"/></g>')
    badge = ('<g filter="url(#sh)"><circle cx="330" cy="250" r="30" fill="url(#brass)"/>'
             '<path d="M330 236 v28 M316 250 h28" stroke="#fff" stroke-width="5" stroke-linecap="round"/></g>')
    return frame(bld + badge)

SCENES = {
    "bookkeeping": s_bookkeeping, "vat": s_vat, "annual": s_annual,
    "payroll": s_payroll, "defense": s_defense, "registration": s_registration,
}
os.makedirs(os.path.join(ROOT, "img", "services"), exist_ok=True)
for name, fn in SCENES.items():
    open(os.path.join(ROOT, "img", "services", name + ".svg"), "w", encoding="utf-8").write(fn())
    print("wrote img/services/%s.svg" % name)

# preview gallery
g = '<!doctype html><meta charset="utf-8"><body style="margin:0;background:#fbf8f2;padding:30px;display:grid;grid-template-columns:1fr 1fr;gap:24px;">'
for n in SCENES:
    g += '<div><img src="../../img/services/%s.svg" style="width:100%%;border-radius:14px;display:block"><p style="font-family:sans-serif;text-align:center;color:#16202e">%s</p></div>' % (n, n)
g += '</body>'
open(os.path.join(ROOT, "build", "_preview", "illustrations.html"), "w", encoding="utf-8").write(g)
print("wrote preview")
