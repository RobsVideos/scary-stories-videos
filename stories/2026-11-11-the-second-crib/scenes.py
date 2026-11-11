"""Scenes for 'The Second Crib' — babysitting, a baby monitor, a rainy night."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

r = random.Random(5)


def rain(n=260, op=0.25, color="#9fb0d0"):
    return "".join(f'<line x1="{x}" y1="{y}" x2="{x - 10}" y2="{y + L}" stroke="{color}" stroke-width="2" opacity="{r.uniform(op * .4, op):.2f}"/>'
                   for x, y, L in ((r.randint(0, W + 40), r.randint(-40, H), r.randint(30, 70)) for _ in range(n)))


def crib(x, y, w, h, color, bar="#000", bars=9, sw=6):
    """Crib seen from the front: top rail, bottom rail, posts, bars. (x,y) top-left of the rail."""
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{sw * 1.6:.0f}" fill="{color}"/>',
           f'<rect x="{x}" y="{y + h * .78:.0f}" width="{w}" height="{sw * 1.6:.0f}" fill="{color}"/>',
           f'<rect x="{x - sw}" y="{y - sw * 2}" width="{sw * 2}" height="{h + sw * 2}" fill="{color}"/>',
           f'<rect x="{x + w - sw}" y="{y - sw * 2}" width="{sw * 2}" height="{h + sw * 2}" fill="{color}"/>']
    for i in range(1, bars + 1):
        bx = x + w * i / (bars + 1)
        out.append(f'<rect x="{bx - sw / 2:.0f}" y="{y}" width="{sw}" height="{h * .78:.0f}" fill="{color}"/>')
    return "".join(out)


def noise(x0, y0, w, h, n=900, color="#dfe8df", op=0.18):
    return "".join(f'<rect x="{r.randint(x0, x0 + w)}" y="{r.randint(y0, y0 + h)}" width="{r.choice([2, 3, 4])}" height="2" fill="{color}" opacity="{r.uniform(.05, op):.2f}"/>' for _ in range(n))


def scan(x0, y0, w, h):
    return f'<g opacity="0.18">{"".join(f"<rect x=\"{x0}\" y=\"{y}\" width=\"{w}\" height=\"2\" fill=\"#000\"/>" for y in range(y0, y0 + h, 6))}</g>'


SX, SY, SW, SH = 600, 190, 720, 600   # monitor screen rect


def monitor(content, glow_op=0.14, rec=True):
    return svg(f'''
<rect width="{W}" height="{H}" fill="#08070a"/>
<rect x="0" y="820" width="{W}" height="260" fill="#16100d"/>
<g stroke="#0d0907" stroke-width="3">{''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in (870, 940, 1030))}</g>
<rect x="{SX - 60}" y="{SY - 70}" width="{SW + 120}" height="{SH + 200}" rx="46" fill="#d9d6cf"/>
<rect x="{SX - 60}" y="{SY - 70}" width="{SW + 120}" height="{SH + 200}" rx="46" fill="#000" opacity="0.55"/>
<rect x="{SX + SW - 30}" y="{SY - 150}" width="26" height="100" rx="12" fill="#5a5852"/>
<g clip-path="url(#scr)">
<rect x="{SX}" y="{SY}" width="{SW}" height="{SH}" fill="#1c241f"/>
{content}
{noise(SX, SY, SW, SH)}
{scan(SX, SY, SW, SH)}
<rect x="{SX}" y="{SY}" width="{SW}" height="{SH}" fill="url(#scrv)"/>
</g>
{'<circle cx="%d" cy="%d" r="9" fill="#ff3b2f"/><text x="%d" y="%d" font-family="%s" font-size="30" fill="#ff3b2f">REC</text>' % (SX + 40, SY + 40, SX + 60, SY + 51, MONO) if rec else ''}
<text x="{SX + SW - 30}" y="{SY + SH - 30}" text-anchor="end" font-family="{MONO}" font-size="28" fill="#cfe0cf" opacity="0.8">11:07 PM</text>
<circle cx="{SX + SW / 2:.0f}" cy="{SY + SH + 70}" r="26" fill="#3a3834"/>
<circle cx="{SX + 120}" cy="{SY + SH + 70}" r="8" fill="#4dff88"/>
<rect x="{SX - 60}" y="{SY - 70}" width="{SW + 120}" height="{SH + 200}" fill="#b8d4c0" opacity="{glow_op}" filter="url(#blur60)"/>
''', f'''<clipPath id="scr"><rect x="{SX}" y="{SY}" width="{SW}" height="{SH}" rx="8"/></clipPath>
<radialGradient id="scrv" cx="0.5" cy="0.5" r="0.7"><stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.75"/></radialGradient>''')


# S1 — the house in the rain, the parents' car pulling away
save("s1", svg(f'''
<rect width="{W}" height="{H}" fill="url(#skyR)"/>
<ellipse cx="960" cy="200" rx="900" ry="160" fill="#4a5470" opacity="0.25" filter="url(#blur60)"/>
{dead_tree(470, 760, 420, "#07080e")}
<g fill="#0a0a12">
<polygon points="640,430 960,250 1280,430"/>
<rect x="680" y="430" width="560" height="360"/>
<rect x="1130" y="250" width="50" height="120"/>
<polygon points="1240,560 1240,790 1460,790 1460,560 1350,500"/>
</g>
{lit_window(910, 330, 100, 80, color="#ffcf8a")}
<circle cx="960" cy="370" r="120" fill="#ffcf8a" opacity="0.10" filter="url(#blur30)"/>
{lit_window(730, 500, 110, 110, color="#ffb54a")}
<rect x="725" y="650" width="160" height="10" fill="#14121a"/>
<rect x="930" y="620" width="80" height="170" fill="#16131a"/><circle cx="995" cy="705" r="5" fill="#a7853f"/>
{lit_window(1080, 500, 110, 110, color="#ffb54a")}
<path d="M0 790 H{W} V1080 H0Z" fill="#11121a"/>
<polygon points="930,790 1010,790 1150,1080 790,1080" fill="#1d1d26"/>
<g transform="translate(1250 800)">
<path d="M0 90 L20 40 C40 10 70 0 120 0 L250 0 C300 0 320 20 340 50 L380 60 C400 64 410 80 410 100 L410 130 L0 130Z" fill="#06060a"/>
<circle cx="80" cy="130" r="36" fill="#030305"/><circle cx="320" cy="130" r="36" fill="#030305"/>
<rect x="395" y="78" width="18" height="20" rx="4" fill="#ff2a1f"/>
</g>
<circle cx="1655" cy="888" r="40" fill="#ff2a1f" opacity="0.5" filter="url(#blur30)"/>
<polygon points="1660,960 1900,1080 1640,1080" fill="#ff2a1f" opacity="0.10"/>
{rain(300)}
{fog(800, op=0.12, ry=70)}
''', sky("skyR", "#05060c", "#151a2a", "#262b3c")))

# S2 — the nursery: one crib, one camera on the shelf
save("s2", svg(f'''
<rect width="{W}" height="{H}" fill="#120f15"/>
<rect x="0" y="0" width="{W}" height="760" fill="url(#wallN)"/>
<g opacity="0.08" fill="#e8d9c0">{''.join(f'<circle cx="{x}" cy="{y}" r="7"/>' for x in range(40, W, 120) for y in range(60, 760, 120))}</g>
<rect x="0" y="760" width="{W}" height="320" fill="#1b1512"/>
<rect x="1180" y="160" width="300" height="300" fill="#141a2a"/>
<rect x="1180" y="160" width="300" height="300" fill="none" stroke="#0a080c" stroke-width="14"/>
<line x1="1330" y1="160" x2="1330" y2="460" stroke="#0a080c" stroke-width="10"/>
{rain(60, 0.4).replace('<line', '<line clip-path="url(#win)"')}
<rect x="560" y="250" width="300" height="16" fill="#0c0a0c"/>
<g transform="translate(700 205)"><rect x="-30" y="0" width="60" height="44" rx="10" fill="#d0ccc4"/><circle cx="0" cy="22" r="14" fill="#1a1a1e"/><circle cx="0" cy="22" r="6" fill="#3b4a6a"/><circle cx="20" cy="8" r="4" fill="#ff3b2f"/></g>
<circle cx="720" cy="213" r="16" fill="#ff3b2f" opacity="0.6" filter="url(#blur8)"/>
<g stroke="#0c0a0c" stroke-width="3"><line x1="960" y1="0" x2="960" y2="330"/></g>
<g fill="#0c0a0c"><path d="M880 330 H1040 L1020 345 H900Z"/><circle cx="900" cy="400" r="18"/><circle cx="960" cy="420" r="18"/><circle cx="1020" cy="400" r="18"/></g>
<g stroke="#0c0a0c" stroke-width="2">{''.join(f'<line x1="{x}" y1="345" x2="{x}" y2="{y}"/>' for x, y in ((900, 382), (960, 402), (1020, 382)))}</g>
{crib(700, 560, 520, 300, "#0a080b", sw=8, bars=11)}
<path d="M720 790 H1200 V840 H720Z" fill="#0a080b"/>
<ellipse cx="960" cy="560" rx="380" ry="60" fill="#e8b878" opacity="0.06" filter="url(#blur30)"/>
<g transform="translate(560 740)"><rect x="-14" y="-10" width="28" height="30" rx="6" fill="#ffcf8a"/></g>
{glow(560, 740, 90, "#ffcf8a", 0.5)}
<polygon points="560,750 960,1080 160,1080" fill="#ffcf8a" opacity="0.05"/>
''', '''<linearGradient id="wallN" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#151320"/><stop offset="1" stop-color="#2a2230"/></linearGradient>
<clipPath id="win"><rect x="1187" y="167" width="286" height="286"/></clipPath>'''))

# S3 / S3b — the monitor: one crib, then two
room_bg = f'''<rect x="{SX}" y="{SY}" width="{SW}" height="{SH}" fill="#2b3530"/>
<rect x="{SX}" y="{SY + 420}" width="{SW}" height="200" fill="#1f2723"/>
<rect x="{SX + 520}" y="{SY + 60}" width="150" height="150" fill="#3c4a42"/>'''
c1 = crib(SX + 90, SY + 260, 260, 170, "#0f1411", sw=5, bars=8)
c2 = crib(SX + 400, SY + 260, 260, 170, "#0f1411", sw=5, bars=8)
baby = f'<ellipse cx="{SX + 220}" cy="{SY + 380}" rx="60" ry="22" fill="#56645b"/>'
save("s3", monitor(room_bg + baby + c1))
thing = (f'<g fill="#050706"><ellipse cx="{SX + 530}" cy="{SY + 140}" rx="30" ry="40"/>'
         f'<path d="M{SX + 500} {SY + 400} C{SX + 490} {SY + 300} {SX + 495} {SY + 210} {SX + 530} {SY + 185} C{SX + 565} {SY + 210} {SX + 570} {SY + 300} {SX + 560} {SY + 400}Z"/></g>')
save("s3b", monitor(room_bg + baby + c1 + thing + c2 + eyes(SX + 530, SY + 138, gap=22, r=4, color="#e8fff0")))

# S4 — close on the second crib
big = (f'<rect x="{SX}" y="{SY}" width="{SW}" height="{SH}" fill="#26302b"/>'
       f'<rect x="{SX}" y="{SY + 470}" width="{SW}" height="200" fill="#1a211d"/>'
       f'<g fill="#040605"><ellipse cx="{SX + 360}" cy="{SY + 110}" rx="52" ry="68"/>'
       f'<path d="M{SX + 300} {SY + 560} C{SX + 280} {SY + 380} {SX + 300} {SY + 230} {SX + 360} {SY + 180} C{SX + 420} {SY + 230} {SX + 440} {SY + 380} {SX + 420} {SY + 560}Z"/>'
       f'<path d="M{SX + 320} {SY + 230} C{SX + 260} {SY + 330} {SX + 250} {SY + 380} {SX + 210} {SY + 420}" stroke="#040605" stroke-width="16" fill="none" stroke-linecap="round"/>'
       f'<path d="M{SX + 400} {SY + 230} C{SX + 460} {SY + 330} {SX + 470} {SY + 380} {SX + 510} {SY + 420}" stroke="#040605" stroke-width="16" fill="none" stroke-linecap="round"/></g>'
       + eyes(SX + 360, SY + 105, gap=34, r=6, color="#e8fff0")
       + crib(SX + 40, SY + 360, 640, 260, "#0c110e", sw=10, bars=9))
save("s4", monitor(big, glow_op=0.2))

# S5 — the phone ringing out on the coffee table
save("s5", svg(f'''
<rect width="{W}" height="{H}" fill="#0a080a"/>
<rect x="0" y="600" width="{W}" height="480" fill="#24180f"/>
<g stroke="#1a110b" stroke-width="3" opacity="0.8">{''.join(f'<path d="M0 {y} C600 {y - 10} 1300 {y + 10} {W} {y}" fill="none"/>' for y in range(640, 1080, 46))}</g>
<g transform="rotate(-12 960 760)">
<rect x="840" y="520" width="240" height="470" rx="34" fill="#050506"/>
<rect x="852" y="534" width="216" height="442" rx="26" fill="url(#ph)"/>
<circle cx="960" cy="660" r="54" fill="#cfd6e4" opacity="0.85"/>
<circle cx="960" cy="645" r="20" fill="#5c6478"/><path d="M925 690 C930 665 990 665 995 690Z" fill="#5c6478"/>
<rect x="890" y="740" width="140" height="16" rx="8" fill="#e6ebf5" opacity="0.8"/>
<rect x="910" y="770" width="100" height="10" rx="5" fill="#e6ebf5" opacity="0.5"/>
<circle cx="910" cy="900" r="30" fill="#e0443a"/><circle cx="1010" cy="900" r="30" fill="#3ac46a"/>
</g>
<circle cx="960" cy="760" r="330" fill="#9fb6e6" opacity="0.16" filter="url(#blur60)"/>
<g fill="none" stroke="#cfe0ff" stroke-width="4" opacity="0.35">
<path d="M1120 600 C1160 640 1160 700 1120 740"/><path d="M1160 570 C1220 630 1220 710 1160 770"/>
<path d="M800 600 C760 640 760 700 800 740"/><path d="M760 570 C700 630 700 710 760 770"/></g>
<g transform="translate(1290 560)"><path d="M0 0 h110 l-10 140 h-90z" fill="#3a2c22"/><ellipse cx="55" cy="0" rx="55" ry="12" fill="#1a120c"/></g>
''', '''<linearGradient id="ph" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a3a64"/><stop offset="1" stop-color="#121a30"/></linearGradient>'''))

# S6 — me on the couch, lit by the monitor, staying downstairs
save("s6", svg(f'''
<rect width="{W}" height="{H}" fill="#1c1a24"/>
<ellipse cx="960" cy="420" rx="520" ry="380" fill="#2c3a36" opacity="0.6" filter="url(#blur60)"/>
<rect x="1240" y="120" width="380" height="440" fill="#121827"/>
{rain(90, 0.35).replace('<line', '<line clip-path="url(#w6)"')}
<rect x="1240" y="120" width="380" height="440" fill="none" stroke="#060508" stroke-width="18"/>
<line x1="1430" y1="120" x2="1430" y2="560" stroke="#060508" stroke-width="12"/>
<g fill="#060508"><rect x="420" y="300" width="14" height="420"/><path d="M360 300 h134 l-30 -110 h-74z" fill="#2a2018"/></g>
<rect x="0" y="820" width="{W}" height="260" fill="#120d0b"/>
<g fill="#050407">
<rect x="520" y="620" width="880" height="230" rx="40"/>
<rect x="470" y="560" width="110" height="300" rx="40"/><rect x="1340" y="560" width="110" height="300" rx="40"/>
<rect x="560" y="520" width="800" height="200" rx="50"/>
</g>
<g fill="#020203">
<circle cx="960" cy="420" r="62"/>
<path d="M880 470 C900 450 1020 450 1040 470 L1080 620 H840Z"/>
<path d="M900 400 C880 330 1040 330 1020 400 C1010 360 920 360 900 400Z" fill="#0a0809"/>
</g>
<circle cx="960" cy="470" r="230" fill="#b8d4c0" opacity="0.18" filter="url(#blur60)"/>
<g fill="none" stroke="#9fc4ae" stroke-width="5" opacity="0.55" stroke-linecap="round">
<path d="M1010 372 C1030 390 1026 440 1010 462"/></g>
<path d="M902 430 C920 388 1000 388 1018 430" fill="none" stroke="#b8d4c0" stroke-width="5" opacity="0.5"/>
<g transform="translate(1040 400)"><rect x="-6" y="0" width="70" height="56" rx="10" fill="#cfe7d6" opacity="0.9"/></g>
{glow(1075, 428, 70, "#cfe7d6", 0.55)}
''', '<clipPath id="w6"><rect x="1240" y="120" width="380" height="440"/></clipPath>'))

# S7 / S7b — the "nursery" on the monitor is the living room: couch, me, and the crib behind it
lr = (f'<rect x="{SX}" y="{SY}" width="{SW}" height="{SH}" fill="#28312c"/>'
      f'<rect x="{SX + 470}" y="{SY + 40}" width="170" height="200" fill="#3d4b43"/>'
      f'<line x1="{SX + 555}" y1="{SY + 40}" x2="{SX + 555}" y2="{SY + 240}" stroke="#141a16" stroke-width="8"/>'
      f'<rect x="{SX + 80}" y="{SY + 120}" width="8" height="240" fill="#121713"/><path d="M{SX + 50} {SY + 120} h70 l-15 -60 h-40z" fill="#4a554e"/>'
      f'<rect x="{SX}" y="{SY + 470}" width="{SW}" height="200" fill="#1c2420"/>')
couch = (f'<g fill="#0b0f0d"><rect x="{SX + 150}" y="{SY + 380}" width="430" height="130" rx="20"/>'
         f'<rect x="{SX + 170}" y="{SY + 320}" width="390" height="100" rx="26"/>'
         f'<circle cx="{SX + 365}" cy="{SY + 290}" r="34" fill="#070a08"/><path d="M{SX + 320} {SY + 330} h90 l20 70 h-130z" fill="#070a08"/></g>'
         f'<rect x="{SX + 400}" y="{SY + 300}" width="34" height="26" rx="5" fill="#d8f0e0" opacity="0.8"/>')
crib7 = crib(SX + 200, SY + 210, 330, 170, "#0f1411", sw=5, bars=9)
it = (f'<g fill="#030504"><ellipse cx="{SX + 300}" cy="{SY + 120}" rx="26" ry="34"/>'
      f'<path d="M{SX + 275} {SY + 330} C{SX + 268} {SY + 240} {SX + 272} {SY + 175} {SX + 300} {SY + 152} C{SX + 328} {SY + 175} {SX + 332} {SY + 240} {SX + 325} {SY + 330}Z"/></g>'
      + eyes(SX + 300, SY + 118, gap=18, r=3.5, color="#e8fff0"))
save("s7", monitor(lr + it + crib7 + couch, glow_op=0.18))
save("s7b", monitor(lr + crib7 + couch, glow_op=0.18))
print("drew scenes")
