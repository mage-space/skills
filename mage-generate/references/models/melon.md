# Melon (`melon`)

Mage's anime video model, as Melon and Melon Pro. It covers anime and illustrated motion, character-driven anime scenes, clips that connect frame to frame, and clips up to 16 s, with optional audio. Photoreal subjects come out better on other models. It is opt-in: use it when the user asks for Melon.

Lines marked _(general)_ are general advice for anime video, not rules tested on Melon.

## Variants

| `model_id` | For |
|---|---|
| `melon` | The cheaper one, for drafts and most clips |
| `melon-pro` | Higher quality, for finals |

Both take `resolution` `540p`, `720p` or `1080p`, and `duration` 3, 4, 5, 6, 8, 10 or 16 s. `aspect_ratio` takes `16:9`, `9:16`, `1:1`, `3:4` or `4:3`. The prompt is at most 5,000 characters.

## How Mage sends your prompt

The fields you fill choose the mode:

| Fields | Mode | Notes |
|---|---|---|
| `first_image` + `last_image` | Start and end frames | The two frames must be close in size and shape. The output follows their aspect ratio |
| `first_image` | Start frame | The output follows its aspect ratio |
| `image`, `additional_images`, `@handles` of characters and references | References | Up to 7 images, handles included. `aspect_ratio` applies |
| none | Text only | `aspect_ratio` applies |

- **No lone last frame.** A `last_image` without a `first_image` is silently dropped, and the clip comes out as text only. Always pair a last frame with a first frame.
- **Frames or references, never both.**
- **Handles.** Mage rewrites `@mika` to `character from image 2` and `@rooftop` to `location from image 3`. Melon receives the images in that order but with no names attached, so the words "image 2" tell it little. Mention the handle once where the character first appears, then describe the character by visible traits.
- **Audio.** `generate_audio` is off by default. Turn it on for synced dialogue, voiceover, sound effects and music. There are no voices and no audio references.
- **Stray `@`.** Any `@word` is read as a handle, and one that matches nothing is refused. Never write an email address or a social handle in the prompt.

## Prompt structure

Build the prompt in this order:

1. **Subject:** who, with the details that define them (hair, outfit, colors).
2. **Action:** one main action for the clip.
3. **Camera:** the shot size and one movement. Always include a camera direction; leaving it out weakens results.
4. **Scene:** the place and the lighting.
5. **Style:** the look and mood, at the end, for example "anime style, flat cel shading, soft evening light".

For a start frame, the frame already shows subject, scene and style. Spend the prompt on the action and the camera. For start and end frames, describe the motion that carries the first frame into the last.

Melon can switch shots within one clip, but it has no shot syntax. When the user wants cuts, write the shots as plain sentences in order ("Then the shot cuts to a close-up of ..."). Keep it to two or three shots for a 10–16 s clip.

## Vocabulary

- **Camera:**
  - Use one movement per clip, on one axis, with a direction: "the camera slowly pushes in", "the camera tilts up", "the camera pans left".
  - Give it a speed word: subtle, gentle, slow or steady.
  - Never stack two moves, as in "slow dolly forward with slight pan left".
- **Anime look _(general)_:** "flat cel-shaded colors", "clean lineart", "anime key-visual style", "soft bloom", "rim light". Put the style tag last.
- **Emotion _(general)_:** state it plainly ("tears welling up, heartbroken"); an implied mood is easy to miss.

## References, characters, and frames

- **Reference images _(general)_:** use a front-facing character on a plain white or solid background, at the highest resolution you have, with flat colors. Gradients and busy backgrounds hold less well.
- **Order _(general)_:** put the most important image first, such as the main character's front view.
- **A series of clips _(general)_:** repeat the same fixed character sentence (hair, eyes, outfit, colors) in every clip, and attach the same location in each.
- **Back views _(general)_:** add "back view, face hidden".

## Audio and dialogue

- **Audio switch:** set `generate_audio: true` for any sound. Spoken lines work in English, Japanese and Chinese.
- **Dialogue _(general)_:** name the speaker and give the exact line in quotes, for example: `The girl with silver hair says softly, "I waited for you."` Keep lines short for the clip length.
- **Narration and sound:** narration, sound effects and music work the same way: say who or what makes the sound and when.

## Text in the image

On-screen text is untested on this model, so do not rely on it. Add titles and captions afterwards in an editor.

## Avoid

- More than one main action or camera move in a clip, or moves in conflicting directions.
- Vague prompts with no camera direction.
- _(general)_ Complex full-body action at high intensity, precise hand work (grabbing, pointing), and cameras that orbit or chase a character. Keep the shot on faces and upper bodies.
- Busy, detail-heavy reference images.
- A last frame without a first frame.

## Examples

Text only, 5 s, with audio:

```text
A girl with short silver hair and a red scarf runs along a school rooftop and stops at the railing, breathing hard, then looks out at the city. The camera slowly pushes in from a medium shot. Sunset sky in orange and violet, long shadows, wind tugging at her scarf. Anime style, flat cel-shaded colors, soft rim light.
```

A saved character, 8 s (`@mika` is mentioned once, then described):

```text
@mika, a boy with spiky black hair and a white school shirt, catches a paper airplane as it glides past the classroom window and smiles. The camera holds a steady medium close-up. Bright afternoon classroom, dust in the sunlight. Anime style, clean lineart, warm colors.
```

Start and end frames, 4 s:

```text
The cat on the windowsill stretches, hops down to the floor and pads toward the sleeping girl, ending curled up beside her. The camera gently pans right. Quiet bedroom at night, blue moonlight. Anime style.
```

Two shots with dialogue, 10 s, `generate_audio: true`:

```text
A tall swordsman in a dark blue coat stands in a rainy alley and turns toward the camera. The camera slowly pushes in. He says in a low voice, "You shouldn't have followed me." Then the shot cuts to a close-up of a young woman under a paper umbrella, eyes wide, rain dripping from the umbrella's edge. Neon reflections on wet stone, steady rain. Anime style, flat cel shading.
```
