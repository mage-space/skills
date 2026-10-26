# Z-Image (`z_image`)

The fastest and cheapest image model on Mage (opt-in): photoreal text-to-image with solid anatomy and lettering, at 1K or 2K. It renders English and Chinese text well and follows dense, concrete descriptions.

## Variants

One variant, `z-image-turbo` (shown as Z-Image).

- `resolution` 1k (default) or 2k. `aspect_ratio` 21:9, 16:9, 3:2, 5:4, 1:1, 4:5 (default), 2:3, 9:16, 9:21.
- Text only: no input image, characters or references.
- Leave `num_inference_steps` and `guidance_scale` at their defaults: this fast variant is built for them.
- Seeds vary the result less than on most models. For real variety, change the prompt (pose, angle, light, setting), not just the seed.

## How Mage sends your prompt

- `prompt` reaches the model as written.
- **The negative prompt does nothing on Z-Image.** It runs without guidance, where a negative prompt is never used. Do not send one; steer by describing what you want instead ("an empty street" rather than a negative "people").
- The prompt is read up to roughly 350 words; anything past that is cut. Put the important things first.

## Prompt structure

Work through the request in this order, then write the result as plain description:

1. **Lock the core**: subject, count, action, state, and any named colours, text or characters the user gave. These never change.
2. **Work out anything the request asks the image to figure out.** When the user asks for a design, an explanation or a solution ("an infographic of how a heat pump works", "a menu for a ramen bar"), decide the concrete content first, then describe it as something visible.
3. **Add professional detail**: composition, lighting and atmosphere, material textures, colour scheme, and layered space (foreground, middle ground, background).
4. **Write every piece of text exactly** (see **Text in the image**).

Rules for the final prompt:

- Objective and concrete. No metaphors, no emotional rhetoric ("a dreamlike symphony of light"), no meta tags such as "8K", "masterpiece" or "best quality".
- Dense details in short clauses work well: "Red hanfu, intricate embroidery. High bun, phoenix headdress, red flowers, beads."
- English or Chinese both work.

## Vocabulary

- **Framing**: "full-body portrait, centered composition, slightly tilted stance, direct eye contact with the camera", "medium shot from waist up", "overhead flat lay".
- **Light**: "daylight evenly illuminates the scene", "soft-lit outdoor night background", "natural light, soft shadows", "neon glow from above".
- **Focus**: "medium depth of field, face and upper body in sharp focus", "blurred colourful lights in the distance".
- **Finish**: "high detail, sharp focus", "casual fashion photography", "street-art aesthetic with halftone patterns".

## References, characters, and frames

None: Z-Image takes no images. For a person, product or design that must match a picture, use a model with references (Mango, GPT Image).

## Text in the image

- Put every string the image should show inside English double quotes, word for word: `a chalkboard reads "Soup of the Day: Miso"`.
- Posters, menus and app screens: describe all the text, its font and its layout. Signs, road signs and screens: give the text, its position, size and material.
- Any text you invent while planning (chart labels, steps) follows the same rule.
- With no text needed, spend the words on visual detail.

## Avoid

| Problem | Write instead |
|---|---|
| A negative prompt to remove something | A positive description of what is there instead |
| "8K, masterpiece, ultra-detailed" padding | Concrete details: materials, light, layout |
| Poetic mood sentences | What is visibly in the frame |
| Vague text ("a sign with a slogan") | The exact quoted words, their place and lettering |
| Raising guidance to force the prompt | Default settings and a more specific prompt |

## Examples

**Fashion portrait with text in the scene** (4:5):

```
Photo of a stylish young woman with short black hair standing confidently in front of a bright cartoon mural. She wears an all-black outfit: a puffed bomber jacket with a ruffled collar, cargo shorts, fishnet tights and chunky black boots, with a gold chain at her waist. The mural has four comic panels: one reads "GRAND STAGE" with sneakers and a soda bottle, one shows green sneakers and a slice of pizza, one reads "HARAJUKU st" with floating shoes, and one shows a blue mouse on a skateboard with the text "Takeshita WELCOME". Bright yellow, teal, orange, pink and green; speech bubbles and halftone patterns. Daylight evenly lights the scene; white tiled pavement underfoot. Full-body portrait, centered composition, slightly tilted stance, direct eye contact with the camera. High detail, sharp focus.
```

**Dense detail in short clauses** (2:3):

```
Young woman in red hanfu, intricate gold embroidery. Neat makeup, red floral forehead mark. Elaborate high bun, gold phoenix headdress, red flowers, beads. Holds a round folding fan painted with a lady, trees and a bird. A small neon lightning-bolt lamp glows bright yellow above her extended left palm. Soft-lit outdoor night background, silhouetted tiered pagoda, blurred colourful lights in the distance.
```

**A worked-out design** (4:5):

```
A printed menu card for a small ramen bar, cream paper with a thin black border. At the top, the title "KUMO RAMEN" in bold black brush lettering. Below, three items in a clean serif font, each with a price aligned right: "Shoyu Ramen 14", "Miso Ramen 15", "Spicy Tantanmen 16". At the bottom, small grey text: "Open 5pm – late". A single ink illustration of a steaming bowl sits beside the title. The card lies on a dark walnut counter, soft overhead light, top-down view.
```
