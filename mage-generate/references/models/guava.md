# Guava (`guava`)

Mage's photorealism family: portraits, fashion, editorial and product images that pass for photographs, plus edits and composites from up to 3 images. Guava 2 Pro makes the final image and Guava 2 is the faster one for iterating. It rewards long, exact descriptions; a vague prompt gives a generic studio look.

## Variants

| `model_id` | Use it for | Prompt length it handles well |
|---|---|---|
| `guava-2-pro` | Final photoreal images, skin, fabric and hair up close, dense text | Very long: up to about 3,000 words |
| `guava-2` | Iterating on the same prompt quickly | Very long: up to about 3,000 words |
| `guava-pro-v1-5` | Matching earlier work made on it | Up to about 700 words |
| `guava-pro` | Matching earlier work made on it | Up to about 700 words |
| `guava` | Matching earlier work made on it (the default when `model_id` is left out) | Up to about 700 words |

- Set `model_id` every time: the default is the oldest variant, `guava`. Start on `guava-2`, finish on `guava-2-pro`.
- The Pro variants render text, realistic texture and the details you asked for more faithfully; the others trade a little of that for speed.
- `resolution` 1K or 2K. `aspect_ratio` 21:9, 16:9, 3:2, 5:4, 1:1, 4:5 (default), 2:3, 9:16, 9:21.

## How Mage sends your prompt

- `prompt` goes to Guava as written, after your images. `image` and `additional_images` hold up to 3 images, shared with mentioned characters and references.
- Mentions are rewritten to the positions Guava reads: `@mara` becomes `character from image 2`, a saved reference `@linencoat` becomes `outfit from image 3` (or `pose`, `location`, `object`), and `@image1` becomes `image 1`. Numbering: your own images first, then characters, then references, in the order first mentioned.
- Guava addresses inputs as `image 1`, `image 2`, `image 3`: refer to them that way in edit instructions, as Mage's rewrite does. With one input, naming the subject by its looks works as well.
- **The output frame is `aspect_ratio` at 1K or 2K, also for edits.** When editing a photo, set `aspect_ratio` to the closest match to the input, or the edit gets reframed.
- `negative_prompt` (up to 500 characters) is not listed by `get_model`, but it passes through and Guava uses it.
- `prompt_extend` (off by default) has Guava rewrite your prompt with its own model. Leave it off when you wrote the prompt. For a one-line idea on `guava-2` or `guava-2-pro` without input images, `prompt_extend: true` with `prompt_extend_mode: "agent"` gives the most careful rewrite.

## Prompt structure

Write one natural paragraph, not a list. The working formula: **subject, described + scene, described + style + camera + mood + detail**. Always name the overall style first or last: "realistic photography", "editorial fashion photograph", "candid smartphone snapshot", "studio product photograph".

**Portrait** (about 200 words), in this order, adapted when a natural order reads better:

1. **Identity**: ethnicity, gender and a specific age ("a 27-year-old", "in her early 40s"). Never just "young" or "old".
2. **Face**: shape (oval, square, heart-shaped), structure (high cheekbones, a strong jawline), eyes (almond-shaped, deep-set; hazel, deep brown), nose, mouth, and a precise expression ("a faint, knowing smile").
3. **Skin and grooming**: tone (porcelain, olive, tan, deep brown) and texture (visible pores, light freckles, fine laugh lines); makeup item by item (brows, eyeliner, lashes, lipstick, blush, highlight) or "no makeup"; facial hair and its grooming.
4. **Clothes, hair, accessories**: every garment with its fabric (ribbed wool turtleneck, washed denim, silk blouse); hair colour, length, texture and cut; jewellery, glasses, headwear.
5. **Pose**: posture, gaze direction, head tilt, and what each hand is doing. Keep it anatomically plausible.
6. **Setting and light**: the place, background objects, the light's direction, hardness and colour temperature, the weather and time.
7. **Camera**: lens, aperture, framing, depth of field.

**Product or general image**: the subject's type, count, material and state; foreground, middle ground and background; light and colour; surface textures; setting, time, weather; how the objects relate in space.

**Layouts** (posters, slides, menus, comics): the one place line breaks help. Describe region by region ("TOP SECTION: ... MIDDLE SECTION: ... BOTTOM SECTION: ...", "Left third: ...", "Row 1 ... Row 2 ...", "a 2x3 grid with white gutters") and give every region its exact content.

## Vocabulary

- **Camera**: "shot on a full-frame camera with a 50mm lens at f/4, 1/160s, ISO 200"; "85mm portrait lens, shallow depth of field, soft bokeh"; "wide-angle smartphone photograph"; "close, eye-level composition, slightly off-center"; "100mm macro".
- **Shot size and angle**: close-up, chest-up close shot, medium shot, full-body, long shot; eye level, high angle, low angle, top-down, aerial.
- **Lens character**: macro, ultra-wide, telephoto compression, fisheye ("enlarged at the center, curving toward the edges").
- **Light**: "soft window light from the front-left at 45 degrees", "strong backlight with a rim of light outlining her hair", "overcast diffused daylight", "warm tungsten interior against cool blue dusk outside the window", "late-afternoon sun raking across the wall", "light beams through dust".
- **Material and colour**: name the surface ("waxy, velvety and leathery leaves", "brushed aluminium with chamfered edges", "matte skin with a light dusting of freckles") and grade colours finely ("five greens from olive to jade").
- **Finish**: "warm film-like tones with fine grain, soft contrast", "crisp, even fashion lighting", "documentary realism".

## References, characters, and frames

- **Say which image changes and what stays**: "Change the background to a rain-wet street at night, keeping the woman in image 1, her pose and her clothes unchanged."
- **Keep a person**: "Perfectly preserve the facial features and long black hair of the woman in image 1." Keep ethnicity, age, hair, expression and outfit unless the user asked to change them, and keep makeup or expression changes subtle.
- **Composites**: give each image its role in one sentence: "The woman in image 1 wears the necklace from image 2 and carries the bag from image 3 on her left shoulder."
- **Add or replace**: name the category, colour, size, orientation and place: "Replace the paper cup in her right hand with a matte black ceramic mug, handle facing the camera." Pick a sensible spot when the user did not say.
- **Style change**: name concrete visual features (brush texture, palette, line weight), not only a style name.
- **Other edits that work**: a pose from a sketch ("Generate an image that matches the pose outlined in image 1 and follows this description: ..."), a new viewpoint ("Show a rear view."), restoration ("Restore the old photo: remove scratches, reduce noise, sharpen details, natural skin tone, clear facial features, no distortion."), a contact sheet ("a nine-panel grid of the same woman in nine different photo poses").
- **Saved characters**: `@mara` works anywhere a name would: "@mara sits on the windowsill, perfectly preserving her facial features and hairstyle." Mention her once per prompt where the description starts; afterwards say "she".

## Text in the image

- Put every string in double quotes, letter for letter, in its own language and capitalisation, and say where it sits, its font style, colour, size and carrier (printed, neon, embroidered, chalk, engraved), with line breaks and reading direction (vertical calligraphy reads right to left).
- When the scene implies text (a menu, a chart, an app screen, a newspaper), write the actual words rather than "a list" or "some labels".
- Never change names, brands, slogans, URLs, phone numbers or figures.
- Guava places text in empty areas and follows surface perspective (glass, fabric, signs). `guava-2-pro` holds small, dense text and many languages; on the older variants keep text short.
- When the image should carry no text, end the prompt with "The image contains no recognizable text."

## Avoid

| Problem | Write instead |
|---|---|
| Generic studio look | Name the light source and direction, the lens and the place |
| Waxy, airbrushed skin | Pores, freckles, fine lines, flyaway hairs; drop "flawless" and "perfect skin" |
| Same face for every "young woman" | Ethnicity, a specific age, face shape and eye detail |
| Edits reframed or stretched | `aspect_ratio` matching the input image |
| Bullet lists or headings in the prompt | One paragraph (layouts excepted) |
| Contradictions ("overcast, hard noon shadows") | One consistent light story |

A default `negative_prompt` for photoreal work: `low resolution, low quality, distorted limbs, malformed fingers, oversaturated colors, wax-figure appearance, lack of facial detail, excessive smoothness, AI-looking artifacts, chaotic composition, blurry or warped text`.

## Examples

**Photoreal portrait** (`guava-2-pro`, 4:5, 2K):

```
Realistic street portrait photograph on a warm afternoon. A 28-year-old Southern Italian woman with an oval face, high cheekbones, deep brown almond-shaped eyes and olive skin with visible pores and a few freckles across her nose stands center-right, looking back over her shoulder at the camera with a warm, slightly amused smile. Her long, thick, wavy black hair is lit at the edges by strong backlight from the end of the street. She wears a black spaghetti-strap backless dress and holds a large bouquet of orange, apricot and peach roses against her chest with both hands. Deep green vines with small orange flowers hang from the eaves above her; behind her a newsstand with black metal-framed glass blurs into shallow depth of field. Shot on an 85mm lens at f/2, eye level. Warm film-like tones with fine grain, soft contrast and a bright edge glow. The image contains no recognizable text.
```

**Product shot** (`guava-2-pro`, 1:1):

```
Studio product photograph of a champagne-gold over-ear headphone resting on a slab of dark slate. A 100mm macro view of the hinge where the telescopic arm meets the ear cup shows the brushed aluminium grain and precise chamfered edges; a sharp backlight sets a small starburst highlight on the metal rim. The ear cushion's protein leather shows fine creases. Dark, softly graded background, crisp detail, no noise. The image contains no recognizable text.
```

**Editing a saved character** (`guava-2`, `aspect_ratio` matched to the input):

```
@mara sits at a window table in a minimalist coffee shop, perfectly preserving her facial features, skin tone and shoulder-length auburn hair. Change her outfit to a camel wool blazer over a cream silk blouse. Soft overcast daylight from the window on the left, a white ceramic cup in her right hand, shallow depth of field, candid editorial photograph.
```

**Composite from three images**:

```
The man in image 1 stands on the rooftop from image 2 at dusk, wearing the leather jacket from image 3 zipped halfway. Keep his face, hairstyle and build exactly as in image 1. Match the jacket's light to the rooftop's cool blue dusk with warm string lights behind him; full-body shot at eye level, 35mm lens, realistic photography.
```

**A photo with a sign in it** (`guava-2-pro`, 3:2):

```
Realistic photograph of a narrow Lisbon side street after rain. Above a small bakery hangs a hand-painted wooden sign reading "PADARIA SOL" in cream serif capitals on a faded blue board, and a chalkboard by the door says "Pastéis de nata 1,20 €" in white handwriting. Wet cobblestones reflect the warm shop window; a woman in a yellow raincoat walks past, slightly blurred. 35mm lens, eye level, soft overcast light.
```
