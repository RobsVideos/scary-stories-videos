"""Scenes for The Snowman Rule. Run inside this folder: python3 scenes.py"""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

_save = save


def save(name, markup):
    for b in ("blur8", "blur30", "blur60"):
        markup = markup.replace(f'<filter id="{b}">', f'<filter id="{b}" x="-200%" y="-200%" width="500%" height="500%">')
    _save(name, markup)


def snow(n, op=0.6, ymax=H):
    return "".join(f'<circle cx="{rnd.randint(0, W)}" cy="{rnd.randint(0, ymax)}" r="{rnd.choice([1.5, 2, 2.6, 3.4])}" '
                   f'fill="#eef3fb" opacity="{rnd.uniform(0.25, op):.2f}"/>' for _ in range(n))


def scarf(cx, y, s, back=False):
    r = "#b3261e"; d = "#7c1712"
    tail = (f'<path d="M{cx + 30 * s} {y + 10 * s} l{18 * s} {90 * s} l{-30 * s} {6 * s} l{-14 * s} {-88 * s}Z" fill="{d}"/>'
            if not back else f'<path d="M{cx - 20 * s} {y + 10 * s} l{-10 * s} {95 * s} l{30 * s} {4 * s} l{6 * s} {-92 * s}Z" fill="{d}"/>')
    return (f'<path d="M{cx - 78 * s} {y - 6 * s} Q{cx} {y + 26 * s} {cx + 78 * s} {y - 6 * s} L{cx + 76 * s} {y + 18 * s} '
            f'Q{cx} {y + 50 * s} {cx - 76 * s} {y + 18 * s}Z" fill="{r}"/>{tail}'
            f'<g stroke="{d}" stroke-width="{3 * s}" opacity="0.7">'
            + "".join(f'<line x1="{cx + k * 22 * s}" y1="{y + 2 * s}" x2="{cx + k * 22 * s}" y2="{y + 34 * s}"/>' for k in (-2, -1, 0, 1, 2))
            + '</g>')


def snowman(cx, base, s=1.0, face=True, body="#d9e1ee", shade="#8f9bb4", eye_glint=False, sc=True):
    """Three-ball snowman standing on (cx, base). face=False draws its back."""
    r1, r2, r3 = 120 * s, 88 * s, 64 * s
    y1 = base - r1 * 0.9; y2 = y1 - r1 - r2 * 0.75; y3 = y2 - r2 - r3 * 0.7
    out = [f'<ellipse cx="{cx}" cy="{base}" rx="{r1 * 1.4}" ry="{18 * s}" fill="#000" opacity="0.35" filter="url(#blur8)"/>']
    for (y, r) in ((y1, r1), (y2, r2), (y3, r3)):
        out.append(f'<circle cx="{cx}" cy="{y}" r="{r}" fill="{body}"/>'
                   f'<circle cx="{cx + r * 0.25}" cy="{y + r * 0.2}" r="{r * 0.92}" fill="{shade}" opacity="0.45" '
                   f'clip-path="none" mask="none"/>'
                   f'<circle cx="{cx - r * 0.18}" cy="{y - r * 0.2}" r="{r * 0.75}" fill="{body}"/>')
    # stick arms
    out.append(f'<path d="M{cx - r2 * .9} {y2 - 10 * s} L{cx - 220 * s} {y2 - 90 * s} M{cx - 190 * s} {y2 - 72 * s} l{-20 * s} {-46 * s}" '
               f'stroke="#1a110c" stroke-width="{8 * s}" stroke-linecap="round" fill="none"/>'
               f'<path d="M{cx + r2 * .9} {y2 - 6 * s} L{cx + 225 * s} {y2 - 40 * s} M{cx + 195 * s} {y2 - 36 * s} l{18 * s} {-40 * s}" '
               f'stroke="#1a110c" stroke-width="{8 * s}" stroke-linecap="round" fill="none"/>')
    if face:
        for k in (-1, 1):
            out.append(f'<circle cx="{cx + k * 22 * s}" cy="{y3 - 14 * s}" r="{9 * s}" fill="#0b0b10"/>')
            if eye_glint:
                out.append(f'<circle cx="{cx + k * 22 * s}" cy="{y3 - 14 * s}" r="{3.5 * s}" fill="#ff3b2f"/>'
                           f'<circle cx="{cx + k * 22 * s}" cy="{y3 - 14 * s}" r="{14 * s}" fill="#ff3b2f" opacity="0.45" filter="url(#blur8)"/>')
        out.append(f'<path d="M{cx - 4 * s} {y3 + 2 * s} L{cx + 62 * s} {y3 + 14 * s} L{cx - 2 * s} {y3 + 14 * s}Z" fill="#e0701e"/>')
        out.append("".join(f'<circle cx="{cx + k * 13 * s}" cy="{y3 + 32 * s - abs(k) * 3 * s}" r="{4.5 * s}" fill="#0b0b10"/>' for k in (-2, -1, 0, 1, 2)))
        out.append("".join(f'<circle cx="{cx}" cy="{y2 - r2 * .4 + i * 40 * s}" r="{8 * s}" fill="#0b0b10"/>' for i in range(3)))
    if sc:
        out.append(scarf(cx, y3 + r3 * 0.78, s, back=not face))
    return "".join(out)


def house(x, base, w, h, color="#0a0c14", windows=(), door=None, light=None):
    roof = base - h
    o = [f'<rect x="{x}" y="{roof}" width="{w}" height="{h}" fill="{color}"/>',
         f'<polygon points="{x - 30},{roof + 4} {x + w / 2},{roof - h * 0.55} {x + w + 30},{roof + 4}" fill="{color}"/>',
         f'<polygon points="{x - 34},{roof + 4} {x + w / 2},{roof - h * 0.55 - 14} {x + w + 34},{roof + 4} {x + w + 18},{roof + 4} {x + w / 2},{roof - h * 0.55 + 6} {x - 18},{roof + 4}" fill="#e6ecf6" opacity="0.85"/>']
    for (wx, wy, ww, wh, c) in windows:
        o.append(lit_window(x + wx, roof + wy, ww, wh, c, color) if c else f'<rect x="{x + wx}" y="{roof + wy}" width="{ww}" height="{wh}" fill="#151a28"/>')
    if door:
        dx, dw = door
        o.append(f'<rect x="{x + dx}" y="{base - 130}" width="{dw}" height="130" fill="#05060a"/>')
    if light:
        o.append(glow(x + light, base - 160, 60, "#ffb54a", 0.8) + f'<circle cx="{x + light}" cy="{base - 160}" r="9" fill="#ffd28a"/>')
    return "".join(o)


SKY = sky("sk", "#04060d", "#16203a", "#33405e")
GROUND = "#c9d3e4"

# S1 — the street on the first snow, snowmen in every yard
houses = (house(120, 700, 300, 190, windows=[(40, 40, 60, 70, "#ffb54a"), (200, 40, 60, 70, None)], door=(130, 50)) +
          house(560, 690, 280, 200, windows=[(40, 50, 60, 70, None), (180, 50, 60, 70, "#ffb54a")], door=(120, 50)) +
          house(1000, 700, 320, 210, windows=[(50, 50, 70, 80, "#ffc46a"), (210, 50, 70, 80, "#ffb54a")], door=(140, 50), light=125) +
          house(1480, 690, 300, 190, windows=[(40, 40, 60, 70, None), (200, 40, 60, 70, None)], door=(120, 50)))
lamps = "".join(f'<rect x="{x}" y="560" width="10" height="250" fill="#07080d"/><circle cx="{x + 5}" cy="555" r="10" fill="#ffd28a"/>{glow(x + 5, 560, 70, "#ffb54a", 0.5)}'
                f'<ellipse cx="{x + 5}" cy="830" rx="160" ry="30" fill="#ffd28a" opacity="0.18" filter="url(#blur30)"/>' for x in (440, 940, 1440))
save("s1", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sk)"/>{stars(80, 350, 0.5)}{moon(1500, 170, 70)}
<path d="M0 520 L80 470 L140 520 L210 450 L290 520 L360 480 L440 520 L1500 520 L1580 470 L1650 520 L1730 455 L1820 520 L1920 490 L1920 700 L0 700Z" fill="#0b1020"/>
{houses}
<path d="M0 690 C500 680 1400 685 1920 690 L1920 1080 L0 1080Z" fill="{GROUND}"/>
<path d="M0 820 C600 800 1300 805 1920 820 L1920 900 C1300 890 600 885 0 905Z" fill="#8a96ad"/>
{lamps}
{snowman(270, 790, 0.45)}{snowman(700, 780, 0.42)}{snowman(1160, 795, 0.5)}{snowman(1630, 785, 0.44)}
<path d="M0 1000 C700 970 1300 975 1920 1000 L1920 1080 L0 1080Z" fill="#aeb9cf"/>
{snow(260, 0.75)}
{fog(700, "#c9d3e4", 0.16, 90)}
''', SKY))

# S2 — Mrs. Pell on her porch, finger raised
pell = ('<g fill="#06060a">'
        '<ellipse cx="830" cy="470" rx="38" ry="44"/>'
        '<path d="M790 470 C770 520 770 540 760 560 L900 560 C890 540 890 520 870 470Z"/>'
        '<path d="M770 540 C740 640 730 760 720 840 L940 840 C930 760 920 640 890 540Z"/>'
        '<path d="M880 560 C930 560 950 520 960 470" stroke="#06060a" stroke-width="22" stroke-linecap="round" fill="none"/>'
        '<path d="M960 470 L966 430" stroke="#06060a" stroke-width="10" stroke-linecap="round"/>'
        '<path d="M806 430 C800 400 860 396 860 430" fill="#06060a"/></g>'
        '<path d="M770 520 C760 600 760 720 760 830" stroke="#2a2030" stroke-width="6" fill="none" opacity="0.6"/>')
save("s2", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sk)"/>{stars(50, 250, 0.4)}
<rect x="300" y="160" width="1320" height="700" fill="#1a1622"/>
<g stroke="#120f18" stroke-width="4">{''.join(f'<line x1="300" y1="{y}" x2="1620" y2="{y}"/>' for y in range(190, 860, 38))}</g>
<polygon points="240,170 960,40 1680,170" fill="#0c0a10"/><polygon points="230,176 960,30 1690,176 1660,176 960,58 260,176" fill="#e6ecf6" opacity="0.8"/>
<rect x="1030" y="400" width="190" height="440" fill="#120d0c"/>
{lit_window(1300, 330, 180, 200, "#ffb54a", "#1a1622")}
<circle cx="1120" cy="300" r="14" fill="#ffd28a"/>{glow(1120, 300, 150, "#ffb54a", 0.55)}
<ellipse cx="960" cy="860" rx="520" ry="80" fill="#ffb54a" opacity="0.18" filter="url(#blur30)"/>
{''.join(f'<rect x="{x}" y="180" width="26" height="680" fill="#0d0a10"/>' for x in (330, 680, 1560))}
<rect x="300" y="840" width="1320" height="40" fill="#0f0c12"/>
{''.join(f'<rect x="{x}" y="760" width="12" height="80" fill="#0d0a10"/>' for x in range(320, 1610, 50))}<rect x="300" y="750" width="1320" height="14" fill="#0d0a10"/>
{pell}
<path d="M0 860 C500 850 1400 850 1920 860 L1920 1080 L0 1080Z" fill="{GROUND}"/>
{snowman(1420, 990, 0.62, face=False)}
{snow(200, 0.7)}{fog(900, "#c9d3e4", 0.12, 80)}
''', SKY))

# S3 — my snowman, facing the road, house behind
save("s3", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sk3)"/>{stars(70, 350, 0.5)}
{house(620, 640, 680, 330, color="#0c0e18", windows=[(80, 70, 120, 140, "#ffb54a"), (480, 70, 120, 140, None)], door=(300, 80), light=340)}
{dead_tree(380, 660, 380, "#090b12")}
<path d="M0 640 C600 630 1300 630 1920 640 L1920 1080 L0 1080Z" fill="{GROUND}"/>
<path d="M0 640 C600 630 1300 630 1920 640 L1920 700 C1300 680 600 680 0 700Z" fill="#9aa6bd"/>
<path d="M880 640 L1040 640 L1240 1080 L680 1080Z" fill="#aab5ca"/>
{snowman(960, 990, 1.25)}
{snow(240, 0.75)}{fog(660, "#c9d3e4", 0.14, 80)}
''', sky("sk3", "#060a16", "#1c2a48", "#4a5a7c")))

# S4 — waking up cold, bedroom, frosted window
frost = "".join(f'<path d="M{x} {y} l{rnd.randint(-30, 30)} {rnd.randint(-30, 30)}" stroke="#dfe8f5" stroke-width="2" opacity="0.5"/>' for x, y in
                [(rnd.randint(780, 1140), rnd.choice([rnd.randint(250, 300), rnd.randint(560, 620)])) for _ in range(90)])
save("s4", svg(f'''
<rect width="{W}" height="{H}" fill="#0a0d16"/>
<rect x="0" y="760" width="{W}" height="320" fill="#0d1019"/>
<rect x="760" y="230" width="400" height="400" fill="#1a2440"/>
<rect x="760" y="230" width="400" height="400" fill="url(#win4)"/>
<circle cx="1060" cy="310" r="40" fill="#e9eef8" opacity="0.8"/>
{frost}
<rect x="752" y="222" width="416" height="416" fill="none" stroke="#06070c" stroke-width="18"/>
<line x1="960" y1="230" x2="960" y2="630" stroke="#06070c" stroke-width="12"/><line x1="760" y1="430" x2="1160" y2="430" stroke="#06070c" stroke-width="12"/>
<rect x="740" y="630" width="440" height="22" fill="#06070c"/>
<polygon points="760,652 1160,652 1420,1080 500,1080" fill="#a9c1ee" opacity="0.10"/>
<g fill="#06070c"><rect x="340" y="640" width="30" height="300"/><rect x="340" y="760" width="760" height="150" rx="10"/>
<path d="M370 740 C500 700 800 700 1100 740 L1100 790 L370 790Z" fill="#141a2a"/>
<ellipse cx="460" cy="730" rx="90" ry="34" fill="#1c2235"/></g>
<path d="M520 720 C600 690 700 690 780 720" stroke="#2a3350" stroke-width="5" fill="none"/>
<g opacity="0.35"><ellipse cx="520" cy="660" rx="40" ry="18" fill="#dfe8f5" filter="url(#blur8)"/><ellipse cx="560" cy="630" rx="30" ry="14" fill="#dfe8f5" filter="url(#blur8)"/></g>
<g transform="translate(1400 420)"><rect x="0" y="0" width="200" height="220" rx="8" fill="#10131c"/>
<g stroke="#1b2030" stroke-width="10">{''.join(f'<line x1="20" y1="{y}" x2="180" y2="{y}"/>' for y in range(30, 210, 30))}</g></g>
{glow(1500, 520, 120, "#7aa0ff", 0.12)}
''', '<linearGradient id="win4" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a3a64"/><stop offset="1" stop-color="#7f93be"/></linearGradient>'))


# S5 / S5b — looking down from the window at the snowman (facing the house / turned back)
def window_view(face, glint):
    return svg(f'''
<rect width="{W}" height="{H}" fill="url(#sk5)"/>
<path d="M0 420 C600 400 1300 405 1920 420 L1920 1080 L0 1080Z" fill="{GROUND}"/>
<path d="M0 420 L1920 420 L1920 470 L0 470Z" fill="#7d89a2"/>
<rect x="0" y="380" width="{W}" height="40" fill="#0b0e18"/>
{''.join(f'<rect x="{x}" y="300" width="12" height="90" fill="#0b0e18"/>' for x in range(0, 1920, 70))}
<path d="M0 800 L1920 640 L1920 700 L0 900Z" fill="#a9b4ca" opacity="0.7"/>
{snowman(960, 960, 1.2, face=face, eye_glint=glint)}
{glow(960, 560, 260, "#c9d6ff", 0.10)}
{snow(200, 0.7)}
<rect x="0" y="0" width="560" height="{H}" fill="#05060a"/><rect x="1360" y="0" width="560" height="{H}" fill="#05060a"/>
<rect x="0" y="0" width="{W}" height="110" fill="#05060a"/><rect x="0" y="990" width="{W}" height="90" fill="#05060a"/>
<rect x="540" y="100" width="840" height="900" fill="none" stroke="#0e0f16" stroke-width="40"/>
<line x1="560" y1="250" x2="1360" y2="250" stroke="#0e0f16" stroke-width="22" opacity="0.9"/>
<rect x="560" y="110" width="800" height="880" fill="#9fb4e8" opacity="0.05"/>
<path d="M560 110 L760 110 L560 300Z M1360 990 L1160 990 L1360 820Z" fill="#dfe8f5" opacity="0.18"/>
''', sky("sk5", "#0b1222", "#1f2c4a", "#3b4a6e"))


save("s5", window_view(True, True))
save("s5b", window_view(False, False))

# S6 — empty yard, round heavy prints to the front door
prints = "".join(f'<ellipse cx="{960 + (i % 2) * 40 - 20 + (i * 6)}" cy="{990 - i * 38}" rx="{40 - i * 2}" ry="{14 - i * 0.6}" fill="#5f6b86"/>'
                 f'<ellipse cx="{960 + (i % 2) * 40 - 20 + (i * 6)}" cy="{986 - i * 38}" rx="{34 - i * 2}" ry="{10 - i * 0.5}" fill="#3e4862"/>' for i in range(9))
save("s6", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sk)"/>{stars(60, 250, 0.4)}
<rect x="560" y="140" width="800" height="520" fill="#0c0e18"/>
<polygon points="520,150 960,-20 1400,150" fill="#0c0e18"/>
{lit_window(620, 220, 140, 160, None or "#26314f", "#0c0e18")}{lit_window(1160, 220, 140, 160, "#26314f", "#0c0e18")}
<rect x="900" y="420" width="140" height="240" fill="#1a1210"/>
<circle cx="1018" cy="545" r="8" fill="#a7853f"/>
<circle cx="1090" cy="380" r="12" fill="#ffd28a"/>{glow(1090, 380, 160, "#ffb54a", 0.6)}
<polygon points="860,660 1080,660 1140,720 800,720" fill="#0b0d16"/>
<path d="M0 680 C600 670 1300 670 1920 680 L1920 1080 L0 1080Z" fill="{GROUND}"/>
<ellipse cx="1000" cy="760" rx="380" ry="60" fill="#ffb54a" opacity="0.15" filter="url(#blur30)"/>
{prints}
<ellipse cx="900" cy="1000" rx="150" ry="40" fill="#8f9bb4"/><path d="M790 1000 Q860 950 900 980 Q950 940 1010 995" fill="#b9c4d8"/>
<path d="M870 990 L850 940 M930 990 L970 950" stroke="#1a110c" stroke-width="7" stroke-linecap="round"/>
{snow(200, 0.7)}{fog(700, "#c9d3e4", 0.12, 80)}
''', SKY))

# S7 — the hallway: the snowman facing my bedroom door
boards = "".join(f'<line x1="960" y1="640" x2="{x}" y2="1080" stroke="#0e0d12" stroke-width="3"/>' for x in range(-600, 2600, 160))
save("s7", svg(f'''
<rect width="{W}" height="{H}" fill="#0a0a10"/>
<polygon points="0,0 740,300 740,640 0,1080" fill="url(#wl)"/>
<polygon points="1920,0 1180,300 1180,640 1920,1080" fill="url(#wr)"/>
<polygon points="0,0 1920,0 1180,300 740,300" fill="#06060a"/>
<polygon points="0,1080 740,640 1180,640 1920,1080" fill="#16141c"/>
<g clip-path="url(#fl)">{boards}</g>
<rect x="740" y="300" width="440" height="340" fill="#121220"/>
<rect x="840" y="330" width="240" height="310" fill="#1d1612"/>
<rect x="860" y="350" width="200" height="130" fill="none" stroke="#120d0b" stroke-width="5"/>
<rect x="860" y="500" width="200" height="120" fill="none" stroke="#120d0b" stroke-width="5"/>
<circle cx="1050" cy="500" r="7" fill="#a7853f"/>
<rect x="845" y="634" width="230" height="6" fill="#ffb54a" opacity="0.9"/>
<ellipse cx="960" cy="1010" rx="300" ry="50" fill="#6f8fc8" opacity="0.35"/>
<ellipse cx="960" cy="1010" rx="300" ry="50" fill="#9fb4e8" opacity="0.25" filter="url(#blur8)"/>
{snowman(960, 1000, 0.95, face=False, body="#7f8aa3", shade="#2c3346")}
<rect x="0" y="0" width="{W}" height="{H}" fill="#2a3a64" opacity="0.18"/>
{glow(960, 640, 160, "#ffb54a", 0.12)}
''', '''<linearGradient id="wl" x1="0" x2="1"><stop offset="0" stop-color="#1e1c28"/><stop offset="1" stop-color="#0f0e16"/></linearGradient>
<linearGradient id="wr" x1="1" x2="0"><stop offset="0" stop-color="#1e1c28"/><stop offset="1" stop-color="#0f0e16"/></linearGradient>
<clipPath id="fl"><polygon points="0,1080 740,640 1180,640 1920,1080"/></clipPath>'''))
print("ok")
