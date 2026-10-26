# MOSS-Image (`moss_image`)

An open-weights text-to-image model from the OpenMOSS team (opt-in), for long, detailed prompts and English or Chinese text in the image (signs, posters, menus), at 1K or 2K. It also takes an experimental layout JSON that places each element in a box.

## Variants

One variant, `moss-image`. Leave `num_inference_steps` and `guidance_scale` at Mage's defaults. It is slower than few-step models.

- `resolution`: `1k` (about one megapixel) or `2k` (about two).
- `aspect_ratio`: 21:9 to 9:21, default 4:5.

## How Mage sends your prompt

- `prompt` reaches the model as written, up to about 4,000 tokens: prose, tags, or a layout JSON string.
- Text to image only: no `image`, no `@handle`s. Any `@` followed by a letter is read as a handle and refused, which rules out `@artist` tags (see Avoid).
- `negative_prompt` works (it is not in `get_model`'s field list, but it passes through). It is empty by default.
- Never send `prompt_enhance`: on this model it appends random words to the prompt.
- The canvas Mage renders, which a layout's boxes must match:

| `aspect_ratio` | `1k` (W x H) | `2k` (W x H) |
|---|---|---|
| 1:1 | 1024 x 1024 | 1440 x 1440 |
| 4:5 | 896 x 1152 | 1280 x 1616 |
| 2:3 | 832 x 1216 | 1168 x 1760 |
| 9:16 | 768 x 1344 | 1072 x 1920 |
| 9:21 | 640 x 1536 | 944 x 2208 |

For the landscape ratios (5:4, 3:2, 16:9, 21:9), swap W and H.

## Prompt structure

Three input forms; prose and structure can be combined.

- **Caption** (the default): cohesive prose about visible choices: subject and action, appearance, setting, camera and framing, medium, lighting, materials, palette, mood. Spatial relations in words. Visible text quoted exactly.
- **Tags**: in the order quality, score, meta, year, character, series, artist, general: `best quality, highres, hatsune miku, vocaloid, 1girl, blue hair`.
- **Layout JSON** (experimental): a whole-image summary plus one item per text block or object, each with a box. Use it for exact text placement, posters, several panels, or controlled object positions; a detailed image does not need one by default.

English gets the best results (most of the training data); Chinese and other languages work.

### The OpenMOSS prompt enhancer

The OpenMOSS team ships an enhancer method. Follow its steps:

1. **Choose caption or layout.** Layout only for placed text, posters, panels, or object relations that must be exact.
2. **Preserve the request**: the user's subjects, counts, relations, medium, style, exclusions, and every word of requested text, unchanged.
3. **Fill ordinary gaps** (light, framing, palette, materials) without changing the style the user asked for, and without stacking quality tags.
4. **Draft a layout** with top-left pixel boxes `[x1, y1, x2, y2]` on the canvas from the table above.
5. **Convert each box** to the model's centered `yxyx` form: `[y1 - H/2, x1 - W/2, y2 - H/2, x2 - W/2]`. On a 1024 x 1024 canvas, a title spanning x 128 to 896 and y 96 to 224 becomes `[-416, -384, -288, 384]`.
6. **Send the JSON as one line** in `prompt`, with the same `aspect_ratio` and `resolution` the boxes were drawn for.
7. **Check the result**: subject, every word of text, positions, and canvas.

Layout schema:

```
{"summary": {"meta": ["poster"], "canvas": "single", "caption": "<the whole scene and its style>"},
 "items": [{"label": "text", "caption": "<how the text looks>", "text": "<exact words>", "bbox": [ymin, xmin, ymax, xmax]},
           {"label": "object", "caption": "<the object>", "bbox": [ymin, xmin, ymax, xmax]}],
 "bbox_coord_space": "abs_centralized", "bbox_format": "yxyx"}
```

Keep the layout JSON as the source of truth: to change a word, a caption or a position, edit that field and regenerate.

## Vocabulary

No published term list. The enhancer asks for camera and framing, medium, lighting, materials and palette in plain words, and warns against redundant quality tags and unrequested style changes. Tag mode uses anime-board quality tags (`best quality`, `highres`) and general tags.

## References, characters, and frames

None: MOSS-Image takes no images. For a character kept across a set, repeat the same description word for word and fix the `seed`; for a picture to match, use a model with references.

## Text in the image

- Its headline strength: Chinese and English text with automatic layout.
- Quote visible text verbatim, in its original language, keeping punctuation, capitalization and line breaks. Keep the words to render apart from instructions about them.
- Automatic line breaks may not fall where you want: put a real line break in the prompt where each line should end.
- In a layout, the exact string goes in the item's `text` field. Always real copy, never "headline here".
- For several text blocks in fixed places (a poster, a menu, a label), use a layout.

## Avoid

| Instead of | Write |
|---|---|
| `@artist` tags (the request is refused) | The artist name without `@`, or the style described in words |
| Placeholder copy in a layout | The real words |
| Boxes drawn for one canvas, sent at another size | The `aspect_ratio` and `resolution` the boxes were drawn for |
| Top-left `xyxy` boxes in the final JSON | Centered `yxyx`, converted as above |
| A stack of quality tags on a caption | Plain visual description |
| A very short prompt | A full caption: the model is built for long prompts |

Negative prompt, when one helps: `worst quality, bad anatomy, watermark, jpeg artifact, nsfw`.

## Examples

Caption with a sign, 3:2:

```
A cozy bookstore cafe at night seen from the rainy street, warm light spilling from tall windows onto wet cobblestones. By the door stands a chalkboard sign that reads "FRESH COFFEE $3" in white hand-lettered capitals. Inside, shelves of books and a few readers at small wooden tables. Photo, eye level, 35mm, soft reflections in the puddles, muted teal street against amber interior light.
```

Chinese handwriting, with real line breaks, 4:5 (the note reads: "Remember to buy milk and eggs! Two cartons of milk, a dozen eggs. Pick up a bag of bread too."):

```
A wide view of a refrigerator beside a kitchen counter with a fruit bowl. A small yellow sticky note on the refrigerator door is handwritten in Chinese:
"记得买牛奶和鸡蛋！
牛奶两盒，鸡蛋一打。
顺便带一袋面包。"
```

Layout poster, `aspect_ratio` 1:1 at `1k` (1024 x 1024):

```
{"summary": {"meta": ["poster"], "canvas": "single", "caption": "A minimalist travel poster with a cream background, a blue mountain illustration, and the title EXPLORE at the top."}, "items": [{"label": "text", "caption": "Large dark-blue uppercase title centered at the top.", "text": "EXPLORE", "bbox": [-416, -384, -288, 384]}, {"label": "object", "caption": "A flat blue mountain illustration in the lower center.", "bbox": [-192, -288, 384, 288]}], "bbox_coord_space": "abs_centralized", "bbox_format": "yxyx"}
```

Tags, 4:5:

```
best quality, highres, 1girl, solo, long blue hair, twin tails, futuristic stage outfit, holding a microphone, stage lights, cheering crowd in the background, dynamic angle
```
