"""Draws each scene as an SVG (1920x1080 viewBox) and rasterizes at 1.5x for smooth slow zooms."""
import subprocess, random

W, H = 1920, 1080
random.seed(7)

def svg(body, defs=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>{defs}
<radialGradient id="vig" cx="960" cy="540" r="1100" gradientUnits="userSpaceOnUse">
<stop offset="0.5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.85"/></radialGradient>
<filter id="blur8"><feGaussianBlur stdDeviation="8"/></filter>
<filter id="blur30"><feGaussianBlur stdDeviation="30"/></filter>
<filter id="blur60"><feGaussianBlur stdDeviation="60"/></filter>
</defs>
{body}
<rect width="{W}" height="{H}" fill="url(#vig)"/>
</svg>'''

def stars(n, ymax, op=0.7):
    return "".join(f'<circle cx="{random.randint(0,W)}" cy="{random.randint(0,ymax)}" r="{random.choice([1,1.3,1.8,2.2])}" fill="#dfe3f5" opacity="{random.uniform(0.3,op):.2f}"/>' for _ in range(n))

def grass(y0, n, color, h=(14, 34)):
    out = []
    for _ in range(n):
        x = random.randint(0, W); hh = random.randint(*h); lean = random.randint(-8, 8)
        out.append(f'<path d="M{x} {y0} q{lean/2} {-hh/2} {lean} {-hh}" stroke="{color}" stroke-width="3" fill="none" stroke-linecap="round"/>')
    return "".join(out)

scenes = {}

# S0 — title card
scenes["s0"] = svg(f'''
<rect width="{W}" height="{H}" fill="#060509"/>
<ellipse cx="960" cy="540" rx="700" ry="260" fill="#3a0d12" opacity="0.35" filter="url(#blur60)"/>
<text x="960" y="520" text-anchor="middle" font-family="GFS Baskerville, DejaVu Serif, serif" font-size="128" fill="#e9e2d0" letter-spacing="6">The Farmhouse Rule</text>
<line x1="760" y1="580" x2="1160" y2="580" stroke="#8c1c1c" stroke-width="3"/>
<text x="960" y="650" text-anchor="middle" font-family="Inter, DejaVu Sans, sans-serif" font-size="34" fill="#a99f8c" letter-spacing="14">A SCARY STORY</text>
''')

# S1 — farmhouse at night
fence = "".join(f'<rect x="{x}" y="{812 - (x%3)}" width="10" height="70" fill="#0a0912"/>' for x in range(60, 1900, 90))
scenes["s1"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(160, 600)}
<circle cx="1450" cy="250" r="230" fill="#f3ead1" opacity="0.12" filter="url(#blur60)"/>
<circle cx="1450" cy="250" r="110" fill="#f1e9d3"/>
<g fill="#000" opacity="0.07"><circle cx="1420" cy="225" r="26"/><circle cx="1480" cy="280" r="18"/><circle cx="1475" cy="210" r="10"/></g>
<path d="M0 760 C300 700 600 720 900 740 C1200 760 1500 700 1920 730 L1920 1080 L0 1080Z" fill="#141022"/>
<g fill="#08070d">
<polygon points="700,790 700,520 960,380 1220,520 1220,790"/>
<polygon points="1220,790 1220,600 1460,600 1460,790"/>
<polygon points="1200,612 1340,520 1480,612"/>
<rect x="1080" y="380" width="40" height="100"/>
<polygon points="660,800 660,640 1260,640 1260,800"/>
<polygon points="640,650 960,590 1280,650"/>
<rect x="320" y="440" width="14" height="360"/>
<polygon points="327,440 230,400 237,390 327,430"/>
<polygon points="327,440 400,350 410,358 330,445"/>
<polygon points="327,440 420,490 414,500 327,452"/>
<polygon points="327,440 260,520 250,512 324,436"/>
</g>
<rect x="905" y="470" width="58" height="76" fill="#ffb54a"/>
<rect x="905" y="470" width="58" height="76" fill="#ffb54a" filter="url(#blur30)" opacity="0.8"/>
<line x1="934" y1="470" x2="934" y2="546" stroke="#08070d" stroke-width="5"/>
<line x1="905" y1="508" x2="963" y2="508" stroke="#08070d" stroke-width="5"/>
<g fill="#0c0b12" opacity="0.9">{''.join(f'<rect x="{x}" y="690" width="70" height="90" />' for x in (740, 1150))}</g>
<path d="M0 840 C400 800 800 830 1200 820 C1500 812 1700 830 1920 820 L1920 1080 L0 1080Z" fill="#1a1630"/>
{fence}
<rect x="0" y="830" width="{W}" height="8" fill="#07060b"/>
<rect x="0" y="860" width="{W}" height="8" fill="#07060b"/>
{grass(1000, 260, "#0d0b18")}{grass(930, 200, "#110e1f")}<path d="M0 960 C500 930 1300 950 1920 935 L1920 1080 L0 1080Z" fill="#0f0c1c"/>{grass(1080, 300, "#07060d", (20,50))}
<ellipse cx="960" cy="800" rx="1300" ry="70" fill="#8a87a8" opacity="0.10" filter="url(#blur30)"/>
''', '''<linearGradient id="sky1" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#05060f"/><stop offset="0.55" stop-color="#1b1638"/><stop offset="1" stop-color="#3b2343"/></linearGradient>''')

# S2 — grave
scenes["s2"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky2)"/>
{stars(60, 400, 0.4)}
<path d="M0 700 C400 650 900 640 1300 680 C1600 710 1800 690 1920 700 L1920 1080 L0 1080Z" fill="#1d2230"/>
<g fill="#151925">
<rect x="250" y="610" width="40" height="70" rx="18"/><rect x="420" y="630" width="32" height="56" rx="14"/>
<rect x="1500" y="620" width="46" height="70" rx="20"/><path d="M1680 690 v-80 h-14 v-24 h14 v-14 h16 v14 h14 v24 h-14 v80z"/>
</g>
<g stroke="#0b0d14" stroke-linecap="round" fill="none">
<path d="M1300 700 C1310 560 1290 470 1320 360" stroke-width="30"/>
<path d="M1318 420 C1370 380 1400 350 1460 330" stroke-width="12"/>
<path d="M1310 480 C1250 440 1220 420 1180 380" stroke-width="12"/>
<path d="M1320 360 C1330 300 1310 270 1340 220" stroke-width="9"/>
<path d="M1460 330 C1490 320 1500 300 1530 290" stroke-width="5"/>
<path d="M1180 380 C1170 350 1150 340 1130 320" stroke-width="5"/>
</g>
<path d="M0 860 C500 820 1200 830 1920 850 L1920 1080 L0 1080Z" fill="#11141d"/>
<path d="M760 560 C760 470 830 430 900 430 C970 430 1040 470 1040 560 L1040 830 L760 830Z" fill="#3a3f4f"/>
<path d="M760 560 C760 470 830 430 900 430 C970 430 1040 470 1040 560 L1040 830 L1020 830 L1020 565 C1020 485 965 450 900 450 C835 450 780 485 780 565 L780 830 L760 830Z" fill="#4d5366"/>
<text x="900" y="560" text-anchor="middle" font-family="GFS Baskerville, DejaVu Serif, serif" font-size="34" fill="#22252f" letter-spacing="3">BELOVED</text>
<text x="900" y="605" text-anchor="middle" font-family="GFS Baskerville, DejaVu Serif, serif" font-size="27" fill="#22252f" letter-spacing="1">GRANDMOTHER</text>
<line x1="840" y1="640" x2="960" y2="640" stroke="#22252f" stroke-width="2"/>
<path d="M700 900 C760 850 1040 850 1100 900 L1100 930 L700 930Z" fill="#2a1d18"/>
<g>
<line x1="860" y1="830" x2="850" y2="880" stroke="#3b4a2c" stroke-width="4"/>
<line x1="880" y1="830" x2="885" y2="885" stroke="#3b4a2c" stroke-width="4"/>
<circle cx="855" cy="825" r="14" fill="#6b2230"/><circle cx="882" cy="822" r="12" fill="#7a2a36"/><circle cx="905" cy="835" r="11" fill="#5c1d2a"/>
</g>
{grass(940, 260, "#1a1f2a", (10, 26))}
<ellipse cx="960" cy="860" rx="1200" ry="110" fill="#aab3c8" opacity="0.13" filter="url(#blur60)"/>
''', '''<linearGradient id="sky2" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#0a0d16"/><stop offset="1" stop-color="#3a4256"/></linearGradient>''')

# S3 — hallway to the front door
boards = "".join(f'<line x1="960" y1="660" x2="{x}" y2="1080" stroke="#1a110c" stroke-width="3"/>' for x in range(-600, 2600, 160))
scenes["s3"] = svg(f'''
<rect width="{W}" height="{H}" fill="#120c0c"/>
<polygon points="0,0 760,300 760,660 0,1080" fill="url(#wallL)"/>
<polygon points="1920,0 1160,300 1160,660 1920,1080" fill="url(#wallR)"/>
<polygon points="0,0 1920,0 1160,300 760,300" fill="#0b0708"/>
<polygon points="0,1080 760,660 1160,660 1920,1080" fill="#2a1a12"/>
<g clip-path="url(#floor)">{boards}</g>
<g stroke="#2a1d1d" stroke-width="2" opacity="0.6">{''.join(f'<line x1="{x}" y1="{300 - (760 - x) * 300 / 760:.0f}" x2="{x}" y2="{660 + (760 - x) * 420 / 760:.0f}"/>' for x in range(80, 760, 70))}</g>
<rect x="760" y="300" width="400" height="360" fill="#1e1414"/>
<rect x="830" y="330" width="260" height="330" fill="#2c1b14"/>
<rect x="850" y="350" width="220" height="140" fill="#0d0d18"/>
<rect x="850" y="350" width="220" height="140" fill="#9fb4e8" opacity="0.25"/>
<line x1="960" y1="350" x2="960" y2="490" stroke="#2c1b14" stroke-width="8"/>
<rect x="860" y="520" width="90" height="120" fill="none" stroke="#1d120d" stroke-width="5"/>
<rect x="970" y="520" width="90" height="120" fill="none" stroke="#1d120d" stroke-width="5"/>
<circle cx="1060" cy="510" r="8" fill="#a7853f"/>
<polygon points="850,660 1070,660 1290,1080 630,1080" fill="#9fb4e8" opacity="0.06"/>
<g fill="#0c0808">
<rect x="380" y="380" width="12" height="440"/><rect x="330" y="810" width="110" height="14"/>
<path d="M386 400 l-60 40 m60 -40 l60 40" stroke="#0c0808" stroke-width="8"/>
<ellipse cx="420" cy="520" rx="46" ry="120"/>
</g>
<g transform="translate(1560 300)">
<rect x="-60" y="0" width="120" height="420" rx="10" fill="#1a100d"/>
<circle cx="0" cy="90" r="46" fill="#d8ccb0"/>
<circle cx="0" cy="90" r="46" fill="none" stroke="#7a5a2a" stroke-width="6"/>
<line x1="0" y1="90" x2="0" y2="58" stroke="#1a100d" stroke-width="5"/>
<line x1="0" y1="90" x2="24" y2="98" stroke="#1a100d" stroke-width="4"/>
<line x1="0" y1="150" x2="0" y2="300" stroke="#7a5a2a" stroke-width="3"/>
<circle cx="0" cy="310" r="18" fill="#a7853f"/>
</g>
<circle cx="1300" cy="250" r="140" fill="#ffae4a" opacity="0.10" filter="url(#blur60)"/>
''', '''<linearGradient id="wallL" x1="0" x2="1"><stop offset="0" stop-color="#2a1715"/><stop offset="1" stop-color="#160d0d"/></linearGradient>
<linearGradient id="wallR" x1="1" x2="0"><stop offset="0" stop-color="#2a1715"/><stop offset="1" stop-color="#160d0d"/></linearGradient>
<clipPath id="floor"><polygon points="0,1080 760,660 1160,660 1920,1080"/></clipPath>''')

def under_door(feet, tint, extra="", spots=()):
    shadows = "".join(f'<polygon points="{a},806 {b},806 {b + (b - 960) * 0.5:.0f},1080 {a + (a - 960) * 0.5:.0f},1080" fill="#000" opacity="0.75"/>' for a, b in spots)
    door_panels = '<rect x="260" y="60" width="600" height="560" fill="none" stroke="#120b09" stroke-width="10"/><rect x="1060" y="60" width="600" height="560" fill="none" stroke="#120b09" stroke-width="10"/>'
    return svg(f'''
<rect width="{W}" height="{H}" fill="#0b0707"/>
<rect x="160" y="0" width="1600" height="770" fill="url(#door)"/>
{door_panels}
<rect x="160" y="770" width="1600" height="36" fill="{tint}"/>
<rect x="160" y="770" width="1600" height="36" fill="{tint}" filter="url(#blur8)"/>
{feet}
<polygon points="160,806 1760,806 2100,1080 -180,1080" fill="url(#spillU)"/>
{shadows}
<rect x="0" y="806" width="{W}" height="286" fill="#120a08" opacity="0.55"/>
<g stroke="#000" stroke-width="3" opacity="0.6">{''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in (860, 950, 1050))}</g>
<rect x="0" y="0" width="160" height="806" fill="#070404"/><rect x="1760" y="0" width="160" height="806" fill="#070404"/>
{extra}
''', f'''<linearGradient id="door" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#160e0b"/><stop offset="1" stop-color="#2a1a13"/></linearGradient>
<linearGradient id="spillU" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{tint}" stop-opacity="0.45"/><stop offset="1" stop-color="{tint}" stop-opacity="0"/></linearGradient>''')

def foot_pair(cx, w=110):
    return f'<rect x="{cx - w - 15}" y="770" width="{w}" height="36" fill="#050303"/><rect x="{cx + 15}" y="770" width="{w}" height="36" fill="#050303"/>'

# S4 — light under the door, one pair of feet
def spots(cx, w=110): return [(cx - w - 15, cx - 15), (cx + 15, cx + 15 + w)]
scenes["s4"] = under_door(foot_pair(960), "#f2b25a", spots=spots(960))

# S5 — hand reaching for the deadbolt
scenes["s5"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#door5)"/>
<g stroke="#120b09" stroke-width="3" opacity="0.6">{''.join(f'<path d="M{x} 0 C{x + 20} 300 {x - 20} 700 {x + 10} 1080" fill="none"/>' for x in range(80, 1920, 170))}</g>
<rect x="1090" y="250" width="70" height="560" fill="#140c0a"/>
<rect x="1180" y="330" width="210" height="210" rx="24" fill="url(#brass)"/>
<circle cx="1285" cy="435" r="70" fill="#7a5c25"/>
<rect x="1270" y="370" width="30" height="130" rx="12" fill="url(#brass)" transform="rotate(-20 1285 435)"/>
<rect x="1200" y="640" width="170" height="60" rx="10" fill="url(#brass)"/>
<path d="M1230 670 C1180 720 1180 780 1240 790 C1300 800 1330 760 1320 700" fill="none" stroke="#b08c3e" stroke-width="10" stroke-dasharray="26 10"/>
<g fill="#000" opacity="0.6" filter="url(#blur8)" transform="translate(-40 40)">
<ellipse cx="900" cy="560" rx="240" ry="150"/>
<rect x="1000" y="430" width="230" height="44" rx="22"/><rect x="1010" y="486" width="250" height="44" rx="22"/>
<rect x="1000" y="542" width="235" height="44" rx="22"/><rect x="980" y="598" width="200" height="40" rx="20"/>
<rect x="880" y="380" width="160" height="40" rx="20" transform="rotate(-25 960 400)"/>
<rect x="400" y="500" width="520" height="160" rx="70"/>
</g>
<circle cx="1285" cy="435" r="300" fill="#ffd28a" opacity="0.08" filter="url(#blur60)"/>
''', '''<linearGradient id="door5" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1a100d"/><stop offset="1" stop-color="#3a2419"/></linearGradient>
<linearGradient id="brass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e3c37a"/><stop offset="0.5" stop-color="#a7853f"/><stop offset="1" stop-color="#5e4318"/></linearGradient>''')

# S6 — hospital monitor
ecg = "M0 260 " + " ".join(f"l60 0 l10 -10 l10 10 l14 0 l8 30 l10 -150 l10 160 l8 -40 l20 0 l16 -24 l16 24 l40 0" for _ in range(4))
scenes["s6"] = svg(f'''
<rect width="{W}" height="{H}" fill="#06090b"/>
<rect x="0" y="0" width="{W}" height="{H}" fill="#0f2a2a" opacity="0.35"/>
<g fill="#0b0f12">
<rect x="1500" y="80" width="12" height="900"/><rect x="1430" y="80" width="150" height="10"/>
<path d="M1440 90 h50 v130 c0 30 -50 30 -50 0z" fill="#1c2a2e"/>
<rect x="0" y="760" width="{W}" height="40" rx="10" fill="#141b1f"/>
<rect x="0" y="800" width="{W}" height="280" fill="#0c1215"/>
{''.join(f'<rect x="{x}" y="700" width="14" height="80" fill="#1b2328"/>' for x in range(100, 1300, 120))}
<rect x="80" y="690" width="1260" height="14" rx="7" fill="#1b2328"/>
</g>
<g transform="translate(560 160)">
<rect x="-30" y="-30" width="860" height="560" rx="30" fill="#0e1417"/>
<rect x="0" y="0" width="800" height="500" rx="12" fill="#03100c"/>
<g opacity="0.25" stroke="#1d5c45" stroke-width="1">{''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="500"/>' for x in range(0, 800, 50))}{''.join(f'<line x1="0" y1="{y}" x2="800" y2="{y}"/>' for y in range(0, 500, 50))}</g>
<path d="{ecg}" fill="none" stroke="#3dff9a" stroke-width="5" stroke-linejoin="round"/>
<path d="{ecg}" fill="none" stroke="#3dff9a" stroke-width="14" opacity="0.35" filter="url(#blur8)"/>
<text x="770" y="80" text-anchor="end" font-family="DejaVu Sans Mono, monospace" font-size="70" fill="#3dff9a">48</text>
<text x="770" y="115" text-anchor="end" font-family="DejaVu Sans Mono, monospace" font-size="24" fill="#3dff9a" opacity="0.7">BPM</text>
<text x="30" y="470" font-family="DejaVu Sans Mono, monospace" font-size="26" fill="#ffb84a">SpO2 86%</text>
</g>
<rect x="530" y="130" width="860" height="560" fill="#3dff9a" opacity="0.06" filter="url(#blur60)"/>
''')

# S6b — flatline variant (used for the last seconds of the scene)
flat = scenes["s6"].replace(f'd="{ecg}"', 'd="M0 260 l340 0 l10 -10 l10 10 l14 0 l8 30 l10 -150 l10 160 l8 -40 l390 0"').replace(">48<", ">0<").replace('fill="#3dff9a">0<', 'fill="#ff4d4d">0<')
scenes["s6b"] = flat

# S7 — many feet under the door, red light
feet_many = foot_pair(520, 95) + foot_pair(960, 110) + foot_pair(1400, 95) + foot_pair(740, 70) + foot_pair(1180, 70)
sp = spots(520, 95) + spots(960, 110) + spots(1400, 95) + spots(740, 70) + spots(1180, 70)
scenes["s7"] = under_door(feet_many, "#c2362b", spots=sp)

# S8 — end card
scenes["s8"] = svg(f'''
<rect width="{W}" height="{H}" fill="#050305"/>
<text x="960" y="490" text-anchor="middle" font-family="GFS Baskerville, DejaVu Serif, serif" font-size="96" fill="#d8cfbd" letter-spacing="5">Never answer the door</text>
<text x="960" y="640" text-anchor="middle" font-family="GFS Baskerville, DejaVu Serif, serif" font-size="96" fill="#b3261e" letter-spacing="5">after midnight.</text>
''')

for name, s in scenes.items():
    open(f"{name}.svg", "w").write(s)
    subprocess.run(["rsvg-convert", "-w", str(W * 3 // 2), "-h", str(H * 3 // 2), f"{name}.svg", "-o", f"{name}.png"], check=True)
print("drew", ", ".join(scenes))
