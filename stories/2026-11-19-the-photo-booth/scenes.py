"""Scenes for 'The Photo Booth'. Run inside this folder: python3 scenes.py"""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

CURTAIN_RED = "#8e1b22"


def curtain(x, y, w, h, open_frac=0.0, color=CURTAIN_RED, sway=0):
    """A pleated curtain hanging from a rod at (x,y); open_frac pulls it toward the left."""
    cw = w * (1 - open_frac)
    folds = max(4, int(cw / 34))
    out = [f'<rect x="{x - 10}" y="{y - 14}" width="{w + 20}" height="14" rx="6" fill="#2a2a30"/>']
    out.append(f'<path d="M{x} {y} L{x + cw:.0f} {y} Q{x + cw + sway:.0f} {y + h * .6:.0f} {x + cw + sway * 1.6:.0f} {y + h} L{x} {y + h} Z" fill="{color}"/>')
    for i in range(folds):
        fx = x + (i + .5) * cw / folds
        out.append(f'<path d="M{fx:.0f} {y + 4} Q{fx + sway * .5 + 6:.0f} {y + h * .5:.0f} {fx + sway * (i / folds) * 1.6:.0f} {y + h - 4}" stroke="#000" stroke-opacity="0.35" stroke-width="9" fill="none"/>')
        out.append(f'<path d="M{fx + 12:.0f} {y + 4} Q{fx + sway * .5 + 18:.0f} {y + h * .5:.0f} {fx + 12 + sway * (i / folds) * 1.6:.0f} {y + h - 4}" stroke="#ff6d6d" stroke-opacity="0.12" stroke-width="5" fill="none"/>')
    return "".join(out)


def booth(cx, base, inner_glow="#ffd9a0", open_frac=0.35, sway=0, glow_op=0.55, hand=False, stool=True):
    """Photo booth cabinet seen from the front; curtain on the right half."""
    x0, w, h = cx - 210, 420, 640
    y0 = base - h
    parts = [
        f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="10" fill="url(#boothbody)"/>',
        f'<rect x="{x0}" y="{y0}" width="{w}" height="70" rx="10" fill="#3a1418"/>',
        f'<text x="{cx}" y="{y0 + 50}" text-anchor="middle" font-family="{SERIF}" font-size="40" fill="#ffd27a" letter-spacing="6">PHOTOS</text>',
        glow(cx, y0 + 35, 120, "#ffb84a", 0.25),
        # booth opening
        f'<rect x="{x0 + 30}" y="{y0 + 100}" width="{w - 60}" height="{h - 150}" fill="#0b0708"/>',
        f'<rect x="{x0 + 30}" y="{y0 + 100}" width="{w - 60}" height="{h - 150}" fill="{inner_glow}" opacity="{glow_op * .45:.2f}"/>',
        f'<rect x="{x0 + 30}" y="{y0 + 100}" width="{w - 60}" height="{h - 150}" fill="{inner_glow}" opacity="{glow_op * .35:.2f}" filter="url(#blur30)"/>',
        # back wall: camera window
        f'<rect x="{cx - 60}" y="{y0 + 150}" width="120" height="80" rx="8" fill="#141218"/>',
        f'<circle cx="{cx}" cy="{y0 + 190}" r="26" fill="#050407"/><circle cx="{cx - 8}" cy="{y0 + 182}" r="7" fill="#9bb6d8" opacity="0.6"/>',
    ]
    if stool:
        parts.append(f'<g fill="#1a1416"><ellipse cx="{cx}" cy="{base - 200}" rx="70" ry="16"/><rect x="{cx - 8}" y="{base - 200}" width="16" height="150"/><ellipse cx="{cx}" cy="{base - 50}" rx="55" ry="10"/></g>')
    parts.append(curtain(x0 + 30, y0 + 100, w - 60, h - 150, open_frac, sway=sway))
    if hand:
        hx = x0 + 30 + (w - 60) * (1 - open_frac) + sway
        parts.append(f'<g fill="#d9d2c4"><rect x="{hx - 14:.0f}" y="{y0 + 300}" width="34" height="18" rx="9"/><rect x="{hx - 14:.0f}" y="{y0 + 322}" width="38" height="18" rx="9"/>'
                     f'<rect x="{hx - 14:.0f}" y="{y0 + 344}" width="36" height="18" rx="9"/><rect x="{hx - 12:.0f}" y="{y0 + 366}" width="30" height="16" rx="8"/></g>')
    # side slot + tray
    parts += [
        f'<rect x="{x0 + w}" y="{y0 + 120}" width="70" height="{h - 120}" fill="#2b0f13"/>',
        f'<rect x="{x0 + w + 12}" y="{y0 + 300}" width="46" height="10" rx="3" fill="#050305"/>',
        f'<rect x="{x0 + w + 12}" y="{y0 + 170}" width="46" height="60" rx="6" fill="#1a0a0c"/>',
        f'<circle cx="{x0 + w + 35}" cy="{y0 + 200}" r="9" fill="#ffcf6a"/>',
    ]
    return "".join(parts)


BOOTH_DEFS = '''<linearGradient id="boothbody" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#4a161c"/><stop offset="0.5" stop-color="#5e1d24"/><stop offset="1" stop-color="#3a1015"/></linearGradient>'''

# S1 — boardwalk arcade at night, off-season
planks = "".join(f'<line x1="{x}" y1="820" x2="{960 + (x - 960) * 1.9:.0f}" y2="1080" stroke="#0c0a10" stroke-width="3"/>' for x in range(-200, 2200, 70))
bulbs = "".join(f'<circle cx="{x}" cy="{388 + (x % 3) * 2}" r="6" fill="#ffd27a"/>' for x in range(640, 1290, 34))
lamps = "".join(f'<rect x="{x}" y="560" width="10" height="260" fill="#07060a"/><circle cx="{x + 5}" cy="555" r="14" fill="#ffe2a8"/>{glow(x + 5, 555, 50, "#ffcf7a", 0.5)}' for x in (420, 1500))
save("s1", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(140, 420)}
{moon(1520, 180, 80)}
<rect x="0" y="560" width="{W}" height="260" fill="#0d1424"/>
<g stroke="#c9d3ea" stroke-opacity="0.18" stroke-width="3">{"".join(f'<line x1="{1350 + i * 8}" y1="{580 + i * 22}" x2="{1690 - i * 8}" y2="{580 + i * 22}"/>' for i in range(9))}</g>
<g fill="#06050a">
<rect x="600" y="400" width="720" height="420"/>
<polygon points="580,410 960,300 1340,410"/>
<rect x="1320" y="520" width="200" height="300"/>
<rect x="180" y="470" width="420" height="350"/>
<path d="M190 470 L190 360 L590 360 L590 470" fill="none" stroke="#06050a" stroke-width="16"/>
</g>
<g transform="translate(240 300)" fill="none" stroke="#08070c" stroke-width="10">
<circle cx="0" cy="0" r="170"/>{"".join(f'<line x1="0" y1="0" x2="{170 * __import__("math").cos(a * 0.524):.0f}" y2="{170 * __import__("math").sin(a * 0.524):.0f}"/>' for a in range(12))}
<line x1="0" y1="0" x2="-90" y2="250"/><line x1="0" y1="0" x2="90" y2="250"/></g>
{bulbs}
<rect x="760" y="420" width="400" height="80" rx="10" fill="#120609"/>
<text x="960" y="480" text-anchor="middle" font-family="{SERIF}" font-size="60" fill="#ff5a5a" letter-spacing="10">ARCADE</text>
{glow(960, 460, 200, "#ff3b3b", 0.25)}
{lit_window(700, 560, 120, 150, "#ffb54a")}
{lit_window(1100, 560, 120, 150, "#ffb54a")}
<rect x="900" y="600" width="120" height="220" fill="#ffb54a" opacity="0.85"/>
<rect x="900" y="600" width="120" height="220" fill="#ffb54a" filter="url(#blur30)" opacity="0.7"/>
<rect x="0" y="815" width="{W}" height="265" fill="#1a1520"/>
{planks}
<polygon points="900,820 1020,820 1200,1080 720,1080" fill="#ffb54a" opacity="0.12"/>
{lamps}
<g fill="#07060a">{"".join(f'<rect x="{x}" y="770" width="10" height="50"/>' for x in range(0, 1920, 120))}<rect x="0" y="770" width="{W}" height="8"/></g>
{fog(800, "#9aa5c4", 0.12)}
''', sky("sky1", "#04050e", "#141a36", "#2a2140")))

# S2 — inside the arcade, booth in back corner
cabinets = ""
for i, x in enumerate((560, 700, 1220, 1360)):
    col = ["#3dd6ff", "#ff4fd8", "#7dff6a", "#ffcf3d"][i]
    cabinets += (f'<g><path d="M{x} 900 L{x} 520 L{x + 20} 480 L{x + 110} 480 L{x + 110} 900 Z" fill="#0b0910"/>'
                 f'<rect x="{x + 22}" y="560" width="70" height="60" fill="{col}" opacity="0.55"/>{glow(x + 57, 590, 60, col, 0.25)}'
                 f'<rect x="{x + 15}" y="650" width="85" height="20" fill="#16131c"/></g>')
save("s2", svg(f'''
<rect width="{W}" height="{H}" fill="#0a0709"/>
<rect x="0" y="0" width="{W}" height="900" fill="url(#wall2)"/>
<g stroke="#1c1418" stroke-width="2">{"".join(f'<line x1="{x}" y1="0" x2="{x}" y2="900"/>' for x in range(0, 1920, 90))}</g>
<rect x="0" y="900" width="{W}" height="180" fill="#120c10"/>
<g fill="#1b1218">{"".join(f'<rect x="{x}" y="{900 + (x // 120 % 2) * 60}" width="60" height="60"/>' for x in range(0, 1920, 120))}{"".join(f'<rect x="{x}" y="{960 - (x // 120 % 2) * 60}" width="60" height="60"/>' for x in range(60, 1920, 120))}</g>
{cabinets}
{booth(960, 900, glow_op=0.6, open_frac=0.4)}
<ellipse cx="960" cy="905" rx="320" ry="30" fill="#ffd9a0" opacity="0.12" filter="url(#blur30)"/>
<circle cx="960" cy="120" r="12" fill="#ffd9a0"/><line x1="960" y1="0" x2="960" y2="110" stroke="#000" stroke-width="3"/>
{glow(960, 140, 160, "#ffcf8a", 0.12)}
''', BOOTH_DEFS + '<linearGradient id="wall2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0d080b"/><stop offset="1" stop-color="#261419"/></linearGradient>'))

# S3 — lights out, booth starts up by itself (dark, booth glowing blue-white)
dark_cabs = "".join(f'<path d="M{x} 900 L{x} 520 L{x + 20} 480 L{x + 110} 480 L{x + 110} 900 Z" fill="#050407"/>' for x in (560, 700, 1220, 1360))
s3 = svg(f'''
<rect width="{W}" height="{H}" fill="#030204"/>
<rect x="0" y="900" width="{W}" height="180" fill="#07050a"/>
{dark_cabs}
{booth(960, 900, inner_glow="#cfe3ff", glow_op=0.75, open_frac=0.55)}
<ellipse cx="960" cy="905" rx="420" ry="40" fill="#cfe3ff" opacity="0.15" filter="url(#blur30)"/>
<polygon points="800,850 1120,850 1500,1080 420,1080" fill="#cfe3ff" opacity="0.05"/>
''', BOOTH_DEFS)
save("s3", s3)

# S3b — the flash
save("s3b", svg(f'''
<rect width="{W}" height="{H}" fill="#1d1a22"/>
{dark_cabs}
{booth(960, 900, inner_glow="#ffffff", glow_op=1.0, open_frac=0.55)}
<rect width="{W}" height="{H}" fill="#f4f6ff" opacity="0.35"/>
<circle cx="960" cy="450" r="520" fill="#ffffff" opacity="0.55" filter="url(#blur60)"/>
<circle cx="960" cy="450" r="200" fill="#ffffff" opacity="0.7" filter="url(#blur60)"/>
''', BOOTH_DEFS))

# S4 — close-up: empty stool, curtain swaying
save("s4", svg(f'''
<rect width="{W}" height="{H}" fill="#070508"/>
<rect x="560" y="0" width="800" height="1080" fill="#1a1216"/>
<rect x="560" y="0" width="800" height="1080" fill="#cfe3ff" opacity="0.12"/>
<rect x="760" y="120" width="400" height="230" rx="16" fill="#100d12"/>
<circle cx="960" cy="235" r="70" fill="#050407"/><circle cx="938" cy="212" r="18" fill="#9bb6d8" opacity="0.55"/>
<rect x="1060" y="150" width="70" height="22" rx="4" fill="#ff3b3b"/>{glow(1095, 160, 30, "#ff3b3b", 0.7)}
<g fill="#24191e"><ellipse cx="900" cy="700" rx="170" ry="38"/><rect x="884" y="700" width="32" height="330"/><ellipse cx="900" cy="1040" rx="130" ry="22"/></g>
<ellipse cx="900" cy="694" rx="160" ry="30" fill="#3a2a30"/>
{curtain(1120, 40, 420, 1040, 0.0, sway=-110)}
<rect x="300" y="0" width="260" height="1080" fill="#3a1015"/>
<rect x="1540" y="0" width="300" height="1080" fill="#3a1015"/>
{glow(960, 500, 300, "#cfe3ff", 0.12)}
'''))

# S5 — the strip in the tray: three frames, curtain wider each time
def frame_img(x, y, w, h, open_frac, hand=False):
    inner = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#d8d3c8"/>'
             f'<rect x="{x + 10}" y="{y + 10}" width="{w - 20}" height="{h - 20}" fill="#57524c"/>'
             f'<ellipse cx="{x + w / 2}" cy="{y + h * .78}" rx="{w * .22}" ry="{h * .05}" fill="#2a2724"/>'
             f'<rect x="{x + w / 2 - 6}" y="{y + h * .78}" width="12" height="{h * .2 - 10}" fill="#2a2724"/>')
    cw = (w - 20) * (1 - open_frac)
    inner += f'<rect x="{x + 10}" y="{y + 10}" width="{cw:.0f}" height="{h - 20}" fill="#1a1514"/>'
    inner += "".join(f'<line x1="{x + 18 + k * 14:.0f}" y1="{y + 12}" x2="{x + 18 + k * 14:.0f}" y2="{y + h - 12}" stroke="#000" stroke-opacity="0.5" stroke-width="4"/>' for k in range(int(cw // 14)))
    inner += f'<rect x="{x + 10 + cw:.0f}" y="{y + 10}" width="6" height="{h - 20}" fill="#2a2724"/>'
    if hand:
        hx = x + 10 + cw
        inner += (f'<g fill="#efeae0"><rect x="{hx - 4:.0f}" y="{y + h * .3:.0f}" width="40" height="16" rx="8"/><rect x="{hx - 4:.0f}" y="{y + h * .3 + 20:.0f}" width="46" height="16" rx="8"/>'
                  f'<rect x="{hx - 4:.0f}" y="{y + h * .3 + 40:.0f}" width="42" height="16" rx="8"/><rect x="{hx - 4:.0f}" y="{y + h * .3 + 60:.0f}" width="34" height="14" rx="7"/></g>')
    return inner

strip = "".join(frame_img(820, 170 + i * 250, 280, 230, f) for i, f in enumerate((0.15, 0.45, 0.75)))
save("s5", svg(f'''
<rect width="{W}" height="{H}" fill="#140709"/>
<rect x="560" y="0" width="800" height="1080" fill="#3a1015"/>
<rect x="680" y="900" width="560" height="120" rx="10" fill="#0a0406"/>
<rect x="700" y="120" width="520" height="40" rx="6" fill="#050305"/>
<g transform="rotate(-4 960 560)">
<rect x="800" y="150" width="320" height="800" fill="#ece6da"/>
{strip}
<rect x="800" y="150" width="320" height="800" fill="#ffd9a0" opacity="0.08"/>
</g>
{glow(960, 560, 380, "#ffcf8a", 0.1)}
<rect x="1450" y="300" width="40" height="40" rx="6" fill="#ffcf6a"/>{glow(1470, 320, 40, "#ffcf6a", 0.6)}
'''))

# S6 — close-up of the last frame: a pale hand on the curtain
save("s6", svg(f'''
<rect width="{W}" height="{H}" fill="#0b0809"/>
<rect x="540" y="60" width="840" height="960" fill="#e6e0d4"/>
<rect x="570" y="90" width="780" height="900" fill="#4c4843"/>
<rect x="570" y="90" width="420" height="900" fill="#0d0c0b"/>
<g stroke="#000" stroke-opacity="0.3" stroke-width="8">{"".join(f'<line x1="{x}" y1="90" x2="{x + 6}" y2="990"/>' for x in range(600, 990, 45))}</g>
<rect x="990" y="90" width="20" height="900" fill="#26231f"/>
<ellipse cx="1170" cy="760" rx="130" ry="26" fill="#22201c"/><rect x="1160" y="760" width="20" height="230" fill="#22201c"/>
<g fill="#f1ece2">
<rect x="955" y="330" width="120" height="44" rx="22"/><rect x="955" y="384" width="140" height="44" rx="22"/>
<rect x="955" y="438" width="132" height="44" rx="22"/><rect x="955" y="492" width="110" height="40" rx="20"/>
<path d="M985 520 C1000 600 1040 640 1080 660 L1100 600 C1060 570 1040 540 1035 520 Z" opacity="0.9"/>
<rect x="940" y="300" width="120" height="40" rx="20" transform="rotate(-20 1000 320)"/>
</g>
<g fill="#1a1816" opacity="0.35"><rect x="1050" y="330" width="22" height="44" rx="10"/><rect x="1070" y="384" width="22" height="44" rx="10"/><rect x="1062" y="438" width="22" height="44" rx="10"/></g>
<rect x="540" y="60" width="840" height="960" fill="#ffd9a0" opacity="0.06"/>
<rect x="570" y="90" width="780" height="900" fill="url(#grain)" opacity="0.4"/>
''', '<radialGradient id="grain" cx="0.5" cy="0.5" r="0.7"><stop offset="0.4" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.9"/></radialGradient>'))

# S7 — walking home: boardwalk behind, arcade dark, booth glow in the doorway
save("s7", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky7)"/>
{stars(120, 450)}
{moon(820, 190, 60)}
<path d="M0 640 C400 620 1400 630 1920 615 L1920 1080 L0 1080Z" fill="#0d0b14"/>
<g fill="#050409">
<rect x="1180" y="430" width="420" height="230"/>
<polygon points="1160,440 1390,370 1620,440"/>
<rect x="960" y="500" width="40" height="160"/>
<rect x="760" y="560" width="10" height="100"/><rect x="1720" y="560" width="10" height="100"/>
</g>
<rect x="1360" y="540" width="60" height="120" fill="#cfe3ff" opacity="0.85"/>
{glow(1390, 600, 90, "#cfe3ff", 0.5)}
<path d="M0 1080 L700 660 L860 660 L1500 1080Z" fill="#1c1822"/>
<g stroke="#0b0910" stroke-width="3">{"".join(f'<line x1="{780 + (i - 6) * 20}" y1="660" x2="{780 + (i - 6) * 170}" y2="1080"/>' for i in range(13))}</g>
<g fill="#030205">
<ellipse cx="760" cy="640" rx="34" ry="40"/>
<path d="M705 690 C705 660 815 660 815 690 L825 860 L800 860 L780 990 L755 990 L760 870 L745 870 L735 990 L710 990 L715 860 L695 860 Z"/>
</g>
{fog(680, "#9aa5c4", 0.15)}
''', sky("sky7", "#03040b", "#10142a", "#221a30")))

# S8 — the fourth photo on the pillow
save("s8", svg(f'''
<rect width="{W}" height="{H}" fill="#06070c"/>
<rect x="0" y="0" width="{W}" height="1080" fill="#7d8fbf" opacity="0.08"/>
<path d="M300 500 C300 420 1620 420 1620 500 L1660 1080 L260 1080 Z" fill="#1a1d2a"/>
<path d="M420 360 C460 260 1460 260 1500 360 C1540 470 1480 620 1440 640 C1100 690 820 690 480 640 C440 620 380 470 420 360Z" fill="#2c3042"/>
<path d="M480 380 C700 330 1200 330 1440 380" stroke="#3a3f55" stroke-width="10" fill="none"/>
<path d="M600 560 C800 590 1100 590 1320 560" stroke="#1d2030" stroke-width="16" fill="none"/>
<path d="M260 780 C700 720 1200 720 1660 780 L1660 1080 L260 1080Z" fill="#232739"/>
<g transform="translate(960 480) scale(1.45) translate(-960 -470) rotate(8 960 470)">
<rect x="870" y="360" width="190" height="230" fill="#ece6da"/>
<rect x="882" y="372" width="166" height="190" fill="#3a3a40"/>
<path d="M882 520 C930 480 1000 480 1048 510 L1048 562 L882 562Z" fill="#6a6a74"/>
<ellipse cx="935" cy="470" rx="32" ry="24" fill="#8a8a92"/>
<rect x="882" y="372" width="166" height="190" fill="#ffffff" opacity="0.15"/>
</g>
<circle cx="960" cy="470" r="160" fill="#dfe6ff" opacity="0.12" filter="url(#blur60)"/>
<polygon points="1500,0 1800,0 1500,1080 1100,1080" fill="#9fb4e8" opacity="0.05"/>
'''))

# S8b — the photo itself: me asleep, shot from beside the bed, flash glare
save("s8b", svg(f'''
<rect width="{W}" height="{H}" fill="#0a0809"/>
<rect x="540" y="40" width="840" height="1000" fill="#ece6da"/>
<rect x="570" y="70" width="780" height="900" fill="#15161d"/>
<path d="M570 600 C800 520 1150 520 1350 580 L1350 970 L570 970Z" fill="#4e5262"/>
<path d="M570 600 C800 520 1150 520 1350 580" stroke="#6b7083" stroke-width="10" fill="none"/>
<path d="M600 420 C620 340 900 330 960 400 C980 460 920 520 800 520 C680 520 590 490 600 420Z" fill="#9a9caa"/>
<ellipse cx="900" cy="470" rx="110" ry="78" fill="#d8cfc4"/>
<path d="M800 430 C820 380 980 370 1010 440 C980 420 880 410 820 450Z" fill="#2a2420"/>
<path d="M860 480 q14 6 28 0" stroke="#3a2e28" stroke-width="5" fill="none"/>
<path d="M930 478 q14 6 28 0" stroke="#3a2e28" stroke-width="5" fill="none"/>
<path d="M1000 540 C1050 560 1100 600 1110 640" stroke="#d8cfc4" stroke-width="40" stroke-linecap="round" fill="none"/>
<circle cx="900" cy="470" r="300" fill="#ffffff" opacity="0.28" filter="url(#blur60)"/>
<rect x="570" y="70" width="780" height="900" fill="url(#fl)"/>
<text x="1330" y="1010" text-anchor="end" font-family="{MONO}" font-size="26" fill="#8e1b22">4</text>
''', '<radialGradient id="fl" cx="0.45" cy="0.42" r="0.75"><stop offset="0.3" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.85"/></radialGradient>'))
print("done")
