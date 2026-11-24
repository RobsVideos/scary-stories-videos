"""The Extra Plate - scenes (1920x1080 viewBox)."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *
import math

TX0, TX1 = 380, 1380          # table left/right ends
END = 1440                    # head-of-table chair x

def room(wall_top, wall_bot, floor, night="#0b1020", moonlit=True, clock_hand=-5, light="#ffb54a", light_op=0.18):
    defs = sky("wall", wall_top, wall_top, wall_bot) + sky("win", "#04060e", night, "#1a2036")
    paper = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="780" stroke="#000" stroke-width="2" opacity="0.18"/>' for x in range(0, 1920, 48))
    dots = "".join(f'<circle cx="{x+24}" cy="{y}" r="4" fill="#000" opacity="0.15"/>' for x in range(0, 1920, 48) for y in range(40, 760, 80))
    boards = "".join(f'<line x1="{x}" y1="800" x2="{960 + (x-960)*1.8:.0f}" y2="1080" stroke="#000" stroke-width="3" opacity="0.35"/>' for x in range(-400, 2400, 120))
    ang = clock_hand * 6
    body = f'''
<rect width="{W}" height="{H}" fill="url(#wall)"/>{paper}{dots}
<rect x="0" y="560" width="{W}" height="220" fill="#000" opacity="0.22"/>
<line x1="0" y1="560" x2="{W}" y2="560" stroke="#000" stroke-width="6" opacity="0.4"/>
<rect x="840" y="150" width="240" height="270" fill="url(#win)"/>
{stars(40, 0) if False else ''}
{('<circle cx="1010" cy="215" r="26" fill="#e9e3cf" opacity="0.85"/><circle cx="1010" cy="215" r="60" fill="#e9e3cf" opacity="0.15" filter="url(#blur30)"/>' if moonlit else '')}
<path d="M840 380 L900 330 L940 360 L1000 300 L1080 370 L1080 420 L840 420Z" fill="#05070c" opacity="0.9"/>
<rect x="840" y="150" width="240" height="270" fill="none" stroke="#120a08" stroke-width="16"/>
<line x1="960" y1="150" x2="960" y2="420" stroke="#120a08" stroke-width="9"/>
<line x1="840" y1="285" x2="1080" y2="285" stroke="#120a08" stroke-width="9"/>
<rect x="822" y="418" width="276" height="16" fill="#120a08"/>
<path d="M800 130 Q820 300 790 470 L830 470 Q850 300 840 140Z" fill="#3a1414" opacity="0.9"/>
<path d="M1120 130 Q1100 300 1130 470 L1090 470 Q1070 300 1080 140Z" fill="#3a1414" opacity="0.9"/>
<rect x="780" y="122" width="360" height="12" rx="6" fill="#120a08"/>
<g transform="translate(1270 250)"><circle r="58" fill="#120a08"/><circle r="48" fill="#d9cdb0" opacity="0.85"/>
<g stroke="#120a08" stroke-width="3">{''.join(f'<line x1="{math.sin(math.radians(a))*40:.1f}" y1="{-math.cos(math.radians(a))*40:.1f}" x2="{math.sin(math.radians(a))*45:.1f}" y2="{-math.cos(math.radians(a))*45:.1f}"/>' for a in range(0,360,30))}</g>
<line x1="0" y1="0" x2="0" y2="-38" stroke="#120a08" stroke-width="5" transform="rotate({ang})"/>
<line x1="0" y1="0" x2="0" y2="-26" stroke="#120a08" stroke-width="7" transform="rotate(-2)"/><circle r="5" fill="#120a08"/></g>
<g transform="translate(600 210)"><rect x="-70" y="-90" width="140" height="180" fill="#120a08"/><rect x="-56" y="-76" width="112" height="152" fill="#2b2420"/>
<ellipse cx="0" cy="-12" rx="26" ry="32" fill="#14100e"/><circle cx="0" cy="-48" r="16" fill="#14100e"/><path d="M-46 76 C-40 30 40 30 46 76Z" fill="#14100e"/></g>
<rect x="0" y="780" width="{W}" height="22" fill="#0e0807"/>
<rect x="0" y="800" width="{W}" height="280" fill="{floor}"/>
<g clip-path="url(#flr)">{boards}</g>
<ellipse cx="900" cy="560" rx="700" ry="300" fill="{light}" opacity="{light_op}" filter="url(#blur60)"/>'''
    defs += '<clipPath id="flr"><rect x="0" y="800" width="1920" height="280"/></clipPath>'
    return body, defs

def person(x, base=610, h=200, color="#0a0607", kind="adult"):
    hr = h * (0.13 if kind != "child" else 0.15)
    sw = h * (0.26 if kind != "child" else 0.2)
    head_y = base - h + hr
    hair = ""
    if kind == "bun": hair = f'<circle cx="{x}" cy="{head_y - hr*1.05:.0f}" r="{hr*0.5:.0f}" fill="{color}"/>'
    if kind == "long": hair = f'<path d="M{x-hr*1.05:.0f} {head_y:.0f} Q{x-hr*1.3:.0f} {head_y+hr*2.2:.0f} {x-hr*0.6:.0f} {head_y+hr*2.4:.0f} L{x+hr*0.6:.0f} {head_y+hr*2.4:.0f} Q{x+hr*1.3:.0f} {head_y+hr*2.2:.0f} {x+hr*1.05:.0f} {head_y:.0f}Z" fill="{color}"/>'
    return (f'<g fill="{color}">{hair}<circle cx="{x}" cy="{head_y:.0f}" r="{hr:.0f}"/>'
            f'<rect x="{x-hr*0.4:.0f}" y="{head_y+hr*0.8:.0f}" width="{hr*0.8:.0f}" height="{hr*0.6:.0f}"/>'
            f'<path d="M{x-sw:.0f} {base} C{x-sw:.0f} {head_y+hr*2.3:.0f} {x-sw*0.6:.0f} {head_y+hr*1.4:.0f} {x:.0f} {head_y+hr*1.4:.0f} C{x+sw*0.6:.0f} {head_y+hr*1.4:.0f} {x+sw:.0f} {head_y+hr*2.3:.0f} {x+sw:.0f} {base}Z"/></g>')

def chair_back(x, top=420, color="#160c09"):
    return f'<g fill="{color}"><rect x="{x-70}" y="{top}" width="12" height="200"/><rect x="{x+58}" y="{top}" width="12" height="200"/><path d="M{x-76} {top} Q{x} {top-30} {x+76} {top} L{x+76} {top+22} L{x-76} {top+22}Z"/></g>'

def end_chair(x=END, color="#1a0e0a", pulled=0, rot=0):
    cx = x + pulled
    return (f'<g transform="rotate({rot} {cx} 900)" fill="{color}">'
            f'<rect x="{cx-50}" y="700" width="110" height="18"/>'
            f'<rect x="{cx+46}" y="440" width="16" height="460"/><rect x="{cx+40}" y="440" width="28" height="14" rx="6"/>'
            f'<rect x="{cx+50}" y="480" width="6" height="220" fill="#000" opacity="0.4"/>'
            f'<rect x="{cx-46}" y="716" width="13" height="184"/>'
            f'<g stroke="{color}" stroke-width="6"><line x1="{cx+50}" y1="520" x2="{cx+50}" y2="690"/></g></g>')

def table(cloth="#5a2a1e", wood="#2a160d", bare_end=False):
    return f'''
<polygon points="{TX0+30},600 {TX1-30},600 {TX1},670 {TX0},670" fill="{wood}"/>
<polygon points="{TX0+30},600 {TX1-30},600 {TX1},670 {TX0},670" fill="#fff" opacity="0.04"/>
<polygon points="{TX0+60},604 {(TX1-280) if bare_end else TX1-60},604 {(TX1-262) if bare_end else TX1-40},666 {TX0+40},666" fill="{cloth}" opacity="0.9"/>
<rect x="{TX0}" y="670" width="{TX1-TX0}" height="34" fill="#1a0d07"/>
<rect x="{TX0}" y="670" width="{TX1-TX0}" height="4" fill="#4a2a18" opacity="0.6"/>
<g fill="#150a06"><rect x="{TX0+20}" y="700" width="26" height="200"/><rect x="{TX1-46}" y="700" width="26" height="200"/>
<rect x="{TX0+110}" y="700" width="18" height="160" opacity="0.6"/><rect x="{TX1-128}" y="700" width="18" height="160" opacity="0.6"/></g>
<ellipse cx="{(TX0+TX1)//2}" cy="905" rx="560" ry="22" fill="#000" opacity="0.45" filter="url(#blur8)"/>'''

def candle(x, y=640, lean=0, flame="#ffcf6a", glow_c="#ffb54a", gop=0.55, h=80):
    top = y - h
    return (f'{glow(x + lean*1.2, top-18, 70, glow_c, gop)}'
            f'<path d="M{x-18} {y} L{x+18} {y} L{x+8} {y-10} L{x-8} {y-10}Z" fill="#8a7a55"/>'
            f'<rect x="{x-7}" y="{top}" width="14" height="{h-10}" fill="#e8dcc0"/>'
            f'<g transform="rotate({lean} {x} {top})"><ellipse cx="{x}" cy="{top-14}" rx="7" ry="16" fill="{flame}"/>'
            f'<ellipse cx="{x}" cy="{top-10}" rx="3" ry="7" fill="#fff6dc"/></g>')

def plate(x, y=640, food=True, rx=46):
    f = ""
    if food:
        f = (f'<ellipse cx="{x-12}" cy="{y-5}" rx="18" ry="8" fill="#8a4a24"/><ellipse cx="{x+14}" cy="{y-4}" rx="14" ry="7" fill="#d9c49a"/>'
             f'<ellipse cx="{x+2}" cy="{y+4}" rx="12" ry="5" fill="#5a6a2a"/>')
    return f'<ellipse cx="{x}" cy="{y+3}" rx="{rx}" ry="{rx*0.28:.0f}" fill="#000" opacity="0.35"/><ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{rx*0.28:.0f}" fill="#e4dccb"/><ellipse cx="{x}" cy="{y}" rx="{rx*0.66:.0f}" ry="{rx*0.18:.0f}" fill="#cfc5b0"/>{f}'

def turkey(x, y=635):
    return (f'<ellipse cx="{x}" cy="{y+6}" rx="90" ry="22" fill="#cfc5b0"/>'
            f'<path d="M{x-60} {y} C{x-60} {y-60} {x+60} {y-60} {x+60} {y}Z" fill="#8a4a20"/>'
            f'<path d="M{x-40} {y-20} C{x-30} {y-45} {x+10} {y-48} {x+30} {y-30}" stroke="#b56a30" stroke-width="6" fill="none" opacity="0.7"/>'
            f'<path d="M{x+50} {y-14} l26 -18 l6 6 l-22 20z" fill="#7a3e1a"/>')

people_x = [520, 700, 1120, 1260]

# S1 - grandmother setting the extra plate
b, d = room("#3a1a14", "#24100c", "#1c0f0a", light_op=0.22)
s1 = b + "".join(chair_back(px) for px in people_x) + end_chair() + table() + \
    turkey(860) + plate(520) + plate(700) + plate(1120) + plate(1260) + plate(1340, food=False) + \
    candle(780) + candle(960) + candle(1050) + \
    person(1210, base=900, h=430, color="#0b0607", kind="bun") + \
    f'<path d="M1240 580 C1280 600 1300 620 1330 628" stroke="#0b0607" stroke-width="22" stroke-linecap="round" fill="none"/>' + \
    glow(1340, 640, 50, "#fff1cf", 0.35)
save("s1", svg(s1, d))

# S2 - family eating, bare end of the table
b, d = room("#3a1a14", "#24100c", "#1c0f0a", light_op=0.24)
fam = person(520, kind="adult") + person(700, kind="long") + person(1120, kind="adult", h=210) + person(1260, kind="child", h=150)
s2 = b + "".join(chair_back(px) for px in people_x) + fam + end_chair() + table(bare_end=True) + \
    turkey(880) + plate(520) + plate(700) + plate(1120) + plate(1260) + \
    candle(780) + candle(960) + candle(1040) + \
    f'<ellipse cx="1300" cy="640" rx="60" ry="16" fill="#000" opacity="0.25"/>'
save("s2", svg(s2, d))

# S3 - cold; candles lean toward the empty end; clock near midnight
b, d = room("#18202c", "#0e131c", "#0d1016", light="#7fa6d8", light_op=0.12, clock_hand=-2)
famc = "".join(person(x, kind=k, h=hh, color="#05070b") for x, k, hh in [(520, "adult", 200), (700, "long", 200), (1120, "adult", 210), (1260, "child", 150)])
s3 = b + "".join(chair_back(px, color="#0c1016") for px in people_x) + famc + end_chair(color="#0c0f15") + \
    table(cloth="#2a2630", wood="#141a22", bare_end=True) + turkey(880) + \
    plate(520) + plate(700) + plate(1120) + plate(1260) + \
    candle(780, lean=55, flame="#bcd6ff", glow_c="#7fa6d8", gop=0.45) + candle(960, lean=58, flame="#bcd6ff", glow_c="#7fa6d8", gop=0.45) + \
    candle(1040, lean=60, flame="#bcd6ff", glow_c="#7fa6d8", gop=0.45) + \
    "".join(f'<path d="M{x} 520 q40 -10 80 0" stroke="#bcd6ff" stroke-width="3" fill="none" opacity="0.35"/>' for x in (820, 1000)) + \
    fog(560, "#9ab4d8", 0.10, 200)
save("s3", svg(s3, d))

# S4 - the chair slides out; something sits in the dark
b, d = room("#121722", "#0a0d14", "#0b0d12", light="#6a8ac0", light_op=0.08, moonlit=False)
shape = (f'<g fill="#020203"><ellipse cx="{END+40}" cy="455" rx="34" ry="44"/>'
         f'<path d="M{END-20} 720 C{END-40} 600 {END-30} 520 {END+40} 505 C{END+110} 520 {END+120} 600 {END+110} 720Z"/>'
         f'<path d="M{END+0} 560 C{END-60} 600 {END-90} 630 {END-130} 650" stroke="#020203" stroke-width="20" stroke-linecap="round" fill="none"/>'
         f'<path d="M{END-10} 715 L{END-60} 730 L{END-60} 900" stroke="#020203" stroke-width="26" fill="none"/></g>')
s4 = b + f'<rect x="1500" y="250" width="260" height="530" fill="#010102"/><rect x="1490" y="240" width="280" height="14" fill="#0a0c12"/>' + \
    chair_back(1120, color="#0b0e14") + chair_back(1260, color="#0b0e14") + \
    end_chair(color="#0d1018", pulled=70, rot=6) + shape + eyes(END+28, 450, gap=22, r=4, color="#ff3b2f") + \
    table(cloth="#22222c", wood="#121820", bare_end=True) + plate(1120) + plate(1260) + \
    candle(1040, lean=70, flame="#9fbff0", glow_c="#6a8ac0", gop=0.35) + candle(960, lean=68, flame="#9fbff0", glow_c="#6a8ac0", gop=0.3) + \
    f'<path d="M{END+20} 905 l60 10" stroke="#3a4660" stroke-width="3" opacity="0.6"/><path d="M{END+20} 915 l70 6" stroke="#3a4660" stroke-width="2" opacity="0.5"/>' + \
    fog(760, "#8aa0c8", 0.08, 160)
save("s4", svg(s4, d))

# S5 - close-up: a fork tapping on the bare wood
grain = "".join(f'<path d="M0 {y} C500 {y+rnd.randint(-20,20)} 1400 {y+rnd.randint(-20,20)} 1920 {y}" stroke="#000" stroke-width="{rnd.choice([2,3,4])}" fill="none" opacity="0.3"/>' for y in range(560, 1080, 34))
s5 = f'''<rect width="{W}" height="{H}" fill="#06070b"/>
<rect x="0" y="520" width="{W}" height="560" fill="#2a1a10"/>{grain}
<rect x="0" y="520" width="{W}" height="560" fill="#6a8ac0" opacity="0.08"/>
<ellipse cx="960" cy="560" rx="900" ry="140" fill="#000" opacity="0.5" filter="url(#blur60)"/>
{glow(420, 380, 120, "#6a8ac0", 0.25)}<rect x="408" y="330" width="24" height="200" fill="#d9d2c0" opacity="0.7"/>
<ellipse cx="420" cy="316" rx="9" ry="20" fill="#9fbff0" transform="rotate(60 420 330)"/>
<g transform="translate(-135 -15)" fill="#030304" stroke="#4a5a80" stroke-width="3" stroke-opacity="0.7">
<path d="M1700 120 C1500 170 1300 260 1160 360 C1110 395 1080 420 1060 450 L1110 470 C1140 440 1180 420 1250 390 C1400 320 1560 260 1760 220Z"/>
<path d="M1060 450 C1040 470 1020 480 990 486 L995 500 C1030 496 1060 488 1090 470Z"/>
<path d="M1070 440 C1050 430 1030 430 1000 440 L1004 452 C1030 446 1050 448 1068 456Z"/>
<path d="M1080 462 C1070 490 1060 510 1050 530 L1062 534 C1074 514 1086 494 1096 470Z"/>
</g>
<g transform="rotate(-18 960 640)">
<rect x="955" y="420" width="12" height="160" rx="5" fill="#b8bcc6"/>
<path d="M944 580 L978 580 L976 640 L946 640Z" fill="#b8bcc6"/>
<g fill="#b8bcc6"><rect x="944" y="640" width="5" height="44"/><rect x="954" y="640" width="5" height="46"/><rect x="964" y="640" width="5" height="46"/><rect x="973" y="640" width="5" height="44"/></g>
</g>
<g stroke="#cfd6e8" stroke-width="4" fill="none" opacity="0.6" stroke-linecap="round">
<path d="M1000 720 q30 -6 50 -24"/><path d="M1010 742 q40 -2 66 -20"/><path d="M930 726 q-30 -8 -50 -26"/></g>
<ellipse cx="985" cy="712" rx="60" ry="10" fill="#9fbff0" opacity="0.2" filter="url(#blur8)"/>
{fog(600, "#8aa0c8", 0.06, 120)}'''
save("s5", svg(s5))

# S6 - I set down a filled plate in front of the dark
b, d = room("#1a1a22", "#100f15", "#0e0d10", light="#ffb54a", light_op=0.10, moonlit=False)
s6 = b + f'<rect x="1500" y="250" width="260" height="530" fill="#010102"/><rect x="1490" y="240" width="280" height="14" fill="#0a0c12"/>' + \
    chair_back(1120, color="#0e0f14") + person(1120, kind="adult", h=210, color="#050508") + chair_back(1260, color="#0e0f14") + person(1260, kind="child", h=150, color="#050508") + \
    end_chair(color="#0d1018", pulled=70, rot=6) + shape + \
    table(cloth="#2a2228", wood="#1a1612", bare_end=True) + plate(1120) + plate(1260) + plate(1330, y=634) + \
    candle(960, flame="#ffcf6a", glow_c="#ffb54a", gop=0.45) + candle(1040, flame="#ffcf6a", glow_c="#ffb54a", gop=0.45) + \
    f'<path d="M700 1080 C820 900 1000 760 1200 690 L1300 640 L1320 660 L1220 720 C1040 800 900 920 840 1080Z" fill="#050406"/>' + \
    f'<path d="M1280 636 l26 -8 l6 10 l-22 10z" fill="#050406"/>'
save("s6", svg(s6, d))

# S7 - morning: the plate is scraped clean, a note beneath
b, d = room("#4a4a50", "#2e2d33", "#2a2522", night="#8a96a8", moonlit=False, light="#c8d4e8", light_op=0.14)
s7 = b + chair_back(1120, color="#1e1a18") + chair_back(1260, color="#1e1a18") + end_chair(color="#241c16") + \
    table(cloth="#6a5048", wood="#3a2a1e", bare_end=True) + \
    f'<polygon points="840,420 1080,420 1300,670 700,670" fill="#e8eef8" opacity="0.10"/>' + \
    f'<polygon points="1300,652 1376,646 1384,664 1306,670" fill="#efe8d6"/><line x1="1310" y1="660" x2="1370" y2="655" stroke="#9a8f7a" stroke-width="2"/>' + \
    plate(1320, y=640, food=False) + \
    "".join(f'<path d="M{1300+i*9} {636 + (i%2)*3} l14 -2" stroke="#b8ad98" stroke-width="2"/>' for i in range(4)) + \
    f'<rect x="1225" y="636" width="70" height="5" rx="2" fill="#b8bcc6" transform="rotate(-8 1260 638)"/>' + \
    candle(960, h=40, flame="none", glow_c="#000", gop=0) + candle(1040, h=38, flame="none", glow_c="#000", gop=0)
save("s7", svg(s7, d))

# S8 - next year: two places at the end, two guests in the dark
b, d = room("#140c10", "#0a0609", "#0a0708", light="#c02a2a", light_op=0.10, moonlit=False, clock_hand=0)
gran = (f'<g fill="#2a2a36" opacity="0.9">'
        f'<circle cx="1250" cy="470" r="30"/><circle cx="1250" cy="436" r="15"/>'
        f'<path d="M1200 620 C1200 540 1220 505 1250 505 C1280 505 1300 540 1300 620Z"/></g>'
        f'<g fill="#8fa0c0" opacity="0.5"><circle cx="1240" cy="468" r="3"/><circle cx="1260" cy="468" r="3"/></g>')
s8 = b + f'<rect x="1500" y="250" width="260" height="530" fill="#010102"/><rect x="1490" y="240" width="280" height="14" fill="#0a0c12"/>' + \
    chair_back(1250, color="#120a0c") + gran + glow(1250, 480, 110, "#8fa0c0", 0.22) + \
    end_chair(color="#140c0e", pulled=70, rot=6) + shape + eyes(END+28, 450, gap=22, r=5) + \
    table(cloth="#3a1418", wood="#1a0e0c") + plate(1250, food=False) + plate(1330, y=636, food=False) + \
    candle(900, lean=0, flame="#ff6a4a", glow_c="#c02a2a", gop=0.5) + candle(1060, lean=0, flame="#ff6a4a", glow_c="#c02a2a", gop=0.5) + \
    fog(780, "#6a5060", 0.08, 160)
save("s8", svg(s8, d))
