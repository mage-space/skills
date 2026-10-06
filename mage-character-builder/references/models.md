# Models

The app's model picker, in the connector's names. The default is Guava (`guava`) at `1K`. Switch only when the user asks for a model, a higher resolution, or a lower price.

| Model | `architecture` | `model_id` | `resolution` | Notes |
|---|---|---|---|---|
| Mango 3 | `mango` | `mango-v3` | `1K`, `2K` | The default, for quality: the most faithful edits. |
| Mango 3 Turbo | `mango` | `mango-v3-turbo` | `1K`, `2K` | For speed: the fastest and cheapest. |
| Mango 3S | `mango` | `mango-v3s` | `2K`, `3K` | Only when the user asks for it or for 3K. Never the default. |
| Mango 2 | `mango` | `mango-v2` | `2K`, `3K`, `4K` | The only one that reaches 4K. |
| Guava 2 Pro | `guava` | `guava-2-pro` | `1K`, `2K` | Photoreal skin, fabric, and hair. |
| Guava 2 | `guava` | `guava-2` | `1K`, `2K` | The faster Guava 2. |
| Guava Pro 1.5 | `guava` | `guava-pro-v1-5` | `1K`, `2K` | An older Guava. |
| Guava Pro | `guava` | `guava-pro` | `1K`, `2K` | An older Guava. |
| Guava | `guava` | `guava` | `1K`, `2K` | The original Guava. |
| Nano Banana 2 | `nano_banana_v2` | `nano-banana-v2` | `512`, `1K`, `2K`, `4K` | Strict safety filter. |
| GPT Image 2 | `gpt_image_2` | `gpt-image-2` | `1K`, `2K` | `quality`: `low` or `high`. Strict safety filter. |
| GPT Image 2.5 Flare | `gpt_image_2` | `gpt-image-2.5-flare` | `1K`, `2K` | `quality`: `low` or `high`. Strict safety filter. |
| GPT Image 2.5 Sunburst | `gpt_image_2` | `gpt-image-2.5-sunburst` | `1K`, `2K` | `quality`: `high` or `max`. Strict safety filter. |

- Every model takes the input images in `image` (the first) and `additional_images` (the rest), and `aspect_ratio` as `W:H`.
- The GPT Image models also take `quality`; each level up costs several times more, so price it with `estimate_cost`.
- Guava takes at most 3 images per request.
- Options and prices change. `get_model` is the source of truth; `estimate_cost` refuses a config the model would refuse, for free.
