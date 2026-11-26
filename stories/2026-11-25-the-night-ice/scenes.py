"""Scenes for The Night Ice."""
import sys, math; sys.path.insert(0, "../../toolkit")
from scenekit import *

RED = "#ff2a22"
WARM = "#ffb54a"
ICE = "#9fc3e6"
DARK = "#07060c"


def rink_interior(lights_on=True, extra="", ice_marks=""):
    """Inside the rink, looking down the ice. Centre ~960."""
    o = []
    roof = "#0a0c14"
    o.append(f'<rect width="{W}" height="{H}" fill="#06070c"/>')
    # arched roof trusses
    for i, x in enumerate(range(-200, 2200, 220)):
        o.append(f'<path d="M{x} 0 Q960 {120 + abs(960 - x) * 0.05:.0f} {1920 - x} 0" stroke="#11141f" stroke-width="10" fill="none" opacity="0.7"/>')
    o.append('<path d="M0 380 Q960 180 1920 380" stroke="#141826" stroke-width="16" fill="none"/>')
    # back stands
    o.append('<polygon points="0,380 1920,380 1920,560 0,560" fill="#0d0f18"/>')
    for y in range(400, 560, 26):
        o.append(f'<line x1="0" y1="{y}" x2="1920" y2="{y}" stroke="#161a28" stroke-width="5"/>')
    # far boards and glass
    o.append('<rect x="0" y="540" width="1920" height="40" fill="#1a2030"/>')
    o.append('<rect x="0" y="470" width="1920" height="72" fill="#7fa7cc" opacity="0.06"/>')
    for x in range(0, 1920, 160):
        o.append(f'<line x1="{x}" y1="470" x2="{x}" y2="542" stroke="#2a3348" stroke-width="3"/>')
    # ice surface
    icecol = "url(#iceOn)" if lights_on else "url(#iceOff)"
    o.append(f'<polygon points="0,580 1920,580 1920,1080 0,1080" fill="{icecol}"/>')
    # rink markings
    lc = "#7a2630" if lights_on else "#2a1318"
    bc = "#2d4a7a" if lights_on else "#121a2a"
    o.append(f'<rect x="0" y="760" width="1920" height="14" fill="{lc}" opacity="0.8"/>')
    o.append(f'<ellipse cx="960" cy="767" rx="230" ry="60" fill="none" stroke="{bc}" stroke-width="8" opacity="0.8"/>')
    o.append(f'<line x1="0" y1="660" x2="1920" y2="660" stroke="{bc}" stroke-width="10" opacity="0.6"/>')
    o.append(f'<line x1="0" y1="900" x2="1920" y2="900" stroke="{bc}" stroke-width="16" opacity="0.6"/>')
    o.append(ice_marks)
    if lights_on:
        for x in range(260, 1800, 280):
            o.append(f'<rect x="{x - 40}" y="250" width="80" height="16" rx="6" fill="#e9f2ff"/>')
            o.append(glow(x, 262, 70, "#dce9ff", 0.55))
            o.append(f'<ellipse cx="{x}" cy="{720 + abs(960 - x) * 0.05:.0f}" rx="120" ry="30" fill="#e9f2ff" opacity="0.18" filter="url(#blur30)"/>')
    else:
        for x in range(260, 1800, 280):
            o.append(f'<rect x="{x - 40}" y="250" width="80" height="16" rx="6" fill="#151a26"/>')
    o.append(extra)
    # near boards
    o.append('<rect x="0" y="1010" width="1920" height="70" fill="#121624"/>')
    o.append('<rect x="0" y="1010" width="1920" height="10" fill="#2a3a5a" opacity="0.7"/>')
    return "".join(o)


DEFS_RINK = '''<linearGradient id="iceOn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#bcd3ea"/><stop offset="0.5" stop-color="#8eaed0"/><stop offset="1" stop-color="#5d7ea6"/></linearGradient>
<linearGradient id="iceOff" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#141c2b"/><stop offset="0.6" stop-color="#0d1320"/><stop offset="1" stop-color="#090c15"/></linearGradient>'''


def resurfacer(x, base, s=1.0, col="#0b0d16", light=True):
    o = [f'<g transform="translate({x} {base}) scale({s})">']
    o.append(f'<path d="M-230 0 L-230 -150 L-120 -150 L-100 -250 L60 -250 L80 -150 L230 -150 L240 -40 L230 0 Z" fill="{col}"/>')
    o.append(f'<rect x="-90" y="-240" width="130" height="80" fill="#1c2436"/>')
    o.append(f'<path d="M-70 -200 q10 -30 40 -30 q30 0 40 30 l0 40 l-80 0z" fill="{col}"/>')  # driver
    o.append(f'<circle cx="-140" cy="0" r="46" fill="#05060a"/><circle cx="150" cy="0" r="46" fill="#05060a"/>')
    o.append(f'<circle cx="-140" cy="0" r="16" fill="#2a3040"/><circle cx="150" cy="0" r="16" fill="#2a3040"/>')
    o.append(f'<rect x="230" y="-30" width="50" height="34" fill="{col}"/>')
    if light:
        o.append(f'<circle cx="236" cy="-110" r="12" fill="{WARM}"/>')
        o.append(glow(260, -110, 60, WARM, 0.7))
    o.append('</g>')
    return "".join(o)


# S1 — rink building exterior at night
snow = "".join(f'<circle cx="{rnd.randint(0, W)}" cy="{rnd.randint(0, 1080)}" r="{rnd.choice([1.5, 2, 2.6, 3])}" fill="#e6ecf7" opacity="{rnd.uniform(0.3, 0.8):.2f}"/>' for _ in range(220))
save("s1", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(120, 420, 0.6)}
{moon(1480, 200, 80)}
<path d="M0 820 C500 790 1400 800 1920 815 L1920 1080 L0 1080Z" fill="#c9d4e6" opacity="0.18"/>
<g fill="#0a0b13">
<path d="M560 820 L560 520 Q960 330 1360 520 L1360 820 Z"/>
<rect x="1360" y="640" width="260" height="180"/>
<rect x="400" y="680" width="160" height="140"/>
</g>
<path d="M560 520 Q960 330 1360 520" stroke="#cfd9ea" stroke-width="10" fill="none" opacity="0.5"/>
<rect x="800" y="470" width="320" height="70" rx="6" fill="#1a0809"/>
<text x="960" y="522" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="48" fill="{RED}" letter-spacing="10">ICE RINK</text>
<rect x="800" y="470" width="320" height="70" rx="6" fill="{RED}" opacity="0.25" filter="url(#blur30)"/>
{lit_window(910, 680, 100, 140, WARM)}
{lit_window(1440, 690, 60, 60, "#c9d8f2")}
<circle cx="1130" cy="640" r="7" fill="#ffe0a0"/>{glow(1130, 640, 40, "#ffe0a0", 0.5)}
<ellipse cx="960" cy="860" rx="300" ry="40" fill="{WARM}" opacity="0.14" filter="url(#blur30)"/>
{dead_tree(300, 830, 360)}
{dead_tree(1720, 840, 300)}
<path d="M0 860 C600 840 1300 850 1920 860 L1920 1080 L0 1080Z" fill="#1b2232"/>
<path d="M0 960 C600 935 1300 950 1920 940 L1920 1080 L0 1080Z" fill="#121826"/>
{fog(840, "#aab3c8", 0.14)}
{snow}
''', sky("sky1", "#04050c", "#141a33", "#2b2f4a")))

# S2 — resurfacer laying fresh ice under the lights
gloss = '<path d="M1180 1000 L1700 640 L1920 640 L1920 1000 Z" fill="#e8f2ff" opacity="0.18"/>'
save("s2", svg(rink_interior(True, extra=resurfacer(900, 760, 1.15) + '<ellipse cx="900" cy="770" rx="320" ry="26" fill="#000" opacity="0.35" filter="url(#blur8)"/>',
                             ice_marks=gloss + '<rect x="1220" y="720" width="700" height="90" fill="#dfeeff" opacity="0.25" filter="url(#blur8)"/>'), DEFS_RINK))

# S3 — rink in the dark, only red EXIT glowing, long scrape arcs in the ice
arcs = "".join(f'<path d="M{700 + i * 30} {860 + i * 10} C{600 + i * 30} {700} {1300 - i * 20} {660 + i * 5} {1320 - i * 20} {830 - i * 6}" stroke="#7d99bf" stroke-width="2.5" fill="none" opacity="{0.45 - i * 0.07:.2f}"/>' for i in range(5))
exit_sign = (f'<rect x="1150" y="380" width="160" height="60" rx="6" fill="#1a0606"/>'
             f'<text x="1230" y="425" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="40" fill="{RED}">EXIT</text>'
             f'{glow(1230, 410, 120, RED, 0.35)}'
             f'<polygon points="1150,580 1310,580 1420,1080 1040,1080" fill="{RED}" opacity="0.05"/>')
save("s3", svg(rink_interior(False, extra=exit_sign, ice_marks=arcs) + fog(700, "#5a6a88", 0.12), DEFS_RINK))

# S4 — hand on the light switch panel
switches = ""
for i in range(4):
    for j in range(2):
        x, y = 700 + i * 150, 330 + j * 230
        switches += f'<rect x="{x}" y="{y}" width="90" height="150" rx="10" fill="#2a2f3c"/><rect x="{x + 30}" y="{y + 80}" width="30" height="50" rx="6" fill="#0e1118"/>'
save("s4", svg(f'''
<rect width="{W}" height="{H}" fill="#0b0d14"/>
<g stroke="#121521" stroke-width="3">{''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in range(60, 1080, 90))}</g>
<g stroke="#121521" stroke-width="3">{''.join(f'<line x1="{x + (y // 90 % 2) * 90}" y1="{y}" x2="{x + (y // 90 % 2) * 90}" y2="{y + 90}"/>' for y in range(60, 1080, 90) for x in range(0, W, 180))}</g>
<rect x="640" y="270" width="660" height="520" rx="16" fill="#3a404f"/>
<rect x="660" y="290" width="620" height="480" rx="10" fill="#1d212c"/>
{switches}
<circle cx="980" cy="200" r="10" fill="{RED}"/>{glow(980, 200, 60, RED, 0.6)}
<g fill="#000" opacity="0.85">
<ellipse cx="1180" cy="760" rx="210" ry="140"/>
<rect x="1040" y="610" width="70" height="200" rx="34" transform="rotate(-12 1075 700)"/>
<rect x="1120" y="590" width="70" height="210" rx="34" transform="rotate(-6 1155 700)"/>
<rect x="1200" y="600" width="66" height="200" rx="32"/>
<rect x="1272" y="630" width="58" height="170" rx="28" transform="rotate(8 1300 700)"/>
<rect x="1000" y="760" width="160" height="56" rx="28" transform="rotate(-40 1080 790)"/>
<rect x="1150" y="820" width="300" height="300" rx="80"/>
</g>
<polygon points="640,270 1300,270 1500,1080 400,1080" fill="#ff3a2a" opacity="0.04"/>
<circle cx="960" cy="520" r="420" fill="#7ea0d8" opacity="0.05" filter="url(#blur60)"/>
'''))

# S5 — small handprint on the dark glass, a little figure behind
hand = ('<g fill="#cfe2ff" opacity="0.55" transform="translate(1050 640)">'
        '<ellipse cx="0" cy="30" rx="34" ry="38"/>'
        '<rect x="-34" y="-50" width="14" height="60" rx="7" transform="rotate(-10)"/>'
        '<rect x="-16" y="-66" width="14" height="72" rx="7"/>'
        '<rect x="2" y="-62" width="14" height="68" rx="7"/>'
        '<rect x="20" y="-48" width="13" height="56" rx="6" transform="rotate(10)"/>'
        '<rect x="28" y="10" width="13" height="44" rx="6" transform="rotate(50 34 30)"/></g>')
girl = ('<g fill="#03040a">'
        '<circle cx="960" cy="470" r="44"/>'
        '<path d="M914 470 q-10 60 -20 90 l40 -20z M1006 470 q10 60 20 90 l-40 -20z"/>'
        '<path d="M920 520 L900 760 L1020 760 L1000 520 Q960 500 920 520Z"/>'
        '<rect x="925" y="760" width="22" height="110"/><rect x="975" y="760" width="22" height="110"/>'
        '<path d="M915 870 l45 0 l0 14 l-55 0z M965 870 l45 0 l10 14 l-55 0z"/>'
        '<rect x="905" y="890" width="60" height="4" fill="#4a5a78"/><rect x="960" y="890" width="60" height="4" fill="#4a5a78"/></g>')
save("s5", svg(f'''
<rect width="{W}" height="{H}" fill="#05070d"/>
<rect x="0" y="0" width="{W}" height="900" fill="url(#glassG)"/>
{fog(760, "#4a5a7a", 0.18)}
{girl}
<rect x="0" y="0" width="{W}" height="900" fill="#9fc3e6" opacity="0.05"/>
{''.join(f'<rect x="{x}" y="0" width="18" height="900" fill="#0c111c"/>' for x in (520, 1400))}
<polygon points="560,0 760,0 520,900 380,900" fill="#cfe2ff" opacity="0.05"/>
<polygon points="1200,0 1260,0 1100,900 1060,900" fill="#cfe2ff" opacity="0.04"/>
{hand}
{glow(1050, 640, 60, "#cfe2ff", 0.15)}
<rect x="0" y="900" width="{W}" height="180" fill="#151b2b"/>
<rect x="0" y="900" width="{W}" height="14" fill="#3a4a6a"/>
<rect x="0" y="914" width="{W}" height="6" fill="{RED}" opacity="0.5"/>
''', '<linearGradient id="glassG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#070a12"/><stop offset="1" stop-color="#0f1626"/></linearGradient>'))

# S6 — back door swinging open onto snowy night
save("s6", svg(f'''
<rect width="{W}" height="{H}" fill="#0a0b11"/>
<polygon points="0,0 1920,0 1920,1080 0,1080" fill="#0c0d15"/>
<rect x="760" y="180" width="400" height="720" fill="url(#night6)"/>
{''.join(f'<circle cx="{rnd.randint(770, 1150)}" cy="{rnd.randint(190, 880)}" r="{rnd.choice([1.5, 2.2, 3])}" fill="#e6ecf7" opacity="{rnd.uniform(0.4, 0.9):.2f}"/>' for _ in range(70))}
<path d="M760 760 C880 740 1040 750 1160 740 L1160 900 L760 900Z" fill="#9fb0c8" opacity="0.5"/>
{dead_tree(1020, 770, 300, "#0a0c14", 0.6)}
<polygon points="760,180 560,120 560,980 760,900" fill="#1b1f2c"/>
<polygon points="760,180 560,120 560,980 760,900" fill="none" stroke="#2c3244" stroke-width="6"/>
<rect x="600" y="500" width="30" height="14" rx="6" fill="#7b818f"/>
<rect x="590" y="330" width="120" height="20" fill="#2c3244" transform="skewY(17)"/>
<rect x="740" y="160" width="440" height="20" fill="#05060a"/>
<rect x="740" y="160" width="20" height="760" fill="#05060a"/><rect x="1160" y="160" width="20" height="760" fill="#05060a"/>
<polygon points="760,900 1160,900 1500,1080 420,1080" fill="#8ea6c8" opacity="0.14"/>
<rect x="0" y="900" width="{W}" height="180" fill="#111420" opacity="0.7"/>
{''.join(f'<ellipse cx="{960 + (i % 2) * 30 - 15}" cy="{1060 - i * 32}" rx="{9 - i * 0.6:.1f}" ry="3" fill="#cfe2ff" opacity="{0.5 - i * 0.04:.2f}"/>' for i in range(6))}
<rect x="1380" y="280" width="140" height="56" rx="6" fill="#1a0606"/>
<text x="1450" y="322" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="36" fill="{RED}">EXIT</text>
{glow(1450, 308, 110, RED, 0.35)}
{fog(880, "#8a98b8", 0.12)}
''', sky("night6", "#05060d", "#1a2138", "#3a4560")))

# S7 — morning ice with tiny skate marks circling, then leading out the gate
loops = ""
for i in range(7):
    rx, ry = 520 + i * 26, 120 + i * 9
    loops += f'<ellipse cx="960" cy="770" rx="{rx}" ry="{ry}" fill="none" stroke="#3a4f72" stroke-width="2.4" opacity="{0.55 - i * 0.04:.2f}" stroke-dasharray="40 8 30 6"/>'
trail = '<path d="M1520 790 C1600 830 1640 880 1620 960 L1600 1010" stroke="#2a3a58" stroke-width="3" fill="none" stroke-dasharray="30 8"/><path d="M1532 786 C1614 828 1656 880 1636 960 L1616 1010" stroke="#2a3a58" stroke-width="3" fill="none" stroke-dasharray="26 10"/>'
gate = '<rect x="1560" y="960" width="110" height="60" fill="#05060a"/><rect x="1670" y="900" width="14" height="120" fill="#2a3348"/>'
save("s7", svg(rink_interior(True, extra=f'<rect width="{W}" height="580" fill="#ffd9a0" opacity="0.06"/>', ice_marks=loops + trail) + gate, DEFS_RINK))

# S8 — kitchen floor at dawn with circling scratches
tiles = "".join(f'<line x1="{x}" y1="620" x2="{960 + (x - 960) * 2.6:.0f}" y2="1080" stroke="#1d1a1c" stroke-width="3"/>' for x in range(160, 1800, 120))
tiles += "".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#1d1a1c" stroke-width="3"/>' for y in (660, 720, 800, 900, 1030))
scr = ""
for i in range(6):
    rx, ry = 300 + i * 22, 90 + i * 7
    scr += f'<ellipse cx="960" cy="860" rx="{rx}" ry="{ry}" fill="none" stroke="#c9b9a8" stroke-width="2.6" opacity="{0.6 - i * 0.06:.2f}" stroke-dasharray="60 10 34 8" transform="rotate({i * 2 - 5} 960 860)"/>'
save("s8", svg(f'''
<rect width="{W}" height="{H}" fill="#0d0b0e"/>
<rect x="0" y="0" width="{W}" height="620" fill="#141116"/>
<rect x="200" y="300" width="1520" height="320" fill="#0a090c"/>
<rect x="200" y="300" width="1520" height="24" fill="#2a2228"/>
{''.join(f'<rect x="{x}" y="340" width="230" height="260" rx="6" fill="none" stroke="#1c171c" stroke-width="4"/><circle cx="{x + 200}" cy="470" r="6" fill="#4a3f44"/>' for x in range(230, 1700, 250) if not 700 < x < 1100)}
<rect x="760" y="80" width="400" height="230" fill="url(#dawn)"/>
<line x1="960" y1="80" x2="960" y2="310" stroke="#0a090c" stroke-width="10"/><line x1="760" y1="195" x2="1160" y2="195" stroke="#0a090c" stroke-width="10"/>
<rect x="740" y="60" width="440" height="270" fill="none" stroke="#0a090c" stroke-width="20"/>
{glow(960, 195, 200, "#ffb27a", 0.25)}
<polygon points="0,620 1920,620 1920,1080 0,1080" fill="#2b2629"/>
{tiles}
<polygon points="760,620 1160,620 1460,1080 460,1080" fill="#ffb27a" opacity="0.10"/>
{scr}
<ellipse cx="960" cy="860" rx="520" ry="160" fill="#000" opacity="0.15" filter="url(#blur60)"/>
''', sky("dawn", "#3a2a4a", "#a0606a", "#f0a070")))
