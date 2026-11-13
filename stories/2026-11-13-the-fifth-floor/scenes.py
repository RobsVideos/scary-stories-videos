"""Scenes for 'The Fifth Floor'. Run inside this folder: python3 scenes.py"""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *
import random

r = random.Random(5135)

BRASS = "#c9953f"
RED = "#8e1a14"
GREEN = "#2b3b2a"


def pines(y0, n, color, hmin=120, hmax=260, x0=0, x1=W):
    out = []
    for _ in range(n):
        x = r.randint(x0, x1); h = r.randint(hmin, hmax); w = h * .38
        out.append(f'<path d="M{x} {y0 - h} L{x - w / 2:.0f} {y0} L{x + w / 2:.0f} {y0} Z" fill="{color}"/>')
        out.append(f'<path d="M{x} {y0 - h * 1.08:.0f} L{x - w * .3:.0f} {y0 - h * .45:.0f} L{x + w * .3:.0f} {y0 - h * .45:.0f} Z" fill="{color}"/>')
    return "".join(out)


def snow(n, op=0.5):
    return "".join(f'<circle cx="{r.randint(0, W)}" cy="{r.randint(0, H)}" r="{r.choice([1.5, 2, 2.5, 3])}" fill="#e8eef8" '
                   f'opacity="{r.uniform(.15, op):.2f}"/>' for _ in range(n))


def wallpaper(x, y, w, h, base=GREEN, line="#1c281c", op=0.5):
    """Old striped/diamond wallpaper."""
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{base}"/>', f'<g opacity="{op}">']
    for xx in range(int(x), int(x + w), 40):
        out.append(f'<line x1="{xx}" y1="{y}" x2="{xx}" y2="{y + h}" stroke="{line}" stroke-width="6"/>')
        for yy in range(int(y) + 20, int(y + h), 60):
            out.append(f'<path d="M{xx + 20} {yy - 10} l8 10 l-8 10 l-8 -10 Z" fill="{line}"/>')
    out.append('</g>')
    return "".join(out)


def bellhop(cx, base, s=1.0, smile=False, eye=True, suitcase=True, arm_out=False, gesture=False):
    """Bellhop: pillbox hat, red jacket with brass buttons, white gloves, dark face in shadow."""
    k = s
    out = []
    # legs
    out.append(f'<path d="M{cx - 62 * k:.0f} {base} L{cx - 50 * k:.0f} {base - 250 * k:.0f} L{cx + 50 * k:.0f} {base - 250 * k:.0f} L{cx + 62 * k:.0f} {base} '
               f'L{cx + 12 * k:.0f} {base} L{cx} {base - 170 * k:.0f} L{cx - 12 * k:.0f} {base} Z" fill="#0b0a10"/>')
    out.append(f'<rect x="{cx - 46 * k:.0f}" y="{base - 250 * k:.0f}" width="6" height="{240 * k:.0f}" fill="{BRASS}" opacity="0.5"/>')
    # jacket
    out.append(f'<path d="M{cx - 96 * k:.0f} {base - 230 * k:.0f} C{cx - 104 * k:.0f} {base - 330 * k:.0f} {cx - 110 * k:.0f} {base - 420 * k:.0f} {cx - 70 * k:.0f} {base - 470 * k:.0f} '
               f'L{cx + 70 * k:.0f} {base - 470 * k:.0f} C{cx + 110 * k:.0f} {base - 420 * k:.0f} {cx + 104 * k:.0f} {base - 330 * k:.0f} {cx + 96 * k:.0f} {base - 230 * k:.0f} Z" fill="{RED}"/>')
    out.append(f'<path d="M{cx - 96 * k:.0f} {base - 230 * k:.0f} C{cx - 104 * k:.0f} {base - 330 * k:.0f} {cx - 110 * k:.0f} {base - 420 * k:.0f} {cx - 70 * k:.0f} {base - 470 * k:.0f} '
               f'L{cx - 30 * k:.0f} {base - 470 * k:.0f} L{cx - 40 * k:.0f} {base - 230 * k:.0f} Z" fill="#000" opacity="0.35"/>')
    for i in range(5):
        y = base - 440 * k + i * 44 * k
        out.append(f'<circle cx="{cx - 22 * k:.0f}" cy="{y:.0f}" r="{7 * k:.0f}" fill="{BRASS}"/><circle cx="{cx + 22 * k:.0f}" cy="{y:.0f}" r="{7 * k:.0f}" fill="{BRASS}"/>')
    out.append(f'<rect x="{cx - 96 * k:.0f}" y="{base - 248 * k:.0f}" width="{192 * k:.0f}" height="{14 * k:.0f}" fill="{BRASS}" opacity="0.7"/>')
    # collar + neck + head
    out.append(f'<rect x="{cx - 26 * k:.0f}" y="{base - 500 * k:.0f}" width="{52 * k:.0f}" height="{36 * k:.0f}" fill="{RED}"/>')
    out.append(f'<ellipse cx="{cx}" cy="{base - 552 * k:.0f}" rx="{44 * k:.0f}" ry="{56 * k:.0f}" fill="#b9b4aa"/>')
    out.append(f'<ellipse cx="{cx}" cy="{base - 590 * k:.0f}" rx="{44 * k:.0f}" ry="{20 * k:.0f}" fill="#000" opacity="0.45" filter="url(#blur8)"/>')
    # pillbox hat
    out.append(f'<rect x="{cx - 40 * k:.0f}" y="{base - 640 * k:.0f}" width="{80 * k:.0f}" height="{46 * k:.0f}" rx="{6 * k:.0f}" fill="{RED}"/>')
    out.append(f'<rect x="{cx - 40 * k:.0f}" y="{base - 604 * k:.0f}" width="{80 * k:.0f}" height="{10 * k:.0f}" fill="{BRASS}"/>')
    out.append(f'<path d="M{cx + 40 * k:.0f} {base - 600 * k:.0f} L{cx + 52 * k:.0f} {base - 560 * k:.0f}" stroke="{BRASS}" stroke-width="{3 * k:.0f}"/>')
    if eye:
        for sg in (-1, 1):
            out.append(f'<ellipse cx="{cx + sg * 17 * k:.0f}" cy="{base - 560 * k:.0f}" rx="{11 * k:.0f}" ry="{9 * k:.0f}" fill="#141010"/>')
            out.append(f'<circle cx="{cx + sg * 17 * k:.0f}" cy="{base - 560 * k:.0f}" r="{2.5 * k:.1f}" fill="#ff3b2f"/>')
    if smile:
        out.append(f'<path d="M{cx - 26 * k:.0f} {base - 526 * k:.0f} Q{cx} {base - 508 * k:.0f} {cx + 26 * k:.0f} {base - 526 * k:.0f}" stroke="#1a0d0d" stroke-width="{4 * k:.0f}" fill="none" stroke-linecap="round"/>')
    else:
        out.append(f'<line x1="{cx - 14 * k:.0f}" y1="{base - 524 * k:.0f}" x2="{cx + 14 * k:.0f}" y2="{base - 524 * k:.0f}" stroke="#1a0d0d" stroke-width="{3 * k:.0f}"/>')
    # arms
    if gesture:
        out.append(f'<path d="M{cx + 92 * k:.0f} {base - 440 * k:.0f} C{cx + 150 * k:.0f} {base - 400 * k:.0f} {cx + 220 * k:.0f} {base - 380 * k:.0f} {cx + 280 * k:.0f} {base - 390 * k:.0f}" '
                   f'stroke="{RED}" stroke-width="{38 * k:.0f}" fill="none" stroke-linecap="round"/>')
        out.append(f'<ellipse cx="{cx + 304 * k:.0f}" cy="{base - 392 * k:.0f}" rx="{30 * k:.0f}" ry="{15 * k:.0f}" fill="#e9e4da"/>')
    elif suitcase:
        out.append(f'<path d="M{cx + 92 * k:.0f} {base - 440 * k:.0f} C{cx + 120 * k:.0f} {base - 360 * k:.0f} {cx + 124 * k:.0f} {base - 300 * k:.0f} {cx + 120 * k:.0f} {base - 250 * k:.0f}" '
                   f'stroke="{RED}" stroke-width="{38 * k:.0f}" fill="none" stroke-linecap="round"/>')
        out.append(f'<circle cx="{cx + 120 * k:.0f}" cy="{base - 236 * k:.0f}" r="{18 * k:.0f}" fill="#e9e4da"/>')
        sx, sy, sw, sh = cx + 40 * k, base - 220 * k, 170 * k, 130 * k
        out.append(f'<path d="M{sx + sw * .35:.0f} {sy} q{sw * .15:.0f} -22 {sw * .3:.0f} 0" stroke="#3a2414" stroke-width="{8 * k:.0f}" fill="none"/>')
        out.append(f'<rect x="{sx:.0f}" y="{sy:.0f}" width="{sw:.0f}" height="{sh:.0f}" rx="{10 * k:.0f}" fill="#5a3a22"/>')
        out.append(f'<rect x="{sx:.0f}" y="{sy + sh * .45:.0f}" width="{sw:.0f}" height="{6 * k:.0f}" fill="#3a2414"/>')
        for fx in (.2, .8):
            out.append(f'<rect x="{sx + sw * fx - 8 * k:.0f}" y="{sy + 4 * k:.0f}" width="{16 * k:.0f}" height="{20 * k:.0f}" fill="{BRASS}"/>')
        out.append(f'<rect x="{sx + sw * .55:.0f}" y="{sy + sh * .55:.0f}" width="{40 * k:.0f}" height="{28 * k:.0f}" fill="#e6dcc4" transform="rotate(8 {sx + sw * .6:.0f} {sy + sh * .6:.0f})"/>')
    else:
        out.append(f'<path d="M{cx + 92 * k:.0f} {base - 440 * k:.0f} C{cx + 110 * k:.0f} {base - 360 * k:.0f} {cx + 110 * k:.0f} {base - 300 * k:.0f} {cx + 100 * k:.0f} {base - 260 * k:.0f}" '
                   f'stroke="{RED}" stroke-width="{38 * k:.0f}" fill="none" stroke-linecap="round"/>')
    if arm_out:
        out.append(f'<path d="M{cx - 92 * k:.0f} {base - 440 * k:.0f} C{cx - 160 * k:.0f} {base - 380 * k:.0f} {cx - 220 * k:.0f} {base - 340 * k:.0f} {cx - 280 * k:.0f} {base - 330 * k:.0f}" '
                   f'stroke="{RED}" stroke-width="{38 * k:.0f}" fill="none" stroke-linecap="round"/>')
        out.append(f'<ellipse cx="{cx - 300 * k:.0f}" cy="{base - 330 * k:.0f}" rx="{30 * k:.0f}" ry="{16 * k:.0f}" fill="#e9e4da"/>')
    else:
        out.append(f'<path d="M{cx - 92 * k:.0f} {base - 440 * k:.0f} C{cx - 120 * k:.0f} {base - 360 * k:.0f} {cx - 120 * k:.0f} {base - 300 * k:.0f} {cx - 110 * k:.0f} {base - 260 * k:.0f}" '
                   f'stroke="{RED}" stroke-width="{38 * k:.0f}" fill="none" stroke-linecap="round"/>')
        out.append(f'<circle cx="{cx - 110 * k:.0f}" cy="{base - 246 * k:.0f}" r="{18 * k:.0f}" fill="#e9e4da"/>')
    return "".join(out)


def fifth_hall(bulb_x=980, swing=12):
    """The fifth-floor hallway seen through the open elevator doors (x 700-1220)."""
    return f'''
<rect x="700" y="160" width="520" height="760" fill="#0c100c"/>
{wallpaper(700, 160, 520, 760, "#26341f", "#141c12", 0.55)}
<polygon points="700,160 860,330 860,700 700,920" fill="#000" opacity="0.45"/>
<polygon points="1220,160 1060,330 1060,700 1220,920" fill="#000" opacity="0.55"/>
<rect x="860" y="330" width="200" height="370" fill="#121810"/>
<rect x="915" y="440" width="90" height="260" fill="#070907"/>
<polygon points="700,920 860,700 1060,700 1220,920" fill="#1a1410"/>
<polygon points="900,920 935,700 985,700 1020,920" fill="{RED}" opacity="0.45"/>
<polygon points="700,160 860,330 1060,330 1220,160" fill="#0a0d0a"/>
<line x1="960" y1="160" x2="{bulb_x}" y2="300" stroke="#0a0a0a" stroke-width="4"/>
{glow(bulb_x, 310, 200, "#f4e2a2", 0.55)}
<circle cx="{bulb_x}" cy="310" r="18" fill="#fff4c8"/>
<g opacity="0.5"><line x1="{bulb_x}" y1="310" x2="{bulb_x - swing}" y2="310" stroke="#fff4c8" stroke-width="2"/></g>
{''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#000" opacity="0.4"/>' for x, y, w, h in ((736, 380, 50, 320), (1134, 380, 50, 320)))}
'''


def cab_frame(doors_gap=520, light="#ffcf8a"):
    """Inside the elevator cab looking out: wood panels, brass rail, doors parted by doors_gap around x=960."""
    half = doors_gap / 2
    return f'''
<rect x="0" y="0" width="700" height="{H}" fill="#2a1a10"/>
<rect x="1220" y="0" width="700" height="{H}" fill="#2a1a10"/>
<g opacity="0.6">{"".join(f'<rect x="{x}" y="200" width="120" height="560" fill="none" stroke="#160d07" stroke-width="10"/>' for x in (120, 300, 480, 1320, 1500, 1680))}</g>
<rect x="0" y="0" width="{W}" height="160" fill="#1e130b"/>
<rect x="0" y="920" width="{W}" height="160" fill="#140d08"/>
<g opacity="0.4">{"".join(f'<line x1="{x}" y1="920" x2="{960 + (x - 960) * 1.6:.0f}" y2="{H}" stroke="#0a0604" stroke-width="3"/>' for x in range(0, W + 1, 80))}</g>
<rect x="0" y="600" width="700" height="18" fill="{BRASS}"/><rect x="1220" y="600" width="700" height="18" fill="{BRASS}"/>
<rect x="{960 - half - 260:.0f}" y="160" width="260" height="760" fill="#6e5532"/>
<rect x="{960 + half:.0f}" y="160" width="260" height="760" fill="#6e5532"/>
<rect x="{960 - half - 260:.0f}" y="160" width="260" height="760" fill="url(#doorSheen)"/>
<rect x="{960 + half:.0f}" y="160" width="260" height="760" fill="url(#doorSheen)"/>
<rect x="660" y="140" width="40" height="800" fill="#1a110a"/><rect x="1220" y="140" width="40" height="800" fill="#1a110a"/>
<rect x="660" y="130" width="600" height="30" fill="#1a110a"/>
{glow(960, 40, 300, light, 0.35)}
<rect x="760" y="20" width="400" height="16" rx="8" fill="#fff0cc" opacity="0.8"/>
'''


DOOR_SHEEN = '''<linearGradient id="doorSheen" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#000" stop-opacity="0.35"/>
<stop offset="0.5" stop-color="#ffe0a0" stop-opacity="0.12"/><stop offset="1" stop-color="#000" stop-opacity="0.35"/></linearGradient>'''

scenes = {}

# S1 — the old mountain hotel at night, four rows of windows, snow
wins = []
for row in range(4):
    for col in range(7):
        x = 610 + col * 100; y = 330 + row * 120
        if (row, col) in ((3, 2), (1, 5)):
            wins.append(lit_window(x, y, 54, 72))
        else:
            wins.append(f'<rect x="{x}" y="{y}" width="54" height="72" fill="#0a0e1a" stroke="#2e3a58" stroke-width="4"/>')
scenes["s1"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(160, 500)}
{moon(1240, 150, 54)}
<path d="M0 560 L260 330 L420 450 L640 230 L900 420 L1100 260 L1380 470 L1600 300 L1920 520 L1920 760 L0 760 Z" fill="#141a2a"/>
<path d="M640 230 L700 290 L660 285 L620 300 Z M1100 260 L1150 300 L1110 300 L1080 290 Z" fill="#c8d2e6" opacity="0.5"/>
{pines(800, 40, "#0a0e18", 140, 260)}
<rect x="580" y="250" width="760" height="560" fill="#1a2234"/><rect x="580" y="250" width="760" height="560" fill="url(#facade)"/>
<polygon points="560,256 960,150 1360,256" fill="#0b0e18"/><path d="M560 256 L960 150 L1360 256" stroke="#c8d2e6" stroke-width="8" fill="none" opacity="0.45"/>
<rect x="930" y="150" width="60" height="150" fill="#080a12"/>
<rect x="940" y="170" width="40" height="60" fill="#0d1220"/>
{"".join(wins)}
<rect x="880" y="700" width="160" height="110" fill="#1c1408"/><rect x="880" y="700" width="160" height="110" fill="#ffb54a" opacity="0.45"/>
{glow(960, 700, 120, "#ffb54a", 0.5)}
<rect x="840" y="680" width="240" height="20" fill="#080a12"/>
<rect x="830" y="590" width="260" height="56" rx="6" fill="#120806"/>
<text x="960" y="633" text-anchor="middle" font-family="{SERIF}" font-weight="bold" font-size="42" letter-spacing="10" fill="#ff4a3a">HOTEL</text>
{glow(960, 618, 140, "#ff3b2f", 0.35)}
<rect x="0" y="800" width="{W}" height="280" fill="#cdd6e6" opacity="0.18"/>
<rect x="0" y="800" width="{W}" height="280" fill="#0b0f1a" opacity="0.7"/>
{pines(1000, 10, "#05070d", 260, 420, 0, 560)}{pines(1000, 10, "#05070d", 260, 420, 1360, 1920)}
{snow(320)}
{fog(820, "#a9b6cc", 0.12)}
''', sky("sky1", "#03040a", "#0e1528", "#1d2640") + sky("facade", "#2a3450", "#1a2234", "#0e1220"))

# S2 — the brass panel: four buttons and a card taped above them
btns = "".join(
    f'<circle cx="960" cy="{780 - i * 120}" r="44" fill="#2a2016" stroke="{BRASS}" stroke-width="8"/>'
    f'<text x="960" y="{796 - i * 120}" text-anchor="middle" font-family="{SERIF}" font-size="44" fill="#e8d6a6">{i + 1}</text>'
    for i in range(4))
scenes["s2"] = svg(f'''
<rect width="{W}" height="{H}" fill="#24170e"/>
<g opacity="0.5">{"".join(f'<rect x="{x}" y="-20" width="150" height="1120" fill="none" stroke="#120b06" stroke-width="10"/>' for x in range(100, 1900, 190))}</g>
{glow(960, 0, 420, "#ffcf8a", 0.3)}
<rect x="830" y="380" width="260" height="520" rx="20" fill="#8a6326"/>
<rect x="846" y="396" width="228" height="488" rx="14" fill="{BRASS}"/>
<rect x="846" y="396" width="228" height="488" rx="14" fill="url(#doorSheen)"/>
{btns}
<circle cx="960" cy="820" r="0"/>
<g transform="rotate(-2.5 960 230)">
<rect x="690" y="80" width="560" height="290" fill="#000" opacity="0.4" filter="url(#blur8)"/>
<rect x="680" y="70" width="560" height="290" fill="#e4d8bb"/>
<rect x="680" y="58" width="90" height="34" fill="#d3c99c" opacity="0.85" transform="rotate(-20 725 75)"/>
<rect x="1150" y="58" width="90" height="34" fill="#d3c99c" opacity="0.85" transform="rotate(20 1195 75)"/>
<text x="960" y="140" text-anchor="middle" font-family="{SERIF}" font-style="italic" font-size="38" fill="#2a1d14">After midnight, if it stops</text>
<text x="960" y="192" text-anchor="middle" font-family="{SERIF}" font-style="italic" font-size="38" fill="#2a1d14">on the FIFTH floor —</text>
<text x="960" y="256" text-anchor="middle" font-family="{SERIF}" font-weight="bold" font-style="italic" font-size="40" fill="#9a1610">Don't step out.</text>
<text x="960" y="316" text-anchor="middle" font-family="{SERIF}" font-weight="bold" font-style="italic" font-size="40" fill="#9a1610">Don't let anyone in.</text>
</g>
''', DOOR_SHEEN)

# S3 — 1 a.m., the sleeping hotel corridor, ice machine humming blue
doors3 = "".join(
    f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#1a110a"/><circle cx="{x + w * .8:.0f}" cy="{y + h * .55:.0f}" r="{w * .05:.0f}" fill="{BRASS}"/>'
    for x, y, w, h in ((620, 360, 90, 300), (1210, 360, 90, 300), (760, 420, 54, 200), (1106, 420, 54, 200)))
scenes["s3"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0d0b0c"/>
<polygon points="0,0 860,380 860,700 0,1080" fill="#3a2e22"/>
<polygon points="1920,0 1060,380 1060,700 1920,1080" fill="#33281e"/>
{wallpaper(860, 380, 200, 320, "#2e2a20", "#1c1912", 0.5)}
<polygon points="0,0 860,380 1060,380 1920,0" fill="#120e0c"/>
<polygon points="0,1080 860,700 1060,700 1920,1080" fill="#2a0e0c"/>
<g opacity="0.35">{"".join(f'<line x1="960" y1="700" x2="{x}" y2="1080" stroke="#140606" stroke-width="4"/>' for x in range(-400, 2400, 160))}</g>
{doors3}
{"".join(glow(960, y, 60, "#ffcf8a", 0.4) + f'<ellipse cx="960" cy="{y}" rx="{rx}" ry="{rx * .25:.0f}" fill="#ffe2b0" opacity="0.8"/>' for y, rx in ((390, 30), (300, 50), (120, 90)))}
<rect x="430" y="380" width="220" height="460" fill="#1a2430"/>
<rect x="450" y="420" width="180" height="160" fill="#8fd4ff" opacity="0.75"/>
{glow(540, 500, 220, "#7ac8ff", 0.45)}
<rect x="470" y="620" width="140" height="80" fill="#0b1018"/>
<polygon points="430,840 650,840 760,1080 300,1080" fill="#7ac8ff" opacity="0.08"/>
<path d="M760 880 L870 880 L855 980 L775 980 Z" fill="#9aa4ae"/><path d="M760 880 Q815 840 870 880" stroke="#c9d1d8" stroke-width="6" fill="none"/>
<g fill="#e6f4ff" opacity="0.85">{"".join(f'<rect x="{770 + r.randint(0, 80)}" y="{860 + r.randint(0, 20)}" width="18" height="16" rx="3"/>' for _ in range(8))}</g>
{fog(700, "#ffcf8a", 0.05)}
''')

# S4 — the floor dial above the doors: the needle past four
labels = ""
import math
for i, ang in enumerate((200, 230, 260, 290, 320)):
    a = math.radians(ang)
    x = 960 + 300 * math.cos(a); y = 640 + 300 * math.sin(a)
    t = "L" if i == 0 else str(i)
    labels += f'<text x="{x:.0f}" y="{y + 18:.0f}" text-anchor="middle" font-family="{SERIF}" font-size="56" fill="#3a2a14">{t}</text>'
na = math.radians(345)
scenes["s4"] = svg(f'''
<rect width="{W}" height="{H}" fill="#1a110a"/>
<rect x="0" y="760" width="{W}" height="320" fill="#6e5532"/>
<rect x="0" y="760" width="{W}" height="320" fill="url(#doorSheen)"/>
<rect x="955" y="760" width="10" height="320" fill="#1a110a"/>
<path d="M560 700 A400 400 0 0 1 1360 700 Z" fill="#8a6326"/>
<path d="M600 690 A360 360 0 0 1 1320 690 Z" fill="#e8d6a6"/>
<path d="M600 690 A360 360 0 0 1 1320 690 Z" fill="url(#doorSheen)"/>
{labels}
<path d="M1220 560 A300 300 0 0 1 1270 690" stroke="#9a1610" stroke-width="10" fill="none" opacity="0.6"/>
<line x1="960" y1="660" x2="{960 + 330 * math.cos(na):.0f}" y2="{660 + 330 * math.sin(na):.0f}" stroke="#120806" stroke-width="12" stroke-linecap="round"/>
<circle cx="960" cy="660" r="30" fill="#120806"/><circle cx="960" cy="660" r="12" fill="{BRASS}"/>
{glow(1270, 600, 120, "#ff3b2f", 0.5)}
<circle cx="1360" cy="380" r="20" fill="#ff3b2f"/>{glow(1360, 380, 60, "#ff3b2f", 0.6)}
<rect x="540" y="690" width="840" height="30" fill="#5a3f1e"/>
''', DOOR_SHEEN)

# S5 — doors open on a hallway that shouldn't exist
scenes["s5"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0c0a08"/>
{fifth_hall(1000, 18)}
{cab_frame(520)}
{fog(820, "#9fb08a", 0.06)}
''', DOOR_SHEEN)

# S6 — the bellhop holding my suitcase
scenes["s6"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0c0a08"/>
{fifth_hall(985, 8)}
{bellhop(940, 900, 1.12, smile=False)}
{cab_frame(520)}
{fog(860, "#9fb08a", 0.05)}
''', DOOR_SHEEN)

# S7 — pressing close; he only smiles through the closing gap
scenes["s7"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0c0a08"/>
{fifth_hall(960, 0)}
<g transform="translate(960 900) scale(1.25) translate(-960 -900)">{bellhop(960, 900, 1.0, smile=True, suitcase=False)}</g>
{cab_frame(150)}
<rect x="1500" y="380" width="200" height="420" rx="16" fill="#8a6326"/>
<rect x="1514" y="394" width="172" height="392" rx="12" fill="{BRASS}"/>
{"".join(f'<circle cx="1600" cy="{720 - i * 90}" r="30" fill="#2a2016" stroke="#8a6326" stroke-width="6"/>' for i in range(4))}
<circle cx="1600" cy="430" r="22" fill="#ff3b2f"/>{glow(1600, 430, 50, "#ff3b2f", 0.6)}
<path d="M1920 640 C1800 600 1720 520 1660 450 C1640 425 1600 440 1612 470 C1630 520 1690 600 1760 700 L1920 760 Z" fill="#0a0706"/>
<path d="M1660 450 C1652 410 1626 400 1608 418 C1600 428 1606 444 1620 452 Z" fill="#0a0706"/>
''', DOOR_SHEEN)

# S8 / S8b — back down at four, doors open on my ordinary hallway... not alone
for name, twist in (("s8", False), ("s8b", True)):
    fig = ""
    if twist:
        fig = (f'<g transform="translate(700 1110) scale(1.5) translate(-700 -1110)">{bellhop(700, 1110, 1.0, smile=True, gesture=True)}</g>'
               f'<g transform="translate(560 960)"><rect x="0" y="0" width="190" height="140" rx="12" fill="#5a3a22"/><rect x="0" y="62" width="190" height="7" fill="#3a2414"/>'
               f'<rect x="30" y="4" width="18" height="22" fill="{BRASS}"/><rect x="142" y="4" width="18" height="22" fill="{BRASS}"/></g>'
               + glow(700, 270, 120, "#ff3b2f", 0.18))
    scenes[name] = svg(f'''
<rect width="{W}" height="{H}" fill="#0c0a08"/>
<rect x="700" y="160" width="520" height="760" fill="#3a2e22"/>
{wallpaper(700, 160, 520, 760, "#3a2e22", "#241c14", 0.45)}
<polygon points="700,160 860,330 860,700 700,920" fill="#000" opacity="0.35"/>
<polygon points="1220,160 1060,330 1060,700 1220,920" fill="#000" opacity="0.35"/>
<polygon points="700,920 860,700 1060,700 1220,920" fill="#2a0e0c"/>
<rect x="860" y="330" width="200" height="370" fill="#2a2018"/>
{glow(960, 260, 140, "#ffcf8a", 0.45)}
<ellipse cx="960" cy="250" rx="40" ry="10" fill="#ffe2b0"/>
{cab_frame(520)}
<rect x="900" y="60" width="120" height="70" rx="8" fill="#120806"/>
<text x="960" y="115" text-anchor="middle" font-family="{SERIF}" font-weight="bold" font-size="56" fill="#ffb54a">4</text>
{glow(960, 95, 60, "#ffb54a", 0.4)}
<rect x="0" y="0" width="{W}" height="{H}" fill="#000" opacity="{0.25 if twist else 0}"/>
{fig}
''', DOOR_SHEEN)

for n, s in scenes.items():
    save(n, s)
