"""Scenes for 'The Book Drop' — a small-town library, a return slot that opens after nine, and an old checkout card."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

r = random.Random(2111)

LAMP = "#ffb54a"
GREEN = "#7fd38a"
RED = "#d8261e"
CARD = "#e6dcc0"
NIGHT = sky("night", "#04050c", "#151a30", "#2c2a40")


def books_row(x0, x1, y, hmin=70, hmax=110, palette=("#3a1f1a", "#22303a", "#2f2a1a", "#1f2a22", "#3b2c3a", "#2a1a14")):
    out, x = [], x0
    while x < x1:
        w = r.randint(14, 30); h = r.randint(int(hmin), int(hmax))
        lean = r.random() < 0.06
        c = r.choice(palette)
        tr = f' transform="rotate(8 {x + w} {y})"' if lean else ""
        out.append(f'<rect x="{x}" y="{y - h}" width="{w}" height="{h}" fill="{c}"{tr}/>'
                   f'<rect x="{x + 3}" y="{y - h + 12}" width="{w - 6}" height="4" fill="#000" opacity="0.25"/>')
        x += w + r.randint(1, 3)
    return "".join(out)


def shelf(x, y, w, h, rows=5, color="#1a120e"):
    rh = h / rows
    g = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"/>']
    for i in range(rows):
        base = y + rh * (i + 1) - 10
        g.append(books_row(x + 12, x + w - 34, base, rh * .55, rh * .8))
        g.append(f'<rect x="{x}" y="{base}" width="{w}" height="12" fill="#0d0907"/>')
    g.append(f'<rect x="{x}" y="{y}" width="12" height="{h}" fill="#0d0907"/><rect x="{x + w - 12}" y="{y}" width="12" height="{h}" fill="#0d0907"/>')
    return "".join(g)


def scrawl(x, y, w, color="#2a2540", sw=3):
    """A handwritten-looking squiggle (illegible name)."""
    pts, cx = [f"M{x} {y}"], x
    while cx < x + w:
        step = r.randint(10, 22)
        pts.append(f"q{step / 2:.0f} {r.randint(-16, -4)} {step} {r.randint(-3, 3)}")
        cx += step
    return f'<path d="{" ".join(pts)}" stroke="{color}" stroke-width="{sw}" fill="none" stroke-linecap="round"/>'


def red_stamp(x, y, w, h, rot=0, op=0.85):
    """A smudged red date stamp (no readable text)."""
    bars = "".join(f'<rect x="{x + 10 + i * (w - 20) / 5:.0f}" y="{y + 10}" width="{(w - 20) / 5 - 8:.0f}" height="{h - 20}" fill="{RED}" opacity="0.8"/>' for i in range(5))
    return (f'<g transform="rotate({rot} {x + w / 2} {y + h / 2})" opacity="{op}">'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{RED}" stroke-width="4"/>{bars}</g>')


def checkout_card(x, y, s=1.0, rows=8, filled=7, final=None, glow_last=False):
    """Old library card: header, ruled lines, names + red stamps; last row optional."""
    g = [f'<rect x="6" y="10" width="520" height="700" fill="#000" opacity="0.45" filter="url(#blur8)"/>',
         f'<rect x="0" y="0" width="520" height="700" fill="{CARD}"/>',
         '<rect x="0" y="0" width="520" height="700" fill="#8a6a3a" opacity="0.10"/>',
         f'<text x="260" y="62" text-anchor="middle" font-family="{SERIF}" font-weight="bold" font-size="34" fill="#3a2f22" letter-spacing="4">DATE DUE</text>',
         '<line x1="30" y1="90" x2="490" y2="90" stroke="#7a3a2a" stroke-width="3"/>',
         '<line x1="300" y1="90" x2="300" y2="690" stroke="#7a3a2a" stroke-width="2"/>']
    rh = 600 / rows
    for i in range(rows):
        ly = 90 + rh * (i + 1)
        g.append(f'<line x1="30" y1="{ly:.0f}" x2="490" y2="{ly:.0f}" stroke="#7d9bb5" stroke-width="2"/>')
        if i < filled:
            g.append(scrawl(45, ly - 22, r.randint(170, 230)))
            g.append(red_stamp(315, ly - rh + 14, 160, rh - 24, r.uniform(-4, 4), r.uniform(0.6, 0.9)))
        elif i == rows - 1 and glow_last:
            g.append(f'<rect x="30" y="{ly - rh:.0f}" width="460" height="{rh:.0f}" fill="#fff6da" opacity="0.55" filter="url(#blur8)"/>')
        if i == rows - 1 and final:
            g.append(final(ly, rh))
    return f'<g transform="translate({x} {y}) scale({s})">{"".join(g)}</g>'


scenes = {}

# S1 — the town library at night, book drop by the steps
cols = "".join(f'<rect x="{x}" y="430" width="34" height="330" fill="#1b1a26"/><rect x="{x - 8}" y="420" width="50" height="16" fill="#14131d"/>' for x in (700, 820, 1066, 1186))
scenes["s1"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>{stars(170, 380, 0.65)}
{moon(1500, 170, 60)}
{dead_tree(250, 820, 420)}{dead_tree(1720, 830, 360, s=0.8)}
<rect x="0" y="780" width="{W}" height="300" fill="#0d0d15"/>
<polygon points="600,420 960,270 1320,420" fill="#12111b"/><polygon points="640,412 960,290 1280,412" fill="#191826"/>
<circle cx="960" cy="360" r="34" fill="#0d0c14"/><circle cx="960" cy="360" r="26" fill="#d8ccb0" opacity="0.25"/>
<rect x="600" y="420" width="720" height="24" fill="#0f0e17"/>
<rect x="560" y="440" width="800" height="340" fill="#15141f"/>
<g stroke="#1d1c29" stroke-width="2">{"".join(f'<line x1="560" y1="{y}" x2="1360" y2="{y}"/>' for y in range(460, 780, 26))}</g>
{cols}
{lit_window(590, 500, 80, 130, LAMP)}
<rect x="1250" y="500" width="80" height="130" fill="#0b0b12"/>
<rect x="905" y="560" width="110" height="200" fill="#0a0910"/><rect x="915" y="570" width="90" height="70" fill="#1b2236"/>
<rect x="520" y="760" width="880" height="22" fill="#1e1d29"/><rect x="560" y="780" width="800" height="20" fill="#181724"/><rect x="600" y="798" width="720" height="18" fill="#13121c"/>
<g transform="translate(1210 690)">
<rect x="0" y="0" width="150" height="130" rx="14" fill="#1f2d44"/><path d="M0 14 Q75 -40 150 14" fill="#24344f"/>
<rect x="25" y="30" width="100" height="16" rx="4" fill="#05060a"/><rect x="25" y="30" width="100" height="16" rx="4" fill="{LAMP}" opacity="0.15"/>
<rect x="18" y="130" width="16" height="16" fill="#111"/><rect x="116" y="130" width="16" height="16" fill="#111"/>
<text x="75" y="88" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="20" fill="#9fb0c9" letter-spacing="2">BOOK</text>
<text x="75" y="112" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="20" fill="#9fb0c9" letter-spacing="2">RETURN</text>
</g>
<rect x="420" y="560" width="10" height="260" fill="#0a0a10"/><rect x="402" y="540" width="46" height="30" rx="6" fill="#16151f"/>
{glow(425, 560, 70, LAMP, 0.55)}
<polygon points="400,570 450,570 520,820 330,820" fill="{LAMP}" opacity="0.06"/>
{grass(1080, 300, "#07070c", (16, 40))}
{fog(820, "#aab3c8", 0.14, 90)}
''', NIGHT)

# S2 — inside: circulation desk, the slot in the wall, clock at nine
clock = (f'<g transform="translate(1180 210)"><circle r="62" fill="#d8ccb0"/><circle r="62" fill="none" stroke="#3a2a1a" stroke-width="8"/>'
         + "".join(f'<line x1="0" y1="-50" x2="0" y2="-42" stroke="#3a2a1a" stroke-width="4" transform="rotate({a})"/>' for a in range(0, 360, 30))
         + '<line x1="0" y1="0" x2="-34" y2="0" stroke="#1a120c" stroke-width="6"/><line x1="0" y1="0" x2="0" y2="-48" stroke="#1a120c" stroke-width="4"/><circle r="5" fill="#1a120c"/></g>')
scenes["s2"] = svg(f'''
<rect width="{W}" height="{H}" fill="#140f0d"/>
<rect x="0" y="0" width="{W}" height="700" fill="#1d1613"/>
{shelf(80, 160, 420, 560)}{shelf(1440, 160, 420, 560)}
<rect x="640" y="250" width="200" height="140" fill="#0d0b0a"/><rect x="652" y="262" width="176" height="116" fill="#20180f"/>
<rect x="690" y="312" width="100" height="14" rx="3" fill="#050404"/>
<rect x="660" y="390" width="160" height="80" fill="#2b2a2e"/><rect x="670" y="400" width="140" height="64" fill="#141316"/>
{clock}
<rect x="0" y="690" width="{W}" height="390" fill="#120d0b"/>
<rect x="560" y="610" width="900" height="40" fill="#3a2516"/><rect x="580" y="650" width="860" height="300" fill="#24170f"/>
<g stroke="#1a100a" stroke-width="3">{"".join(f'<line x1="{x}" y1="660" x2="{x}" y2="940"/>' for x in range(640, 1440, 120))}</g>
<g transform="translate(1260 610)"><path d="M0 0 L20 -150 L-40 -170" stroke="#2a2a30" stroke-width="10" fill="none"/>
<path d="M-90 -150 L-20 -190 L10 -150 Z" fill="#3a3a42"/></g>
{glow(1220, 560, 190, LAMP, 0.5)}
<polygon points="1170,450 1270,450 1380,610 1060,610" fill="{LAMP}" opacity="0.18"/>
<rect x="900" y="560" width="200" height="50" fill="#d8ccb0"/><rect x="910" y="545" width="190" height="20" fill="#c9bea2"/>
<rect x="700" y="575" width="140" height="35" rx="4" fill="#30353f"/><rect x="760" y="566" width="20" height="10" fill="#e33"/>
{glow(770, 570, 24, "#ff3b2f", 0.6)}
''')

# S3 — the metal slot creaks open
scenes["s3"] = svg(f'''
<rect width="{W}" height="{H}" fill="#18110e"/>
<g stroke="#21170f" stroke-width="3">{"".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in range(40, 1080, 70))}</g>
<rect x="560" y="260" width="800" height="320" rx="12" fill="#5c5c64"/>
<rect x="580" y="280" width="760" height="280" rx="8" fill="#6f6f78"/>
<rect x="640" y="370" width="640" height="110" rx="6" fill="#020203"/>
<g transform="translate(640 370)"><polygon points="0,0 640,0 620,-80 20,-80" fill="#8a8a94"/><polygon points="0,0 640,0 620,-80 20,-80" fill="#000" opacity="0.15"/>
<rect x="250" y="-60" width="140" height="16" rx="6" fill="#4a4a52"/></g>
<rect x="660" y="390" width="600" height="70" fill="#0e1424" opacity="0.8"/>
<ellipse cx="960" cy="420" rx="260" ry="26" fill="#3a4a7a" opacity="0.35" filter="url(#blur8)"/>
<text x="960" y="535" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="34" fill="#2a2a30" letter-spacing="6">RETURNS</text>
<rect x="600" y="640" width="720" height="360" fill="#2a1d14"/><rect x="600" y="640" width="720" height="30" fill="#3b2a1c"/>
<rect x="630" y="670" width="660" height="330" fill="#140d09"/>
<g opacity="0.8">{books_row(660, 1260, 760, 40, 70)}</g>
{glow(960, 440, 260, "#5a6a9a", 0.22)}
<polygon points="660,460 1260,460 1320,700 600,700" fill="#8aa0d8" opacity="0.05"/>
<g transform="translate(1520 240)"><circle r="54" fill="#d8ccb0"/><circle r="54" fill="none" stroke="#3a2a1a" stroke-width="7"/>
<line x1="0" y1="0" x2="-28" y2="6" stroke="#1a120c" stroke-width="5"/><line x1="0" y1="0" x2="18" y2="34" stroke="#1a120c" stroke-width="3"/><circle r="4" fill="#1a120c"/></g>
''')

# S4 — a small black book with no title, a card inside the cover
scenes["s4"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0d0907"/>
<rect x="420" y="160" width="1080" height="880" fill="#1d140e"/>
<rect x="460" y="200" width="1000" height="840" fill="#120c08"/>
{glow(960, 560, 380, LAMP, 0.28)}
<g transform="rotate(-8 960 600)">
<rect x="690" y="370" width="520" height="440" rx="10" fill="#000" opacity="0.55" filter="url(#blur30)"/>
<rect x="700" y="350" width="500" height="420" rx="8" fill="#0b0a0c"/>
<rect x="700" y="350" width="40" height="420" fill="#050406"/>
<rect x="1196" y="360" width="10" height="400" fill="#c9bea2"/>
<g transform="translate(940 270) rotate(6)"><rect x="0" y="0" width="200" height="280" fill="{CARD}"/>
<line x1="12" y1="40" x2="188" y2="40" stroke="#7a3a2a" stroke-width="3"/>
{"".join(f'<line x1="12" y1="{60 + i * 26}" x2="188" y2="{60 + i * 26}" stroke="#7d9bb5" stroke-width="2"/>' for i in range(5))}
<rect x="120" y="44" width="56" height="14" fill="{RED}" opacity="0.75"/><rect x="120" y="70" width="56" height="14" fill="{RED}" opacity="0.7"/>
</g>
<rect x="760" y="440" width="380" height="260" fill="none" stroke="#1a181c" stroke-width="4"/>
</g>
{books_row(480, 680, 1040, 140, 220)}{books_row(1240, 1440, 1040, 140, 220)}
<ellipse cx="960" cy="300" rx="380" ry="80" fill="{LAMP}" opacity="0.10" filter="url(#blur60)"/>
''')

# S5 — break-room wall: faded photos of the night clerks
def photo(x, y, w, h, people=1, empty=False):
    inner = ('<rect x="0" y="0" width="{w}" height="{h}" fill="#2c2924"/>'.format(w=w, h=h))
    if not empty:
        inner += f'<rect x="10" y="10" width="{w - 20}" height="{h - 20}" fill="#8f8572"/>'
        for k in range(people):
            px = (k + 1) * w / (people + 1)
            inner += (f'<ellipse cx="{px:.0f}" cy="{h * .42:.0f}" rx="{w * .09:.0f}" ry="{h * .12:.0f}" fill="#d2c7ae"/>'
                      f'<path d="M{px - w * .17:.0f} {h - 10} Q{px:.0f} {h * .5:.0f} {px + w * .17:.0f} {h - 10} Z" fill="#3a332a"/>')
        inner += f'<rect x="10" y="10" width="{w - 20}" height="{h - 20}" fill="#c9b892" opacity="0.35"/>'
    else:
        inner += f'<rect x="10" y="10" width="{w - 20}" height="{h - 20}" fill="#111"/>'
    return f'<g transform="translate({x} {y})"><rect x="-8" y="-8" width="{w + 16}" height="{h + 16}" fill="#120c08"/>{inner}</g>'

frames = [(480, 200, 200, 250, 1), (740, 170, 180, 220, 1), (980, 210, 220, 270, 2), (1260, 180, 180, 230, 1),
          (560, 520, 190, 240, 1), (820, 480, 210, 260, 1), (1090, 540, 180, 220, 1)]
scenes["s5"] = svg(f'''
<rect width="{W}" height="{H}" fill="#1c1814"/>
<g stroke="#241f1a" stroke-width="3">{"".join(f'<line x1="{x}" y1="0" x2="{x}" y2="820"/>' for x in range(0, W, 60))}</g>
<rect x="0" y="820" width="{W}" height="260" fill="#0f0c0a"/><rect x="0" y="812" width="{W}" height="16" fill="#2a2018"/>
{"".join(photo(*f) for f in frames)}
{photo(1320, 500, 180, 230, empty=True)}
<rect x="1310" y="490" width="200" height="250" fill="none" stroke="#5a1a14" stroke-width="3" opacity="0.6"/>
<path d="M1410 490 L1410 440" stroke="#3a3028" stroke-width="2"/><circle cx="1410" cy="438" r="5" fill="#6a5a48"/>
<rect x="1580" y="600" width="140" height="220" fill="#2b2b30"/><rect x="1590" y="612" width="120" height="60" fill="#1c1c20"/>
{glow(1100, 40, 260, "#d8e0c8", 0.18)}
<rect x="1040" y="0" width="120" height="16" fill="#cfd8c6"/>
<polygon points="1040,16 1160,16 1500,820 700,820" fill="#cfe0c8" opacity="0.04"/>
''')

# S6 — the checkout card: names, red dates, one empty line
scenes["s6"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0c0807"/>
<rect x="0" y="0" width="{W}" height="{H}" fill="#2a1a10" opacity="0.6"/>
{glow(960, 520, 420, LAMP, 0.22)}
{checkout_card(741, 50, 0.92, rows=8, filled=7, glow_last=True)}
<ellipse cx="960" cy="1040" rx="500" ry="80" fill="#000" opacity="0.5" filter="url(#blur30)"/>
''')

# S7 — the parking lot; behind, the return slot creaks open and stays open
scenes["s7"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>{stars(120, 360, 0.55)}
{moon(420, 160, 46)}
<rect x="0" y="700" width="{W}" height="380" fill="#101019"/>
<g stroke="#e6e0c8" stroke-width="5" opacity="0.25">{"".join(f'<line x1="{x}" y1="1080" x2="{x + 120}" y2="760"/>' for x in range(-100, 2000, 260))}</g>
<polygon points="1050,360 1350,260 1650,360" fill="#0d0c14"/>
<rect x="1060" y="360" width="580" height="340" fill="#0f0e17"/>
<rect x="1100" y="430" width="70" height="120" fill="#08080d"/><rect x="1530" y="430" width="70" height="120" fill="#08080d"/>
<rect x="1310" y="540" width="90" height="160" fill="#07070b"/>
<g transform="translate(1200 600)"><rect x="0" y="0" width="80" height="20" fill="#020203"/>
<polygon points="0,0 80,0 74,-26 6,-26" fill="#4a4a52"/><ellipse cx="40" cy="10" rx="34" ry="8" fill="{RED}" opacity="0.8"/></g>
{glow(1240, 610, 70, RED, 0.55)}
<g transform="translate(250 840)">
<path d="M0 0 L0 -70 Q10 -100 60 -104 L150 -112 L210 -170 L420 -170 L470 -110 L560 -100 Q600 -96 600 -60 L600 0 Z" fill="#1e2230"/>
<polygon points="220,-160 300,-160 300,-112 175,-112" fill="#0a0c12"/><polygon points="314,-160 410,-160 456,-112 314,-112" fill="#0a0c12"/>
<circle cx="120" cy="0" r="42" fill="#07070b"/><circle cx="480" cy="0" r="42" fill="#07070b"/>
<rect x="-6" y="-70" width="24" height="18" rx="4" fill="#fff3c4"/></g>
<polygon points="250,780 0,700 0,900" fill="#fff3c4" opacity="0.10" filter="url(#blur30)"/>
{glow(255, 778, 40, "#fff3c4", 0.7)}
{figure(1000, 880, 300, "#030306")}
<ellipse cx="1000" cy="882" rx="60" ry="10" fill="#000" opacity="0.6"/>
<circle cx="1440" cy="560" r="5" fill="#ffb54a" opacity="0.0"/>
<rect x="700" y="590" width="10" height="250" fill="#0a0a10"/><rect x="682" y="570" width="46" height="26" rx="6" fill="#16151f"/>
{glow(705, 590, 60, LAMP, 0.45)}
{fog(820, "#aab3c8", 0.12, 80)}
''', NIGHT)

# S8 — home: the coat on its hook, something in the pocket
scenes["s8"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0f0d12"/>
<g stroke="#17141b" stroke-width="3">{"".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}"/>' for x in range(0, W, 90))}</g>
<rect x="0" y="900" width="{W}" height="180" fill="#0a0809"/>
<rect x="1380" y="120" width="320" height="480" fill="#0a0d18"/><rect x="1395" y="135" width="290" height="450" fill="#1a2238"/>
<line x1="1540" y1="135" x2="1540" y2="585" stroke="#0a0d18" stroke-width="10"/><line x1="1395" y1="360" x2="1685" y2="360" stroke="#0a0d18" stroke-width="10"/>
<polygon points="1395,585 1685,585 1500,1080 1000,1080" fill="#8aa0d8" opacity="0.05"/>
<rect x="700" y="160" width="520" height="26" rx="6" fill="#3a2a1c"/>
<g fill="#6a5a42"><circle cx="820" cy="198" r="10"/><circle cx="960" cy="198" r="10"/><circle cx="1100" cy="198" r="10"/></g>
<path d="M960 200 Q880 210 820 260 L760 300 L720 760 Q720 800 760 810 L1160 810 Q1200 800 1200 760 L1160 300 L1100 260 Q1040 210 960 200 Z" fill="#2c2a30"/>
<path d="M960 210 L900 320 L960 760 L1020 320 Z" fill="#1c1a20"/>
<path d="M760 300 L700 720 L740 730 Z" fill="#232127"/><path d="M1160 300 L1220 720 L1180 730 Z" fill="#232127"/>
<g fill="#5a5560">{"".join(f'<circle cx="955" cy="{y}" r="9"/>' for y in (360, 460, 560, 660))}</g>
<rect x="790" y="600" width="140" height="110" rx="8" fill="#232127"/><path d="M790 600 h140" stroke="#18161c" stroke-width="8"/>
<g transform="rotate(-6 860 560)"><rect x="820" y="520" width="80" height="110" fill="{CARD}"/>
<line x1="826" y1="540" x2="894" y2="540" stroke="#7a3a2a" stroke-width="3"/>
<rect x="860" y="550" width="34" height="12" fill="{RED}" opacity="0.8"/></g>
{glow(860, 560, 90, "#fff1c8", 0.25)}
<rect x="380" y="520" width="200" height="380" fill="#120f0c"/><rect x="380" y="520" width="200" height="20" fill="#1e1914"/>
''')

# S9 — the card, close: the last line has a name... and a stamp
def final_row(ly, rh):
    return (scrawl(45, ly - 24, 220, "#141020", 4)
            + f'<g transform="rotate(-5 400 {ly - rh / 2:.0f})"><rect x="306" y="{ly - rh + 10:.0f}" width="196" height="{rh - 18:.0f}" fill="none" stroke="{RED}" stroke-width="5"/>'
            + f'<text x="404" y="{ly - rh / 2 + 8:.0f}" text-anchor="middle" font-family="{SANS}" font-weight="900" font-size="23" fill="{RED}">DUE TONIGHT</text></g>')

scenes["s9"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0a0607"/>
{glow(960, 560, 420, "#7a1a14", 0.3)}
{checkout_card(741, 50, 0.92, rows=8, filled=7, final=final_row)}
{glow(1120, 860, 120, RED, 0.25)}
''')

for k, v in scenes.items():
    save(k, v)
