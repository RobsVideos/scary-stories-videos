"""Scenes for 'The Head Count' — a night swim at a lake camp."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *


def pines(y, n, hmin, hmax, color, x0=0, x1=W, seed=3):
    r = random.Random(seed); out = []
    for _ in range(n):
        x = r.randint(x0, x1); h = r.randint(hmin, hmax); w = h * 0.32
        pts = []
        for k in range(4):
            ty = y - h + k * h * 0.22; by = ty + h * 0.34; ww = w * (0.35 + k * 0.22)
            pts.append(f'<polygon points="{x},{ty:.0f} {x - ww:.0f},{by:.0f} {x + ww:.0f},{by:.0f}"/>')
        out.append("".join(pts) + f'<rect x="{x - 4}" y="{y - h * 0.1:.0f}" width="8" height="{h * 0.1 + 6:.0f}"/>')
    return f'<g fill="{color}">{"".join(out)}</g>'


def treeline(y, color, seed=3, mirror=False, op=1.0):
    g = pines(y, 70, 70, 190, color, seed=seed) + f'<rect x="0" y="{y - 8}" width="{W}" height="12" fill="{color}"/>'
    if mirror:
        return f'<g transform="translate(0 {2 * y}) scale(1 -1)" opacity="{op}">{g}</g>'
    return g


def kid(cx, base, h=150, color="#06050a", smile=False, drip=False, towel="#0c0b14"):
    """Small child silhouette wrapped in a towel, facing us."""
    hr = h * 0.15
    s = (f'<g><circle cx="{cx}" cy="{base - h + hr:.0f}" r="{hr:.0f}" fill="{color}"/>'
         f'<path d="M{cx - h * .26:.0f} {base} C{cx - h * .30:.0f} {base - h * .45:.0f} {cx - h * .24:.0f} {base - h * .66:.0f} {cx:.0f} {base - h * .7:.0f} '
         f'C{cx + h * .24:.0f} {base - h * .66:.0f} {cx + h * .30:.0f} {base - h * .45:.0f} {cx + h * .26:.0f} {base} Z" fill="{towel}"/>'
         f'<path d="M{cx - h * .05:.0f} {base - h * .66:.0f} L{cx - h * .02:.0f} {base - h * .1:.0f}" stroke="#000" stroke-width="{max(2, h * .02):.0f}" opacity="0.6"/>'
         f'<rect x="{cx - h * .14:.0f}" y="{base - 2}" width="{h * .09:.0f}" height="{h * .12:.0f}" fill="{color}"/>'
         f'<rect x="{cx + h * .05:.0f}" y="{base - 2}" width="{h * .09:.0f}" height="{h * .12:.0f}" fill="{color}"/>')
    hy = base - h + hr
    if smile:
        s += (f'<path d="M{cx - hr * .55:.0f} {hy + hr * .25:.0f} Q{cx} {hy + hr * .85:.0f} {cx + hr * .55:.0f} {hy + hr * .25:.0f}" '
              f'stroke="#e9eef5" stroke-width="{max(2, hr * .14):.1f}" fill="none" stroke-linecap="round"/>'
              f'<circle cx="{cx - hr * .38:.0f}" cy="{hy - hr * .12:.0f}" r="{max(1.5, hr * .09):.1f}" fill="#e9eef5"/>'
              f'<circle cx="{cx + hr * .38:.0f}" cy="{hy - hr * .12:.0f}" r="{max(1.5, hr * .09):.1f}" fill="#e9eef5"/>')
    if drip:
        s += "".join(f'<ellipse cx="{cx + d:.0f}" cy="{base + h * .13:.0f}" rx="{h * .05:.0f}" ry="{h * .015:.0f}" fill="#8fb0d8" opacity="0.35"/>' for d in (-h * .2, 0, h * .18))
    return s + "</g>"


NIGHT = sky("skyN", "#04060e", "#141a33", "#2b2a48")
LAKE = '''<linearGradient id="lake" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#151a30"/><stop offset="1" stop-color="#05060c"/></linearGradient>'''


def reflect_streaks(cx, y0, y1, color="#f1e9d3"):
    r = random.Random(11); out = []
    for y in range(y0, y1, 14):
        w = r.randint(20, 120) * (1 + (y - y0) / 300)
        out.append(f'<rect x="{cx - w / 2 + r.randint(-20, 20):.0f}" y="{y}" width="{w:.0f}" height="4" rx="2" fill="{color}" opacity="{r.uniform(.25, .6):.2f}"/>')
    return "".join(out)


# S1 — the camp by the lake
cabin = lambda x, y, s, win=True: (
    f'<g fill="#07060c"><polygon points="{x},{y} {x + 90 * s},{y - 70 * s} {x + 180 * s},{y}"/>'
    f'<rect x="{x + 10 * s}" y="{y}" width="{160 * s}" height="{90 * s}"/></g>'
    + (lit_window(x + 30 * s, y + 22 * s, 46 * s, 36 * s) if win else '')
    + f'<rect x="{x + 110 * s}" y="{y + 30 * s}" width="{36 * s}" height="{60 * s}" fill="#0f0d16"/>')
chair = lambda x, y, s=1: (
    f'<g stroke="#05040a" stroke-width="{9 * s}" stroke-linecap="round" fill="none">'
    f'<path d="M{x} {y} L{x + 30 * s} {y - 210 * s} M{x + 110 * s} {y} L{x + 80 * s} {y - 210 * s}"/>'
    f'<path d="M{x + 10 * s} {y - 60 * s} H{x + 100 * s} M{x + 18 * s} {y - 130 * s} H{x + 92 * s}"/>'
    f'<path d="M{x + 20 * s} {y - 210 * s} H{x + 95 * s} M{x + 80 * s} {y - 210 * s} L{x + 88 * s} {y - 290 * s}"/></g>')
dock1 = ('<polygon points="860,1080 1060,1080 1010,700 960,700" fill="#0b0a12"/>'
         + "".join(f'<line x1="{860 + (960 - 860) * t:.0f}" y1="{1080 - 380 * t:.0f}" x2="{1060 - (1060 - 1010) * t:.0f}" y2="{1080 - 380 * t:.0f}" stroke="#16141f" stroke-width="3"/>' for t in [i / 14 for i in range(14)])
         + '<rect x="955" y="690" width="8" height="40" fill="#0b0a12"/><rect x="1008" y="690" width="8" height="40" fill="#0b0a12"/>')
save("s1", svg(f'''
<rect width="{W}" height="{H}" fill="url(#skyN)"/>
{stars(170, 520)}
{moon(1130, 230, 95)}
{treeline(620, "#0a0b16", seed=4)}
<rect x="0" y="620" width="{W}" height="460" fill="url(#lake)"/>
{treeline(620, "#0a0b16", seed=4, mirror=True, op=0.35)}
{reflect_streaks(1130, 640, 900)}
{fog(640, op=0.12, ry=60)}
{cabin(1190, 560, 0.9)}{cabin(1380, 575, 0.7, win=False)}
<path d="M0 860 C300 830 520 850 760 880 L760 1080 L0 1080Z" fill="#191623"/>
<path d="M1160 900 C1400 860 1700 870 1920 850 L1920 1080 L1160 1080Z" fill="#191623"/>
{chair(640, 930)}
{dock1}
<rect x="600" y="925" width="200" height="12" fill="#1f1b2b"/>
{grass(1080, 80, "#07060c")}
''', NIGHT + LAKE))

# S2 — the clipboard: twelve in, twelve out
tally = lambda x, y, n: "".join(
    (f'<line x1="{x + (i // 5) * 140 + (i % 5) * 22}" y1="{y}" x2="{x + (i // 5) * 140 + (i % 5) * 22 - 4}" y2="{y + 70}" stroke="#1d2a5a" stroke-width="7" stroke-linecap="round"/>'
     if i % 5 != 4 else f'<line x1="{x + (i // 5) * 140 - 14}" y1="{y + 56}" x2="{x + (i // 5) * 140 + 104}" y2="{y + 12}" stroke="#1d2a5a" stroke-width="7" stroke-linecap="round"/>')
    for i in range(n))
planks = "".join(f'<rect x="0" y="{y}" width="{W}" height="86" fill="{c}"/><line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#08070a" stroke-width="5"/>'
                 for y, c in zip(range(0, 1100, 90), ["#1b1512", "#211a15", "#1d1713"] * 5))
save("s2", svg(f'''
<rect width="{W}" height="{H}" fill="#0d0a09"/>
{planks}
<circle cx="960" cy="560" r="520" fill="#ffe2a8" opacity="0.18" filter="url(#blur60)"/>
<g transform="rotate(-4 960 560)">
<rect x="650" y="110" width="620" height="880" rx="26" fill="#5a3b22"/>
<rect x="690" y="180" width="540" height="780" fill="#e8e1cf"/>
<rect x="690" y="180" width="540" height="780" fill="#ffd79a" opacity="0.15"/>
<rect x="840" y="88" width="240" height="70" rx="14" fill="#9a9aa4"/><rect x="870" y="70" width="180" height="40" rx="12" fill="#7b7b86"/>
<text x="960" y="270" text-anchor="middle" font-family="{SANS}" font-size="46" font-weight="bold" fill="#2a2a33" letter-spacing="4">SWIM COUNT</text>
<line x1="730" y1="300" x2="1190" y2="300" stroke="#2a2a33" stroke-width="3"/>
<text x="740" y="420" font-family="{SANS}" font-size="44" fill="#2a2a33">IN</text>
{tally(890, 365, 12)}
<text x="740" y="580" font-family="{SANS}" font-size="44" fill="#2a2a33">OUT</text>
{tally(890, 525, 12)}
<g stroke="#b9b2a0" stroke-width="3">{''.join(f'<line x1="730" y1="{y}" x2="1190" y2="{y}"/>' for y in range(660, 940, 70))}</g>
</g>
<g stroke="#b3261e" stroke-width="8" fill="none" stroke-linecap="round"><path d="M1300 160 C1340 400 1260 600 1290 800"/></g>
<rect x="1220" y="790" width="110" height="46" rx="20" fill="#c9ccd4"/><circle cx="1290" cy="813" r="34" fill="#c9ccd4"/><circle cx="1290" cy="813" r="14" fill="#5d6068"/>
''', ""))

# S3 — the lake like black glass
dock3 = ('<polygon points="820,1080 1100,1080 990,640 930,640" fill="#07060b"/>'
         + "".join(f'<line x1="{820 + 110 * t:.0f}" y1="{1080 - 440 * t:.0f}" x2="{1100 - 110 * t:.0f}" y2="{1080 - 440 * t:.0f}" stroke="#121019" stroke-width="3"/>' for t in [i / 16 for i in range(16)])
         + '<rect x="926" y="630" width="8" height="30" fill="#07060b"/><rect x="986" y="630" width="8" height="30" fill="#07060b"/>')
save("s3", svg(f'''
<rect width="{W}" height="{H}" fill="url(#skyN)"/>
{stars(150, 500, 0.8)}
{moon(1160, 220, 80)}
{treeline(560, "#06070f", seed=9)}
<rect x="0" y="560" width="{W}" height="520" fill="#080a16"/>
{treeline(560, "#06070f", seed=9, mirror=True, op=0.9)}
<g opacity="0.6">{moon(1160, 900, 80)}</g>
<ellipse cx="960" cy="562" rx="1100" ry="6" fill="#4a5276" opacity="0.5"/>
{fog(590, op=0.10, ry=45)}
{dock3}
''', NIGHT))

# S4 — twelve heads in the black water
heads = [(620, 700, 16), (720, 690, 14), (820, 705, 17), (930, 695, 15), (1050, 702, 16), (1160, 690, 14), (1270, 704, 17),
         (680, 790, 24), (830, 800, 26), (1000, 785, 23), (1130, 805, 27), (1290, 792, 24)]
ripples = "".join(f'<ellipse cx="{x}" cy="{y + r * .9:.0f}" rx="{r * 2.8:.0f}" ry="{r * .5:.0f}" fill="none" stroke="#7f8fbf" stroke-width="2" opacity="0.4"/>'
                  f'<path d="M{x - r * 1.1:.0f} {y + r * .9:.0f} C{x - r:.0f} {y - r * .4:.0f} {x + r:.0f} {y - r * .4:.0f} {x + r * 1.1:.0f} {y + r * .9:.0f}" fill="#050409"/>'
                  f'<circle cx="{x}" cy="{y - r * .5:.0f}" r="{r * .9:.0f}" fill="#050409"/>' for x, y, r in heads)
save("s4", svg(f'''
<rect width="{W}" height="{H}" fill="url(#skyN)"/>
{stars(120, 460)}
{moon(1240, 200, 80)}
{treeline(540, "#090a15", seed=21)}
<rect x="0" y="540" width="{W}" height="540" fill="url(#lake)"/>
{treeline(540, "#090a15", seed=21, mirror=True, op=0.3)}
{reflect_streaks(1240, 560, 760)}
{ripples}
{fog(600, op=0.1, ry=50)}
<path d="M0 900 C400 880 1500 890 1920 910 L1920 1080 L0 1080Z" fill="#1b1825"/>
<path d="M0 905 C400 885 1500 895 1920 915" stroke="#7f8fbf" stroke-width="3" opacity="0.3" fill="none"/>
<g fill="#2a2338"><rect x="600" y="955" width="120" height="26" rx="8"/><rect x="610" y="935" width="100" height="24" rx="8" fill="#3a2a35"/><rect x="1180" y="960" width="130" height="24" rx="8"/></g>
<rect x="1240" y="920" width="12" height="60" fill="#0d0b14" transform="rotate(25 1246 950)"/>
{glow(1235, 930, 22, "#ffd17a", 0.8)}
''', NIGHT + LAKE))

# S5 — thirteen kids on the beach
back = [(600 + i * 120, 780, 150) for i in range(7)]
front = [(660 + i * 125, 940, 205) for i in range(6)]


def beach(smile):
    kids = "".join(kid(x, y, h, smile=smile, drip=True) for x, y, h in back) + "".join(kid(x, y, h, smile=smile, drip=True) for x, y, h in front)
    return svg(f'''
<rect width="{W}" height="{H}" fill="url(#skyN)"/>
{stars(120, 380)}
{moon(960, 170, 70)}
{treeline(430, "#090a15", seed=31)}
<rect x="0" y="430" width="{W}" height="300" fill="url(#lake)"/>
{reflect_streaks(960, 445, 700)}
<path d="M0 700 C500 680 1400 690 1920 700 L1920 1080 L0 1080Z" fill="#221d2c"/>
<path d="M0 700 C500 680 1400 690 1920 700" stroke="#9aa8d4" stroke-width="3" opacity="0.35" fill="none"/>
{fog(700, op=0.14, ry=70)}
<ellipse cx="960" cy="1000" rx="700" ry="90" fill="#000" opacity="0.4" filter="url(#blur30)"/>
{kids}
{glow(960, 200, 60, "#f1e9d3", 0.05)}
''', NIGHT + LAKE)


save("s5", beach(False))
save("s5b", beach(True))

# S6 — wet footprints circling the cabin
steps = []
for i in range(26):
    import math
    a = math.pi * (0.95 - i / 13.5)
    x = 960 + 520 * math.cos(a); y = 930 + 110 * math.sin(a) * (1 if i < 14 else -1)
    if i >= 14: x = 960 + 520 * math.cos(math.pi * (i - 14) / 12); y = 930 + 110 * math.sin(math.pi * (i - 14) / 12)
    s = 0.8 + (y - 820) / 300
    off = 12 if i % 2 else -12
    steps.append(f'<g transform="translate({x:.0f} {y + off:.0f}) rotate({(-1 if i < 14 else 1) * 75}) scale({s:.2f})">'
                 f'<ellipse rx="16" ry="9" fill="#9fc0ea" opacity="0.55"/><circle cx="18" cy="-6" r="3.5" fill="#9fc0ea" opacity="0.55"/>'
                 f'<circle cx="19" cy="1" r="3" fill="#9fc0ea" opacity="0.55"/></g>')
save("s6", svg(f'''
<rect width="{W}" height="{H}" fill="url(#skyN)"/>
{stars(120, 380)}
{pines(560, 22, 260, 420, "#07080f", seed=41)}
<path d="M0 640 C500 620 1400 630 1920 640 L1920 1080 L0 1080Z" fill="#18151f"/>
<g fill="#0a0910">
<polygon points="580,450 960,260 1340,450"/>
<rect x="620" y="450" width="680" height="380"/>
</g>
<g stroke="#15131c" stroke-width="3">{''.join(f'<line x1="620" y1="{y}" x2="1300" y2="{y}"/>' for y in range(480, 830, 38))}</g>
{lit_window(700, 520, 150, 120)}
{lit_window(1070, 520, 150, 120)}
<rect x="900" y="610" width="120" height="220" fill="#140f12"/>
<rect x="990" y="700" width="20" height="40" rx="4" fill="#5d4a2a"/>
<rect x="890" y="830" width="140" height="16" fill="#0d0b11"/>
<polygon points="700,640 850,640 900,900 560,900" fill="#ffb54a" opacity="0.06"/>
<polygon points="1070,640 1220,640 1360,900 1020,900" fill="#ffb54a" opacity="0.06"/>
{''.join(steps)}
{fog(960, op=0.12, ry=90)}
{grass(1080, 200, "#0b0a10")}
''', NIGHT))

# S7 — morning: the camper list
names = "".join(f'<text x="745" y="{360 + i * 52}" font-family="{SANS}" font-size="30" fill="#3a3a44">{i + 1}.</text>'
                f'<rect x="800" y="{338 + i * 52}" width="{[300, 260, 340, 220, 310, 280, 250, 330, 290, 240, 300][i]}" height="16" rx="8" fill="#5a5b68" opacity="0.55"/>'
                for i in range(11))
save("s7", svg(f'''
<rect width="{W}" height="{H}" fill="#1a1e26"/>
<rect x="1180" y="0" width="740" height="760" fill="#3c4a5e"/>
<rect x="1220" y="40" width="660" height="680" fill="#8fa3bb" opacity="0.6"/>
<rect x="1220" y="40" width="660" height="680" fill="#c9d4e2" opacity="0.4" filter="url(#blur60)"/>
<line x1="1550" y1="40" x2="1550" y2="720" stroke="#3c4a5e" stroke-width="16"/><line x1="1220" y1="380" x2="1880" y2="380" stroke="#3c4a5e" stroke-width="16"/>
<polygon points="1220,720 1880,720 1500,1080 700,1080" fill="#c9d4e2" opacity="0.07"/>
<rect x="0" y="780" width="{W}" height="300" fill="#2a221c"/>
<g transform="rotate(3 960 560)">
<rect x="660" y="110" width="600" height="900" rx="26" fill="#5a3b22"/>
<rect x="700" y="180" width="520" height="800" fill="#a8a59d"/>
<rect x="840" y="88" width="240" height="70" rx="14" fill="#9a9aa4"/>
<text x="960" y="270" text-anchor="middle" font-family="{SANS}" font-size="44" font-weight="bold" fill="#2a2a33" letter-spacing="4">CAMPERS</text>
<line x1="740" y1="298" x2="1180" y2="298" stroke="#2a2a33" stroke-width="3"/>
{names}
<g stroke="#c3c0b8" stroke-width="3">{''.join(f'<line x1="740" y1="{y}" x2="1180" y2="{y}"/>' for y in range(960 - 52 * 1, 980, 52))}</g>
<ellipse cx="760" cy="880" rx="44" ry="30" fill="none" stroke="#b3261e" stroke-width="6"/>
</g>
{glow(1500, 300, 260, "#dfe7f2", 0.12)}
''', ""))

# S8 — dawn: one small figure waiting at the end of the dock
dock8 = ('<polygon points="800,1080 1120,1080 990,660 930,660" fill="#0b0b12"/>'
         + "".join(f'<line x1="{800 + 130 * t:.0f}" y1="{1080 - 420 * t:.0f}" x2="{1120 - 130 * t:.0f}" y2="{1080 - 420 * t:.0f}" stroke="#191923" stroke-width="3"/>' for t in [i / 16 for i in range(16)]))
save("s8", svg(f'''
<rect width="{W}" height="{H}" fill="url(#dawn)"/>
<ellipse cx="960" cy="560" rx="900" ry="120" fill="#c2362b" opacity="0.30" filter="url(#blur60)"/>
{treeline(560, "#121520", seed=51)}
<rect x="0" y="560" width="{W}" height="520" fill="url(#dawnLake)"/>
{treeline(560, "#121520", seed=51, mirror=True, op=0.4)}
<ellipse cx="960" cy="600" rx="900" ry="60" fill="#c2362b" opacity="0.18" filter="url(#blur30)"/>
{dock8}
{kid(960, 672, 170, color="#030306", towel="#07070c", smile=True)}
<ellipse cx="960" cy="690" rx="70" ry="10" fill="#000" opacity="0.5"/>
{fog(640, color="#c8ccd8", op=0.22, ry=80)}
{fog(900, color="#c8ccd8", op=0.12, ry=120)}
''', sky("dawn", "#1a1d2a", "#3a3c4e", "#6b5a60")
    + '<linearGradient id="dawnLake" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a4352"/><stop offset="1" stop-color="#0d0e16"/></linearGradient>'))
print("drew scenes")
