# Models

The app's model picker, in the connector's names. The default is Cherry at `480p`, 4 seconds, `16:9`. Switch only when the user asks for a model, a higher resolution, a longer clip, or a lower price, and say what it costs first.

| Model | `architecture` | `model_id` | `resolution` | `duration` | `aspect_ratio` |
|---|---|---|---|---|---|
| Cherry | `cherry` | `cherry` | `480p` (default), `720p` | `4` (default), `5`, `8`, `10`, `15` | `16:9` (default), `9:16`, `1:1` |
| Cherry Pro | `cherry` | `cherry-pro` | `480p`, `720p` | `4`, `5`, `8`, `10`, `15` | as Cherry |
| Cherry 2 Pro | `cherry` | `cherry-2-pro` | `480p`, `720p` | `4`, `5`, `8`, `10`, `15`, `20`, `25`, `30` | as Cherry |
| Raspberry | `raspberry` | `raspberry` | `720p`, `1080p` | `2`–`15` | `16:9`, `4:3`, `1:1`, `3:4`, `9:16` |
| Lemon | `lemon` | `lemon` | `480p`, `720p`, `1080p` | `2`–`30` | `16:9`, `4:3`, `1:1`, `3:4`, `9:16` |

- The app offers the Cherry models at `480p` and `720p` only in Scene Builder.
- Character images go in `image` (the first) and `additional_images` (the second) on every model, never `first_image`. Saved characters are `@handle` mentions in the prompt.
- Saved characters with a voice speak with it; that is the default (`use_character_voices: true`) and the app leaves it on here, unlike the other video apps. Don't send `false`.
- "Cherry" alone is `cherry`. Raspberry is an opt-in model: it runs only when the user asks for it by name.
- Raspberry takes at most 5 images per request, and Cherry 8.

`get_model` is the source of truth for fields, options, and rules; `estimate_cost` refuses a config the model would refuse, for free.
