"""Scenes for 'The Rearview' — a Thanksgiving drive home through a mountain pass, a tunnel, a rearview mirror."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

r = random.Random(11)


def pines(y, n, color, hmin=60, hmax=150, x0=0, x1=W):
    out = []
    for _ in range(n):
        x = r.randint(x0, x1); h = r.randint(hmin, hmax); w = h * 0.32
        out.append(f'<polygon points="{x},{y - h} {x - w:.0f},{y} {x + w:.0f},{y}" fill="{color}"/>'
                   f'<polygon points="{x},{y - h * 1.15:.0f} {x - w * .7:.0f},{y - h * .45:.0f} {x + w * .7:.0f},{y - h * .45:.0f}" fill="{color}"/>')
    return "".join(out)


def drops(x0, y0, w, h, n, color="#9fb0c8", op=0.5):
    return "".join(f'<ellipse cx="{r.randint(x0, x0 + w)}" cy="{r.randint(y0, y0 + h)}" rx="{r.choice([2, 3, 4])}" ry="{r.choice([3, 5, 6])}" '
                   f'fill="{color}" opacity="{r.uniform(op * .3, op):.2f}"/>' for _ in range(n))


def woman(cx, base, head_up=False):
    """Seated woman in a gray coat, wet black hair over her face. (cx, base) = where she sits on the seat."""
    hy = base - 300 if head_up else base - 270
    hx = cx if head_up else cx + 8
    hair = (f'<path d="M{hx - 62} {hy - 20} C{hx - 70} {hy - 90} {hx + 70} {hy - 90} {hx + 62} {hy - 20} '
            f'L{hx + 74} {hy + 150} C{hx + 40} {hy + 170} {hx + 20} {hy + 140} {hx + 6} {hy + 175} '
            f'C{hx - 10} {hy + 140} {hx - 40} {hy + 172} {hx - 76} {hy + 150} Z" fill="#050407"/>')
    strands = "".join(f'<path d="M{hx + dx} {hy - 30} C{hx + dx * 1.1:.0f} {hy + 40} {hx + dx * .9:.0f} {hy + 100} {hx + dx * 1.2:.0f} {hy + 165}" '
                      f'stroke="#1a1a24" stroke-width="2" fill="none" opacity="0.8"/>' for dx in (-48, -30, -14, 4, 20, 36, 52))
    face = ""
    if head_up:
        # pale face showing through gaps in the hair, eyes and a wide smile
        face = (f'<ellipse cx="{hx}" cy="{hy + 30}" rx="50" ry="66" fill="#b9bfc2"/>'
                f'<g fill="#050407">'
                f'<path d="M{hx - 52} {hy - 30} C{hx - 30} {hy + 20} {hx - 40} {hy + 70} {hx - 34} {hy + 110} L{hx - 60} {hy + 110} Z"/>'
                f'<path d="M{hx + 52} {hy - 30} C{hx + 34} {hy + 20} {hx + 44} {hy + 70} {hx + 36} {hy + 110} L{hx + 62} {hy + 110} Z"/>'
                f'<path d="M{hx - 8} {hy - 34} C{hx - 4} {hy + 20} {hx + 6} {hy + 40} {hx + 2} {hy + 92} L{hx + 12} {hy + 92} C{hx + 14} {hy + 40} {hx + 6} {hy + 10} {hx + 10} {hy - 34}Z"/>'
                f'</g>'
                f'<ellipse cx="{hx - 22}" cy="{hy + 18}" rx="9" ry="6" fill="#0b0b10"/><ellipse cx="{hx + 26}" cy="{hy + 18}" rx="9" ry="6" fill="#0b0b10"/>'
                f'<circle cx="{hx - 20}" cy="{hy + 17}" r="2.5" fill="#e8e8e8"/><circle cx="{hx + 28}" cy="{hy + 17}" r="2.5" fill="#e8e8e8"/>'
                f'<path d="M{hx - 34} {hy + 58} Q{hx + 4} {hy + 92} {hx + 40} {hy + 56} Q{hx + 4} {hy + 76} {hx - 34} {hy + 58}Z" fill="#14070a"/>'
                f'<path d="M{hx - 28} {hy + 62} Q{hx + 4} {hy + 80} {hx + 34} {hy + 60}" stroke="#d9d4c8" stroke-width="3" fill="none" opacity="0.7"/>')
        hair = (f'<path d="M{hx - 66} {hy - 20} C{hx - 74} {hy - 100} {hx + 74} {hy - 100} {hx + 66} {hy - 20} '
                f'L{hx + 80} {hy + 170} L{hx + 50} {hy + 160} L{hx + 52} {hy + 20} C{hx + 30} {hy - 40} {hx - 30} {hy - 40} {hx - 52} {hy + 20} '
                f'L{hx - 50} {hy + 160} L{hx - 80} {hy + 170} Z" fill="#050407"/>')
    coat = (f'<path d="M{cx - 120} {base} C{cx - 130} {base - 120} {cx - 110} {base - 180} {cx - 60} {base - 200} '
            f'L{cx + 60} {base - 200} C{cx + 110} {base - 180} {cx + 130} {base - 120} {cx + 120} {base} Z" fill="#4a4e57"/>'
            f'<path d="M{cx - 20} {base - 196} L{cx} {base - 120} L{cx + 20} {base - 196}" stroke="#2b2e35" stroke-width="5" fill="none"/>'
            f'<line x1="{cx}" y1="{base - 120}" x2="{cx}" y2="{base}" stroke="#2b2e35" stroke-width="4"/>'
            f'<circle cx="{cx + 12}" cy="{base - 90}" r="5" fill="#2b2e35"/><circle cx="{cx + 12}" cy="{base - 45}" r="5" fill="#2b2e35"/>'
            f'<path d="M{cx - 100} {base - 40} C{cx - 60} {base - 20} {cx + 60} {base - 20} {cx + 100} {base - 40}" stroke="#2b2e35" stroke-width="10" fill="none"/>')
    wet = drops(cx - 110, base - 190, 220, 190, 40, "#c3cfe0", 0.55)
    return f'{coat}{wet}{face}{hair}{strands}'


def mirror_scene(head_up):
    """Driver's view of the rearview mirror against the windshield; the back seat reflected inside."""
    MX, MY, MW, MH = 540, 170, 840, 450
    inner = f'''
<rect x="{MX}" y="{MY}" width="{MW}" height="{MH}" fill="#14121a"/>
<rect x="{MX}" y="{MY}" width="{MW}" height="{MH}" fill="url(#rearglow)"/>
<rect x="{MX}" y="{MY + 20}" width="{MW}" height="150" fill="#06060a"/>
<rect x="{MX + 40}" y="{MY + 32}" width="{MW - 80}" height="120" rx="20" fill="#1b2638"/>
<circle cx="{MX + 300}" cy="{MY + 100}" r="5" fill="#ffd7a0"/><circle cx="{MX + 340}" cy="{MY + 104}" r="4" fill="#ffd7a0" opacity="0.7"/>
<rect x="{MX - 20}" y="{MY + 230}" width="{MW + 40}" height="{MH}" rx="30" fill="#24212a"/>
<g stroke="#17151c" stroke-width="5">{''.join(f'<line x1="{x}" y1="{MY + 240}" x2="{x}" y2="{MY + MH}"/>' for x in range(MX + 60, MX + MW, 120))}</g>
<rect x="{MX + 60}" y="{MY + 190}" width="90" height="70" rx="14" fill="#1d1a22"/>
<rect x="{MX + MW - 150}" y="{MY + 190}" width="90" height="70" rx="14" fill="#1d1a22"/>
<g transform="translate({MX + MW / 2} {MY + MH + 40}) scale(0.95)">{woman(0, 0, head_up)}</g>
'''
    accent = '#ff2a2a' if head_up else '#ff6a3a'
    return svg(f'''
<rect width="{W}" height="{H}" fill="url(#night)"/>
{stars(70, 420, 0.5)}
<path d="M0 640 L380 420 L620 520 L900 360 L1200 500 L1500 380 L1920 560 L1920 1080 L0 1080Z" fill="#0d1018"/>
{pines(700, 70, "#07080d", 70, 170)}
<path d="M760 1080 L940 700 L980 700 L1160 1080Z" fill="#191b22"/>
<path d="M955 1080 L958 700 L962 700 L965 1080Z" fill="#c9a24a" opacity="0.5"/>
<polygon points="700,1080 960,690 1220,1080" fill="#f4e7c2" opacity="0.10" filter="url(#blur30)"/>
{drops(0, 0, W, 760, 50, "#aab8d0", 0.25)}
<path d="M0 0 L1920 0 L1920 150 C1500 120 420 120 0 150Z" fill="#050508"/>
<rect x="950" y="120" width="20" height="140" fill="#08080b"/>
<rect x="{MX - 22}" y="{MY - 22}" width="{MW + 44}" height="{MH + 44}" rx="46" fill="#0b0b0e"/>
<clipPath id="mclip"><rect x="{MX}" y="{MY}" width="{MW}" height="{MH}" rx="30"/></clipPath>
<g clip-path="url(#mclip)">{inner}
<rect x="{MX}" y="{MY}" width="{MW}" height="{MH}" fill="#8ea6c8" opacity="0.05"/>
<path d="M{MX} {MY} L{MX + 260} {MY} L{MX + 120} {MY + MH} L{MX} {MY + MH}Z" fill="#fff" opacity="0.04"/></g>
{glow(960, MY + MH / 2, 300, accent, 0.10)}
<path d="M0 1080 L0 860 C300 820 700 830 960 840 C1220 830 1620 820 1920 860 L1920 1080Z" fill="#060508"/>
<path d="M0 900 C400 870 800 880 960 885" stroke="#1a1820" stroke-width="4" fill="none"/>
<circle cx="380" cy="960" r="10" fill="#ff8a3a"/><circle cx="380" cy="960" r="30" fill="#ff8a3a" opacity="0.3" filter="url(#blur8)"/>
''', sky("night", "#04050b", "#0f1424", "#1d2232") +
        f'<radialGradient id="rearglow" cx="0.5" cy="0.2" r="0.8"><stop offset="0" stop-color="{accent}" stop-opacity="0.22"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>')


# S1 — the mountain road at night, the tunnel mouth, one car's headlights
s1 = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky1)"/>
{stars(180, 520)}
{moon(1500, 210, 70)}
<path d="M0 520 L260 360 L480 470 L760 260 L1040 430 L1300 300 L1620 450 L1920 340 L1920 1080 L0 1080Z" fill="#141a2a"/>
{fog(520, "#9aa6c4", 0.12, 90)}
<path d="M0 640 L300 520 L560 600 L820 430 L1080 560 L1340 480 L1600 600 L1920 520 L1920 1080 L0 1080Z" fill="#0c1019"/>
{pines(640, 60, "#080b12", 50, 120)}
<path d="M640 1080 C760 900 1000 820 1120 720 C1200 650 1250 620 1300 600" stroke="#1d1f27" stroke-width="70" fill="none"/>
<path d="M640 1080 C760 900 1000 820 1120 720 C1200 650 1250 620 1300 600" stroke="#c9a24a" stroke-width="3" stroke-dasharray="26 22" fill="none" opacity="0.6"/>
<path d="M1220 640 C1220 560 1270 530 1320 530 C1370 530 1420 560 1420 640 Z" fill="#26262c"/>
<path d="M1240 640 C1240 575 1280 550 1320 550 C1360 550 1400 575 1400 640 Z" fill="#020203"/>
<g>{''.join(f'<circle cx="{1320 + dx}" cy="{565 + dy}" r="4" fill="#ffb24a" opacity="{o}"/>' for dx, dy, o in ((-30, 30, .9), (0, 12, .9), (30, 30, .9), (-14, 48, .6), (14, 48, .6)))}</g>
{glow(1320, 600, 70, "#ffa040", 0.35)}
<path d="M1040 1080 C1100 900 1180 820 1240 760 L1240 1080Z" fill="#090c14"/>
<g transform="translate(905 812) rotate(-28)">
<rect x="-46" y="-20" width="92" height="36" rx="10" fill="#050608"/>
<rect x="-30" y="-36" width="54" height="22" rx="8" fill="#050608"/>
</g>
<polygon points="935,795 1150,700 1160,740 945,812" fill="#f4e7c2" opacity="0.22" filter="url(#blur8)"/>
<circle cx="938" cy="800" r="7" fill="#fff6dc"/><circle cx="938" cy="800" r="26" fill="#fff6dc" opacity="0.4" filter="url(#blur8)"/>
<circle cx="872" cy="828" r="5" fill="#ff2a2a"/><circle cx="872" cy="828" r="18" fill="#ff2a2a" opacity="0.4" filter="url(#blur8)"/>
{pines(1080, 40, "#04060a", 120, 260)}
{fog(860, "#aab3c8", 0.10, 120)}
''', sky("sky1", "#04050d", "#121a32", "#2b2b45"))
save("s1", s1)

# S2 — the warning: Dad at the wheel on an older trip, kid in the passenger seat, the mirror between them
s2 = svg(f'''
<rect width="{W}" height="{H}" fill="#07070b"/>
<path d="M300 130 C700 90 1220 90 1620 130 L1700 600 L220 600Z" fill="url(#ws)"/>
{stars(60, 420, 0.4)}
<path d="M300 560 L620 380 L860 470 L1100 330 L1360 450 L1640 520 L1700 600 L220 600Z" fill="#0c0f18"/>
<path d="M820 600 L940 470 L980 470 L1100 600Z" fill="#1b1c22"/>
<polygon points="760,600 960,460 1160,600" fill="#f4e7c2" opacity="0.10" filter="url(#blur30)"/>
<rect x="900" y="150" width="200" height="66" rx="18" fill="#0b0b0e"/>
<rect x="912" y="160" width="176" height="46" rx="12" fill="#1a1d28"/>
<rect x="990" y="110" width="16" height="44" fill="#0b0b0e"/>
<path d="M0 600 L1920 600 L1920 1080 L0 1080Z" fill="#0b0a0e"/>
<path d="M0 640 C500 600 1400 600 1920 640 L1920 700 L0 700Z" fill="#141218"/>
<g fill="#ffa040"><circle cx="560" cy="668" r="5"/><circle cx="600" cy="668" r="5"/><circle cx="640" cy="668" r="5"/></g>
{glow(600, 668, 70, "#ffa040", 0.25)}
<g fill="#040306">
<ellipse cx="600" cy="420" rx="70" ry="84"/>
<path d="M480 1080 L490 560 C500 500 540 490 600 490 C660 490 700 500 710 560 L720 1080Z"/>
<path d="M690 610 C760 640 790 690 820 760" stroke="#040306" stroke-width="44" stroke-linecap="round" fill="none"/>
<ellipse cx="1400" cy="520" rx="48" ry="58"/>
<path d="M1320 1080 L1330 660 C1340 610 1370 600 1400 600 C1430 600 1460 610 1470 660 L1480 1080Z"/>
</g>
<ellipse cx="620" cy="840" rx="220" ry="220" fill="none" stroke="#050407" stroke-width="40"/>
<path d="M630 412 C640 400 660 400 668 410" stroke="#3a2c24" stroke-width="3" fill="none"/>
<path d="M440 360 C420 320 520 300 600 320" stroke="#1b1a20" stroke-width="2" fill="none" opacity="0.6"/>
{glow(1000, 183, 120, "#ff6a3a", 0.12)}
''', '<linearGradient id="ws" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#05060d"/><stop offset="1" stop-color="#202538"/></linearGradient>')
save("s2", s2)

# S3 — this year: I drive, Dad asleep against the passenger window, tunnel ahead
s3 = svg(f'''
<rect width="{W}" height="{H}" fill="#07070b"/>
<path d="M240 120 C700 80 1220 80 1680 120 L1760 620 L160 620Z" fill="url(#ws3)"/>
{stars(50, 360, 0.35)}
<path d="M160 560 L500 300 L760 420 L1060 250 L1380 400 L1760 330 L1760 620 L160 620Z" fill="#11151f"/>
<path d="M800 530 C800 440 870 400 960 400 C1050 400 1120 440 1120 530 L1120 620 L800 620Z" fill="#2a2a30"/>
<path d="M830 620 L830 530 C830 460 890 425 960 425 C1030 425 1090 460 1090 530 L1090 620Z" fill="#020203"/>
<g>{''.join(f'<circle cx="{960 + dx}" cy="{460 + dy}" r="5" fill="#ffb24a"/>' for dx, dy in ((-80, 40), (-40, 14), (0, 6), (40, 14), (80, 40)))}</g>
{glow(960, 480, 120, "#ffa040", 0.3)}
<path d="M560 620 L900 560 L1020 560 L1360 620Z" fill="#1c1d23"/>
<polygon points="620,620 960,540 1300,620" fill="#f4e7c2" opacity="0.14" filter="url(#blur30)"/>
{pines(620, 30, "#06080d", 60, 150, 160, 760)}{pines(620, 30, "#06080d", 60, 150, 1160, 1760)}
<rect x="860" y="140" width="200" height="66" rx="18" fill="#0b0b0e"/>
<rect x="872" y="150" width="176" height="46" rx="12" fill="#1a1d28"/>
<rect x="950" y="100" width="16" height="44" fill="#0b0b0e"/>
<path d="M0 620 L1920 620 L1920 1080 L0 1080Z" fill="#0b0a0e"/>
<path d="M0 660 C500 620 1400 620 1920 660 L1920 720 L0 720Z" fill="#141218"/>
<g fill="#040306">
<ellipse cx="1300" cy="520" rx="62" ry="74" transform="rotate(24 1300 520)"/>
<path d="M1180 1080 L1190 640 C1210 590 1260 580 1300 590 C1350 600 1390 620 1400 680 L1420 1080Z"/>
<path d="M1220 760 C1260 740 1320 740 1360 770" stroke="#15131a" stroke-width="10" fill="none"/>
</g>
<path d="M1220 590 L1430 1080" stroke="#3a3a42" stroke-width="12" opacity="0.6"/>
<path d="M1252 540 Q1270 552 1288 544" stroke="#2a2630" stroke-width="3" fill="none"/>
<ellipse cx="560" cy="860" rx="230" ry="230" fill="none" stroke="#050407" stroke-width="42"/>
<path d="M330 860 L790 860" stroke="#050407" stroke-width="30"/>
<rect x="420" y="1010" width="40" height="70" rx="16" fill="#050407"/><rect x="660" y="1010" width="40" height="70" rx="16" fill="#050407"/>
<g fill="#ffa040"><circle cx="520" cy="694" r="5"/><circle cx="560" cy="694" r="5"/><circle cx="600" cy="694" r="5"/></g>
''', '<linearGradient id="ws3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#05060d"/><stop offset="1" stop-color="#262a3c"/></linearGradient>')
save("s3", s3)

# S4 — coming out of the tunnel, sodium lights fading behind the car
lamps = "".join(f'<circle cx="{960 + (i * 70)}" cy="{300 + i * 24}" r="{6 + i}" fill="#ffb24a"/><circle cx="{960 + i * 70}" cy="{300 + i * 24}" r="{30 + i * 4}" fill="#ffa040" opacity="0.25" filter="url(#blur8)"/>' for i in range(0, 6))
lamps += "".join(f'<circle cx="{960 - (i * 70)}" cy="{300 + i * 24}" r="{6 + i}" fill="#ffb24a"/><circle cx="{960 - i * 70}" cy="{300 + i * 24}" r="{30 + i * 4}" fill="#ffa040" opacity="0.25" filter="url(#blur8)"/>' for i in range(1, 6))
s4 = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky4)"/>
{stars(120, 300, 0.5)}
<path d="M0 420 L300 200 L560 300 L700 160 L1200 160 L1360 300 L1620 220 L1920 400 L1920 1080 L0 1080Z" fill="#141a26"/>
<path d="M520 820 L520 470 C520 260 700 160 960 160 C1220 160 1400 260 1400 470 L1400 820 Z" fill="#2c2b31"/>
<path d="M560 820 L560 480 C560 290 720 200 960 200 C1200 200 1360 290 1360 480 L1360 820 Z" fill="#1a130c"/>
<path d="M560 820 L560 480 C560 290 720 200 960 200 C1200 200 1360 290 1360 480 L1360 820 Z" fill="url(#tun)"/>
{lamps}
<path d="M560 820 L860 520 L1060 520 L1360 820Z" fill="#20180f"/>
<rect x="952" y="520" width="16" height="300" fill="#c9a24a" opacity="0.4"/>
<path d="M0 820 L1920 820 L1920 1080 L0 1080Z" fill="#0b0d13"/>
<path d="M460 1080 L700 820 L1220 820 L1460 1080Z" fill="#1b1c22"/>
<g transform="translate(960 900)">
<rect x="-210" y="-60" width="420" height="120" rx="30" fill="#040406"/>
<path d="M-150 -60 C-130 -150 130 -150 150 -60Z" fill="#040406"/>
<path d="M-120 -64 C-104 -128 104 -128 120 -64Z" fill="#0f1420"/>
<path d="M-112 -66 C-96 -120 96 -120 112 -66Z" fill="#ffa040" opacity="0.12"/>
<rect x="-200" y="-20" width="60" height="22" rx="6" fill="#ff2a2a"/><rect x="140" y="-20" width="60" height="22" rx="6" fill="#ff2a2a"/>
</g>
{glow(790, 890, 70, "#ff2a2a", 0.5)}{glow(1130, 890, 70, "#ff2a2a", 0.5)}
<path d="M-40 1080 C120 900 300 860 420 820 L460 1080Z" fill="#06070b"/>
<path d="M1960 1080 C1800 900 1620 860 1500 820 L1460 1080Z" fill="#06070b"/>
{fog(980, "#aab3c8", 0.10, 100)}
''', sky("sky4", "#04050d", "#101628", "#1c2234") +
    '<radialGradient id="tun" cx="0.5" cy="0.55" r="0.6"><stop offset="0" stop-color="#ffb24a" stop-opacity="0.35"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>')
save("s4", s4)

# S5 — the mirror: a woman in the back seat, head down
save("s5", mirror_scene(False))

# S6 — close on the back seat: dark water pooling and dripping
seat = svg(f'''
<rect width="{W}" height="{H}" fill="#060509"/>
<rect x="0" y="0" width="{W}" height="380" fill="#0a0a10"/>
<path d="M300 40 C700 10 1220 10 1620 40 L1600 330 L320 330Z" fill="#141a28"/>
<path d="M200 380 C200 300 260 270 380 270 L1540 270 C1660 270 1720 300 1720 380 L1720 720 L200 720Z" fill="#26222c"/>
<g stroke="#1a1720" stroke-width="7">{''.join(f'<line x1="{x}" y1="290" x2="{x}" y2="720"/>' for x in range(380, 1600, 150))}</g>
<path d="M160 720 C160 660 220 640 320 640 L1600 640 C1700 640 1760 660 1760 720 L1760 860 L160 860Z" fill="#2c2833"/>
<g stroke="#1e1b24" stroke-width="7">{''.join(f'<line x1="{x}" y1="650" x2="{x}" y2="860"/>' for x in range(380, 1600, 150))}</g>
<ellipse cx="980" cy="760" rx="300" ry="60" fill="#0d1018"/>
<ellipse cx="980" cy="760" rx="300" ry="60" fill="#5d6f8f" opacity="0.25"/>
<ellipse cx="930" cy="748" rx="120" ry="14" fill="#a9bad6" opacity="0.18"/>
<path d="M820 640 C760 560 820 470 980 460 C1140 470 1200 560 1140 640Z" fill="#0d1018" opacity="0.6"/>
<path d="M800 300 C780 420 760 560 820 640 L1140 640 C1200 560 1180 420 1160 300Z" fill="#0d1018" opacity="0.45"/>{drops(760, 300, 440, 340, 22, "#b7c6de", 0.5)}
<g fill="#b7c6de">
<path d="M1020 860 C1014 880 1010 892 1020 900 C1030 892 1026 880 1020 860Z" opacity="0.8"/>
<path d="M940 870 C935 890 931 900 940 908 C949 900 945 890 940 870Z" opacity="0.6"/>
<path d="M1100 880 C1095 898 1092 908 1100 914 C1108 908 1105 898 1100 880Z" opacity="0.5"/>
</g>
<rect x="0" y="860" width="{W}" height="220" fill="#08070b"/>
<ellipse cx="1000" cy="1000" rx="360" ry="50" fill="#5d6f8f" opacity="0.18"/>
<g>{''.join(f'<ellipse cx="{1000 + dx}" cy="1000" rx="{rx}" ry="{rx / 5:.0f}" fill="none" stroke="#a9bad6" stroke-width="2" opacity="{o}"/>' for dx, rx, o in ((20, 40, .5), (20, 90, .3), (20, 150, .15)))}</g>
{glow(960, 120, 260, "#ff2a2a", 0.10)}
''')
save("s6", seat)

# S7 — the gas station, red canopy light, the car parked, Dad and me standing by the pump
s7 = svg(f'''
<rect width="{W}" height="{H}" fill="url(#sky7)"/>
{stars(120, 360, 0.5)}
<path d="M0 520 L360 300 L640 420 L900 260 L1200 400 L1500 280 L1920 460 L1920 1080 L0 1080Z" fill="#10141f"/>
{pines(640, 50, "#070910", 80, 180)}
<rect x="0" y="640" width="{W}" height="440" fill="#121218"/>
<rect x="420" y="330" width="1080" height="70" fill="#1a0b0e"/>
<rect x="420" y="390" width="1080" height="14" fill="#ff3030"/>
{glow(960, 400, 300, "#ff2a2a", 0.30)}
<rect x="520" y="404" width="26" height="380" fill="#0a090c"/><rect x="1374" y="404" width="26" height="380" fill="#0a090c"/>
<polygon points="420,404 1500,404 1700,900 220,900" fill="#ff6a5a" opacity="0.07"/>
<g transform="translate(820 600)">
<rect x="0" y="0" width="90" height="190" rx="8" fill="#16151b"/>
<rect x="14" y="20" width="62" height="40" fill="#3a1416"/><rect x="14" y="20" width="62" height="40" fill="#ff3030" opacity="0.4"/>
<path d="M90 80 C130 80 130 140 150 150" stroke="#0a090c" stroke-width="8" fill="none"/>
</g>
<rect x="1580" y="520" width="240" height="170" fill="#0c0b10"/>
{lit_window(1610, 560, 180, 90, "#d9e2c0")}
<g transform="translate(1180 760)">
<rect x="-260" y="-70" width="520" height="120" rx="34" fill="#050508"/>
<path d="M-170 -70 C-150 -170 150 -170 170 -70Z" fill="#050508"/>
<path d="M-140 -74 C-124 -150 -10 -150 -10 -74Z" fill="#1a1d28"/><path d="M10 -74 C10 -150 124 -150 140 -74Z" fill="#1a1d28"/>
<circle cx="-170" cy="50" r="44" fill="#020203"/><circle cx="170" cy="50" r="44" fill="#020203"/>
</g>
{figure(930, 830, 330, "#040306")}
{figure(1010, 830, 280, "#040306")}
<ellipse cx="970" cy="836" rx="160" ry="16" fill="#000" opacity="0.6"/>
{fog(900, "#c8a0a8", 0.08, 120)}
''', sky("sky7", "#04050d", "#11162a", "#2a1a24"))
save("s7", s7)

# S8 — the mirror again: her head is up, and she is smiling
save("s8", mirror_scene(True))
