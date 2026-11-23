"""Scenes for The Thirteenth Chime."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *
import math

WARM = "#ffb54a"
RED = "#c2362b"
GRAYF = "#8d93a3"


def clock_face(cx, cy, r, hour_ang=0, min_ang=0, glow_col="#f2e6c4", tint="#e9dfc2"):
    ticks = "".join(
        f'<line x1="{cx + math.sin(math.radians(a)) * r * .78:.0f}" y1="{cy - math.cos(math.radians(a)) * r * .78:.0f}" '
        f'x2="{cx + math.sin(math.radians(a)) * r * .92:.0f}" y2="{cy - math.cos(math.radians(a)) * r * .92:.0f}" '
        f'stroke="#2a2520" stroke-width="{r * .06:.0f}" stroke-linecap="round"/>' for a in range(0, 360, 30))
    def hand(ang, ln, w):
        return (f'<line x1="{cx}" y1="{cy}" x2="{cx + math.sin(math.radians(ang)) * ln:.0f}" '
                f'y2="{cy - math.cos(math.radians(ang)) * ln:.0f}" stroke="#1a1612" stroke-width="{w:.0f}" stroke-linecap="round"/>')
    return (f'<circle cx="{cx}" cy="{cy}" r="{r * 1.9:.0f}" fill="{glow_col}" opacity="0.14" filter="url(#blur60)"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r * 1.08:.0f}" fill="#141016"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{tint}"/>{ticks}'
            f'{hand(hour_ang, r * .5, r * .09)}{hand(min_ang, r * .78, r * .06)}'
            f'<circle cx="{cx}" cy="{cy}" r="{r * .07:.0f}" fill="#1a1612"/>')


def tower(cx, base, top, w=150, col="#0a0910", face_r=46, face_tint="#e9dfc2", glow="#f2e6c4"):
    hw = w / 2
    return (f'<g fill="{col}"><rect x="{cx - hw}" y="{top}" width="{w}" height="{base - top}"/>'
            f'<rect x="{cx - hw - 14}" y="{top - 10}" width="{w + 28}" height="18"/>'
            f'<rect x="{cx - hw + 10}" y="{top - 120}" width="{w - 20}" height="112"/>'
            f'<polygon points="{cx - hw - 6},{top - 116} {cx},{top - 300} {cx + hw + 6},{top - 116}"/>'
            f'<rect x="{cx - 3}" y="{top - 360}" width="6" height="70"/></g>'
            f'<rect x="{cx - 24}" y="{top - 100}" width="48" height="80" rx="24" fill="#1c1820"/>'
            f'<path d="M{cx - 22} {top - 70} q22 -30 44 0 v30 h-44z" fill="#2b2430"/>'
            f'{clock_face(cx, top + face_r + 34, face_r, 0, 0, glow, face_tint)}')


def house(x, base, w=300, h=200, porch=None, win=None, col="#0b0a12", door_col="#06050a"):
    """Simple two-storey house. porch: colour of porch light or None (off). win: window colour or None."""
    roof = h * .55
    out = [f'<g fill="{col}"><rect x="{x}" y="{base - h}" width="{w}" height="{h}"/>'
           f'<polygon points="{x - 18},{base - h + 4} {x + w / 2},{base - h - roof} {x + w + 18},{base - h + 4}"/>'
           f'<rect x="{x + w * .72}" y="{base - h - roof * .8}" width="{w * .1}" height="{roof * .6}"/>'
           f'<rect x="{x - 20}" y="{base - h * .42}" width="{w + 40}" height="12"/>'
           f'<rect x="{x - 10}" y="{base - h * .42}" width="8" height="{h * .42}"/><rect x="{x + w + 2}" y="{base - h * .42}" width="8" height="{h * .42}"/></g>']
    dx = x + w * .42
    out.append(f'<rect x="{dx}" y="{base - h * .36}" width="{w * .16}" height="{h * .36}" fill="{door_col}"/>')
    for wx in (x + w * .12, x + w * .68):
        if win:
            out.append(lit_window(wx, base - h * .82, w * .2, h * .26, win, col))
        else:
            out.append(f'<rect x="{wx}" y="{base - h * .82}" width="{w * .2}" height="{h * .26}" fill="#14131d"/>')
    if porch:
        px, py = dx - 22, base - h * .3
        out.append(f'<circle cx="{px}" cy="{py}" r="10" fill="#fff3d6"/>{glow(px, py, 50, porch, 0.95)}'
                   f'<ellipse cx="{px + 30}" cy="{base + 6}" rx="{w * .5}" ry="22" fill="{porch}" opacity="0.28" filter="url(#blur30)"/>'
                   f'<circle cx="{px}" cy="{py}" r="{h * .5}" fill="{porch}" opacity="0.10" filter="url(#blur60)"/>')
    return "".join(out)


def gray_shape(cx, base, h, op=0.85):
    return (f'<g opacity="{op}">{figure(cx, base, h, GRAYF)}</g>'
            f'<g opacity="0.35" filter="url(#blur30)">{figure(cx, base, h, "#b8bdc9")}</g>')


# S1 — Alder Falls: a small town square with its clock tower
row = "".join(house(x, 820, 230, 150, porch=WARM if i % 2 == 0 else None, win=WARM if i in (1, 4) else None, col="#0d0c16")
              for i, x in enumerate((90, 380, 1290, 1580)))
save("s1", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>{stars(170, 560)}{moon(1340, 220, 70)}
<path d="M0 760 C400 730 1500 730 1920 750 L1920 1080 L0 1080Z" fill="#131020"/>
{tower(960, 830, 380, 170, "#0a0910", 58)}
<g fill="#0a0910"><rect x="700" y="640" width="180" height="190"/><polygon points="690,644 790,570 890,644"/>
<rect x="1040" y="660" width="200" height="170"/><polygon points="1030,664 1140,600 1250,664"/></g>
{lit_window(735, 690, 46, 56, WARM)}{lit_window(1120, 700, 46, 56, WARM)}
{row}
<path d="M0 830 L1920 830 L1920 1080 L0 1080Z" fill="#0c0b14"/>
<polygon points="860,830 1060,830 1300,1080 620,1080" fill="#1a1726"/>
{"".join(f'<g fill="#07060b"><rect x="{x}" y="770" width="6" height="64"/><circle cx="{x + 3}" cy="768" r="12" fill="{WARM}" opacity="0.9"/></g>{glow(x + 3, 768, 40, WARM, 0.5)}' for x in (600, 1314))}
{fog(840, "#9aa0bf", 0.12)}
''', sky("sky1", "#05060f", "#1a1736", "#33223f")))

# S2 — bedroom, bells waking me just after midnight
save("s2", svg(f'''
<rect width="{W}" height="{H}" fill="#0b0a12"/>
<rect x="0" y="760" width="{W}" height="320" fill="#120f18"/>
<rect x="1060" y="180" width="420" height="440" fill="url(#night2)"/>
{stars(30, 0)}
<g clip-path="url(#win2)">{stars(40, 620, 0.6)}{tower(1270, 640, 420, 70, "#07060c", 22)}
<g fill="#07060c"><rect x="1080" y="560" width="120" height="80"/><rect x="1330" y="540" width="140" height="100"/></g></g>
<rect x="1060" y="180" width="420" height="440" fill="none" stroke="#1d1824" stroke-width="22"/>
<line x1="1270" y1="180" x2="1270" y2="620" stroke="#1d1824" stroke-width="12"/><line x1="1060" y1="400" x2="1480" y2="400" stroke="#1d1824" stroke-width="12"/>
<path d="M1020 160 C1050 300 1030 500 1060 660 L1000 660 L990 160Z" fill="#1b1522"/>
<path d="M1520 160 C1490 300 1510 500 1480 660 L1540 660 L1550 160Z" fill="#1b1522"/>
<polygon points="1080,640 1460,640 1380,1080 820,1080" fill="#a9b4dc" opacity="0.06"/>
<g transform="translate(-260 0)"><rect x="380" y="620" width="700" height="200" rx="20" fill="#1a1626"/>
<rect x="380" y="560" width="40" height="300" rx="10" fill="#0e0c14"/>
<path d="M440 640 C600 600 800 610 1080 650 L1080 760 L440 760Z" fill="#2a2538"/>
<ellipse cx="520" cy="610" rx="90" ry="40" fill="#3a3449"/>
<path d="M600 640 C640 600 700 600 740 630" stroke="#1a1626" stroke-width="6" fill="none"/>
</g><rect x="830" y="640" width="190" height="180" fill="#0f0c15"/>
<rect x="845" y="570" width="160" height="70" rx="8" fill="#08070b"/>
<text x="925" y="622" text-anchor="middle" font-family="{MONO}" font-size="50" fill="{RED}">12:03</text>
{glow(925, 605, 90, RED, 0.4)}
''', '''<linearGradient id="night2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0d1230"/><stop offset="1" stop-color="#2b2550"/></linearGradient>
<clipPath id="win2"><rect x="1060" y="180" width="420" height="440"/></clipPath>'''))

# S3 — the tower clock, close, striking thirteen
save("s3", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky3)"/>{stars(90, 700, 0.5)}
<rect x="700" y="0" width="520" height="1080" fill="#0b0910"/>
<g fill="#0e0b13">{"".join(f'<rect x="{700 + (i % 2) * 30}" y="{y}" width="{460}" height="6" opacity="0.6"/>' for i, y in enumerate(range(40, 1080, 70)))}</g>
<rect x="650" y="170" width="620" height="24" fill="#08070c"/><rect x="650" y="880" width="620" height="24" fill="#08070c"/>
{clock_face(960, 540, 240, 0, 0, RED, "#e4d8bb")}
<circle cx="960" cy="540" r="240" fill="{RED}" opacity="0.18"/>
<g stroke="#e4d8bb" stroke-width="4" fill="none" opacity="0.25">
<path d="M610 540 a350 350 0 0 1 700 0"/><path d="M560 540 a400 400 0 0 1 800 0"/><path d="M510 540 a450 450 0 0 1 900 0"/></g>
{fog(950, "#b44", 0.12)}
''', sky("sky3", "#07050a", "#1e0d14", "#3a1018")))

# S4 / S4b — the street, porch lights going out; all except mine
def street(lit):
    houses = []
    xs = (130, 500, 880, 1260, 1630)
    for i, x in enumerate(xs):
        p = WARM if (lit or i == 2) else None
        houses.append(house(x - 10, 760, 250, 190, porch=p, win=(WARM if lit and i % 2 == 0 else None), col="#0d0c16"))
    return svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky4)"/>{stars(140, 450)}{moon(1500, 140, 50)}
{tower(380, 560, 300, 60, "#100e1a", 18)}
<path d="M0 560 L1920 560 L1920 760 L0 760Z" fill="#100e19"/>
{"".join(houses)}
<rect x="0" y="760" width="{W}" height="320" fill="#0b0a12"/>
<rect x="0" y="790" width="{W}" height="200" fill="#1a1726"/>
<g fill="#3a3550" opacity="0.6">{"".join(f'<rect x="{x}" y="884" width="80" height="8"/>' for x in range(30, 1920, 180))}</g>
{fog(870, "#9aa0bf", 0.10)}
''', sky("sky4", "#05060f", "#151530", "#2a1f3a"))
save("s4", street(True))
save("s4b", street(False))

# S5 — through the curtain gap: tall gray shapes walking down the road
def through_curtain(body):
    return svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky5)"/>{stars(60, 300, 0.4)}
<path d="M0 520 L1920 520 L1920 1080 L0 1080Z" fill="#0f0d17"/>
{body}
<path d="M0 0 L800 0 C770 300 820 700 770 1080 L0 1080Z" fill="#1b1420"/>
<path d="M1920 0 L1120 0 C1150 300 1100 700 1150 1080 L1920 1080Z" fill="#1b1420"/>
<g stroke="#120c16" stroke-width="10" fill="none" opacity="0.8">{"".join(f'<path d="M{x} 0 C{x - 20} 400 {x + 20} 700 {x - 10} 1080"/>' for x in (200, 420, 640, 780, 1140, 1300, 1520, 1740))}</g>
<path d="M800 0 C770 300 820 700 770 1080" stroke="{WARM}" stroke-width="4" fill="none" opacity="0.35"/>
''', sky("sky5", "#05060d", "#11132a", "#1f1d33"))
road = ('<polygon points="900,520 1020,520 1500,1080 420,1080" fill="#1c1a2a"/>'
        '<g fill="#4a4660">' + "".join(f'<rect x="{958 - (y - 520) * .02:.0f}" y="{y}" width="{4 + (y - 520) * .03:.0f}" height="{10 + (y - 520) * .05:.0f}"/>' for y in (540, 600, 690, 820, 980)) + '</g>')
save("s5", through_curtain(f'''{road}
{house(560, 520, 160, 110, None, None, "#0a0911")}{house(1210, 520, 160, 110, None, None, "#0a0911")}
{gray_shape(930, 640, 260, 0.7)}{gray_shape(1010, 700, 330, 0.8)}{gray_shape(905, 780, 420, 0.9)}
{fog(720, "#a7adc2", 0.16)}'''))

# S6 — they stop at my lit porch
save("s6", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky6)"/>{stars(110, 380)}
<path d="M0 760 L1920 760 L1920 1080 L0 1080Z" fill="#0d0b14"/>
{house(620, 760, 680, 440, porch=WARM, win=None, col="#0c0a13")}
<polygon points="860,760 1040,760 1080,1080 760,1080" fill="#241c20"/>
<rect x="0" y="1000" width="{W}" height="80" fill="#1a1726"/>
{gray_shape(700, 1060, 470, 0.85)}{gray_shape(960, 1080, 520, 0.92)}{gray_shape(1220, 1060, 470, 0.85)}
{fog(1000, "#a7adc2", 0.12)}
''', sky("sky6", "#04050c", "#131330", "#241b33")))

# S7 — the cracked light switch in the dark
save("s7", svg(f'''
<rect width="{W}" height="{H}" fill="#0c0a10"/>
<g stroke="#15121a" stroke-width="3" opacity="0.7">{"".join(f'<line x1="{x}" y1="0" x2="{x}" y2="1080"/>' for x in range(40, 1920, 120))}</g>
<rect x="840" y="330" width="240" height="380" rx="18" fill="#cfc6b2"/>
<rect x="840" y="330" width="240" height="380" rx="18" fill="#000" opacity="0.45"/>
<rect x="915" y="420" width="90" height="200" rx="12" fill="#a59c88"/>
<rect x="930" y="535" width="60" height="75" rx="8" fill="#e3dac6"/>
<rect x="930" y="535" width="60" height="75" rx="8" fill="#000" opacity="0.3"/>
<path d="M990 430 L960 480 L985 500 L950 560 L970 590 L940 660" stroke="#1a1612" stroke-width="5" fill="none"/>
<circle cx="960" cy="370" r="8" fill="#6d6555"/><circle cx="960" cy="670" r="8" fill="#6d6555"/>
<g fill="#050407">
<path d="M1000 640 C1080 620 1180 640 1260 700 C1330 750 1400 780 1500 790 L1500 900 C1380 900 1260 860 1170 800 C1100 760 1040 740 990 700Z"/>
<rect x="940" y="590" width="90" height="34" rx="17" transform="rotate(-10 985 607)"/>
<rect x="950" y="628" width="80" height="32" rx="16"/>
</g>
<polygon points="0,1080 600,760 1320,760 1920,1080" fill="#a9b4dc" opacity="0.04"/>
{glow(1600, 200, 220, "#5a6aa8", 0.08)}
'''))

# S8 — morning: the neighbor waiting at the fence
fence = "".join(f'<path d="M{x} 1000 v-170 l18 -26 l18 26 v170z" fill="#5b5f6e"/>' for x in range(-20, 1940, 64))
save("s8", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky8)"/>
<circle cx="1500" cy="620" r="320" fill="#e9d6c0" opacity="0.25" filter="url(#blur60)"/>
<path d="M0 640 C500 610 1400 620 1920 640 L1920 1080 L0 1080Z" fill="#6a6e7c"/>
{tower(300, 640, 420, 60, "#4c5060", 18, "#c9c2b0", "#c9c2b0")}
<g fill="#545867"><rect x="1300" y="520" width="300" height="140"/><polygon points="1280,524 1450,440 1620,524"/></g>
{dead_tree(1720, 660, 300, "#3c3f4a", 0.8)}
<g fill="#2b2d36">
<ellipse cx="960" cy="560" rx="48" ry="58"/>
<path d="M880 1000 L890 700 C880 640 920 620 960 620 C1000 620 1040 640 1030 700 L1040 1000Z"/>
<path d="M910 590 C900 640 880 700 870 760 L900 760 C910 700 920 650 930 610Z" opacity="0.9"/>
<path d="M1010 590 C1020 640 1040 700 1050 760 L1020 760 C1010 700 1000 650 990 610Z" opacity="0.9"/>
</g>
{fence}
<rect x="0" y="880" width="{W}" height="14" fill="#4a4e5c"/><rect x="0" y="950" width="{W}" height="14" fill="#4a4e5c"/>
<rect x="0" y="1000" width="{W}" height="80" fill="#3c3f4a"/>
<g fill="#2b2d36"><rect x="870" y="830" width="40" height="70" rx="18"/><rect x="1010" y="830" width="40" height="70" rx="18"/></g>
{fog(760, "#e8e6ee", 0.28, 160)}
''', sky("sky8", "#8c8fa0", "#b5b2b8", "#d9c8bb")))

# S9 — my kitchen window from the yard: someone tall making breakfast
save("s9", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky9)"/>
<rect x="0" y="0" width="{W}" height="1080" fill="#3b3e4c"/>
<g stroke="#30333f" stroke-width="4">{"".join(f'<line x1="0" y1="{y}" x2="1920" y2="{y}"/>' for y in range(30, 1080, 54))}</g>
<rect x="600" y="220" width="720" height="560" fill="#ffcf86"/>
<g clip-path="url(#k9)">
<rect x="600" y="220" width="720" height="560" fill="url(#kit)"/>
<g fill="#b98a55"><rect x="600" y="300" width="720" height="16"/>
<rect x="640" y="240" width="60" height="60" rx="6"/><rect x="1200" y="246" width="80" height="54" rx="6"/></g>
<rect x="600" y="650" width="720" height="130" fill="#8a6038"/>
<rect x="1000" y="630" width="240" height="24" fill="#3a2a1e"/>
<ellipse cx="1110" cy="628" rx="80" ry="14" fill="#1d1612"/><rect x="1180" y="620" width="120" height="10" rx="5" fill="#1d1612"/>
<g opacity="0.5" stroke="#fff" stroke-width="6" fill="none"><path d="M1090 600 c-20 -30 20 -40 0 -80"/><path d="M1130 600 c-20 -30 20 -40 0 -80"/></g>
<g fill="#5d6170">
<ellipse cx="900" cy="200" rx="46" ry="60"/>
<path d="M820 780 L835 420 C820 300 860 270 900 268 C940 270 980 300 965 420 L980 780Z"/>
<path d="M955 330 C1010 400 1050 520 1100 610" stroke="#5d6170" stroke-width="26" stroke-linecap="round" fill="none"/>
</g>
<rect x="600" y="220" width="720" height="560" fill="{RED}" opacity="0.06"/>
</g>
<rect x="600" y="220" width="720" height="560" fill="#ffcf86" opacity="0.25" filter="url(#blur30)"/>
<rect x="600" y="220" width="720" height="560" fill="none" stroke="#e7e3da" stroke-width="22"/>
<line x1="960" y1="220" x2="960" y2="780" stroke="#e7e3da" stroke-width="12"/>
<rect x="570" y="780" width="780" height="34" fill="#d6d1c6"/>
<polygon points="600,814 1320,814 1520,1080 400,1080" fill="#ffcf86" opacity="0.08"/>
{grass(1080, 260, "#22242c", (20, 50))}
''', sky("sky9", "#9aa0ad", "#b9bbc3", "#cfc8c0") + '''
<linearGradient id="kit" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6d49c"/><stop offset="1" stop-color="#d9a36a"/></linearGradient>
<clipPath id="k9"><rect x="600" y="220" width="720" height="560"/></clipPath>'''))
print("ok")
