# Models

The app's model picker, in the connector's names. The default is Lemon at `480p`. Switch only when the user asks for a model, a higher resolution, or a lower price, and say what it costs first.

| Model | `architecture` | `model_id` | Clip field | Source clip | Output settings | Notes |
|---|---|---|---|---|---|---|
| Lemon | `lemon` | `lemon` | `videos` (a list of one) | 1–15 s | `resolution` `480p`/`720p`/`1080p`, `duration`, `aspect_ratio` | Clip length + `duration` ≤ 30 s. The clip's seconds bill like output seconds. |
| Cherry 2 Pro | `cherry` | `cherry-2-pro` | `videos` (a list of one) | 4–30 s | `resolution` `480p`/`720p`/`1080p` only | Leave `duration` and `aspect_ratio` out: the output follows the clip. Uses the wrapped prompt. |
| Cherry Pro | `cherry` | `cherry-pro` | `videos` (a list of one) | 2–15 s | `resolution` up to `4k`, `duration`, `aspect_ratio` | Uses the wrapped prompt. |
| Cherry | `cherry` | `cherry` | `videos` (a list of one) | 2–15 s | `resolution` `480p`/`720p`, `duration`, `aspect_ratio` | Uses the wrapped prompt. |
| Cherry Mini | `cherry` | `cherry-mini` | `videos` (a list of one) | 2–15 s | `resolution` `480p`/`720p`, `duration`, `aspect_ratio` | The cheapest Cherry. Uses the wrapped prompt. |
| Plum | `plum` | `plum` | `videos` (a list of one) | 2–15 s | `resolution` `768P`/`2K`, `duration` from 4, `aspect_ratio` | At most 2 reference images. |
| Plum Max | `plum` | `plum-max` | `videos` (a list of one) | 2–15 s | `resolution` `480P`/`768P`, `duration` from 5, `aspect_ratio` | At most 2 reference images. The clip bills at a higher rate than on Plum. |
| Berry | `berry` | `berry` | `video` (one URL) | 3–60 s | `resolution` `720p`/`1080p` only | Leave `duration` and `aspect_ratio` out. Editing runs on `berry`, not `berry-2`. |
| Grok Video | `grok_video` | `grok-imagine-video` | `video` | up to 8.7 s | none | The output keeps the clip's length and shape. No reference images. Strict safety filter. |

## Settings by model

- **`duration`** (Lemon, Cherry Pro, Cherry, Cherry Mini): round the clip's length to the nearest whole second, then take the shortest option that is at least that. A 4.04 s clip rounds to 4 and takes `"4"`; a 6 s clip takes `"6"` on Lemon and `"8"` on Cherry. Lemon's options are every whole second from `"2"` to `"30"`; Cherry's are `"4"`, `"5"`, `"8"`, `"10"`, `"15"`. These models rebuild the clip end to end at that length.
- **`duration` on Plum and Plum Max** is the output length: every whole second from `"4"` (Plum) or `"5"` (Plum Max) to `"15"`. Use the same rule; when the clip is shorter than the model's minimum, use the minimum and tell the user the output will run longer than the clip.
- **`aspect_ratio`** (every model but Cherry 2 Pro, Berry, and Grok Video): the option whose width ÷ height is closest to the clip's. Lemon: `16:9`, `4:3`, `1:1`, `3:4`, `9:16`. Cherry: `16:9`, `9:16`, `1:1`. Plum: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`. (The app's picker starts at `16:9`; matching the clip is what a user would choose.)
- **`resolution`:** the lowest the model lists, unless the user asks for more: `480p` on Lemon and Cherry, `480P` on Plum Max, `768P` on Plum, `720p` on Berry. Plum writes it with a capital `P`.
- **`use_character_voices: false`** on Lemon, every Cherry model, Plum, and Plum Max, as the app sends it. Berry and Grok Video don't take the field.
- **References** (up to 2 references): an image goes in `image`, and a second in `additional_images`; a saved character is mentioned as `@handle` in the prompt instead and takes no image field. Grok Video takes none.
- **Which model a name means:** "Cherry" alone is `cherry`; "Cherry 2 Pro", "Cherry Pro", and "Cherry Mini" are their own ids. "Plum" alone is `plum`.
- **Opt-in models:** Plum, Plum Max, Berry, and Grok Video run only when the user asks for them by name.

## The wrapped prompt (Cherry models only)

On any Cherry model, the app wraps the instruction in this before sending it. Send it the same way, with the instruction in the slot:

```
Use the provided reference video as the source of truth. Recreate its visual content as closely and faithfully as possible from beginning to end.

Preserve the shot sequence, timing, camera angle, camera movement, framing, composition, subject identity, poses, actions, body movement, facial expressions, environment, background, lighting, color grading, and visual style of the reference video.

Apply only the following requested change:
<the change>

Make the minimum changes necessary to fulfill the request. Everything not explicitly mentioned in the requested change must remain consistent with the reference video. Do not restage the scene, reinterpret the action, alter the camera or motion, add or remove unrelated subjects or objects, or introduce unrelated visual changes unless the request explicitly requires it.
```

The slot takes the whole instruction, however many paragraphs it has. A `Reference: @handle` line for a saved character goes after the entire wrapped prompt, separated by a blank line, not inside the slot. Every other model gets the instruction alone.

## Audio

The app has a "keep original audio" switch for Cherry and Berry. The connector doesn't list a field for it, so don't send one: the model decides the soundtrack. Lemon and Plum generate audio with the clip. If the user needs the original sound kept exactly, say this is a limit and suggest laying the original audio back over the result in an editor.

`get_model` is the source of truth for fields, options, and rules; `estimate_cost` refuses a config the model would refuse, for free.
