#!/usr/bin/env python3
"""Builds a vertical (1080x1920) scary-story Short from a story folder.

Usage:  python3 toolkit/make_short.py stories/<date>-<slug>
Needs in the story folder: story.json and one <scene id>.svg per scene (drawn by the folder's scenes.py).
Writes into the story folder: <slug>.mp4, caption.txt, timeline.json (and work files under _work/).
See toolkit/README.md for the story.json format.
"""
import json, os, re, subprocess, sys, shutil
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.expanduser("~/.cache/scary-kokoro")
MODEL_URL = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/"
FPS, W, H, SH = 30, 1080, 1920, 1350
SY = (H - SH) // 2
LEAD, END_GAP, END_HOLD = 3.5, 0.4, 3.8


def sh(*a, **k): return subprocess.run(a, check=True, **k)


def ensure_deps():
    try:
        import kokoro_onnx, soundfile, scipy, PIL  # noqa
    except ImportError:
        sh(sys.executable, "-m", "pip", "install", "--break-system-packages", "-q", "kokoro-onnx", "soundfile", "scipy", "pillow")
    os.makedirs(CACHE, exist_ok=True)
    for f in ("kokoro-v1.0.onnx", "voices-v1.0.bin"):
        p = os.path.join(CACHE, f)
        if not os.path.exists(p) or os.path.getsize(p) < 1_000_000:
            sh("curl", "-sSL", "--retry", "3", "-o", p, MODEL_URL + f)


# ---------------------------------------------------------------- narration
def narrate(story, work):
    import soundfile as sf
    from kokoro_onnx import Kokoro
    k = Kokoro(os.path.join(CACHE, "kokoro-v1.0.onnx"), os.path.join(CACHE, "voices-v1.0.bin"))
    voice, speed = story.get("voice", "am_onyx"), story.get("speed", 0.88)
    pauses = {int(a): b for a, b in story.get("pauses", {}).items()}
    sr = 24000; out = [np.zeros(int(LEAD * sr), np.float32)]; t = LEAD; lines = []
    for i, text in enumerate(story["lines"]):
        s, sr = k.create(text, voice=voice, speed=speed, lang="en-us")
        lines.append({"i": i, "start": round(t, 3), "end": round(t + len(s) / sr, 3), "text": text})
        out.append(s.astype(np.float32)); t += len(s) / sr
        p = pauses.get(i, 1.1 if (text.endswith("...") or len(text) < 40) else 0.6)
        out.append(np.zeros(int(p * sr), np.float32)); t += p
    sf.write(os.path.join(work, "voice.wav"), np.concatenate(out), sr)
    return lines, t


def anchor(a, lines):
    """{'line': i, 'edge': 'start'|'end', 'offset': s} -> seconds."""
    if isinstance(a, (int, float)): return float(a)
    ln = lines[a["line"]]
    return ln[a.get("edge", "start")] + a.get("offset", 0.0)


# ---------------------------------------------------------------- sound effects
def build_sfx(story, lines, scenes, total, work):
    import soundfile as sf
    from scipy.signal import butter, sosfilt, fftconvolve
    SR = 48000; N = int(total * SR); rng = np.random.default_rng(3)
    L = np.zeros(N); R = np.zeros(N)
    t_ = lambda d: np.arange(int(d * SR)) / SR
    bp = lambda x, lo, hi: sosfilt(butter(2, [lo, hi], "bandpass", fs=SR, output="sos"), x)
    lp = lambda x, f: sosfilt(butter(2, f, "lowpass", fs=SR, output="sos"), x)
    hp = lambda x, f: sosfilt(butter(2, f, "highpass", fs=SR, output="sos"), x)
    norm = lambda x: x / (np.max(np.abs(x)) + 1e-9)

    def place(sig, at, gain_db=0.0, pan=0.0):
        i = int(max(0, at) * SR); sig = sig[: max(0, N - i)] * 10 ** (gain_db / 20)
        L[i:i + len(sig)] += sig * np.sqrt((1 - pan) / 2) * 1.414
        R[i:i + len(sig)] += sig * np.sqrt((1 + pan) / 2) * 1.414

    def fade(sig, fi=0.5, fo=0.5):
        a = np.ones(len(sig)); fi, fo = int(fi * SR), int(fo * SR)
        if fi: a[:fi] = np.linspace(0, 1, fi)
        if fo: a[-fo:] = np.minimum(a[-fo:], np.linspace(1, 0, fo))
        return sig * a

    def room(sig, decay=0.5, mix=0.25):
        n = int(decay * SR); tail = rng.standard_normal(n) * np.exp(-np.linspace(0, 7, n))
        out = np.concatenate([sig, np.zeros(n)]); wet = fftconvolve(sig, lp(tail, 3000))
        wet = np.pad(wet, (0, max(0, len(out) - len(wet))))[: len(out)]
        return out + wet / (np.max(np.abs(wet)) + 1e-9) * np.max(np.abs(sig)) * mix

    # beds (looping textures, length d)
    def wind(d):
        n = rng.standard_normal(int(d * SR)); tt = t_(d)
        lfo = 0.55 + 0.45 * np.sin(2 * np.pi * 0.11 * tt + 1.3) * np.sin(2 * np.pi * 0.047 * tt)
        return norm((norm(bp(n, 180, 900)) * 0.6 + norm(bp(n, 900, 2400)) * 0.15 * lfo ** 2) * lfo)

    def drone(d, base=55.0, rise=0.0):
        tt = t_(d); f = base * (1 + rise * tt / max(d, 1e-3)); ph = 2 * np.pi * np.cumsum(f) / SR
        s = np.sin(ph) + 0.6 * np.sin(ph * 1.06) + 0.35 * np.sin(ph * 1.5 + 0.4) + 0.2 * np.sin(ph * 2.01)
        return norm(s * (0.75 + 0.25 * np.sin(2 * np.pi * 0.2 * tt)) + 0.4 * norm(lp(rng.standard_normal(len(tt)), 160)))

    def rain(d):
        n = rng.standard_normal(int(d * SR)); drops = (rng.random(len(n)) > 0.9993) * rng.standard_normal(len(n)) * 6
        return norm(norm(bp(n, 800, 6000)) * 0.5 + hp(drops, 2000))

    beds = {
        "wind": lambda d: (wind(d), -24), "room": lambda d: (norm(lp(rng.standard_normal(int(d * SR)), 220)), -30),
        "drone": lambda d: (drone(d, 52, 0.06), -24), "drone_rise": lambda d: (drone(d, 55, 0.12), -22),
        "drone_deep": lambda d: (drone(d, 41, -0.08), -20), "rain": lambda d: (rain(d), -24), "none": None,
    }

    # one-shots
    def knock():
        tt = t_(0.35); body = sum(a * np.sin(2 * np.pi * f * tt) for f, a in ((85, 1), (132, .7), (215, .45), (340, .2))) * np.exp(-tt * 22)
        return norm(room(body + lp(rng.standard_normal(len(tt)), 1800) * np.exp(-tt * 90) * .8, .9, .35))

    def tick(hi=True):
        tt = t_(0.05); s = hp(rng.standard_normal(len(tt)), 1500) * np.exp(-tt * 180) + np.sin(2 * np.pi * (2600 if hi else 2100) * tt) * np.exp(-tt * 120) * .6
        return norm(room(s, .25, .2))

    def lock():
        out = np.zeros(int(.6 * SR))
        for at, f in ((0, 3100), (.18, 2500), (.24, 4100)):
            tt = t_(.12); s = bp(rng.standard_normal(len(tt)), 1800, 7000) * np.exp(-tt * 120) + np.sin(2 * np.pi * f * tt) * np.exp(-tt * 60) * .5
            i = int(at * SR); out[i:i + len(s)] += s
        return norm(room(out, .4, .2))

    def step():
        tt = t_(.25); s = lp(rng.standard_normal(len(tt)), 900) * np.exp(-tt * 30) + np.sin(2 * np.pi * 70 * tt) * np.exp(-tt * 25) * .8
        return norm(room(s, .6, .3))

    def creak(d=1.6):
        tt = t_(d); f = 220 + 90 * np.sin(2 * np.pi * .7 * tt) + 40 * rng.standard_normal(len(tt)).cumsum() / SR
        s = np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * (0.5 + 0.5 * np.sin(2 * np.pi * 23 * tt))
        return norm(room(bp(s, 300, 2500) * np.sin(np.pi * tt / d), .7, .3))

    def heartbeat_one():
        tt = t_(.5); thump = lambda o: np.sin(2 * np.pi * 50 * (tt - o)) * np.exp(-np.clip(tt - o, 0, None) * 18) * (tt >= o)
        return norm(thump(0) + .7 * thump(.22))

    def beep(d=.16):
        tt = t_(d); return np.sin(2 * np.pi * 960 * tt) * np.minimum(1, tt * 200) * np.minimum(1, (d - tt) * 60)

    def boom(d=3.5, f0=90, f1=32):
        tt = t_(d); f = f1 + (f0 - f1) * np.exp(-tt * 2.5)
        return norm(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 1.2) + lp(rng.standard_normal(len(tt)), 120) * np.exp(-tt * 3) * .5)

    def thunder(d=4.0):
        tt = t_(d); crack = hp(rng.standard_normal(len(tt)), 1500) * np.exp(-tt * 14)
        rumble = lp(rng.standard_normal(len(tt)), 140) * np.exp(-tt * .9) * (0.6 + 0.4 * np.sin(2 * np.pi * 1.3 * tt))
        return norm(crack * .5 + norm(rumble))

    def riser(d=3.0):
        tt = t_(d); return norm(bp(rng.standard_normal(len(tt)), 400, 3000) * (tt / d) ** 2.5)

    def whisper(d=2.5):
        tt = t_(d); n = bp(rng.standard_normal(len(tt)), 2500, 7000)
        env = np.clip(np.sin(2 * np.pi * 3.1 * tt) * np.sin(2 * np.pi * 1.7 * tt + 1), 0, None) ** 1.5
        return norm(room(n * env * np.sin(np.pi * tt / d), .8, .4))

    def static(d=2.0):
        tt = t_(d); return norm(hp(rng.standard_normal(len(tt)), 1000) * (0.7 + 0.3 * (rng.random(len(tt)) > .5)))

    def phone(d=3.0):
        tt = t_(d); on = ((tt % 1.0) < .55)
        return norm((np.sin(2 * np.pi * 440 * tt) + np.sin(2 * np.pi * 480 * tt)) * on * (0.6 + 0.4 * np.sin(2 * np.pi * 20 * tt)))

    def glass():
        tt = t_(1.2); s = sum(np.sin(2 * np.pi * f * tt) * np.exp(-tt * (6 + i * 3)) for i, f in enumerate((3100, 4700, 6200, 8300)))
        return norm(room(s + hp(rng.standard_normal(len(tt)), 3000) * np.exp(-tt * 30), .6, .3))

    def repeat(fn, d, every, gain=0.0):
        out = np.zeros(int(d * SR)); k = 0
        while k * every < d - 0.05:
            s = fn(k); i = int(k * every * SR); out[i:i + len(s)] += s[: max(0, len(out) - i)]; k += 1
        return out

    oneshots = {
        "knock": lambda e: (knock(), -3), "knock3": lambda e: (repeat(lambda k: knock(), 2.2, .9), -3),
        "clock": lambda e: (repeat(lambda k: tick(k % 2 == 0), e.get("dur", 8), 1.0), -20),
        "lock": lambda e: (lock(), -10), "footsteps": lambda e: (repeat(lambda k: step(), e.get("dur", 4), e.get("every", .65)), -10),
        "creak": lambda e: (creak(e.get("dur", 1.6)), -12), "heartbeat": lambda e: (repeat(lambda k: heartbeat_one(), e.get("dur", 6), e.get("every", .85)), -6),
        "monitor": lambda e: (repeat(lambda k: beep(), e.get("dur", 4), 1.15), -18),
        "flatline": lambda e: (fade(np.sin(2 * np.pi * 960 * t_(e.get("dur", 2.2))), .02, .6), -20),
        "boom": lambda e: (boom(4.0, 70, 26), -2), "hit": lambda e: (boom(2.0, 110, 40), -6), "thunder": lambda e: (thunder(), -6),
        "riser": lambda e: (riser(e.get("dur", 3.0)), -20), "whisper": lambda e: (whisper(e.get("dur", 2.5)), -16),
        "static": lambda e: (static(e.get("dur", 2.0)), -22), "phone": lambda e: (phone(e.get("dur", 3.0)), -18),
        "glass": lambda e: (glass(), -10),
    }

    place(boom(3.2), 0.2, -8)  # title hit
    for sc in scenes:
        if sc.get("bed", "none") in (None, "none") or sc["id"] in ("_title", "_end"): continue
        sig, g = beds[sc["bed"]](sc["end"] - sc["start"] + 0.6)
        place(fade(sig, 1.5, 1.2), sc["start"] - 0.3, g + sc.get("bed_gain", 0))
    for e in story.get("events", []):
        if e["sfx"] not in oneshots: print("unknown sfx, skipped:", e["sfx"]); continue
        sig, g = oneshots[e["sfx"]](e)
        place(sig, anchor(e["at"], lines), g + e.get("gain", 0), e.get("pan", 0))
    place(riser(3.0), total - END_HOLD - 3.0, -22)
    place(boom(4.0, 70, 26), total - END_HOLD - 0.05, -2)  # ending stinger
    mix = np.stack([L, R], 1); mix /= max(1.0, np.max(np.abs(mix)) / 0.9)
    sf.write(os.path.join(work, "sfx.wav"), mix.astype(np.float32), SR)


# ---------------------------------------------------------------- pictures
def build_frames(story, lines, scenes, total, sdir, work):
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
    fm = lambda q: subprocess.run(["fc-match", "-f", "%{file}", q], capture_output=True, text=True).stdout
    SERIF, BOLD, REG = fm("DejaVu Serif"), fm("Inter:extrabold"), fm("Inter")
    BG = (7, 5, 8)

    def text_center(d, y, s, font, fill, sp=0):
        w = d.textlength(s, font=font) + sp * (len(s) - 1); x = (W - w) / 2
        for ch in (s if sp else [s]):
            d.text((x, y), ch, font=font, fill=fill); x += d.textlength(ch, font=font) + sp

    def fit(d, s, size, maxw, path):
        while size > 40 and d.textlength(s, font=ImageFont.truetype(path, size)) > maxw: size -= 4
        return ImageFont.truetype(path, size)

    def card(rows):
        im = Image.new("RGB", (W, H), BG); g = Image.new("RGB", (W, H), BG)
        ImageDraw.Draw(g).ellipse((90, 700, 990, 1220), fill=(70, 14, 20))
        im = Image.blend(im, g.filter(ImageFilter.GaussianBlur(120)), 0.6); d = ImageDraw.Draw(im)
        for y, s, size, fill, sp, path in rows: text_center(d, y, s, fit(d, s, size, 960, path), fill, sp)
        return im

    title = story["title"]; words = title.split()
    if len(words) == 1: t1, t2 = "", title
    elif words[0].lower() in ("the", "a", "an"): t1, t2 = words[0], " ".join(words[1:])
    else:  # most even two-line split
        k = min(range(1, len(words)), key=lambda k: max(len(" ".join(words[:k])), len(" ".join(words[k:]))))
        t1, t2 = " ".join(words[:k]), " ".join(words[k:])
    title_card = card([(760, t1, 130, (233, 226, 208), 4, SERIF), (920, t2, 104, (233, 226, 208), 3, SERIF),
                       (1120, "A SCARY STORY", 40, (169, 159, 140), 14, REG)])
    end = story.get("end_card", ["Sleep well."])
    end_rows = [(760 + i * 130 - (len(end) - 3) * 60, s, 96, (179, 38, 30) if i == len(end) - 1 else (216, 207, 189), 3, SERIF) for i, s in enumerate(end)]
    end_card = card(end_rows)

    panels = {}
    for sc in scenes:
        if sc["id"] in ("_title", "_end") or sc["id"] in panels: continue
        png = os.path.join(work, f"p_{sc['id']}.png")
        sh("rsvg-convert", "-w", str(round(1920 * SH / 1080)), "-h", str(SH), os.path.join(sdir, f"{sc['id']}.svg"), "-o", png)
        im = Image.open(png).convert("RGB"); left = round(sc.get("cx", 960) * SH / 1080 - W / 2)
        left = max(0, min(im.width - W, left)); panels[sc["id"]] = im.crop((left, 0, left + W, SH))

    # captions: balanced chunks (<=5 words), timed by character share
    chunks = []
    for ln in lines:
        parts = [p.strip() for p in re.split(r"(?<=[.?!])\s+|(?<=\.\.\.)\s*", ln["text"]) if p and p.strip()]
        out = []
        for p in parts:
            ws = p.split(); k = -(-len(ws) // 5); size = -(-len(ws) // k)
            out += [" ".join(ws[j:j + size]) for j in range(0, len(ws), size)]
        tot = sum(len(p) for p in out); t = ln["start"]; span = ln["end"] - ln["start"]
        for p in out:
            d = span * len(p) / tot; chunks.append((t, t + d, p)); t += d
    caps = [(a, min(chunks[i + 1][0] if i + 1 < len(chunks) else total, b + .6), s) for i, (a, b, s) in enumerate(chunks)]

    header = story["title"].upper(); cache = {}

    def frame(sid, cap):
        if sid == "_title": return title_card
        if sid == "_end": return end_card
        im = Image.new("RGB", (W, H), BG); im.paste(panels[sid], (0, SY)); d = ImageDraw.Draw(im)
        text_center(d, 140, header, fit(d, header, 50, 900, SERIF), (226, 218, 200), 6)
        d.line((390, 225, 690, 225), fill=(140, 28, 28), width=3)
        if cap:
            f = ImageFont.truetype(BOLD, 64); rows, cur = [], ""
            for w_ in cap.split():
                t = (cur + " " + w_).strip()
                if d.textlength(t, font=f) > 860 and cur: rows.append(cur); cur = w_
                else: cur = t
            rows.append(cur); y0 = 1300 - (len(rows) - 1) * 40
            for i, r in enumerate(rows):
                d.text(((W - d.textlength(r, font=f)) / 2, y0 + i * 80), r, font=f, fill=(255, 255, 255), stroke_width=7, stroke_fill=(0, 0, 0))
        return im

    segs = []
    for sc in scenes:
        a, b = sc["start"], sc["end"]
        cuts = sorted({a, b} | {x for c in caps for x in c[:2] if a < x < b})
        for s, e in zip(cuts, cuts[1:]):
            mid = (s + e) / 2
            cap = None if sc["id"] in ("_title", "_end") else next((c[2] for c in caps if c[0] <= mid < c[1]), None)
            key = (sc["id"], cap)
            if key not in cache:
                cache[key] = os.path.join(work, f"f_{len(cache):03d}.png"); frame(sc["id"], cap).save(cache[key])
            segs.append({"png": cache[key], "start": s, "end": e,
                         "fade_in": 0.5 if (s == a and sc.get("fade_in", True)) else 0,
                         "fade_out": (1.5 if sc["id"] == "_end" else 0.5) if (e == b and sc.get("fade_out", True)) else 0})
    return segs


def encode(segs, work, out_mp4):
    lst = os.path.join(work, "list.txt")
    with open(lst, "w") as fh:
        for i, s in enumerate(segs):
            F = round(s["end"] * FPS) - round(s["start"] * FPS)
            if F <= 0: continue
            D = F / FPS; vf = f"format=yuv420p,loop=-1:1,trim=duration={D}"
            if s["fade_in"]: vf += f",fade=t=in:st=0:d={min(s['fade_in'], D)}"
            if s["fade_out"]: fo = min(s["fade_out"], D); vf += f",fade=t=out:st={D - fo}:d={fo}"
            o = os.path.join(work, f"seg_{i:03d}.mp4")
            sh("ffmpeg", "-nostdin", "-y", "-v", "error", "-framerate", str(FPS), "-i", s["png"], "-vf", vf, "-frames:v", str(F),
               "-r", str(FPS), "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-pix_fmt", "yuv420p", o + ".tmp.mp4")
            os.replace(o + ".tmp.mp4", o); fh.write(f"file '{os.path.basename(o)}'\n")
    sh("ffmpeg", "-nostdin", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", os.path.join(work, "video.mp4"))
    sh("ffmpeg", "-nostdin", "-y", "-v", "error", "-i", os.path.join(work, "voice.wav"), "-i", os.path.join(work, "sfx.wav"), "-filter_complex",
       "[0:a]aresample=48000:resampler=soxr,highpass=f=60,equalizer=f=3500:t=q:w=1.2:g=2,pan=stereo|c0=c0|c1=c0[v];"
       "[1:a]volume=0.8[s];[v][s]amix=inputs=2:normalize=0:duration=longest,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]",
       "-map", "[a]", "-c:a", "pcm_s16le", os.path.join(work, "mix.wav"))
    sh("ffmpeg", "-nostdin", "-y", "-v", "error", "-i", os.path.join(work, "video.mp4"), "-i", os.path.join(work, "mix.wav"), "-map", "0:v", "-map", "1:a",
       "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-shortest", "-movflags", "+faststart", out_mp4 + ".tmp.mp4")
    os.replace(out_mp4 + ".tmp.mp4", out_mp4)


def main(sdir):
    ensure_deps()
    story = json.load(open(os.path.join(sdir, "story.json")))
    work = os.path.join(sdir, "_work"); shutil.rmtree(work, ignore_errors=True); os.makedirs(work)
    lines, t_end = narrate(story, work)
    end_start = lines[-1]["end"] + END_GAP; total = end_start + END_HOLD
    # scene windows
    sc_in = story["scenes"]; scenes = [{"id": "_title", "start": 0.0, "end": LEAD}]
    starts = []
    for j, sc in enumerate(sc_in):
        st = LEAD if j == 0 else anchor(sc["at"] if "at" in sc else {"line": sc["from_line"], "edge": "start", "offset": -0.25}, lines)
        starts.append(st)
    for j, sc in enumerate(sc_in):
        nxt = starts[j + 1] if j + 1 < len(sc_in) else end_start
        d = dict(sc); d["start"], d["end"] = starts[j], nxt
        if sc.get("cut"): d["fade_in"] = False; scenes[-1]["fade_out"] = False
        scenes.append(d)
    scenes.append({"id": "_end", "start": end_start, "end": total})
    for a, b in zip(scenes, scenes[1:]):
        assert b["start"] > a["start"] + 0.3, f"scene {b['id']} starts too soon after {a['id']}"
    build_sfx(story, lines, scenes, total, work)
    # voice must be at least `total` long for the mix; pad it
    import soundfile as sf
    v, sr = sf.read(os.path.join(work, "voice.wav"), dtype="float32")
    if len(v) < int(total * sr): sf.write(os.path.join(work, "voice.wav"), np.pad(v, (0, int(total * sr) - len(v))), sr)
    segs = build_frames(story, lines, scenes, total, sdir, work)
    slug = story["slug"]; out = os.path.join(sdir, f"{slug}.mp4")
    encode(segs, work, out)
    json.dump({"lines": lines, "scenes": scenes, "total": total}, open(os.path.join(sdir, "timeline.json"), "w"), indent=1)
    tags = story.get("hashtags", ["#scarystories", "#horrorstories", "#creepy", "#scary", "#horrortok", "#fyp"])
    open(os.path.join(sdir, "caption.txt"), "w").write(f"{story['title']}\n\n{story.get('hook', '')}\n\nFollow for a new scary story every day.\n\n{' '.join(tags)}\n")
    print(f"OK {out} {total:.1f}s")


if __name__ == "__main__":
    main(sys.argv[1].rstrip("/"))
