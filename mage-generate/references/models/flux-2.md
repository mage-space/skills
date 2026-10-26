# Flux 2 (`flux2`)

Flux 2 Dev, an open-weights image model on Mage (opt-in) for long, detailed prompts, generation, and edits from up to three reference images. It reads structured JSON prompts as well as prose, and takes exact hex colors.

## Variants

One variant, `flux2-dev`. `resolution` `1k` (about one megapixel) or `2k` (about two); `aspect_ratio` 21:9 to 9:21, default 4:5. Leave the step and guidance settings at Mage's defaults.

## How Mage sends your prompt

- `prompt` reaches the model as written, prose or JSON text alike. There is no negative prompt.
- Characters and references are not supported: `@handle`s are refused on this model. Pass images directly in `image` and `additional_images`, three in all. They are image 1, 2 and 3 in the order sent; name them that way in the prompt.
- With one input image, the output takes that image's shape and `aspect_ratio` is ignored. With two or three, the output uses `aspect_ratio` and `resolution`.
- `seed` is a field: keep it fixed while you change one part of a prompt, so the change is the only difference.
- Never send `prompt_enhance`: on this model it appends random words to the prompt.

## Prompt structure

Subject + Action + Style + Context (setting, light, time, mood). The model weighs early words most, so order by priority: main subject, key action, critical style, essential context, secondary details.

- 30 to 80 words is usually right; 10 to 30 for quick concept and style exploration; 80 or more for complex scenes.
- Prose and JSON work equally well. Use prose for quick, simple scenes; use JSON for production work, several subjects, and changing one element at a time. Paste the JSON as the prompt.
- English is the most precise; a native-language prompt can render a local culture more authentically.

### Build the prompt field by field

1. Start with one subject in a JSON scene: `scene`, `subjects` (each with `description`, `position`, `action`, optional `pose` and `color_palette`), `style`, `color_palette`, `lighting`, `mood`, `background`, `composition`, `camera` (`angle`, `distance`, `lens-mm`, `f-number`, `focus`).
2. Generate and look.
3. Change one field per run, with the same `seed`: add a second entry to `subjects`, change `lighting`, swap the `background`. Leave every other field byte-for-byte identical.
4. When it is right, keep the JSON as the source of truth for the series.

### Brand colors with hex

- Attach each hex code to a specific object: "The car is #FF0000", "walls in hex #C4725A". "Use #FF0000 somewhere" is applied inconsistently.
- For a product, break it into parts, give each part a `description` with its exact hex and `"color_match": "exact"`, and list the brand palette in `color_palette`.
- Hex works for type too: "The logo text 'ACME' in color #FF5733."

## Vocabulary

- **Photo eras**: "shot on Sony A7IV, clean sharp, high dynamic range" (modern); "early digital camera, slight noise, flash photography, candid, 2000s digicam style"; "film grain, warm color cast, soft focus, 80s vintage photo"; "shot on Kodak Portra 400, natural grain, organic colors".
- **Camera and lens**: name body, lens and aperture: "Shot on Hasselblad X2D, 80mm lens, f/2.8, natural lighting". f/1.4 to f/2.8 for shallow depth of field, f/8 to f/16 for deep; 24mm wide, 35mm documentary, 50mm neutral, 85mm portrait, 135mm and up for compression; ISO 1600 to 3200 for a grainy film look; macro; anamorphic for oval bokeh. Specific gear beats "professional photo".
- **Light**: golden hour, blue hour, overcast, Rembrandt, split, chiaroscuro, backlit or rim, softbox key, practical lights, diffused, harsh direct; say source, direction and softness.
- **Styles**: anamorphic flare, teal-and-orange grade, film noir; oil, watercolor, impasto, Art Nouveau, Bauhaus; concept art, matte painting, stylized 3D; flat vector, comic, anime, graphic novel; VHS, polaroid, sepia.
- **Composition**: rule of thirds, leading lines, foreground and background layers, worm's-eye, bird's-eye, dutch angle, symmetry, negative space.

## References, characters, and frames

- Give each input one job and say how they combine: "the woman from image 1, wearing the jacket from image 2, in the painterly style of image 3, in a rainy city street at dusk".
- Multi-reference jobs it handles: combining garments into one outfit, placing furniture into a room, product composites, keeping a character.
- **A character across separate images** (the comic playbook): write one detailed character description and repeat it word for word in every prompt, with the same labeled fields per panel (Style, Character, Setting, Text, Mood). Add the approved first image as image 1 for the later panels.
- For an edit of one photo, say the change and what stays, as with any instruction-following model.

## Text in the image

- Put the exact words in quotation marks, front-load the text description, and keep strings short.
- Say placement ("below the title, centered"), style ("elegant serif", "bold industrial lettering", "handwritten script"), size ("large headline", "small body copy") and color, by hex when it matters.
- Ads, magazine covers and infographics are strengths. For an infographic, give title, subtitle, each section's heading, content and visual, and a hex color scheme.

## Avoid

| Instead of | Write |
|---|---|
| "no blur", "no people", "no text" | "sharp focus throughout", "an empty street", a plain background |
| The subject buried after style and mood | The subject first |
| "professional photo", "high quality" | The camera, lens, aperture and light |
| A hex code with no object | The hex on the object it colors |
| More than three images | The three that matter, one role each |
| `@handle` mentions | The image itself in `image` or `additional_images` |
| Rewriting the whole JSON between runs | One field changed, same `seed` |

## Examples

Prose, direct-flash editorial, 4:5:

```
Dog wrapped in a white towel after a bath, photographed with direct flash and high exposure, wet fur sharply detailed, editorial raw portrait, harsh flash lighting, intimate humorous documentary style
```

Brand colors on objects, 3:2:

```
A modern living room with warm terracotta walls in hex #C4725A, a large L-shaped sectional sofa in deep teal hex #1B6B6F, and amber hex #E8A847 accent pillows, throw blanket and a velvet ottoman. Light oak floors, a round marble coffee table with dried pampas grass in a glass vase, floor-to-ceiling windows with sheer white curtains letting in soft afternoon light, two potted fiddle leaf figs, and an abstract painting on the main wall in all three accent colors. Clean minimal composition, natural daylight casting soft shadows.
```

JSON, the first step of a product series, 1:1:

```json
{
  "scene": "Professional studio product photography on a polished concrete surface",
  "subjects": [
    {
      "description": "Minimalist ceramic coffee mug with steam rising from hot coffee",
      "position": "Center foreground",
      "color_palette": ["matte black ceramic"]
    }
  ],
  "style": "Ultra-realistic commercial product photography",
  "color_palette": ["matte black", "concrete gray", "soft white highlights"],
  "lighting": "Three-point softbox setup, soft diffused highlights, no harsh shadows",
  "mood": "Clean, professional, minimalist",
  "background": "Polished concrete surface with a seamless studio backdrop",
  "composition": "rule of thirds",
  "camera": {
    "angle": "high angle",
    "distance": "medium shot",
    "lens-mm": 85,
    "f-number": "f/5.6",
    "focus": "Sharp on the steam and the mug"
  }
}
```

Poster with text, 2:3:

```
Groovy retro poster with the quote "If you love me let me sleep". Bold 70s typography in deep red and warm pink tones, cream background, a bold orange doodle around the text, funky layout with a playful drop shadow. Style: bold vintage aesthetic, dopamine decor.
```

Macro with text and a hex gradient, 4:5:

```
Realistic macro photograph of a hermit crab using a soda can as its shell, partly emerging from the can, sharp detail and natural colors, on a sunlit beach with soft shadows and a shallow depth of field, blurred ocean waves behind. The can reads "TIDE POP" and has a color gradient from #FF5733 at the top to #33FF57 at the bottom.
```

Multi-reference outfit, a person photo as `image` and two garments in `additional_images`, 2:3:

```
The woman from image 1 wearing the cropped denim jacket from image 2 over the white slip dress from image 3, standing on a sunlit Lisbon street. Full body, eye level, 50mm lens, soft afternoon light, natural skin texture, editorial street-style photograph.
```
