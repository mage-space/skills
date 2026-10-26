# MiniMax-H3 (`minimax_h3`)

MiniMax-H3 is an open video model (opt-in) that makes video and stereo audio together. It handles dialogue, characters with their voices, reference images, video and audio, and first and last frames. It is cheap, and the Turbo variant runs clips up to 15 s. Use it when the user asks for it.

## Variants

| `model_id` | For | `duration` (s) | `resolution` |
|---|---|---|---|
| `minimax-h3-turbo` (default) | Drafts, long clips, price | 5–15 | `480p`, `544p`, `720p`, `768p` |
| `minimax-h3` | The full-step model | 5–8 | `480p`, `544p`, `720p`, `768p` |

`768p` is the model's native size, and `544p` is the biggest speed saving below it. `aspect_ratio` takes `21:9`, `16:9`, `3:2`, `5:4`, `1:1`, `4:5`, `2:3`, `9:16` or `9:21`. Both variants read a prompt the same way.

## How Mage sends your prompt

Apart from the `@handle` rewrite below, your prompt reaches the model unchanged. No rewriter expands it, so the structure below is entirely up to you. The fields you fill choose the mode:

| Mode | Fields | Rules |
|---|---|---|
| Text only | none | `aspect_ratio` applies |
| Frames | `first_image`, `last_image`, each alone or both | The canvas follows the frame's shape. No references |
| References | `image`, `additional_images`, `videos` (up to 3, 2–15 s each), and `@handles` | Up to 9 images, handles included. Audio needs an image or a video alongside |

**Reference budget.** The references share a 21-second budget with the clip. Count `duration`, plus 2 s for each image, mentioned character and mentioned reference, plus 1.15 s for each second of each reference video, counted up to `duration`. For example, a 5 s clip has room for 8 images, but a 15 s clip has room for 3.

**Labels.** The model numbers its inputs per type, in this order. They are the labels it was trained on:

| Label | Inputs, in order |
|---|---|
| `<Picture N>` | `image`, then `additional_images`, then mentioned characters in order of first mention, then mentioned references (object, location, pose, outfit) in order of first mention |
| `<Audio N>` | Audio-reference handles in order of first mention, then the voices of mentioned characters (3 slots in all), then each reference video's own soundtrack |
| `<Video N>` | `videos` in order |

In frame mode, the frame line names the first frame `Picture 1` and the last frame `Picture 2`, or `<Picture 1>` when the last frame stands alone.

**Handle rewrite.** Before the model sees the prompt, Mage rewrites each handle into words that do not match those labels:

| You write | The model reads |
|---|---|
| `@image2` | `image 2` |
| `@mara` (a character) | `character from image 3` |
| `@mara` (a character with a voice) | `character from image 3 with voice from [Audio 1]` |
| `@cabin` (a location reference) | `location from image 4` |
| `@rain` (an audio reference) | `[Audio 1]` |

Bridge the two in `subject_definitions`: mention each handle once there, next to its label, then use only labels. `<Subject 1> is the woman in <Picture 3> (@mara), with short black hair...` reaches the model as `<Subject 1> is the woman in <Picture 3> (character from image 3 with voice from [Audio 1]), with short black hair...`. For an uploaded image, write its `<Picture N>` label directly; it needs no handle.

- This model is built to read labelled inputs, and each input needs a stated role.
- Any `@word` is read as a handle, and one that matches nothing is refused. Never write an email address or a social handle; in dialogue, write "at".
- Every clip has audio. Describe the sound you want, and state what to leave out.

## Prompt structure

This follows MiniMax's own prompt-writing guide for the model. Write the sections in English, but keep dialogue, lyrics, and on-screen text in their original language. The timeline must fill `duration` exactly.

**Text only or frames.** Start with the frame line (frames only) and a blank line, then write three fields in this order:

```text
integrated_multimodal_description: [Shot 1] <style>, <shot size> frames <subject, place, starting state>. <camera move as a sentence>. <actions, reactions, dialogue, synced sounds>. [Shot 2] At 00:05.000, the camera cuts to <something new>...

overall_soundscape: <1–4 sentences: ambience, physical sounds, breaths and laughs across the whole clip>

non_diegetic_music: <1–3 sentences: score instruments, tempo, rhythm, dynamics; or N/A>
```

Copy the frame line exactly. `S.SS` is the clip length with two decimals, and `N` is the number of the last shot.

| Frames | First line |
|---|---|
| First only | `For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.` |
| First and last | `How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot N) aligns with the S.SS-second mark of the target video.` |
| Last only | `How the reference pictures align with the target video — <Picture 1> (from [Shot N]) aligns with the S.SS-second mark of the target video.` |

- **First frame:** open on what `<Picture 1>` shows (style, subjects, composition), keeping identity, clothing, colors and layout. Then write the action's start, its development, and its result.
- **First and last:** write one shot unless the user asks for cuts. Describe the path between the frames: the first state, the visible changes, the narrowing differences, then the last state. Never describe the two stills again.
- **Last only:** invent a plausible earlier state and converge on `<Picture 1>` in the final shot.

**References.** Write six sections in this order:

```text
subject_definitions:
<Subject 1> is the woman in <Picture 1> (@mara), <visible traits to keep>.
<Subject 2> is the red sneaker in <Picture 2>, <traits>.
<Audio 1> is the voice-timbre reference for <Subject 1> (S1).

summary:
[reference generation + audio reference] <one short paragraph: the target video and the role of each label>

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - <what is kept>.
<Audio 1>: reference - <what carries over>.

detailed_description:
<one or two style sentences>
[Shot 1] ... [Shot 2] At 00:04.000, the shot cuts to ...

overall_soundscape:
<as above>

non_diegetic_music:
<as above>
```

- **`<Subject N>`** is content you reuse: a person, place, object, outfit, style or motion. One subject can draw on several inputs, for example "whose face comes from <Picture 1> and whose walk comes from <Video 1>". Use `<Picture N>` on its own only when the image is a frame or a storyboard for given shots.
- **`<Video N>`** stands for a whole video: the clip to edit, the clip to continue, or the source of camera, cut or rhythm structure. A person or motion taken from a video is still a `<Subject N>`.
- **`summary`** opens with its task types in brackets, joined by `+`: `keyframe completion` (an image is a frame of the target), `reference generation` (inputs guide a character, place, style or motion), `video editing` (begin "The target video is an edited version of <Video 1>."), `video continuation`, `audio reuse` (the same audio plays), `audio reference` (only its timbre, rhythm or style carries over).
- **`retention_analysis`** gets one line per label. For visuals, mark it `fully_preserved`, `partially_preserved`, `attribute_transfer` or `weak_reference`. For audio, mark it `fully_copy`, `partially_copy`, `reference` or `weak_reference`.
- **`detailed_description`** runs 350–500 words for a generation; an edit scales with its source. For each shot, give the composition, the subjects and where they stand, the setting and light, the actions, the camera, the sound, and where each label applies.

## Vocabulary

- **Camera moves:** `push in` / `pull out` (the camera travels), `zoom in` / `zoom out` (only the lens), `pan left/right`, `truck left/right`, `tilt up/down`, `pedestal up/down`, `arc shot`, `tracking shot`, `static shot`, `shake slightly/strongly`, `POV`, `roll clockwise/counterclockwise`.
- **Size and pace of a move:** add `with small amplitude` / `with large amplitude` and `at slow speed` / `at fast speed` only when they matter. Write the move as a sentence inside its shot: "The camera holds a static shot as the runner exits the frame." For an orbit, write truck left plus pan right.
- **Style that opens `[Shot 1]`:** `Live-action, cinematic`, `2D-animated`, `3D CG`, `claymation`, `watercolor`, `vintage film`. With frames, take the style from the frame.
- **Cuts:** write `the camera cuts to` or `the shot switches to`, and give each cut new information (a subject, space, state, viewpoint or time); for a tighter framing, move the camera instead. Use a cross-dissolve, fade or wipe only when the user asks for one.
- **Concrete over abstract:** write "shallow depth of field, backlight keeps the foreground dark", not "beautiful, cinematic".

## References, characters, and frames

- **Roles:** give every input one stated role: character, object, environment, frame, voice, storyboard, style, composition, motion, camera motion, or audio reuse.
- **Fixed features:** name the features of an input that must not change.
- **Faces:** a face holds only when the person is attached, through a character handle or an image. Never expect text alone to keep a face.
- **At every cut:** state the framing and which `<Subject N>` is on screen. Keep the label, and never redefine it.
- **Reference videos:** a reference video costs budget for each second, so trim it to the part you need before attaching it.

## Audio and dialogue

- **Speakers:** each voice gets a stable ID, `(S1)`, `(S2)`, or `(S1,S2)` for a line spoken together; characters who never make a sound get none, and a referenced subject who speaks is `<Subject 1> (S1)`. Describe each voice once, outside the tag, when it first appears: age, gender, on or off screen, pitch, timbre, pace, accent.
- **Lines:** write `<d>[English] exact words.</d>`, with only the language tag and the words inside, never translated. Fit the words to the shot: a long speech in a 3-second shot breaks the lip sync.
- **Voiceover:** write `says in an off-screen voiceover:` before the line, and add "while her lips remain completely closed" after the `</d>`.
- **A line that crosses a cut:** put `<scenetrans>` at both joins and add "continues seamlessly across the cut". For speech that the end of the clip cuts off, use `<cutoff>`.
- **Voice reference:** write `<Audio N> is the voice-timbre reference for <Subject 1> (S1).` When only the timbre carries over, leave out the clip's words. For reuse, write out the exact words or lyrics, with `[unclear]` for any you cannot make out.
- **Sound layers:** synced sounds and in-scene music go in the description; ambience and physical sounds in `overall_soundscape` (`N/A` only for total silence); score in `non_diegetic_music`, as instruments, tempo, rhythm and dynamics without mood words (`N/A` for none). Never repeat dialogue in the two sound fields.

## Text in the image

- **Visible text:** put signs, labels, subtitles and neon in English double quotes, verbatim, in their original language: `A blue neon sign reading "NOODLES" flickers above the stall.`
- **Layout:** use one main piece of text per shot, and keep it off faces.
- **No text:** when nothing should appear, write "No subtitles, on-screen text, or watermarks."

## Avoid

- Free prose with no fields. Nothing expands it for this model, so a loose paragraph loses detail.
- Labels that do not match the order above, a label used before it is defined, or one input under two labels.
- Asking for "one continuous take" and also writing several `[Shot N]` blocks, or asking for music and also for "no background music".
- A timeline longer or shorter than `duration`, cut times past the end of the clip, or more than 8 s on `minimax-h3`.
- Plot summaries in place of what is seen and heard, and abstract adjectives.
- Expecting a negative-prompt field; there is none. Write exclusions as "No ..." and "Do not ..." lines in the text.

## Examples

Text only, 6 s, with a voiceover:

```text
integrated_multimodal_description: [Shot 1] Live-action, cinematic, a wide shot frames a lone lighthouse on a black rock at dusk as waves break white against its base. The camera pushes in with small amplitude at slow speed while the lamp at the top turns on and sweeps across the water. A weathered older man (S1) with a low, gravelly voice says in an off-screen voiceover: <d>[English] Forty years, and she never once went dark.</d> while no one on screen speaks.

overall_soundscape: Heavy surf crashes and drains off the rocks, gulls cry overhead, and the lamp mechanism hums faintly.

non_diegetic_music: A slow, sustained cello line joined by soft low strings, swelling slightly as the beam sweeps past.
```

First frame, 5 s:

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 2D-animated, the girl with silver twin tails shown in <Picture 1> stays at the train window in her navy coat, preserving the carriage layout. The camera trucks right with small amplitude at slow speed as she lifts her gaze from her phone to the passing city lights, and her reflection slides across the glass. She smiles and presses one gloved hand to the window.

overall_soundscape: Train wheels keep a steady metallic rhythm under a low ventilation hum, and rain ticks against the glass.

non_diegetic_music: N/A
```

References, 8 s: a saved character with a voice, plus one uploaded product image in `image` (it comes first, so it is `<Picture 1>` and the character is `<Picture 2>`). Shortened; a full description runs longer.

```text
subject_definitions:
<Subject 1> is the man in <Picture 2> (@theo), with a shaved head, round glasses and a green knit sweater.
<Subject 2> is the white ceramic coffee grinder in <Picture 1>, with a walnut lid and a brass crank.
<Audio 1> is the voice-timbre reference for <Subject 1> (S1).

summary:
[reference generation + audio reference] <Subject 1> grinds beans with <Subject 2> at a sunny kitchen counter and speaks to camera in the voice referenced from <Audio 1>.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - face, glasses and sweater are kept.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - shape, walnut lid and brass crank are kept exactly.
<Audio 1>: reference - his delivery follows its timbre without copying its words.

detailed_description:
Live-action, warm morning light through a window on the left, shallow depth of field.
[Shot 1] A medium shot frames <Subject 1> at a pale stone counter, turning the brass crank of <Subject 2> as beans crackle inside. The camera pushes in with small amplitude at slow speed. [Shot 2] At 00:04.000, the camera cuts to a close-up of <Subject 1> (S1), who looks into the lens and says in a relaxed, warm voice: <d>[English] Thirty seconds. That's all good coffee asks.</d> He lifts the walnut lid and the grounds catch the light.

overall_soundscape:
Beans crunch in the grinder, the crank creaks, and a kettle begins to whistle softly in the background.

non_diegetic_music:
A light acoustic guitar figure at a moderate tempo, fading out after the line.
```
