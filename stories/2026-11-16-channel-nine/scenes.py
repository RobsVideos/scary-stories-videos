"""Scenes for 'Channel Nine' (1920x1080 SVGs, cropped to an 864-wide strip around each scene's cx)."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

HAND = "DejaVu Serif, serif"


def walkie(x, y, s=1.0, body="#2b2f36", led="#ff3b2f", screen="#ffb54a", ch="2", glow_on=True, antenna=True, rot=0):
    """A chunky 90s walkie-talkie, top-left at (x, y), 160x330 units at s=1."""
    g = [f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">']
    if antenna:
        g.append(f'<rect x="28" y="-150" width="22" height="170" rx="8" fill="#15171c"/>'
                 f'<circle cx="39" cy="-152" r="13" fill="#15171c"/>')
    g.append(f'<rect x="100" y="-30" width="26" height="40" rx="6" fill="#1b1e24"/>'  # knob
             f'<rect x="0" y="0" width="160" height="330" rx="26" fill="{body}"/>'
             f'<rect x="0" y="0" width="160" height="330" rx="26" fill="none" stroke="#0d0f13" stroke-width="6"/>'
             f'<rect x="10" y="10" width="40" height="310" rx="16" fill="#ffffff" opacity="0.05"/>'
             f'<circle cx="128" cy="26" r="9" fill="{led}"/>')
    if glow_on:
        g.append(f'<circle cx="128" cy="26" r="26" fill="{led}" opacity="0.55" filter="url(#blur8)"/>')
    # speaker grille
    for i in range(6):
        g.append(f'<rect x="28" y="{52 + i * 18}" width="104" height="8" rx="4" fill="#0e1014"/>')
    # channel screen
    g.append(f'<rect x="30" y="172" width="100" height="70" rx="8" fill="#0a0806"/>'
             f'<rect x="36" y="178" width="88" height="58" rx="5" fill="{screen}" opacity="0.92"/>'
             f'<text x="80" y="226" text-anchor="middle" font-family="{MONO}" font-size="50" font-weight="bold" fill="#2a1406">{ch}</text>')
    if glow_on:
        g.append(f'<rect x="20" y="166" width="120" height="82" fill="{screen}" opacity="0.45" filter="url(#blur30)"/>')
    # push-to-talk + buttons
    g.append(f'<rect x="-14" y="120" width="16" height="90" rx="6" fill="#16181d"/>'
             f'<circle cx="55" cy="280" r="14" fill="#1a1c22"/><circle cx="105" cy="280" r="14" fill="#1a1c22"/>')
    g.append('</g>')
    return "".join(g)


def rain(n, op=0.25, color="#9fb0d8", y0=0, y1=1080, x0=0, x1=1920):
    return "".join(f'<line x1="{(x := rnd.randint(x0, x1))}" y1="{(y := rnd.randint(y0, y1))}" x2="{x - 14}" y2="{y + 46}" '
                   f'stroke="{color}" stroke-width="2" opacity="{rnd.uniform(0.1, op):.2f}"/>' for _ in range(n))


def kid_bed_room(defs_id, flash=False, body_extra=""):
    """A kid's bedroom at night with a stormy window; used for s4/s6."""
    win = "#cfdcff" if flash else "#1c2747"
    return svg(f'''
<rect width="{W}" height="{H}" fill="#0b0d16"/>
<rect x="0" y="0" width="{W}" height="760" fill="url(#{defs_id}w)"/>
<g opacity="0.25" stroke="#1a1f30" stroke-width="2">{''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="760"/>' for x in range(40, 1920, 80))}</g>
<rect x="0" y="760" width="{W}" height="320" fill="#0d0b12"/>
<g stroke="#07060a" stroke-width="3">{''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in (800, 860, 940, 1040))}</g>
<!-- window -->
<rect x="700" y="130" width="520" height="440" fill="#090a10"/>
<rect x="720" y="150" width="480" height="400" fill="{win}"/>
{rain(90, 0.5, "#c6d2f0", 150, 550, 720, 1200)}
{'<path d="M1010 150 L975 260 L1010 270 L960 400 L995 405 L940 550" stroke="#ffffff" stroke-width="7" fill="none"/>' if flash else ''}
<g fill="#06070c"><path d="M720 550 L720 470 C780 430 820 460 860 420 C900 390 960 430 1010 400 C1060 380 1120 420 1200 390 L1200 550Z"/>
{dead_tree(800, 560, 330, "#06070c", 0.7)}</g>
<rect x="955" y="150" width="12" height="400" fill="#090a10"/><rect x="720" y="344" width="480" height="12" fill="#090a10"/>
<rect x="680" y="560" width="560" height="26" fill="#14121a"/>
{'<rect x="0" y="0" width="1920" height="1080" fill="#dfe6ff" opacity="0.10"/>' if flash else ''}
<polygon points="720,560 1200,560 1500,1080 420,1080" fill="{win}" opacity="{0.16 if flash else 0.07}"/>
<!-- curtains -->
<path d="M640 110 C660 300 620 480 670 610 L720 610 L720 110Z" fill="#2a1420"/>
<path d="M1280 110 C1260 300 1300 480 1250 610 L1200 610 L1200 110Z" fill="#2a1420"/>
<rect x="620" y="100" width="680" height="14" rx="7" fill="#151018"/>
<!-- bed -->
<rect x="250" y="640" width="1420" height="60" rx="16" fill="#1b1d2c"/>
<path d="M260 700 C500 620 1300 640 1660 700 L1660 900 L260 900Z" fill="#2a2f4c"/>
<path d="M260 700 C500 620 1300 640 1660 700" stroke="#3a4168" stroke-width="8" fill="none"/>
<rect x="200" y="540" width="60" height="420" rx="10" fill="#120f18"/>
<rect x="1660" y="540" width="60" height="420" rx="10" fill="#120f18"/>
<ellipse cx="420" cy="680" rx="140" ry="52" fill="#454b70"/>
{body_extra}
''', sky(f"{defs_id}w", "#141829", "#1a1e30", "#20243a"))


scenes = {}

# S1 — yard sale table at dusk, house behind, two walkie-talkies on the table
items = (
    '<rect x="420" y="660" width="120" height="90" fill="#3a2a22"/>'  # box
    '<rect x="1290" y="610" width="90" height="140" rx="6" fill="#2a2433"/>'  # lamp base
    '<path d="M1270 610 L1400 610 L1370 540 L1300 540Z" fill="#5a4636"/>'
    '<circle cx="1160" cy="720" r="34" fill="#4a3a40"/>'
)
scenes["s1"] = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sk1)"/>
{stars(80, 300, 0.5)}
<ellipse cx="960" cy="560" rx="900" ry="160" fill="#c56a3a" opacity="0.25" filter="url(#blur60)"/>
<path d="M0 560 C400 530 1400 540 1920 550 L1920 1080 L0 1080Z" fill="#1a1622"/>
<g fill="#0a0910">
<polygon points="560,560 560,330 860,180 1160,330 1160,560"/>
<rect x="1020" y="200" width="40" height="90"/>
<polygon points="500,350 860,150 1220,350 1200,360 860,175 520,360"/>
</g>
{lit_window(640, 380, 90, 110)}
<rect x="900" y="390" width="80" height="100" fill="#121018"/>
{dead_tree(1500, 600, 380, "#08070d")}
{dead_tree(300, 600, 300, "#08070d", 0.8)}
<path d="M0 620 C600 600 1300 610 1920 620 L1920 1080 L0 1080Z" fill="#15121c"/>
{grass(640, 200, "#0e0c15")}
<!-- table -->
<rect x="380" y="740" width="1160" height="26" fill="#3b2c22"/>
<rect x="380" y="766" width="1160" height="20" fill="#241a14"/>
<rect x="420" y="786" width="18" height="190" fill="#1a130e"/><rect x="1480" y="786" width="18" height="190" fill="#1a130e"/>
{items}
<rect x="600" y="690" width="70" height="52" rx="4" fill="#efe6cf"/>
<text x="635" y="726" text-anchor="middle" font-family="{HAND}" font-size="26" fill="#7a1c1c">25¢</text>
{walkie(800, 470, 0.8, ch="9", led="#ff3b2f", screen="#3a2a1a", glow_on=False)}
{walkie(960, 490, 0.75, ch="9", led="#5a1a16", screen="#3a2a1a", glow_on=False, rot=8)}
<circle cx="900" cy="630" r="260" fill="#ffb54a" opacity="0.06" filter="url(#blur60)"/>
{grass(1080, 260, "#08070c", (20, 50))}
{fog(900, "#c9a98a", 0.08)}
''', sky("sk1", "#0c0c1c", "#3a2440", "#8a4a3a"))

# S2 — close-up of the handwritten note inside the open battery door
lines_note = [("NEVER use", "#1d1a3a"), ("channel 9", "#8c1414"), ("after dark.", "#1d1a3a")]
note_txt = "".join(f'<text x="960" y="{470 + i * 82}" text-anchor="middle" font-family="{HAND}" font-style="italic" font-size="62" fill="{c}" transform="rotate(-3 960 540)">{t}</text>' for i, (t, c) in enumerate(lines_note))
scenes["s2"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0c0a0e"/>
<rect x="560" y="80" width="800" height="1000" rx="70" fill="#2b2f36"/>
<rect x="560" y="80" width="800" height="1000" rx="70" fill="none" stroke="#0d0f13" stroke-width="16"/>
<rect x="640" y="200" width="640" height="780" rx="24" fill="#16181d"/>
<g fill="#22252c">{''.join(f'<rect x="{x}" y="230" width="130" height="300" rx="20"/>' for x in (690, 860, 1030))}</g>
<g fill="#a9a08a">{''.join(f'<rect x="{x + 50}" y="214" width="30" height="20"/>' for x in (690, 860, 1030))}</g>
<g transform="rotate(-3 960 540)">
<rect x="650" y="330" width="620" height="380" fill="#e8dfc4"/>
<g stroke="#9fb0d0" stroke-width="2" opacity="0.6">{''.join(f'<line x1="650" y1="{y}" x2="1270" y2="{y}"/>' for y in range(380, 700, 41))}</g>
<line x1="700" y1="330" x2="700" y2="710" stroke="#d9867f" stroke-width="2"/>
<rect x="840" y="310" width="240" height="44" fill="#d6cfa8" opacity="0.8"/>
</g>
{note_txt}
<text x="960" y="690" text-anchor="middle" font-family="{HAND}" font-style="italic" font-size="34" fill="#1d1a3a" transform="rotate(-3 960 540)">don't tell them where you are</text>
<path d="M1000 980 C1100 960 1300 1000 1400 1080 L560 1080 C640 1020 800 990 1000 980Z" fill="#0a0809" opacity="0.8"/>
<circle cx="1300" cy="200" r="300" fill="#ffd9a0" opacity="0.10" filter="url(#blur60)"/>
''')

# S3 — dark hallway, two bedroom doors facing each other, walkie glow under each
boards = "".join(f'<line x1="960" y1="640" x2="{x}" y2="1080" stroke="#140f10" stroke-width="3"/>' for x in range(-600, 2600, 170))
scenes["s3"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0b0a10"/>
<polygon points="0,0 780,320 780,640 0,1080" fill="url(#wl3)"/>
<polygon points="1920,0 1140,320 1140,640 1920,1080" fill="url(#wr3)"/>
<polygon points="0,0 1920,0 1140,320 780,320" fill="#07060a"/>
<polygon points="0,1080 780,640 1140,640 1920,1080" fill="#1a1416"/>
<g clip-path="url(#fl3)">{boards}</g>
<rect x="780" y="320" width="360" height="320" fill="#100e15"/>
<rect x="880" y="380" width="160" height="260" fill="#16131c"/>
<!-- left door, ajar with warm glow -->
<polygon points="540,240 760,328 760,700 540,800" fill="#17121a"/>
<polygon points="556,258 746,334 746,694 556,786" fill="#ffb54a" opacity="0.6"/>
<polygon points="556,258 746,334 746,694 556,786" fill="#ffb54a" opacity="0.35" filter="url(#blur30)"/>
<polygon points="556,258 630,290 630,760 556,786" fill="#1d1620"/>
<!-- right door, ajar with red glow -->
<polygon points="1380,240 1160,328 1160,700 1380,800" fill="#17121a"/>
<polygon points="1364,258 1174,334 1174,694 1364,786" fill="#ff5a3a" opacity="0.45"/>
<polygon points="1364,258 1174,334 1174,694 1364,786" fill="#ff5a3a" opacity="0.3" filter="url(#blur30)"/>
<polygon points="1364,258 1290,290 1290,760 1364,786" fill="#1d1620"/>
<polygon points="746,694 556,786 700,1080 900,1080" fill="#ffb54a" opacity="0.12"/>
<polygon points="1174,694 1364,786 1220,1080 1020,1080" fill="#ff5a3a" opacity="0.10"/>
<!-- glowing radio wave arcs crossing the hall -->
<g fill="none" stroke="#ffcf7a" stroke-width="5" opacity="0.6">
<path d="M800 520 q40 -40 0 -80"/><path d="M830 540 q70 -80 0 -160"/><path d="M860 560 q100 -120 0 -240"/>
</g>
<g fill="none" stroke="#ff7a5a" stroke-width="5" opacity="0.55">
<path d="M1120 520 q-40 -40 0 -80"/><path d="M1090 540 q-70 -80 0 -160"/><path d="M1060 560 q-100 -120 0 -240"/>
</g>
<rect x="900" y="150" width="120" height="20" fill="#1a1720"/>
{fog(900, "#7a7088", 0.08, 90)}
''', '''<linearGradient id="wl3" x1="0" x2="1"><stop offset="0" stop-color="#1e1a2a"/><stop offset="1" stop-color="#0f0d16"/></linearGradient>
<linearGradient id="wr3" x1="1" x2="0"><stop offset="0" stop-color="#1e1a2a"/><stop offset="1" stop-color="#0f0d16"/></linearGradient>
<clipPath id="fl3"><polygon points="0,1080 780,640 1140,640 1920,1080"/></clipPath>''')

# S4 — bedroom in the storm, walkie-talkie on the pillow
scenes["s4"] = kid_bed_room("r4", flash=True, body_extra=walkie(860, 520, 0.55, ch="2", screen="#7fe08a"))

# S5 — close-up: the channel display reads 9, red
def closeup(ch, screen, led, extra=""):
    return svg(f'''
<rect width="{W}" height="{H}" fill="#08070b"/>
<rect x="0" y="0" width="{W}" height="{H}" fill="#2a3150" opacity="0.25"/>
<path d="M0 860 C500 800 1400 820 1920 880 L1920 1080 L0 1080Z" fill="#202542"/>
<path d="M0 860 C500 800 1400 820 1920 880" stroke="#2f365c" stroke-width="10" fill="none"/>
<circle cx="960" cy="540" r="380" fill="{screen}" opacity="0.10" filter="url(#blur60)"/>
{walkie(720, 140, 1.5, ch=ch, screen=screen, led=led, antenna=False)}
{extra}
''')
scenes["s5"] = closeup("9", "#ff4a3a", "#ff3b2f",
                       '<g fill="none" stroke="#ff8a7a" stroke-width="6" opacity="0.5">'
                       '<path d="M1250 360 q50 60 0 120"/><path d="M1300 320 q90 100 0 200"/><path d="M1350 280 q130 140 0 280"/>'
                       '<path d="M670 360 q-50 60 0 120"/><path d="M620 320 q-90 100 0 200"/><path d="M570 280 q-130 140 0 280"/></g>')

# S6 — kid under the blanket, holding the radio to his mouth, red screen glow
kid = f'''
<path d="M560 900 C560 600 760 470 960 470 C1160 470 1360 600 1360 900Z" fill="#2a2f4c"/>
<path d="M600 900 C600 640 780 520 960 520 C1140 520 1320 640 1320 900Z" fill="#141626"/>
<ellipse cx="960" cy="720" rx="230" ry="200" fill="#ff4a3a" opacity="0.18" filter="url(#blur30)"/>
<ellipse cx="930" cy="700" rx="92" ry="110" fill="#1b0c0c"/>
<path d="M850 660 C860 600 1000 590 1020 650" fill="#0d0607"/>
<ellipse cx="900" cy="700" rx="10" ry="6" fill="#ffd0c0" opacity="0.8"/>
<ellipse cx="950" cy="702" rx="10" ry="6" fill="#ffd0c0" opacity="0.8"/>
{walkie(990, 640, 0.6, ch="9", screen="#ff4a3a", led="#ff3b2f", rot=-15)}
<path d="M960 820 C1000 790 1040 760 1030 720" stroke="#1b0c0c" stroke-width="40" stroke-linecap="round" fill="none"/>
'''
scenes["s6"] = kid_bed_room("r6", body_extra=kid)

# S7 — Danny's room: asleep, walkie on the dresser, battery door open and empty
scenes["s7"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0a0c14"/>
<rect x="0" y="0" width="{W}" height="760" fill="#121726"/>
<g opacity="0.3">{''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="#2a3352"/>' for x in range(60, 1920, 120) for y in range(60, 760, 120))}</g>
<rect x="0" y="760" width="{W}" height="320" fill="#0c0a10"/>
<!-- night-light -->
<circle cx="540" cy="800" r="14" fill="#9fd0ff"/>{glow(540, 800, 100, "#9fd0ff", 0.5)}
<!-- small bed with sleeping lump -->
<g transform="translate(470 0)">
<rect x="120" y="640" width="700" height="40" rx="12" fill="#1b1d2c"/>
<path d="M130 680 C300 560 650 580 810 680 L810 860 L130 860Z" fill="#2c3a5a"/>
<path d="M250 640 C330 560 520 560 620 630 C660 650 700 670 720 690" fill="#344670"/>
<ellipse cx="220" cy="650" rx="70" ry="44" fill="#3d4a6c"/>
<circle cx="250" cy="625" r="40" fill="#1a1622"/>
<path d="M220 600 C240 580 280 585 290 610" fill="#0e0b12"/>
</g>
<!-- dresser -->
<g transform="translate(1270 940) scale(0.7) translate(-1000 -940)">
<rect x="1000" y="560" width="600" height="380" rx="10" fill="#1d1620"/>
<g fill="#140f17">{''.join(f'<rect x="1030" y="{y}" width="540" height="100" rx="6"/>' for y in (600, 720, 840))}</g>
<g fill="#5a4636">{''.join(f'<circle cx="1300" cy="{y + 50}" r="10"/>' for y in (600, 720, 840))}</g>
<!-- walkie face down-ish, battery door open, empty -->
<g transform="translate(1180 330)">
<rect x="28" y="-120" width="20" height="130" rx="8" fill="#15171c"/>
<rect x="0" y="0" width="150" height="232" rx="22" fill="#2b2f36"/>
<rect x="18" y="20" width="114" height="190" rx="12" fill="#0c0d10"/>
<g stroke="#3a3f48" stroke-width="3">{''.join(f'<rect x="{x}" y="34" width="28" height="160" rx="8" fill="none"/>' for x in (30, 62, 94))}</g>
<rect x="160" y="40" width="90" height="190" rx="12" fill="#2b2f36" transform="rotate(25 160 40)"/>
<circle cx="120" cy="18" r="7" fill="#2a1c1c"/>
</g>
<circle cx="1260" cy="460" r="200" fill="#9fd0ff" opacity="0.06" filter="url(#blur60)"/>
</g>
<!-- open doorway on the right edge -->
<rect x="1720" y="200" width="200" height="740" fill="#050508"/>
''')

# S8 — looking back: my doorway, my radio glowing on the bed, a tall shape in the hall
scenes["s8"] = svg(f'''
<rect width="{W}" height="{H}" fill="#07060a"/>
<rect x="0" y="0" width="{W}" height="{H}" fill="#1a1020" opacity="0.4"/>
<rect x="640" y="140" width="640" height="860" fill="#0f0a10"/>
<rect x="680" y="180" width="560" height="820" fill="#2a0e10"/>
<rect x="680" y="180" width="560" height="820" fill="#ff3b2f" opacity="0.10" filter="url(#blur30)"/>
<rect x="700" y="760" width="520" height="140" fill="#1a0a0c"/>
<path d="M700 760 C800 720 1100 720 1220 760" fill="#3a1416"/>
{walkie(900, 640, 0.42, ch="9", screen="#ff4a3a", led="#ff3b2f", rot=-70)}
{glow(960, 690, 160, "#ff3b2f", 0.45)}
{figure(1110, 1000, 760, "#030203")}
{eyes(1110, 340, 24, 5, "#ffd9c8")}
<polygon points="680,1000 1240,1000 1500,1080 420,1080" fill="#ff3b2f" opacity="0.08"/>
<rect x="0" y="1000" width="{W}" height="80" fill="#0a0709"/>
{fog(1000, "#6a3040", 0.12, 80)}
''')

# S9 — present day attic: a little girl by the round window holding the old walkie, red glow
scenes["s9"] = svg(f'''
<rect width="{W}" height="{H}" fill="#0a0910"/>
<polygon points="0,1080 0,620 960,40 1920,620 1920,1080" fill="#16121c"/>
<g stroke="#0b090f" stroke-width="22">
<line x1="0" y1="620" x2="960" y2="40"/><line x1="1920" y1="620" x2="960" y2="40"/>
<line x1="320" y1="420" x2="320" y2="1080" stroke-width="16"/><line x1="1600" y1="420" x2="1600" y2="1080" stroke-width="16"/>
</g>
<circle cx="960" cy="380" r="150" fill="#0a0b14"/>
<circle cx="960" cy="380" r="128" fill="#2a3456"/>
{rain(40, 0.5, "#c6d2f0", 260, 500, 840, 1080)}
<g stroke="#0a0b14" stroke-width="12"><line x1="832" y1="380" x2="1088" y2="380"/><line x1="960" y1="252" x2="960" y2="508"/></g>
<polygon points="860,470 1060,470 1300,1080 620,1080" fill="#8fa4d8" opacity="0.07"/>
<rect x="0" y="900" width="{W}" height="180" fill="#100d14"/>
<!-- boxes -->
<g fill="#2a2018"><rect x="380" y="760" width="200" height="160"/><rect x="420" y="640" width="150" height="120"/>
<rect x="1360" y="780" width="220" height="140"/></g>
<g stroke="#1a140f" stroke-width="4"><line x1="380" y1="790" x2="580" y2="790"/><line x1="1360" y1="810" x2="1580" y2="810"/></g>
<path d="M1340 780 L1380 720 L1560 720 L1600 780Z" fill="#33281e"/>
<!-- little girl silhouette, pigtails -->
<g fill="#050407">
<circle cx="960" cy="660" r="46"/>
<ellipse cx="906" cy="650" rx="16" ry="30" transform="rotate(25 906 650)"/>
<ellipse cx="1014" cy="650" rx="16" ry="30" transform="rotate(-25 1014 650)"/>
<path d="M915 705 L1005 705 L1060 910 L860 910Z"/>
<rect x="915" y="905" width="26" height="40"/><rect x="980" y="905" width="26" height="40"/>
<path d="M925 730 L900 820" stroke="#050407" stroke-width="22" stroke-linecap="round"/>
</g>
{walkie(1020, 690, 0.3, ch="9", screen="#ff4a3a", led="#ff3b2f", rot=10)}
{glow(1050, 740, 120, "#ff3b2f", 0.5)}
<rect x="440" y="720" width="70" height="20" fill="#2b2f36" transform="rotate(-10 470 730)"/>
{fog(960, "#8a7a98", 0.10, 70)}
''')

for name, markup in scenes.items():
    save(name, markup)
print("drew", ", ".join(scenes))
