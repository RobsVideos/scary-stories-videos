# Daily scary story kit

Everything here lives on the **`videos`** branch. Each day gets one folder `stories/YYYY-MM-DD-<slug>/`.
`stories/2026-11-10-the-farmhouse-rule/` is the reference video the owner approved: match its quality, pacing and look.

## Daily steps

1. **Write the story.** New, original, never a retelling of a known creepypasta, film or book. Read the titles in
   `stories/` first so you never repeat a premise. 10–14 short lines of first-person narration, 55–75 s of speech
   (about 150–190 words). Shape: a hook in line 1, an everyday setting, a rule or warning, slow escalation, one
   quiet beat of dread, and a twist in the last line that lands like a punch. Simple words, no gore, no slurs,
   nothing about real people or real crimes. Every line is spoken, so write for the ear; use "..." for a held breath.
2. **Plan 6–9 scenes.** Each scene is a still illustration that covers one or more lines (`from_line`). Change
   scene every 1–3 lines. Plan the sound: one bed per scene and 3–6 timed effects on the key beats.
3. **Draw the scenes.** Write `scenes.py` in the story folder using `toolkit/scenekit.py`
   (`svg`, `sky`, `stars`, `moon`, `fog`, `glow`, `lit_window`, `dead_tree`, `figure`, `eyes`, `grass`, `save`).
   Raw SVG shapes are fine and expected for anything specific to the story; see
   `stories/2026-11-10-the-farmhouse-rule/scenes_example.py` for the level of detail. Canvas is 1920×1080; only an
   864-wide strip around the scene's `cx` is shown, so keep the subject inside it. Dark night palette, silhouettes,
   one or two warm or red accent lights, soft fog and glow. No text in scenes except short signs.
   Run `python3 scenes.py` inside the folder, then **look at** the `_check_*.png` files and fix anything unreadable.
4. **Write `story.json`** (format below) and run `python3 toolkit/make_short.py stories/<folder>`.
5. **Check** a few frames of the output (`ffmpeg -ss <t> -i <mp4> -frames:v 1 x.png`): captions readable,
   subject visible in each panel, no blank scenes. Fix and re-run if needed.
6. **Publish** (see the daily task prompt): commit the folder (mp4, caption.txt, story.json, scenes.py, svgs) and push.

## story.json

```json
{
 "title": "The Farmhouse Rule",
 "slug": "2026-11-10-the-farmhouse-rule",
 "hook": "One-sentence teaser used in the post caption.",
 "voice": "am_onyx", "speed": 0.88,
 "lines": ["line 0", "line 1", "..."],
 "pauses": {"4": 3.0},
 "scenes": [
   {"id": "s1", "from_line": 0, "cx": 1010, "bed": "wind"},
   {"id": "s6b", "at": {"line": 9, "edge": "end", "offset": 0.3}, "cx": 960, "bed": "room", "cut": true}
 ],
 "events": [
   {"sfx": "knock3", "at": {"line": 4, "edge": "end", "offset": 0.3}},
   {"sfx": "clock", "at": {"line": 3, "edge": "start", "offset": 0.3}, "dur": 7.5, "pan": 0.55}
 ],
 "end_card": ["Never answer", "the door", "after midnight."],
 "hashtags": ["#scarystories", "#horrorstories", "#creepy", "#scary", "#horrortok", "#fyp"]
}
```

- `pauses`: seconds of silence after a line (default 0.6, or 1.1 for short lines). Leave 2.5–3 s after a line
  that is followed by a sound beat (knocks, a phone ringing).
- `scenes`: in order. The first scene starts after the 3.5 s title card. A scene starts 0.25 s before its
  `from_line`, or at an explicit `at` anchor. `cut: true` swaps in with no fade (for a changed version of the
  same picture). `cx` is the horizontal centre of the shown strip (default 960).
- Scene `bed` (background loop): `wind`, `rain`, `room`, `drone`, `drone_rise`, `drone_deep`, `none`.
- Event `sfx`: `knock`, `knock3`, `clock` (dur), `lock`, `footsteps` (dur, every), `creak` (dur),
  `heartbeat` (dur, every), `monitor` (dur), `flatline` (dur), `hit`, `boom`, `thunder`, `riser` (dur),
  `whisper` (dur), `static` (dur), `phone` (dur), `glass`. Optional `gain` (dB) and `pan` (-1..1).
- `end_card`: 2–3 short lines shown at the end; the last line is drawn in red. It should echo the story's rule
  or twist.
- The title card, header, captions, title boom and ending stinger are added automatically.

Output: `<slug>.mp4` (1080×1920, 30 fps, about 60–80 s), `caption.txt` (post text with hashtags),
`timeline.json`.

Voice and model files download automatically to `~/.cache/scary-kokoro` on first run (about 340 MB from GitHub).
