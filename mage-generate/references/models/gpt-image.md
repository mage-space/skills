# GPT Image (`gpt_image_2`)

OpenAI's image models on Mage, for generation and edits from up to 15 input images. GPT Image 2.5 Flare is the pick for text in the image: precise prompt adherence, graphics, memes, comics, and detailed edits from many references. OpenAI's safety filter applies and Mage cannot override it.

## Variants

| `model_id` | Use it for | Notes |
|---|---|---|
| `gpt-image-2.5-flare` | The usual choice: text, layouts, comics, product shots, edits | Speed-tuned. Set it explicitly: the family's default `model_id` is `gpt-image-2`. |
| `gpt-image-2.5-sunburst` | Opt-in. The hardest edits: identity, product geometry, dense multi-font layouts | The quality-first model; slower, same price as Flare. |
| `gpt-image-2` | Opt-in. Matching earlier work | No `xhigh` or `max` quality. |

`quality` is the cost lever (default `low`): `low`, `medium`, `high`, `xhigh`, `max`, each several times the price of the one below; 2K doubles the price, and every input image adds to it. Price it with `estimate_cost`.

- Draft on Flare at `low`; it is strong for its price.
- Go to `medium` when small text, dense panels or several fonts must be legible.
- Go higher, or to Sunburst, only when a named requirement still fails (a garbled label, a drifting face, a warped product), then try stepping back down. A higher level is not always a better image.

## How Mage sends your prompt

- `prompt` reaches the model as written; nothing expands or rewrites it.
- No input image: a fresh generation. Any input image: an edit of those images.
- Mage numbers the inputs in this order: your own `image`, then `additional_images` (image 1, 2, ...), then each `@handle` character, then each `@handle` reference. It rewrites the prompt to match: `@image1` becomes "image 1"; with two images of your own, a character `@ana` becomes "character from image 3" and a saved outfit `@red-coat` "outfit from image 4". All of them share the 15-image budget.
- `aspect_ratio` (21:9 to 9:21, default 4:5) and `resolution` (1K is about one megapixel, 2K doubles each side) set the canvas on every call, edits included: for an edit, pick the ratio closest to the source or the result is reframed.
- Output is always JPEG, so there is no transparent background. For a cutout, render the subject on a plain, evenly lit backdrop ("plain light-gray seamless backdrop, soft even light, no shadow on the backdrop") and remove the background afterwards with a cutout tool. Never ask for a "transparent" or "checkerboard" background: the model paints the checkerboard.
- No negative prompt and no mask: write exclusions into the prompt and name the region to change in words.
- Any `@` followed by a letter is read as a saved handle, and the request is refused when none matches, so a social handle on a poster cannot be written with its `@` (see Text).

## Prompt structure

Say what the image is for first (ad, poster, UI mock, diagram, product photo, comic): it sets the mode and the polish. Then, in a fixed order: scene or background, subject, key details, constraints. Anything complex gets short labeled lines instead of one paragraph:

```
<What it is and what it is for>
Scene: <setting, light, time of day>
Subject: <who or what, look, pose, action>
Details: <materials, props, framing, camera>
Text (EXACT, verbatim): "<copy>"   Typography: <weight, style, color, placement>
Constraints: <what must not appear or change>
```

- Any format works (prose, labeled lines, JSON-like blocks, tags); choose the easiest to read and change.
- State composition and placement outright: "logo top-right", "subject centered with empty space on the left for copy", "full body visible, feet included".
- Start clean and iterate with single changes rather than packing every idea into one long prompt.
- An edit has two parts: the change ("Replace ONLY the white chairs with oak chairs") and a preserve list ("Keep the camera angle, room lighting, floor shadows and every other object unchanged").

## Vocabulary

- **Medium first**: photograph, watercolor, 3D render, pixel art, flat vector icon, children's book illustration, classroom handout.
- **Photorealism**: the word "photorealistic" switches it on; "real photograph", "taken on a real camera", "iPhone photo", "35mm film, 50mm lens" (lens terms are read as look, not physics).
- **An honest photo**: "honest and unposed, real skin texture, worn materials, everyday detail. No glamorization, no heavy retouching." For an ordinary snapshot, also "Avoid cinematic lighting, dramatic color grading, or stylized composition."
- **Hard scenes** (wide, low light, rain, neon): give scale, atmosphere and color detail; mood words alone trade realism for style.
- **People**: body framing, relative scale ("child-sized next to the table"), gaze ("looking down at the open book, not at the camera"), hands ("hands naturally gripping the handlebars").
- **Texture cues** only when needed: film grain, textured brushstrokes, macro detail.

## References, characters, and frames

- **One role per input, by number**: "Image 1: product photo. Image 2: style reference (palette and brushwork only)." Then say how they combine: "Apply image 2's style to image 1", "Place the dog from image 2 next to the woman in image 1, matching the lighting and perspective. Do not change anything else." Numbered inputs are this model's convention and match Mage's own `@handle` rewrite.
- **Identity edits**: list what must not change (face, facial features, skin tone, body shape, pose, expression, hairstyle, proportions) and match lighting, shadows and color temperature so the change is not "pasted on".
- **The edit loop** (OpenAI's playbook): generate a clean base, then pass each approved result back as `image` and change one thing per turn, restating the preserve list every turn ("Keep everything else unchanged: her face, the red coat, the street, the framing"). Compare each result with the last before adding instructions. Edits drift over many turns; when a region must stay pixel-identical, composite the approved change over the original in an image editor instead of asking again.
- **Character continuity** (OpenAI's playbook):
  1. Generate a clean reference of the original character: alone, full body, plain background, no text. Save it with `create_character` if it will recur.
  2. For each scene, edit from that image (as `image` or its `@handle`): describe the new scene, then a "Character consistency" list (same clothing, facial features, proportions, palette) and "Do not redesign the character."
  3. Check every scene against the reference before building on it.
- **Virtual try-on**: the person as image 1, garments as image 2 onward; "Replace only the clothing, fitted to her existing pose with realistic fabric behavior"; lock face, pose, background, camera angle and framing.
- **Re-staging**: change only the conditions ("Make it a winter evening with snowfall") and keep the geometry.

## Text in the image

- Quote the exact copy and give its placement, typography (weight, style, size, color, contrast, kerning, alignment) and count: "Render the tagline exactly once."
- Multi-part copy goes in a labeled verbatim block: `Billboard text (EXACT, verbatim, no extra characters): "Fresh and clean"`, then one `Typography:` line.
- Spell unusual names letter by letter when accuracy matters ("the brand name KAIRO, spelled K-A-I-R-O").
- Stop stray copy: "No extra text, no watermarks, no unrelated logos."
- Small text, dense panels, several fonts: `medium` quality or higher, and no tiny text in diagrams. For diagrams, give the real labels and numbers; the model does not check facts.
- Translate in place as an edit: "Translate all text into Spanish. Do not change any other aspect of the image."
- A social handle: write the name without the `@` (Mage would read it as a handle) and add the sign afterwards in an editor, or phrase it as a web address.
- Read every word of the result before delivering it. Fix a misspelling with an edit that spells the word out letter by letter.

## Avoid

| Instead of | Write |
|---|---|
| "transparent background", "PNG cutout" | A plain, evenly lit backdrop, then a cutout tool |
| A full new prompt for an edit | The one change, then the preserve list |
| Several changes in one edit turn | One change per turn, preserve list restated |
| "the reference", "the attached photo" | "image 2", by Mage's numbering |
| Mood words alone for night, rain or neon | Light sources, atmosphere, scale and color |
| `max` quality on the first try | A `low` draft, then escalate for a named failure |
| A long list of things to avoid | Two or three specific exclusions ("no watermark", "no extra text") |
| Fresh prompts for a recurring character or logo | Edits from one approved image, which keep it from drifting |

## Examples

Photoreal candid, Flare at `medium`:

```
Create a photorealistic candid photograph of an elderly sailor on a small fishing boat, calmly mending a net while his dog sits on the deck. Weathered skin with visible pores and sun texture, a few faded tattoos on his forearms. 35mm film look, medium close-up at eye level, 50mm lens. Soft coastal daylight, shallow depth of field, subtle film grain, natural color balance. Honest and unposed, real skin texture, worn materials. No glamorization, no heavy retouching.
```

Ad with exact copy, Flare at `medium`, 4:5:

```
A polished campaign image for Thread, a young streetwear brand: four friends laughing on a concrete stoop at dusk, natural poses, premium fashion photography, strong color direction, clean composition.
Text (EXACT, verbatim): "Yours to Create." in a bold condensed sans-serif, white, lower third, centered.
Render the tagline exactly once, clearly and legibly. No extra text, no watermarks, no unrelated logos.
```

Diagram, Flare at `high`, 3:2:

```
A simple biology diagram titled "Cellular Respiration at a Glance" for high school students: glucose turning into energy inside a cell through glycolysis, the Krebs cycle and the electron transport chain. Arrows connect the steps; label glucose, pyruvate, ATP, NADH, FADH2, CO2, O2 and H2O. A clean classroom handout look: white background, simple icons, clear labels, easy-to-read text. Avoid tiny text and extra decoration.
```

Edit loop, turn two, with the turn-one billboard as `image`:

```
Make it a winter evening with snowfall. Keep the billboard, its text "Fresh and clean", the shampoo bottle, the highway and the camera angle exactly as they are.
```

Character continuity, the approved character saved as `@fern-hero`:

```
Continue the children's book story with @fern-hero.
Scene: after a winter storm, the young forest hero kneels beside a fallen tree and gently helps a frightened squirrel out of a hollow.
Character consistency: same green hooded tunic, same facial features, proportions and color palette.
Style: children's book watercolor illustration, soft light, snowy forest, warm and comforting mood.
Constraints: do not redesign the character. No text, no watermarks.
```
