"""The Last Reel — scenes for an old drive-in theater after the last movie."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

INK = "#05060b"
FOGWIN = "#d3d9e4"


def car(x, base, s=1.0, color="#07080d", fogged=False, rider=False, wave=False, flip=False):
    """Side view of an old sedan, front to the left (or right with flip). Ground at base."""
    sx = -s if flip else s
    p = [f'<g transform="translate({x},{base}) scale({sx},{s})">']
    p.append(f'<ellipse cx="0" cy="2" rx="280" ry="16" fill="#000" opacity="0.5" filter="url(#blur8)"/>')
    p.append(f'<path d="M-262 -40 L-262 -92 Q-258 -112 -228 -114 L-140 -120 L-92 -182 Q-82 -192 -60 -192 L82 -192 '
             f'Q102 -192 116 -178 L168 -122 L238 -114 Q264 -110 264 -88 L264 -40 Z" fill="{color}"/>')
    # chrome line + bumpers
    p.append('<path d="M-258 -78 L262 -78" stroke="#2a2f3d" stroke-width="3" opacity="0.8"/>')
    p.append(f'<rect x="-272" y="-56" width="22" height="14" rx="4" fill="{color}"/><rect x="252" y="-56" width="22" height="14" rx="4" fill="{color}"/>')
    # windows
    win_front = "M-84 -178 L-8 -178 L-8 -126 L-130 -126 Z"
    win_rear = "M4 -178 L78 -178 Q94 -178 106 -166 L144 -126 L4 -126 Z"
    if fogged:
        for d in (win_front, win_rear):
            p.append(f'<path d="{d}" fill="{FOGWIN}" opacity="0.88"/>')
            p.append(f'<path d="{d}" fill="{FOGWIN}" opacity="0.5" filter="url(#blur8)"/>')
        # condensation drips
        for dx in (-70, -48, -30, 20, 44, 70, 96):
            p.append(f'<path d="M{dx} -150 L{dx} {-130 - (dx % 7)}" stroke="#8d96a8" stroke-width="2" opacity="0.6"/>')
        if rider:
            # blurred head and shoulders behind the fog (driver seat = front window)
            p.append('<g opacity="0.75" filter="url(#blur8)"><ellipse cx="-44" cy="-150" rx="20" ry="24" fill="#1a1d26"/>'
                     '<path d="M-84 -126 Q-80 -146 -44 -128 Q-10 -146 -8 -126Z" fill="#1a1d26"/></g>')
        if wave:
            # a palm pressed and wiping a clear patch in the fog
            p.append('<g transform="translate(-30,-155) scale(1.45) translate(30,155)">')
            p.append('<ellipse cx="-30" cy="-158" rx="22" ry="16" fill="#0d0f15" opacity="0.85" filter="url(#blur8)"/>')
            p.append('<g fill="#0a0b10"><ellipse cx="-30" cy="-148" rx="11" ry="12"/>'
                     '<rect x="-40" y="-172" width="5" height="18" rx="2.5"/><rect x="-33" y="-176" width="5" height="22" rx="2.5"/>'
                     '<rect x="-26" y="-175" width="5" height="21" rx="2.5"/><rect x="-19" y="-170" width="5" height="16" rx="2.5"/>'
                     '<rect x="-46" y="-156" width="5" height="12" rx="2.5" transform="rotate(-35 -44 -150)"/></g></g>')
    else:
        for d in (win_front, win_rear):
            p.append(f'<path d="{d}" fill="#141824"/>')
    # wheels
    for wx in (-168, 170):
        p.append(f'<circle cx="{wx}" cy="-34" r="40" fill="#020203"/><circle cx="{wx}" cy="-34" r="17" fill="#1b1e27"/>'
                 f'<circle cx="{wx}" cy="-34" r="6" fill="#3a3f4d"/>')
    p.append('</g>')
    return "".join(p)


def speaker_pole(x, base, h=150, color=INK, s=1.0):
    t = base - h * s
    return (f'<g fill="{color}"><rect x="{x - 4 * s:.0f}" y="{t:.0f}" width="{8 * s:.0f}" height="{h * s:.0f}"/>'
            f'<rect x="{x - 30 * s:.0f}" y="{t + 6 * s:.0f}" width="{26 * s:.0f}" height="{34 * s:.0f}" rx="{4 * s:.0f}"/>'
            f'<rect x="{x + 4 * s:.0f}" y="{t + 6 * s:.0f}" width="{26 * s:.0f}" height="{34 * s:.0f}" rx="{4 * s:.0f}"/>'
            f'<rect x="{x - 14 * s:.0f}" y="{base - 6 * s:.0f}" width="{28 * s:.0f}" height="{6 * s:.0f}"/></g>')


def big_screen(x, y, w, h, face, frame="#07080d", legs=True):
    out = ""
    if legs:
        for i in range(5):
            lx = x + 40 + i * (w - 80) / 4
            out += f'<rect x="{lx - 9:.0f}" y="{y + h - 10}" width="18" height="{1080 - y - h + 10}" fill="{frame}"/>'
        out += (f'<path d="M{x + 40} {y + h + 60} L{x + w - 40} {y + h + 260} M{x + w - 40} {y + h + 60} L{x + 40} {y + h + 260}" '
                f'stroke="{frame}" stroke-width="7"/>')
    out += f'<rect x="{x - 18}" y="{y - 18}" width="{w + 36}" height="{h + 36}" fill="{frame}"/>'
    out += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{face}"/>'
    return out


def booth(x, base, w=260, h=170, lit=True, door_open=False, color="#0a0b11"):
    t = base - h
    out = f'<rect x="{x}" y="{t}" width="{w}" height="{h}" fill="{color}"/><rect x="{x - 14}" y="{t - 14}" width="{w + 28}" height="18" fill="{color}"/>'
    if lit:
        out += lit_window(x + 30, t + 40, 90, 50, "#ffb54a", color)
        out += f'<rect x="{x + 150}" y="{t + 50}" width="26" height="22" fill="#fff1c9"/>' + glow(x + 163, t + 60, 30, "#fff1c9", 0.6)
    if door_open:
        out += (f'<rect x="{x + w - 70}" y="{t + 70}" width="48" height="{h - 70}" fill="#ffb54a"/>'
                f'<rect x="{x + w - 70}" y="{t + 70}" width="48" height="{h - 70}" fill="#ffb54a" opacity="0.7" filter="url(#blur30)"/>')
    else:
        out += f'<rect x="{x + w - 70}" y="{t + 70}" width="48" height="{h - 70}" fill="#16120f"/>'
    out += f'<circle cx="{x + w - 20}" cy="{t - 26}" r="7" fill="#ff3b2f"/>' + glow(x + w - 20, t - 26, 18, "#ff3b2f", 0.7)
    return out


def gravel(y0, y1, n, color="#3a3f4f", op=0.35):
    return "".join(f'<circle cx="{rnd.randint(0, W)}" cy="{rnd.randint(y0, y1)}" r="{rnd.uniform(1, 3):.1f}" fill="{color}" opacity="{rnd.uniform(0.1, op):.2f}"/>' for _ in range(n))


def grain(x, y, w, h, n, light="#e8ecf2", dark="#000", op=0.35):
    out = []
    for _ in range(n):
        gx, gy = rnd.randint(x, x + w - 4), rnd.randint(y, y + h - 2)
        out.append(f'<rect x="{gx}" y="{gy}" width="{rnd.randint(2, 6)}" height="2" fill="{rnd.choice([light, dark])}" opacity="{rnd.uniform(0.1, op):.2f}"/>')
    for _ in range(6):
        gy = rnd.randint(y, y + h)
        out.append(f'<rect x="{x}" y="{gy}" width="{w}" height="{rnd.randint(2, 5)}" fill="{light}" opacity="{rnd.uniform(0.04, 0.12):.2f}"/>')
    return "".join(out)


def moth(x, y, s=1.0):
    return (f'<g fill="#c9c2b0" opacity="0.85" transform="translate({x},{y}) scale({s})">'
            '<ellipse cx="-6" cy="0" rx="8" ry="5" transform="rotate(-25 -6 0)"/><ellipse cx="6" cy="0" rx="8" ry="5" transform="rotate(25 6 0)"/>'
            '<ellipse cx="0" cy="1" rx="2" ry="5" fill="#6d665a"/></g>')


GROUND = '<path d="M0 760 C500 740 1400 750 1920 735 L1920 1080 L0 1080Z" fill="#141826"/>'

# ---------------------------------------------------------------- S1 — the drive-in at night, a movie playing
cars1 = "".join(car(x, b, s, "#06070c") for x, b, s in [(300, 930, 0.62), (800, 940, 0.62), (1360, 930, 0.62), (560, 1060, 0.8), (1180, 1070, 0.8)])
poles1 = "".join(speaker_pole(x, b, 150, "#06070c", 0.8) for x, b in [(560, 935), (1080, 940), (1620, 930)])
beam = ('<polygon points="1273,660 500,170 500,490" fill="#e8eefc" opacity="0.10" filter="url(#blur8)"/>'
        '<polygon points="1273,660 580,230 580,430" fill="#e8eefc" opacity="0.08" filter="url(#blur30)"/>')
scenes = {}
scenes["s1"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(160, 520, 0.7)}
{moon(1640, 150, 58)}
<path d="M0 700 L200 640 L420 670 L700 620 L1000 660 L1300 610 L1600 650 L1920 620 L1920 780 L0 780Z" fill="#0b0e18"/>
{dead_tree(1760, 760, 260, "#080a12", 0.8)}
{big_screen(500, 170, 560, 320, "url(#movie)")}
{glow(780, 330, 300, "#9fb4dc", 0.18)}
{GROUND}
{gravel(780, 1080, 400)}
{beam}
{booth(1110, 760, 240, 160)}
{fog(800, "#9aa6c4", 0.10)}
{poles1}{cars1}
''', sky("sky1", "#03040a", "#0e1424", "#1d2538") +
   '<linearGradient id="movie" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#b9c7e2"/><stop offset="0.6" stop-color="#7f8fb0"/><stop offset="1" stop-color="#3a4462"/></linearGradient>')

# ---------------------------------------------------------------- S2 — the back row: one car left, windows fogged white
scenes["s2"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky2)"/>
{stars(120, 480, 0.6)}
{big_screen(1250, 120, 520, 280, "#2a3248", legs=True)}
<path d="M0 640 C500 630 1400 640 1920 620 L1920 1080 L0 1080Z" fill="#121624"/>
{gravel(640, 1080, 600, "#4a5064", 0.4)}
{''.join(speaker_pole(x, 700, 120, "#090b12", 0.7) for x in (140, 1700, 1860))}
{fog(720, "#a9b4cf", 0.14, 140)}
{speaker_pole(560, 860, 150, INK, 1.2)}
{glow(960, 760, 260, "#cfd6e4", 0.10)}
{car(960, 900, 1.25, "#06070c", fogged=True)}
{speaker_pole(1360, 880, 150, INK, 1.25)}
<path d="M0 1000 C600 980 1300 990 1920 975 L1920 1080 L0 1080Z" fill="#0a0c14"/>
{fog(1000, "#9aa6c4", 0.10)}
''', sky("sky2", "#02030a", "#0b1020", "#1a2236"))

# ---------------------------------------------------------------- S3 — the screen goes black / S3b — it flickers back on
def screen_scene(face, extra="", glowc=None):
    g = glow(960, 400, 420, glowc, 0.28) if glowc else ""
    return svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky3)"/>
{stars(220, 640, 0.8)}
{g}
{big_screen(560, 150, 800, 470, face)}
{extra}
<path d="M0 820 C500 805 1400 815 1920 800 L1920 1080 L0 1080Z" fill="#0f121d"/>
{gravel(820, 1080, 380)}
{''.join(speaker_pole(x, 900, 150, "#05060a", 0.9) for x in (420, 760, 1160, 1500))}
{fog(860, "#8e9abb", 0.10)}
''', sky("sky3", "#02030a", "#0a0f1e", "#161d30"))


scenes["s3"] = screen_scene("#05060a")
static = grain(560, 150, 800, 470, 900, "#f2f4f8", "#30364a", 0.6)
scenes["s3b"] = screen_scene("url(#flick)", static + '<rect x="560" y="370" width="800" height="18" fill="#ffffff" opacity="0.25"/>', "#c6d0e6")
scenes["s3b"] = scenes["s3b"].replace("<defs>", '<defs><radialGradient id="flick" cx="0.5" cy="0.5" r="0.7"><stop offset="0" stop-color="#b8bec9"/><stop offset="1" stop-color="#5a606c"/></radialGradient>', 1)

# ---------------------------------------------------------------- S4 — on the screen: the lot, filmed from the back row
def footage(x, y, w, h, walker=None, door_open=False, car_in=False):
    """A grainy black-and-white image of the lot as seen from the back row, looking at the booth."""
    cx = x + w / 2
    g = [f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 800 470">',
         '<rect width="800" height="470" fill="#5d626b"/>',
         '<rect width="800" height="230" fill="#3e424a"/>',
         '<path d="M0 230 C200 225 600 232 800 226 L800 470 L0 470Z" fill="#7b8089"/>',
         '<rect x="320" y="140" width="160" height="100" fill="#2a2d33"/><rect x="310" y="132" width="180" height="12" fill="#2a2d33"/>',
         '<rect x="338" y="164" width="56" height="30" fill="#d9dbe0"/>',
         f'<rect x="436" y="182" width="30" height="58" fill="{"#eceef2" if door_open else "#1b1d22"}"/>']
    if door_open:
        g.append('<rect x="436" y="182" width="30" height="58" fill="#eceef2" opacity="0.6" filter="url(#blur8)"/>')
    for px, ps in ((120, 0.9), (250, 0.7), (580, 0.7), (700, 0.9)):
        g.append(speaker_pole(px, 330 + ps * 40, 120, "#2e3138", ps))
    for px, ps in ((60, 1.6), (760, 1.6)):
        g.append(speaker_pole(px, 470, 120, "#202227", ps))
    if walker:
        wx, wy, wh = walker
        g.append(figure(wx, wy, wh, "#16181d"))
    g.append(grain(0, 0, 800, 470, 700, "#ffffff", "#000000", 0.45))
    g.append('</svg>')
    return "".join(g)


scenes["s4"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky4)"/>
{stars(160, 300, 0.6)}
{glow(960, 470, 470, "#c6cbd4", 0.22)}
{big_screen(530, 110, 860, 505, "#000", legs=False)}
{footage(530, 110, 860, 505)}
<rect x="512" y="633" width="896" height="447" fill="#07080d"/>
<path d="M0 830 C500 815 1400 825 1920 810 L1920 1080 L0 1080Z" fill="#0d1019"/>
{speaker_pole(700, 1080, 300, "#020203", 1.6)}
{glow(700, 640, 90, "#e8dcc0", 0.25)}
{moth(650, 560, 1.6)}{moth(760, 610, 1.3)}{moth(700, 700, 1.1)}{moth(620, 660, 1.0)}{moth(790, 530, 0.9)}
{fog(900, "#8e9abb", 0.08)}
''', sky("sky4", "#02030a", "#0a0f1e", "#161d30"))

# ---------------------------------------------------------------- S5 — on the screen, "I" walk out of the booth toward the car
scenes["s5"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky5)"/>
{glow(960, 470, 500, "#c6cbd4", 0.26)}
{big_screen(500, 80, 920, 540, "#000", legs=False)}
{footage(500, 80, 920, 540, walker=(560, 420, 220), door_open=True)}
<rect x="482" y="638" width="956" height="442" fill="#07080d"/>
<path d="M0 860 C500 845 1400 855 1920 840 L1920 1080 L0 1080Z" fill="#0d1019"/>
{''.join(speaker_pole(x, 960, 150, "#030305", 1.0) for x in (560, 1360))}
{fog(940, "#8e9abb", 0.08)}
''', sky("sky5", "#02030a", "#080c18", "#121828"))

# ---------------------------------------------------------------- S6 — inside the booth: my hand on the switch / S6b — the screen goes black
def booth_inside(screen_on=True):
    face = "#9aa1ad" if screen_on else "#05060a"
    on_screen = ""
    if screen_on:
        on_screen = (f'<svg x="640" y="250" width="470" height="200" viewBox="0 0 800 340">'
                     '<rect width="800" height="340" fill="#80858e"/><path d="M0 180 L800 170 L800 340 L0 340Z" fill="#9a9fa8"/>'
                     f'{car(470, 300, 0.75, "#24272d", fogged=False)}{figure(330, 300, 200, "#1d2025")}'
                     f'{grain(0, 0, 800, 340, 400, "#ffffff", "#000000", 0.4)}</svg>')
    return svg(f'''
<rect width="{W}" height="{H}" fill="#0b0a0c"/>
<rect x="520" y="160" width="700" height="440" fill="url(#night6)"/>
{stars(40, 0, 0) if False else ''}
<rect x="620" y="235" width="510" height="230" fill="#07080d"/>
<rect x="640" y="250" width="470" height="200" fill="{face}"/>
{on_screen}
{glow(875, 350, 260, "#c6cbd4", 0.22) if screen_on else ''}
<path d="M520 160 L1220 160 L1220 600 L520 600 Z M540 180 L540 580 L1200 580 L1200 180Z" fill="#1a1612" fill-rule="evenodd"/>
<line x1="870" y1="160" x2="870" y2="600" stroke="#1a1612" stroke-width="16"/>
<!-- projector -->
<g fill="#050405" transform="translate(200,60)">
<circle cx="360" cy="330" r="150"/><circle cx="360" cy="330" r="60" fill="#0f0d0e"/><circle cx="360" cy="330" r="14" fill="#2a2426"/>
<circle cx="250" cy="560" r="110"/><circle cx="250" cy="560" r="44" fill="#0f0d0e"/>
<rect x="260" y="470" width="300" height="190" rx="18"/>
<rect x="540" y="520" width="110" height="80" rx="10"/>
<rect x="300" y="660" width="40" height="300"/><rect x="200" y="940" width="240" height="40"/>
</g>
<g transform="translate(-90,0)">
<!-- desk + switch panel -->
<rect x="0" y="820" width="1920" height="260" fill="#120f0d"/>
<rect x="0" y="812" width="1920" height="12" fill="#2a221c"/>
<rect x="1240" y="600" width="220" height="230" rx="8" fill="#1e1a17"/>
<rect x="1258" y="618" width="184" height="194" rx="6" fill="#141110"/>
<circle cx="1300" cy="650" r="10" fill="{'#ff3b2f' if screen_on else '#3a1a18'}"/>{glow(1300, 650, 22, '#ff3b2f', 0.8) if screen_on else ''}
<rect x="1335" y="680" width="30" height="110" rx="6" fill="#050405"/>
<rect x="1330" y="{'690' if screen_on else '750'}" width="40" height="34" rx="6" fill="#8b8f98"/>
<!-- my hand on the switch -->
<path d="M1700 1080 C1640 940 1560 820 1440 760 L1380 744 C1360 738 1350 720 1366 712 L1430 716 C1440 700 1360 696 1352 682 C1346 670 1360 664 1374 666 L1440 676 C1446 668 1440 660 1430 656 L1390 648 C1376 644 1378 628 1394 628 L1452 638 C1470 642 1490 660 1500 676 C1560 700 1700 780 1840 900 L1920 960 L1920 1080Z" fill="#1c140f" stroke="#8a5f3a" stroke-width="4" opacity="0.97"/>
{glow(1420, 640, 220, "#ffb54a", 0.18)}</g>
''', '<linearGradient id="night6" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#03040a"/><stop offset="1" stop-color="#141a2a"/></linearGradient>')


scenes["s6"] = booth_inside(True)
scenes["s6b"] = booth_inside(False)

# ---------------------------------------------------------------- S7 — dawn, the back row is empty: tire tracks in the dew
tracks = ('<g fill="none" stroke="#5a5f6e" stroke-width="22" opacity="0.55">'
          '<path d="M820 800 C840 880 900 960 1000 1090"/><path d="M1080 800 C1110 880 1190 960 1320 1090"/></g>'
          '<g fill="none" stroke="#232733" stroke-width="10" opacity="0.6" stroke-dasharray="6 10">'
          '<path d="M820 800 C840 880 900 960 1000 1090"/><path d="M1080 800 C1110 880 1190 960 1320 1090"/></g>')
scenes["s7"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky7)"/>
{glow(960, 600, 520, "#ff9a5c", 0.35)}
{big_screen(480, 140, 520, 290, "#1c1a22")}
<path d="M0 640 L300 610 L600 630 L900 600 L1300 625 L1600 600 L1920 615 L1920 760 L0 760Z" fill="#1d1820"/>
<path d="M0 720 C500 700 1400 712 1920 695 L1920 1080 L0 1080Z" fill="#2b2a33"/>
{gravel(720, 1080, 700, "#7a7684", 0.45)}
{''.join(speaker_pole(x, 760, 120, "#0d0b10", 0.8) for x in (180, 1720))}
{speaker_pole(700, 880, 150, "#0a090c", 1.2)}{speaker_pole(1220, 880, 150, "#0a090c", 1.2)}
<ellipse cx="955" cy="800" rx="210" ry="22" fill="#18161c" opacity="0.6" filter="url(#blur8)"/>
{tracks}
{fog(760, "#e9c4b0", 0.16, 120)}
''', sky("sky7", "#14121e", "#5a3a4a", "#d9805a"))

# ---------------------------------------------------------------- S8 — my car, in the back row now; someone inside, waving
scenes["s8"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky8)"/>
{glow(960, 560, 520, "#ff7a4a", 0.30)}
{big_screen(1300, 120, 520, 290, "#1c1a22")}
<path d="M0 620 L300 600 L600 615 L900 590 L1300 610 L1600 590 L1920 600 L1920 760 L0 760Z" fill="#1d1820"/>
<path d="M0 700 C500 690 1400 700 1920 685 L1920 1080 L0 1080Z" fill="#26242c"/>
{gravel(700, 1080, 600, "#7a7684", 0.45)}
{speaker_pole(420, 900, 150, "#08070a", 1.3)}
{car(1000, 960, 1.55, "#0a090d", fogged=True, rider=True, wave=True)}
{speaker_pole(1520, 920, 150, "#08070a", 1.3)}
{fog(940, "#e9c4b0", 0.12, 120)}
''', sky("sky8", "#0e0c16", "#4a2e40", "#c0603e"))

for k, v in scenes.items():
    save(k, v)
print("saved", list(scenes))
