"""Scenes for The Rest Stop Phone."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

SKY = sky("sky1", "#04050c", "#141a2e", "#2a2236")
SODIUM = "#ffb24a"
STEEL = '''<linearGradient id="steel" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#c7ccd6" stop-opacity="0.5"/><stop offset="0.5" stop-color="#6c717c" stop-opacity="0.2"/><stop offset="1" stop-color="#2a2e36" stop-opacity="0.6"/></linearGradient>'''


def payphone(x, base, s=1.0, receiver="hung", ring=False, sticker=True, light="#e8d9a8"):
    """A roadside payphone on a post. (x, base) = bottom of post. receiver: hung | off."""
    def S(v): return v * s
    top = base - S(560)
    p = [f'<rect x="{x - S(14):.0f}" y="{top + S(300):.0f}" width="{S(28):.0f}" height="{S(260):.0f}" fill="#0a0b10"/>']
    # hood
    p.append(f'<rect x="{x - S(150):.0f}" y="{top - S(40):.0f}" width="{S(300):.0f}" height="{S(360):.0f}" rx="{S(14):.0f}" fill="#1b2230"/>')
    p.append(f'<rect x="{x - S(150):.0f}" y="{top - S(40):.0f}" width="{S(300):.0f}" height="{S(50):.0f}" rx="{S(10):.0f}" fill="#2a3446"/>')
    p.append(f'<rect x="{x - S(130):.0f}" y="{top - S(30):.0f}" width="{S(260):.0f}" height="{S(30):.0f}" fill="{light}" opacity="0.85"/>')
    # body
    p.append(f'<rect x="{x - S(95):.0f}" y="{top + S(20):.0f}" width="{S(190):.0f}" height="{S(280):.0f}" rx="{S(10):.0f}" fill="#8a8f99"/>')
    p.append(f'<rect x="{x - S(95):.0f}" y="{top + S(20):.0f}" width="{S(190):.0f}" height="{S(280):.0f}" rx="{S(10):.0f}" fill="url(#steel)"/>')
    # keypad
    for r in range(4):
        for c in range(3):
            p.append(f'<rect x="{x - S(40) + c * S(30):.0f}" y="{top + S(120) + r * S(30):.0f}" width="{S(22):.0f}" height="{S(20):.0f}" rx="{S(3):.0f}" fill="#2b2f37"/>')
    # coin slot + return
    p.append(f'<rect x="{x + S(45):.0f}" y="{top + S(50):.0f}" width="{S(30):.0f}" height="{S(8):.0f}" fill="#1a1c22"/>')
    p.append(f'<rect x="{x - S(30):.0f}" y="{top + S(250):.0f}" width="{S(60):.0f}" height="{S(32):.0f}" rx="{S(4):.0f}" fill="#2b2f37"/>')
    if sticker:
        p.append(f'<rect x="{x - S(60):.0f}" y="{top + S(40):.0f}" width="{S(95):.0f}" height="{S(60):.0f}" fill="#e6d68a" transform="rotate(-4 {x} {top + S(70):.0f})"/>')
        p.append(f'<g transform="rotate(-4 {x} {top + S(70):.0f})" fill="#5a1414">'
                 + "".join(f'<rect x="{x - S(52):.0f}" y="{top + S(52) + i * S(12):.0f}" width="{S(78 - i * 10):.0f}" height="{S(4):.0f}"/>' for i in range(4)) + '</g>')
    # cord + receiver
    if receiver == "hung":
        p.append(f'<rect x="{x - S(140):.0f}" y="{top + S(40):.0f}" width="{S(42):.0f}" height="{S(200):.0f}" rx="{S(18):.0f}" fill="#101217"/>')
        p.append(f'<path d="M{x - S(118):.0f} {top + S(240):.0f} c{S(-10):.0f} {S(30):.0f} {S(30):.0f} {S(30):.0f} {S(20):.0f} {S(60):.0f} c{S(-10):.0f} {S(30):.0f} {S(30):.0f} {S(10):.0f} {S(40):.0f} {S(-20):.0f}" stroke="#101217" stroke-width="{S(8):.0f}" fill="none"/>')
    else:
        cord = " ".join(f"q{S(18) * (1 if i % 2 else -1):.0f} {S(9):.0f} 0 {S(18):.0f}" for i in range(14))
        p.append(f'<path d="M{x - S(95):.0f} {top + S(250):.0f} {cord}" stroke="#3a3e4a" stroke-width="{S(7):.0f}" fill="none"/>')
        rb = top + S(250) + S(18) * 14
        p.append(f'<g transform="rotate(12 {x - S(95):.0f} {rb:.0f})"><rect x="{x - S(117):.0f}" y="{rb:.0f}" width="{S(44):.0f}" height="{S(190):.0f}" rx="{S(18):.0f}" fill="#2b2f3a" stroke="#ff6a50" stroke-width="{S(3):.0f}"/>'
                 f'<ellipse cx="{x - S(95):.0f}" cy="{rb + S(20):.0f}" rx="{S(30):.0f}" ry="{S(22):.0f}" fill="#16181f"/>'
                 f'<ellipse cx="{x - S(95):.0f}" cy="{rb + S(170):.0f}" rx="{S(30):.0f}" ry="{S(22):.0f}" fill="#16181f"/></g>')
    if ring:
        for k, r in enumerate((60, 100, 140)):
            p.append(f'<path d="M{x - S(160) - S(r) * .3:.0f} {top + S(60):.0f} a{S(r):.0f} {S(r):.0f} 0 0 0 0 {S(r * 1.2):.0f}" stroke="#ffe2a8" stroke-width="{S(6):.0f}" fill="none" opacity="{0.8 - k * .22:.2f}" stroke-linecap="round"/>')
            p.append(f'<path d="M{x + S(160) + S(r) * .3:.0f} {top + S(60):.0f} a{S(r):.0f} {S(r):.0f} 0 0 1 0 {S(r * 1.2):.0f}" stroke="#ffe2a8" stroke-width="{S(6):.0f}" fill="none" opacity="{0.8 - k * .22:.2f}" stroke-linecap="round"/>')
    return "".join(p)


def lamp(x, base, h=620, color=SODIUM):
    top = base - h
    return (f'<rect x="{x - 8}" y="{top}" width="16" height="{h}" fill="#08090e"/>'
            f'<path d="M{x} {top} q0 -30 60 -30 h50" stroke="#08090e" stroke-width="12" fill="none"/>'
            f'<rect x="{x + 70}" y="{top - 40}" width="80" height="20" rx="8" fill="#08090e"/>'
            f'<ellipse cx="{x + 110}" cy="{top - 18}" rx="34" ry="8" fill="{color}"/>'
            f'<polygon points="{x + 80},{top - 18} {x + 140},{top - 18} {x + 360},{base} {x - 140},{base}" fill="{color}" opacity="0.10"/>'
            + glow(x + 110, top - 10, 70, color, 0.7))


def vending(x, y, w=200, h=420, color="#8fd4ff"):
    rows = "".join(f'<rect x="{x + 20}" y="{y + 40 + i * 60}" width="{w - 80}" height="40" fill="{["#c0392b", "#e0a030", "#2f80c0", "#3aa055", "#b05090"][i % 5]}" opacity="0.7"/>' for i in range(5))
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#1c2028"/>'
            f'<rect x="{x + 12}" y="{y + 20}" width="{w - 64}" height="{h - 110}" fill="{color}" opacity="0.85"/>{rows}'
            f'<rect x="{x + w - 44}" y="{y + 40}" width="30" height="120" fill="#2c313b"/>'
            f'<rect x="{x + 16}" y="{y + h - 70}" width="{w - 70}" height="40" fill="#0b0d12"/>'
            + glow(x + w / 2, y + h / 2, w * 0.9, color, 0.35))


def building(x0, x1, roof, base):
    return (f'<rect x="{x0}" y="{roof}" width="{x1 - x0}" height="{base - roof}" fill="#14131c"/>'
            f'<rect x="{x0 - 30}" y="{roof - 30}" width="{x1 - x0 + 60}" height="34" fill="#0b0a11"/>'
            + "".join(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="#1d1c27" stroke-width="3"/>' for y in range(roof + 30, base, 32)))


def car_side(x, base, s=1.0, interior=None):
    """A sedan in profile, facing right. interior: None or glow color in the rear window."""
    def S(v): return v * s
    body = (f'<path d="M{x:.0f} {base - S(60):.0f} L{x:.0f} {base - S(150):.0f} Q{x + S(10):.0f} {base - S(180):.0f} {x + S(80):.0f} {base - S(185):.0f} '
            f'L{x + S(170):.0f} {base - S(190):.0f} L{x + S(260):.0f} {base - S(280):.0f} L{x + S(520):.0f} {base - S(285):.0f} '
            f'L{x + S(640):.0f} {base - S(190):.0f} L{x + S(800):.0f} {base - S(175):.0f} Q{x + S(850):.0f} {base - S(160):.0f} {x + S(850):.0f} {base - S(110):.0f} '
            f'L{x + S(850):.0f} {base - S(60):.0f} Z" fill="#0b0c13"/>')
    win = (f'<path d="M{x + S(280):.0f} {base - S(265):.0f} L{x + S(395):.0f} {base - S(268):.0f} L{x + S(395):.0f} {base - S(195):.0f} L{x + S(200):.0f} {base - S(192):.0f} Z" fill="#1a2030"/>'
           f'<path d="M{x + S(410):.0f} {base - S(268):.0f} L{x + S(510):.0f} {base - S(268):.0f} L{x + S(610):.0f} {base - S(195):.0f} L{x + S(410):.0f} {base - S(195):.0f} Z" fill="#1a2030"/>')
    extra = ""
    if interior:
        extra = (f'<path d="M{x + S(280):.0f} {base - S(265):.0f} L{x + S(395):.0f} {base - S(268):.0f} L{x + S(395):.0f} {base - S(195):.0f} L{x + S(200):.0f} {base - S(192):.0f} Z" fill="{interior}" opacity="0.45"/>'
                 + glow(x + S(320), base - S(220), S(60), interior, 0.6)
                 + f'<ellipse cx="{x + S(330):.0f}" cy="{base - S(232):.0f}" rx="{S(22):.0f}" ry="{S(27):.0f}" fill="#06070b"/>'
                 f'<path d="M{x + S(290):.0f} {base - S(195):.0f} q{S(40):.0f} {S(-40):.0f} {S(80):.0f} 0" fill="#06070b"/>')
    wheels = "".join(f'<circle cx="{x + S(c):.0f}" cy="{base - S(55):.0f}" r="{S(62):.0f}" fill="#050508"/><circle cx="{x + S(c):.0f}" cy="{base - S(55):.0f}" r="{S(26):.0f}" fill="#20222b"/>' for c in (170, 680))
    lights = (f'<rect x="{x + S(830):.0f}" y="{base - S(155):.0f}" width="{S(22):.0f}" height="{S(24):.0f}" fill="#fff1c8"/>'
              f'<rect x="{x - S(4):.0f}" y="{base - S(145):.0f}" width="{S(14):.0f}" height="{S(30):.0f}" fill="#d12a22"/>')
    return body + win + extra + wheels + lights


# S1 — the rest area at night
s1 = f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(150, 520)}
{moon(1560, 190, 70)}
<path d="M0 640 C400 610 800 625 1200 615 C1500 608 1700 620 1920 612 L1920 1080 L0 1080Z" fill="#0d0d16"/>
{''.join(f'<path d="M{x} 640 l40 -120 l40 120z" fill="#090910"/>' for x in range(-20, 1960, 70))}
{building(380, 1100, 520, 760)}
<rect x="560" y="600" width="110" height="160" fill="#090910"/>
<rect x="820" y="600" width="110" height="160" fill="#090910"/>
{vending(1000, 590, 90, 170)}
{lamp(1150, 860, 560)}
<rect x="0" y="760" width="{W}" height="320" fill="#121119"/>
<rect x="0" y="760" width="{W}" height="320" fill="url(#lot)"/>
{''.join(f'<rect x="{x}" y="900" width="10" height="120" fill="#3a3a44" transform="skewX(-25)" opacity="0.6"/>' for x in range(600, 2300, 190))}
{payphone(1290, 860, 0.55)}
<g transform="translate(560 430)"><rect x="-6" y="0" width="12" height="90" fill="#08090e"/><rect x="-110" y="-60" width="220" height="70" rx="6" fill="#1f4a32"/>
<text x="0" y="-14" text-anchor="middle" font-family="{SANS}" font-size="30" font-weight="bold" fill="#e8efe8">REST AREA</text></g>
{fog(780, "#9fa6c0", 0.10)}
'''
save("s1", svg(s1, SKY + STEEL + f'<linearGradient id="lot" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SODIUM}" stop-opacity="0.12"/><stop offset="1" stop-color="#000" stop-opacity="0.5"/></linearGradient>'))


# S2 — close-up of the sticker
s2 = f'''
<rect width="{W}" height="{H}" fill="#0c0e14"/>
<rect x="520" y="0" width="880" height="1080" fill="#4e535c"/>
<rect x="520" y="0" width="880" height="1080" fill="url(#steel)"/>
{''.join(f'<rect x="{620 + c * 120}" y="{720 + r * 110}" width="90" height="80" rx="10" fill="#262a31"/>' for r in range(3) for c in range(3))}
{''.join(f'<text x="{665 + c * 120}" y="{775 + r * 110}" text-anchor="middle" font-family="{SANS}" font-size="40" fill="#c9ccd2">{1 + r * 3 + c}</text>' for r in range(3) for c in range(3))}
<rect x="1060" y="120" width="160" height="26" fill="#1a1c22"/>
<g transform="rotate(-4 900 330)">
<rect x="600" y="180" width="620" height="330" fill="#e9d98c"/>
<rect x="600" y="180" width="620" height="330" fill="#7a5a10" opacity="0.15"/>
<text x="910" y="270" text-anchor="middle" font-family="{SANS}" font-size="56" font-weight="bold" fill="#6a1515">IF THIS PHONE RINGS</text>
<text x="910" y="350" text-anchor="middle" font-family="{SANS}" font-size="56" font-weight="bold" fill="#6a1515">IT'S FOR YOU</text>
<rect x="680" y="390" width="460" height="80" fill="#6a1515"/>
<text x="910" y="450" text-anchor="middle" font-family="{SANS}" font-size="54" font-weight="bold" fill="#e9d98c">DO NOT ANSWER</text>
<path d="M600 180 l60 0 l-60 50z" fill="#b8a960"/>
</g>
<rect x="520" y="0" width="880" height="1080" fill="{SODIUM}" opacity="0.08"/>
{glow(900, 120, 300, SODIUM, 0.15)}
'''
save("s2", svg(s2, STEEL))

# S3 — driving through the night
s3 = f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(120, 450)}
<path d="M0 560 C300 520 700 540 1000 530 C1300 520 1600 540 1920 525 L1920 1080 L0 1080Z" fill="#0b0b14"/>
{''.join(f'<path d="M{x} 570 l{30 + (x * 7) % 25} -{100 + (x * 13) % 80} l{30 + (x * 7) % 25} {100 + (x * 13) % 80}z" fill="#07070d"/>' for x in range(-20, 1960, 55))}
<polygon points="900,560 1020,560 1700,1080 220,1080" fill="#16161f"/>
{''.join(f'<polygon points="{958 - (y - 560) * 0.006:.0f},{y} {962 + (y - 560) * 0.006:.0f},{y} {962 + (y + 30 - 560) * 0.012:.0f},{y + 30 + (y - 560) * 0.1:.0f} {958 - (y + 30 - 560) * 0.012:.0f},{y + 30 + (y - 560) * 0.1:.0f}" fill="#d8c070" opacity="0.8"/>' for y in (580, 640, 740, 900))}

<g transform="translate(960 800)">
<path d="M-170 0 L-160 -70 L-110 -130 L110 -130 L160 -70 L170 0 Z" fill="#0b0c13"/>
<path d="M-100 -122 L100 -122 L140 -75 L-140 -75Z" fill="#1d2536"/>
<ellipse cx="-30" cy="-98" rx="16" ry="18" fill="#06070b"/><ellipse cx="45" cy="-96" rx="17" ry="19" fill="#06070b"/>
<rect x="-160" y="-55" width="60" height="22" rx="5" fill="#ff3b2f"/><rect x="100" y="-55" width="60" height="22" rx="5" fill="#ff3b2f"/>
<rect x="-40" y="-40" width="80" height="22" fill="#cfcfc0"/>
<rect x="-150" y="0" width="50" height="26" fill="#050508"/><rect x="100" y="0" width="50" height="26" fill="#050508"/>
</g>
{glow(830, 755, 50, "#ff3b2f", 0.6)}{glow(1090, 755, 50, "#ff3b2f", 0.6)}
<polygon points="860,560 1060,560 1180,780 740,780" fill="#fff1c8" opacity="0.07"/>
<g transform="translate(1290 520)"><rect x="-5" y="0" width="10" height="120" fill="#07070d"/><rect x="-60" y="-70" width="120" height="80" rx="8" fill="#e8e4d8"/>
<text x="0" y="-40" text-anchor="middle" font-family="{SANS}" font-size="22" font-weight="bold" fill="#111">ROUTE</text>
<text x="0" y="-4" text-anchor="middle" font-family="{SANS}" font-size="38" font-weight="bold" fill="#111">9</text></g>
{fog(600, "#8f93b0", 0.10)}
'''
save("s3", svg(s3, SKY))

# S4 — the empty lot: me, the vending machine, the payphone
s4 = f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(80, 300, 0.5)}
{building(300, 1700, 300, 760)}
<rect x="420" y="420" width="140" height="340" fill="#090910"/>
{vending(620, 360, 210, 400)}
{lamp(1240, 900, 700)}
<rect x="0" y="760" width="{W}" height="320" fill="#121119"/>
<rect x="0" y="760" width="{W}" height="320" fill="url(#lot)"/>
{payphone(1120, 900, 0.85)}
{figure(860, 1010, 330, "#040306")}
<ellipse cx="860" cy="1012" rx="80" ry="12" fill="#000" opacity="0.6"/>
{fog(860, "#9fa6c0", 0.10)}
'''
save("s4", svg(s4, SKY + STEEL + f'<linearGradient id="lot" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SODIUM}" stop-opacity="0.15"/><stop offset="1" stop-color="#000" stop-opacity="0.5"/></linearGradient>'))

# S5 — the payphone rings
s5 = f'''
<rect width="{W}" height="{H}" fill="#07080d"/>
<rect x="0" y="0" width="{W}" height="760" fill="#100f17"/>
{''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#18171f" stroke-width="3"/>' for y in range(40, 760, 36))}
<rect x="0" y="760" width="{W}" height="320" fill="#14131b"/>
{glow(960, 230, 380, "#ffd590", 0.30)}
{payphone(960, 1040, 1.35, ring=True, light="#fff0c8")}
<ellipse cx="960" cy="1045" rx="200" ry="20" fill="#000" opacity="0.6"/>
'''
save("s5", svg(s5, STEEL))

# S6 — my cell: the caller ID is the payphone
s6 = f'''
<rect width="{W}" height="{H}" fill="#050508"/>
{glow(960, 520, 420, "#8fb8ff", 0.25)}
<g fill="#a07a62">
<path d="M760 1080 L780 760 C790 700 840 690 880 700 L900 1080Z"/>
<rect x="1050" y="560" width="60" height="170" rx="30" transform="rotate(20 1080 640)"/>
<rect x="1060" y="680" width="60" height="150" rx="30" transform="rotate(15 1090 750)"/>
</g>
<rect x="760" y="130" width="400" height="800" rx="56" fill="#111318"/>
<rect x="780" y="150" width="360" height="760" rx="40" fill="#0e1830"/>
<rect x="780" y="150" width="360" height="760" rx="40" fill="url(#screen)"/>
<text x="960" y="300" text-anchor="middle" font-family="{SANS}" font-size="30" fill="#c8d4ee">incoming call</text>
<text x="960" y="390" text-anchor="middle" font-family="{SANS}" font-size="46" font-weight="bold" fill="#ffffff">RT 9 REST AREA</text>
<text x="960" y="445" text-anchor="middle" font-family="{SANS}" font-size="34" fill="#c8d4ee">PAYPHONE</text>
<circle cx="860" cy="800" r="50" fill="#d83a32"/><circle cx="1060" cy="800" r="50" fill="#2fb35a"/>
<rect x="835" y="792" width="50" height="16" rx="8" fill="#fff"/>
<path d="M1040 785 q20 30 40 30" stroke="#fff" stroke-width="12" fill="none" stroke-linecap="round"/>
<g fill="#a07a62"><path d="M700 1080 L720 860 C730 800 790 780 830 820 L860 1080Z"/>
<rect x="760" y="640" width="60" height="180" rx="30" transform="rotate(-10 790 730)"/></g>
'''
save("s6", svg(s6, '<linearGradient id="screen" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a4a8a" stop-opacity="0.6"/><stop offset="1" stop-color="#000" stop-opacity="0.3"/></linearGradient>'))

# S7 — my sister answers in the car
s7 = f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(70, 300, 0.5)}
{building(0, 1920, 260, 720)}
{lamp(1500, 880, 640)}
<rect x="0" y="720" width="{W}" height="360" fill="#121119"/>
<rect x="0" y="720" width="{W}" height="360" fill="url(#lot)"/>
{car_side(500, 960, 1.15, interior="#9cc4ff")}
<ellipse cx="990" cy="965" rx="520" ry="22" fill="#000" opacity="0.6"/>
{fog(900, "#9fa6c0", 0.08)}
'''
save("s7", svg(s7, SKY + f'<linearGradient id="lot" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SODIUM}" stop-opacity="0.12"/><stop offset="1" stop-color="#000" stop-opacity="0.5"/></linearGradient>'))


def car_window(locked=False, red=False):
    tint = "#c2362b" if red else "#7fa6e0"
    pin_h = 14 if locked else 60
    body = f'''
<rect width="{W}" height="{H}" fill="#06070b"/>
<rect x="0" y="700" width="{W}" height="380" fill="#0d0e15"/>
<path d="M300 700 L420 160 Q440 120 500 120 L1500 120 Q1560 120 1580 170 L1700 700Z" fill="#0c0f18"/>
<path d="M360 680 L460 190 Q475 160 520 160 L1470 160 Q1520 160 1535 200 L1640 680Z" fill="#141c2c"/>
<path d="M360 680 L460 190 Q475 160 520 160 L1470 160 Q1520 160 1535 200 L1640 680Z" fill="{tint}" opacity="{0.22 if red else 0.12}"/>
{glow(960, 470, 260, tint, 0.35)}
<g fill="#04050a">
<ellipse cx="960" cy="380" rx="120" ry="150"/>
<path d="M760 690 C770 560 860 520 960 520 C1060 520 1150 560 1160 690Z"/>
<path d="M840 300 C850 220 1070 220 1080 300 L1090 420 L1050 330 L870 330 L830 420Z"/>
</g>
<g fill="#e8ecf4" opacity="0.55"><ellipse cx="915" cy="390" rx="11" ry="6"/><ellipse cx="1005" cy="390" rx="11" ry="6"/></g>
<path d="M400 200 L700 680" stroke="#ffffff" stroke-width="40" opacity="0.04"/>
<path d="M1250 160 L1500 680" stroke="#ffffff" stroke-width="70" opacity="0.03"/>
<rect x="1290" y="{700 - pin_h}" width="18" height="{pin_h + 6}" rx="8" fill="#aab0bc"/>
<rect x="1270" y="696" width="58" height="12" rx="6" fill="#20232c"/>
<rect x="250" y="760" width="200" height="40" rx="18" fill="#1b1e27"/>
'''
    if red:
        body += glow(1299, 690, 40, "#ff3b2f", 0.6)
    return svg(body)

save("s8", car_window(locked=False))
save("s8b", car_window(locked=True, red=True))

# S9 — the receiver swinging on its cord
s9 = f'''
<rect width="{W}" height="{H}" fill="#060407"/>
<rect x="0" y="0" width="{W}" height="780" fill="#120a0d"/>
{''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#1c1015" stroke-width="3"/>' for y in range(40, 780, 36))}
<rect x="0" y="780" width="{W}" height="300" fill="#150c10"/>
{glow(960, 300, 420, "#c2362b", 0.35)}
{payphone(960, 800, 1.0, receiver="off", sticker=True, light="#ff6a50")}
{glow(870, 860, 90, "#ff3b2f", 0.25)}
'''
save("s9", svg(s9, STEEL))
print("ok")
