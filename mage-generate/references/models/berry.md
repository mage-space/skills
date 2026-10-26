# Berry (`berry`)

Mage's reference-driven video model (opt-in): very faithful to the images you give it, with generated dialogue and sound, from text, a first frame, up to 9 reference images, or a source video to edit. Berry 2 is the current version.

## Variants

| `model_id` | Character | Options |
|---|---|---|
| `berry-2` (default) | Literal: executes timecodes, counts and positions exactly, copies reference images closely, delivers scripted lines reliably | 480p, 720p, 1080p; 3–15 s |
| `berry` | Freer: more natural, improvised acting; timecodes are soft hints; its filter is stricter; English prompts work better than other languages; the only variant that edits video | 720p, 1080p; 3–15 s |

- Pick `berry-2` for consistent characters, props and positions, multi-shot sequences and dialogue-heavy scenes. Pick `berry` (or `berry-2` written loosely, below) for one character's restrained, emotional acting.
- Results vary noticeably from run to run: when a shot matters, plan two or three takes and pick one. Draft at 480p on `berry-2`.

## How Mage sends your prompt

- Mage sends `prompt` unchanged, in one of four modes picked by the inputs: text only; `first_image` (the clip starts on it; the output takes its shape); references in `image` + `additional_images` (1 to 9); or a source `video` to edit (`berry` only).
- A first frame and reference images never mix. There is no last frame.
- No negative-prompt field and no prompt rewriting: everything, including exclusions, lives in the prompt.
- Sound (dialogue, effects, ambience, music) is always generated; steer it or silence it in the prompt.
- **Image citations**: Berry's own convention is `[Image N]`, square brackets and a space (`[Image1]` without the space breaks it). Mage rewrites a mention like `@mara` to plain `character from image N`. For full control, pass each character's image (from `list_characters`) in `image` or `additional_images` yourself and cite `[Image N]` in that order; Berry takes no voices, so nothing is lost. If you do mention `@handles`, the numbering is your own images first, then characters, then references, in the order first mentioned.

## Prompt structure

Formula: **scene + subject + motion + sound + quality and consistency**. Put sound notes after the action.

**Reference video** (four blocks):

```
[Image 1] is the scene: <place>. [Image 2] is <name>. [Image 3] is <name>.
<One style sentence: visual style + light direction + colour grade + texture.>
[Image 2] <name>: <silhouette, costume, emotional state>.
[Image 3] <name>: <silhouette, costume, emotional state>.
<Body: timecoded beats or loose narration, with lines.>
<Footer: lip sync and complete lines; faces and costumes of [Image 2] and [Image 3] stay identical; no subtitles, captions, logos or watermarks.>
```

- Declare every image's job on the first line. For scenes with people: `[Image 1]` the location, then one image per character. Give a product its own image so it is placed as a hero object rather than worn.
- Name what you take from an image: "the woman in a red qipao from [Image 1]", "the fan from [Image 2]".

**First frame**: the frame already shows the look. Write only 2 or 3 concrete action verbs, one camera instruction and the sound, in one to three short sentences. Never restate clothing, face or background.

**Text to video**: an opening paragraph with the look (style, grade, lens character, "16:9 widescreen"), a `Characters:` line and a `Location:` line, then timecoded beats, then a physics-and-consistency footer.

**Timecodes or loose narration**:

| Scene | Write |
|---|---|
| Positions, props, multi-shot, brand rhythm | Timecoded beats: `[00:00-00:04] Medium shot. ...` |
| Dialogue-heavy scenes | Timecoded beats, at most 2 lines per beat |
| One character's subtle emotion, long pauses, monologue | Loose narration in natural order, no timecodes, no "pause two seconds" |
| A dense stream of continuous action | Continuous narration, no timecodes |

`berry-2` follows timecodes and numbers literally, which can make emotional scenes stiff; that is when to drop them.

**Camera gets its own paragraph**, never mixed into the acting. Say what it must not do ("no shake, no zoom, no cut"), and give push-in amounts ("pushes in slowly and evenly from a chest-up shot to a face close-up, about 1.3x"). A fixed-camera prompt must not imply any push-in anywhere.

## Vocabulary

- **Camera**: low tracking shot, aerial chase angle, front crash-zoom, slow-motion side wide shot, hard cut to rear tracking, slow dolly in, drone shot, orbit, binocular POV with a circular vignette, "single continuous shot, no cuts, no camera movement".
- **Look stacks**: "teal-and-orange blockbuster grade, IMAX-scale spectacle, anamorphic lens flares, practical destruction realism"; "photorealistic luxury fashion-ad cinematography, warm low sun, shallow depth of field, elegant motion blur, 24fps film look".
- **Style guards**: "ink-wash animation style maintained throughout, no colour shift"; "NOT illustration, NOT anime"; "original design, not resembling existing characters".
- **Specific beats vague**: "the camera slowly pushes from full body to a chest close-up" over "the camera moves"; "her hair streams to the right in the wind" over "moving".

## References, characters, and frames

- Each character's reference image shows that one person only.
- Lock identity in the footer: "Keep [Image 2]'s face, hair and costume identical in every shot."
- **Storyboard sheets**: a grid as `[Image 1]`, then "Follow panel order 1 to 9, left to right, top to bottom"; number cells ("Cell 4 (middle left): ..."); Berry splits the time between cells, and one 15-second clip can cover 9 cells.
- **`berry-2` copies text from references**: it will render a storyboard's captions and cell numbers. Use reference images without text, and add the text ban in the footer.
- **Longer stories in several clips**: keep the same first-line declaration, style sentence, character cards and footer in every clip and change only the body. Open each body with "Continuing from the previous clip: <positions, hands, light, prop states>." For tighter joins, add a frame from the middle and the last frame of the previous clip as extra references.
- **Editing a video** (`berry`, `video` of 3 to 60 seconds; only the first 15 seconds are used, and the output keeps that length): always pair what to change with what stays exactly as it is.
  - Object swap: restate the motion the new object inherits (path, speed, direction, contact points) and that its light and shadows match the source.
  - Style change: name every element to re-skin (mountains, mist, buildings) and keep "the camera path and scene layout unchanged".
  - A reference image plus text beats either alone for materials and costumes; refer to it as `Image 1`.
  - Several edits: one sentence per edit, each with its own keep clause.
  - `audio_setting: "origin"` keeps the source's sound and `"auto"` makes new sound; it passes through though `get_model` does not list it.

## Audio and dialogue

- **Formats**: `[Mara / low, restrained / "You wrote all night."]` inside timecoded beats; a line folded into narration for loose acting ("she says, barely audible: 'I was wrong about you.'"); or plain `Jun says quietly: "Let's go."`.
- **Timing**: in Chinese about 4 characters per second, times 1.2 for emotional delivery, plus 0.5 to 1 second of slack: a 5-second window fits about 17 characters. In English keep each line to one short sentence. At most 2 lines per time window gives the best lip sync.
- **Silence**: a placeholder like `[Jun / silent / tense / no line]` stops Berry inventing filler. Write "No dialogue" for a wordless clip.
- **Lip sync misses**: fewer lines, a longer window, no entrance action for a character already on screen, a speaking verb right before the line ("she opens her mouth and says: ..."). Narrator lines (`Narrator: "..."`) clash less with lip sync than on-screen speech.
- **Language**: write a line in the language the character speaks (Japanese for a Japanese school scene, Korean for a Korean drama).
- **Sound effects and music** go at the end of each beat or of the prompt: "Screaming engine, rotor thunder closing in", "Music drops to silence, only wind", "Driving percussive score slams back in on landing".

## Text in the image

- Ban text in the footer: "No subtitles, captions, printed text, logos or watermarks on screen."
- When text belongs in the scene, control it instead of banning it: allow it as soft, illegible background texture ("old vertical brush calligraphy on the scrolls, soft-focus, unreadable") and forbid legible blocks of text.
- A product's own logo: "Every cap and shoe shows the red star logo clearly; no text overlays, no extra graphics."

## Avoid

| Problem | Write instead |
|---|---|
| Over-acting, wailing | A forbidden list: "no loud crying, no exaggerated sobbing, no head shaking" |
| Berry "adds drama" or filler lines | A shorter clip, silence placeholders, beats that cover the whole duration |
| Restating the first frame | Action, camera and sound only |
| Captions copied from a storyboard | Text-free references and a footer ban |
| Morphing faces, vehicles or props | "Stable character and vehicle design throughout, no morphing, no deformation" |
| Camera directions mixed into the acting | A separate camera paragraph |

## Examples

**Two characters from references** (`berry-2`, 10 s; `image` = the study, `additional_images` = the two people):

```
[Image 1] is the scene: a candle-lit study at night. [Image 2] is the scholar. [Image 3] is his wife.
Realistic period drama, warm candlelight from the right, low-saturation grade, fine film grain, real skin texture.
[Image 2] the scholar: dark round-collared robe, hair tied up, tired and restrained.
[Image 3] his wife: pale embroidered jacket, simple bun, calm, holding back her feelings.
[00:00-00:04] Medium shot. She walks to the desk, her eyes falling on the unfinished letter. [The wife / quiet / "You wrote all night."]
[00:04-00:07] Close shot. He stops his brush mid-stroke and looks up. [The scholar / tired / "It had to be finished."]
[00:07-00:10] Two-shot. They hold each other's gaze; the candle flame wavers. [Both / silent / no line]
Camera: fixed, no shake, no zoom, no cut.
Lips sync naturally and every line is spoken in full. Keep the faces and costumes of [Image 2] and [Image 3] identical. No subtitles, printed text, logos or watermarks.
```

**First frame** (`berry-2`, 5 s):

```
She slowly turns her head toward the window as a breeze lifts strands of her hair, then smiles. Fixed camera, medium close-up. Sound: cicadas outside, a soft breeze.
```

**Action from text** (`berry-2`, 12 s, 16:9):

```
High-octane motorcycle chase across a collapsing suspension bridge at sunset. Photorealistic, teal-and-orange grade, anamorphic lens flares, heavy smoke. 16:9 widescreen.
Characters: The Rider, an athletic man in his 30s in a black leather jacket, no helmet, on a matte-black sport bike. Location: a suspension bridge over a bay, abandoned cars across the lanes.
[00:00-00:04] Low tracking shot. The Rider weaves between abandoned cars at full speed as steel cables snap overhead. Screaming engine, metallic shrieks.
[00:04-00:08] Front crash-zoom. The roadway ahead cracks and tilts upward; he accelerates up the rising slab like a ramp. Groaning metal, engine at redline.
[00:08-00:12] Slow-motion side wide shot. The bike sails over the gap against the burning sky, then lands hard on the far side, suspension compressing, sparks flying. Music drops out, then a percussive score slams back in on landing.
Realistic vehicle physics. Stable rider and motorcycle design throughout, no morphing, no deformation. No text, no watermarks, no subtitles on screen.
```

**Editing a video** (`berry`, `video` + one reference image):

```
Replace the white cruise ship in the video with the spaceship from Image 1. The spaceship follows the ship's original path, speed and heading exactly, and its light, reflections and shadows match the source lighting. The water, the sky and the camera path stay 100% unchanged.
```

**Restrained emotion, written loosely** (`berry` or `berry-2`, 8 s, one reference):

```
[Image 1] is the woman. Realistic drama, one continuous shot with no cuts. Soft warm light from the upper right, shallow depth of field. Keep her face, hair and dress identical to [Image 1].
She begins calm, eyes lowered, then presses her lips together and her brows draw in slightly. She speaks very softly, each word catching in her throat: "I was wrong about you." Her eyes fill; one small tear runs down her left cheek and she holds back from crying aloud. She does not look up, shake her head or turn away.
Camera: starts at a chest-up shot and pushes in very slowly and evenly to her face, about 1.3x; no shake, no zoom, no cut.
No subtitles or on-screen text.
```
