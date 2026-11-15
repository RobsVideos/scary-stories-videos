"""The Last Chair — scenes for a ski lift at night in heavy snow."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

INK = "#06070c"
SNOW = "#dfe6f2"


def snowfall(n, op=(0.25, 0.85), r=(1.2, 4.2), y0=0, y1=H):
    return "".join(f'<circle cx="{rnd.randint(0, W)}" cy="{rnd.randint(y0, y1)}" r="{rnd.uniform(*r):.1f}" '
                   f'fill="{SNOW}" opacity="{rnd.uniform(*op):.2f}"/>' for _ in range(n))


def pine(x, base, h, color=INK):
    w = h * 0.36
    tiers = []
    for i in range(4):
        top = base - h + i * h * 0.2
        bw = w * (0.45 + i * 0.2)
        tiers.append(f'<polygon points="{x},{top:.0f} {x - bw:.0f},{top + h * 0.32:.0f} {x + bw:.0f},{top + h * 0.32:.0f}"/>')
    return f'<g fill="{color}">{"".join(tiers)}<rect x="{x - h * .03:.0f}" y="{base - h * .1:.0f}" width="{h * .06:.0f}" height="{h * .1:.0f}"/></g>'


def tower(x, base, h, color=INK, s=1.0, lamp=False):
    top = base - h
    out = (f'<g fill="{color}"><polygon points="{x - 16 * s:.0f},{base} {x + 16 * s:.0f},{base} {x + 8 * s:.0f},{top} {x - 8 * s:.0f},{top}"/>'
           f'<rect x="{x - 90 * s:.0f}" y="{top - 6 * s:.0f}" width="{180 * s:.0f}" height="{12 * s:.0f}"/>'
           f'<circle cx="{x - 70 * s:.0f}" cy="{top + 10 * s:.0f}" r="{12 * s:.0f}"/><circle cx="{x + 70 * s:.0f}" cy="{top + 10 * s:.0f}" r="{12 * s:.0f}"/>'
           f'<rect x="{x - 4 * s:.0f}" y="{top - 40 * s:.0f}" width="{8 * s:.0f}" height="{36 * s:.0f}"/></g>')
    if lamp:
        out += glow(x, top - 44 * s, 40 * s, "#ffcf7a", 0.55) + f'<circle cx="{x}" cy="{top - 44 * s:.0f}" r="{6 * s:.0f}" fill="#ffe2a8"/>'
    return out


def chair(x, y, s=1.0, color="#0b0d14", rider=False, bar=True, snowcap=True):
    """Front view of a double chair hanging from a grip at (x, y)."""
    sw = max(2, 8 * s)
    p = []
    p.append(f'<rect x="{x - 14 * s:.0f}" y="{y - 10 * s:.0f}" width="{28 * s:.0f}" height="{22 * s:.0f}" rx="{4 * s:.0f}" fill="{color}"/>')
    p.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y + 150 * s:.0f}" stroke="{color}" stroke-width="{sw:.0f}"/>')
    p.append(f'<path d="M{x - 95 * s:.0f} {y + 275 * s:.0f} L{x - 95 * s:.0f} {y + 165 * s:.0f} Q{x - 95 * s:.0f} {y + 150 * s:.0f} {x - 80 * s:.0f} {y + 150 * s:.0f} '
             f'L{x + 80 * s:.0f} {y + 150 * s:.0f} Q{x + 95 * s:.0f} {y + 150 * s:.0f} {x + 95 * s:.0f} {y + 165 * s:.0f} L{x + 95 * s:.0f} {y + 275 * s:.0f}" '
             f'fill="none" stroke="{color}" stroke-width="{sw:.0f}"/>')
    p.append(f'<rect x="{x - 88 * s:.0f}" y="{y + 190 * s:.0f}" width="{176 * s:.0f}" height="{52 * s:.0f}" rx="{6 * s:.0f}" fill="{color}"/>')
    if rider:
        R = "#020203"
        # torso from seat up to slumped shoulders, head bowed forward above the backrest
        p.append(f'<path d="M{x - 60 * s:.0f} {y + 270 * s:.0f} C{x - 66 * s:.0f} {y + 220 * s:.0f} {x - 62 * s:.0f} {y + 182 * s:.0f} {x - 30 * s:.0f} {y + 172 * s:.0f} '
                 f'L{x + 30 * s:.0f} {y + 172 * s:.0f} C{x + 62 * s:.0f} {y + 182 * s:.0f} {x + 66 * s:.0f} {y + 220 * s:.0f} {x + 60 * s:.0f} {y + 270 * s:.0f} Z" fill="{R}"/>')
        p.append(f'<rect x="{x - 12 * s:.0f}" y="{y + 158 * s:.0f}" width="{24 * s:.0f}" height="{20 * s:.0f}" fill="{R}"/>')
        p.append(f'<ellipse cx="{x}" cy="{y + 160 * s:.0f}" rx="{25 * s:.0f}" ry="{29 * s:.0f}" fill="{R}"/>')
        p.append(f'<path d="M{x - 40 * s:.0f} {y + 280 * s:.0f} L{x - 36 * s:.0f} {y + 365 * s:.0f} M{x + 40 * s:.0f} {y + 280 * s:.0f} L{x + 36 * s:.0f} {y + 365 * s:.0f}" stroke="{R}" stroke-width="{24 * s:.0f}" stroke-linecap="round"/>')
        p.append(f'<path d="M{x - 52 * s:.0f} {y + 190 * s:.0f} C{x - 70 * s:.0f} {y + 240 * s:.0f} {x - 70 * s:.0f} {y + 280 * s:.0f} {x - 66 * s:.0f} {y + 320 * s:.0f} '
                 f'M{x + 52 * s:.0f} {y + 190 * s:.0f} C{x + 70 * s:.0f} {y + 240 * s:.0f} {x + 70 * s:.0f} {y + 280 * s:.0f} {x + 66 * s:.0f} {y + 320 * s:.0f}" '
                 f'stroke="{R}" stroke-width="{11 * s:.0f}" fill="none" stroke-linecap="round"/>')
        if snowcap:
            p.append(f'<path d="M{x - 23 * s:.0f} {y + 146 * s:.0f} Q{x} {y + 122 * s:.0f} {x + 23 * s:.0f} {y + 146 * s:.0f} Q{x} {y + 138 * s:.0f} {x - 23 * s:.0f} {y + 146 * s:.0f}Z" fill="{SNOW}" opacity="0.85"/>')
            for sg in (-1, 1):
                p.append(f'<path d="M{x + sg * 62 * s:.0f} {y + 192 * s:.0f} Q{x + sg * 46 * s:.0f} {y + 170 * s:.0f} {x + sg * 26 * s:.0f} {y + 172 * s:.0f} L{x + sg * 28 * s:.0f} {y + 178 * s:.0f} Q{x + sg * 46 * s:.0f} {y + 180 * s:.0f} {x + sg * 62 * s:.0f} {y + 198 * s:.0f}Z" fill="{SNOW}" opacity="0.7"/>')
    p.append(f'<rect x="{x - 100 * s:.0f}" y="{y + 266 * s:.0f}" width="{200 * s:.0f}" height="{18 * s:.0f}" rx="{5 * s:.0f}" fill="{color}"/>')
    if snowcap:
        p.append(f'<rect x="{x - 98 * s:.0f}" y="{y + 261 * s:.0f}" width="{196 * s:.0f}" height="{7 * s:.0f}" rx="{3 * s:.0f}" fill="{SNOW}" opacity="0.55"/>')
        p.append(f'<rect x="{x - 86 * s:.0f}" y="{y + 186 * s:.0f}" width="{172 * s:.0f}" height="{6 * s:.0f}" rx="{3 * s:.0f}" fill="{SNOW}" opacity="0.45"/>')
    if bar:
        p.append(f'<line x1="{x - 95 * s:.0f}" y1="{y + 226 * s:.0f}" x2="{x + 95 * s:.0f}" y2="{y + 226 * s:.0f}" stroke="{color}" stroke-width="{max(2, 6 * s):.0f}"/>')
        p.append(f'<path d="M{x - 50 * s:.0f} {y + 226 * s:.0f} L{x - 50 * s:.0f} {y + 330 * s:.0f} L{x + 50 * s:.0f} {y + 330 * s:.0f} L{x + 50 * s:.0f} {y + 226 * s:.0f}" fill="none" stroke="{color}" stroke-width="{max(2, 5 * s):.0f}"/>')
    return "".join(p)


def cable(x1, y1, x2, y2, sag=30, color="#05060a", w=4):
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2 + sag
    return f'<path d="M{x1} {y1} Q{mx:.0f} {my:.0f} {x2} {y2}" stroke="{color}" stroke-width="{w}" fill="none"/>'


def hut(x, y, w=360, h=250, door_open=False, color="#0a0b12"):
    roof = f'<polygon points="{x - 30},{y} {x + w / 2:.0f},{y - 110} {x + w + 30},{y}" fill="{color}"/>'
    snowroof = f'<polygon points="{x - 34},{y + 2} {x + w / 2:.0f},{y - 116} {x + w + 34},{y + 2} {x + w + 20},{y + 8} {x + w / 2:.0f},{y - 98} {x - 20},{y + 8}" fill="{SNOW}" opacity="0.75"/>'
    body = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"/>'
    win = lit_window(x + 40, y + 60, 110, 90, "#ffb54a", color)
    dx = x + w - 140
    if door_open:
        door = (f'<rect x="{dx}" y="{y + 60}" width="90" height="{h - 60}" fill="#ffb54a"/>'
                f'<rect x="{dx}" y="{y + 60}" width="90" height="{h - 60}" fill="#ffb54a" filter="url(#blur30)" opacity="0.7"/>'
                f'<polygon points="{dx + 90},{y + 60} {dx + 128},{y + 46} {dx + 128},{y + h + 12} {dx + 90},{y + h}" fill="#1a1410"/>')
    else:
        door = f'<rect x="{dx}" y="{y + 60}" width="90" height="{h - 60}" fill="#14100e"/>'
    return roof + body + snowroof + win + door


scenes = {}

# S1 — ski hill at night: towers climbing the slope, base hut lit
towers = [(470, 860, 330), (900, 690, 300), (1290, 545, 270), (1620, 425, 240), (1880, 330, 210)]
tw = "".join(tower(x, b, h, "#080a12", s=h / 330) for x, b, h in towers)
cab = "".join(cable(towers[i][0] - 70 * towers[i][2] / 330, towers[i][1] - towers[i][2] + 10, towers[i + 1][0] - 70 * towers[i + 1][2] / 330, towers[i + 1][1] - towers[i + 1][2] + 10, 26) +
              cable(towers[i][0] + 70 * towers[i][2] / 330, towers[i][1] - towers[i][2] + 10, towers[i + 1][0] + 70 * towers[i + 1][2] / 330, towers[i + 1][1] - towers[i + 1][2] + 10, 26)
              for i in range(len(towers) - 1))
chairs1 = ""
for i in range(len(towers) - 1):
    (xa, ba, ha), (xb, bb, hb) = towers[i], towers[i + 1]
    for f in (0.33, 0.68):
        s = (ha + (hb - ha) * f) / 330 * 0.42
        cx = xa + (xb - xa) * f - 70 * s / 0.42 * (ha + (hb - ha) * f) / 330 * 0
        x = xa - 70 * ha / 330 + ((xb - 70 * hb / 330) - (xa - 70 * ha / 330)) * f
        y = (ba - ha + 10) + ((bb - hb + 10) - (ba - ha + 10)) * f + 26 * 4 * f * (1 - f) / 2
        chairs1 += chair(x, y, s, "#080a12", snowcap=False)
scenes["s1"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(120, 420, 0.5)}
{moon(1500, 170, 70)}
<ellipse cx="1300" cy="200" rx="600" ry="70" fill="#1d2234" opacity="0.8" filter="url(#blur30)"/>
<path d="M0 520 L380 300 L620 410 L980 160 L1340 330 L1640 120 L1920 260 L1920 1080 L0 1080Z" fill="#1a2033"/>
<path d="M980 160 L1050 240 L1010 250 L1090 330 L980 300Z M1640 120 L1700 190 L1660 196 L1730 260 L1630 230Z" fill="#cfd8ea" opacity="0.18"/>
<path d="M0 1000 L0 900 C300 860 700 760 1100 600 C1400 480 1700 380 1920 300 L1920 1080 L0 1080Z" fill="#2b3348"/>
<path d="M0 1000 C300 950 700 860 1100 700 C1400 580 1700 470 1920 400 L1920 300 C1700 380 1400 480 1100 600 C700 760 300 860 0 900Z" fill="#3a445e" opacity="0.6"/>
{''.join(pine(x, b, h, "#070910") for x, b, h in [(40, 960, 260), (150, 930, 200), (1180, 680, 180), (1260, 640, 150), (1460, 560, 160), (1750, 470, 130), (1820, 450, 110), (700, 820, 120)])}
{tw}{cab}{chairs1}
{hut(560, 800, 300, 200)}
<path d="M0 1010 C400 990 900 1010 1920 980 L1920 1080 L0 1080Z" fill="#1c2232"/>
{fog(880, "#b8c3dc", 0.12)}
{snowfall(160, (0.2, 0.6), (1, 3))}
''', sky("sky1", "#04050c", "#141a2e", "#2c3550"))

# S2 — heavy snow, towers vanishing up the slope into white
tw2 = ""
for i, (x, b, h, op) in enumerate([(700, 1000, 520, 1), (900, 760, 380, .7), (1060, 590, 280, .45), (1180, 470, 210, .25), (1270, 380, 160, .12)]):
    tw2 += f'<g opacity="{op}">{tower(x, b, h, "#070810", s=h / 330, lamp=(i == 0))}</g>'
scenes["s2"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky2)"/>
<path d="M0 1080 L0 900 C400 820 800 620 1300 360 L1920 200 L1920 1080Z" fill="#323a52"/>
<ellipse cx="1150" cy="420" rx="700" ry="260" fill="#aeb8d0" opacity="0.35" filter="url(#blur60)"/>
{cable(630, 490, 892, 390, 30, "#070810", 5)}{cable(892, 390, 1053, 318, 20, "#070810", 4)}
{cable(770, 490, 948, 390, 30, "#070810", 5)}{cable(948, 390, 1110, 318, 20, "#070810", 4)}
{tw2}
<g opacity="0.75">{chair(800, 410, 0.55, "#070810")}</g>
<g opacity="0.35">{chair(990, 330, 0.36, "#070810")}</g>
{''.join(pine(x, b, h, "#06070d") for x, b, h in [(300, 1000, 380), (420, 1030, 300), (1500, 1060, 420), (1640, 1040, 340)])}
<path d="M0 1080 L0 1000 C500 960 1300 980 1920 950 L1920 1080Z" fill="#9aa5c0" opacity="0.4"/>
{fog(600, "#c8d2e8", 0.22, 200)}
{snowfall(700, (0.3, 0.95), (1.5, 5.5))}
''', sky("sky2", "#0b0e1a", "#2a3249", "#4a5470"))

# S3 — empty chairs stopped on the cable at the base station, red STOP light
row = "".join(f'<g opacity="{op}">{chair(x, y, s, "#090b12")}</g>' for x, y, s, op in [(560, 200, 1.05, 1), (960, 230, 0.9, 1), (1330, 255, 0.75, 0.9), (1640, 275, 0.6, 0.7)])
scenes["s3"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky3)"/>
{cable(-40, 195, 1960, 270, 40, "#05060a", 7)}
{row}
<path d="M0 880 C500 860 1300 870 1920 850 L1920 1080 L0 1080Z" fill="#283048"/>
<path d="M0 880 C500 860 1300 870 1920 850" stroke="#566384" stroke-width="5" fill="none" opacity="0.6"/>
<g transform="translate(1230 640)">
<rect x="0" y="0" width="150" height="250" rx="8" fill="#0d0f17"/>
<rect x="20" y="24" width="110" height="70" rx="4" fill="#161a26"/>
<circle cx="75" cy="140" r="26" fill="#ff3b2f"/>
<circle cx="75" cy="140" r="60" fill="#ff3b2f" opacity="0.5" filter="url(#blur30)"/>
<rect x="45" y="190" width="60" height="20" rx="4" fill="#2a2f3e"/>
<rect x="-4" y="-8" width="158" height="12" rx="5" fill="{SNOW}" opacity="0.7"/>
</g>
{glow(1305, 780, 260, "#ff3b2f", 0.12)}
{fog(820, "#aab3c8", 0.14)}
{snowfall(320, (0.25, 0.85), (1.2, 4))}
''', sky("sky3", "#04050b", "#121726", "#262d42"))

# S4 — one chair coming down out of the dark, someone sitting in it
scenes["s4"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky4)"/>
<path d="M0 1080 L0 760 C500 620 1100 380 1920 120 L1920 1080Z" fill="#1d2335"/>
{tower(1500, 520, 420, "#05060b", s=1.1)}
{cable(1423, 112, 400, 600, 60, "#04050a", 5)}
{cable(1577, 112, 600, 640, 60, "#04050a", 5)}
{glow(960, 420, 280, "#7f8fb8", 0.12)}
{chair(960, 335, 0.95, "#06070c", rider=True)}
{''.join(pine(x, b, h, "#05060b") for x, b, h in [(200, 960, 360), (330, 1000, 280), (1700, 900, 300), (1820, 940, 380)])}
{fog(700, "#9aa6c4", 0.16, 160)}
{snowfall(380, (0.25, 0.85), (1.2, 4.5))}
''', sky("sky4", "#020309", "#0d1120", "#1c2236"))

# S5 — close: chair stopped at the platform under the lamp, rider waiting
scenes["s5"] = svg(f'''
<rect width="{W}" height="{H}" fill="#05060b"/>
<polygon points="760,0 1160,0 1500,1080 420,1080" fill="#ffcf8a" opacity="0.06" filter="url(#blur30)"/>
{glow(960, 30, 180, "#ffcf7a", 0.45)}
<rect x="900" y="0" width="120" height="26" fill="#0d0e14"/>
{cable(-40, 60, 1960, 60, 4, "#030306", 8)}
<path d="M0 900 L1920 900 L1920 1080 L0 1080Z" fill="#1e2232"/>
<rect x="0" y="895" width="1920" height="10" fill="{SNOW}" opacity="0.35"/>
<polygon points="620,900 1300,900 1420,1080 500,1080" fill="#ffcf8a" opacity="0.08"/>
{chair(960, 60, 1.95, "#07080d", rider=True)}
<ellipse cx="960" cy="925" rx="230" ry="18" fill="#000" opacity="0.6" filter="url(#blur8)"/>
{snowfall(260, (0.3, 0.9), (1.5, 5))}
''')

# S6 — the chair carried back up into the snow, small and fading
scenes["s6"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky6)"/>
<path d="M0 1080 L0 980 C500 820 1100 520 1920 240 L1920 1080Z" fill="#2a3249"/>
{cable(380, 1000, 1500, 260, 80, "#05060b", 6)}
{cable(560, 1040, 1660, 290, 80, "#05060b", 6)}
<g opacity="0.85">{chair(1150, 440, 0.55, "#05060b", rider=True)}</g>
{tower(380, 1100, 300, "#04050a", s=1.6)}
{''.join(pine(x, b, h, "#05060b") for x, b, h in [(1600, 760, 200), (1700, 720, 170), (150, 1000, 300)])}
<ellipse cx="1500" cy="300" rx="600" ry="260" fill="#b8c3dc" opacity="0.32" filter="url(#blur60)"/>
{fog(500, "#c8d2e8", 0.16, 200)}
{snowfall(500, (0.3, 0.9), (1.4, 5))}
''', sky("sky6", "#070912", "#1d2438", "#3a4562"))

# S7 — the radio in a gloved hand, green call light, snow
scenes["s7"] = svg(f'''
<rect width="{W}" height="{H}" fill="#06070c"/>
{glow(960, 600, 420, "#3a4870", 0.25)}
<g transform="translate(960 560) rotate(-8)">
<rect x="-14" y="-430" width="28" height="200" rx="12" fill="#0e1016"/>
<rect x="-120" y="-250" width="240" height="560" rx="34" fill="#151821"/>
<rect x="-120" y="-250" width="240" height="560" rx="34" fill="none" stroke="#252a38" stroke-width="6"/>
<rect x="-80" y="-200" width="160" height="90" rx="8" fill="#0b2a1c"/>
<rect x="-80" y="-200" width="160" height="90" rx="8" fill="#3dff9a" opacity="0.18"/>
<text x="0" y="-140" text-anchor="middle" font-family="{MONO}" font-size="40" fill="#3dff9a">CH 2</text>
<g fill="#0b0d13">{''.join(f'<rect x="-80" y="{y}" width="160" height="12" rx="6"/>' for y in range(-70, 120, 30))}</g>
<circle cx="70" cy="-226" r="10" fill="#ff3b2f"/>
<circle cx="70" cy="-226" r="30" fill="#ff3b2f" opacity="0.6" filter="url(#blur8)"/>
<rect x="-160" y="-30" width="60" height="140" rx="20" fill="#232838"/>
</g>
<path d="M330 1080 C380 900 520 800 700 760 C780 740 860 760 880 800 L900 1080Z" fill="#0f1119"/>
<path d="M700 760 C760 700 860 690 900 720 C930 745 900 790 860 800 Z" fill="#141722"/>
<path d="M1200 1080 C1180 920 1140 820 1080 780 C1040 750 1000 770 1010 800 L1060 1080Z" fill="#0f1119"/>
{''.join(f'<rect x="{x}" y="{y}" width="120" height="44" rx="22" fill="#141722" transform="rotate(-8 {x} {y})"/>' for x, y in [(1010, 520), (1020, 580), (1015, 640), (1005, 700)])}
{snowfall(260, (0.3, 0.9), (1.5, 5))}
''')

# S8 — footprints across fresh snow, right into the lit hut. None come back out.
prints = ""
for i in range(14):
    t = i / 13
    x = 760 + (1140 - 760) * t + (18 if i % 2 else -18) * (1 - t * 0.6)
    y = 1065 - (1065 - 778) * t
    s = 1 - t * 0.7
    prints += f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{20 * s:.1f}" ry="{9 * s:.1f}" fill="#0b0e18" transform="rotate({-10 if i % 2 else 10} {x:.0f} {y:.0f})"/>'
    prints += f'<ellipse cx="{x:.0f}" cy="{y + 4 * s:.0f}" rx="{20 * s:.1f}" ry="{5 * s:.1f}" fill="#9aa6c4" opacity="0.5" transform="rotate({-10 if i % 2 else 10} {x:.0f} {y:.0f})"/>'
scenes["s8"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky8)"/>
{''.join(pine(x, b, h, "#05060b") for x, b, h in [(560, 760, 420), (680, 760, 330), (1500, 760, 440), (1640, 760, 360), (420, 760, 300)])}
<path d="M0 760 L1920 760 L1920 1080 L0 1080Z" fill="#8a96b6"/>
<path d="M0 760 L1920 760 L1920 1080 L0 1080Z" fill="url(#snowg)"/>
{hut(880, 520, 360, 250, door_open=True)}
<polygon points="1100,770 1190,770 1290,1080 1060,1080" fill="#ffb54a" opacity="0.16"/>
{prints}
{figure(1145, 770, 175, "#050304")}
{fog(760, "#c8d2e8", 0.12)}
{snowfall(300, (0.3, 0.9), (1.4, 4.6))}
''', sky("sky8", "#03040a", "#111628", "#232b42") +
   '<linearGradient id="snowg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a5576"/><stop offset="1" stop-color="#2a3149"/></linearGradient>')

for name, s in scenes.items():
    save(name, s)
print("drew", ", ".join(scenes))
