# LTX Video (`ltx_video`)

A fast open-weights video model (opt-in) for cheap iteration, from text or a start frame, in Distilled and Dev variants. Silent clips of about four seconds, 240p to 720p.

## Variants

| `model_id` | Use it for | What changes |
|---|---|---|
| `ltx-video-096-distilled` | The default: drafts and fast iteration | Runs without guidance, so `negative_prompt` has little or no effect. |
| `ltx-video-096-dev` | The keeper, once the prompt works | Slower, higher quality; uses guidance, so the negative prompt counts. |

Draft on Distilled; when a prompt works, run the same prompt on Dev.

- Length is fixed: 97 frames at 24 fps, about 4 seconds. There is no `duration`.
- `resolution`: `240p`, `360p`, `480p` (default) or `720p`. `aspect_ratio`: 21:9 to 9:21, default 3:2.
- Each variant runs a fixed recipe; step and guidance fields do not change it.

## How Mage sends your prompt

- **A built-in rewriter runs on short prompts.** The model's prompt enhancer is always on: any prompt under 120 words is rewritten by a small built-in language model before the video model sees it, and with a start frame that model first captions the image. A prompt of 120 words or more goes through as written. Write 120 to 200 words in the structure below and you keep control of every detail; a short prompt gets someone else's words. `prompt_enhance: false` does not turn it off.
- `first_image` conditions frame 0 at full strength. The clip takes the image's shape, and `aspect_ratio` is ignored.
- `negative_prompt` defaults to `worst quality, inconsistent motion, blurry, jittery, distorted`. Keep it; add to it only on Dev.
- No reference images, no `@handle`s, no last frame. Any `@` followed by a letter is refused.

## Prompt structure

One flowing paragraph, chronological, literal and precise, at most about 200 words, in English. Think like a cinematographer describing a shot list, in this order:

1. The main action, in a single sentence that starts with the action itself.
2. Specific movements and gestures.
3. The precise appearance of the characters and objects.
4. The background and environment.
5. Camera angles and movements.
6. Lighting and colors.
7. Changes or sudden events.

- The more elaborate the better: spell out colors, textures, materials and light ("The rocks are dark and jagged, covered in patches of green moss").
- Four seconds holds one continuous action and one camera move: no cuts, no second scene.
- 120 words is easy to reach with appearance, environment and light detail; never pad with repeated adjectives.

## Vocabulary

Plain, literal description beats cinematic jargon:

- **Motion**: "the waves crash against the rocks, sending white foam spraying into the air", "takes out a book and starts reading it", "a single vehicle traveling along the road".
- **Openers**: "The video depicts ...", "The scene is dominated by ..." for an establishing description after the action sentence.
- **Light and color**: "the light is dim", "the stark contrast between the bright blue water and the dark, almost black rocks", "the sky is cloudy".
- Name one camera behavior in plain words: "the camera slowly pushes in", "the camera stays still at eye level", "the camera tracks alongside from the left".

## References, characters, and frames

- Only a start frame, in `first_image`. The prompt still opens with the action; then describe what the frame shows in the same literal terms (colors, clothing, setting), so the words and the image agree and the rewriter is not needed.
- The clip takes the frame's own aspect: use a frame already at the delivery ratio.
- For a character across several clips, start each clip from an approved still of that character and repeat the same appearance sentence word for word.

## Audio and dialogue

None: the clips are silent. Leave sound and dialogue out of the prompt, and add audio afterwards (Seed Audio for music or effects).

## Text in the image

Not a strength. Add titles and captions afterwards in an editor.

## Avoid

| Instead of | Write |
|---|---|
| A one-line prompt | 120 to 200 words in the order above, so the rewriter stays off |
| Opening with the setting or a style line | The main action as the first sentence |
| Cinematic jargon and mood adjectives | Literal descriptions of motion, colors, textures and light |
| A story with several beats or a cut | One continuous action in about four seconds |
| Expecting the negative prompt to fix a Distilled draft | A clearer positive description, or the Dev variant |
| More than 200 words | The essentials of each of the seven parts |

## Examples

Text to video, coastline, 16:9 (about 130 words):

```
Turquoise waves crash against the dark, jagged rocks of the shore, sending white foam spraying into the air before it slides back down the stone. Each wave rises, curls over and breaks in turn, and thin streams of water run off the rocks between them. The scene is dominated by the stark contrast between the bright blue water and the dark, almost black rocks. The water is a clear turquoise, and the waves are capped with white foam. The rocks are jagged and covered in patches of green moss. The shore is lined with lush green trees and bushes, and rolling hills covered in dense forest rise in the background. The camera stays still at shoulder height, framing the rocks in the lower half. The sky is cloudy and the light is dim and even.
```

Start frame of a penguin in a library, `first_image`, about 130 words:

```
A small penguin takes a red book from a low wooden shelf, opens it with both flippers and starts reading. It tilts its head toward the pages, then turns one page slowly as its feet shuffle on the floor. The penguin is round and glossy, with a black back, a white belly, a short orange beak and bright black eyes. The book has a worn red cloth cover with faded gold lettering. Behind it, tall dark bookshelves full of old leather-bound books stretch back into a quiet library with a green-shaded reading lamp on a desk. The camera stays at the penguin's eye level and slowly pushes in from a medium shot to a close-up. Warm lamplight falls from the left, with soft shadows and a calm, cozy amber and green palette.
```

Text to video, mountain road, 21:9 (about 130 words):

```
A single dark green car drives along a winding mountain road covered in fresh snow, its headlights on and a thin spray of powder rising behind its rear wheels. The car follows the curve to the right, slows slightly at the bend, then accelerates onto a short straight stretch. The road is narrow and white, with two dark tire tracks pressed into it. Steep gray rocky cliffs rise on the left, with sparse pine trees clinging to ledges, and on the right the slope drops away to a frozen river in the valley far below. The camera follows from high above and behind, drifting slowly to the right with the road. The light is cold and overcast, with pale blue shadows on the snow and a white, hazy sky over the peaks.
```
