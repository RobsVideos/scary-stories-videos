"""Scenes for 'The Visitor Log'. Run inside this folder: python3 scenes.py"""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *
import random, math

r = random.Random(21)


def rain(n, op=0.35, x0=0, x1=W, y0=0, y1=H, color="#b9c6dd"):
    out = []
    for _ in range(n):
        x = r.randint(x0, x1); y = r.randint(y0, y1); L = r.randint(30, 70)
        out.append(f'<line x1="{x}" y1="{y}" x2="{x - L * .18:.0f}" y2="{y + L}" stroke="{color}" stroke-width="{r.choice([1.5, 2, 2.5])}" opacity="{r.uniform(.12, op):.2f}" stroke-linecap="round"/>')
    return "".join(out)


def tube_light(x, y, w, op=0.9, color="#dff3ee"):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="14" rx="4" fill="{color}" opacity="{op}"/>'
            f'<rect x="{x - 30}" y="{y - 20}" width="{w + 60}" height="60" fill="{color}" opacity="{op * .25:.2f}" filter="url(#blur30)"/>')


def old_woman(cx, base, s=1.0, color="#06070a", back=False):
    """Hunched old woman in a long nightgown, long thin hair, bare feet; optional bracelet glint."""
    h = 430 * s
    head_x = cx + (0 if back else 18 * s)
    return (f'<g fill="{color}">'
            # nightgown
            f'<path d="M{cx - 70 * s:.0f} {base - 20 * s:.0f} C{cx - 60 * s:.0f} {base - h * .45:.0f} {cx - 70 * s:.0f} {base - h * .65:.0f} {cx - 40 * s:.0f} {base - h * .76:.0f} '
            f'C{cx - 10 * s:.0f} {base - h * .82:.0f} {cx + 40 * s:.0f} {base - h * .8:.0f} {cx + 52 * s:.0f} {base - h * .7:.0f} '
            f'C{cx + 60 * s:.0f} {base - h * .5:.0f} {cx + 66 * s:.0f} {base - h * .3:.0f} {cx + 78 * s:.0f} {base - 20 * s:.0f} Z"/>'
            # head (bent forward)
            f'<ellipse cx="{head_x:.0f}" cy="{base - h * .86:.0f}" rx="{30 * s:.0f}" ry="{36 * s:.0f}"/>'
            # bare feet / ankles
            f'<rect x="{cx - 34 * s:.0f}" y="{base - 26 * s:.0f}" width="{14 * s:.0f}" height="{24 * s:.0f}"/>'
            f'<rect x="{cx + 22 * s:.0f}" y="{base - 26 * s:.0f}" width="{14 * s:.0f}" height="{24 * s:.0f}"/>'
            f'<ellipse cx="{cx - 22 * s:.0f}" cy="{base - 3 * s:.0f}" rx="{20 * s:.0f}" ry="{6 * s:.0f}"/>'
            f'<ellipse cx="{cx + 34 * s:.0f}" cy="{base - 3 * s:.0f}" rx="{20 * s:.0f}" ry="{6 * s:.0f}"/>'
            # arms hanging
            f'<path d="M{cx - 44 * s:.0f} {base - h * .72:.0f} C{cx - 80 * s:.0f} {base - h * .55:.0f} {cx - 78 * s:.0f} {base - h * .45:.0f} {cx - 70 * s:.0f} {base - h * .36:.0f}" stroke="{color}" stroke-width="{18 * s:.0f}" fill="none" stroke-linecap="round"/>'
            f'<path d="M{cx + 46 * s:.0f} {base - h * .7:.0f} C{cx + 80 * s:.0f} {base - h * .55:.0f} {cx + 82 * s:.0f} {base - h * .45:.0f} {cx + 76 * s:.0f} {base - h * .36:.0f}" stroke="{color}" stroke-width="{18 * s:.0f}" fill="none" stroke-linecap="round"/>'
            '</g>'
            # long wet hair strands
            + "".join(f'<path d="M{head_x + dx * s:.0f} {base - h * .9:.0f} q{dx * .4 * s:.0f} {80 * s:.0f} {dx * .2 * s:.0f} {(140 + abs(dx)) * s:.0f}" stroke="#2b2e36" stroke-width="{3 * s:.1f}" fill="none" opacity="0.8"/>'
                      for dx in (-26, -18, -10, -2, 6, 14, 22))
            # hospital bracelet glint
            + f'<rect x="{cx + 66 * s:.0f}" y="{base - h * .4:.0f}" width="{20 * s:.0f}" height="{8 * s:.0f}" fill="#e8eef2" opacity="0.9"/>'
            + glow(cx + 76 * s, base - h * .4 + 4 * s, 14 * s, "#e8eef2", 0.5))


def guard(cx, base, s=1.0, color="#07070b"):
    """Older security guard: cap, broad shoulders."""
    return (f'<g fill="{color}">'
            f'<ellipse cx="{cx}" cy="{base - 330 * s:.0f}" rx="{42 * s:.0f}" ry="{50 * s:.0f}"/>'
            f'<path d="M{cx - 50 * s:.0f} {base - 362 * s:.0f} L{cx + 50 * s:.0f} {base - 362 * s:.0f} L{cx + 86 * s:.0f} {base - 350 * s:.0f} L{cx + 48 * s:.0f} {base - 344 * s:.0f} L{cx - 46 * s:.0f} {base - 344 * s:.0f} Z"/>'
            f'<path d="M{cx - 48 * s:.0f} {base - 362 * s:.0f} Q{cx} {base - 410 * s:.0f} {cx + 48 * s:.0f} {base - 362 * s:.0f} Z"/>'
            f'<path d="M{cx - 140 * s:.0f} {base} C{cx - 150 * s:.0f} {base - 150 * s:.0f} {cx - 130 * s:.0f} {base - 250 * s:.0f} {cx - 60 * s:.0f} {base - 275 * s:.0f} '
            f'L{cx + 60 * s:.0f} {base - 275 * s:.0f} C{cx + 130 * s:.0f} {base - 250 * s:.0f} {cx + 150 * s:.0f} {base - 150 * s:.0f} {cx + 140 * s:.0f} {base} Z"/>'
            f'</g><rect x="{cx - 70 * s:.0f}" y="{base - 230 * s:.0f}" width="{34 * s:.0f}" height="{22 * s:.0f}" fill="#8a7a4a" opacity="0.7"/>')


def log_page(x, y, w, rows, extra=False, lamp=True):
    """Open visitor log seen from above: two pages, ruled lines, header, handwritten rows."""
    out = []
    if lamp:
        out.append(glow(x + w * .5, y + 200, 520, "#ffb860", 0.28))
    out.append(f'<rect x="{x - 14}" y="{y - 14}" width="{w + 28}" height="{728}" rx="10" fill="#2a160c"/>')
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="700" fill="#d9ccaa"/>')
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="700" fill="url(#paperShade)"/>')
    out.append(f'<text x="{x + w / 2}" y="{y + 62}" text-anchor="middle" font-family="{SERIF}" font-size="36" letter-spacing="6" fill="#3a2a1a">VISITOR LOG</text>')
    out.append(f'<line x1="{x + 30}" y1="{y + 90}" x2="{x + w - 30}" y2="{y + 90}" stroke="#7a1d18" stroke-width="3"/>')
    for i, lbl in enumerate(["NAME", "ROOM", "TIME"]):
        lx = [x + 40, x + w * .62, x + w * .8][i]
        out.append(f'<text x="{lx}" y="{y + 128}" font-family="{SANS}" font-size="22" letter-spacing="3" fill="#5a4a36">{lbl}</text>')
    for k in range(9):
        ly = y + 150 + k * 60
        out.append(f'<line x1="{x + 30}" y1="{ly + 50}" x2="{x + w - 30}" y2="{ly + 50}" stroke="#8fa0b6" stroke-width="2" opacity="0.7"/>')
    out.append(f'<line x1="{x + w * .6}" y1="{y + 100}" x2="{x + w * .6}" y2="{y + 690}" stroke="#b08a80" stroke-width="2" opacity="0.6"/>')
    out.append(f'<line x1="{x + w * .78}" y1="{y + 100}" x2="{x + w * .78}" y2="{y + 690}" stroke="#b08a80" stroke-width="2" opacity="0.6"/>')
    for k, (name, room, t, ink) in enumerate(rows):
        ly = y + 192 + k * 60
        out.append(f'<text x="{x + 44}" y="{ly}" font-family="{SERIF}" font-style="italic" font-size="44" fill="{ink}" transform="rotate(-1.5 {x + 44} {ly})">{name}</text>')
        out.append(f'<text x="{x + w * .62 + 6}" y="{ly}" font-family="{SERIF}" font-style="italic" font-size="44" fill="{ink}">{room}</text>')
        out.append(f'<text x="{x + w * .8 + 6}" y="{ly}" font-family="{SERIF}" font-style="italic" font-size="40" fill="{ink}">{t}</text>')
    if extra:
        ly = y + 252
        # shaky, smeared signature (the narrator's own name)
        pts = []
        xx = x + 48
        while xx < x + w * .56:
            pts.append(f"{xx:.0f},{ly - 18 + r.uniform(-16, 14):.0f}")
            xx += r.uniform(12, 22)
        out.append(f'<polyline points="{" ".join(pts)}" stroke="#5a0f0c" stroke-width="5" fill="none" stroke-linejoin="round"/>')
        out.append(f'<text x="{x + w * .62 + 6}" y="{ly}" font-family="{SERIF}" font-style="italic" font-size="48" fill="#9a1610">413</text>')
        out.append(glow(x + w * .69, ly - 16, 70, "#ff2a1a", 0.35))
        # wet drips on the page
        for dx, dy in ((0.3, 330), (0.5, 410), (0.66, 300)):
            out.append(f'<ellipse cx="{x + w * dx:.0f}" cy="{y + dy}" rx="18" ry="12" fill="#6e6650" opacity="0.35"/>')
    return "".join(out)


PAPER = '''<linearGradient id="paperShade" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff3d6" stop-opacity="0.15"/>
<stop offset="1" stop-color="#2a1a0a" stop-opacity="0.45"/></linearGradient>'''

scenes = {}

# S1 — hospital at night in the rain
win = []
for row in range(6):
    for col in range(9):
        x = 560 + col * 92; y = 180 + row * 86
        if (row, col) in ((1, 2), (3, 6), (2, 4), (4, 1)):
            win.append(f'<rect x="{x}" y="{y}" width="54" height="50" fill="#9fd6cf" opacity="0.8"/>'
                       f'<rect x="{x}" y="{y}" width="54" height="50" fill="#9fd6cf" opacity="0.4" filter="url(#blur8)"/>')
        elif (row, col) == (1, 5):
            win.append(f'<rect x="{x}" y="{y}" width="54" height="50" fill="#ffb54a"/>'
                       f'<rect x="{x}" y="{y}" width="54" height="50" fill="#ffb54a" opacity="0.7" filter="url(#blur30)"/>')
        else:
            win.append(f'<rect x="{x}" y="{y}" width="54" height="50" fill="#141824"/>')
scenes["s1"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
<rect x="520" y="120" width="880" height="700" fill="#0b0d14"/>
<rect x="500" y="110" width="920" height="22" fill="#07080d"/>
{"".join(win)}
<rect x="1080" y="60" width="16" height="60" fill="#07080d"/><circle cx="1088" cy="56" r="7" fill="#ff3b2f"/>{glow(1088, 56, 30, "#ff3b2f", 0.6)}
<rect x="620" y="700" width="680" height="30" fill="#05060a"/>
<rect x="650" y="660" width="620" height="40" fill="#0e1018"/>
<text x="960" y="690" text-anchor="middle" font-family="{SANS}" font-size="28" letter-spacing="10" fill="#c9eee8">VISITORS</text>
{glow(960, 682, 140, "#9fe6dc", 0.25)}
<rect x="800" y="730" width="320" height="110" fill="#cfeee6" opacity="0.85"/>
<rect x="800" y="730" width="320" height="110" fill="#cfeee6" opacity="0.6" filter="url(#blur30)"/>
<line x1="960" y1="730" x2="960" y2="840" stroke="#2a3a3a" stroke-width="6"/>
<rect x="0" y="830" width="{W}" height="250" fill="#0a0c12"/>
<path d="M800 840 L1120 840 L1300 1080 L620 1080 Z" fill="#cfeee6" opacity="0.10" filter="url(#blur30)"/>
<ellipse cx="960" cy="930" rx="260" ry="30" fill="#cfeee6" opacity="0.14" filter="url(#blur8)"/>
<ellipse cx="1088" cy="1000" rx="40" ry="8" fill="#ff3b2f" opacity="0.2" filter="url(#blur8)"/>
<rect x="430" y="560" width="10" height="270" fill="#05060a"/><path d="M435 560 q30 -20 60 0" stroke="#05060a" stroke-width="10" fill="none"/>
{glow(495, 572, 60, "#ffb54a", 0.5)}
{rain(420, 0.4)}
{fog(860, "#9aa6bb", 0.12)}
''', sky("sky1", "#04050b", "#121a2a", "#22273a"))

# S2 — the guard slides the log across the desk
scenes["s2"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0b0d12"/>
{tube_light(700, 70, 520, 0.6)}
<rect x="0" y="120" width="{W}" height="520" fill="#121620"/>
<rect x="560" y="200" width="300" height="200" fill="#0a0c12"/><rect x="1060" y="200" width="300" height="200" fill="#0a0c12"/>
<circle cx="1210" cy="290" r="52" fill="#d9d4c4" opacity="0.8"/><circle cx="1210" cy="290" r="44" fill="#141414"/>
<line x1="1210" y1="290" x2="1210" y2="258" stroke="#d9d4c4" stroke-width="4"/><line x1="1210" y1="290" x2="1232" y2="300" stroke="#d9d4c4" stroke-width="3"/>
{guard(960, 760, 1.25)}
{glow(1290, 600, 260, "#ffb860", 0.45)}
<path d="M1260 470 L1330 470 L1300 560 Z" fill="#1a120a"/><rect x="1294" y="560" width="10" height="110" fill="#1a120a"/>
<ellipse cx="1300" cy="565" rx="50" ry="12" fill="#ffd28a" opacity="0.8" filter="url(#blur8)"/>
<path d="M0 660 L{W} 660 L{W} 1080 L0 1080 Z" fill="#1d130c"/>
<rect x="0" y="650" width="{W}" height="18" fill="#2c1e12"/>
<g transform="translate(960 830) scale(1 0.42) rotate(-6)">
<rect x="-280" y="-200" width="560" height="400" rx="8" fill="#2a160c"/>
<rect x="-266" y="-188" width="262" height="376" fill="#d9ccaa"/><rect x="4" y="-188" width="262" height="376" fill="#d2c39f"/>
{"".join(f'<line x1="-250" y1="{yy}" x2="250" y2="{yy}" stroke="#8fa0b6" stroke-width="3" opacity="0.6"/>' for yy in range(-120, 180, 40))}
</g>
<path d="M1080 600 C1110 680 1090 740 1020 790" stroke="#07070b" stroke-width="44" fill="none" stroke-linecap="round"/><ellipse cx="1010" cy="796" rx="36" ry="18" fill="#07070b"/>
<line x1="1080" y1="845" x2="1190" y2="790" stroke="#c9b994" stroke-width="10" stroke-linecap="round"/>
<ellipse cx="960" cy="840" rx="380" ry="120" fill="#ffb860" opacity="0.10" filter="url(#blur30)"/>
''')

# S3 — empty lobby, rain on the glass doors
chairs = "".join(f'<g fill="#07080c"><rect x="{x}" y="760" width="78" height="16"/><rect x="{x + 4}" y="690" width="70" height="72" rx="6"/>'
                 f'<rect x="{x + 6}" y="776" width="8" height="60"/><rect x="{x + 64}" y="776" width="8" height="60"/></g>' for x in list(range(460, 860, 92)) + list(range(1080, 1480, 92)))
scenes["s3"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0c1016"/>
<rect x="0" y="0" width="{W}" height="140" fill="#080a0e"/>
{tube_light(520, 110, 280, 0.75)}{tube_light(1120, 110, 280, 0.45)}
<rect x="0" y="140" width="{W}" height="560" fill="#141a22"/>
<rect x="720" y="250" width="480" height="470" fill="#0f1a26"/>
<rect x="720" y="250" width="480" height="470" fill="url(#outside)"/>
{rain(160, 0.5, 730, 1190, 260, 700, "#c8d6ea")}
<g stroke="#9fb4c8" stroke-width="3" opacity="0.4">{"".join(f'<path d="M{x} {y} q3 20 0 {r.randint(30, 70)}" fill="none"/>' for x, y in [(r.randint(740, 1180), r.randint(270, 600)) for _ in range(30)])}</g>
<rect x="716" y="246" width="488" height="478" fill="none" stroke="#06070a" stroke-width="16"/>
<line x1="960" y1="250" x2="960" y2="720" stroke="#06070a" stroke-width="12"/>
<rect x="890" y="180" width="140" height="44" fill="#1a0606"/><text x="960" y="213" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="30" letter-spacing="4" fill="#ff4a3a">EXIT</text>
{glow(960, 202, 90, "#ff3b2f", 0.4)}
<path d="M0 700 L{W} 700 L{W} 1080 L0 1080 Z" fill="#161c24"/>
<path d="M720 720 L1200 720 L1420 1080 L500 1080 Z" fill="#9fb4c8" opacity="0.08"/>
{chairs}
{fog(980, "#8aa0b6", 0.08)}
''', '''<linearGradient id="outside" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1c2b3c"/><stop offset="1" stop-color="#2c3a48"/></linearGradient>''')

# S4 — doors slide open, the old woman shuffles in
scenes["s4"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0c1016"/>
<rect x="0" y="140" width="{W}" height="560" fill="#121820"/>
<rect x="620" y="220" width="680" height="500" fill="url(#outside4)"/>
{rain(220, 0.55, 630, 1290, 230, 700, "#c8d6ea")}
{glow(960, 420, 220, "#b7cde0", 0.35)}
<rect x="520" y="216" width="200" height="508" fill="#0f1a26" opacity="0.85"/><rect x="1200" y="216" width="200" height="508" fill="#0f1a26" opacity="0.85"/>
<rect x="516" y="212" width="208" height="516" fill="none" stroke="#06070a" stroke-width="14"/><rect x="1196" y="212" width="208" height="516" fill="none" stroke="#06070a" stroke-width="14"/>
<rect x="600" y="200" width="720" height="22" fill="#06070a"/>
<rect x="890" y="140" width="140" height="44" fill="#1a0606"/><text x="960" y="173" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="30" letter-spacing="4" fill="#ff4a3a">EXIT</text>
{glow(960, 162, 90, "#ff3b2f", 0.45)}
<path d="M0 720 L{W} 720 L{W} 1080 L0 1080 Z" fill="#141a22"/>
<path d="M720 720 L1200 720 L1500 1080 L420 1080 Z" fill="#b7cde0" opacity="0.10"/>
{old_woman(960, 900, 1.15)}
<ellipse cx="970" cy="930" rx="150" ry="22" fill="#9fb4c8" opacity="0.18" filter="url(#blur8)"/>
<g fill="#9fb4c8" opacity="0.25">{"".join(f'<ellipse cx="{960 + dx}" cy="{960 + dy}" rx="26" ry="7"/>' for dx, dy in ((-60, 30), (40, 70), (-10, 120)))}</g>
{fog(760, "#9fb4c8", 0.12)}
''', '''<linearGradient id="outside4" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#26384c"/><stop offset="1" stop-color="#3a4a5a"/></linearGradient>''')

ROW_RUTH = ("Ruth Ellery", "412", "2:15", "#1e2a44")

# S5 — the log, close up
scenes["s5"] = svg(f'''
<rect width="{W}" height="{H}" fill="#120b07"/>
{log_page(560, 190, 800, [ROW_RUTH])}
<path d="M1260 840 L1420 640" stroke="#0a0a0d" stroke-width="22" stroke-linecap="round"/><path d="M1260 840 l-10 18" stroke="#c9b994" stroke-width="6"/>
<path d="M1460 560 C1440 600 1430 640 1420 700 L1520 740 C1540 680 1560 620 1560 560 Z" fill="#06060a" opacity="0.9"/>
''', PAPER)

# S6 — the screen says she is upstairs, asleep
scenes["s6"] = svg(f'''
<rect width="{W}" height="{H}" fill="#06080b"/>
{glow(960, 470, 480, "#3aff9a", 0.10)}
<rect x="560" y="200" width="800" height="540" rx="22" fill="#0e1012"/>
<rect x="596" y="232" width="728" height="470" fill="#06140c"/>
<rect x="596" y="232" width="728" height="470" fill="#1aff7a" opacity="0.04"/>
<g font-family="{MONO}" fill="#4dff9a">
<text x="630" y="300" font-size="30" opacity="0.7">PATIENT LOOKUP</text>
<line x1="630" y1="320" x2="1290" y2="320" stroke="#4dff9a" stroke-width="2" opacity="0.5"/>
<text x="630" y="400" font-size="46" font-weight="bold">ELLERY, RUTH</text>
<text x="630" y="470" font-size="38">ROOM  412</text>
<text x="630" y="530" font-size="38">FLOOR 4</text>
<text x="630" y="610" font-size="40" fill="#ffd27a">STATUS: ASLEEP</text>
</g>
{"".join(f'<line x1="596" y1="{y}" x2="1324" y2="{y}" stroke="#000" stroke-width="2" opacity="0.25"/>' for y in range(236, 700, 6))}
<rect x="880" y="740" width="160" height="80" fill="#0b0c0e"/><rect x="760" y="815" width="400" height="22" rx="6" fill="#0b0c0e"/>
<path d="M0 860 L{W} 860 L{W} 1080 L0 1080 Z" fill="#160e08"/>
<ellipse cx="960" cy="880" rx="420" ry="40" fill="#4dff9a" opacity="0.08" filter="url(#blur30)"/>
''')

# S7 — she walks back out into the rain
scenes["s7"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky7)"/>
<rect x="0" y="0" width="{W}" height="160" fill="#06070a"/>
<rect x="560" y="160" width="800" height="600" fill="#22303e" opacity="0.6"/>
<rect x="1180" y="260" width="12" height="520" fill="#05060a"/><path d="M1186 262 q-40 -24 -80 0" stroke="#05060a" stroke-width="10" fill="none"/>
{glow(1106, 276, 120, "#ffb54a", 0.55)}
<path d="M1106 280 L960 780 L1260 780 Z" fill="#ffb54a" opacity="0.07"/>
{old_woman(1010, 770, 0.55, "#06070a", back=True)}
<ellipse cx="1010" cy="776" rx="70" ry="10" fill="#ffb54a" opacity="0.2" filter="url(#blur8)"/>
{rain(500, 0.55, 0, W, 160, 900)}
<rect x="556" y="156" width="808" height="608" fill="none" stroke="#06070a" stroke-width="18"/>
<path d="M0 760 L{W} 760 L{W} 1080 L0 1080 Z" fill="#0e131a"/>
<path d="M760 760 L1160 760 L1300 1080 L620 1080 Z" fill="#9fb4c8" opacity="0.08"/>
<g fill="#cfd9e6" opacity="0.35">{"".join(f'<ellipse cx="{x}" cy="{y}" rx="12" ry="5"/>' for x, y in ((940, 1000), (1000, 920), (900, 860), (1030, 820)))}</g>
<rect x="460" y="160" width="100" height="640" fill="#0a0d12"/><rect x="1360" y="160" width="100" height="640" fill="#0a0d12"/>
{fog(780, "#9fb4c8", 0.12)}
''', sky("sky7", "#0c121c", "#18222e", "#202c38"))

# S8 — fourth floor, room 412
doors = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#0d1016"/>' for x, y, w, h in ((380, 380, 110, 300), (1430, 380, 110, 300)))
scenes["s8"] = svg(f'''
<rect width="{W}" height="{H}" fill="#07090d"/>
<polygon points="0,0 {W},0 1160,360 760,360" fill="#0c0f15"/>
<polygon points="0,{H} {W},{H} 1160,700 760,700" fill="#11151c"/>
<polygon points="0,0 760,360 760,700 0,{H}" fill="#0e1218"/>
<polygon points="{W},0 1160,360 1160,700 {W},{H}" fill="#0e1218"/>
<rect x="760" y="360" width="400" height="340" fill="#05060a"/>
{tube_light(880, 372, 160, 0.25)}
{doors}
<polygon points="600,250 720,320 720,760 600,860" fill="#130a0a"/>
<polygon points="620,264 700,312 700,752 620,838" fill="#ff2a1a" opacity="0.45"/>
{glow(680, 560, 200, "#ff2a1a", 0.35)}
<polygon points="720,760 600,860 900,1080 1100,1080" fill="#ff2a1a" opacity="0.08"/>
<rect x="612" y="190" width="100" height="44" fill="#d8dde4"/><text x="662" y="224" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="32" fill="#1a1d22">412</text>
<rect x="1000" y="420" width="60" height="44" fill="#1a0606"/><circle cx="1030" cy="442" r="10" fill="#ff3b2f"/>{glow(1030, 442, 30, "#ff3b2f", 0.6)}
<g fill="#05060a"><rect x="1210" y="700" width="160" height="16"/><rect x="1220" y="716" width="8" height="70"/><rect x="1350" y="716" width="8" height="70"/>
<rect x="1240" y="560" width="10" height="140"/><circle cx="1245" cy="550" r="12"/></g>
{fog(820, "#c06060", 0.06)}
''')

# S9 — dawn: the log, before / after the second line
for name, extra in (("s9", False), ("s9b", True)):
    scenes[name] = svg(f'''
<rect width="{W}" height="{H}" fill="#0d0f14"/>
{glow(960, 120, 420, "#7a8aa8", 0.25)}
{log_page(560, 190, 800, [ROW_RUTH], extra=extra, lamp=False)}
<rect x="560" y="190" width="800" height="700" fill="#2a3550" opacity="0.18"/>
''', PAPER)

for n, s in scenes.items():
    save(n, s)
