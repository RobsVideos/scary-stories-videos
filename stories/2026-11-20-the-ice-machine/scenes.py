"""Scenes for 'The Ice Machine' — a desert motel, a humming ice machine, and a knock with a full bucket."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

r = random.Random(1120)

NEON = "#ff3b4e"
ICE = "#8fd8ff"
LAMP = "#ffb54a"


def cactus(x, base, h=260, color="#07060c"):
    w = h * 0.13
    return (f'<g fill="{color}" stroke="{color}" stroke-linecap="round" fill-opacity="1">'
            f'<rect x="{x - w / 2:.0f}" y="{base - h}" width="{w:.0f}" height="{h}" rx="{w / 2:.0f}"/>'
            f'<path d="M{x - w / 2:.0f} {base - h * .45:.0f} h{-w * 1.2:.0f} v{-h * .32:.0f}" fill="none" stroke-width="{w * .8:.0f}"/>'
            f'<path d="M{x + w / 2:.0f} {base - h * .6:.0f} h{w * 1.1:.0f} v{-h * .25:.0f}" fill="none" stroke-width="{w * .8:.0f}"/></g>')


def bucket(cx, base, s=1.0, full=False, melt=False):
    """Plastic motel ice bucket."""
    ice = ""
    if full:
        cubes = "".join(f'<rect x="{-70 + i * 28 + r.randint(-6, 6)}" y="{-178 + r.randint(-14, 6)}" width="30" height="30" rx="6" '
                        f'fill="#dff4ff" opacity="{r.uniform(.75, .95):.2f}" transform="rotate({r.randint(-30, 30)} {-55 + i * 28} -165)"/>'
                        for i in range(6))
        ice = cubes if not melt else '<ellipse cx="0" cy="-168" rx="88" ry="16" fill="#bfe6ff" opacity="0.8"/>'
    return (f'<g transform="translate({cx} {base}) scale({s})">'
            f'<ellipse cx="0" cy="4" rx="120" ry="20" fill="#000" opacity="0.5" filter="url(#blur8)"/>'
            f'<path d="M-100 -170 L-80 0 L80 0 L100 -170 Z" fill="url(#bk)"/>'
            f'{ice}'
            f'<ellipse cx="0" cy="-170" rx="100" ry="20" fill="none" stroke="#c9a46a" stroke-width="10"/>'
            f'<path d="M-92 -110 L92 -110" stroke="#8a6a3a" stroke-width="6" opacity="0.6"/>'
            f'<path d="M-104 -160 C-130 -240 130 -240 104 -160" fill="none" stroke="#3a2c1e" stroke-width="7"/></g>')


BK = '''<linearGradient id="bk" x1="0" x2="1"><stop offset="0" stop-color="#6b4f2c"/><stop offset="0.45" stop-color="#d1aa6c"/><stop offset="1" stop-color="#4a3520"/></linearGradient>'''

# S1 — desert motel at night
doors = ""
for i, x in enumerate(range(520, 1460, 150)):
    lit = i == 3
    doors += (f'<rect x="{x}" y="560" width="70" height="150" fill="#1a1520"/>'
              f'<rect x="{x + 82}" y="585" width="48" height="50" fill="{LAMP if lit else "#120f18"}"/>'
              + (f'<rect x="{x + 82}" y="585" width="48" height="50" fill="{LAMP}" filter="url(#blur30)"/>' if lit else "")
              + f'<circle cx="{x + 35}" cy="545" r="5" fill="#ffe2a8"/><circle cx="{x + 35}" cy="545" r="20" fill="#ffd79a" opacity="0.35" filter="url(#blur8)"/>')
save("s1", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sk1)"/>
{stars(220, 560, 0.9)}
{moon(1060, 170, 64)}
<path d="M0 640 L180 560 L330 600 L520 520 L700 610 L1300 600 L1500 540 L1700 590 L1920 560 L1920 760 L0 760Z" fill="#1c1628"/>
<rect x="0" y="720" width="{W}" height="360" fill="#140f1a"/>
<g fill="#0a0810">
<rect x="460" y="500" width="1040" height="220"/>
<polygon points="430,510 1530,510 1500,480 460,480"/>
</g>
<rect x="460" y="700" width="1040" height="20" fill="#2a2230"/>
{doors}
<g transform="translate(1390 250)">
<rect x="-6" y="120" width="14" height="350" fill="#0a0810"/>
<rect x="-110" y="0" width="220" height="130" rx="10" fill="#0d0a12" stroke="{NEON}" stroke-width="5"/>
<text x="0" y="70" text-anchor="middle" font-family="{SANS}" font-weight="700" font-size="58" fill="{NEON}" letter-spacing="6">MOTEL</text>
<text x="0" y="112" text-anchor="middle" font-family="{SANS}" font-size="26" fill="#ff8a96" letter-spacing="4">VACANCY</text>
<rect x="-110" y="0" width="220" height="130" fill="{NEON}" opacity="0.35" filter="url(#blur30)"/>
</g>
{glow(1390, 320, 260, NEON, 0.18)}
<g transform="translate(700 790)">
<path d="M0 0 L20 -60 Q40 -95 110 -100 L260 -100 Q300 -96 330 -60 L380 -50 Q400 -40 400 0 Z" fill="#0b0910"/>
<circle cx="80" cy="0" r="34" fill="#050407"/><circle cx="320" cy="0" r="34" fill="#050407"/>
<path d="M70 -60 L110 -92 L250 -92 L290 -60 Z" fill="#1d2433"/>
</g>
{cactus(220, 860, 300)}{cactus(1820, 900, 240)}{cactus(380, 780, 160, "#0d0a14")}
<ellipse cx="960" cy="730" rx="900" ry="60" fill="{NEON}" opacity="0.06" filter="url(#blur30)"/>
{fog(800, "#9a8fb8", 0.10)}
<path d="M0 940 C500 910 1300 930 1920 915 L1920 1080 L0 1080Z" fill="#0a0810"/>
''', sky("sk1", "#04050d", "#1a1538", "#4a2340") + BK))

# S2 — front desk: key, empty bucket, clerk
save("s2", svg(f'''
<rect width="{W}" height="{H}" fill="#140d0c"/>
<rect x="0" y="0" width="{W}" height="640" fill="url(#wall2)"/>
<g stroke="#2a1a14" stroke-width="3" opacity="0.5">{''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="640"/>' for x in range(0, W, 60))}</g>
<g transform="translate(1180 140)">
<rect width="260" height="230" fill="#22150f" stroke="#3a2518" stroke-width="6"/>
{''.join(f'<circle cx="{35 + (k % 4) * 62}" cy="{40 + (k // 4) * 60}" r="7" fill="#6e5a3a"/><rect x="{28 + (k % 4) * 62}" y="{48 + (k // 4) * 60}" width="14" height="26" rx="3" fill="{"#1a0f0b" if k == 5 else "#8a3a2a"}"/>' for k in range(12))}
</g>
<g fill="#060404">
<ellipse cx="760" cy="300" rx="72" ry="88"/>
<path d="M600 640 C600 470 650 410 760 405 C870 410 920 470 920 640Z"/>
</g>
<rect x="745" y="285" width="8" height="8" fill="{LAMP}" opacity="0.5"/>
<rect x="0" y="620" width="{W}" height="60" fill="#3a2416"/>
<rect x="0" y="680" width="{W}" height="400" fill="url(#desk2)"/>
<g transform="translate(520 430)">
<path d="M-90 0 L90 0 L60 -80 L-60 -80Z" fill="#c98a3a"/>
<path d="M-90 0 L90 0 L60 -80 L-60 -80Z" fill="{LAMP}" opacity="0.4" filter="url(#blur8)"/>
<rect x="-6" y="0" width="12" height="180" fill="#20140c"/><ellipse cx="0" cy="190" rx="60" ry="14" fill="#20140c"/>
</g>
{glow(520, 560, 220, LAMP, 0.35)}
{bucket(1080, 660, 1.15)}
<g transform="translate(780 650) rotate(-12)">
<path d="M0 0 L120 -30 L150 10 L30 40 Z" fill="#b8322a"/>
<text x="80" y="12" text-anchor="middle" font-family="{SANS}" font-weight="700" font-size="30" fill="#f3e2c6" transform="rotate(-14 80 12)">7</text>
<circle cx="20" cy="10" r="9" fill="#2a120f"/>
<path d="M-10 6 L-90 30 L-95 20 L-100 30 L-106 22" fill="none" stroke="#d9c38a" stroke-width="9" stroke-linecap="round"/>
<circle cx="-2" cy="4" r="16" fill="none" stroke="#d9c38a" stroke-width="5"/>
</g>
''', BK + '''<linearGradient id="wall2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a100c"/><stop offset="1" stop-color="#3a2216"/></linearGradient>
<linearGradient id="desk2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a2c18"/><stop offset="1" stop-color="#160c07"/></linearGradient>'''))

# S3 — the ice machine in its concrete alcove
save("s3", svg(f'''
<rect width="{W}" height="{H}" fill="#07080c"/>
<polygon points="560,120 1360,120 1360,900 560,900" fill="#1a1d24"/>
<g stroke="#11131a" stroke-width="3">{''.join(f'<line x1="560" y1="{y}" x2="1360" y2="{y}"/>' for y in range(160, 900, 70))}{''.join(f'<line x1="{x + (40 if (y // 70) % 2 else 0)}" y1="{y}" x2="{x + (40 if (y // 70) % 2 else 0)}" y2="{y + 70}"/>' for y in range(160, 900, 70) for x in range(600, 1360, 160))}</g>
<rect x="760" y="150" width="400" height="20" rx="8" fill="#e8f6ff"/>
<rect x="740" y="140" width="440" height="40" fill="{ICE}" opacity="0.5" filter="url(#blur30)"/>
<polygon points="760,170 1160,170 1420,900 500,900" fill="{ICE}" opacity="0.07"/>
<g transform="translate(700 330)">
<rect width="520" height="560" rx="14" fill="url(#steel)"/>
<rect x="30" y="30" width="460" height="150" rx="8" fill="#2b313c"/>
<text x="260" y="128" text-anchor="middle" font-family="{SANS}" font-weight="700" font-size="88" fill="{ICE}" letter-spacing="14">ICE</text>
<text x="260" y="128" text-anchor="middle" font-family="{SANS}" font-weight="700" font-size="88" fill="{ICE}" letter-spacing="14" filter="url(#blur8)" opacity="0.7">ICE</text>
<rect x="90" y="240" width="340" height="190" rx="10" fill="#14181f" stroke="#59616e" stroke-width="6"/>
<rect x="130" y="320" width="260" height="20" rx="10" fill="#9aa3b0"/>
{''.join(f'<line x1="{x}" y1="470" x2="{x}" y2="540" stroke="#3a414c" stroke-width="6"/>' for x in range(60, 480, 30))}
</g>
<rect x="700" y="330" width="520" height="560" fill="{ICE}" opacity="0.05"/>
<rect x="0" y="900" width="{W}" height="180" fill="#101218"/>
<ellipse cx="960" cy="905" rx="420" ry="30" fill="#000" opacity="0.7" filter="url(#blur8)"/>
<path d="M1260 900 q20 -6 40 0 q30 10 70 2" fill="none" stroke="{ICE}" stroke-width="3" opacity="0.35"/>
<ellipse cx="1300" cy="912" rx="90" ry="10" fill="{ICE}" opacity="0.18"/>
<rect x="0" y="0" width="560" height="900" fill="#050609"/><rect x="1360" y="0" width="560" height="900" fill="#050609"/>
''', '''<linearGradient id="steel" x1="0" x2="1"><stop offset="0" stop-color="#3b424e"/><stop offset="0.5" stop-color="#707b8a"/><stop offset="1" stop-color="#2a2f38"/></linearGradient>'''))

# S4 — motel room, two beds, 2:00 a.m.
def room(sister_turned=False):
    return f'''
<rect width="{W}" height="{H}" fill="#0b090f"/>
<rect x="0" y="0" width="{W}" height="620" fill="#15111b"/>
<rect x="760" y="140" width="400" height="330" fill="#2a0c12"/>
<rect x="760" y="140" width="400" height="330" fill="{NEON}" opacity="0.35" filter="url(#blur30)"/>
<g fill="#1d1420">{''.join(f'<rect x="{x}" y="120" width="34" height="380" rx="8"/>' for x in range(740, 900, 40))}{''.join(f'<rect x="{x}" y="120" width="34" height="380" rx="8"/>' for x in range(1030, 1180, 40))}</g>
<rect x="720" y="110" width="480" height="16" fill="#0a070c"/>
<polygon points="900,480 1020,480 1180,620 740,620" fill="{NEON}" opacity="0.10"/>
<rect x="0" y="620" width="{W}" height="460" fill="#120d14"/>
<g transform="translate(560 575) scale(0.74)">
<rect x="-40" y="-170" width="440" height="190" rx="10" fill="#1c1420"/>
<rect x="-60" y="10" width="500" height="160" rx="16" fill="#2a2030"/>
<path d="M-60 40 C40 -30 160 -20 220 10 C300 -10 400 0 440 40 L440 170 L-60 170Z" fill="#3a2c40"/>
<ellipse cx="40" cy="0" rx="70" ry="28" fill="#d8cfe0" opacity="0.5"/>
</g>
<g transform="translate(1074 575) scale(0.74)">
<rect x="-40" y="-170" width="440" height="190" rx="10" fill="#1c1420"/>
<rect x="-60" y="10" width="500" height="160" rx="16" fill="#2a2030"/>
<path d="M-60 40 C40 -40 180 -30 240 10 C320 -10 400 0 440 40 L440 170 L-60 170Z" fill="#3a2c40"/>
<ellipse cx="320" cy="0" rx="70" ry="28" fill="#d8cfe0" opacity="0.5"/>
<path d="M260 -10 C270 -50 330 -60 360 -30 C370 -10 350 10 320 14 Z" fill="#0b070c"/>
</g>
<g transform="translate(960 640)">
<rect x="-56" y="0" width="112" height="140" fill="#1a1219"/>
<rect x="-56" y="-46" width="112" height="50" rx="8" fill="#0a070b"/>
<text x="0" y="-8" text-anchor="middle" font-family="{MONO}" font-size="34" fill="{NEON}">2:00</text>
{glow(0, -22, 70, NEON, 0.4)}
</g>
'''
save("s4", svg(room()))

# S5 — inside of the door: chain, peephole, light and feet beneath
save("s5", svg(f'''
<rect width="{W}" height="{H}" fill="#0a0709"/>
<rect x="560" y="0" width="800" height="900" fill="url(#door5)"/>
<rect x="620" y="60" width="680" height="360" fill="none" stroke="#120b0c" stroke-width="10"/>
<rect x="620" y="470" width="680" height="380" fill="none" stroke="#120b0c" stroke-width="10"/>
<circle cx="960" cy="300" r="22" fill="#2b2026" stroke="#8a7a56" stroke-width="6"/>
<circle cx="960" cy="300" r="9" fill="{LAMP}"/>
{glow(960, 300, 34, LAMP, 0.6)}
<text x="960" y="210" text-anchor="middle" font-family="{SANS}" font-weight="700" font-size="54" fill="#b89a5a">7</text>
<rect x="1230" y="360" width="60" height="40" rx="6" fill="#8a7a56"/>
<path d="M1260 380 C1220 430 1180 450 1120 440" fill="none" stroke="#b9a46e" stroke-width="9" stroke-dasharray="20 8"/>
<rect x="1100" y="420" width="40" height="34" rx="6" fill="#8a7a56"/>
<circle cx="1270" cy="520" r="34" fill="url(#brass5)"/>
<rect x="1240" y="470" width="80" height="20" rx="8" fill="url(#brass5)"/>
<rect x="560" y="900" width="800" height="22" fill="#ffc678"/>
<rect x="560" y="896" width="800" height="30" fill="#ffc678" filter="url(#blur8)"/>
<rect x="780" y="900" width="120" height="22" fill="#050304"/><rect x="960" y="900" width="120" height="22" fill="#050304"/>
<polygon points="560,922 1360,922 1600,1080 320,1080" fill="url(#spill5)"/>
<polygon points="780,922 900,922 940,1080 760,1080" fill="#000" opacity="0.6"/>
<polygon points="960,922 1080,922 1130,1080 960,1080" fill="#000" opacity="0.6"/>
<rect x="0" y="0" width="560" height="1080" fill="#080507"/><rect x="1360" y="0" width="560" height="1080" fill="#080507"/>
''', '''<linearGradient id="door5" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1c1216"/><stop offset="1" stop-color="#33222a"/></linearGradient>
<linearGradient id="brass5" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e3c37a"/><stop offset="1" stop-color="#5e4318"/></linearGradient>
<linearGradient id="spill5" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc678" stop-opacity="0.4"/><stop offset="1" stop-color="#ffc678" stop-opacity="0"/></linearGradient>'''))

# S6 — the other bed: "her", curled up, facing the wall
def other_bed(face=False):
    head = ('<path d="M760 430 C740 340 860 300 940 330 C990 350 1000 420 960 460 Z" fill="#0b070c"/>'
            '<path d="M760 430 C720 470 700 520 690 560" fill="none" stroke="#0b070c" stroke-width="26" stroke-linecap="round"/>'
            '<path d="M800 420 C780 470 770 520 740 580" fill="none" stroke="#0b070c" stroke-width="18" stroke-linecap="round"/>')
    if face:
        head = ('<ellipse cx="880" cy="400" rx="96" ry="110" fill="#c9bfc6"/>'
                '<ellipse cx="880" cy="400" rx="96" ry="110" fill="#5a2a3a" opacity="0.35"/>'
                '<path d="M780 360 C790 270 980 260 990 370 C970 320 900 300 840 320 C810 330 790 350 780 360 Z" fill="#0b070c"/>'
                '<path d="M786 360 C760 440 740 520 720 600" fill="none" stroke="#0b070c" stroke-width="28" stroke-linecap="round"/>'
                '<path d="M984 370 C1000 450 1010 520 1030 600" fill="none" stroke="#0b070c" stroke-width="24" stroke-linecap="round"/>'
                '<ellipse cx="845" cy="392" rx="18" ry="10" fill="#0a0507"/><ellipse cx="920" cy="392" rx="18" ry="10" fill="#0a0507"/>'
                '<circle cx="849" cy="391" r="4" fill="#ff5a5a"/><circle cx="924" cy="391" r="4" fill="#ff5a5a"/>'
                '<path d="M828 450 C860 482 910 482 940 450" fill="none" stroke="#2a0e14" stroke-width="7" stroke-linecap="round"/>'
                '<path d="M832 452 C862 474 906 474 936 452" fill="#efe7e2"/>')
    return f'''
<rect width="{W}" height="{H}" fill="#0a070c"/>
<rect x="0" y="0" width="{W}" height="560" fill="#1a131d"/>
<g stroke="#120c14" stroke-width="4" opacity="0.8">{''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="560"/>' for x in range(30, W, 90))}</g>
<rect x="1500" y="90" width="260" height="190" fill="#120c14" stroke="#2a1d24" stroke-width="10"/>
<path d="M1540 240 L1600 170 L1650 210 L1700 150 L1740 240 Z" fill="#241820"/>
<rect x="300" y="300" width="1320" height="260" rx="12" fill="#1f1622"/>
<ellipse cx="880" cy="470" rx="260" ry="80" fill="#cfc4d6" opacity="0.55"/>
<path d="M300 560 L1620 560 L1700 1080 L220 1080Z" fill="#2c2032"/>
<path d="M600 520 C700 450 860 470 980 520 C1100 470 1260 480 1380 530 C1480 560 1560 600 1600 680 L1660 1080 L260 1080 L340 680 C380 600 480 540 600 520Z" fill="#45334c"/>
<path d="M600 520 C700 450 860 470 980 520 C1100 470 1260 480 1380 530" fill="none" stroke="#5e4866" stroke-width="10"/>
{head}
<rect x="0" y="0" width="{W}" height="{H}" fill="{NEON}" opacity="0.10"/>
{glow(1900, 200, 360, NEON, 0.25)}
'''
save("s6", svg(other_bed()))

# S7 — morning: a full bucket of ice outside door 7
save("s7", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sk7)"/>
<rect x="0" y="0" width="{W}" height="760" fill="#c8a98a"/>
<rect x="0" y="0" width="{W}" height="760" fill="url(#sun7)"/>
<rect x="640" y="140" width="420" height="620" fill="#6f4e3a"/>
<rect x="660" y="160" width="380" height="600" fill="#7d5a43"/>
<text x="850" y="290" text-anchor="middle" font-family="{SANS}" font-weight="700" font-size="90" fill="#e2c48a">7</text>
<circle cx="1000" cy="480" r="16" fill="#e2c48a"/>
<rect x="1180" y="220" width="420" height="300" fill="#2e2a2e"/>
<rect x="1200" y="240" width="380" height="260" fill="#3c3640"/>
<rect x="1200" y="240" width="380" height="260" fill="#fff" opacity="0.06"/>
<rect x="0" y="760" width="{W}" height="320" fill="#9e8670"/>
<g stroke="#8a725c" stroke-width="4">{''.join(f'<line x1="{x}" y1="760" x2="{x - 200}" y2="1080"/>' for x in range(100, 2200, 260))}</g>
<polygon points="0,0 1920,0 1920,60 0,140" fill="#2a1f1c"/>
{bucket(860, 880, 1.35, full=True, melt=True)}
<path d="M760 900 C820 940 940 950 1060 920 C1120 960 1200 990 1260 1000" fill="none" stroke="#5f7b8f" stroke-width="22" opacity="0.5" stroke-linecap="round"/>
<path d="M760 900 C820 940 940 950 1060 920 C1120 960 1200 990 1260 1000" fill="none" stroke="#cfe7f3" stroke-width="6" opacity="0.5" stroke-linecap="round"/>
<ellipse cx="900" cy="440" rx="900" ry="500" fill="#ffd9a0" opacity="0.12" filter="url(#blur60)"/>
''', BK + sky("sk7", "#f0c890", "#d8a070", "#a07a60") + '''<linearGradient id="sun7" x1="1" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffe0a8" stop-opacity="0.5"/><stop offset="1" stop-color="#000" stop-opacity="0.2"/></linearGradient>'''))

# S8 — the girl in her bed rolls over and smiles
save("s8", svg(other_bed(face=True)))
print("ok")
