# Breaking a video down with rea-video

[rea-video](https://github.com/JuneYaooo/rea-video) (Apache-2.0) reverse-engineers a video shot by shot. This skill pins its v0.1.0 commit, `1b4a340957bdc25155deec55489523bdb3412842`. Upgrade it deliberately, after reading its changelog, never by installing `main`.

## Install

```bash
pipx install "rea-video[ocr] @ git+https://github.com/JuneYaooo/rea-video@1b4a340957bdc25155deec55489523bdb3412842"
```

- **No pipx:** a virtual environment works the same way:

  ```bash
  python3 -m venv ~/.venvs/rea-video
  ~/.venvs/rea-video/bin/pip install "rea-video[ocr] @ git+https://github.com/JuneYaooo/rea-video@1b4a340957bdc25155deec55489523bdb3412842"
  ~/.venvs/rea-video/bin/rea-video --help
  ```

- **`externally-managed-environment`:** use pipx or the virtual environment; never `--break-system-packages`.
- **No matching `onnxruntime` wheel:** the default Python is too new. Pick a 3.10 to 3.14 interpreter: `pipx install --python python3.12 …`.
- **Two OpenCV builds** (Python 3.12 and below with `[ocr]`): the OCR extra pulls in the GUI `opencv-python` beside `opencv-python-headless`. Remove it once: `pipx runpip rea-video uninstall -y opencv-python`, then `pipx runpip rea-video install --force-reinstall --no-deps "opencv-python-headless>=4.8,<5"`.
- **ffmpeg:** `brew install ffmpeg` on macOS, `sudo apt install ffmpeg` on Debian and Ubuntu.

## Run

```bash
rea-video decompose video.mp4 -o breakdown/ref --lang en
rea-video summary breakdown/ref/breakdown.json
rea-video review breakdown/ref
```

| Flag | When |
|---|---|
| `--lang en` or `zh` | The package's language: the user's, or English for any language rea-video doesn't write |
| `--no-stems` | Skip the voice and music separation (and its model download, about 220 MB on first use) |
| `--no-ocr` | Skip on-screen text: faster, but no caption timeline |
| `--ocr-lang ja` | Captions in Japanese (downloads a recognition model on first use) |
| `--vlm` | Only when the user has set up a vision model for rea-video themselves. Never ask for an API key in the chat, and never open a `.env` file |

rea-video works without a vision model. When you can see images, you are its vision model: do the review below.

## Review every shot

`rea-video review breakdown/ref` writes `review_tasks.json` (each shot's images, the tools' call and evidence, a priority) and `review_answers.json` (the template you fill). Its `instructions` field defines every field; it may be in Chinese.

1. Look at `storyboard.jpg`, then each shot's sheet `shots/shot_NNN.jpg` (first, middle, and last frames): every `priority: high` shot, then as many others as you can.
2. For each shot you looked at, fill:
   - `label_probs`: the 11 kinds (`live_action`, `ai_video`, `avatar`, `cg_3d`, `code_render`, `screen_capture`, `still_motion`, `static_hold`, `anim_2d`, `stop_motion`, `film_footage`), summing to 1. Spread them when you're unsure (`ai_video` 0.55, `live_action` 0.45).
   - `evidence`: a list of what you can see: real hands and a real kitchen, warped text, a face that drifts, physics that fails.
   - `description`: the subject, action, setting, and camera.
   - `narrative`: the shot's `role` in the story and its `point` in one line, written so it holds without the original's product.
   - At the top: `story` (`summary`, the `hook`, two to four `highlights` with the second and why each works) and `cast` (characters, scenes, and props, described well enough to redraw).
   - Leave shots you didn't look at as they are; leave `replication` empty (the remake writes its own prompts).
3. Merge: `rea-video apply-review breakdown/ref --by agent`. The merge weighs your answers against hard evidence, such as a 24 fps source padded to 30 or an AI label in the file's metadata, so it may keep a call you disagreed with. Tell the user which and why.

Judging tips:

- A platform download is recompressed: "no sensor noise" no longer means AI. Trust what you see: real hands, real rooms, natural physics, a phone's wobble.
- Flat shapes, crisp type, and perfectly smooth motion are usually code; a 3D look with stable geometry is a render; warped hands, drifting textures, and melting text are AI.
- 2D animation, stop motion, and film clips are yours to call: the tools can't measure them.

## Read the package

| File | Read it for |
|---|---|
| `REEL.md` | The verdict, the share of each kind by duration, open questions, and a map of the rest |
| `reel/timeline.md` | One line per shot: `#07 16.2-18.5 \| seen … \| cam … \| over … \| made~ … \| real~ … \| remake … · G1 \| flag …`. Keys ending in `~` are inferred; `G1` groups shots that share a set and cast |
| `reel/shots/<n>.md` | One shot: what is visible, what was inferred and why, and its frames |
| `reel/sound.md` | Voice, music tempo and key, sound effects with times, and whether cuts land on the beat |
| `reel/packaging.md` | Every caption and styled text with its time, color, outline, and entrance; stickers |
| `reel/look.md` | For filmed shots: framing, camera, light, and grade |
| `reel/content.md`, `reel/cast.md` | The story's steps, the script, and the cast |

Useful exports: `packaging/subtitles.srt` (the caption timeline) and `packaging/overlays.ass` (the caption styles). Use their times and styles, with the user's words.

Skip `breakdown.json` (very large), the report's remake section, and `reel/remake.md`: they plan for other services' models, and the remake here runs on Mage. The original's frames and stems are for study, never inputs to a generation.
