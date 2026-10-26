# Plum (`plum`)

Mage's full-feature video model. Every clip comes with generated audio. It handles dialogue, characters with their own voices, first and last frames, reference images and audio, edits of a source video, and output up to 2K. Opt-in: run it only when the user asks for Plum.

## Variants

| `model_id` | For | `resolution` | `duration` (s) | Frames |
|---|---|---|---|---|
| `plum` | Finals and motion at 2K | `768P`, `2K` | 4–15 | First, last, or both |
| `plum-max` | Faster finals | `480P`, `768P` | 5–15 | A last frame needs a first |
| `plum-fast` (default) | Drafts; the cheapest | `480P`, `768P` | 4–15 | A last frame needs a first |

One prompt suits all three: draft on `plum-fast`, then change only `model_id` for the final. On `plum-max`, an edit's source video bills above the output rate.

## How Mage sends your prompt

Plum expands your prompt into its own detailed script before it renders. Write it a director's brief in plain language and let Plum do that expansion; never write a script format yourself. Keep the brief under 7,000 characters.

| Mode | What you fill | Limits |
|---|---|---|
| Text only | Nothing but `prompt` | `aspect_ratio` applies |
| Frames | `first_image` and/or `last_image` | Shape comes from the frame; no reference images or handles |
| References | `image`, `additional_images`, and handles of characters, references, audio | 9 images at most, handles counted; audio needs an image beside it; `aspect_ratio` applies |
| Edit | `videos` with exactly one 2–15 s clip | 2 images at most, handles counted; no frames, no audio, `use_character_voices: false` for a voiced character |

**What Plum calls each input.** Mage replaces each handle with a positional name:

| In your prompt | Plum reads |
|---|---|
| `@image1` (your first upload) | `image 1` |
| `@jun`, a saved character | `character from image 2` |
| `@jun`, if he has a saved voice | `character from image 2 with voice from [Audio 1]` |
| `@harbor`, a saved location | `location from image 3` |
| `@waves`, a saved audio clip | `[Audio 1]` |

- **Image numbering.** Uploads come first (`image`, then `additional_images`). Mentioned characters follow, ordered by first mention, and mentioned object, location, pose and outfit references come last, ordered the same way.
- **Audio numbering.** Saved audio clips come first, ordered by first mention, then each mentioned character's own voice, up to three in all. Plum gets audio only through handles; save a new clip with `create_reference` (`kind: "audio"`) before mentioning it.
- **The source video** of an edit has no handle. Call it `video 1`.
- **Use these names, not descriptions.** For any input you name yourself, write `image N`, `[Audio N]` or `video 1`, so every name matches what Plum receives. Plum wants every input named and given a job.
- **Handles only after `@`.** Any `@` plus a word is read as a saved handle, and the request is refused when nothing matches. `@Image 1` therefore fails. Spell out email addresses and social handles in dialogue ("jun at harbor dot com").
- **Sound is always on.** Plum generates audio on every clip, so the brief must say what the clip should sound like and what to keep out.
- **Long clips get trimmed.** Audio clips that add up to more than 15 s are trimmed, splitting the time evenly. Say which part of a voice clip matters.

## Prompt structure

A complete brief has four parts, in this order. Leave out the first when nothing is attached.

```text
Inputs: image 1 is the character reference; keep her face, cropped silver hair and green bomber jacket. image 2 is the environment reference. [Audio 1] is her voice.
Concept: <one sentence: subject, place, action, style, any special camera treatment, the camera movement, the editing style>.
0–3 s: <shot size>. <what is on screen>. <camera>. <action>. <exact line in quotes>. <sound effects>.
3–7 s: Cut to <shot size>. <...>
Requirements: <look, palette, lighting, text rules, character rules>. No <what must not appear>. <music: describe it, or "Do not add any additional background music.">
```

- **Inputs.** Number each input as Plum receives it and give it one job. Add the features that must not change. Write out the exact words to keep for any audio Plum should copy.
- **Concept.** One sentence that sets up the whole clip. Tie each element to its input in parentheses: "a courier (image 1) races across a rooftop market (image 2)". Plum cuts between shots by default; write "one continuous take" when it should not.
- **Timeline.** Split `duration` into time ranges that add up to it exactly. In each range, give the shot size, what is visible, the camera move, the action, any dialogue word for word, and the sound effects.
- **Requirements.** Rules that hold across the whole clip, then exclusions as "No ..." and "Do not ..." lines. Plum has no negative-prompt field.
- **Short asks.** A short ask can be two or three sentences with the jobs inline. For example: "Image 1: mood and film grain. Image 2: the courier. Image 3: the ending logo. Story: ... Tone cool and premium; edit fast and fashion-forward."

**Writing by mode:**

- **Text only.** With nothing attached, Plum invents everything. Give at least the subject's appearance, the setting, the action and the style. Plan coverage in layers: a wide shot for the space, a medium shot for the action, a close-up for the detail.
- **Frames.** Say which frame opens the clip and which ends it. Between two frames, Plum adds no cut: it generates the motion, light change and sound that link them. Describe that path as "one natural, continuous shot with no cuts".
- **References.** List the inputs, write the concept, then the timeline.
- **Edits.** A plain instruction per change works best. Say what changes and what stays: "In video 1, replace the cat with a dog." "Replace the view outside the window in video 1 with image 1." "Change the final line from '...' to '...'." "Relight video 1 from midday to blue dusk."

## Vocabulary

- **Shot sizes:** extreme close-up, close-up, medium close-up (waist-up), medium shot, wide shot, establishing wide, over-the-shoulder, POV.
- **Coverage:** shot/reverse-shot for conversations; facial close-ups for tension; a wide shot to establish a new place.
- **Camera treatments:** aerial shot, one continuous take, slow motion, handheld, locked-off, fast lateral tracking, subtle push-ins and pull-backs. For an orbit, write "truck left while panning right"; "orbiting camera" is less reliable.
- **Editing styles:** standard cuts, hard cuts, jump cuts, smash cuts, beat-synced cuts, fast cuts, white-flash cuts, cuts hidden behind a passing object, dissolves or fades, and J-cuts and L-cuts for dialogue.
- **Look:**
  - Name lighting the camera can see: "a cool, soft front-side key", "backlight keeps the foreground dark and the distance bright", "shallow depth of field with snow as soft bokeh".
  - Name the palette: "low-saturation cold blue, ink green and charcoal".
  - Name the texture: "heavy grain", "halftone dots".
- **Plain, visible language:** Plum follows direct visual description more reliably than metaphor. Write what the camera sees, not what the scene feels like.

## References, characters, and frames

- **Jobs an input can have:**
  - character (keep the face or design), object, or environment;
  - opening or ending frame;
  - voice (keep the timbre);
  - storyboard (one image per shot);
  - style (copy the visual language, not the content) or composition (copy the placement);
  - motion or camera motion;
  - audio reuse, whole or a stated time range;
  - the clip to edit.
- **Partial use.** For style and mood inputs, add "Reference only the stated qualities; do not reproduce the image itself."
- **Faces.** Faces drift unless the person is attached and named as the character reference; a description alone will not hold one.
- **At every cut,** name the new framing and which established character is on screen: "Cut to a medium close-up of the courier (image 1)".
- **Motion from a video:** "she performs the dance from video 1; her appearance follows image 1."

## Audio and dialogue

- **Exact lines.** Write every spoken line word for word, in quotes, after its speaker: `The courier (image 1) says, breathless: "Last drop of the night."`
- **Fit and continuity:**
  - Match the words to the time range. Too much dialogue in a short shot is the main cause of broken lip sync.
  - Name the time ranges a line spans, for example "she continues speaking from the previous shot".
- **Off-screen voices:**
  - Mark a speaker the camera cannot see as off-screen or voiceover.
  - When a cut reveals the speaker, say so: "Cut to a close-up of the old man, revealing him as the voice."
- **Voices:**
  - A voiced character's handle already brings its voice. For any other voice clip, write "Her voice timbre follows [Audio 1]".
  - When only the timbre is wanted, never repeat the clip's words.
- **Languages:** dialogue holds best in Arabic, Chinese, English, French, German, Italian, Japanese, Korean, Portuguese, Russian and Spanish. Keep each line in the language it should be spoken in.
- **Sound effects** go in the time range where they happen; steady ambience goes in Requirements.
- **Music.** Describe the score you want (instruments, tempo, where it builds), or end with "Do not add any additional background music."

## Text in the image

- **Exact wording.** Quote every word that should appear: `The following English text appears on screen: "NIGHT MARKET".` / `The phone screen displays the title "Track Order" and a button labeled "Open Map".`
- **One main text element per shot,** and never over a face or the eyes.
- **Spelling.** Add "All text is spelled and rendered correctly, with no garbled characters." when text matters.
- **Logos.** Attach a brand logo as an image with the job "ending logo". To keep brands out, add "Do not reproduce brands, logos or text from the inputs".
- **No text.** When nothing should be written, add "No subtitles, on-screen text, watermarks or stickers."

## Avoid

| Problem | Fix |
|---|---|
| The whole brief as one unbroken paragraph | Inputs, concept, timed shots, requirements |
| An input with no stated job | "image 2 is the environment reference." |
| Music asked for, plus "no background music" | Keep one, or give each section its own rule |
| "One continuous take" with several timed shots | One continuous paragraph of action, no time ranges |
| A face expected to stay the same with nothing attached | Attach the character and name it as the character reference |
| A text-only brief that is too short | Appearance, setting, action and style at the least |

Requests Mage refuses:

- Frames together with references.
- A last frame alone on `plum-max` or `plum-fast`.
- Audio handles with no image.
- More than two images, or any audio, in an edit.
- Time ranges that run past `duration`.

## Examples

Text only, 10 s, `aspect_ratio: 9:16`:

```text
Concept: a vertical live-action standoff in a cramped noodle shop at night, natural short-form drama performances, shot mainly in medium close-ups with shot/reverse-shot cutting.
0–4 s: Medium close-up. A young cook in a stained white apron slams a ladle on the counter and glares across it. He says, voice tight: "You said you'd pay me Friday."
4–8 s: Cut to a medium close-up of the owner, a heavy-set man in a cardigan, slowly folding his newspaper. He answers flatly: "It is Friday. Tomorrow."
8–10 s: Cut back to the cook, jaw clenched, steam rising between them from a pot.
Requirements: warm tungsten light, red paper lanterns soft in the background, shallow depth of field. Pots bubble and a fan hums throughout. No subtitles, watermarks or stickers. Do not add any additional background music.
```

Opening and ending frames, 6 s:

```text
The opening frame shows a paper boat at the edge of a rain puddle; the ending frame shows it caught against a storm drain grate. Animate the boat from the opening frame to the ending frame in one natural, continuous shot with no cuts: a gust pushes it off, it spins once, rides the stream along the curb and lodges against the grate. Low angle at street level, rain pattering, water gurgling into the drain.
```

References, 8 s (an upload in `image`, plus `@jun` with a voice and `@harbor`):

```text
Inputs: @jun is the character reference; keep his face, round glasses and orange windbreaker. @harbor is the environment reference. image 1 is the object reference: the matte black thermos; keep its shape and white logo exactly.
Concept: at dawn on the harbor, Jun (image 2) pours tea from the thermos (image 1) and toasts the fishing boats heading out, cinematic and calm, a slow push-in, standard cuts.
0–4 s: Wide shot. Jun sits on a bollard as boats slide past in the mist. He unscrews the thermos and steam curls up. Gulls cry, engines thrum in the distance.
4–8 s: Cut to a medium close-up of Jun. He raises the cup toward the boats and says quietly: "Bring them all home." The camera pushes in slowly.
Requirements: cold blue dawn light with a warm glow on his face from the east. No on-screen text. Do not add any additional background music.
```

Brand film in short form, 15 s, `aspect_ratio: 16:9`:

```text
A 16:9 premium outdoor-gear film. Image 1: mood, setting and film grain. Image 2: the climber. Image 3: the backpack. Image 4: the ending logo. Story: on a windy ridge at sunrise, the climber pulls the backpack tight, scrambles up the last rocks and stands at the summit as the sun breaks through. Tone cool and confident; edit fast, with beat-synced cuts.
```

Edit (`videos` holds the clip; `image` holds the jacket):

```text
In video 1, replace the grey suit jacket on the man with the red leather jacket from image 1, keeping its zips and collar. Keep his face, his movements, the camera path, the street and the original audio unchanged.
```
