"""Scenes for The Back Corner (a Christmas tree lot at night)."""
import sys, math; sys.path.insert(0, "../../toolkit")
from scenekit import *

RED = "#e0261d"
WARM = "#ffb54a"
DARK = "#06070c"
SNOW_GROUND = "#2b3346"
BULBS = ["#ffc95a", "#ff4a3a", "#ffe9b0", "#7fd08a", "#ffc95a", "#ff7a3a"]


def pine(x, base, h, col="#0a0f12", snow="#3d4659", tag=False, snowcap=True, w=None):
    """Layered pine silhouette rooted at (x, base)."""
    w = w or h * 0.42
    o = [f'<rect x="{x - h * .025:.0f}" y="{base - h * .08:.0f}" width="{h * .05:.0f}" height="{h * .08:.0f}" fill="{col}"/>']
    tiers = 5
    for i in range(tiers):
        top = base - h + i * h * 0.17
        bot = base - h * 0.08 - (tiers - 1 - i) * h * 0.12
        hw = w * (0.35 + 0.65 * (i + 1) / tiers) / 2
        # jagged lower edge
        pts = [f"{x:.0f},{top:.0f}"]
        n = 6
        for k in range(n + 1):
            px = x + hw - 2 * hw * k / n
            py = bot + (8 if k % 2 == 0 else -6) * h / 400
            pts.append(f"{px:.0f},{py:.0f}")
        o.append(f'<polygon points="{" ".join(pts[:1] + pts[1:])}" fill="{col}"/>')
        if snowcap:
            o.append(f'<path d="M{x - hw * .55:.0f} {bot - (bot - top) * .35:.0f} Q{x} {bot - (bot - top) * .48:.0f} {x + hw * .55:.0f} {bot - (bot - top) * .35:.0f}" '
                     f'stroke="{snow}" stroke-width="{max(2, h / 90):.0f}" fill="none" opacity="0.7" stroke-linecap="round"/>')
    if tag:
        tx, ty = x + w * 0.18, base - h * 0.42
        o.append(f'<line x1="{tx:.0f}" y1="{ty - 10:.0f}" x2="{tx:.0f}" y2="{ty:.0f}" stroke="#9a8f80" stroke-width="2"/>')
        o.append(f'<rect x="{tx - 7:.0f}" y="{ty:.0f}" width="14" height="20" rx="2" fill="{RED}"/>')
    return "".join(o)


def lights(x1, y1, x2, y2, sag=60, n=14, glow_op=0.55, wire="#05060a"):
    """A sagging string of bulbs between two points."""
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2 + sag
    o = [f'<path d="M{x1} {y1} Q{mx:.0f} {my + sag:.0f} {x2} {y2}" stroke="{wire}" stroke-width="3" fill="none"/>']
    for k in range(1, n):
        t = k / n
        px = (1 - t) ** 2 * x1 + 2 * (1 - t) * t * mx + t * t * x2
        py = (1 - t) ** 2 * y1 + 2 * (1 - t) * t * (my + sag) + t * t * y2
        c = BULBS[k % len(BULBS)]
        o.append(f'<circle cx="{px:.0f}" cy="{py + 6:.0f}" r="14" fill="{c}" opacity="{glow_op * .5:.2f}" filter="url(#blur8)"/>')
        o.append(f'<circle cx="{px:.0f}" cy="{py + 6:.0f}" r="5" fill="{c}"/>')
    return "".join(o)


def pole(x, top, base, col=DARK):
    return f'<rect x="{x - 6}" y="{top}" width="12" height="{base - top}" fill="{col}"/>'


def trailer(x, y, w=330, h=170, col="#0b0d14", lit=True, door=True):
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="{col}"/>',
         f'<rect x="{x + 10}" y="{y + h}" width="{w - 20}" height="14" fill="#040509"/>',
         f'<circle cx="{x + w * .3:.0f}" cy="{y + h + 18}" r="22" fill="#040509"/>',
         f'<line x1="{x}" y1="{y + 30}" x2="{x + w}" y2="{y + 30}" stroke="#1a1e2a" stroke-width="3"/>']
    if lit:
        o.append(lit_window(x + 40, y + 55, 90, 58))
    else:
        o.append(f'<rect x="{x + 40}" y="{y + 55}" width="90" height="58" fill="#1a2030"/>')
    if door:
        o.append(f'<rect x="{x + w - 100}" y="{y + 45}" width="58" height="{h - 45}" fill="#05060a"/>')
        o.append(f'<rect x="{x + w - 112}" y="{y + h + 2}" width="82" height="10" fill="#05060a"/>')
    # snow on roof
    o.append(f'<path d="M{x + 12} {y + 4} Q{x + w / 2} {y - 14} {x + w - 12} {y + 4}" stroke="#56607a" stroke-width="10" fill="none" stroke-linecap="round"/>')
    return "".join(o)


def snow(n, op=0.75, ymax=1080, rmin=1.5, rmax=4.5, avoid=()):
    out = []
    for _ in range(n):
        x, y = rnd.randint(0, W), rnd.randint(0, ymax)
        if any(((x - ax) / rx) ** 2 + ((y - ay) / ry) ** 2 < 1 for ax, ay, rx, ry in avoid):
            continue
        out.append(f'<circle cx="{x}" cy="{y}" r="{rnd.uniform(rmin, rmax):.1f}" fill="#e8ecf6" opacity="{rnd.uniform(0.3, op):.2f}"/>')
    return "".join(out)


def person(cx, base, h=420, col="#040406", scarf=True, smile=False, back=False):
    """Coat-wearing silhouette with a red scarf."""
    hw = h * 0.16
    head_r = h * 0.085
    hy = base - h + head_r
    o = [f'<g>']
    o.append(f'<path d="M{cx - hw * .55:.0f} {base} L{cx - hw:.0f} {base - h * .45:.0f} Q{cx - hw * 1.05:.0f} {base - h * .74:.0f} {cx - hw * .55:.0f} {base - h * .78:.0f} '
             f'L{cx + hw * .55:.0f} {base - h * .78:.0f} Q{cx + hw * 1.05:.0f} {base - h * .74:.0f} {cx + hw:.0f} {base - h * .45:.0f} L{cx + hw * .55:.0f} {base} Z" fill="{col}"/>')
    o.append(f'<rect x="{cx - hw * .5:.0f}" y="{base - h * .2:.0f}" width="{hw * .4:.0f}" height="{h * .2:.0f}" fill="{col}"/>')
    o.append(f'<rect x="{cx + hw * .1:.0f}" y="{base - h * .2:.0f}" width="{hw * .4:.0f}" height="{h * .2:.0f}" fill="{col}"/>')
    o.append(f'<circle cx="{cx}" cy="{hy:.0f}" r="{head_r:.0f}" fill="{col}"/>')
    if scarf:
        sy = base - h * .79
        o.append(f'<rect x="{cx - hw * .62:.0f}" y="{sy - h * .02:.0f}" width="{hw * 1.24:.0f}" height="{h * .055:.0f}" rx="{h * .02:.0f}" fill="{RED}"/>')
        tail_x = cx + (hw * .25 if not back else -hw * .3)
        o.append(f'<path d="M{tail_x:.0f} {sy:.0f} l{hw * .28:.0f} 0 l{hw * .05:.0f} {h * .2:.0f} l{-hw * .3:.0f} 0 Z" fill="#b81c15"/>')
        o.append(f'<rect x="{cx - hw * .62:.0f}" y="{sy - h * .02:.0f}" width="{hw * 1.24:.0f}" height="{h * .055:.0f}" fill="{RED}" opacity="0.5" filter="url(#blur8)"/>')
    if smile:
        r = head_r * .55
        o.append(f'<path d="M{cx - r:.0f} {hy + head_r * .15:.0f} Q{cx} {hy + head_r * .75:.0f} {cx + r:.0f} {hy + head_r * .15:.0f}" stroke="#d9d4c4" stroke-width="{max(2, h / 140):.0f}" fill="none" stroke-linecap="round" opacity="0.85"/>')
        o.append(f'<circle cx="{cx - head_r * .35:.0f}" cy="{hy - head_r * .2:.0f}" r="{max(2, h / 120):.0f}" fill="#d9d4c4" opacity="0.8"/>')
        o.append(f'<circle cx="{cx + head_r * .35:.0f}" cy="{hy - head_r * .2:.0f}" r="{max(2, h / 120):.0f}" fill="#d9d4c4" opacity="0.8"/>')
    o.append('</g>')
    return "".join(o)


def family(cx, base, s=1.0, smile=False, back=False):
    return (person(cx - 150 * s, base, 430 * s, smile=smile, back=back) +
            person(cx + 150 * s, base, 460 * s, smile=smile, back=back) +
            person(cx - 55 * s, base + 6 * s, 250 * s, smile=smile, back=back) +
            person(cx + 55 * s, base + 6 * s, 220 * s, smile=smile, back=back))


def ground(y, col=SNOW_GROUND, col2="#1d2333"):
    return (f'<path d="M0 {y} C500 {y - 20} 1300 {y + 15} 1920 {y - 10} L1920 1080 L0 1080Z" fill="{col}"/>'
            f'<path d="M0 {y + 140} C600 {y + 110} 1300 {y + 150} 1920 {y + 125} L1920 1080 L0 1080Z" fill="{col2}" opacity="0.6"/>')


NIGHT = sky("night", "#04050c", "#141a2e", "#2a2f48")

# S1 — the lot at night
rows = ""
for r, (yb, hh, col) in enumerate([(700, 150, "#0d1218"), (760, 200, "#0b1015"), (840, 260, "#080c10")]):
    for x in range(480 + r * 40, 1460, 110 + r * 40):
        if 1080 < x < 1420: continue
        rows += pine(x + rnd.randint(-15, 15), yb, hh + rnd.randint(-20, 20), col=col, tag=(r == 2 and rnd.random() < .6))
save("s1", svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(120, 500)}
{moon(700, 230, 70)}
{ground(690)}
{pole(500, 380, 700)}{pole(1420, 380, 700)}{pole(960, 400, 700)}
{lights(500, 390, 960, 410, 30)}{lights(960, 410, 1420, 390, 30)}
<rect x="1180" y="560" width="160" height="40" fill="#11141c"/>
<text x="1260" y="589" text-anchor="middle" font-family="{SANS}" font-size="24" font-weight="700" fill="{RED}" letter-spacing="3">TREES</text>
{trailer(1140, 610, 260, 140)}
{rows}
{glow(1220, 700, 140, WARM, .15)}
{fog(760, op=.12)}
{snow(260, .7)}
''', NIGHT))

# S2 — the tall tree in the back corner
back = "".join(pine(x, 760, 190 + rnd.randint(-20, 20), col="#0c1117", tag=True) for x in (560, 680, 1240, 1360))
save("s2", svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(80, 300, .5)}
{ground(740)}
<ellipse cx="980" cy="430" rx="230" ry="380" fill="#4a1414" opacity="0.18" filter="url(#blur60)"/>
{back}
{pine(980, 800, 680, col="#020305", snow="#2a3142", snowcap=False, w=330)}
<ellipse cx="980" cy="805" rx="170" ry="16" fill="#000" opacity="0.6"/>
{fog(830, op=.15)}
<g>{person(640, 1040, 470, col="#020203", scarf=False)}
<path d="M676 640 L860 600" stroke="#020203" stroke-width="20" stroke-linecap="round"/>
<path d="M610 590 Q640 540 670 590Z" fill="#020203"/><rect x="590" y="584" width="100" height="10" rx="5" fill="#020203"/></g>
{snow(160, .6)}
''', NIGHT))

# S3 — inside the trailer: space heater and the window
outside = "".join(pine(x, 470, 120 + rnd.randint(-15, 15), col="#0a0f14", snowcap=False) for x in range(760, 1240, 70))
save("s3", svg(f'''
<rect width="{W}" height="{H}" fill="#120d0c"/>
<rect x="0" y="760" width="{W}" height="320" fill="#1c1310"/>
<rect x="700" y="180" width="520" height="320" rx="16" fill="#0a0d18"/>
<rect x="715" y="195" width="490" height="290" fill="url(#night)"/>
{lights(715, 260, 1205, 250, 20, 10)}
{outside}
<rect x="715" y="420" width="490" height="65" fill="#2b3346"/>
<line x1="960" y1="195" x2="960" y2="485" stroke="#0a0d18" stroke-width="10"/>
<rect x="700" y="500" width="520" height="22" fill="#24180f"/>
<g transform="translate(960 780)">
<rect x="-120" y="-150" width="240" height="190" rx="18" fill="#2a201b"/>
<rect x="-95" y="-125" width="190" height="130" rx="8" fill="#170e0a"/>
{''.join(f'<rect x="-82" y="{-112 + i * 30}" width="164" height="10" rx="5" fill="#ff6a24"/>' for i in range(4))}
<rect x="-95" y="-125" width="190" height="130" fill="#ff7a2a" opacity="0.5" filter="url(#blur30)"/>
<rect x="-110" y="40" width="40" height="14" fill="#160f0b"/><rect x="70" y="40" width="40" height="14" fill="#160f0b"/>
</g>
{glow(960, 690, 200, "#ff7a2a", .22)}
<path d="M1260 640 h70 v80 q0 22 -22 22 h-26 q-22 0 -22 -22 z" fill="#3a2a22"/><path d="M1330 660 q30 0 30 25 q0 25 -30 25" stroke="#3a2a22" stroke-width="10" fill="none"/>
<path d="M1280 630 q-10 -30 8 -55 M1305 628 q12 -30 -4 -60" stroke="#8d8070" stroke-width="3" fill="none" opacity="0.4"/>
{snow(40, .5, 480)}
'''.replace('<rect x="715" y="195" width="490" height="290" fill="url(#night)"/>', '<rect x="715" y="195" width="490" height="290" fill="url(#night)"/>'), NIGHT))

# S4 — the front gate creaking open
mesh = "".join(f'<path d="M{x} 520 l60 60 l-60 60 l60 60 l-60 60 l60 60" stroke="#2c3346" stroke-width="2" fill="none"/>' for x in range(560, 1380, 34))
save("s4", svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(70, 350, .5)}
{ground(830)}
<path d="M830 830 L1090 830 L1400 1080 L520 1080Z" fill="#3a4357" opacity="0.5"/>
<g clip-path="url(#fenceL)">{mesh}</g>
<rect x="540" y="500" width="14" height="340" fill="{DARK}"/><rect x="820" y="500" width="14" height="340" fill="{DARK}"/>
<line x1="540" y1="520" x2="834" y2="520" stroke="{DARK}" stroke-width="8"/>
<g transform="translate(1100 500) skewY(-8)">
<rect x="0" y="0" width="12" height="330" fill="{DARK}"/><rect x="230" y="0" width="12" height="330" fill="{DARK}"/>
<line x1="0" y1="20" x2="242" y2="20" stroke="{DARK}" stroke-width="8"/><line x1="0" y1="320" x2="242" y2="320" stroke="{DARK}" stroke-width="8"/>
<path d="M0 320 L242 20" stroke="{DARK}" stroke-width="6"/>
<g opacity="0.8">{''.join(f'<line x1="{x}" y1="20" x2="{x}" y2="320" stroke="#2c3346" stroke-width="2"/>' for x in range(20, 240, 22))}</g>
</g>
<rect x="1090" y="500" width="16" height="340" fill="{DARK}"/>
<g transform="rotate(25 1140 680)"><rect x="1100" y="650" width="80" height="12" fill="#5a4a3a"/></g>
{lights(540, 520, 834, 520, 15, 8)}
<rect x="1400" y="260" width="12" height="580" fill="{DARK}"/><path d="M1406 270 q-60 0 -80 30" stroke="{DARK}" stroke-width="10" fill="none"/>
<path d="M1326 300 L1180 840 L1500 840 Z" fill="#e6dfc4" opacity="0.06"/>
{glow(1326, 305, 50, "#ffe3a8", .7)}
<g opacity="0.6">{''.join(pine(x, 840, 160, col="#0b1016") for x in (420, 300))}</g>
{fog(860, op=.14)}
{snow(240, .75)}
''', NIGHT + '<clipPath id="fenceL"><rect x="540" y="520" width="294" height="320"/></clipPath>'))

# S5 — the family walks in, red scarves
aisle_l = "".join(pine(x, 820 - (x - 300) * .05, 300, col="#090d12", tag=True) for x in (360, 520))
aisle_r = "".join(pine(x, 820 - (1620 - x) * .05, 300, col="#090d12", tag=True) for x in (1420, 1580))
save("s5", svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(70, 300, .5)}
{ground(700)}
{''.join(pine(x, 700, 150, col="#0d1218") for x in range(600, 1400, 90))}
{lights(400, 360, 1520, 360, 50, 20)}
{aisle_l}{aisle_r}
{fog(820, op=.14)}
{family(960, 1000, 1.0)}
{snow(260, .75)}
''', NIGHT))

# S6 — at the tall tree, smiling
save("s6", svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{ground(780)}
<ellipse cx="960" cy="380" rx="300" ry="420" fill="#4a1414" opacity="0.22" filter="url(#blur60)"/>
{pine(960, 860, 820, col="#020305", snowcap=False, w=420)}
{fog(860, op=.12)}
<ellipse cx="960" cy="880" rx="260" ry="50" fill="#2b3346"/><ellipse cx="960" cy="1020" rx="420" ry="30" fill="#000" opacity="0.4"/>
{family(960, 1030, 0.95, smile=True)}
{snow(200, .7)}
''', NIGHT))

# S7 — snow falls, but not on them
avoid = [(817, 790, 100, 250), (1103, 770, 100, 270), (908, 900, 60, 150), (1012, 910, 55, 135)]
save("s7", svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{ground(760)}
{''.join(pine(x, 760, 260, col="#0a0e14") for x in (560, 700, 1220, 1360))}
{fog(800, op=.16)}
{family(960, 1030, 0.95, smile=True)}
{snow(900, .9, 1080, 2, 5.5, avoid)}
<g fill="none" stroke="#e8ecf6" stroke-width="2" opacity="0.18">{''.join(f'<ellipse cx="{a}" cy="{b}" rx="{c}" ry="{d}" stroke-dasharray="4 14"/>' for a, b, c, d in avoid)}</g>
''', NIGHT))

# S8 — morning: smooth snow, the tall tree far in the back
DAWN = sky("dawn", "#1e2638", "#4a5570", "#8a8f9e")


def morning(tall_x, tall_base, tall_h, scarf=False):
    small = "".join(pine(x, 640, 140, col="#1c2330", snow="#8d97ab", tag=True) for x in range(560, 1100, 95))
    s = (f'<rect width="{W}" height="{H}" fill="url(#dawn)"/>'
         f'{glow(1400, 520, 260, "#d8b9a0", .2)}'
         f'<path d="M0 640 C500 625 1300 650 1920 630 L1920 1080 L0 1080Z" fill="#9aa2b4"/>'
         f'<path d="M0 820 C600 800 1300 830 1920 810 L1920 1080 L0 1080Z" fill="#aab1c1" opacity="0.7"/>'
         f'{small}'
         f'{pole(520, 360, 650, "#1a2030")}{pole(1400, 360, 650, "#1a2030")}'
         f'{lights(520, 370, 1400, 370, 30, 16, .2, "#1a2030")}'
         f'{trailer(1150, 650, 300, 160, col="#232a38", lit=False)}')
    if tall_base > 700:
        s += f'<ellipse cx="{tall_x}" cy="{tall_base + 4}" rx="{tall_h * .18:.0f}" ry="14" fill="#5a6274" opacity="0.6"/>'
    s += pine(tall_x, tall_base, tall_h, col="#07090d", snowcap=False, w=tall_h * .45)
    if scarf:
        y = tall_base - tall_h * .45
        s += f'<path d="M{tall_x - 60} {y} q60 30 120 -5 l-6 22 q-55 30 -110 4 Z" fill="{RED}"/><path d="M{tall_x + 40} {y + 10} l12 110 l-26 0 l-4 -100 Z" fill="#b81c15"/>'
    s += fog(700, "#c8ccd6", .18) + snow(70, .5)
    return svg(s, DAWN)


save("s8", morning(860, 650, 330))
save("s8b", morning(1000, 900, 720, scarf=True))
print("ok")
