# Models

The app's model picker, in the connector's names. The default is Plum at `768P`. Switch only when the user asks for a model, a higher resolution, or a lower price, and say what it costs first.

| Model | `architecture` | `model_id` | `resolution` | `duration` | `aspect_ratio` |
|---|---|---|---|---|---|
| Plum | `plum` | `plum` | `768P` (default), `2K` | `4`–`15` | `9:16` (default), `16:9`, `1:1`, `4:3`, `3:4`, `21:9` |
| Plum Max | `plum` | `plum-max` | `480P`, `768P` | `5`–`15` | as Plum |
| Lemon | `lemon` | `lemon` | `480p` (default), `720p`, `1080p` | `2`–`30` | `9:16` (default), `16:9`, `4:3`, `1:1`, `3:4` |
| Cherry 2 Pro | `cherry` | `cherry-2-pro` | `480p` (default), `720p`, `1080p` | `4`, `5`, `8`, `10`, `15`, … | `9:16` (default), `16:9`, `1:1` |
| Cherry Pro | `cherry` | `cherry-pro` | `480p` (default) up to `4k` | `4`, `5`, `8`, `10`, `15` | as Cherry 2 Pro |
| Cherry | `cherry` | `cherry` | `480p` (default), `720p` | `4`, `5`, `8`, `10`, `15` | as Cherry 2 Pro |
| Cherry Mini | `cherry` | `cherry-mini` | `480p` (default), `720p` | `4`, `5`, `8`, `10`, `15` | as Cherry 2 Pro |
| Blueberry 2 | `blueberry` | `blueberry-v2` | `720p` (default), `1080p` | `2`–`15` | leave out |
| Blueberry | `blueberry` | `blueberry` | `720p` (default), `1080p` | `2`–`15` | leave out |

## Settings on every model

- **`duration`:** the shortest option that is at least the audio's length, rounded up to a whole second, so the whole clip of audio is covered. A 4.2 s clip takes `"5"`; on Cherry a 6 s clip takes `"8"`. If the audio is longer than the model's longest option, use the longest.
- **`aspect_ratio`:** `9:16`, the app's default, unless the user asks for another.
- **`use_character_voices: false`** on Plum, Lemon, and Cherry, so the chosen audio is the only voice.
- **Images** go in `image` (and `additional_images`), never `first_image`: these models don't take audio alongside a first frame.
- **Blueberry is different:** the subject image goes in `first_image` and is animated directly as the first frame. The prompt is built the same way, with the `Audio:` line. It takes no characters, so with a saved character pass the character's image URL (from `list_characters`) as `first_image`, drop the `Subject:` mention, and tell the user Blueberry skips character identity; Lemon, Plum, and Cherry keep it. It takes one audio reference and has no `use_character_voices`.
- **Audio** is always a saved audio reference mentioned as `@handle` in the prompt. It is trimmed to 15 seconds when saved.
- **Which model a name means:** "Cherry" alone is `cherry`; "Plum" alone is `plum`.
- **Opt-in models:** Plum, Plum Max, Blueberry, and Blueberry 2 are opt-in on Mage. Plum is this app's default, so name it and its price in the quote; the others run only when the user asks for them.

`get_model` is the source of truth for fields, options, and rules; `estimate_cost` refuses a config the model would refuse, for free.
