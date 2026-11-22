"""Scenes for 'The Mirror Wall' — a downtown dance studio, a mirror wall, and a reflection that lags behind."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

r = random.Random(2222)

WARM = "#ffc46a"
RED = "#d8261e"
NIGHT = sky("night", "#03040b", "#131a33", "#2a2540")
DEFS = ('<radialGradient id="halo"><stop offset="0" stop-color="#ffd38a" stop-opacity="0.55"/><stop offset="1" stop-color="#ffd38a" stop-opacity="0"/></radialGradient>'
        '<linearGradient id="floorg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5a3a22"/><stop offset="1" stop-color="#2a1a10"/></linearGradient>'
        '<linearGradient id="floord" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0e1222"/><stop offset="1" stop-color="#05060c"/></linearGradient>'
        '<linearGradient id="glass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5d6478"/><stop offset="0.5" stop-color="#3d4356"/><stop offset="1" stop-color="#2a2f40"/></linearGradient>'
        '<linearGradient id="glassd" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#141a2e"/><stop offset="1" stop-color="#070912"/></linearGradient>'
        '<linearGradient id="dawn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1c2340"/><stop offset="1" stop-color="#7a4a52"/></linearGradient>')


def person(cx, base, s=1.0, color="#07060a", arm="down", mop=True, face=None, flip=False):
    """Janitor silhouette: head, shoulders, coat, legs; optional mop. arm: down/up/switch."""
    k = -1 if flip else 1
    g = [f'<g fill="{color}">',
         f'<ellipse cx="{cx}" cy="{base - 372 * s}" rx="{30 * s}" ry="{36 * s}"/>',
         f'<rect x="{cx - 12 * s}" y="{base - 342 * s}" width="{24 * s}" height="{22 * s}"/>',
         f'<path d="M{cx - 62 * s} {base - 160 * s} L{cx - 58 * s} {base - 300 * s} Q{cx - 50 * s} {base - 326 * s} {cx} {base - 328 * s} '
         f'Q{cx + 50 * s} {base - 326 * s} {cx + 58 * s} {base - 300 * s} L{cx + 62 * s} {base - 160 * s} Z"/>',
         f'<rect x="{cx - 46 * s}" y="{base - 170 * s}" width="{36 * s}" height="{170 * s}" rx="{8 * s}"/>',
         f'<rect x="{cx + 10 * s}" y="{base - 170 * s}" width="{36 * s}" height="{170 * s}" rx="{8 * s}"/>',
         '</g>']
    sw = 22 * s
    if arm == "up":
        g.append(f'<path d="M{cx + k * 54 * s} {base - 300 * s} L{cx + k * 110 * s} {base - 400 * s} L{cx + k * 120 * s} {base - 470 * s}" stroke="{color}" stroke-width="{sw}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    elif arm == "switch":
        g.append(f'<path d="M{cx + k * 54 * s} {base - 300 * s} L{cx + k * 130 * s} {base - 280 * s} L{cx + k * 190 * s} {base - 300 * s}" stroke="{color}" stroke-width="{sw}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    else:
        g.append(f'<path d="M{cx + k * 56 * s} {base - 300 * s} L{cx + k * 70 * s} {base - 160 * s}" stroke="{color}" stroke-width="{sw}" fill="none" stroke-linecap="round"/>')
    g.append(f'<path d="M{cx - k * 56 * s} {base - 300 * s} L{cx - k * 74 * s} {base - 170 * s}" stroke="{color}" stroke-width="{sw}" fill="none" stroke-linecap="round"/>')
    if mop:
        mx = cx - k * 80 * s
        g.append(f'<line x1="{mx}" y1="{base - 330 * s}" x2="{mx - k * 30 * s}" y2="{base}" stroke="#2a2420" stroke-width="{8 * s}"/>')
        g.append(f'<path d="M{mx - k * 30 * s - 40 * s} {base} q{40 * s} {-40 * s} {80 * s} 0 z" fill="#4a4440"/>')
    if face:
        g.append(face)
    return "".join(g)


def studio(lit=True, mirror_fill=None):
    """Front view of the studio: mirror wall across the back, barre, wood floor in perspective."""
    wall = "#3e2c22" if lit else "#0a0c16"
    ceil = "#2a1e18" if lit else "#06070d"
    floor = "url(#floorg)" if lit else "url(#floord)"
    mf = mirror_fill or ("url(#glass)" if lit else "url(#glassd)")
    g = [f'<rect width="{W}" height="{H}" fill="{wall}"/>',
         f'<rect x="0" y="0" width="{W}" height="150" fill="{ceil}"/>',
         f'<polygon points="0,{H} {W},{H} {W},760 0,760" fill="{floor}"/>']
    # floor boards converge
    g.append("".join(f'<line x1="{960 + (x - 960) * 0.45:.0f}" y1="760" x2="{x}" y2="{H}" stroke="#000" stroke-width="2" opacity="{0.35 if lit else 0.5}"/>' for x in range(-900, 2900, 140)))
    # mirror panels
    g.append(f'<rect x="200" y="200" width="1520" height="560" fill="{mf}"/>')
    for x in range(200, 1721, 380):
        g.append(f'<line x1="{x}" y1="200" x2="{x}" y2="760" stroke="#15121a" stroke-width="8"/>')
    g.append(f'<rect x="200" y="200" width="1520" height="560" fill="none" stroke="#15121a" stroke-width="12"/>')
    if lit:
        # reflected floor + diagonal sheen
        g.append('<rect x="200" y="640" width="1520" height="120" fill="#5a3a22" opacity="0.35"/>')
        g.append('<polygon points="420,200 560,200 360,760 220,760" fill="#fff" opacity="0.07"/><polygon points="1180,200 1240,200 1040,760 980,760" fill="#fff" opacity="0.06"/>')
        for lx in (560, 960, 1360):
            g.append(f'<rect x="{lx - 70}" y="130" width="140" height="18" rx="6" fill="#fff3d0"/>')
            g.append(f'<ellipse cx="{lx}" cy="200" rx="380" ry="180" fill="url(#halo)"/>')
    else:
        g.append('<polygon points="420,200 560,200 360,760 220,760" fill="#8fa0d0" opacity="0.04"/>')
    # barre
    bc = "#a6845a" if lit else "#1d1f2c"
    g.append(f'<rect x="150" y="560" width="1620" height="16" rx="8" fill="{bc}"/>')
    for x in (300, 700, 1220, 1620):
        g.append(f'<rect x="{x}" y="560" width="12" height="200" fill="{"#3a2a1c" if lit else "#0c0d16"}"/>')
    return "".join(g)


scenes = {}

# S1 — downtown storefront at night, studio window lit
bldg = []
for x0, w, h, c in ((0, 420, 640, "#0b0c16"), (1500, 420, 700, "#0a0b14")):
    bldg.append(f'<rect x="{x0}" y="{H - h}" width="{w}" height="{h}" fill="{c}"/>')
    for wy in range(H - h + 60, H - 260, 110):
        for wx in range(x0 + 40, x0 + w - 60, 100):
            if r.random() < 0.18:
                bldg.append(f'<rect x="{wx}" y="{wy}" width="44" height="60" fill="#e8a24a" opacity="0.6"/>')
            else:
                bldg.append(f'<rect x="{wx}" y="{wy}" width="44" height="60" fill="#141626"/>')
win_inside = (f'<rect x="600" y="520" width="720" height="300" fill="#e0a45a"/>'
              f'<rect x="600" y="520" width="720" height="300" fill="#ffcf80" opacity="0.6" filter="url(#blur30)"/>'
              f'<rect x="640" y="540" width="640" height="230" fill="#8a7a78" opacity="0.55"/>'
              f'<rect x="600" y="700" width="720" height="10" fill="#7a5a3a"/>'
              + "".join(f'<rect x="{x}" y="700" width="6" height="120" fill="#7a5a3a"/>' for x in (680, 900, 1120))
              + f'<line x1="960" y1="520" x2="960" y2="820" stroke="#120d0c" stroke-width="10"/>')
scenes["s1"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>{stars(70, 300, 0.5)}
{moon(1380, 150, 50)}
{''.join(bldg)}
<rect x="420" y="300" width="1080" height="780" fill="#2a1a18"/>
<g stroke="#1d1212" stroke-width="3" opacity="0.7">{''.join(f'<line x1="420" y1="{y}" x2="1500" y2="{y}"/>' for y in range(320, 1080, 34))}</g>
<rect x="420" y="290" width="1080" height="24" fill="#140d0c"/>
{lit_window(520, 360, 120, 120, "#3a3248")}{lit_window(1280, 360, 120, 120, "#e8a24a")}
<rect x="560" y="500" width="800" height="340" fill="#120d0c"/>
{win_inside}
<rect x="700" y="430" width="520" height="60" rx="6" fill="#120d0c"/>
<text x="960" y="474" text-anchor="middle" font-family="{SERIF}" font-size="40" letter-spacing="10" fill="#e9c3c8">DANCE STUDIO</text>
<text x="960" y="474" text-anchor="middle" font-family="{SERIF}" font-size="40" letter-spacing="10" fill="#ff8aa0" opacity="0.6" filter="url(#blur8)">DANCE STUDIO</text>
<rect x="1370" y="560" width="100" height="280" fill="#0d0909"/><circle cx="1455" cy="710" r="6" fill="#a7853f"/>
<polygon points="560,840 1360,840 1540,1080 380,1080" fill="#ffc46a" opacity="0.18"/>
<rect x="0" y="840" width="{W}" height="240" fill="#0d0e18" opacity="0.85"/>
<rect x="0" y="840" width="{W}" height="14" fill="#1c1d2a"/>
<rect x="250" y="420" width="12" height="420" fill="#07070c"/><path d="M256 420 q40 -20 80 0" stroke="#07070c" stroke-width="10" fill="none"/>
{glow(336, 440, 60, "#ffd38a", 0.5)}<circle cx="336" cy="436" r="12" fill="#fff1c9"/>
{fog(900, op=0.12)}
''', NIGHT + DEFS)

# S2 — inside: the mirror wall, lights on, mop bucket, switch by the door
bucket = ('<path d="M1380 920 L1400 780 L1540 780 L1560 920 Z" fill="#c9a12a"/><rect x="1390" y="770" width="160" height="16" rx="6" fill="#a9851a"/>'
          '<line x1="1470" y1="780" x2="1430" y2="430" stroke="#2a2420" stroke-width="10"/>'
          '<rect x="1360" y="920" width="220" height="14" fill="#111"/>')
scenes["s2"] = svg(studio(True) + person(1030, 720, 0.75, color="#141018", mop=True, flip=True) + bucket + fog(760, "#ffd8a0", 0.05), DEFS)

# S3 — back to the glass, hand on the switch by the door; reflection in the mirror
door = ('<rect x="1560" y="250" width="200" height="560" fill="#140c0a"/><rect x="1575" y="265" width="170" height="545" fill="#24160f"/>'
        '<circle cx="1590" cy="560" r="8" fill="#a7853f"/>'
        '<rect x="1490" y="470" width="44" height="70" rx="6" fill="#e9dcc0"/><rect x="1504" y="484" width="16" height="22" rx="3" fill="#b9ab90"/>')
scenes["s3"] = svg(studio(True)
                   + person(1110, 720, 0.6, color="#2a2430", arm="switch", mop=False, flip=True)   # reflection, dimmer
                   + door
                   + person(1300, 1040, 1.25, color="#050407", arm="switch", mop=False)
                   + glow(1512, 505, 40, "#fff1c9", 0.3), DEFS)

# S4 — close-up: hand on the switch, phone lighting up in the other hand
scenes["s4"] = svg(f'''
<rect width="{W}" height="{H}" fill="#3a2a20"/>
<rect width="{W}" height="{H}" fill="#000" opacity="0.25"/>
<rect x="1060" y="260" width="300" height="460" rx="26" fill="#e9dcc0"/>
<rect x="1060" y="260" width="300" height="460" rx="26" fill="none" stroke="#b9ab90" stroke-width="6"/>
<rect x="1170" y="380" width="80" height="140" rx="12" fill="#cfc2a6"/><rect x="1180" y="390" width="60" height="60" rx="8" fill="#f6eedc"/>
<circle cx="1210" cy="300" r="8" fill="#a99a80"/><circle cx="1210" cy="680" r="8" fill="#a99a80"/>
<g fill="#0a0708">
<path d="M1500 1080 L1360 620 Q1340 560 1290 560 L1240 470 Q1225 440 1250 430 Q1275 425 1290 450 L1330 520 L1500 520 L1700 1080 Z"/>
<rect x="1300" y="560" width="120" height="44" rx="22"/><rect x="1300" y="610" width="130" height="44" rx="22"/>
</g>
<g transform="rotate(-14 640 720)">
<path d="M380 1080 L460 760 L780 760 L860 1080 Z" fill="#0a0708"/>
<rect x="520" y="420" width="220" height="400" rx="26" fill="#111"/>
<rect x="536" y="440" width="188" height="360" rx="16" fill="#8fc4ff"/>
<rect x="556" y="500" width="150" height="56" rx="10" fill="#e9f4ff"/>
<rect x="566" y="514" width="40" height="28" rx="6" fill="#5a8ed8"/>
<rect x="616" y="516" width="80" height="8" rx="4" fill="#5a8ed8"/><rect x="616" y="530" width="60" height="8" rx="4" fill="#9ab8e0"/>
<rect x="500" y="680" width="120" height="44" rx="22" fill="#0a0708"/><rect x="500" y="730" width="130" height="44" rx="22" fill="#0a0708"/>
</g>
{glow(640, 620, 260, "#8fc4ff", 0.35)}
<g stroke="#8fc4ff" stroke-width="6" fill="none" opacity="0.7" stroke-linecap="round">
<path d="M450 470 q-30 40 0 80"/><path d="M410 440 q-50 70 0 140"/><path d="M830 470 q30 40 0 80"/><path d="M870 440 q50 70 0 140"/></g>
{glow(1210, 450, 160, "#ffd38a", 0.25)}
''', DEFS)

# S5 — lights out, staring into the glass
me_dark = person(1090, 1060, 1.3, color="#020204", mop=False)
refl_dark = person(880, 730, 0.62, color="#1d2440", mop=False)
scenes["s5"] = svg(studio(False) + refl_dark + me_dark + fog(720, "#8fa0d0", 0.06), DEFS)

# S5b — same, but pale ballet shoes tap inside the mirror, behind the reflection
def shoe(x, y, s=1.0, op=0.85):
    return (f'<g opacity="{op}"><path d="M{x} {y} q{-6 * s} {-70 * s} {4 * s} {-110 * s} l{18 * s} 0 q{8 * s} {50 * s} {2 * s} {110 * s} z" fill="#e8c6c8"/>'
            f'<path d="M{x + 6 * s} {y - 90 * s} l{-26 * s} {-30 * s} M{x + 14 * s} {y - 90 * s} l{30 * s} {-30 * s}" stroke="#d8a8ae" stroke-width="{3 * s}"/></g>')
shoes = (shoe(680, 735, 0.8) + shoe(715, 728, 0.8, 0.7) + shoe(560, 732, 0.7, 0.6) + shoe(590, 736, 0.7, 0.8)
         + glow(700, 700, 300, "#e8c6c8", 0.12))
scenes["s5b"] = svg(studio(False) + shoes + refl_dark + me_dark + fog(720, "#8fa0d0", 0.06), DEFS)

# S6 — lights back on: me and my reflection, the reflection a beat behind (arm still down while mine is raised)
refl_face = ''
scenes["s6"] = svg(studio(True)
                   + person(840, 735, 0.62, color="#241e28", arm="down", mop=True)
                   + eyes(840, 735 - 372 * 0.62, gap=16, r=3.5, color=RED)
                   + person(1110, 1060, 1.3, color="#050407", arm="up", mop=True, flip=True)
                   + fog(760, "#ffd8a0", 0.04), DEFS)

# S7 — leaving fast down the street; something in the studio window
scenes["s7"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>{stars(60, 260, 0.5)}
<rect x="300" y="200" width="1320" height="880" fill="#1d1414"/>
<g stroke="#140d0d" stroke-width="3" opacity="0.7">{''.join(f'<line x1="300" y1="{y}" x2="1620" y2="{y}"/>' for y in range(220, 1080, 34))}</g>
<rect x="520" y="360" width="880" height="380" fill="#120d0c"/>
<rect x="550" y="380" width="820" height="340" fill="#0c0f1c"/>
<rect x="580" y="400" width="760" height="260" fill="url(#glassd)"/>
{glow(960, 560, 200, "#8fa0d0", 0.1)}
{person(960, 690, 0.55, color="#000", arm="up", mop=False)}
{eyes(960, 690 - 372 * 0.55, gap=14, r=3.5, color=RED)}
<rect x="700" y="300" width="520" height="50" rx="6" fill="#120d0c"/>
<text x="960" y="338" text-anchor="middle" font-family="{SERIF}" font-size="34" letter-spacing="10" fill="#5a4448">DANCE STUDIO</text>
<rect x="0" y="860" width="{W}" height="220" fill="#0b0c16"/>
<rect x="0" y="860" width="{W}" height="12" fill="#1c1d2a"/>
<rect x="1480" y="380" width="12" height="480" fill="#07070c"/>{glow(1540, 400, 70, "#ffd38a", 0.5)}<circle cx="1540" cy="396" r="12" fill="#fff1c9"/>
<path d="M1486 380 q30 -16 54 0" stroke="#07070c" stroke-width="10" fill="none"/>
<polygon points="1470,1080 1610,1080 1560,420 1520,420" fill="#ffd38a" opacity="0.08"/>
{person(560, 1070, 0.85, color="#030305", mop=False)}
{fog(940, op=0.14)}
''', NIGHT + DEFS)

# S8 — dawn through the front window: the empty studio, and in the mirror, me... dancing
dancer = (f'<g fill="#0a080c">'
          f'<ellipse cx="960" cy="380" rx="22" ry="27"/>'
          f'<path d="M930 420 Q960 405 990 420 L985 560 L935 560 Z"/>'
          f'<path d="M935 560 L955 740" stroke="#0a080c" stroke-width="20" stroke-linecap="round"/>'
          f'<path d="M980 560 L1080 640 L1150 600" stroke="#0a080c" stroke-width="18" stroke-linecap="round" fill="none" stroke-linejoin="round"/>'
          f'<path d="M935 430 Q870 330 920 270 M985 430 Q1050 330 1000 270" stroke="#0a080c" stroke-width="15" fill="none" stroke-linecap="round"/>'
          f'<line x1="920" y1="270" x2="1000" y2="270" stroke="#0a080c" stroke-width="12" stroke-linecap="round"/>'
          f'<path d="M1100 520 L1050 760" stroke="#2a2420" stroke-width="7"/>'
          f'</g>' + eyes(960, 380, gap=14, r=3.5, color=RED))
scenes["s8"] = svg(studio(False, mirror_fill="url(#dawn)")
                   + '<polygon points="300,760 1620,760 1920,1080 0,1080" fill="#7a4a52" opacity="0.18"/>'
                   + dancer
                   + '<path d="M1000 900 q60 -20 120 0 q-60 30 -120 0z" fill="#3a2a20" opacity="0.6"/>'
                   + glow(960, 500, 300, RED, 0.12) + fog(780, "#c08a90", 0.08), DEFS)

for name, s in scenes.items():
    save(name, s)
print("drew", ", ".join(scenes))
