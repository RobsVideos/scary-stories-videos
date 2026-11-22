"""Scenes for The Sleep Lab."""
import sys; sys.path.insert(0, "../../toolkit")
from scenekit import *

IR_DEFS = '''<linearGradient id="irwall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0d1715"/><stop offset="1" stop-color="#22332e"/></linearGradient>
<linearGradient id="irfloor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1d2b27"/><stop offset="1" stop-color="#0a110f"/></linearGradient>
<pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="2" fill="#000" opacity="0.28"/></pattern>'''


def room_view(x, y, w, h, state="lie", label="RM 6", empty=False, eyes_on=True):
    """An infrared camera view of a sleep room, drawn in a 400x300 box scaled to (w,h)."""
    p = []
    p.append('<rect width="400" height="300" fill="url(#irwall)"/>')
    p.append('<polygon points="0,210 400,210 400,300 0,300" fill="url(#irfloor)"/>')
    p.append('<rect x="300" y="60" width="60" height="70" fill="#2b3d37" stroke="#0a110f" stroke-width="3"/>')  # framed picture
    p.append('<rect x="250" y="120" width="34" height="80" fill="#0e1714"/><circle cx="267" cy="132" r="4" fill="#d24a3a"/>')  # machine
    # bed
    p.append('<rect x="40" y="130" width="22" height="90" fill="#101a17"/>')
    p.append('<rect x="50" y="175" width="220" height="30" rx="6" fill="#3e524b"/>')
    p.append('<rect x="60" y="205" width="10" height="20" fill="#0a110f"/><rect x="255" y="205" width="10" height="20" fill="#0a110f"/>')
    p.append('<ellipse cx="95" cy="170" rx="34" ry="11" fill="#6f8780"/>')  # pillow
    if not empty:
        if state == "lie":
            p.append('<path d="M110 178 C130 150 230 150 262 172 L262 182 L110 182Z" fill="#5a716a"/>')
            p.append('<circle cx="98" cy="160" r="15" fill="#88a199"/>')
            p.append('<path d="M150 160 C190 150 230 140 256 128" stroke="#1a2622" stroke-width="2" fill="none"/>')
        else:
            p.append('<path d="M140 182 C160 168 230 165 262 176 L262 184 L140 184Z" fill="#5a716a"/>')
            p.append('<path d="M112 182 L118 104 C120 92 160 92 162 104 L166 182Z" fill="#8aa39b"/>')
            p.append('<rect x="132" y="80" width="16" height="16" fill="#8aa39b"/>')
            p.append('<ellipse cx="140" cy="66" rx="17" ry="21" fill="#9bb5ac"/>')
            if eyes_on:
                p.append('<circle cx="133" cy="64" r="3.4" fill="#f2fff9"/><circle cx="147" cy="64" r="3.4" fill="#f2fff9"/>')
                p.append('<g filter="url(#blur8)" opacity="0.7"><circle cx="133" cy="64" r="6" fill="#e0fff2"/><circle cx="147" cy="64" r="6" fill="#e0fff2"/></g>')
            p.append('<path d="M140 120 C190 126 230 128 256 128" stroke="#1a2622" stroke-width="2" fill="none"/>')
            p.append('<path d="M144 118 C190 140 230 136 256 134" stroke="#1a2622" stroke-width="2" fill="none"/>')
    p.append('<rect width="400" height="300" fill="url(#scan)"/>')
    p.append(f'<text x="14" y="26" font-family="{MONO}" font-size="18" fill="#cfe9df" opacity="0.85">{label}</text>')
    p.append('<circle cx="380" cy="20" r="6" fill="#ff3b2f"/>')
    return (f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 400 300" preserveAspectRatio="none">'
            + "".join(p) + '</svg>')


def desk_cam(x, y, w, h, with_figure=True):
    """Overhead camera view of the control room: the narrator at the desk, something behind."""
    p = ['<rect width="400" height="300" fill="#0e1614"/>',
         '<polygon points="0,0 400,0 330,70 70,70" fill="#0a100e"/>',
         '<rect x="70" y="190" width="260" height="60" fill="#1f2d29"/>',  # desk
         ''.join(f'<rect x="{90 + i * 40}" y="196" width="34" height="22" fill="#5d7c73"/>' for i in range(6)),
         '<rect x="70" y="190" width="260" height="60" fill="#7fe0c5" opacity="0.06"/>',
         # narrator from above/behind
         '<ellipse cx="200" cy="168" rx="46" ry="26" fill="#3a4c46"/>',
         '<circle cx="200" cy="148" r="18" fill="#53675f"/>',
         '<rect x="150" y="150" width="100" height="22" rx="10" fill="#26332f"/>']  # chair back
    if with_figure:
        p.append('<path d="M232 300 L236 120 C238 92 290 92 292 120 L296 300Z" fill="#030505"/>')
        p.append('<ellipse cx="264" cy="78" rx="20" ry="26" fill="#030505"/>')
        p.append('<path d="M236 126 C226 150 214 160 206 164" stroke="#030505" stroke-width="9" stroke-linecap="round" fill="none"/>')
        p.append('<circle cx="257" cy="76" r="3.2" fill="#ff3b2f"/><circle cx="271" cy="76" r="3.2" fill="#ff3b2f"/>')
        p.append('<g filter="url(#blur8)" opacity="0.8"><circle cx="257" cy="76" r="7" fill="#ff3b2f"/><circle cx="271" cy="76" r="7" fill="#ff3b2f"/></g>')
    p.append('<rect width="400" height="300" fill="url(#scan)"/>')
    p.append(f'<text x="14" y="26" font-family="{MONO}" font-size="18" fill="#cfe9df" opacity="0.85">CAM 1</text>')
    p.append('<circle cx="380" cy="20" r="6" fill="#ff3b2f"/>')
    return (f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 400 300" preserveAspectRatio="none">'
            + "".join(p) + '</svg>')


def monitor_grid(states, cam1=None, cx=960, top=230, sw=250, sh=180, gap=22):
    out = []
    total = 3 * sw + 2 * gap
    x0 = cx - total / 2
    out.append(f'<rect x="{x0 - 30}" y="{top - 30}" width="{total + 60}" height="{2 * sh + gap + 60}" rx="10" fill="#07090a"/>')
    for i in range(6):
        r, c = divmod(i, 3)
        x = x0 + c * (sw + gap); y = top + r * (sh + gap)
        out.append(f'<rect x="{x - 8}" y="{y - 8}" width="{sw + 16}" height="{sh + 16}" rx="6" fill="#141a1a"/>')
        if i == 0 and cam1 is not None:
            out.append(cam1(x, y, sw, sh))
        else:
            st = states[i]
            out.append(room_view(x, y, sw, sh, state=st, label=f"RM {i + 1}", empty=(st == "empty")))
    out.append(f'<rect x="{x0 - 40}" y="{top - 40}" width="{total + 80}" height="{2 * sh + gap + 80}" fill="#7fe0c5" opacity="0.10" filter="url(#blur60)"/>')
    return "".join(out)


def control_room(grid, tech=True):
    return f'''
<rect width="{W}" height="{H}" fill="#05080a"/>
<rect x="0" y="0" width="{W}" height="760" fill="url(#cwall)"/>
<g stroke="#0c1214" stroke-width="2">{''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in (120, 140))}</g>
{glow(960, 420, 520, "#3ec7a8", 0.16)}
{grid}
<polygon points="0,760 1920,760 1920,1080 0,1080" fill="#0c1112"/>
<rect x="300" y="740" width="1320" height="40" fill="#1a2224"/>
<rect x="300" y="740" width="1320" height="6" fill="#3d5a55" opacity="0.7"/>
<rect x="1310" y="690" width="44" height="52" rx="6" fill="#1b2022"/><path d="M1354 702 c22 0 22 28 0 28" stroke="#1b2022" stroke-width="8" fill="none"/>
<path d="M1318 680 c6 -20 -6 -30 2 -50" stroke="#9fb3ad" stroke-width="3" fill="none" opacity="0.3"/>
<rect x="520" y="700" width="260" height="40" rx="4" fill="#111618"/>
{''.join(f'<rect x="{530 + i * 25}" y="710" width="18" height="10" rx="2" fill="#1f292a"/>' for i in range(10))}
<circle cx="1500" cy="725" r="6" fill="#ff3b2f"/>{glow(1500, 725, 24, "#ff3b2f", 0.6)}
{'<g fill="#020304"><path d="M760 1080 C760 950 820 880 960 880 C1100 880 1160 950 1160 1080Z"/><ellipse cx="960" cy="820" rx="78" ry="92"/></g>' if tech else ''}
'''


CDEFS = IR_DEFS + sky("cwall", "#06090b", "#0d1517", "#121b1c")

# S1 — the control room, six sleepers
save("s1", svg(control_room(monitor_grid(["lie"] * 6)), CDEFS))

# S2 — the trainer's note on the monitor bezel
s2 = f'''
<rect width="{W}" height="{H}" fill="#06090a"/>
<rect x="300" y="120" width="1400" height="820" rx="24" fill="#121718"/>
<rect x="360" y="170" width="1280" height="720" fill="#0b1110"/>
{room_view(360, 170, 1280, 720, "lie", label="RM 6")}
<rect x="360" y="170" width="1280" height="720" fill="#000" opacity="0.35"/>
<g transform="translate(0 -230) rotate(-6 760 640)">
<rect x="560" y="470" width="420" height="380" fill="#000" opacity="0.5" filter="url(#blur30)"/>
<rect x="540" y="440" width="420" height="380" fill="#e6d38a"/>
<rect x="540" y="440" width="420" height="50" fill="#d4c073"/>
<text x="750" y="590" text-anchor="middle" font-family="{SERIF}" font-style="italic" font-size="46" fill="#2a1c12">If they sit up...</text>
<text x="750" y="690" text-anchor="middle" font-family="{SERIF}" font-weight="bold" font-size="50" fill="#8c1c1c">DON'T GO IN</text>
<text x="750" y="770" text-anchor="middle" font-family="{SERIF}" font-style="italic" font-size="44" fill="#2a1c12">just wait.</text>
</g>
{glow(760, 420, 300, "#ffcf7a", 0.12)}
'''
save("s2", svg(s2, IR_DEFS))

# S3/S4 — room six close up: lying, then sitting up and staring
def closeup(state):
    return f'''
<rect width="{W}" height="{H}" fill="#040606"/>
<rect x="330" y="60" width="1260" height="960" rx="30" fill="#111617"/>
{room_view(380, 110, 1160, 860, state, label="RM 6  03:00")}
<rect x="380" y="110" width="1160" height="860" fill="#7fe0c5" opacity="0.05"/>
{glow(960, 540, 600, "#3ec7a8", 0.10)}
'''
save("s3", svg(closeup("lie"), IR_DEFS))
save("s4", svg(closeup("sit"), IR_DEFS))

# S5 — turning up the room audio
wave = "M740 370 " + " ".join(f"L{754 + i * 15} {370 + (-1) ** i * (6 + (i * 37) % 55)}" for i in range(28))
s5 = f'''
<rect width="{W}" height="{H}" fill="#06080a"/>
<rect x="420" y="220" width="1080" height="720" rx="20" fill="#151b1d"/>
<rect x="420" y="220" width="1080" height="12" fill="#2a3739"/>
<rect x="720" y="280" width="480" height="160" rx="8" fill="#071210"/>
<path d="{wave}" stroke="#56e0b8" stroke-width="5" fill="none"/>
<path d="{wave}" stroke="#56e0b8" stroke-width="12" fill="none" opacity="0.4" filter="url(#blur8)"/>
<text x="740" y="310" font-family="{MONO}" font-size="24" fill="#56e0b8" opacity="0.8">RM 6 AUDIO</text>
{''.join(f'<rect x="{560 + i * 140}" y="500" width="14" height="300" rx="7" fill="#05080a"/><rect x="{530 + i * 140}" y="{720 - (i == 2) * 180 - (i * 23) % 60}" width="74" height="40" rx="6" fill="#8a9a9a"/>' for i in range(6))}
<circle cx="1370" cy="560" r="80" fill="#0b0f10"/><circle cx="1370" cy="560" r="62" fill="#2c3638"/>
<line x1="1370" y1="560" x2="1420" y2="510" stroke="#ff3b2f" stroke-width="8" stroke-linecap="round"/>
<circle cx="1460" cy="260" r="8" fill="#ff3b2f"/>{glow(1460, 260, 30, "#ff3b2f", 0.7)}
<g fill="#020304">
<path d="M700 1080 C690 960 730 870 790 830 C840 800 870 760 860 720 C858 700 880 690 896 704 C930 740 900 820 880 860 L940 1080Z"/>
</g>
{glow(960, 360, 420, "#3ec7a8", 0.14)}
'''
save("s5", svg(s5, IR_DEFS))

# S6 — every room sitting up
save("s6", svg(control_room(monitor_grid(["lie", "sit", "sit", "sit", "sit", "sit"],
                                         cam1=lambda x, y, w, h: desk_cam(x, y, w, h, with_figure=False))), CDEFS))

# S7 — hands flat on the desk
s7 = f'''
<rect width="{W}" height="{H}" fill="#040607"/>
<rect x="0" y="0" width="{W}" height="520" fill="#0b1415"/>
{glow(960, 260, 700, "#3ec7a8", 0.25)}
<polygon points="0,520 1920,520 1920,1080 0,1080" fill="#162022"/>
<polygon points="0,520 1920,520 1920,1080 0,1080" fill="url(#deskl)"/>
<g fill="#8b9a95">
<path d="M560 1080 L600 760 C604 720 640 700 680 700 L800 700 C840 700 860 720 860 750 L880 1080Z"/>
{''.join(f'<rect x="{600 + i * 58}" y="{610 + abs(i - 1.5) * 18:.0f}" width="46" height="130" rx="22"/>' for i in range(4))}
<rect x="830" y="700" width="40" height="110" rx="20" transform="rotate(35 850 750)"/>
<path d="M1360 1080 L1320 760 C1316 720 1280 700 1240 700 L1120 700 C1080 700 1060 720 1060 750 L1040 1080Z"/>
{''.join(f'<rect x="{1134 + i * 58}" y="{610 + abs(i - 1.5) * 18:.0f}" width="46" height="130" rx="22"/>' for i in range(4))}
<rect x="1050" y="700" width="40" height="110" rx="20" transform="rotate(-35 1070 750)"/>
</g>
<g fill="#000" opacity="0.35">
<path d="M560 1080 L600 860 L880 860 L880 1080Z"/><path d="M1360 1080 L1320 860 L1040 860 L1040 1080Z"/>
</g>
<rect x="0" y="0" width="{W}" height="520" fill="url(#scan)" opacity="0.4"/>
'''
save("s7", svg(s7, IR_DEFS + '<linearGradient id="deskl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3ec7a8" stop-opacity="0.25"/><stop offset="1" stop-color="#000" stop-opacity="0.4"/></linearGradient>'))

# S8 — screen one: the control room camera, and what stands behind the chair
s8 = f'''
<rect width="{W}" height="{H}" fill="#030404"/>
<rect x="330" y="60" width="1260" height="960" rx="30" fill="#111617"/>
{desk_cam(380, 110, 1160, 860, with_figure=True)}
{glow(1080, 380, 260, "#ff3b2f", 0.10)}
'''
save("s8", svg(s8, IR_DEFS))

# S6b — the count reaches one: screen one glows red
save("s6b", svg(control_room(monitor_grid(["lie", "sit", "sit", "sit", "sit", "sit"],
                                          cam1=lambda x, y, w, h: desk_cam(x, y, w, h, with_figure=False)))
                + glow(660, 320, 160, "#ff3b2f", 0.35), CDEFS))
