# Model guide

Mage names its own models after fruit. Use these names with the user; never guess which lab or upstream model is behind one. Prices in Gems, options, and limits change, so read them from `get_model` and `estimate_cost` rather than from this file. How to write the prompt for each model is in its own file in `references/models/`.

## Images

| Model | Architecture / `model_id` | Pick it for | Watch out for |
|---|---|---|---|
| Mango 3 | `mango` / `mango-v3` | The default. Exact instructions, the same character across a set, several references merged into one scene, edits that keep the rest of the image in place, short text in 16 languages. Up to 10 images, characters and references. | The priciest Mango; 1K or 2K only. |
| Mango 3 Turbo | `mango` / `mango-v3-turbo` | Fast, cheap drafts and volume, with characters and references; strong layouts and text. The same prompt runs on Mango 3 for the final. | Not the default: use it when speed or price matters more. |
| Mango 3S | `mango` / `mango-v3s` | 3K output, with characters and references. Use it only when the user wants 3K. | No point or box tags. For speed or price, use Mango 3 Turbo instead. |
| Mango 2 | `mango` / `mango-v2` | 4K stills. | Previous generation, 2K and above only. |
| Guava 2 Pro | `guava` / `guava-2-pro` | Photoreal portraits, fashion, editorial, product shots that pass for photographs; skin, fabric, and hair texture. | Set `model_id`: the family default is the oldest Guava. At most 3 images; a vague prompt gives a generic studio look. |
| Guava 2 | `guava` / `guava-2` | Cheaper photoreal iterations. | Guava 2 Pro makes the better final. |
| GPT Image 2.5 Flare | `gpt_image_2` / `gpt-image-2.5-flare` | Text rendered in the image, graphic design, infographics, comics, memes, detailed edits from up to 15 references. Very cheap at the default `quality`. | Set `model_id`: the family default is the opt-in GPT Image 2. OpenAI's safety filter applies and cannot be overridden. Higher `quality` levels cost several times more: price them. No transparent backgrounds. |

Aspect ratios for images: `21:9`, `16:9`, `3:2`, `5:4`, `1:1`, `4:5`, `2:3`, `9:16`, `9:21`. Resolution tokens: `1K`, `2K`, `3K`, `4K`, depending on the variant.

## Video

| Model | Architecture / `model_id` | Pick it for | Watch out for |
|---|---|---|---|
| Cherry 2 Pro | `cherry` / `cherry-2-pro` | The default and the flagship: cinematic motion with sound, 4–30 s, up to 29 images (your images, characters, and references together), characters with their voices, audio references, and edits of a source video. | The most expensive model; price climbs steeply with resolution and length. No first or last frame, no 4K. An edit keeps the source's length and ratio. |
| Cherry Pro | `cherry` / `cherry-pro` | 4K video, up to 15 s. | Up to 8 images. Second ranges in the prompt are ignored: mark shots with `Shot N`. |
| Cherry | `cherry` / `cherry` | Cherry at a lower price, 480p or 720p. | Shorter, up to 8 images. |
| Cherry Mini | `cherry` / `cherry-mini` | The cheapest Cherry, for drafts of motion and timing. | Lower quality, and its look differs from Cherry 2 Pro's. |
| Lemon | `lemon` / `lemon` | A first frame and a last frame, up to 10 reference images and 5 reference videos, characters with their voices, 2–30 s, generated sound (`audio: true`). Good quality for the price. | One request uses frames or references, never both. Reference-video seconds bill like output seconds. |

Video aspect ratios: Cherry `16:9`, `9:16`, `1:1`; Lemon adds `4:3` and `3:4`. `duration` and `resolution` are string tokens such as `"10"` and `"720p"`.

## Audio

| Model | Architecture / `model_id` | Pick it for | Watch out for |
|---|---|---|---|
| Seed Audio | `seed_audio` / `seed-audio-1.0` | The default: voices, dialogue, music, sound effects, as an MP3 of exactly `duration` seconds (5, 10, 30, 60, 120). | One image reference (a voice to fit a face) or up to 3 voice clips by `@handle`, not both. Prompt at most about 3,000 characters. |
| Eleven Speech | `eleven_speech` / `eleven-v4` | The most natural narration, voiceover, and character lines, in 90+ languages, directed by audio tags such as `[whispers]`. One of 16 preset voices (`voice`). | Speech only, one voice per generation, no references. Priced by the length of the text; the clip runs as long as the text. |
| Eleven Music | `eleven_music` / `eleven-music-v2.5` | Full songs with vocals, or instrumentals (`instrumental: true`), 10 s to 5 minutes. | Music only. A prompt that names an artist or quotes copyrighted lyrics is refused (and refunded). |

Seed Audio also takes `speech_rate` (−50 to 100), `loudness_rate` (−50 to 100), and `pitch_rate` (−12 to 12). Eleven Speech takes `stability` (0 expressive to 1 steady).

## Opt-in models

Every other model runs only when the user names it ("make it with Melon"). `list_models` with `include_opt_in: true` lists them. When one clearly suits the request better, such as an anime model for an anime clip, suggest it and wait for the user to agree. Each has its own prompting file in `references/models/`.

## Characters, references, and voices

`get_model` reports which variants accept `@character` and `@reference` mentions (`mentions`), the shared image budget (`max_images`, per variant in `max_images_by_model`), and whether a character's saved voice rides along into video (`character_voices`; turn it off with `use_character_voices: false`).
