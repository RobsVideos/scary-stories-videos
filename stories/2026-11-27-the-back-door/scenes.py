"""Scenes for The Back Door (a dark country school-bus route and a knock on the rear emergency door)."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

BUS = "#b88a1e"      # school-bus yellow, dimmed for night
BUS_D = "#7a5a12"
BUS_DD = "#3d2c08"
RED = "#ff2f22"
WARM = "#ffc46a"
HAND = "Comic Relief, DejaVu Sans, sans-serif"

DAWN = sky("dawn", "#03040a", "#111a30", "#3a3550")
_svg = svg


def svg(body, defs=""):
    return _svg(body, defs + '<filter id="bb30" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="30"/></filter>')


def gl(cx, cy, r, color, op=0.6):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" opacity="{op}" filter="url(#bb30)"/>'


def frost(n, y0, y1, op=0.35):
    return "".join(f'<circle cx="{rnd.randint(0, W)}" cy="{rnd.randint(y0, y1)}" r="{rnd.choice([1, 1.5, 2])}" '
                   f'fill="#cfd8ee" opacity="{rnd.uniform(0.1, op):.2f}"/>' for _ in range(n))


def fence(y, col="#07080e", x0=0, x1=W, step=110):
    posts = "".join(f'<rect x="{x}" y="{y - 60}" width="9" height="66" fill="{col}"/>' for x in range(x0, x1, step))
    return posts + f'<line x1="{x0}" y1="{y - 46}" x2="{x1}" y2="{y - 46}" stroke="{col}" stroke-width="3"/>' \
                   f'<line x1="{x0}" y1="{y - 24}" x2="{x1}" y2="{y - 24}" stroke="{col}" stroke-width="3"/>'


def bus_side(x, y, s=1.0, lit=True, door_open=False):
    """Side view of a school bus, front facing right. (x, y) = rear-bottom corner at the wheels' baseline."""
    L, Hh = 820 * s, 250 * s
    o = [f'<g transform="translate({x} {y})">']
    # body
    o.append(f'<path d="M0 {-30*s} L0 {-Hh} Q0 {-Hh-22*s} {30*s} {-Hh-22*s} L{L-150*s} {-Hh-22*s} Q{L-120*s} {-Hh-22*s} {L-110*s} {-Hh+10*s} '
             f'L{L-100*s} {-150*s} L{L} {-135*s} Q{L+14*s} {-130*s} {L+14*s} {-110*s} L{L+14*s} {-30*s} Z" fill="{BUS}"/>')
    o.append(f'<path d="M0 {-30*s} L{L+14*s} {-30*s} L{L+14*s} {-60*s} L0 {-60*s} Z" fill="{BUS_DD}"/>')
    o.append(f'<rect x="0" y="{-118*s}" width="{L-100*s}" height="{8*s}" fill="#111"/>')
    o.append(f'<rect x="0" y="{-98*s}" width="{L-100*s}" height="{6*s}" fill="#111"/>')
    # windows
    for i in range(8):
        wx = 34 * s + i * 76 * s
        fill = "#ffcf7a" if lit else "#0c1020"
        o.append(f'<rect x="{wx}" y="{-Hh+8*s}" width="{60*s}" height="{70*s}" rx="{6*s}" fill="{fill}" opacity="{0.85 if lit else 1}"/>')
        o.append(f'<line x1="{wx}" y1="{-Hh+40*s}" x2="{wx+60*s}" y2="{-Hh+40*s}" stroke="#2a1e06" stroke-width="{4*s}"/>')
        if lit and i in (1, 3, 4, 6):
            o.append(f'<ellipse cx="{wx+30*s}" cy="{-Hh+62*s}" rx="{14*s}" ry="{16*s}" fill="#3a2a10" opacity="0.8"/>')
    # door
    dx = L - 165 * s
    dcol = "#ffd889" if door_open else "#151a28"
    o.append(f'<rect x="{dx}" y="{-Hh+2*s}" width="{55*s}" height="{Hh-40*s}" fill="{dcol}"/>')
    o.append(f'<line x1="{dx+27*s}" y1="{-Hh+2*s}" x2="{dx+27*s}" y2="{-38*s}" stroke="#2a1e06" stroke-width="{4*s}"/>')
    # windshield + hood
    o.append(f'<path d="M{L-104*s} {-Hh+10*s} L{L-96*s} {-160*s} L{L-40*s} {-150*s} L{L-60*s} {-Hh+5*s} Z" fill="#1a2238"/>')
    # stop arm and red lights
    o.append(f'<circle cx="{L-180*s}" cy="{-Hh-12*s}" r="{8*s}" fill="{RED}"/>')
    o.append(f'<circle cx="{16*s}" cy="{-Hh-12*s}" r="{8*s}" fill="{RED}"/>')
    # wheels
    for wx in (130 * s, L - 140 * s):
        o.append(f'<circle cx="{wx}" cy="{-30*s}" r="{48*s}" fill="#07070a"/><circle cx="{wx}" cy="{-30*s}" r="{18*s}" fill="#2c2c33"/>')
    # headlight
    o.append(f'<rect x="{L+4*s}" y="{-110*s}" width="{12*s}" height="{20*s}" fill="#fff6d8"/>')
    o.append('</g>')
    return "".join(o)


scenes = {}

# S1 — bus on a dark country road before sunrise (lines 0-1)
beam = '<polygon points="1395,742 1920,640 1920,900 1395,770" fill="#fff2c8" opacity="0.18" filter="url(#blur8)"/>'
scenes["s1"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#dawn)"/>
{stars(150, 520, 0.6)}
<ellipse cx="960" cy="690" rx="1200" ry="90" fill="#6a4a5a" opacity="0.25" filter="url(#blur60)"/>
<path d="M0 690 C300 670 620 660 960 680 C1300 700 1600 660 1920 675 L1920 1080 L0 1080Z" fill="#0e1220"/>
{"".join(f'<ellipse cx="{x}" cy="{665 + (x % 7) * 2}" rx="{70 + x % 40}" ry="{40 + x % 20}" fill="#080a14"/>' for x in range(40, 1920, 150))}
{dead_tree(250, 760, 380, "#06070d", 0.9)}
{dead_tree(1720, 760, 300, "#06070d", 0.8)}
{frost(260, 760, 1080)}
<path d="M0 790 L1920 760 L1920 860 L0 900Z" fill="#141826"/>
<path d="M0 845 L1920 812" stroke="#4a4f5f" stroke-width="4" stroke-dasharray="40 40"/>
{fence(760, "#05060b")}
{beam}
{bus_side(560, 830, 1.0, lit=True)}
{gl(1420, 735, 60, "#fff2c8", 0.5)}
{grass(1080, 300, "#06070c", (20, 50))}
{fog(760, "#9aa3c0", 0.16, 90)}
''', DAWN)

# S2 — the driver's mirror with the scratched rule (lines 1-2)
scenes["s2"] = svg(f'''
<rect width="{W}" height="{H}" fill="#07080d"/>
<rect x="0" y="0" width="{W}" height="300" fill="#12131a"/>
{"".join(f'<circle cx="{x}" cy="150" r="6" fill="#26272f"/>' for x in range(100, 1920, 220))}
<path d="M0 560 L1920 560 L1920 1080 L0 1080Z" fill="#0b0c12"/>
<!-- windshield view: road in headlights -->
<path d="M120 300 L1800 300 L1800 600 L120 600Z" fill="#0a0f1d"/>
<path d="M760 600 L940 360 L980 360 L1160 600Z" fill="#2a2a2c" opacity="0.7"/>
<path d="M960 600 L960 360" stroke="#c9b46a" stroke-width="4" stroke-dasharray="30 26" opacity="0.6"/>
<ellipse cx="960" cy="560" rx="420" ry="120" fill="#fff0c0" opacity="0.12" filter="url(#blur60)"/>
<!-- mirror -->
<rect x="940" y="270" width="40" height="70" fill="#1c1d24"/>
<rect x="640" y="120" width="640" height="200" rx="30" fill="#2b2d36"/>
<rect x="660" y="138" width="600" height="164" rx="22" fill="#141a2a"/>
<!-- aisle in the mirror: dim seats -->
<path d="M720 300 L860 160 L1060 160 L1200 300Z" fill="#0c101c"/>
{"".join(f'<rect x="{700 + i*18}" y="{170 + i*24}" width="{90 - i*6}" height="{18}" fill="#3a2418" opacity="0.8"/><rect x="{1130 - i*18 - (90 - i*6) + 90}" y="{170 + i*24}" width="{90 - i*6}" height="18" fill="#3a2418" opacity="0.8"/>' for i in range(5))}
<rect x="935" y="160" width="50" height="40" fill="{RED}" opacity="0.5"/>
<rect x="660" y="138" width="600" height="164" rx="22" fill="#9fb4e8" opacity="0.07"/>
<!-- scratched note on the sun visor -->
<rect x="580" y="345" width="760" height="230" rx="14" fill="#2a241c"/>
<rect x="580" y="345" width="760" height="230" rx="14" fill="none" stroke="#14110c" stroke-width="6"/>
<text x="960" y="410" text-anchor="middle" font-family="{HAND}" font-size="44" fill="#d9cdb0" opacity="0.9">IF IT KNOCKS ON</text>
<text x="960" y="470" text-anchor="middle" font-family="{HAND}" font-size="44" fill="#d9cdb0" opacity="0.9">THE BACK DOOR...</text>
<text x="960" y="535" text-anchor="middle" font-family="{HAND}" font-size="44" fill="#ff6a55" opacity="0.9">DON'T STOP. DON'T LOOK.</text>
<!-- steering wheel -->
<circle cx="960" cy="1060" r="330" fill="none" stroke="#050507" stroke-width="56"/>
<rect x="930" y="760" width="60" height="320" fill="#050507"/>
<circle cx="960" cy="1060" r="80" fill="#050507"/>
{gl(960, 435, 400, "#ffd28a", 0.06)}
''', DAWN)

# S3 — morning stop at a frosty farm, kids boarding (line 3)
kids = "".join(f'<g fill="#06060a"><circle cx="{x}" cy="{748 - hh}" r="{hh*0.16:.0f}"/><rect x="{x - hh*0.17:.0f}" y="{748 - hh*0.84:.0f}" width="{hh*0.34:.0f}" height="{hh*0.84:.0f}" rx="{hh*0.1:.0f}"/>'
               f'<rect x="{x - hh*0.24:.0f}" y="{748 - hh*0.78:.0f}" width="{hh*0.14:.0f}" height="{hh*0.38:.0f}" rx="6" fill="#2a1210"/></g>' for x, hh in ((1190, 120), (1260, 100), (1330, 130)))
scenes["s3"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#dawn)"/>
{stars(80, 420, 0.5)}
<path d="M0 640 C400 610 900 630 1920 600 L1920 1080 L0 1080Z" fill="#0f1322"/>
<g fill="#07080e">
<polygon points="1450,640 1450,430 1590,350 1730,430 1730,640"/>
<polygon points="1730,640 1730,500 1860,500 1860,640"/>
<rect x="1620" y="350" width="26" height="70"/>
</g>
{lit_window(1530, 470, 46, 62, WARM)}
{gl(1790, 520, 40, WARM, 0.5)}
<circle cx="1790" cy="520" r="8" fill="{WARM}"/>
{frost(300, 640, 1080, 0.4)}
<path d="M0 760 L1920 740 L1920 850 L0 870Z" fill="#161a28"/>
{bus_side(260, 800, 1.05, lit=True, door_open=True)}
<polygon points="1080,600 1180,600 1260,760 1000,760" fill="#ffd889" opacity="0.18" filter="url(#blur8)"/>
{kids}
<g fill="#07080e"><rect x="1400" y="650" width="10" height="100"/><rect x="1380" y="620" width="60" height="36" rx="12"/></g>
{grass(1080, 260, "#06070c", (20, 46))}
{fog(700, "#9aa3c0", 0.14, 80)}
''', DAWN)

# S4 — inside, looking down the aisle at the rear emergency door (lines 4-6)
def aisle(heads=True, knock=False):
    seats = []
    for i in range(6):
        t = i / 5
        y = 980 - t * 470
        w = 560 - t * 380
        hgt = 130 - t * 80
        lx = 960 - 120 + t * 60 - w - 40 * (1 - t)
        rx = 960 + 120 - t * 60 + 40 * (1 - t)
        for sx in (lx, rx):
            seats.append(f'<rect x="{sx:.0f}" y="{y - hgt:.0f}" width="{w:.0f}" height="{hgt:.0f}" rx="{16 - t*8:.0f}" fill="#3a1e14"/>'
                         f'<rect x="{sx:.0f}" y="{y - hgt:.0f}" width="{w:.0f}" height="{hgt*0.18:.0f}" rx="8" fill="#55301f"/>')
            if heads and i in (1, 2, 4) and sx == (lx if i != 2 else rx):
                r = 46 - t * 26
                seats.append(f'<circle cx="{sx + w*0.5:.0f}" cy="{y - hgt - r*0.7:.0f}" r="{r:.0f}" fill="#08080c"/>')
    return "".join(reversed(seats))


def back_view(heads=True, red_op=0.85, prints=False):
    p = ""
    if prints:
        p = "".join(f'<ellipse cx="{x}" cy="{y}" rx="16" ry="22" fill="#bcc6dc" opacity="0.25"/>' for x, y in ((925, 300), (990, 290), (958, 350)))
    return svg(f'''
<rect width="{W}" height="{H}" fill="#08090e"/>
<polygon points="0,0 700,180 700,560 0,1080" fill="#14161f"/>
<polygon points="1920,0 1220,180 1220,560 1920,1080" fill="#14161f"/>
<polygon points="0,0 1920,0 1220,180 700,180" fill="#0d0e14"/>
{"".join(f'<line x1="{x}" y1="{180 - (700 - x)*180/700:.0f}" x2="{1920 - x}" y2="{180 - (700 - x)*180/700:.0f}" stroke="#1d1f29" stroke-width="5"/>' for x in range(100, 700, 140))}
<!-- side windows: black, frosted -->
{"".join(f'<polygon points="{x},{220 - (700 - x)*0.26:.0f} {x+90 - (700-x)*0.05:.0f},{224 - (610 - x)*0.26:.0f} {x+90:.0f},{360 + (610-x)*0.3:.0f} {x},{360 + (700-x)*0.3:.0f}" fill="#0a0e1c"/>' for x in (120, 320, 500))}
{"".join(f'<polygon points="{1920-x},{220 - (700 - x)*0.26:.0f} {1920-x-90 + (700-x)*0.05:.0f},{224 - (610 - x)*0.26:.0f} {1920-x-90:.0f},{360 + (610-x)*0.3:.0f} {1920-x},{360 + (700-x)*0.3:.0f}" fill="#0a0e1c"/>' for x in (120, 320, 500))}
<polygon points="0,1080 700,560 1220,560 1920,1080" fill="#101119"/>
<polygon points="840,1080 900,560 1020,560 1080,1080" fill="#1b1c24"/>
<!-- emergency door -->
<rect x="830" y="200" width="260" height="360" fill="#1a1c24"/>
<rect x="852" y="222" width="216" height="170" fill="#04060c"/>
<rect x="852" y="222" width="216" height="170" fill="#7d8fbf" opacity="0.07"/>
{p}
<rect x="860" y="440" width="200" height="16" rx="6" fill="#55575f"/>
<rect x="1020" y="420" width="40" height="56" rx="8" fill="#6e6f77"/>
<rect x="880" y="160" width="160" height="32" rx="4" fill="#2a0806"/>
<text x="960" y="185" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="22" fill="{RED}" opacity="{red_op}">EMERGENCY EXIT</text>
{gl(960, 176, 120, RED, 0.35 * red_op)}
<rect x="830" y="200" width="260" height="360" fill="{RED}" opacity="0.05"/>
{aisle(heads)}
<ellipse cx="960" cy="900" rx="700" ry="120" fill="#ffb060" opacity="0.05" filter="url(#blur60)"/>
''')

scenes["s4"] = back_view(heads=True)
scenes["s4b"] = back_view(heads=True, red_op=1.0, prints=True)

# S5 — the driver's white-knuckle hands, eyes on the road (lines 7-9)
scenes["s5"] = svg(f'''
<rect width="{W}" height="{H}" fill="#05060a"/>
<path d="M0 0 L1920 0 L1920 640 L0 640Z" fill="#0a0f1e"/>
{stars(50, 220, 0.4)}
<path d="M0 470 C500 450 1400 450 1920 470 L1920 640 L0 640Z" fill="#0d1120"/>
{"".join(f'<ellipse cx="{x}" cy="460" rx="60" ry="34" fill="#070912"/>' for x in range(0, 1920, 120))}
<path d="M640 640 L940 470 L980 470 L1280 640Z" fill="#26272c"/>
<path d="M960 640 L960 472" stroke="#c9b46a" stroke-width="5" stroke-dasharray="34 30" opacity="0.7"/>
<ellipse cx="960" cy="600" rx="500" ry="120" fill="#fff0c0" opacity="0.14" filter="url(#blur60)"/>
{fog(500, "#8e97b6", 0.15, 60)}
<rect x="0" y="620" width="{W}" height="460" fill="#0a0b10"/>
<rect x="0" y="0" width="{W}" height="60" fill="#07080c"/>
<!-- mirror, top: dark, unlooked-at -->
<rect x="1380" y="70" width="360" height="120" rx="20" fill="#24262e"/>
<rect x="1394" y="82" width="332" height="96" rx="14" fill="#03040a"/>
<rect x="1540" y="100" width="40" height="28" fill="{RED}" opacity="0.35"/>
<!-- wheel and hands -->
<circle cx="960" cy="1020" r="420" fill="none" stroke="#030304" stroke-width="64"/>
<rect x="920" y="660" width="80" height="420" fill="#030304"/>
<g fill="#3a2a22">
<path d="M520 720 C540 660 640 640 680 690 C700 720 690 780 650 800 C600 820 530 800 520 720Z"/>
<path d="M1400 720 C1380 660 1280 640 1240 690 C1220 720 1230 780 1270 800 C1320 820 1390 800 1400 720Z"/>
</g>
<g stroke="#5a4236" stroke-width="5" fill="none" opacity="0.8">
<path d="M560 700 q30 -20 60 -4"/><path d="M560 730 q30 -18 62 -2"/><path d="M566 760 q28 -14 56 0"/>
<path d="M1360 700 q-30 -20 -60 -4"/><path d="M1360 730 q-30 -18 -62 -2"/><path d="M1354 760 q-28 -14 -56 0"/>
</g>
<g fill="#100c0e"><rect x="300" y="760" width="260" height="120" rx="50" transform="rotate(-18 430 820)"/>
<rect x="1360" y="760" width="260" height="120" rx="50" transform="rotate(18 1490 820)"/></g>
''')

# S6 — the bus parked at school, pale dawn (line 10)
scenes["s6"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#dawn2)"/>
{stars(40, 260, 0.35)}
<path d="M0 640 L1920 640 L1920 1080 L0 1080Z" fill="#11141f"/>
<g fill="#090b13">
<rect x="160" y="360" width="1100" height="290"/>
<polygon points="560,360 710,250 860,360"/>
<rect x="680" y="200" width="60" height="70"/>
</g>
{"".join(lit_window(x, 420, 64, 80, "#d9c48a") if x in (260, 980) else f'<rect x="{x}" y="420" width="64" height="80" fill="#151a2c"/>' for x in range(220, 1220, 120))}
<rect x="660" y="520" width="100" height="130" fill="#1a1d28"/>
{gl(710, 520, 50, WARM, 0.4)}
<path d="M0 720 L1920 700 L1920 820 L0 840Z" fill="#191c28"/>
{bus_side(900, 800, 1.0, lit=False, door_open=True)}
<polygon points="1570,560 1625,560 1700,760 1480,760" fill="#ffd889" opacity="0.12" filter="url(#blur8)"/>
{"".join(f'<g fill="#07070b"><circle cx="{x}" cy="{690 - h}" r="{h*0.16:.0f}"/><rect x="{x - h*0.17:.0f}" y="{690 - h*0.84:.0f}" width="{h*0.34:.0f}" height="{h*0.84:.0f}" rx="{h*0.1:.0f}"/></g>' for x, h in ((640, 90), (720, 80), (800, 96), (560, 84)))}
{frost(160, 720, 1080, 0.3)}
{fog(700, "#a6aec8", 0.12, 70)}
''', sky("dawn2", "#0a0d1a", "#2a2f4c", "#6a5566"))

# S7 — the last little girl on the steps, looking back down the aisle (lines 11-12)
scenes["s7"] = svg(f'''
<rect width="{W}" height="{H}" fill="#07080d"/>
<!-- open door frame, pale dawn outside -->
<rect x="500" y="120" width="420" height="900" fill="url(#dawn2)"/>
<rect x="500" y="120" width="420" height="900" fill="#8a7a8a" opacity="0.15"/>
<rect x="470" y="100" width="30" height="940" fill="#1b1c22"/><rect x="920" y="100" width="30" height="940" fill="#1b1c22"/>
<rect x="470" y="100" width="480" height="30" fill="#1b1c22"/>
<!-- steps -->
<path d="M500 820 L920 820 L920 860 L500 860Z" fill="#23242c"/>
<path d="M500 920 L920 920 L920 960 L500 960Z" fill="#23242c"/>
<path d="M500 860 L920 860 L920 920 L500 920Z" fill="#14151b"/>
<path d="M500 960 L920 960 L920 1080 L500 1080Z" fill="#0f1015"/>
<rect x="490" y="820" width="440" height="8" fill="{BUS_D}"/>
<!-- handrail -->
<path d="M960 300 L960 880" stroke="#5a5c66" stroke-width="16" stroke-linecap="round"/>
<!-- girl: small, turned, looking back up and over her shoulder -->
<g fill="#050508">
<path d="M660 820 L650 640 C640 590 680 560 720 560 C760 560 800 590 790 640 L780 820Z"/>
<circle cx="725" cy="510" r="58"/>
<path d="M670 500 C660 560 640 600 630 640 L660 640 C670 600 680 560 690 520Z"/>
<path d="M780 500 C800 560 810 600 815 640 L790 640 C785 600 775 560 760 520Z"/>
<rect x="650" y="600" width="60" height="120" rx="14" fill="#3a1414"/>
</g>
<ellipse cx="745" cy="500" rx="10" ry="6" fill="#cfd6ea" opacity="0.5"/>
<!-- the aisle she is looking down (right): dark, empty, red glow far back -->
<path d="M950 100 L1920 0 L1920 1080 L950 1080Z" fill="#0b0c12"/>
<path d="M1100 1080 L1500 560 L1620 560 L1920 900 L1920 1080Z" fill="#121319"/>
{"".join(f'<rect x="{1180 + i*70:.0f}" y="{700 - i*40:.0f}" width="{150 - i*18}" height="{110 - i*12}" rx="10" fill="#2e1810"/>' for i in range(5))}
{gl(1600, 520, 90, RED, 0.45)}
<rect x="1570" y="500" width="70" height="20" fill="{RED}" opacity="0.8"/>
<rect x="1540" y="530" width="130" height="200" fill="#04050a"/>
''', sky("dawn2", "#0a0d1a", "#2a2f4c", "#6a5566"))

# S8 — the very back seat: something sitting there in the red light (line 13)
s8 = back_view(heads=False, red_op=1.0, prints=True)
shape = (f'<g>{gl(960, 460, 150, RED, 0.15)}'
         f'<path d="M880 560 L890 430 C890 380 920 350 960 350 C1000 350 1030 380 1030 430 L1040 560Z" fill="#020203"/>'
         f'<ellipse cx="960" cy="330" rx="46" ry="56" fill="#020203"/>'
         f'<path d="M1040 470 C1060 440 1070 410 1080 395" stroke="#020203" stroke-width="18" stroke-linecap="round" fill="none"/>'
         f'<circle cx="1082" cy="390" r="16" fill="#020203"/>'
         f'{eyes(960, 330, 30, 6)}</g>')
scenes["s8"] = s8.replace('<rect x="860" y="440"', shape + '<rect x="860" y="440"', 1)

for name, m in scenes.items():
    save(name, m)
print("drew", ", ".join(scenes))
