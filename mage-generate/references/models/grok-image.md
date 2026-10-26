# Grok Image (`grok_image`)

xAI's Grok Imagine image models on Mage (opt-in), in three tiers, for generation and edits from up to 3 reference images. xAI's safety filter applies. xAI judges a prompt by one thing first: whether the subject in the picture is the subject in the prompt.

## Variants

| `model_id` | Use it for |
|---|---|
| `grok-imagine-image-quality` | The family default |
| `grok-imagine-image` | Cheap drafts and volume |
| `grok-imagine-image-2.0` | The newest; xAI's prompting guide is written for it |

- `quality` applies to 2.0 only: `low` or `medium` (the default). Pin `medium` and `2k` when fine detail must be recognizable (a watch face, fabric weave, a product label).
- xAI is retiring the Quality tier, after which `grok-imagine-image-quality` is served by Grok Image 2.0. Prefer 2.0 for a new series so the look does not shift mid-project.
- Every input image adds to the price; `estimate_cost` has the total.

## How Mage sends your prompt

- `prompt` reaches the model as written. No negative prompt.
- No input image: a generation. Any input image: an edit of it.
- Up to 3 images in all: your `image`, then `additional_images`, then `@handle` characters, then `@handle` references, numbered in that order. Mage rewrites mentions to match: `@image1` becomes "image 1", and with one image of your own a character `@ana` becomes "character from image 2".
- `aspect_ratio` is sent on every call (default 1:1): 1:1, 3:2, 2:3, 4:3, 3:4, 16:9, 9:16, 2:1, 1:2, 20:9, 9:20, 19.5:9, 9:19.5. For an edit, set the source's ratio. 3:2 suits most photographs.
- Any `@` followed by a letter is read as a saved handle and refused when none matches.

## Prompt structure

Use xAI's fixed six-part order for every prompt, and keep the same order across a series:

1. **Subject**, in one opening sentence: what it is, the state or form it is in, what holds or supports it, and the setting. "A matte sage-green ceramic pour-over dripper sitting on a glass carafe half full of coffee, on a pale oak counter against white square tile."
2. **Details and focal point**: every key element by name and in the form it takes (a wool coat is "heavy twill with a visible weave"; coffee in a glass carafe is "dark amber, lighter at the edges"), how many of each, and the camera angle, so the cluster fills the frame.
3. **Art direction**: the color fields and two or three named props ("oak counter, white tile, linen towel, one brass spoon").
4. **Light**: source, direction and hardness, what the highlights and shadows look like, and an exposure bright enough to read the subject.
5. **Color**: the subject's colors and the background's colors as separate statements.
6. **Composition**: the crop, what the frame cuts off, what stays sharp. One scene.

- A standalone still needs four to six sentences. Write prose that describes one photograph.
- State the camera angle once in the subject part and repeat it, in the same words, in the composition part.
- Leading with mood, film stock or an avoid list gives a styled scene where the subject is a stand-in: subject first, always.

### Generate, then edit (xAI's playbook)

Check every result against the prompt, point by point:

1. The right subject, in the form described.
2. Each named element visible, in the form described.
3. Every count right.
4. Each object the one named (a plate, not a bowl; a tote, not a backpack).
5. Bright enough to read the subject.

A matching background with the wrong subject is a miss. When the subject itself is wrong (another object, a missing element, a wrong count), regenerate with a sharper subject sentence. When only one to three details are wrong, edit the result. Each pass changes only the failed detail; keep the rest of the prompt word for word.

## Vocabulary

- **Camera**: "45-degree three-quarter view at counter height", "straight-down overhead", "low three-quarter angle", "eye level, framed from the waist up", "50mm product photograph", "35mm photograph".
- **Light**: name source, direction and hardness: "hard afternoon sun from the left with on-camera fill flash", "soft window light from the left, bright and warm". For readable exposure: "bright and vivid, hard sun, flash, warm shadows with texture".
- **Materials over adjectives**: "brushed steel with fine horizontal grain", not "not shiny".
- **Texture**: state each texture once, physically, on the surface it belongs to; repeated texture words get painted onto the wrong surface.
- **Style**: ultra-real photography, anime, oil painting, pencil sketch. For a style change, describe the target look in the edit prompt.

## References, characters, and frames

- **Edit prompt shape**: the changes first, then one sentence that keeps the same subject, angle, crop and prop placement. "Replace the metal watch strap with a brown leather strap with cream stitching. Keep the same wrist, the same shirt cuff, the same angle, and the same desk."
- An edit that opens with "keep everything" barely moves; an edit that pastes a whole new prompt restages the scene (the subject drifts, props duplicate, objects morph).
- When a fix does not land, change the words and point at the part ("the leather shows creases where the strap bends") instead of repeating "more realistic".
- **Multi-turn**: feed each output back as `image` for the next edit.
- **Several inputs**: refer to them by Mage's numbers ("put the sneaker from image 2 on the concrete step in image 1"); the output's framing follows `aspect_ratio`.
- **A consistent character across scenes** (xAI's storyboard playbook): generate the first keyframe, then make each other scene as an edit of it that uses it only as a subject and style reference and asks for the new scene and camera angle. Or save the character with `create_character` and mention the `@handle`.
- **Product placement**: edit one product photo into several scenes at the delivery ratio, asking each time to keep the product exactly as it is.

## Text in the image

xAI publishes no typography guidance. Quote the exact words and say where they sit and in what lettering; keep it to a short label or sign. For posters, menus or anything text-led, use GPT Image 2.5 Flare.

## Avoid

| Instead of | Write |
|---|---|
| Opening with mood, film stock or "avoid ..." | The subject sentence |
| "slightly underexposed", "crushed shadows" | Bright, readable light with texture in the shadows |
| "chromatic fringing", "dust", "scratches" | Leave defect words out: they get drawn as defects |
| A long avoid list | A count or a specific object paired with the wanted thing: "one stainless spoon resting on the saucer" |
| "make the coat darker" in a generation prompt | "a charcoal wool coat": a generation has no before and after |
| "a bag", "a dish" | "a tan leather satchel", "an enameled cast-iron skillet" |
| Repeating "more realistic" | The exact part that looks wrong and what it should look like |

## Examples

Product, 3:2:

```
A pair of white leather low-top sneakers with gum rubber soles, shot from a low three-quarter angle. The laces are loosely tied, the toe boxes show soft creases, and the left shoe sits slightly ahead of the right. They stand on pale gray concrete against a warm off-white wall. Hard morning sun from the right casts long, sharp shadows, with soft fill on the shaded side. 50mm product photograph from a low three-quarter angle, both shoes sharp, cropped just above the heel tabs.
```

Portrait, 2:3:

```
A woman in her sixties with short silver hair and reading glasses pushed up on her head, laughing while she pots a small olive tree at a wooden workbench. Her hands are dusted with dark soil and her sleeves are rolled to the elbow. Terracotta pots and a steel trowel sit on the bench beside her. Soft window light from the left, bright and warm, with gentle shadows. 35mm photograph at eye level, framed from the waist up, her face in sharp focus.
```

Food, 4:3:

```
A vegetarian Greek salad in a warm cream ceramic bowl, shot from a slight overhead angle. Cucumber, tomato, thick red onion, irregular feta crumbles and wrinkled black olives overlap in olive oil, with oregano on the tomatoes. The bowl sits on butter-yellow linen over terracotta; a warm pita is partly visible at the right edge and a fork rests on the rim. Hard summer sun and on-camera flash, bright and vivid, with warm shadows. 35mm photograph from a slight overhead angle, the food filling the bowl, one frame.
```

Edit, the watch photo as `image`, its own ratio:

```
Replace the metal watch strap with a brown leather strap with cream stitching. Keep the same wrist, the same shirt cuff, the same angle, and the same desk.
```

Style change, the photo as `image`:

```
Render this as a pencil sketch with detailed cross-hatched shading on off-white paper. Keep the same people, poses and framing.
```
