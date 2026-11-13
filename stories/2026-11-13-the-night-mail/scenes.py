"""Scenes for 'The Night Mail'. Run inside this folder: python3 scenes.py"""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *
import random

r = random.Random(1113)

BRASS = "#c9953f"


def rain(n, op=0.35, x0=0, x1=W, y0=0, y1=H, color="#b9c6dd"):
    out = []
    for _ in range(n):
        x = r.randint(x0, x1); y = r.randint(y0, y1); L = r.randint(30, 70)
        out.append(f'<line x1="{x}" y1="{y}" x2="{x - L * .18:.0f}" y2="{y + L}" stroke="{color}" stroke-width="{r.choice([1.5, 2, 2.5])}" '
                   f'opacity="{r.uniform(.12, op):.2f}" stroke-linecap="round"/>')
    return "".join(out)


def floorboards(y0, c1="#1d130d", c2="#170f0a"):
    """Floor in perspective, boards running toward the door."""
    out = [f'<rect x="0" y="{y0}" width="{W}" height="{H - y0}" fill="{c2}"/>']
    for i in range(-14, 15):
        x_top = 960 + i * 46; x_bot = 960 + i * 150
        out.append(f'<line x1="{x_top}" y1="{y0}" x2="{x_bot}" y2="{H}" stroke="#0a0604" stroke-width="3" opacity="0.8"/>')
    return "".join(out)


def door(x, y, w, h, slot=True, flap_open=0.0, color="#2a1b12", panel="#22160f", slot_glow=0.0):
    """Front door seen straight on, with recessed panels, knob, peephole and a brass mail slot."""
    out = [f'<rect x="{x - 22}" y="{y - 22}" width="{w + 44}" height="{h + 22}" fill="#0f0a07"/>',
           f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"/>']
    pw = w * .34; ph = h * .30
    for px in (x + w * .1, x + w * .56):
        for py in (y + h * .07, y + h * .6):
            out.append(f'<rect x="{px:.0f}" y="{py:.0f}" width="{pw:.0f}" height="{ph:.0f}" fill="{panel}" stroke="#120b07" stroke-width="6"/>')
    # knob + peephole
    out.append(f'<circle cx="{x + w * .86:.0f}" cy="{y + h * .52:.0f}" r="{w * .035:.0f}" fill="{BRASS}"/>')
    out.append(f'<circle cx="{x + w * .5:.0f}" cy="{y + h * .2:.0f}" r="{w * .018:.0f}" fill="{BRASS}" opacity="0.8"/>')
    if slot:
        sx = x + w * .26; sy = y + h * .43; sw = w * .48; sh_ = h * .07
        out.append(f'<rect x="{sx - 12:.0f}" y="{sy - 12:.0f}" width="{sw + 24:.0f}" height="{sh_ + 24:.0f}" rx="8" fill="#8a6326"/>')
        out.append(f'<rect x="{sx:.0f}" y="{sy:.0f}" width="{sw:.0f}" height="{sh_:.0f}" fill="#050403"/>')
        if slot_glow:
            out.append(f'<rect x="{sx:.0f}" y="{sy:.0f}" width="{sw:.0f}" height="{sh_:.0f}" fill="#ffd59a" opacity="{slot_glow}"/>')
            out.append(glow(sx + sw / 2, sy + sh_ / 2, sw * .45, "#ffcf8a", slot_glow * .6))
        fh = sh_ * (1 - flap_open)
        out.append(f'<rect x="{sx:.0f}" y="{sy:.0f}" width="{sw:.0f}" height="{max(fh, 6):.0f}" fill="{BRASS}"/>')
        out.append(f'<rect x="{sx:.0f}" y="{sy:.0f}" width="{sw:.0f}" height="6" fill="#f1cf86" opacity="0.6"/>')
    return "".join(out)


def envelope(cx, cy, w=360, rot=-8, scrawl=True, opened=False, color="#d8ccb0"):
    h = w * .62
    out = [f'<g transform="translate({cx} {cy}) rotate({rot})">',
           f'<rect x="{-w / 2 + 10:.0f}" y="{-h / 2 + 14:.0f}" width="{w:.0f}" height="{h:.0f}" fill="#000" opacity="0.45" filter="url(#blur8)"/>',
           f'<rect x="{-w / 2:.0f}" y="{-h / 2:.0f}" width="{w:.0f}" height="{h:.0f}" fill="{color}"/>',
           f'<path d="M{-w / 2:.0f} {-h / 2:.0f} L0 {h * .08:.0f} L{w / 2:.0f} {-h / 2:.0f}" stroke="#a89878" stroke-width="3" fill="none"/>']
    if opened:
        out.append(f'<path d="M{-w / 2:.0f} {-h / 2:.0f} L0 {-h * 1.05:.0f} L{w / 2:.0f} {-h / 2:.0f} Z" fill="#cbbd9e" stroke="#a89878" stroke-width="3"/>')
        out.append(f'<rect x="{-w * .38:.0f}" y="{-h * .85:.0f}" width="{w * .76:.0f}" height="{h * .5:.0f}" fill="#efe6d0"/>')
        for k in range(3):
            out.append(f'<path d="M{-w * .3:.0f} {-h * .72 + k * 22:.0f} q{w * .1:.0f} -8 {w * .2:.0f} 0 t{w * .2:.0f} 0 t{w * .15:.0f} 0" stroke="#3a1412" stroke-width="3" fill="none"/>')
    if scrawl:
        pts = []; xx = -w * .3
        while xx < w * .28:
            pts.append(f"{xx:.0f},{h * .18 + r.uniform(-14, 12):.0f}"); xx += r.uniform(10, 18)
        out.append(f'<polyline points="{" ".join(pts)}" stroke="#2a1a14" stroke-width="5" fill="none" stroke-linejoin="round" stroke-linecap="round"/>')
        out.append(f'<path d="M{-w * .3:.0f} {h * .32:.0f} q{w * .3:.0f} 10 {w * .56:.0f} -4" stroke="#2a1a14" stroke-width="3" fill="none"/>')
    out.append('</g>')
    return "".join(out)


def woman(cx, base, s=1.0, color="#07060a", arms_up=True):
    """Neighbor: shoulder-length hair, cardigan, holding a letter up in both hands."""
    h = 520 * s
    out = [f'<g fill="{color}">',
           f'<ellipse cx="{cx}" cy="{base - h * .86:.0f}" rx="{44 * s:.0f}" ry="{54 * s:.0f}"/>',
           # hair
           f'<path d="M{cx - 54 * s:.0f} {base - h * .84:.0f} C{cx - 64 * s:.0f} {base - h * .98:.0f} {cx + 64 * s:.0f} {base - h * .98:.0f} {cx + 54 * s:.0f} {base - h * .84:.0f} '
           f'L{cx + 62 * s:.0f} {base - h * .72:.0f} L{cx - 62 * s:.0f} {base - h * .72:.0f} Z"/>',
           f'<rect x="{cx - 20 * s:.0f}" y="{base - h * .78:.0f}" width="{40 * s:.0f}" height="{30 * s:.0f}"/>',
           # torso / cardigan / skirt
           f'<path d="M{cx - 110 * s:.0f} {base} C{cx - 120 * s:.0f} {base - h * .3:.0f} {cx - 120 * s:.0f} {base - h * .6:.0f} {cx - 70 * s:.0f} {base - h * .7:.0f} '
           f'L{cx + 70 * s:.0f} {base - h * .7:.0f} C{cx + 120 * s:.0f} {base - h * .6:.0f} {cx + 120 * s:.0f} {base - h * .3:.0f} {cx + 110 * s:.0f} {base} Z"/>',
           '</g>']
    if arms_up:
        for sgn in (-1, 1):
            out.append(f'<path d="M{cx + sgn * 92 * s:.0f} {base - h * .64:.0f} C{cx + sgn * 120 * s:.0f} {base - h * .45:.0f} {cx + sgn * 80 * s:.0f} {base - h * .42:.0f} {cx + sgn * 46 * s:.0f} {base - h * .46:.0f}" '
                       f'stroke="{color}" stroke-width="{30 * s:.0f}" fill="none" stroke-linecap="round"/>')
    return "".join(out)


def hallway_bg(op=1.0):
    """Apartment hallway seen through an open doorway: worn wallpaper, ceiling lamp, stairs going down."""
    return f'''
<rect x="640" y="140" width="640" height="760" fill="#3a3222"/>
<g opacity="0.25">{"".join(f'<line x1="{x}" y1="140" x2="{x}" y2="900" stroke="#1a140c" stroke-width="10"/>' for x in range(660, 1280, 46))}</g>
<rect x="640" y="140" width="640" height="760" fill="url(#hallShade)"/>
{glow(960, 170, 220, "#ffd79a", 0.55 * op)}
<ellipse cx="960" cy="164" rx="60" ry="18" fill="#ffe2b0" opacity="{0.9 * op}"/>
<rect x="640" y="760" width="640" height="140" fill="#20180f"/>
<g fill="#151009">{"".join(f'<rect x="{1120 + k * 30}" y="{700 + k * 26}" width="{170 - k * 30}" height="14"/>' for k in range(5))}</g>
<rect x="1110" y="560" width="10" height="200" fill="#151009"/>
'''


HALLSHADE = '''<linearGradient id="hallShade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity="0.05"/>
<stop offset="1" stop-color="#000" stop-opacity="0.65"/></linearGradient>'''

scenes = {}

# S1 — the front door from inside, brass slot catching lamplight
scenes["s1"] = svg(f'''
<rect width="{W}" height="{H}" fill="#120d0b"/>
<g opacity="0.35">{"".join(f'<rect x="{x}" y="0" width="22" height="{H}" fill="#1a1310"/>' for x in range(0, W, 60))}</g>
{door(760, 150, 400, 760)}
<rect x="760" y="902" width="400" height="10" fill="#ffcf8a" opacity="0.55"/>
{glow(960, 912, 160, "#ffcf8a", 0.35)}
{floorboards(910)}
<path d="M760 912 L1160 912 L1300 1080 L620 1080 Z" fill="#ffcf8a" opacity="0.06"/>
{glow(1420, 520, 260, "#ffb54a", 0.45)}
<path d="M1370 420 L1470 420 L1450 500 L1390 500 Z" fill="#3a2414"/><path d="M1370 420 L1470 420 L1450 500 L1390 500 Z" fill="#ffc070" opacity="0.6"/>
<rect x="1414" y="500" width="12" height="260" fill="#0c0806"/><rect x="1370" y="760" width="100" height="150" fill="#0c0806"/>
<rect x="520" y="400" width="140" height="14" fill="#0c0806"/><path d="M540 414 L530 700 L610 700 L600 414 Z" fill="#0c0806"/><path d="M600 414 q30 140 10 230 l40 0 q10 -120 -20 -230 Z" fill="#100a08"/>
{fog(1000, "#ffcf8a", 0.04)}
''')

# S2 — the landlord's note taped above the slot
scenes["s2"] = svg(f'''
<rect width="{W}" height="{H}" fill="#140e0b"/>
<g transform="translate(960 540) scale(1.9) translate(-960 -560)">{door(760, 150, 400, 760)}</g>
{glow(1300, 160, 380, "#ffb54a", 0.25)}
<g transform="rotate(-3 960 300)">
<rect x="700" y="130" width="520" height="330" fill="#000" opacity="0.4" filter="url(#blur8)"/>
<rect x="690" y="120" width="520" height="330" fill="#e2d6b8"/>
<rect x="890" y="104" width="140" height="40" fill="#cfc59a" opacity="0.8"/>
<text x="950" y="210" text-anchor="middle" font-family="{SERIF}" font-style="italic" font-size="44" fill="#2a1d14">Mail comes in</text>
<text x="950" y="266" text-anchor="middle" font-family="{SERIF}" font-style="italic" font-size="44" fill="#2a1d14">the MORNING.</text>
<text x="950" y="340" text-anchor="middle" font-family="{SERIF}" font-style="italic" font-size="40" fill="#2a1d14">After dark —</text>
<text x="950" y="410" text-anchor="middle" font-family="{SERIF}" font-weight="bold" font-style="italic" font-size="54" fill="#9a1610">BURN IT.</text>
<line x1="800" y1="424" x2="1100" y2="420" stroke="#9a1610" stroke-width="4"/>
</g>
''')

# S3 — the apartment building in a thunderstorm, one window lit
wins = []
for row in range(5):
    for col in range(6):
        x = 640 + col * 110; y = 240 + row * 120
        if (row, col) == (2, 3):
            wins.append(lit_window(x, y, 60, 76))
        elif (row, col) in ((0, 1), (4, 4)):
            wins.append(f'<rect x="{x}" y="{y}" width="60" height="76" fill="#3a4258"/>')
        else:
            wins.append(f'<rect x="{x}" y="{y}" width="60" height="76" fill="#0c0f18"/>')
scenes["s3"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky3)"/>
{glow(1300, 120, 340, "#c9d6ff", 0.35)}
<path d="M1380 0 L1330 120 L1370 130 L1300 280 L1350 290 L1280 440" stroke="#eef2ff" stroke-width="6" fill="none"/>
<path d="M1380 0 L1330 120 L1370 130 L1300 280 L1350 290 L1280 440" stroke="#c9d6ff" stroke-width="22" fill="none" opacity="0.35" filter="url(#blur8)"/>
<rect x="600" y="180" width="720" height="760" fill="#0b0d14"/>
<polygon points="580,186 960,100 1340,186" fill="#080a10"/>
{"".join(wins)}
<rect x="900" y="840" width="120" height="100" fill="#1c1408"/><rect x="900" y="840" width="120" height="100" fill="#ffb54a" opacity="0.35"/>
{glow(960, 830, 60, "#ffb54a", 0.5)}
<rect x="0" y="930" width="{W}" height="150" fill="#06080c"/>
<rect x="420" y="560" width="12" height="380" fill="#05060a"/>{glow(426, 560, 50, "#ffb54a", 0.5)}
{rain(520, 0.45)}
{fog(940, "#9aa6bb", 0.12)}
''', sky("sky3", "#05060c", "#151c2e", "#222a3c"))

# S4 — the envelope on the floorboards, close
scenes["s4"] = svg(f'''
<rect width="{W}" height="{H}" fill="#120c09"/>
<rect x="560" y="0" width="800" height="430" fill="#2a1b12"/>
<rect x="560" y="0" width="800" height="430" fill="#000" opacity="0.3"/>
<rect x="760" y="120" width="400" height="60" rx="8" fill="#8a6326"/><rect x="776" y="132" width="368" height="36" fill="{BRASS}"/>
<rect x="560" y="418" width="800" height="14" fill="#ffcf8a" opacity="0.5"/>
{glow(960, 430, 260, "#ffcf8a", 0.25)}
{floorboards(430)}
{envelope(960, 700, 520, -7)}
{glow(960, 690, 360, "#ffcf8a", 0.10)}
''')

# S5 — the flap held open from outside; something breathing behind it
scenes["s5"] = svg(f'''
<rect width="{W}" height="{H}" fill="#140d0a"/>
<rect x="0" y="0" width="{W}" height="{H}" fill="#2a1b12" opacity="0.6"/>
<rect x="520" y="390" width="880" height="300" rx="20" fill="#8a6326"/>
<rect x="556" y="420" width="808" height="240" fill="#020102"/>
{glow(960, 560, 200, "#7a0a06", 0.5)}
{eyes(960, 560, gap=120, r=12)}
<rect x="556" y="420" width="808" height="66" fill="{BRASS}"/>
<rect x="556" y="420" width="808" height="10" fill="#f1cf86" opacity="0.6"/>
<g fill="#8f8a84">
{"".join(f'<path d="M{x} 486 q-6 30 0 54 q10 14 20 0 q6 -24 0 -54 Z"/>' for x in (700, 740, 780, 1150, 1190))}
</g>
<g fill="#5a5450">{"".join(f'<ellipse cx="{x + 10}" cy="534" rx="8" ry="5"/>' for x in (700, 740, 780, 1150, 1190))}</g>
{glow(960, 900, 400, "#ffb54a", 0.12)}
<rect x="0" y="860" width="{W}" height="220" fill="#0e0907"/>
''')

# S6 — burning the letter in the sink
scenes["s6"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0c0a0a"/>
<g opacity="0.5">{"".join(f'<rect x="{x}" y="{y}" width="76" height="76" fill="none" stroke="#1c1814" stroke-width="4"/>' for x in range(400, 1520, 80) for y in range(80, 560, 80))}</g>
<rect x="900" y="200" width="30" height="160" fill="#4a4a4e"/><path d="M915 210 q0 -60 90 -60 l40 0" stroke="#4a4a4e" stroke-width="30" fill="none"/>
<rect x="360" y="560" width="1200" height="60" fill="#22201c"/>
<path d="M600 620 L1320 620 L1260 900 L660 900 Z" fill="#141312"/>
<path d="M620 620 L1300 620 L1250 880 L670 880 Z" fill="#1d1c1a"/>
{glow(960, 700, 300, "#ff7a1a", 0.55)}
<g transform="translate(960 760) rotate(-6)">
<rect x="-170" y="-60" width="340" height="120" fill="#cfc2a4"/>
<path d="M-170 -60 L-60 -60 Q-30 0 -80 60 L-170 60 Z" fill="#141010"/>
<path d="M-80 60 Q-30 0 -60 -60" stroke="#ff7a1a" stroke-width="10" fill="none"/>
</g>
<g>
<path d="M800 760 C780 660 860 640 840 540 C900 600 900 660 880 700 C920 640 960 600 940 520 C1020 610 1000 680 980 740 Z" fill="#ff7a1a" opacity="0.9"/>
<path d="M830 760 C820 690 870 670 860 610 C900 660 900 700 890 730 C920 690 940 660 940 610 C980 670 970 720 960 760 Z" fill="#ffd27a"/>
</g>
{glow(900, 640, 160, "#ffb54a", 0.6)}
<g fill="#3a3430" opacity="0.6">{"".join(f'<circle cx="{900 + r.randint(-80, 80)}" cy="{460 - k * 40}" r="{20 + k * 6}" filter="url(#blur8)"/>' for k in range(6))}</g>
<rect x="0" y="900" width="{W}" height="180" fill="#0a0808"/>
''')

# S7 — three quiet nights: the narrator's chair facing the closed door
scenes["s7"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0a0a10"/>
{door(980, 200, 340, 650, color="#1d140e", panel="#171009")}
<rect x="980" y="842" width="340" height="8" fill="#9fb4c8" opacity="0.25"/>
{floorboards(850, "#120d0a", "#0e0a08")}
<path d="M300 0 L640 0 L640 700 L300 760 Z" fill="#1a2232"/>
<path d="M300 0 L640 0 L640 700 L300 760 Z" fill="#9fb4c8" opacity="0.08"/>
<line x1="470" y1="0" x2="470" y2="730" stroke="#0a0a10" stroke-width="10"/><line x1="300" y1="380" x2="640" y2="360" stroke="#0a0a10" stroke-width="10"/>
<path d="M300 760 L640 700 L1100 1080 L560 1080 Z" fill="#9fb4c8" opacity="0.06"/>
<g fill="#050507">
<rect x="700" y="760" width="200" height="30"/><rect x="706" y="790" width="14" height="140"/><rect x="880" y="790" width="14" height="140"/>
<rect x="700" y="560" width="26" height="230"/>
<ellipse cx="800" cy="610" rx="44" ry="52"/>
<path d="M740 770 C730 700 740 670 800 662 C860 670 870 700 862 770 Z"/>
</g>
<circle cx="1550" cy="300" r="70" fill="#18161c" stroke="#3a3640" stroke-width="6"/>
<line x1="1550" y1="300" x2="1550" y2="252" stroke="#9a9aa4" stroke-width="5"/><line x1="1550" y1="300" x2="1586" y2="318" stroke="#9a9aa4" stroke-width="4"/>
{fog(900, "#8090a8", 0.06)}
''')

# S8 / S8b — the neighbor at the open door with the opened letter
for name, close in (("s8", False), ("s8b", True)):
    if not close:
        fig = woman(960, 900, 1.0) + envelope(960, 680, 230, -4, scrawl=True, opened=True)
        extra = ""
    else:
        fig = (f'<g transform="translate(960 900) scale(1.45) translate(-960 -900)">{woman(960, 900, 1.0, arms_up=False)}</g>'
               + eyes(960, 900 - 1.45 * 520 * .86 + 8, gap=36, r=6))
        extra = envelope(760, 1010, 260, 24, scrawl=True, opened=True, color="#bfb398")
    scenes[name] = svg(f'''
<rect width="{W}" height="{H}" fill="#100b09"/>
{hallway_bg()}
{fig}
<rect x="600" y="100" width="40" height="820" fill="#2a1b12"/><rect x="1280" y="100" width="40" height="820" fill="#2a1b12"/>
<rect x="600" y="100" width="720" height="40" fill="#2a1b12"/>
<rect x="0" y="0" width="600" height="{H}" fill="#0e0a08"/><rect x="1320" y="0" width="600" height="{H}" fill="#0e0a08"/>
<polygon points="1320,100 1500,40 1500,1000 1320,920" fill="#22160f"/>
<rect x="1310" y="490" width="70" height="18" rx="4" fill="#8a6326"/>
{floorboards(920)}
<path d="M640 920 L1280 920 L1440 1080 L480 1080 Z" fill="#ffd79a" opacity="0.07"/>
{extra}
''', HALLSHADE)

for n, s in scenes.items():
    save(n, s)
