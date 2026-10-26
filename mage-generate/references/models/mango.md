# Mango (`mango`)

Mage's flagship image family: consistent characters, precise edits that leave the rest of the image alone, and one scene merged from several references. Mango 3 (`mango-v3`) is the default still.

## Variants

| `model_id` | Name | `resolution` | `@handles` | Point and box tags | Use it for |
|---|---|---|---|---|---|
| `mango-v3` | Mango 3 | 1K, 2K | yes | yes | Every final still: exact instructions, multi-reference scenes, edits |
| `mango-v3-turbo` | Mango 3 Turbo | 1K, 2K | yes | yes | Drafts and volume; layouts and text. Same prompts as Mango 3 |
| `mango-v3s` | Mango 3S | 2K, 3K | yes | no | A 3K still |
| `mango-v2` | Mango 2 | 2K, 3K, 4K | yes | no | A 4K still |
| `mango` | Mango | 1K–4K | no | no | Matching earlier work on the original Mango only |

- One prompt carries across the family: draft on Turbo, final on Mango 3 with the same text. Coordinate tags (below) work only on Mango 3 and Mango 3 Turbo; drop them for the others.
- Native text in 14 languages beyond English and Chinese is Mango 3 and Mango 3 Turbo only.
- Mango 3 reasons over your prompt and expands it before drawing. It needs precise facts, not stacked adjectives.
- The original `mango` refuses every `@handle`, `@image1` included. Send its inputs in `image` and `additional_images` and write `image 1`, `image 2` in plain words.

## How Mage sends your prompt

- Fields: `prompt`, `model_id`, `aspect_ratio` (21:9 to 9:21), `resolution`, `image`, `additional_images`. Mage renders an exact pixel size from `aspect_ratio` and `resolution`, so aspect-ratio, resolution and "4K" words in the prompt do nothing: set the fields.
- All images reach the model as one numbered list, in this order: `image`, then `additional_images`, then each mentioned character in order of first mention, then each mentioned reference in order of first mention. Up to 10 in all.
- Mage rewrites every mention before the model reads it, and numbers it for you:

| You write | The model reads |
|---|---|
| `@image1`, `@image2` | `image 1`, `image 2` (your own inputs, in order) |
| `@ana` (a saved character) | `character from image N` |
| `@red-coat` (a saved outfit) | `outfit from image N`; likewise `location`, `pose`, `object` |

- Numbered images are this model's convention, so on Mango name each image by its number and say what to take from it. Never write unnumbered pointers ("the reference", "the attached photo").
- A mention is replaced wherever it appears, with the long phrase each time. Mention a handle once, bind a name to it, and use the name afterwards: `Ana (@ana) sits…` becomes `Ana (character from image 2) sits…`.
- Any `@` followed by letters is a handle. `@Image 1`, `@video1`, an email address, or an unsaved handle is refused before anything is charged.
- There is no negative-prompt field. Put exclusions in a sentence ("Do not include any text or hand-drawn edges from the sketch").
- One call returns one image.

## Prompt structure

Write coherent sentences: subject + action + environment, then style, color, lighting and composition when the look matters. Name the image type first when there is one ("Design a logo…", "Create an infographic…", "A poster…"). Keep it under about 600 words; past that, details get dropped. For a busy scene, inventory every element by location instead of adding adjectives.

Text to image:

```
[Image type or use, if any.] [Subject] [action] in [environment].
[Key elements, placed: "On the left… In the foreground… On the top shelf…"]
[Style or medium.] [Light: source, direction, the shadows it casts.] [Framing or lens.]
```

From references, in two parts: what to keep, then the new scene:

```
[Reference target: what to take from which image — "Ana's face and hair from image 2", "the bottle's shape and label from image 3".]
[Generated scene: setting, layout, where each subject is, what they do.]
[Style and light; "consistent art style and harmonious composition" when merging.]
```

Edit (an input image is the canvas):

```
Keep [named elements: pose, face, composition, lighting] unchanged.
[Add | Remove | Replace | Change] [exact target by visible traits or position] [to what].
[The physical consequence: shadows, reflections, how it blends into the scene.]
```

## Vocabulary

- Style: precise names beat adjectives: "picture book style", "children's book illustration", "Monet oil painting", "linear minimalist icon style", "3D cartoon style", "anime key visual", "felt wool figure on a small stand", "transparent crystal".
- Photography: "photorealistic", "cinematic photographic feel", "high-definition commercial product photography", "editorial portrait, shot in medium format, shallow depth of field, dramatic studio lighting". A comma-phrase brief works for a single portrait or product; use sentences once there are several subjects or a layout.
- Light: plain and directional ("Sunlight shines from the right side, casting light and shadow on the desk").
- Knowledge images: exact technical terms plus the format and layout ("Draw this system of equations and its solution steps on a blackboard: 5x + 2y = 26; 2x − y = 5.").
- Edit verbs the model is tuned on: add, remove, replace, change, turn into, "keeping … unchanged".

## References, characters, and frames

- One role per image, said with its number: "Dress the character in image 1 in the outfit from image 2." "Replace the subject in image 1 with the subject from image 2." "Apply the style of image 2 to image 1." "Use image 1 as the background."
- Keeping a person on model (the prompt guide's Likeness section): mention the character and pass the face crop as `image`: `Ana (@ana), her face exactly as in @image1, …`. The model reads `Ana (character from image 2), her face exactly as in image 1`.
- Name the target in edits by what it visibly is, never a pronoun: "the tallest panda", "the person on the left", "the largest bread man".
- Marks drawn on the input (all variants): a circle, arrow, doodle or colored box, then point at the mark in words: "Insert a TV where the red area is marked and a sofa where the blue area is marked. Keep the original wooden style." End with "Remove all sketch lines."
- Coordinates (Mango 3 and Mango 3 Turbo): a 0–999 grid per image, (0,0) top-left, (999,999) bottom-right; `x = round(x_px / width × 1000)`, the same for y. Put the tag right after the image label.
  - `<point>x y</point>`: the model decides the affected area. `@image1 <point>520 460</point>` reads as `image 1 <point>520 460</point>`.
  - `<bbox>x1 y1 x2 y2</bbox>` (top-left, bottom-right): the exact region and size.
  - Name the target when a box holds several subjects ("the person on the left in image 1 <bbox>…</bbox>"), and box what must not change ("keep image 1 <bbox>700 120 920 360</bbox> unchanged").
  - Use coordinates only when you know them: you can see the image, or you have pixel positions from a layout you built. A guessed box is worse than words.
- Sketch, wireframe or floor plan to render: name the subject ("a photorealistic modern living room"), say what must match ("layout and furniture placement exactly match image 1"), add "Generate based on the text in the image" when it carries labels, and "Do not include any text or hand-drawn edges from the sketch."
- A character image for video or `create_character`: one person only, head through knees, slight three-quarter turn with the face nearly frontal and large, both empty hands visible, plain neutral backdrop, soft even light showing both eyes, neutral closed-mouth expression. Close with constraints: "No writing, logos or watermark. No props. No collage or multiple views. This image fixes appearance only."
- Several images that belong together (a storyboard, a campaign, a character in four settings): one call each with the same handles and references, changing only the scene line. "A set of four" in one prompt gives one image, at best a sheet of panels. When you want that sheet, ask for it: "one image laid out as a 2×2 grid of four panels, thin white gutters".

## Text in the image

- Put the exact words in double quotes, with position and style: `the title "NIGHT MARKET" in bold red brush lettering across the top`. Never `titled Night Market`.
- Say what the image is for: `Design a logo for a gaming company. The logo shows a dog playing with a game controller. The company name "PITBULL" is written below it.`
- Mango 3 and Mango 3 Turbo render text natively in Russian, Arabic, Filipino, Thai, Turkish, Korean, Malay, Spanish, Portuguese, Indonesian, French, German, Vietnamese and Japanese, besides English and Chinese. Write the quoted words in their own script. Other Mango variants: English and Chinese.
- Text edits are edits: `Change the text on the sign to "OPEN LATE" in the same font.` "Enlarge the title to fill the red box and match its style to the saxophone icon."
- Long copy that must be spelled letter-perfect belongs on GPT Image 2.5 Flare (`gpt-image.md`).

## Avoid

| Instead of | Write |
|---|---|
| `girl, umbrella, tree-lined street, oil painting` | `A girl in a long dress walks under a parasol along a tree-lined path, painted in the style of a Monet oil painting.` |
| `put that one in pink` | `Dress the tallest panda in a pink opera costume and headdress, keeping its pose unchanged.` |
| `like the reference`, `same as the photo` | `with the face and hair of the woman in image 1` |
| `16:9, 4K, ultra HD` | Set `aspect_ratio` and `resolution` |
| `Generate four images of…` | Four calls, or one image laid out as a grid |
| `@ana` repeated in every clause | `Ana (@ana)` once, then `Ana` |
| `<bbox>` on Mango 3S, Mango 2 or Mango | Words, or a mark drawn on the image |
| Twelve adjectives about mood | The one light source, one lens, one style that make that mood |

## Examples

Text to image, a busy scene inventoried by place (Mango 3):

```
A cluttered developer's desk at night. An open laptop shows green code on a black screen. Beside it, a mug printed with the word "DEPLOY" lets off a thin curl of steam. An open notebook shows a hand-drawn Venn diagram of three overlapping circles in gray, blue and light green. A yellow sticky note carries a three-level mind map. A fountain pen lies with its cap beside it, next to a phone lighting up with a new message. A small pot of succulents sits in the far corner. Behind, a bookshelf falls soft and out of focus. A desk lamp on the right casts warm light and long shadows across the desk.
```

A saved character in a saved outfit and location (Mango 3):

```
Ana (@ana) wears @red-coat and stands at the rail of @harbor-pier at dusk, one hand on the rail, looking back over her shoulder toward the camera with a small smile. Wind lifts the hem of the coat. Keep her face, hair and the coat's cut and color exactly as in their images. Photorealistic, 50mm lens at eye level, the low sun behind her rimming her hair, harbor lights starting to glow in the background.
```

Edit that keeps everything else (Mango 3, the product shot in `image`, the new bottle in `additional_images`):

```
Keep the composition, the marble surface, the lighting and the bottle's position unchanged. Replace the green glass bottle with the frosted white bottle from @image2, matching its label exactly. Its reflection and shadow on the marble follow the same light from the upper left.
```

Point and box edit (Mango 3 Turbo for the draft, Mango 3 for the final; the room photo is `image`):

```
Replace the floor lamp at @image1 <point>812 430</point> with a tall potted fiddle-leaf fig in a terracotta pot. Replace the painting in @image1 <bbox>310 120 590 360</bbox> with a large black-and-white photograph of ocean waves. Keep @image1 <bbox>0 600 999 999</bbox> unchanged. Everything blends with the room's warm afternoon light.
```

Character image for a video shoot (Mango 3, 2:3):

```
Asset: one fictional character identity reference for a live-action short film. One original woman, early thirties, athletic build, warm brown skin, dark brown eyes, short natural curls, small gold hoop earrings. She wears a faded olive bomber jacket over a white T-shirt, dark jeans and white sneakers. One person only, a single portrait from the top of her head through the knees, standing in a slight three-quarter turn with her face nearly frontal and both empty hands relaxed at her sides. Plain warm-gray studio backdrop, soft even light showing both eyes and the fabric textures, natural unretouched skin. Neutral closed-mouth expression. No writing, logos or watermark. No props. No collage or multiple views. This image fixes appearance only.
```

Poster with non-English text (Mango 3):

```
A vertical poster for a neighborhood jazz night. A saxophonist in a brown suit plays under a single warm spotlight on a small brick-walled stage, his shadow long on the wall behind him. Across the top, the title "NOCHE DE JAZZ" in tall cream art-deco lettering; along the bottom, "Viernes · 21:00 · Café Lumbre" in small clean sans-serif. Deep navy and amber palette, screen-print texture.
```
