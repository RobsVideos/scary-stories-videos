"""Scenes for Fitting Room Six."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

RED = "#ff2a22"
WARM = "#ffb54a"
PALE = "#cfd6e6"
DARK = "#07060c"


def tiles(y0, color="#14121c", line="#0a0910", vp=960, n=18, rows=(0,)):
    """Perspective floor from y0 down to the bottom."""
    o = [f'<rect x="0" y="{y0}" width="{W}" height="{H - y0}" fill="{color}"/>']
    for k in range(-n, n + 1):
        x = vp + k * 260
        o.append(f'<line x1="{vp + k * 40}" y1="{y0}" x2="{x}" y2="{H}" stroke="{line}" stroke-width="3"/>')
    y, step = y0 + 14, 18
    while y < H:
        o.append(f'<line x1="0" y1="{y:.0f}" x2="{W}" y2="{y:.0f}" stroke="{line}" stroke-width="3"/>')
        step *= 1.35; y += step
    return "".join(o)


def door(cx, top, bot, w, num, closed=True, ind=None, gap_light=None, fill="#2a2430", frame="#120f16", right=False):
    x = cx - w / 2
    o = [f'<rect x="{x - 14}" y="{top - 14}" width="{w + 28}" height="{bot - top + 14}" fill="{frame}"/>']
    if closed:
        o.append(f'<rect x="{x}" y="{top}" width="{w}" height="{bot - top - 22}" fill="{fill}"/>')
        o.append("".join(f'<line x1="{x + 24}" y1="{yy}" x2="{x + w - 24}" y2="{yy}" stroke="#16121a" stroke-width="5"/>'
                         for yy in range(int(top) + 60, int(top) + 260, 18)))
        o.append(f'<rect x="{x + 24}" y="{top + 300}" width="{w - 48}" height="{bot - top - 360}" fill="none" stroke="#16121a" stroke-width="5"/>')
        o.append(f'<rect x="{cx - 26}" y="{top + 18}" width="52" height="36" rx="5" fill="#8a7444"/>'
                 f'<text x="{cx}" y="{top + 47}" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="30" fill="#1a1408">{num}</text>')
        o.append(f'<circle cx="{x + w - 26}" cy="{(top + bot) / 2 + 20}" r="9" fill="#9c8650"/>')
        if ind:
            o.append(f'<rect x="{x + w - 42}" y="{(top + bot) / 2 - 22}" width="32" height="16" rx="4" fill="{ind}"/>'
                     f'<circle cx="{x + w - 26}" cy="{(top + bot) / 2 - 14}" r="30" fill="{ind}" opacity="0.6" filter="url(#blur8)"/>')
        gl = gap_light or "#05040a"
        o.append(f'<rect x="{x}" y="{bot - 22}" width="{w}" height="22" fill="{gl}"/>')
        if gap_light:
            o.append(f'<rect x="{x}" y="{bot - 22}" width="{w}" height="22" fill="{gl}" filter="url(#blur8)"/>')
    else:
        o.append(f'<rect x="{x}" y="{top}" width="{w}" height="{bot - top}" fill="#0a0910"/>')
        # mirror at back
        o.append(f'<rect x="{cx - w * .28}" y="{top + 60}" width="{w * .56}" height="{bot - top - 120}" fill="#1c2230"/>'
                 f'<line x1="{cx - w * .2}" y1="{top + 120}" x2="{cx - w * .05}" y2="{top + 40 + (bot - top) * .4}" stroke="#3a4458" stroke-width="5"/>')
        o.append(f'<rect x="{cx - w * .4}" y="{bot - 110}" width="{w * .8}" height="16" fill="#18141c"/>')  # bench
        # door swung outward toward us
        if right:
            xr = x + w
            o.append(f'<polygon points="{xr},{top} {xr + w * .45},{top - 30} {xr + w * .45},{bot + 30} {xr},{bot}" fill="{fill}"/>')
        else:
            o.append(f'<polygon points="{x},{top} {x - w * .45},{top - 30} {x - w * .45},{bot + 30} {x},{bot}" fill="{fill}"/>'
                     f'<rect x="{x - w * .45 + 8}" y="{top + 10}" width="22" height="30" fill="#8a7444" opacity="0.6"/>')
        o.append(f'<rect x="{cx - 26}" y="{top - 60}" width="52" height="36" rx="5" fill="#6d5c38"/>'
                 f'<text x="{cx}" y="{top - 31}" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="30" fill="#1a1408">{num}</text>')
    return "".join(o)


def sneaker_front(cx, base, s=1.0, lace="#f2f2f2", body="#e8e6e0"):
    """A white sneaker seen from the front (toe toward viewer)."""
    g = [f'<g transform="translate({cx} {base}) scale({s})">']
    g.append(f'<path d="M-70 0 L-74 -18 C-74 -70 -40 -96 0 -96 C40 -96 74 -70 74 -18 L70 0Z" fill="{body}"/>')
    g.append('<path d="M-76 0 L-76 -20 L76 -20 L76 0Z" fill="#cfcac0"/>')
    g.append('<path d="M-60 -22 C-40 -40 40 -40 60 -22" stroke="#a9a49a" stroke-width="4" fill="none"/>')
    g.append('<path d="M-30 -96 L-26 -60 L26 -60 L30 -96" fill="#d8d4cc"/>')
    for k in range(3):
        yy = -88 + k * 10
        g.append(f'<line x1="-24" y1="{yy}" x2="24" y2="{yy + 6}" stroke="{lace}" stroke-width="5"/>'
                 f'<line x1="24" y1="{yy}" x2="-24" y2="{yy + 6}" stroke="{lace}" stroke-width="5"/>')
    g.append('<path d="M-60 -10 L-40 -6 M60 -10 L40 -6" stroke="#8d887e" stroke-width="3"/>')  # scuffs
    g.append('</g>')
    return "".join(g)


def rack(x, y, w, color="#0c0a10", n=9):
    o = [f'<line x1="{x}" y1="{y}" x2="{x + w}" y2="{y}" stroke="{color}" stroke-width="6"/>'
         f'<line x1="{x + 10}" y1="{y}" x2="{x + 10}" y2="{y + 260}" stroke="{color}" stroke-width="6"/>'
         f'<line x1="{x + w - 10}" y1="{y}" x2="{x + w - 10}" y2="{y + 260}" stroke="{color}" stroke-width="6"/>']
    for k in range(n):
        cx = x + 20 + k * (w - 40) / (n - 1)
        o.append(f'<path d="M{cx - 30} {y + 22} L{cx} {y + 8} L{cx + 30} {y + 22} L{cx + 26} {y + 150} L{cx - 26} {y + 150}Z" fill="{color}"/>')
    return "".join(o)


def kneeler(cx, base, h=330, color="#040306"):
    """A person kneeling, seen from behind, head bowed toward the floor."""
    return (f'<g fill="{color}">'
            f'<path d="M{cx - 90} {base} C{cx - 100} {base - 60} {cx - 70} {base - 110} {cx - 30} {base - 120} L{cx + 60} {base - 120} '
            f'C{cx + 110} {base - 110} {cx + 120} {base - 60} {cx + 110} {base}Z"/>'
            f'<path d="M{cx - 60} {base - 110} C{cx - 70} {base - h * .55} {cx - 20} {base - h * .78} {cx + 40} {base - h * .78} '
            f'C{cx + 100} {base - h * .78} {cx + 120} {base - h * .6} {cx + 90} {base - 110}Z"/>'
            f'<ellipse cx="{cx + 70}" cy="{base - h * .7}" rx="46" ry="52"/>'
            f'<path d="M{cx + 70} {base - h * .62} L{cx + 130} {base - 30}" stroke="{color}" stroke-width="30" stroke-linecap="round"/>'
            f'</g>')


def walker(cx, base, h=170, color="#030205"):
    hw = h * .12
    return (f'<g fill="{color}"><ellipse cx="{cx}" cy="{base - h * .9}" rx="{h * .07}" ry="{h * .085}"/>'
            f'<path d="M{cx - hw} {base - h * .82} L{cx + hw} {base - h * .82} L{cx + hw * .9} {base - h * .45} L{cx - hw * .9} {base - h * .45}Z"/>'
            f'<path d="M{cx - hw * .6} {base - h * .46} L{cx - hw * 1.1} {base - 8} M{cx + hw * .6} {base - h * .46} L{cx + hw * 1.2} {base - 14}" '
            f'stroke="{color}" stroke-width="{h * .08}" stroke-linecap="round"/></g>'
            f'<ellipse cx="{cx - hw * 1.1}" cy="{base - 4}" rx="12" ry="6" fill="#e8e6e0"/>'
            f'<ellipse cx="{cx + hw * 1.2}" cy="{base - 10}" rx="12" ry="6" fill="#e8e6e0"/>')


# S1 — storefront in the dark mall, gate half down
gate = "".join(f'<line x1="{x}" y1="250" x2="{x}" y2="520" stroke="#3a3644" stroke-width="4"/>' for x in range(580, 1360, 22))
gate += "".join(f'<line x1="570" y1="{y}" x2="1350" y2="{y}" stroke="#2a2732" stroke-width="3"/>' for y in range(260, 521, 26))
mannequin = ('<g fill="#08070b"><ellipse cx="1180" cy="560" rx="26" ry="32"/><rect x="1172" y="588" width="16" height="20"/>'
             '<path d="M1130 610 L1230 610 L1218 700 L1200 790 L1160 790 L1142 700Z"/><rect x="1176" y="790" width="8" height="40"/>'
             '<rect x="1140" y="828" width="80" height="8"/></g>')
s1 = f'''
<rect width="{W}" height="{H}" fill="#0a0910"/>
<polygon points="0,0 1920,0 1920,140 0,140" fill="#06050a"/>
<g fill="#0e0c15">{''.join(f'<rect x="{x}" y="40" width="160" height="70" rx="6"/>' for x in range(100, 1900, 260))}</g>
<rect x="0" y="140" width="{W}" height="20" fill="#14121c"/>
{tiles(860, "#100e17", "#08070c")}
<rect x="80" y="240" width="380" height="600" fill="#09080e"/><rect x="1460" y="240" width="380" height="600" fill="#09080e"/>
<rect x="540" y="180" width="840" height="56" fill="#16131c"/>
<rect x="760" y="192" width="400" height="32" rx="6" fill="#2a2430"/>
<rect x="560" y="240" width="800" height="600" fill="url(#shop)"/>
{rack(620, 560, 260, "#1a1218")}
{mannequin}
<rect x="900" y="470" width="120" height="14" fill="#ffd9a0" opacity="0.7"/>
{gate}
<rect x="560" y="512" width="800" height="16" fill="#4a4554"/>
<rect x="540" y="236" width="20" height="604" fill="#16131c"/><rect x="1360" y="236" width="20" height="604" fill="#16131c"/>
<polygon points="560,840 1360,840 1560,1080 360,1080" fill="{WARM}" opacity="0.10"/>
{glow(960, 560, 320, WARM, 0.12)}
<rect x="1600" y="280" width="90" height="34" rx="4" fill="#5a0e0c"/><text x="1645" y="306" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="24" fill="{RED}">EXIT</text>
{glow(1645, 297, 70, RED, 0.35)}
{fog(860, "#6a6478", 0.10, 80)}
'''
save("s1", svg(s1, '<linearGradient id="shop" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a3424"/><stop offset="1" stop-color="#22170f"/></linearGradient>'))


# S2 / S3 — the fitting room row (doors open / door six locked)
def row(six_closed, light):
    base = f'''
<rect width="{W}" height="{H}" fill="{'#1a1720' if light else '#0c0b11'}"/>
<rect x="0" y="0" width="{W}" height="200" fill="#08070c"/>
{''.join(f'<rect x="{x}" y="70" width="200" height="22" rx="4" fill="{"#e6ecf5" if light else "#1a1a22"}"/>' for x in (420, 860, 1300))}
{''.join(glow(x + 100, 90, 120, "#dfe8ff", 0.25) for x in (420, 860, 1300)) if light else ''}
{tiles(880, "#17141d" if light else "#0e0c13", "#0a090e")}
{door(440, 300, 880, 230, 4, closed=False)}
{door(700, 300, 880, 230, 5, closed=False)}
{door(960, 300, 880, 230, 6, closed=six_closed, ind=RED if six_closed else None, gap_light="#d7c49a" if six_closed else None)}
{door(1220, 300, 880, 230, 7, closed=False, right=True)}
<rect x="1400" y="600" width="260" height="22" fill="#100d14"/><rect x="1410" y="622" width="14" height="250" fill="#100d14"/><rect x="1636" y="622" width="14" height="250" fill="#100d14"/>
'''
    if six_closed:
        base += f'<polygon points="845,880 1075,880 1180,1080 740,1080" fill="#d7c49a" opacity="0.12"/>'
        base += glow(1300, 560, 140, "#ff3b2f", 0.06)
        base += f'<rect x="1500" y="230" width="80" height="30" rx="4" fill="#5a0e0c"/><text x="1540" y="253" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="20" fill="{RED}">EXIT</text>' + glow(1540, 245, 60, RED, 0.35)
    base += fog(880, "#8a8fa6", 0.08, 70)
    return base

save("s2", svg(row(False, True)))
save("s3", svg(row(True, False)))


# S4 — close on door six, red indicator, light at the gap
s4 = f'''
<rect width="{W}" height="{H}" fill="#0a090e"/>
<rect x="560" y="0" width="800" height="1000" fill="#120f16"/>
<rect x="600" y="0" width="720" height="960" fill="url(#d4)"/>
{''.join(f'<line x1="650" y1="{y}" x2="1270" y2="{y}" stroke="#16121a" stroke-width="10"/>' for y in range(40, 420, 36))}
<rect x="650" y="480" width="620" height="420" fill="none" stroke="#16121a" stroke-width="10"/>
<rect x="890" y="120" width="140" height="96" rx="10" fill="url(#brass)"/>
<text x="960" y="196" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="80" fill="#1a1408">6</text>
<rect x="1180" y="430" width="80" height="40" rx="8" fill="{RED}"/>
<circle cx="1220" cy="450" r="70" fill="{RED}" opacity="0.5" filter="url(#blur30)"/>
<circle cx="1220" cy="530" r="20" fill="#9c8650"/>
<rect x="600" y="960" width="720" height="40" fill="#e0c995"/>
<rect x="600" y="960" width="720" height="40" fill="#e0c995" filter="url(#blur8)"/>
<polygon points="600,1000 1320,1000 1500,1080 420,1080" fill="#e0c995" opacity="0.18"/>
<g fill="#050407" transform="translate(760 560) rotate(-8)">
<rect x="-260" y="-40" width="230" height="130" rx="50"/>
<rect x="-50" y="-60" width="60" height="44" rx="22"/><rect x="-50" y="-12" width="66" height="44" rx="22"/>
<rect x="-50" y="36" width="60" height="44" rx="22"/><rect x="-40" y="82" width="46" height="34" rx="17"/>
<rect x="-400" y="0" width="200" height="120" rx="40"/>
</g>
{glow(960, 990, 260, "#e0c995", 0.18)}
'''
save("s4", svg(s4, '''<linearGradient id="d4" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1e1a24"/><stop offset="1" stop-color="#2e2834"/></linearGradient>
<linearGradient id="brass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e3c37a"/><stop offset="0.5" stop-color="#a7853f"/><stop offset="1" stop-color="#5e4318"/></linearGradient>'''))


# S5 — floor level, looking under the door: white sneakers, one red lace
s5 = f'''
<rect width="{W}" height="{H}" fill="#08070b"/>
<rect x="0" y="0" width="{W}" height="500" fill="url(#d5)"/>
{''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#16121a" stroke-width="8"/>' for y in range(60, 480, 60))}
<rect x="0" y="500" width="{W}" height="220" fill="#d9c79c"/>
<rect x="0" y="500" width="{W}" height="220" fill="url(#inside)"/>
{sneaker_front(810, 706, 1.75, lace=RED)}
{sneaker_front(1110, 710, 1.75)}
<ellipse cx="960" cy="712" rx="300" ry="16" fill="#000" opacity="0.35" filter="url(#blur8)"/>
<rect x="0" y="490" width="{W}" height="14" fill="#0c0a10"/>
<rect x="0" y="720" width="{W}" height="360" fill="#100e15"/>
<polygon points="0,720 1920,720 2300,1080 -380,1080" fill="#d9c79c" opacity="0.14"/>
{''.join(f'<line x1="{960 + k * 60}" y1="720" x2="{960 + k * 320}" y2="1080" stroke="#07060a" stroke-width="3"/>' for k in range(-12, 13))}
<line x1="0" y1="780" x2="{W}" y2="780" stroke="#07060a" stroke-width="3"/><line x1="0" y1="880" x2="{W}" y2="880" stroke="#07060a" stroke-width="3"/>
{glow(960, 620, 380, "#ffe2a8", 0.12)}
<circle cx="840" cy="600" r="60" fill="{RED}" opacity="0.10" filter="url(#blur30)"/>
'''
save("s5", svg(s5, '''<linearGradient id="d5" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0e0c12"/><stop offset="1" stop-color="#2a2430"/></linearGradient>
<linearGradient id="inside" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f3e2b8" stop-opacity="0.6"/><stop offset="1" stop-color="#8a7a58" stop-opacity="0.5"/></linearGradient>'''))


# S6 — the door swings open on an empty room
s6 = f'''
<rect width="{W}" height="{H}" fill="#09080d"/>
{tiles(900, "#0e0c13", "#07060a")}
<rect x="700" y="230" width="520" height="670" fill="#120f16"/>
<rect x="720" y="250" width="480" height="650" fill="url(#room)"/>
<rect x="830" y="300" width="260" height="520" fill="#a9b3c6" opacity="0.85"/>
<rect x="830" y="300" width="260" height="520" fill="none" stroke="#3a3440" stroke-width="10"/>
<line x1="860" y1="340" x2="940" y2="520" stroke="#e6ecf5" stroke-width="6" opacity="0.6"/>
<rect x="750" y="760" width="420" height="22" fill="#2a2430"/>
<rect x="1050" y="380" width="8" height="40" fill="#3a3440"/><path d="M1054 420 l-24 30 h48z" fill="none" stroke="#3a3440" stroke-width="4"/>
<polygon points="720,250 470,190 470,980 720,900" fill="#2a2430"/>
<polygon points="720,250 470,190 470,980 720,900" fill="#000" opacity="0.35"/>
<rect x="490" y="560" width="26" height="14" rx="3" fill="#2a8a3a"/>
<polygon points="720,900 1200,900 1480,1080 440,1080" fill="#e6dcc0" opacity="0.18"/>
{glow(960, 560, 340, "#f3e6c8", 0.18)}
{fog(900, "#9aa0b6", 0.08, 70)}
'''
save("s6", svg(s6, '<linearGradient id="room" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfc3a6"/><stop offset="1" stop-color="#7a6e58"/></linearGradient>'))


# S7 — the tall mirror: a kneeling figure in it, the room in front empty
s7 = f'''
<rect width="{W}" height="{H}" fill="url(#room7)"/>
<rect x="640" y="60" width="640" height="900" fill="#2a2430"/>
<rect x="670" y="90" width="580" height="840" fill="url(#mir)"/>
<rect x="670" y="760" width="580" height="170" fill="#4a4238" opacity="0.8"/>
{kneeler(930, 860, 360, "#0a080c")}
<ellipse cx="960" cy="866" rx="160" ry="12" fill="#000" opacity="0.4" filter="url(#blur8)"/>
<line x1="720" y1="140" x2="860" y2="420" stroke="#ffffff" stroke-width="8" opacity="0.18"/>
<line x1="760" y1="130" x2="900" y2="400" stroke="#ffffff" stroke-width="3" opacity="0.15"/>
<rect x="0" y="960" width="{W}" height="120" fill="#3a3228"/>
<rect x="0" y="960" width="{W}" height="10" fill="#1a1612"/>
<rect x="1300" y="300" width="10" height="60" fill="#2a2430"/><path d="M1305 360 l-30 38 h60z" fill="#2a2430"/>
{glow(960, 400, 420, "#f3e6c8", 0.10)}
'''
save("s7", svg(s7, '''<linearGradient id="room7" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5a5040"/><stop offset="1" stop-color="#2a241c"/></linearGradient>
<linearGradient id="mir" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#b9c2d4"/><stop offset="1" stop-color="#6f7a90"/></linearGradient>'''))


# S8 — looking down: kneeling in socks on the cold tile
s8 = f'''
<rect width="{W}" height="{H}" fill="#2a241c"/>
{''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="#1a1612" stroke-width="4"/>' for x in range(0, W, 220))}
{''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#1a1612" stroke-width="4"/>' for y in range(60, H, 220))}
<g>
<path d="M640 0 L700 520 C710 600 760 640 820 640 L900 640 L900 0Z" fill="#141018"/>
<path d="M1020 0 L1020 640 L1100 640 C1160 640 1210 600 1220 520 L1280 0Z" fill="#141018"/>
<path d="M720 560 C700 700 720 880 780 920 C830 950 880 930 890 880 L900 620Z" fill="#7d7a86"/>
<path d="M1200 560 C1220 700 1200 880 1140 920 C1090 950 1040 930 1030 880 L1020 620Z" fill="#7d7a86"/>
<ellipse cx="830" cy="880" rx="52" ry="34" fill="#68646f"/>
<ellipse cx="1090" cy="880" rx="52" ry="34" fill="#68646f"/>
<path d="M705 600 L900 640" stroke="#5a5662" stroke-width="10"/><path d="M1215 600 L1020 640" stroke="#5a5662" stroke-width="10"/>
</g>
<ellipse cx="960" cy="960" rx="380" ry="40" fill="#000" opacity="0.3" filter="url(#blur30)"/>
<path d="M560 980 C620 960 640 1000 700 990" stroke="#e8e6e0" stroke-width="0" fill="none"/>
{glow(960, 300, 500, "#f3e6c8", 0.08)}
<rect width="{W}" height="{H}" fill="#000" opacity="0.15"/>
'''
save("s8", svg(s8))


# S9 — the dark mall; someone walking toward the exit in white sneakers
s9 = f'''
<rect width="{W}" height="{H}" fill="#07060b"/>
<polygon points="0,0 1920,0 1060,420 860,420" fill="#05040a"/>
<polygon points="0,0 860,420 860,640 0,1080" fill="#0b0a12"/>
<polygon points="1920,0 1060,420 1060,640 1920,1080" fill="#0b0a12"/>
{''.join(f'<polygon points="{x},{420 - (860 - x) * .49:.0f} {x + 60},{420 - (800 - x) * .49:.0f} {x + 60},{640 + (800 - x) * .51:.0f} {x},{640 + (860 - x) * .51:.0f}" fill="#120f1a"/>' for x in (100, 400, 640))}
{''.join(f'<polygon points="{W - x},{420 - (860 - x) * .49:.0f} {W - x - 60},{420 - (800 - x) * .49:.0f} {W - x - 60},{640 + (800 - x) * .51:.0f} {W - x},{640 + (860 - x) * .51:.0f}" fill="#120f1a"/>' for x in (100, 400, 640))}
<polygon points="0,1080 860,640 1060,640 1920,1080" fill="#0f0d16"/>
{''.join(f'<line x1="{860 + k * 20}" y1="640" x2="{860 + k * 20 + (k * 20 - 100) * 4.6:.0f}" y2="1080" stroke="#07060a" stroke-width="2"/>' for k in range(0, 11))}
<rect x="860" y="420" width="200" height="220" fill="#1a2236"/>
<rect x="870" y="440" width="85" height="200" fill="#3a4a70" opacity="0.7"/><rect x="965" y="440" width="85" height="200" fill="#3a4a70" opacity="0.7"/>
<rect x="920" y="396" width="80" height="22" rx="3" fill="#5a0e0c"/><text x="960" y="413" text-anchor="middle" font-family="{SANS}" font-weight="bold" font-size="16" fill="{RED}">EXIT</text>
{glow(960, 407, 60, RED, 0.5)}
{glow(960, 540, 160, "#6a80b8", 0.25)}
<polygon points="880,640 1040,640 1120,1080 800,1080" fill="#6a80b8" opacity="0.07"/>
{walker(960, 800, 300)}
<ellipse cx="960" cy="806" rx="60" ry="6" fill="#000" opacity="0.5"/>
{fog(700, "#5a6480", 0.10, 60)}
'''
save("s9", svg(s9))
print("ok")
