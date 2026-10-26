# Open image models: HiDream, Chroma, Stable Diffusion

Older and community open-weights image models on Mage, all opt-in: HiDream (`hidream`), Chroma (`chroma`), Stable Diffusion v3.5 Large (`stable_diffusion_v35_large`), Stable Diffusion XL (`stable_diffusion_xl`), SDXL Plus (`sdxl_plus`) and Stable Diffusion v1.5 (`stable_diffusion_v15`). None has a dedicated prompting guide; this file rests on their model cards and on how Mage runs them.

## Variants

| Model (`model_id`) | Best for | Prompt style |
|---|---|---|
| HiDream (`hidream-fast`) | Fast general images, photoreal or illustrated | Natural language |
| Chroma (`chroma-v1-hd`) | General images across artistic, photographic and niche styles | Natural-language paragraph |
| Stable Diffusion v3.5 Large (`sd-3-5-large`) | The Stable Diffusion that follows detailed prompts best; short signs | Natural language |
| Stable Diffusion XL (default checkpoint) | Photoreal output: the default is a community photoreal fine-tune | Short, tag-forward phrases |
| SDXL Plus (same checkpoint) | The same, with a high-resolution second pass and automatic face and hand repair; slower | Short, tag-forward phrases |
| Stable Diffusion v1.5 (default checkpoint) | The classic look, cheap; native 512 px | Short, tag-forward phrases |

The SDXL, SDXL Plus and v1.5 `model_id`s are checkpoint hashes: leave `model_id` out and the default runs. All six take `aspect_ratio` 21:9 to 9:21 (default 4:5) and no `resolution`.

## How Mage sends your prompt

- **Negative prompts**: `negative_prompt` works on Chroma, SD3.5 Large, SDXL, SDXL Plus and v1.5. On Chroma it is missing from `get_model`'s field list but passes through; when it is empty, Mage uses `bad quality, worst quality`. On HiDream it does nothing: the Fast model runs without guidance.
- **Weighting**: SDXL, SDXL Plus and v1.5 read the common weight syntax: `(word:1.3)`, `(word)` for a little more, `[word]` for a little less; weights are capped at 1.6. Escape literal parentheses as `\(` and `\)`. SD3.5 Large, HiDream and Chroma do not parse weights: parentheses go through as text.
- **Prompt length**: SDXL and SDXL Plus, at the default `prompt_embed_version` `"v1"`, keep only about the first 75 tokens (50 to 60 words) and drop the rest. For a longer prompt, send `prompt_embed_version: "v2"`, which reads long prompts in chunks. v1.5 chunks long prompts by itself. SD3.5 Large reads about 256 tokens; put the essentials first.
- **Input image**: SD3.5 Large, SDXL, SDXL Plus and v1.5 take one `image` as an image-to-image starting point (strength 0.5), and the output takes that image's shape. The prompt describes the whole result, not an edit instruction: these models do not follow "change the sofa to leather". HiDream and Chroma take no image.
- No characters or references: any `@` followed by a letter is refused.
- Never send `prompt_enhance`: on these models it appends random words to the prompt.
- If SD3.5 Large colors look burnt or over-contrasted, set `guidance_scale` to about 4.5.

## Prompt structure

- **HiDream**: plain sentences with each object's attributes and the relations between objects spelled out ("a small red cube resting on top of a large blue sphere, on a wooden table"); relations and attributes are its strength.
- **Chroma**: one natural-language paragraph in the model card's order: subject and styling, then the light and color treatment, then the background, then finish statements ("The photo is sharp and well-composed. It looks professionally done.").
- **SD3.5 Large**: a strong, descriptive prompt that names the elements, colors and subjects; short keyword prompts and long narrative paragraphs both work.
- **SDXL, SDXL Plus, v1.5**: compact, comma-separated visual tokens, most important first: (1) subject and subject count, (2) key appearance details, (3) pose or action, (4) framing or composition, (5) environment, (6) style or render cues. Prefer short tag clusters over conversational instructions, use weighting sparingly, and skip filler like `masterpiece`, `best quality` or `stunning`. The SDXL default is tuned for photos, so photographic terms (lens, light, film stock) pull harder than anime tags; for anime, prefer Anima.
- **Anime subjects** on the SD models: use count tags when the count is clear (`1girl`, `1boy`, `2girls`, `solo`), then concrete tags for hair, eyes, outfit, pose, expression, framing and background: `1girl, solo, anime illustration, long black hair, blue eyes, school uniform, soft smile, standing under cherry blossoms, spring petals, full body, looking at viewer, clean lineart, detailed background`.

## Vocabulary

None published for these models. Use concrete visual terms: the medium (photo, oil painting, 3D render), framing (close-up, full body, wide shot), light (soft window light, rim light, overcast), and color ("cold color palette, muted colors", from the SD3.5 card's own example).

## References, characters, and frames

- Only the Stable Diffusion models take an `image`, as a starting point at strength 0.5: the composition and colors carry over and the details change. To keep a person or product exact, use a model with references (Mango, GPT Image, Nano Banana).
- For a consistent subject across a set, repeat the same description word for word and fix the `seed`.

## Text in the image

- **SD3.5 Large**: short signs work: "a capybara holding a sign that reads Hello World".
- **HiDream**: quote the words on a sign: `A cat holding a sign that says "HELLO".`
- **SDXL, SDXL Plus, v1.5**: the model cards state they cannot render legible text. Add text afterwards in an editor.
- **Chroma**: untested; keep any text to a word or two, or add it afterwards.
- For real typography, use GPT Image 2.5 Flare.

## Avoid

| Instead of | Write |
|---|---|
| A 100-word prompt on SDXL at `prompt_embed_version` `"v1"` | Under about 60 words, or `prompt_embed_version: "v2"` |
| A negative prompt on HiDream | The wanted state, in the prompt |
| `(blue:0.3)` weights on SD3.5 Large, HiDream or Chroma | Plain words; weights only on SDXL, SDXL Plus and v1.5 |
| Edit instructions with an `image` on Stable Diffusion | A description of the whole finished image |
| Complex spatial setups on SDXL or v1.5 ("a red cube on a blue sphere") | HiDream or SD3.5 Large, or a simpler composition |
| Filler like "masterpiece, 8k, best quality" stacks | Concrete subject, light and framing |
| Non-English prompts on v1.5 | English: it was trained mostly on English captions |

## Examples

HiDream, 4:5:

```
A ginger cat sitting upright on a wooden stool, holding a small cardboard sign in both front paws that says "HELLO". Behind it, a sunny kitchen with a green tiled wall. Soft morning light from the left, photoreal, shallow depth of field.
```

Chroma, 4:5, with `negative_prompt: "low quality, ugly, unfinished, out of focus, deformed, disfigure, blurry, smudged, restricted palette, flat colors"`:

```
A high-fashion close-up portrait of a blonde woman in clear sunglasses. The image uses a bold teal and red color split for dramatic lighting. The background is a simple teal-green. The photo is sharp and well-composed, designed for viewing with anaglyph 3D glasses. It looks professionally done.
```

SD3.5 Large, 3:2:

```
A whimsical hybrid creature, half waffle and half hippopotamus, basking in a river of melted butter in a breakfast-themed landscape. It has the bulky body of a hippo, but its skin is a crispy waffle with a glistening grid of syrup. Pancake-like foliage and oversized utensils peek out in the background, and a towering pepper mill stands in for a tree. A warm morning glow falls over the scene as the creature yawns and a flock of birds takes flight.
```

SDXL (photoreal default), 2:3, with `negative_prompt: "cartoon, illustration, blurry, deformed hands"`:

```
photo of a young woman in a yellow raincoat, standing on a wet city street at night, (neon reflections:1.2), medium shot, 50mm lens, shallow depth of field, cinematic color
```

Stable Diffusion v1.5, 1:1:

```
a photo of an astronaut riding a horse on mars, red desert, dramatic sky, wide shot
```
