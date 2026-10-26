# Grok Video (`grok_video`)

xAI's Grok Imagine video on Mage (opt-in): clips from text, from up to 5 reference images, or an edit of a source video. 1 to 15 seconds, 480p or 720p, with a generated soundtrack. xAI's safety filter applies.

## Variants

One variant, `grok-imagine-video`. The price is per second and higher at 720p; an edit is priced from the source clip. Draft at 480p; render the keeper at 720p.

- `duration`: "1" to "15" seconds (default "5"); capped at 10 with reference images.
- `resolution`: `480p` (default) or `720p`.
- `aspect_ratio`: 16:9 (default), 9:16, 1:1, 4:3, 3:4, 3:2, 2:3.

## How Mage sends your prompt

The inputs pick the mode:

| You send | Mode | What happens |
|---|---|---|
| `prompt` only | Text to video | The prompt is the whole shot. |
| `image`, `additional_images`, `@handle`s | Reference to video | Up to 5 images supply people, products, clothing or places; none of them becomes the first frame. |
| `video` (at most 8.7 s) | Edit | The output keeps the source's length, framing and resolution (up to 720p); `duration`, `aspect_ratio` and `resolution` are ignored, and references are refused. |

- There is no first or last frame. When the clip must open on an exact still, use a first-frame model such as Lemon.
- Mage numbers reference images in order (your `image`, `additional_images`, then `@handle` characters, then `@handle` references) and rewrites mentions to match: `@image1` becomes "image 1", a character `@mara` becomes "character from image N", a saved outfit `@linen-shirt` "outfit from image N". Use `@handle`s and `@image1`-style mentions and let Mage write the numbers. xAI's own docs tag references as `<IMAGE_0>`, `<IMAGE_1>`; Mage does not convert between the two, so never mix those tags into a prompt that uses `@` mentions.
- The prompt reaches the model as written. No negative prompt.
- Any `@` followed by a letter is read as a saved handle and refused when none matches.

## Prompt structure

xAI publishes no video prompting guide; its example prompts share one shape. Write one shot in prose, in this order:

1. Shot type and angle ("High-angle wide shot", "Extreme slow-motion macro shot").
2. The subject and its action, in sequence, joined with "then".
3. The environment.
4. The light.
5. A short mood or style line.
6. The sound.
7. When objects must hold still, a continuity sentence: "Continuity: every object stays exactly where it is for the whole clip; nothing appears, disappears, duplicates, or changes shape."

- **Reference to video**: open with the camera move, then bring each referenced subject in with its one role and place. Describe the action, not the reference pictures.
- **Edit**: one change, then what stays: "Change the color of the woman's dress to red. Keep everything else exactly as in the original, including her face, hands, pose, and the background."
- Keep a short clip to one or two beats; a 3 s clip has no room for a story.

## Vocabulary

- **Camera moves in xAI's examples**: slow zoom in, slow smooth push-in, "The camera dollies from the sunlit doorway to the window", locked-off ("The camera never moves"), "Only the camera moves", high-angle wide shot, action POV with extreme camera motion.
- **Time**: time-lapse, "slow time-lapse feel", high-quality slow motion, extreme slow-motion macro.
- **Light**: dappled sunlight drifting across the scene, warm morning window light, giant glowing billboards reflecting on wet asphalt.
- **Style**: "Stop-motion claymation, visible fingerprints in the clay, slightly choppy frame rate, wide miniature set"; cinematic.

## References, characters, and frames

- **One role per reference**, each with a fixed place in the scene: "the model from image 1 walks the runway wearing the shirt from image 2". Keep the cast small (two or three), and keep props static: moving props are where references break.
- **Products**: name what must not change, "the bottle, cap and label text stay unchanged while only the camera moves".
- **The same character across shots**: pass the same approved still or `@handle` in every shot. xAI's storyboard playbook makes the keyframes first (an image, then edits of it for each new scene and angle); on Mage, make those keyframes with Grok Image edits and pass each as this model's reference, or animate them with a first-frame model.
- **Edit fan-out**: run several single-change edits of one source clip at once (a red dress, a black hat, a different jacket), each with its own keep sentence, and let the user pick.
- Trim a longer source to 8.7 s or less before an edit (with ffmpeg when you can run commands, then `create_upload`).

## Audio and dialogue

- Every clip comes with a generated soundtrack; there is no switch for a silent clip. Write the sound into the prompt, last: "gentle music box melody", "rain on asphalt, distant traffic, a passing tram bell", "crowd murmur and footsteps".
- This model has no lip-synced speech, no voice references and no character voices. Leave dialogue lines out; for a talking character, use a model with voices (Cherry 2 Pro, Lemon).
- To keep a source clip's own audio after an edit, put it back over the result afterwards (ffmpeg or an editor).

## Text in the image

Not covered by xAI for this model. Keep on-screen text static and existing (a label already in a reference image), and say it stays unchanged; add titles afterwards in an editor instead of generating them.

## Avoid

| Instead of | Write |
|---|---|
| A description of what each reference image shows | What the referenced people and things do in the shot |
| Five references with overlapping roles | Two or three, one role each |
| Props that move, pass between hands, or multiply | Static props, plus the continuity sentence |
| A full scene description for an edit | The one change, then "Keep everything else exactly as in the original, including ..." |
| Dialogue in quotes | The soundscape and music |
| `duration` above "10" with references | "10" or less, or no references |
| `<IMAGE_0>` tags beside `@` mentions | `@handle`s and `@image1`, which Mage numbers |

## Examples

Establishing shot, text only, 16:9, 8 s:

```
High-angle wide shot of a huge scramble crossing in Tokyo at night in the rain. When the lights change, hundreds of pedestrians with colorful umbrellas pour into the intersection from every corner and weave past each other without colliding. Giant glowing billboards, wet asphalt reflecting the lights, taxis waiting at the edges. Slow time-lapse feel. Rain hiss, crossing chimes and a low city hum.
```

Food ad, text only, 9:16, 6 s:

```
Extreme slow-motion macro shot: thick amber honey pours from a wooden dipper onto a tall stack of fluffy pancakes. The honey ribbon folds over itself, pools on top, then slowly drips down the edges as a pat of butter melts and slides. Warm morning window light, steam rising, shallow depth of field. Soft kitchen ambience and a slow, warm piano note.
```

Stop-motion with continuity, text only, 16:9, 6 s:

```
Stop-motion claymation, visible fingerprints in the clay, slightly choppy frame rate, wide miniature set. A small orange clay fox in a knitted red scarf stands next to a finished snowman with a carrot nose and three coal buttons, in a snowy clay meadow with a little wooden cabin and two pine trees behind them. The fox pats the snowman's belly, steps back to admire it, then waves happily as tiny cotton snowflakes fall. Continuity: every object stays exactly where it is for the whole clip; nothing appears, disappears, duplicates, or changes shape. Warm miniature set lighting, cozy handmade look, gentle music box melody.
```

Reference to video, a saved character `@mara` and a saved outfit `@linen-shirt`, 9:16, 8 s:

```
Slow zoom in on a white fashion runway stage. Then @mara walks in from the opening at the back and strides out to the front of the platform, wearing @linen-shirt with black flared jeans. She reaches the end of the runway, looks dramatically at the camera and gives a subtle smile as the camera keeps slowly zooming. High-quality slow motion, highly detailed face. Thumping runway beat and camera shutters.
```

Edit, the source clip as `video`:

```
Give the woman a wide-brimmed black hat. Keep everything else exactly as in the original, including her face, hands, pose, and the background.
```
