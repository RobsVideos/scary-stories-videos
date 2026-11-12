"""Scenes for 'The Cabin Phone'. Run inside this folder: python3 scenes.py"""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *
import random

r = random.Random(12)


def pine(x, base, h, color="#070a10"):
    """Snowy pine silhouette."""
    out = [f'<rect x="{x - h * .03:.0f}" y="{base - h * .12:.0f}" width="{h * .06:.0f}" height="{h * .12:.0f}" fill="{color}"/>']
    for k in range(5):
        y = base - h * .1 - k * h * .17
        w = h * (.36 - k * .06)
        out.append(f'<polygon points="{x - w:.0f},{y:.0f} {x + w:.0f},{y:.0f} {x},{y - h * .3:.0f}" fill="{color}"/>')
        out.append(f'<path d="M{x - w * .8:.0f} {y - 4:.0f} Q{x} {y - h * .06:.0f} {x + w * .7:.0f} {y - 6:.0f}" stroke="#c9d3e6" stroke-width="5" fill="none" opacity="0.35"/>')
    return "".join(out)


def snowflakes(n, op=0.7, ymax=H):
    return "".join(f'<circle cx="{r.randint(0, W)}" cy="{r.randint(0, ymax)}" r="{r.choice([1.5, 2, 2.5, 3.5])}" fill="#e6ecf7" opacity="{r.uniform(.25, op):.2f}"/>' for _ in range(n))


def planks(x0, x1, y0, y1, c1="#24160f", c2="#1b100b", step=70):
    return "".join(f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="{step - 4}" fill="{c1 if i % 2 else c2}"/>'
                   f'<rect x="{x0}" y="{y + step - 4}" width="{x1 - x0}" height="4" fill="#0b0604"/>'
                   for i, y in enumerate(range(y0, y1, step)))


def rotary_phone(cx, cy, s=1.0, body="#1a1414", ring="#2a2020", glowc=None, receiver=True, shake=False):
    """Wall-mounted rotary phone centred at (cx, cy)."""
    g = ""
    if glowc:
        g = glow(cx, cy, 260 * s, glowc, 0.35)
    holes = "".join(
        f'<circle cx="{cx + 62 * s * __import__("math").cos(a):.0f}" cy="{cy + 40 * s + 62 * s * __import__("math").sin(a):.0f}" r="{13 * s:.0f}" fill="#0a0707"/>'
        for a in [i * 0.52 - 2.6 for i in range(10)])
    rec = ""
    if receiver:
        rec = (f'<path d="M{cx - 150 * s} {cy - 110 * s} Q{cx} {cy - 170 * s} {cx + 150 * s} {cy - 110 * s} '
               f'L{cx + 150 * s} {cy - 70 * s} Q{cx} {cy - 120 * s} {cx - 150 * s} {cy - 70 * s} Z" fill="{body}"/>'
               f'<ellipse cx="{cx - 150 * s}" cy="{cy - 88 * s}" rx="{42 * s}" ry="{30 * s}" fill="{body}"/>'
               f'<ellipse cx="{cx + 150 * s}" cy="{cy - 88 * s}" rx="{42 * s}" ry="{30 * s}" fill="{body}"/>')
    sh = ""
    if shake:
        sh = "".join(f'<path d="M{cx + sx * (230 + k * 45) * s:.0f} {cy - 120 * s:.0f} q{sx * 30 * s:.0f} {80 * s:.0f} 0 {160 * s:.0f}" '
                     f'stroke="#ff5a3c" stroke-width="{8 - k * 2}" fill="none" stroke-linecap="round" opacity="{0.9 - k * 0.25:.2f}"/>'
                     for sx in (-1, 1) for k in range(3))
    return (g + f'<rect x="{cx - 130 * s}" y="{cy - 90 * s}" width="{260 * s}" height="{300 * s}" rx="{40 * s}" fill="{body}"/>'
            f'<rect x="{cx - 130 * s}" y="{cy - 90 * s}" width="{260 * s}" height="{300 * s}" rx="{40 * s}" fill="none" stroke="#4a3a30" stroke-width="{3 * s}" opacity="0.6"/>'
            f'<circle cx="{cx}" cy="{cy + 40 * s}" r="{92 * s}" fill="{ring}"/>{holes}'
            f'<circle cx="{cx}" cy="{cy + 40 * s}" r="{30 * s}" fill="#c9b994"/>'
            f'<path d="M{cx + 70 * s} {cy + 110 * s} l{30 * s} {20 * s}" stroke="#8a8070" stroke-width="{5 * s}"/>'
            + rec + sh)


def cut_cord(x, y, s=1.0, color="#120d0d"):
    return (f'<path d="M{x} {y} C{x - 20 * s} {y + 80 * s} {x + 30 * s} {y + 140 * s} {x - 10 * s} {y + 230 * s} '
            f'C{x - 30 * s} {y + 290 * s} {x + 20 * s} {y + 330 * s} {x + 6 * s} {y + 380 * s}" stroke="{color}" stroke-width="{12 * s}" fill="none" stroke-dasharray="{14 * s} {5 * s}" stroke-linecap="round"/>'
            f'<path d="M{x + 6 * s} {y + 380 * s} l-8 14 m8 -14 l4 16 m-4 -16 l12 10" stroke="#b56a3a" stroke-width="3"/>')


scenes = {}

# S1 — cabin in the snow
cabin = f'''
<g fill="#07080d">
<polygon points="700,820 700,600 960,450 1220,600 1220,820"/>
<polygon points="660,612 960,420 1260,612 1250,630 960,445 670,630"/>
<rect x="1080" y="440" width="44" height="110"/>
<rect x="760" y="760" width="400" height="20" fill="#0d0e14"/>
</g>
<path d="M660 612 L960 420 L1260 612" stroke="#d6deee" stroke-width="10" fill="none" opacity="0.75"/>
<rect x="1076" y="436" width="52" height="10" fill="#d6deee" opacity="0.7"/>
{lit_window(770, 640, 100, 90)}
{lit_window(1050, 640, 100, 90)}
<rect x="920" y="680" width="80" height="140" fill="#100c0a"/>
<circle cx="985" cy="755" r="5" fill="#a7853f"/>
<path d="M1100 430 C1080 380 1140 350 1110 290 C1090 250 1150 220 1130 170" stroke="#9aa3b8" stroke-width="30" fill="none" opacity="0.18" filter="url(#blur30)"/>
'''
scenes["s1"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(120, 450, 0.6)}
{moon(1380, 200, 70)}
<path d="M0 700 C400 640 800 680 1200 650 C1500 630 1700 660 1920 640 L1920 1080 L0 1080Z" fill="#1a2030"/>
{pine(200, 760, 420, "#0b0f18")}{pine(380, 740, 330, "#0b0f18")}{pine(1550, 740, 400, "#0b0f18")}{pine(1720, 760, 340, "#0b0f18")}
{fog(720, op=0.18)}
<path d="M0 810 C500 790 1300 800 1920 790 L1920 1080 L0 1080Z" fill="#c4cde0" opacity="0.22"/>
{cabin}
<path d="M0 840 C400 820 1500 830 1920 815 L1920 1080 L0 1080Z" fill="#8d97ad"/>
<path d="M0 900 C500 880 1300 900 1920 885 L1920 1080 L0 1080Z" fill="#6b7590"/>
<polygon points="770,820 870,820 900,1080 690,1080" fill="#ffb54a" opacity="0.12" filter="url(#blur30)"/>
<polygon points="1050,820 1150,820 1250,1080 1020,1080" fill="#ffb54a" opacity="0.12" filter="url(#blur30)"/>
{pine(560, 1000, 520)}{pine(1400, 1010, 560)}
{snowflakes(220)}
''', sky("sky1", "#04060e", "#141a30", "#2c3550"))

# S2 — the rotary phone with a cut cord
kitchen_wall = planks(0, W, 0, H, "#2a1a11", "#22150e", 80)
scenes["s2"] = svg(f'''
{kitchen_wall}
<rect width="{W}" height="{H}" fill="#000" opacity="0.35"/>
{glow(1300, 150, 300, "#ffb54a", 0.12)}
{glow(960, 520, 420, "#ffb060", 0.22)}
<rect x="780" y="300" width="360" height="460" rx="20" fill="#000" opacity="0.4" filter="url(#blur30)"/>
{rotary_phone(960, 470, 1.1, body="#2a1c18", ring="#3a2a24", receiver=True)}
{cut_cord(1050, 700, 0.75, "#4a3428")}
<rect x="1400" y="640" width="400" height="18" fill="#140c08"/>
<rect x="1450" y="560" width="60" height="80" rx="8" fill="#140c08"/><rect x="1540" y="580" width="40" height="60" rx="6" fill="#140c08"/>
<path d="M250 0 L250 180" stroke="#0a0604" stroke-width="4"/><path d="M200 180 L300 180 L280 230 L220 230Z" fill="#0f0905"/>
{fog(1000, "#ffcf8a", 0.05)}
''')

# S3 — guestbook with the rule
lines_txt = "".join(f'<path d="M{x0} {y} q40 -10 80 0 t80 0 t80 0 t60 0" stroke="#5a4a38" stroke-width="3" fill="none" opacity="0.6"/>'
                    for x0 in (560, 1000) for y in range(420, 700, 46) if not (x0 == 1000 and 500 < y < 640))
scenes["s3"] = svg(f'''
<rect width="{W}" height="{H}" fill="#120b07"/>
{glow(1400, 330, 300, "#ffb04a", 0.45)}
<rect x="0" y="700" width="{W}" height="380" fill="#24160e"/>
<g stroke="#120a06" stroke-width="3">{''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in (780, 880, 990))}</g>
<g transform="rotate(-4 960 560)">
<rect x="510" y="340" width="900" height="460" rx="14" fill="#3b1f14"/>
<path d="M530 360 L955 380 L955 800 L530 780Z" fill="#d9cba8"/>
<path d="M965 380 L1390 360 L1390 780 L965 800Z" fill="#e3d6b4"/>
<rect x="950" y="375" width="20" height="430" fill="#000" opacity="0.25" filter="url(#blur8)"/>
{lines_txt}
<text x="1180" y="560" text-anchor="middle" font-family="DejaVu Serif, serif" font-style="italic" font-size="44" fill="#2a1a10">If it rings,</text>
<text x="1180" y="615" text-anchor="middle" font-family="DejaVu Serif, serif" font-style="italic" font-size="44" fill="#8a1a14">don't answer.</text>
<path d="M1050 632 L1310 628" stroke="#8a1a14" stroke-width="4"/><path d="M1055 645 L1305 642" stroke="#8a1a14" stroke-width="4"/>
</g>
<g transform="translate(1440 440)">
<rect x="-26" y="0" width="52" height="170" rx="6" fill="#efe6cf"/>
<path d="M0 -6 C-14 -40 4 -60 0 -80 C10 -55 16 -35 0 -6Z" fill="#ffc35a"/>
<ellipse cx="0" cy="-30" rx="16" ry="34" fill="#ffd27a" opacity="0.7" filter="url(#blur8)"/>
<ellipse cx="0" cy="175" rx="60" ry="14" fill="#2a1a10"/>
</g>
<rect x="620" y="770" width="220" height="16" rx="8" fill="#14100c" transform="rotate(20 730 778)"/>
''')

# S4 — a perfect first night: fire and falling snow
logs = "".join(f'<rect x="{x}" y="{y}" width="260" height="46" rx="23" fill="#2a170c"/><circle cx="{x + 240}" cy="{y + 23}" r="20" fill="#5a3a20"/>'
               for x, y in ((180, 900), (170, 850), (200, 800), (1500, 900), (1520, 850)))
scenes["s4"] = svg(f'''
<rect width="{W}" height="{H}" fill="#140c08"/>
{planks(0, W, 0, H, "#1f130c", "#1a100a", 90)}
<rect width="{W}" height="{H}" fill="#000" opacity="0.3"/>
<rect x="620" y="260" width="680" height="640" fill="#2b2622"/>
<g fill="#3a332d" stroke="#1d1814" stroke-width="4">{''.join(f'<rect x="{x}" y="{y}" width="110" height="60"/>' for y in range(260, 900, 64) for x in range(620 + (y // 64 % 2) * 55 - 55, 1300, 112) if x >= 600)}</g>
<rect x="600" y="240" width="720" height="40" fill="#1a1410"/>
<path d="M740 900 L740 560 Q960 470 1180 560 L1180 900Z" fill="#0b0705"/>
{glow(960, 800, 220, "#ff8a2a", 0.8)}
<path d="M860 860 C840 780 900 760 890 690 C930 740 950 700 940 640 C990 700 1010 740 1000 690 C1050 750 1070 800 1050 860Z" fill="#ff9a3a"/>
<path d="M900 860 C890 810 930 790 925 750 C960 790 970 760 975 730 C1000 780 1020 810 1010 860Z" fill="#ffd27a"/>
<rect x="820" y="855" width="280" height="30" rx="14" fill="#2a170c"/>
<polygon points="600,900 1320,900 1500,1080 420,1080" fill="#ff8a2a" opacity="0.12" filter="url(#blur30)"/>
{logs}
<g transform="translate(1440 300)">
<rect x="0" y="0" width="300" height="360" fill="#16203a"/>
<g clip-path="url(#win4)">{''.join(f'<circle cx="{r.randint(0, 300)}" cy="{r.randint(0, 360)}" r="{r.choice([2, 3, 4])}" fill="#e8eef9" opacity="0.8"/>' for _ in range(60))}
<path d="M0 300 C100 280 200 300 300 290 L300 360 L0 360Z" fill="#9aa6c0"/></g>
<rect x="0" y="0" width="300" height="360" fill="none" stroke="#0c0705" stroke-width="16"/>
<line x1="150" y1="0" x2="150" y2="360" stroke="#0c0705" stroke-width="10"/><line x1="0" y1="180" x2="300" y2="180" stroke="#0c0705" stroke-width="10"/>
</g>
''', '<clipPath id="win4"><rect x="0" y="0" width="300" height="360"/></clipPath>')

# S5 — 3 a.m., the phone rings
clock = '''<g transform="translate(560 260)">
<circle r="80" fill="#cfc4a8"/><circle r="80" fill="none" stroke="#2a1a10" stroke-width="10"/>
<line x1="0" y1="0" x2="0" y2="-55" stroke="#120a06" stroke-width="7"/><line x1="0" y1="0" x2="38" y2="0" stroke="#120a06" stroke-width="9"/>
<circle r="7" fill="#120a06"/></g>'''
scenes["s5"] = svg(f'''
{planks(0, W, 0, H, "#1a1214", "#151012", 80)}
<rect width="{W}" height="{H}" fill="#06070f" opacity="0.55"/>
<polygon points="1500,0 1920,0 1920,1080 1700,1080" fill="#7f97c9" opacity="0.10"/>
{clock}
{rotary_phone(960, 470, 1.1, body="#2a1616", ring="#3a2020", glowc="#ff3b2f", shake=True)}
{cut_cord(1050, 700, 0.75, "#6a3a30")}
{fog(1000, "#ff6a4a", 0.06)}
''')

# S6 — someone in the dark kitchen picks it up
fig = figure(880, 1040, 820, "#030203")
scenes["s6"] = svg(f'''
{planks(0, W, 0, H, "#120d10", "#0f0b0d", 80)}
<rect width="{W}" height="{H}" fill="#04050b" opacity="0.6"/>
<polygon points="1350,120 1650,120 1650,520 1350,520" fill="#8fa6d8" opacity="0.35"/>{glow(1500, 320, 260, "#8fa6d8", 0.25)}
<polygon points="1350,520 1650,520 1300,1080 700,1080" fill="#8fa6d8" opacity="0.07"/>
<line x1="1500" y1="120" x2="1500" y2="520" stroke="#04050b" stroke-width="10"/><line x1="1350" y1="320" x2="1650" y2="320" stroke="#04050b" stroke-width="10"/>
{rotary_phone(1110, 420, 0.8, body="#140c0c", receiver=False)}
{glow(880, 600, 380, "#8fa6d8", 0.16)}
{figure(884, 1040, 820, "#5a6a90")}
{fig}
<path d="M960 470 C990 420 980 360 945 330" stroke="#030203" stroke-width="34" fill="none" stroke-linecap="round"/>
<rect x="912" y="236" width="40" height="150" rx="16" fill="#2a2026"/>
<path d="M940 386 C980 460 930 520 970 580 C1000 630 960 680 985 730" stroke="#3a4462" stroke-width="9" fill="none" stroke-dasharray="11 4"/>
<path d="M985 730 l-8 14 m8 -14 l4 16 m-4 -16 l12 10" stroke="#b56a3a" stroke-width="3"/>
<rect x="0" y="880" width="{W}" height="200" fill="#0a0708"/>
<rect x="0" y="870" width="620" height="22" fill="#1a1214"/>
{fog(980, "#8fa6d8", 0.07)}
''')

# S7 — bedroom: the door opens, he leans over the bed
scenes["s7"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0a0a12"/>
{planks(0, W, 0, 720, "#14121c", "#100e17", 90)}
<rect width="{W}" height="{H}" fill="#000" opacity="0.4"/>
<rect x="1180" y="160" width="300" height="560" fill="#060508"/>
<rect x="1180" y="160" width="300" height="560" fill="#ff9a4a" opacity="0.10"/>
<polygon points="1480,160 1640,120 1640,760 1480,720" fill="#2a1d18"/>
<polygon points="1180,720 1480,720 1700,1080 960,1080" fill="#ff9a4a" opacity="0.06"/>
<path d="M1130 720 C1100 560 1090 420 1110 300 C1120 250 1180 240 1200 290 C1215 330 1220 380 1215 440 C1060 450 960 470 900 520" stroke="#030203" stroke-width="0" fill="#030203"/>
<g fill="#030203">
<ellipse cx="900" cy="470" rx="62" ry="76" transform="rotate(-30 900 470)"/>
<path d="M1240 720 L1250 420 C1250 340 1200 300 1130 330 C1060 360 980 420 930 470 L960 520 C1030 480 1100 460 1150 470 L1160 720Z"/>
<path d="M1150 470 C1100 520 1060 580 1030 640" stroke="#030203" stroke-width="40" stroke-linecap="round"/>
</g>
{eyes(885, 470, 30, 6)}
<rect x="300" y="640" width="1100" height="80" rx="20" fill="#1c2030"/>
<path d="M300 700 C500 640 900 660 1400 690 L1400 900 L300 900Z" fill="#2a3048"/>
<path d="M300 700 C500 640 900 660 1400 690" stroke="#3c4566" stroke-width="6" fill="none"/>
<ellipse cx="560" cy="650" rx="150" ry="55" fill="#3c4566"/>
<path d="M600 640 C640 600 720 600 760 650 C700 680 640 680 600 640Z" fill="#141826"/>
<rect x="260" y="560" width="40" height="440" fill="#0e0c12"/><rect x="1400" y="620" width="36" height="380" fill="#0e0c12"/>
<rect x="0" y="900" width="{W}" height="180" fill="#07060a"/>
{fog(900, "#8fa6d8", 0.06)}
''')

# S8 — dawn: signing the guestbook
sig = '<path d="M1060 600 c20 -60 40 -60 30 0 c-6 40 20 -40 40 -30 c20 10 -10 40 10 40 c30 0 40 -60 60 -40 c10 20 0 40 20 30 c20 -10 30 -30 50 -20 c10 10 20 0 40 -10" stroke="#1a2a6a" stroke-width="6" fill="none" stroke-linecap="round"/>'
scenes["s8"] = svg(f'''
<rect width="{W}" height="{H}" fill="#1a2234"/>
<rect x="1300" y="80" width="460" height="400" fill="url(#dawn)"/>
<rect x="1300" y="80" width="460" height="400" fill="none" stroke="#0e0b0a" stroke-width="18"/>
<line x1="1530" y1="80" x2="1530" y2="480" stroke="#0e0b0a" stroke-width="10"/>
{pine(1380, 480, 180, "#1a2034")}{pine(1660, 480, 220, "#1a2034")}
{glow(1530, 300, 260, "#9fb4e8", 0.2)}
<rect x="0" y="700" width="{W}" height="380" fill="#2a1d16"/>
<g transform="rotate(-3 960 560)">
<rect x="510" y="340" width="900" height="460" rx="14" fill="#3b1f14"/>
<path d="M530 360 L955 380 L955 800 L530 780Z" fill="#c9c4b4"/>
<path d="M965 380 L1390 360 L1390 780 L965 800Z" fill="#d3cebd"/>
{lines_txt}
<line x1="1030" y1="620" x2="1340" y2="612" stroke="#5a4a38" stroke-width="3"/>
{sig}
</g>
<g transform="rotate(35 1360 600)"><rect x="1320" y="560" width="26" height="260" rx="10" fill="#101418"/><polygon points="1320,820 1346,820 1333,850" fill="#c9b994"/></g>
<rect x="160" y="640" width="260" height="120" rx="14" fill="#141826"/><rect x="200" y="610" width="180" height="40" rx="12" fill="#141826"/>
''', sky("dawn", "#3a4a78", "#8a8fb0", "#d8a98a"))

# S9 — home, the phone lights up: CABIN
scenes["s9"] = svg(f'''
<rect width="{W}" height="{H}" fill="#06070c"/>
<rect x="0" y="0" width="{W}" height="620" fill="#0b0d16"/>
<g fill="#10131e">{''.join(f'<rect x="{x}" y="120" width="220" height="300" rx="6"/>' for x in (180, 1520))}</g>
<rect x="0" y="620" width="{W}" height="40" fill="#1a1d28"/>
<rect x="0" y="660" width="{W}" height="420" fill="#0c0e15"/>
{glow(960, 560, 360, "#ff3b2f", 0.22)}
<g transform="translate(960 560) rotate(-8)">
<rect x="-150" y="-280" width="300" height="560" rx="44" fill="#050608"/>
<rect x="-132" y="-258" width="264" height="516" rx="30" fill="#140a0c"/>
<rect x="-132" y="-258" width="264" height="516" rx="30" fill="url(#scr)"/>
<text x="0" y="-150" text-anchor="middle" font-family="{SANS}" font-size="22" fill="#e9d7d4" opacity="0.7" letter-spacing="3">INCOMING CALL</text>
<text x="0" y="-80" text-anchor="middle" font-family="{SANS}" font-size="56" font-weight="bold" fill="#fff4f0">CABIN</text>
<circle cx="0" cy="40" r="56" fill="#3a1414"/>
<circle cx="0" cy="22" r="22" fill="#6a2a2a"/><path d="M-34 78 C-30 46 30 46 34 78Z" fill="#6a2a2a"/>
<circle cx="-70" cy="190" r="34" fill="#c0302a"/><circle cx="70" cy="190" r="34" fill="#2aa04a"/>
<rect x="-86" y="184" width="32" height="12" rx="6" fill="#fff" transform="rotate(-20 -70 190)"/>
<rect x="54" y="184" width="32" height="12" rx="6" fill="#fff"/>
</g>
<g stroke="#ff5a3c" stroke-width="5" fill="none" opacity="0.6" stroke-linecap="round">
<path d="M700 420 q-30 80 0 160"/><path d="M660 400 q-40 100 0 200"/><path d="M1220 420 q30 80 0 160"/><path d="M1260 400 q40 100 0 200"/></g>
<path d="M1500 660 L1500 600 L1560 600 L1560 660" fill="#14161f"/><rect x="1480" y="560" width="100" height="44" rx="10" fill="#14161f"/>
''', '<linearGradient id="scr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5a1a1c"/><stop offset="1" stop-color="#1a0a0c"/></linearGradient>')

for name, s in scenes.items():
    save(name, s)
print("drew", ", ".join(scenes))
