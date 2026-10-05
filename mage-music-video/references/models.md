# Models

The app's model picker, in the connector's names. The default is Cherry 2 Pro at `480p`. When the user asks for another model, use it, and say what it costs first.

| Model | `architecture` | `model_id` | `resolution` | `duration` | `aspect_ratio` |
|---|---|---|---|---|---|
| Cherry 2 Pro (default) | `cherry` | `cherry-2-pro` | `480p`, `720p`, `1080p` | `4`, `5`, `8`, `10`, `15`, `20`, `25`, `30` | `9:16`, `16:9`, `1:1` |
| Cherry Pro | `cherry` | `cherry-pro` | `480p` up to `4k` | `4`, `5`, `8`, `10`, `15` | as Cherry 2 Pro |
| Cherry | `cherry` | `cherry` | `480p`, `720p` | `4`, `5`, `8`, `10`, `15` | as Cherry 2 Pro |
| Cherry Mini | `cherry` | `cherry-mini` | `480p`, `720p` | `4`, `5`, `8`, `10`, `15` | as Cherry 2 Pro |
| Lemon | `lemon` | `lemon` | `480p`, `720p`, `1080p` | `2`–`30` | `9:16`, `16:9`, `4:3`, `1:1`, `3:4` |
| Plum | `plum` | `plum` | `768P`, `2K` | `4`–`15` | `9:16`, `16:9`, `1:1`, `4:3`, `3:4`, `21:9` |
| Plum Max | `plum` | `plum-max` | `480P`, `768P` | `5`–`15` | as Plum |

## Settings on every model

- **`duration`:** the shortest option that is at least the audio's length, rounded up to a whole second, so the whole clip of audio is covered. A 4.2 s clip takes `"5"`; on Cherry a 6 s clip takes `"8"`. If the audio is longer than the model's longest option, use the longest.
- **`resolution`:** the lowest the model lists, unless the user asks for more.
- **`aspect_ratio`:** `9:16`, the app's default, unless the user asks for another.
- **`use_character_voices: false`** on Plum, Lemon, and Cherry, so the chosen audio is the only voice.
- **Images** go in `image` (and `additional_images`), never `first_image`: these models don't take audio alongside a first frame.
- **Audio** is always a saved audio reference mentioned as `@handle` in the prompt. It is trimmed to 15 seconds when saved.
- **Which model a name means:** "Cherry" alone is `cherry`; "Plum" alone is `plum`.
- **Opt-in models:** Plum, Plum Max run only when the user asks for them by name.

`get_model` is the source of truth for fields, options, and rules; `estimate_cost` refuses a config the model would refuse, for free.
