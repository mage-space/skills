# Krea 2 (`krea_2`)

A fast text-to-image model (opt-in) with a strong built-in aesthetic, at 1K or 2K. Good for aesthetic-led images and quick exploration of composition and style. Text only: no image inputs.

## Variants

One variant, `krea-2-turbo`: a distilled model that draws in few steps with guidance off. Leave `num_inference_steps` and `guidance_scale` at their defaults.

- `resolution`: `1k` or `2k`. Krea's own showcase images were made at 2K; use `2k` for finals.
- `aspect_ratio`: 21:9 to 9:21, default 4:5.

## How Mage sends your prompt

- `prompt` reaches the model as written.
- No `image`, no `@handle`s: characters and references are not supported, and any `@` followed by a letter is refused.
- Guidance is off, so a `negative_prompt` has no effect. State exclusions as the wanted state ("a bare white wall", "an empty beach").
- Never send `prompt_enhance`: on this model it appends random words to the prompt.

## Prompt structure

Natural language. Long, detailed prompts give the best results, though the model looks good with little prompting. Krea's examples use two shapes, and both work:

- **A comma-separated phrase list**: subject, its attributes, medium, light, palette, framing.
- **A prose paragraph**: the subject and its action first, then the setting, then style, light and depth of field.

### Expanding a short idea (Krea's approach)

Krea publishes rules for turning a short idea into a full prompt. Apply them yourself whenever the user gives you a short idea:

1. Think about the subject, the mood, and two or three style options; then choose one style, one medium, one framing and one lighting.
2. Keep every subject, action, color, count and spatial relation the user gave, and keep the user's medium (a sketch stays a sketch, a photo stays a photo).
3. Group each subject with its own attributes and actions, so details do not leak between subjects.
4. Use grounded phrasing for poses, interactions and layout ("her left hand rests on the railing", "a rock in the lower left foreground").
5. Add no objects or characters the user did not imply, and do not over-specify clothing, colors or materials the idea does not support.
6. When text is wanted, state the exact words and wrap them in quotes.
7. Write one cohesive paragraph: no bullets, no JSON, no markdown.
8. When the user's prompt is already detailed, polish it lightly; do not re-expand it.

## Vocabulary

Terms from Krea's examples:

- **Framing**: extreme close-up, close-up portrait, medium close-up shot, tightly framed medium shot, high-angle wide perspective, extreme low-angle close-up, dynamic tilted framing, low-angle portrait.
- **Optics**: macro lens, shallow depth of field, smooth creamy bokeh, distinct film grain texture.
- **Light**: bright high-key lighting, soft directional studio lighting, soft diffused natural lighting, cinematic shafts of light, harsh direct lighting, golden hour sunlight, cinematic warm lighting.
- **Style and medium**: 3D rendered designer toy, vintage analog collage, ligne claire flat-color illustration, stylized digital painting with blocky brushstrokes, 1990s cel animation, crisp cel-shaded anime, black-and-white ink with stippling and cross-hatching, 1980s airbrush, high-fashion editorial.

## References, characters, and frames

None: Krea 2 takes no images. For a person, product or design that must match a picture, use a model with references (Mango, GPT Image, Nano Banana). For consistency across a set here, repeat the same subject description word for word and fix the `seed`.

## Text in the image

Put the words to render in quotes and keep them short: a sign, a label, a title. For text-led designs, use GPT Image 2.5 Flare.

## Avoid

| Instead of | Write |
|---|---|
| A `negative_prompt` | The wanted state, in the prompt |
| Mixing several styles or media | One style, one medium |
| Props and people the user never implied | Only what the idea supports |
| Turning the user's sketch or painting into a photo | The user's medium |
| Bullets, JSON or markdown in the prompt | One paragraph, or one phrase list |
| Re-expanding an already detailed prompt | Light polish |

## Examples

A short phrase, which the model can carry on its own:

```
immense rocket launch exhaust as seen from extremely close up
```

Phrase list, 4:5:

```
3D rendered matte black designer toy figure, stylized round anthropomorphic shape, backward black baseball cap, oversized gold-rimmed aviator sunglasses, white traditional line-art tattoos of a tiger and a bird on the torso, black studded belt with a gold buckle, smooth vinyl texture, studio lighting, solid vibrant blue background, high contrast minimal composition
```

Macro prose, 3:2:

```
A tiny russet-brown harvest mouse clings to a slender diagonal branch amid vibrant green lobed leaves and small round buds. The mouse has soft textured fur, glossy black eyes, a pink nose, fine whiskers, and delicate pink paws firmly gripping the wood. In this macro photograph, an extremely shallow depth of field sharply focuses on the animal's face. The deep green background dissolves into a smooth, creamy bokeh, lit by soft, diffused natural light that brings out the fur and foliage.
```

Retro anime, 16:9:

```
1990s vintage anime style cel animation, densely packed crowd of teenagers in summer uniforms, central boy with short black hair raising a clenched right fist, squinting one eye with a determined expression, white short-sleeve shirt and solid green necktie, surrounding students looking in various directions, girls in white sailor blouses with green striped collars, light blue skirts and trousers, tightly framed medium shot, flat shading, soft muted retro palette
```

Flat illustration, an expanded short idea ("someone wading in the sea, flat illustration"), 3:2:

```
A minimalist flat-color illustration of a person wading through expansive shallow ocean waves beneath a pale peach sky. The dark-skinned figure, wearing an orange swim cap, a light blue top and bright green shorts, steps carefully through knee-deep water. The ocean is muted mint green with thin black linework tracing the continuous ripples and gentle whitecaps, and soft pinkish-peach reflections echo the sky. A dark, jagged rock rests in the lower left foreground near a pale gray shoreline; the horizon holds a solid purplish-blue landmass and a stylized layered yellow and blue cloud. The high-angle wide perspective leaves vast negative space in the water, in a clean ligne claire style with a subtle paper texture.
```
