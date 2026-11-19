"""Scenes for 'The Tent Count' — a pine campground, a ranger's rule, a tent zipper at 2 a.m., and one head too many."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

r = random.Random(1119)

FIRE = "#ff8a2a"
EMBER = "#d2361c"
MOONBLUE = "#9fb6e6"


def pine(x, base, h, color="#070a10", w=None):
    """A layered pine silhouette rooted at (x, base)."""
    w = w or h * 0.42
    tiers = []
    for i in range(5):
        top = base - h + i * h * 0.17
        bot = top + h * 0.32
        ww = w * (0.35 + i * 0.17)
        tiers.append(f'<polygon points="{x},{top:.0f} {x + ww / 2:.0f},{bot:.0f} {x + ww * .18:.0f},{bot - 8:.0f} '
                     f'{x - ww * .18:.0f},{bot - 8:.0f} {x - ww / 2:.0f},{bot:.0f}"/>')
    return (f'<g fill="{color}">{"".join(tiers)}'
            f'<rect x="{x - h * .025:.0f}" y="{base - h * .2:.0f}" width="{h * .05:.0f}" height="{h * .2:.0f}"/></g>')


def treeline(base, n, hmin, hmax, color, x0=-80, x1=2000):
    return "".join(pine(r.randint(x0, x1), base + r.randint(-10, 10), r.randint(hmin, hmax), color) for _ in range(n))


def tent(x, base, w, h, body="#2b3a3a", shade="#16201f", glow=None, door_open=0.0, door_color="#0a0d0f"):
    """A side-on A-frame tent. glow = interior light color; door_open 0..1 = how much the front flap is unzipped."""
    out = (f'<polygon points="{x - w / 2},{base} {x},{base - h} {x + w / 2},{base}" fill="{body}"/>'
           f'<polygon points="{x},{base - h} {x + w / 2},{base} {x + w * .12:.0f},{base}" fill="{shade}" opacity="0.8"/>'
           f'<line x1="{x}" y1="{base - h}" x2="{x}" y2="{base - h - 26}" stroke="#0b0b0b" stroke-width="6"/>'
           f'<line x1="{x}" y1="{base - h - 20}" x2="{x - w * .7:.0f}" y2="{base + 6}" stroke="#4a4a44" stroke-width="2" opacity="0.6"/>'
           f'<line x1="{x}" y1="{base - h - 20}" x2="{x + w * .7:.0f}" y2="{base + 6}" stroke="#4a4a44" stroke-width="2" opacity="0.6"/>')
    if glow:
        out += (f'<polygon points="{x - w / 2},{base} {x},{base - h} {x + w / 2},{base}" fill="{glow}" opacity="0.35"/>'
                f'<polygon points="{x - w / 2},{base} {x},{base - h} {x + w / 2},{base}" fill="{glow}" opacity="0.35" filter="url(#blur30)"/>')
    # front door: zipper seam down the middle
    dh = h * 0.78
    out += f'<line x1="{x}" y1="{base - dh:.0f}" x2="{x}" y2="{base}" stroke="#0d1212" stroke-width="4"/>'
    if door_open > 0:
        oh = dh * door_open
        out += (f'<path d="M{x} {base - dh:.0f} C{x - 30} {base - dh + oh * .4:.0f} {x - 60} {base - dh + oh:.0f} {x - w * .22:.0f} {base} '
                f'L{x + w * .22:.0f} {base} C{x + 60} {base - dh + oh:.0f} {x + 30} {base - dh + oh * .4:.0f} {x} {base - dh:.0f}Z" fill="{door_color}"/>')
    return out


def sitter(x, base, s=1.0, color="#050407", lean=0):
    """A person sitting on a log, seen from behind/side, silhouette."""
    return (f'<g fill="{color}" transform="rotate({lean} {x} {base})">'
            f'<path d="M{x - 48 * s:.0f} {base} C{x - 56 * s:.0f} {base - 90 * s:.0f} {x - 40 * s:.0f} {base - 150 * s:.0f} {x:.0f} {base - 158 * s:.0f} '
            f'C{x + 40 * s:.0f} {base - 150 * s:.0f} {x + 56 * s:.0f} {base - 90 * s:.0f} {x + 48 * s:.0f} {base}Z"/>'
            f'<circle cx="{x}" cy="{base - 190 * s:.0f}" r="{32 * s:.0f}"/></g>')


def campfire(x, base, s=1.0, lit=True):
    logs = (f'<g fill="#1a0e08"><rect x="{x - 70 * s:.0f}" y="{base - 16 * s:.0f}" width="{140 * s:.0f}" height="{18 * s:.0f}" rx="8" transform="rotate(14 {x} {base})"/>'
            f'<rect x="{x - 70 * s:.0f}" y="{base - 16 * s:.0f}" width="{140 * s:.0f}" height="{18 * s:.0f}" rx="8" transform="rotate(-14 {x} {base})"/></g>'
            + "".join(f'<circle cx="{x + dx * s:.0f}" cy="{base + 8}" r="{14 * s:.0f}" fill="#1c1c22"/>' for dx in (-110, -80, 80, 110, -40, 40)))
    if lit:
        flame = (f'<path d="M{x - 45 * s:.0f} {base - 8} C{x - 55 * s:.0f} {base - 70 * s:.0f} {x - 10 * s:.0f} {base - 90 * s:.0f} {x:.0f} {base - 160 * s:.0f} '
                 f'C{x + 18 * s:.0f} {base - 100 * s:.0f} {x + 60 * s:.0f} {base - 80 * s:.0f} {x + 45 * s:.0f} {base - 8}Z" fill="{FIRE}"/>'
                 f'<path d="M{x - 22 * s:.0f} {base - 8} C{x - 26 * s:.0f} {base - 50 * s:.0f} {x:.0f} {base - 60 * s:.0f} {x + 4 * s:.0f} {base - 100 * s:.0f} '
                 f'C{x + 14 * s:.0f} {base - 60 * s:.0f} {x + 30 * s:.0f} {base - 50 * s:.0f} {x + 22 * s:.0f} {base - 8}Z" fill="#ffd36b"/>')
        return glow(x, base - 60 * s, 260 * s, FIRE, 0.45) + logs + flame + glow(x, base - 60 * s, 90 * s, "#ffc35a", 0.5)
    coals = "".join(f'<circle cx="{x + r.randint(-50, 50) * s:.0f}" cy="{base - r.randint(0, 14)}" r="{r.randint(5, 10) * s:.0f}" fill="{EMBER}"/>' for _ in range(18))
    return glow(x, base - 10, 120 * s, EMBER, 0.45) + logs + coals


NIGHT = sky("night", "#04060d", "#121a2e", "#22283d")
DUSK = sky("dusk", "#0a0b1c", "#2b2245", "#5a2f3e")
scenes = {}

# S1 — Pine Hollow campground at dusk
scenes["s1"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#dusk)"/>
{stars(140, 520, 0.6)}
{moon(1380, 230, 80)}
{treeline(760, 40, 260, 420, "#120f22")}
<rect x="0" y="740" width="{W}" height="40" fill="#120f22"/>
<path d="M300 790 C700 760 1200 770 1650 790 L1650 820 L300 820Z" fill="#3a3c5c" opacity="0.6"/>
<path d="M300 790 C700 760 1200 770 1650 790" stroke="#8890b8" stroke-width="3" fill="none" opacity="0.5"/>
{treeline(820, 26, 380, 560, "#0a0912", x0=-100, x1=520)}{treeline(820, 22, 380, 560, "#0a0912", x0=1420, x1=2020)}
<path d="M0 820 C500 800 1400 805 1920 820 L1920 1080 L0 1080Z" fill="#0c0b14"/>
<g fill="#06050a">
<path d="M560 880 h300 l-20 -50 c-10 -20 -30 -30 -50 -30 h-150 c-20 0 -40 10 -50 30z"/>
<rect x="540" y="860" width="340" height="44" rx="12"/>
<circle cx="610" cy="908" r="26"/><circle cx="810" cy="908" r="26"/>
</g>
<rect x="640" y="818" width="62" height="34" fill="#2a2440"/><rect x="712" y="818" width="62" height="34" fill="#2a2440"/>
{tent(1180, 900, 300, 220, glow="#ffa645")}
{campfire(960, 930, 0.6)}
{fog(800, "#b9a8c8", 0.12)}
{grass(1080, 260, "#08070d", (20, 46))}
''', DUSK)

# S2 — the ranger booth at the gate
booth = f'''
<rect x="700" y="420" width="420" height="440" fill="#1d1512"/>
<g stroke="#120c0a" stroke-width="3">{''.join(f'<line x1="700" y1="{y}" x2="1120" y2="{y}"/>' for y in range(440, 860, 28))}</g>
<polygon points="660,430 910,300 1160,430" fill="#0c0908"/>
{lit_window(760, 500, 300, 190, "#ffbb5c")}
<g fill="#100a08">
<ellipse cx="900" cy="560" rx="38" ry="44"/>
<ellipse cx="900" cy="520" rx="96" ry="14"/><path d="M866 520 c0 -40 68 -40 68 0z"/>
<path d="M830 690 C830 620 860 600 900 600 C940 600 970 620 970 690Z"/>
</g>
<rect x="756" y="690" width="308" height="14" fill="#0c0908"/>'''
gate = f'''
<rect x="1150" y="720" width="40" height="140" fill="#0c0b10"/>
<g transform="rotate(0 1170 735)"><rect x="1170" y="722" width="640" height="26" fill="#d8d2c2"/>
{''.join(f'<rect x="{x}" y="722" width="40" height="26" fill="#b3261e"/>' for x in range(1210, 1800, 90))}</g>'''
sign = f'''
<rect x="420" y="560" width="16" height="300" fill="#140d09"/><rect x="600" y="560" width="16" height="300" fill="#140d09"/>
<rect x="380" y="560" width="280" height="130" rx="8" fill="#3b2416"/>
<rect x="392" y="572" width="256" height="106" rx="6" fill="none" stroke="#5c3a22" stroke-width="4"/>
<text x="520" y="616" text-anchor="middle" font-family="{SERIF}" font-weight="bold" font-size="34" fill="#d9c79c" letter-spacing="3">PINE</text>
<text x="520" y="660" text-anchor="middle" font-family="{SERIF}" font-weight="bold" font-size="34" fill="#d9c79c" letter-spacing="3">HOLLOW</text>'''
scenes["s2"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(160, 450)}
{treeline(860, 46, 380, 620, "#0a0d14")}
<path d="M0 860 L1920 860 L1920 1080 L0 1080Z" fill="#111015"/>
<polygon points="760,1080 1160,1080 1020,860 900,860" fill="#1d1b20"/>
{glow(910, 600, 380, "#ffaa4a", 0.18)}
{booth}{gate}{sign}
<polygon points="760,704 1060,704 1180,1080 640,1080" fill="#ffbb5c" opacity="0.07"/>
{fog(900, "#9aa3b8", 0.12)}
{grass(1080, 220, "#07070b", (20, 46))}
''', NIGHT)

# S3 — four friends around the campfire, laughing
scenes["s3"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(150, 420)}
{treeline(760, 50, 420, 680, "#080a10")}
<path d="M0 760 C500 740 1400 745 1920 760 L1920 1080 L0 1080Z" fill="#0d0c12"/>
{tent(1230, 790, 360, 260, body="#25302f")}
{campfire(960, 900, 1.0)}
<g fill="#ff8a2a" opacity="0.14">{''.join(f'<ellipse cx="{x}" cy="{y}" rx="130" ry="40" filter="url(#blur30)"/>' for x, y in ((700, 950), (1220, 950)))}</g>
<rect x="580" y="925" width="260" height="34" rx="16" fill="#140c08"/><rect x="1080" y="925" width="260" height="34" rx="16" fill="#140c08"/>
{sitter(650, 930, 1.0, lean=-6)}{sitter(770, 930, 0.92, lean=8)}
{sitter(1150, 930, 0.95, lean=-8)}{sitter(1270, 930, 1.02, lean=6)}
<g fill="#ffb054" opacity="0.5">{''.join(f'<circle cx="{960 + r.randint(-60, 60)}" cy="{r.randint(560, 760)}" r="{r.choice([2, 3])}"/>' for _ in range(16))}</g>
{fog(760, "#a3acc2", 0.1)}
''', NIGHT)

# S4 — fire down to coals, everyone in one tent
scenes["s4"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(200, 480, 0.8)}
{moon(560, 200, 60)}
{treeline(760, 50, 420, 700, "#06080d")}
<path d="M0 760 C500 740 1400 745 1920 760 L1920 1080 L0 1080Z" fill="#0a0a0f"/>
{tent(1080, 860, 520, 360, body="#1c2524", shade="#0e1414", glow="#3a2c22")}
{campfire(620, 930, 0.8, lit=False)}
<path d="M600 900 C590 800 640 720 600 620 C570 540 620 480 600 400" stroke="#9aa3b8" stroke-width="10" fill="none" opacity="0.12" filter="url(#blur8)"/>
<g fill="#06070a">
<rect x="1420" y="840" width="90" height="40" rx="8"/><rect x="760" y="860" width="60" height="50" rx="10"/>
</g>
{fog(820, "#a3acc2", 0.16, 130)}
{grass(1080, 240, "#050508", (18, 44))}
''', NIGHT)

# S5 — inside the dark tent: the zipper starts to open
def inside_tent(open_frac, sliver=True, extra=""):
    zy = 260 + 560 * open_frac
    gap = (f'<path d="M960 260 C930 {260 + (zy - 260) * .4:.0f} 900 {zy - 40:.0f} 960 {zy:.0f} C1020 {zy - 40:.0f} 990 {260 + (zy - 260) * .4:.0f} 960 260Z" fill="#0b1426"/>'
           f'<path d="M960 260 C930 {260 + (zy - 260) * .4:.0f} 900 {zy - 40:.0f} 960 {zy:.0f} C1020 {zy - 40:.0f} 990 {260 + (zy - 260) * .4:.0f} 960 260Z" fill="{MOONBLUE}" opacity="0.35"/>'
           f'<path d="M960 260 C930 {260 + (zy - 260) * .4:.0f} 900 {zy - 40:.0f} 960 {zy:.0f}" fill="none" stroke="{MOONBLUE}" stroke-width="3" opacity="0.6"/>'
           f'<path d="M960 260 C990 {260 + (zy - 260) * .4:.0f} 1020 {zy - 40:.0f} 960 {zy:.0f}" fill="none" stroke="{MOONBLUE}" stroke-width="3" opacity="0.6"/>') if sliver else ""
    teeth = "".join(f'<rect x="954" y="{y}" width="12" height="5" fill="#3a4040"/>' for y in range(int(zy) + 6, 830, 12))
    pull = (f'<rect x="948" y="{zy - 4:.0f}" width="24" height="16" rx="4" fill="#9aa0a6"/>'
            f'<rect x="954" y="{zy + 10:.0f}" width="12" height="40" rx="5" fill="#b6bcc2"/>')
    return svg(f'''
<rect width="{W}" height="{H}" fill="#06080a"/>
<polygon points="960,-200 2100,1080 -180,1080" fill="url(#canvas)"/>
<g stroke="#0a0f0e" stroke-width="3" opacity="0.7">{''.join(f'<line x1="960" y1="-200" x2="{x}" y2="1080"/>' for x in range(-180, 2100, 260))}</g>
<path d="M600 230 C700 200 1220 200 1320 230 L1360 860 C1100 900 820 900 560 860Z" fill="#141c1b"/>
<path d="M600 230 C700 200 1220 200 1320 230 L1360 860 C1100 900 820 900 560 860Z" fill="none" stroke="#0a0f0e" stroke-width="10"/>
<line x1="960" y1="250" x2="960" y2="860" stroke="#0b100f" stroke-width="10"/>
{gap}{teeth}{pull}
{glow(960, zy, 160, MOONBLUE, 0.22)}
{extra}
<path d="M-50 1080 C200 900 500 930 760 990 C820 1010 860 1080 860 1080Z" fill="#1d1420"/>
<path d="M1060 1080 C1100 960 1300 920 1500 950 C1700 980 1900 900 2000 1080Z" fill="#162024"/>
<path d="M380 960 C460 930 560 940 640 980" stroke="#2c2030" stroke-width="6" fill="none"/>
''', '''<linearGradient id="canvas" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#101716"/><stop offset="1" stop-color="#1b2423"/></linearGradient>''')

scenes["s5"] = inside_tent(0.45)

# S6 — outside: the flap open, something long and thin crawling in
crawler = f'''<g fill="#020203">
<path d="M1010 840 C1060 780 1130 740 1220 735 C1300 730 1380 760 1420 800 C1440 820 1450 840 1450 860 L1000 860Z"/>
<ellipse cx="1000" cy="770" rx="44" ry="52" transform="rotate(-30 1000 770)"/>
<path d="M1080 790 C1040 820 990 850 930 858" stroke="#020203" stroke-width="22" fill="none" stroke-linecap="round"/>
<path d="M1150 780 C1110 820 1060 846 990 862" stroke="#020203" stroke-width="20" fill="none" stroke-linecap="round"/>
<path d="M1400 820 C1460 760 1520 740 1560 760 C1600 780 1610 830 1640 862" stroke="#020203" stroke-width="24" fill="none" stroke-linecap="round"/>
<path d="M1340 830 C1380 780 1440 770 1480 800 C1510 820 1520 850 1540 864" stroke="#020203" stroke-width="20" fill="none" stroke-linecap="round"/>
</g>
<g stroke="#020203" stroke-width="5" stroke-linecap="round">{''.join(f'<line x1="{930 + i * 4}" y1="858" x2="{905 + i * 9}" y2="{866 + i}"/>' for i in range(4))}</g>'''
scenes["s6"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(200, 480, 0.8)}
{moon(1500, 190, 64)}
{treeline(760, 50, 420, 700, "#06080d")}
<path d="M0 760 C500 740 1400 745 1920 760 L1920 1080 L0 1080Z" fill="#0b0c12"/>
<ellipse cx="1250" cy="790" rx="520" ry="120" fill="#7f8aa8" opacity="0.32" filter="url(#blur60)"/>
<ellipse cx="1250" cy="830" rx="420" ry="60" fill="#9aa6c4" opacity="0.25" filter="url(#blur30)"/>
{tent(880, 870, 560, 380, body="#34433f", shade="#16201f", door_open=1.0, door_color="#010102")}
{crawler}
<ellipse cx="1220" cy="870" rx="300" ry="20" fill="#000" opacity="0.6" filter="url(#blur8)"/>
{campfire(420, 930, 0.7, lit=False)}
{fog(840, "#a3acc2", 0.16, 130)}
{grass(1080, 240, "#050508", (18, 44))}
''', NIGHT)


# S7 — top-down: four sleeping bags in the dark, my hand counting heads
def bag(x, y, color, hair="#120d0c", face=None, eyes_on=False):
    out = (f'<rect x="{x - 75}" y="{y}" width="150" height="620" rx="74" fill="{color}"/>'
           f'<g stroke="#000" stroke-width="3" opacity="0.35">{"".join(f"<line x1=\'{x - 70}\' y1=\'{yy}\' x2=\'{x + 70}\' y2=\'{yy}\'/>" for yy in range(y + 140, y + 600, 70))}</g>'
           f'<path d="M{x - 80} {y + 120} C{x - 60} {y + 160} {x + 60} {y + 160} {x + 80} {y + 120}" stroke="#000" stroke-width="6" fill="none" opacity="0.4"/>')
    if face:
        out += (f'<ellipse cx="{x}" cy="{y + 40}" rx="62" ry="74" fill="{face}"/>'
                f'<ellipse cx="{x}" cy="{y + 10}" rx="60" ry="52" fill="{hair}"/>')
    else:
        out += f'<ellipse cx="{x}" cy="{y + 40}" rx="54" ry="66" fill="{hair}"/>'
    return out


def tent_floor(extra=""):
    bags = (bag(660, 300, "#2c2440", hair="#1a1210") + bag(830, 300, "#203038", hair="#0d0b0a")
            + bag(1000, 300, "#3a2a22", hair="#2a1a10") + bag(1170, 300, "#28343a", hair="#14100e"))
    hand = (f'<g fill="#8f7f78" opacity="0.9" transform="translate(-170 -10)"><path d="M1330 370 C1300 350 1260 330 1220 320 C1200 316 1196 330 1210 336 '
            f'C1170 330 1150 326 1140 332 C1132 340 1150 350 1170 352 C1150 354 1130 360 1136 370 C1144 380 1170 376 1190 374 '
            f'C1180 384 1176 394 1190 396 C1220 398 1290 400 1330 410Z"/></g>')
    return svg(f'''
<rect width="{W}" height="{H}" fill="#05070a"/>
<rect x="380" y="140" width="1160" height="880" rx="20" fill="#121a1c"/>
<rect x="380" y="140" width="1160" height="880" rx="20" fill="none" stroke="#0a0f10" stroke-width="16"/>
<g stroke="#0c1314" stroke-width="3" opacity="0.6">{''.join(f'<line x1="380" y1="{y}" x2="1540" y2="{y}"/>' for y in range(200, 1020, 90))}</g>
{glow(960, 160, 260, MOONBLUE, 0.14)}
{bags}{hand}
{extra}
<polygon points="960,140 1110,140 1400,1020 520,1020" fill="{MOONBLUE}" opacity="0.04"/>
''')

scenes["s7"] = tent_floor()

# S7b — the same, with a fifth head squeezed in beside mine, eyes open
fifth = (f'<g><rect x="1265" y="330" width="96" height="580" rx="48" fill="#0a0c0e"/>'
         f'<ellipse cx="1313" cy="330" rx="54" ry="70" fill="#c9c4ba"/>'
         f'<ellipse cx="1313" cy="300" rx="58" ry="42" fill="#060506"/>'
         f'<path d="M1263 300 C1258 360 1268 410 1278 430" stroke="#060506" stroke-width="14" fill="none"/>'
         f'<path d="M1363 300 C1368 360 1358 410 1348 430" stroke="#060506" stroke-width="14" fill="none"/>'
         f'<ellipse cx="1313" cy="330" rx="140" ry="160" fill="#e6e0d2" opacity="0.10" filter="url(#blur30)"/>'
         f'{eyes(1313, 345, gap=40, r=7, color="#ff3b2f")}'
         f'<path d="M1298 385 Q1313 392 1328 385" stroke="#3a2a28" stroke-width="3" fill="none"/></g>')
scenes["s7b"] = tent_floor(fifth)

for name, s in scenes.items():
    save(name, s)
print("drew", ", ".join(scenes))
