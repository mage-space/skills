# Model guide

Mage names its own models after fruit. Use these names with the user; never guess which lab or upstream model is behind one. Prices in Gems, options, and limits change, so read them from `get_model` and `estimate_cost` rather than from this file.

## Images

| Model | Architecture / `model_id` | Pick it for | Watch out for |
|---|---|---|---|
| Mango 3 | `mango` / `mango-v3` | The default. Exact instructions, the same character across a set, several references merged into one scene, edits that keep the rest of the image in place. Up to 10 reference images. | The priciest Mango; 1K or 2K only. |
| Mango 3S | `mango` / `mango-v3s` | Cheaper, faster Mango with characters and references; 3K output. | Slightly less precise than Mango 3. |
| Mango 2 | `mango` / `mango-v2` | 4K stills. | Previous generation. |
| Guava 2 Pro | `guava` / `guava-2-pro` | Photoreal portraits, fashion, editorial, product shots that pass for photographs; skin, fabric, and hair texture. | At most 3 reference images; a vague prompt gives a generic studio look. |
| Guava 2 | `guava` / `guava-2` | Cheaper photoreal iterations. | Guava 2 Pro makes the better final. |
| GPT Image 2.5 Flare | `gpt_image_2` / `gpt-image-2.5-flare` | Text rendered in the image, graphic design, infographics, comics, memes, detailed edits from up to 15 references. Very cheap at the default `quality`. | OpenAI's safety filter applies and cannot be overridden. Higher `quality` levels cost several times more: price them. |

Aspect ratios for images: `21:9`, `16:9`, `3:2`, `5:4`, `1:1`, `4:5`, `2:3`, `9:16`, `9:21`. Resolution tokens: `1K`, `2K`, `3K`, `4K`, depending on the variant.

## Video

| Model | Architecture / `model_id` | Pick it for | Watch out for |
|---|---|---|---|
| Cherry 2 Pro | `cherry` / `cherry-2-pro` | The default and the flagship: cinematic motion with sound, 4–30 s, up to 50 reference images, characters with their voices, audio references, and edits of a source video. | The most expensive model; price climbs steeply with resolution and length. No first or last frame, no 4K. |
| Cherry Pro | `cherry` / `cherry-pro` | 4K video, up to 15 s. | Fewer references. |
| Cherry | `cherry` / `cherry` | Cherry at a lower price, 480p or 720p. | Shorter, fewer references. |
| Cherry Mini | `cherry` / `cherry-mini` | The cheapest Cherry, for drafts. | Lower quality. |
| Lemon | `lemon` / `lemon` | A first frame and a last frame, reference images or reference videos, 2–30 s, generated sound (`audio: true`). Good quality for the price. | One request uses frames or references, never both. |

Video aspect ratios: Cherry `16:9`, `9:16`, `1:1`; Lemon adds `4:3` and `3:4`. `duration` and `resolution` are string tokens such as `"10"` and `"720p"`.

## Audio

| Model | Architecture / `model_id` | Pick it for | Watch out for |
|---|---|---|---|
| Seed Audio | `seed_audio` / `seed-audio-1.0` | Voices, dialogue, music, sound effects, as an MP3 of exactly `duration` seconds (5, 10, 30, 60, 120). | One image reference or up to 3 voice clips by `@handle`, not both. Prompt at most about 3,000 characters. |

Seed Audio also takes `speech_rate` (−50 to 100), `loudness_rate` (−50 to 100), and `pitch_rate` (−12 to 12).

## Opt-in models

Every other model runs only when the user names it ("make it with Melon"). `list_models` with `include_opt_in: true` lists them. When one clearly suits the request better, such as an anime model for an anime clip, suggest it and wait for the user to agree.

## Characters, references, and voices

`get_model` reports which variants accept `@character` and `@reference` mentions (`mentions`), the shared image budget (`max_images`), and whether a character's saved voice rides along into video (`character_voices`; turn it off with `use_character_voices: false`).
