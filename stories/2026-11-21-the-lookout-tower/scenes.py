"""Scenes for The Lookout Tower."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *


def pine(x, base, h, color, w=None):
    """Layered pine silhouette."""
    w = w or h * 0.42
    out = [f'<rect x="{x - 5}" y="{base - h * 0.12:.0f}" width="10" height="{h * 0.12:.0f}" fill="{color}"/>']
    tiers = 5
    for i in range(tiers):
        tb = base - h * 0.1 - i * h * 0.17
        tw = w * (1 - i * 0.17)
        top = tb - h * 0.3
        out.append(f'<polygon points="{x - tw / 2:.0f},{tb:.0f} {x},{top:.0f} {x + tw / 2:.0f},{tb:.0f}" fill="{color}"/>')
    return "".join(out)


def pine_row(y, n, hmin, hmax, color, x0=-60, x1=1980):
    out = []
    for _ in range(n):
        out.append(pine(rnd.randint(x0, x1), y + rnd.randint(-10, 20), rnd.randint(hmin, hmax), color))
    return "".join(out)


def mountains(y, color, amp=120, seed_pts=None):
    pts = [(-50, y)]
    x = -50
    while x < 2000:
        x += rnd.randint(110, 220)
        pts.append((x, y - rnd.randint(int(amp * 0.3), amp)))
    d = "M" + " L".join(f"{a} {b}" for a, b in pts) + f" L1980 1080 L-60 1080 Z"
    return f'<path d="{d}" fill="{color}"/>'


SKY = sky("sk", "#03040b", "#121733", "#2a2340")

# ---------- S1: the tower on the ridge ----------
cx, cab_y = 960, 250
legs = (f'<g stroke="#07070c" stroke-width="16" stroke-linecap="round">'
        f'<line x1="{cx - 210}" y1="900" x2="{cx - 120}" y2="{cab_y + 150}"/>'
        f'<line x1="{cx + 210}" y1="900" x2="{cx + 120}" y2="{cab_y + 150}"/></g>')
braces = ""
for i in range(5):
    y1 = 900 - i * 125; y2 = y1 - 125
    xl1 = cx - 210 + i * 18; xl2 = cx - 210 + (i + 1) * 18
    braces += (f'<line x1="{xl1}" y1="{y1}" x2="{2 * cx - xl2}" y2="{max(y2, cab_y + 150)}" stroke="#07070c" stroke-width="7"/>'
               f'<line x1="{2 * cx - xl1}" y1="{y1}" x2="{xl2}" y2="{max(y2, cab_y + 150)}" stroke="#07070c" stroke-width="7"/>'
               f'<line x1="{xl1}" y1="{y1}" x2="{2 * cx - xl1}" y2="{y1}" stroke="#07070c" stroke-width="8"/>')
stairs = ""
for i in range(6):
    y = 880 - i * 105
    if i % 2 == 0:
        stairs += f'<line x1="{cx - 150 + i * 10}" y1="{y}" x2="{cx + 130 - i * 10}" y2="{y - 105}" stroke="#0d0d15" stroke-width="10"/>'
    else:
        stairs += f'<line x1="{cx + 130 - i * 10}" y1="{y}" x2="{cx - 150 + i * 10}" y2="{y - 105}" stroke="#0d0d15" stroke-width="10"/>'
cab = (f'<rect x="{cx - 150}" y="{cab_y}" width="300" height="150" fill="#08080e"/>'
       f'<polygon points="{cx - 180},{cab_y + 4} {cx},{cab_y - 70} {cx + 180},{cab_y + 4}" fill="#06060b"/>'
       f'<rect x="{cx - 170}" y="{cab_y + 148}" width="340" height="14" fill="#06060b"/>'
       + "".join(f'<rect x="{x}" y="{cab_y + 30}" width="56" height="70" fill="#ffb54a"/>' for x in range(cx - 132, cx + 130, 66))
       + f'<rect x="{cx - 132}" y="{cab_y + 30}" width="264" height="70" fill="#ffb54a" filter="url(#blur30)" opacity="0.7"/>'
       + "".join(f'<line x1="{x}" y1="{cab_y + 30}" x2="{x}" y2="{cab_y + 100}" stroke="#08080e" stroke-width="10"/>' for x in range(cx - 70, cx + 130, 66))
       + f'<line x1="{cx - 132}" y1="{cab_y + 65}" x2="{cx + 132}" y2="{cab_y + 65}" stroke="#08080e" stroke-width="4"/>'
       + f'<line x1="{cx - 170}" y1="{cab_y + 115}" x2="{cx + 170}" y2="{cab_y + 115}" stroke="#06060b" stroke-width="6"/>'
       + "".join(f'<line x1="{x}" y1="{cab_y + 115}" x2="{x}" y2="{cab_y + 150}" stroke="#06060b" stroke-width="4"/>' for x in range(cx - 165, cx + 170, 30)))
save("s1", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sk)"/>
{stars(220, 700)}
{moon(1330, 190, 70)}
{mountains(720, "#141830", 160)}
{fog(700, "#8d93b5", 0.12)}
{pine_row(840, 40, 120, 220, "#0c0e1a")}
<path d="M0 900 C400 860 700 880 960 870 C1250 860 1600 880 1920 900 L1920 1080 L0 1080Z" fill="#08090f"/>
{glow(cx, cab_y + 70, 230, "#ffae4a", 0.22)}
{legs}{braces}{stairs}{cab}
{pine_row(1000, 30, 220, 380, "#050609")}
{fog(960, "#aab3c8", 0.1)}
''', SKY))

# ---------- S2: inside the cab, trapdoor in the floor ----------
win = "".join(f'<rect x="{x}" y="60" width="300" height="300" fill="#0a0d22"/>' for x in range(60, 1900, 320))
mull = "".join(f'<rect x="{x - 10}" y="40" width="20" height="340" fill="#1a120d"/>' for x in range(50, 1920, 320))
planks = "".join(f'<line x1="{960 + (x - 960) * 0.45:.0f}" y1="520" x2="{x}" y2="1080" stroke="#1f150e" stroke-width="3"/>' for x in range(-800, 2800, 140))
trap = (f'<polygon points="800,700 1120,700 1190,900 730,900" fill="#3a2717"/>'
        f'<polygon points="800,700 1120,700 1190,900 730,900" fill="none" stroke="#120b07" stroke-width="10"/>'
        + "".join(f'<line x1="{800 + i * 64}" y1="700" x2="{730 + i * 92}" y2="900" stroke="#1d130b" stroke-width="4"/>' for i in range(1, 5))
        + '<rect x="900" y="780" width="170" height="26" rx="6" fill="#5a5f6a"/>'
          '<rect x="1060" y="768" width="40" height="50" rx="6" fill="#43474f"/>'
          '<rect x="930" y="770" width="26" height="46" rx="6" fill="#6c717c"/>'
          '<circle cx="880" cy="793" r="16" fill="#2b2d33" stroke="#6c717c" stroke-width="5"/>')
lantern = ('<g transform="translate(1440 560)">'
           f'{glow(0, 40, 260, "#ffae4a", 0.45)}'
           '<rect x="-130" y="110" width="260" height="20" fill="#24180f"/><rect x="-110" y="130" width="16" height="250" fill="#1a110a"/><rect x="94" y="130" width="16" height="250" fill="#1a110a"/>'
           '<path d="M-30 -20 h60 l10 20 h-80z" fill="#2a2a2e"/><rect x="-36" y="0" width="72" height="90" rx="8" fill="#ffcf7a" opacity="0.9"/>'
           '<rect x="-40" y="90" width="80" height="20" fill="#2a2a2e"/><path d="M-20 -20 q20 -40 40 0" stroke="#2a2a2e" stroke-width="5" fill="none"/>'
           '<path d="M0 70 q-10 -25 0 -45 q10 20 0 45z" fill="#fff3c4"/></g>')
save("s2", svg(f'''
<rect width="{W}" height="{H}" fill="#140d09"/>
<rect x="0" y="0" width="{W}" height="420" fill="#100a07"/>
{win}
<g>{stars(120, 360, 0.8)}</g>
{mull}
<rect x="0" y="380" width="{W}" height="150" fill="#1d130c"/>
<rect x="0" y="372" width="{W}" height="16" fill="#2c1d12"/>
<polygon points="0,1080 0,520 1920,520 1920,1080" fill="#2a1b10"/>
<g clip-path="url(#fl)">{planks}</g>
{trap}
{lantern}
<g transform="translate(400 560)"><ellipse cx="0" cy="0" rx="150" ry="40" fill="#3a2717"/><rect x="-14" y="0" width="28" height="300" fill="#1a110a"/>
<ellipse cx="0" cy="-6" rx="120" ry="28" fill="#5d4a2e"/><line x1="-100" y1="-6" x2="100" y2="-6" stroke="#2a1b10" stroke-width="3"/><line x1="0" y1="-30" x2="0" y2="18" stroke="#2a1b10" stroke-width="3"/></g>
''', '<clipPath id="fl"><polygon points="0,1080 0,520 1920,520 1920,1080"/></clipPath>'))

# ---------- S3: flashlight in the pines ----------
frame = ('<rect x="0" y="0" width="1920" height="90" fill="#0c0805"/><rect x="0" y="960" width="1920" height="120" fill="#140d08"/>'
         '<rect x="420" y="0" width="34" height="1080" fill="#0c0805"/><rect x="1466" y="0" width="34" height="1080" fill="#0c0805"/>'
         '<rect x="454" y="520" width="1012" height="16" fill="#0c0805"/>')
save("s3", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sk)"/>
{stars(160, 400)}
{mountains(420, "#161a33", 110)}
{fog(470, "#8d93b5", 0.12)}
{pine_row(560, 70, 60, 110, "#0f1222")}
{pine_row(700, 70, 90, 150, "#0b0d19")}
{pine_row(860, 60, 120, 200, "#07080f")}
<polygon points="1000,780 700,600 780,540" fill="#fff1c6" opacity="0.45" filter="url(#blur8)"/><polygon points="1000,780 700,600 780,540" fill="#fff1c6" opacity="0.25" filter="url(#blur30)"/>
<circle cx="1000" cy="780" r="60" fill="#fff1c6" opacity="0.8" filter="url(#bb)"/>
<circle cx="1000" cy="780" r="7" fill="#fffbe8"/>
{pine_row(1000, 25, 220, 300, "#040509", 0, 1920)}
{frame}
<rect x="454" y="90" width="1012" height="870" fill="#9fb4e8" opacity="0.04"/>
''', SKY + '<filter id="bb" x="-2" y="-2" width="5" height="5"><feGaussianBlur stdDeviation="30"/></filter>'))

# ---------- S4: something climbing the stairs ----------
st = ""
for i in range(7):
    y = 1080 - i * 150
    a, b = (620, 1300) if i % 2 == 0 else (1300, 620)
    st += (f'<line x1="{a}" y1="{y}" x2="{b}" y2="{y - 150}" stroke="#1b1c27" stroke-width="22"/>'
           f'<line x1="{a}" y1="{y - 55}" x2="{b}" y2="{y - 205}" stroke="#14151e" stroke-width="6"/>'
           + "".join(f'<line x1="{a + (b - a) * t / 8:.0f}" y1="{y - 150 * t / 8:.0f}" x2="{a + (b - a) * t / 8:.0f}" y2="{y - 55 - 150 * t / 8:.0f}" stroke="#14151e" stroke-width="5"/>' for t in range(1, 8)))
save("s4", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sk)"/>
{stars(120, 900, 0.5)}
{pine_row(1080, 40, 300, 600, "#0a0c16")}
<g stroke="#0a0a10" stroke-width="40"><line x1="560" y1="1080" x2="680" y2="0"/><line x1="1360" y1="1080" x2="1240" y2="0"/></g>
<g stroke="#0a0a10" stroke-width="12"><line x1="560" y1="1080" x2="1310" y2="540"/><line x1="1360" y1="1080" x2="610" y2="540"/><line x1="620" y1="540" x2="1300" y2="0"/><line x1="1300" y1="540" x2="620" y2="0"/></g>
{st}
<rect x="590" y="0" width="740" height="90" fill="#06060a"/>
<rect x="840" y="40" width="240" height="50" fill="#ffb54a" opacity="0.5"/>{glow(960, 60, 120, "#ffae4a", 0.35)}
<g transform="rotate(-12 900 560)">{figure(900, 640, 330, "#020203")}</g>
{fog(900, "#aab3c8", 0.12)}
''', SKY))


# ---------- S5: knocking at the trapdoor (top-down) ----------
def trapdoor_close(hand=False, light="#ff6a3a"):
    pl = "".join(f'<rect x="{x}" y="0" width="118" height="1080" fill="{c}"/><line x1="{x}" y1="0" x2="{x}" y2="1080" stroke="#120a05" stroke-width="5"/>'
                 for x, c in zip(range(0, 1920, 120), ["#2d1e12", "#33220f", "#2a1b10", "#30200f"] * 5))
    door = (f'<rect x="600" y="260" width="720" height="560" fill="#3b2715"/>'
            + "".join(f'<line x1="{x}" y1="260" x2="{x}" y2="820" stroke="#1b1108" stroke-width="5"/>' for x in range(720, 1320, 120))
            + f'<rect x="600" y="260" width="720" height="560" fill="none" stroke="{light}" stroke-width="6" opacity="0.8"/>'
            + f'<rect x="600" y="260" width="720" height="560" fill="none" stroke="{light}" stroke-width="22" opacity="0.4" filter="url(#blur8)"/>'
            + '<rect x="560" y="320" width="80" height="34" fill="#3d3f46"/><rect x="560" y="720" width="80" height="34" fill="#3d3f46"/>'
            + '<rect x="980" y="500" width="380" height="60" rx="10" fill="#585d68"/><rect x="1330" y="480" width="80" height="100" rx="10" fill="#40444c"/>'
            + '<rect x="1060" y="482" width="40" height="96" rx="8" fill="#6c717c"/>')
    h = ""
    if hand:
        h = ('<g fill="#c9a888" stroke="#7d5f47" stroke-width="3">'
             '<path d="M1040 1080 L1030 640 C1030 600 1060 585 1100 588 L1180 590 C1210 590 1220 610 1210 640 L1200 1080Z"/>'
             '<path d="M1045 600 C1040 545 1060 520 1080 522 C1098 524 1100 560 1096 600Z"/>'
             '<path d="M1097 596 C1095 535 1110 510 1132 512 C1152 515 1150 560 1145 596Z"/>'
             '<path d="M1146 598 C1146 545 1160 525 1180 528 C1198 532 1196 570 1190 604Z"/>'
             '<path d="M1030 680 C990 660 970 620 985 600 C1000 585 1030 610 1045 640Z"/></g>')
    return svg(f'''
<rect width="{W}" height="{H}" fill="#1c120a"/>{pl}
{glow(960, 540, 420, light, 0.18)}
{door}{h}
<rect width="{W}" height="{H}" fill="#000" opacity="0.25"/>
{glow(1700, 150, 260, "#ffae4a", 0.18)}
''')


save("s5", trapdoor_close())
save("s5b", trapdoor_close(hand=True))

# ---------- S6: clear sky, no storm, empty road ----------
road = '<path d="M1000 1080 C980 980 1150 940 1080 880 C1010 820 860 820 900 760 C930 715 1020 700 1000 660" stroke="#232741" stroke-width="18" fill="none"/>'
save("s6", svg(f'''
<rect width="{W}" height="{H}" fill="url(#sk6)"/>
{stars(520, 640, 0.95)}
<path d="M300 0 C700 200 1200 300 1700 640" stroke="#c8cdf0" stroke-width="160" fill="none" opacity="0.05" filter="url(#blur60)"/>
{mountains(660, "#171b38", 150)}
{mountains(740, "#10132a", 110)}
{fog(700, "#8d93b5", 0.1)}
{pine_row(820, 70, 60, 120, "#0a0c1a")}
{road}
{pine_row(960, 50, 120, 200, "#06070f")}
{frame}
''', sky("sk6", "#02030a", "#0e1330", "#262a4e")))

# ---------- S7: sitting on the trapdoor until dawn ----------
person = ('<g fill="#060403">'
          '<circle cx="960" cy="520" r="52"/>'
          '<path d="M900 575 C870 640 860 720 880 800 L1050 800 C1070 720 1050 640 1020 575 Z"/>'
          '<path d="M880 780 L790 700 L760 820 L820 840 Z"/><path d="M1040 780 L1130 700 L1160 820 L1100 840 Z"/>'
          '<path d="M900 650 C860 690 820 700 800 700" stroke="#060403" stroke-width="34" stroke-linecap="round" fill="none"/>'
          '<path d="M1020 650 C1060 690 1100 700 1120 700" stroke="#060403" stroke-width="34" stroke-linecap="round" fill="none"/></g>')
save("s7", svg(f'''
<rect width="{W}" height="{H}" fill="#0e0907"/>
<rect x="0" y="0" width="{W}" height="460" fill="#0a0705"/>
{win.replace('y="60"', 'y="80"')}
{stars(90, 380, 0.6)}
{mull}
<rect x="0" y="420" width="{W}" height="20" fill="#24180e"/>
<polygon points="0,1080 0,760 1920,760 1920,1080" fill="#1f140b"/>
<polygon points="700,800 1220,800 1300,1000 620,1000" fill="#2e1e10" stroke="#120b07" stroke-width="8"/>
{glow(1330, 880, 160, "#ffae4a", 0.5)}
<rect x="1305" y="850" width="50" height="62" rx="6" fill="#ffcf7a" opacity="0.85"/><rect x="1300" y="912" width="60" height="14" fill="#2a2a2e"/>
{glow(960, 650, 300, "#ffae4a", 0.12)}
{person}
'''))


# ---------- S8: the tap on the glass, sixty feet up ----------
def glass(face=False):
    hand = ('<g fill="#b9c0cf" opacity="0.85">'
            '<path d="M1010 620 C1000 560 1010 520 1040 515 L1110 512 C1140 515 1150 560 1140 620 Z"/>'
            '<path d="M1015 525 C1008 440 1014 380 1030 378 C1046 376 1048 440 1045 520Z"/>'
            '<path d="M1050 515 C1048 420 1056 350 1072 348 C1090 346 1090 420 1084 515Z"/>'
            '<path d="M1088 515 C1088 430 1098 370 1114 370 C1130 372 1126 440 1120 518Z"/>'
            '<path d="M1122 525 C1124 460 1134 420 1148 422 C1162 426 1156 480 1148 540Z"/>'
            '<path d="M1012 600 C980 580 960 540 972 525 C986 512 1010 545 1020 570Z"/></g>')
    f = ""
    if face:
        f = (f'<g opacity="0.95"><ellipse cx="860" cy="470" rx="150" ry="200" fill="#020203"/>'
             f'<path d="M640 960 C660 760 720 660 860 650 C1000 660 1060 760 1080 960Z" fill="#020203"/></g>'
             + eyes(860, 450, 70, 11))
    return svg(f'''
<rect width="{W}" height="{H}" fill="url(#sk)"/>
{stars(260, 900, 0.8)}
{f}{hand}
<rect x="454" y="90" width="1012" height="870" fill="#9fb4e8" opacity="0.05"/>
<path d="M500 140 L700 90 M1300 900 L1450 840" stroke="#dfe3f5" stroke-width="3" opacity="0.15"/>
{frame}
{glow(1700, 980, 260, "#ffae4a", 0.25)}
''', SKY)


save("s8", glass())
save("s8b", glass(face=True))
