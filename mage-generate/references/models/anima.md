# Anima (`anima`)

An anime and illustration model (opt-in) with clean lines and flat color, prompted with Danbooru-style tags, prose, or both, with prompt weighting. Not for realism: the model is deliberately weak there.

## Variants

One variant, `anima-v1`: the base model, deliberately plain and neutral until tags give it a style.

- `resolution`: `1k` (about one megapixel) or `2k`. The model works from 512 to 1536 pixels a side.
- `aspect_ratio`: 21:9 to 9:21, default 4:5.
- Leave the step and guidance settings at Mage's defaults; they are model controls, never prompt words.

## How Mage sends your prompt

**Mage adds the quality tags and a negative prompt itself.** Every Anima run gets a fixed quality prefix (`masterpiece`, `best quality`, high score tags, a recent year, `highres`, `very aesthetic`) and a long negative list (low-quality and low-score tags, `early`, `old`, `cartoon`, `painting`, `crayon`, `graphite`, `abstract`, `artist name`, `blurry`, `lowres`, `text bubble`, `speech bubble`, and anatomy fixes such as bad hands and extra digits). Neither can be switched off. So:

- Do not write quality, score, year or `highres` tags: they are already there, and repeating them only adds weight.
- Start your prompt with the rating tag, which Mage leaves to you: `safe` for general work.
- In `negative_prompt`, add only what Mage's list lacks: `chromatic aberration` and the ratings to keep out. `negative_prompt` is not in `get_model`'s field list, but it passes through. End it with a comma (`chromatic aberration, nsfw, explicit,`): Mage joins its own list on with only a space.

The rest:

- **Prompt weighting is on** (`prompt_weighting: true`): parentheses are weights. Escape every literal parenthesis as `\(` and `\)`. Danbooru tags with a qualifier need it: `artoria pendragon \(fate\)`, `fate \(series\)`, `1990s \(style\)`, `watercolor \(medium\)`. A prompt full of literal parenthesized tags and no weights can send `prompt_weighting: false` instead.
- **Weights must be strong**: `(chibi:2)`, not `(chibi:1.1)`. Use 1.5 to 2 for a visible change, on one or two tags.
- **No `@`**: any `@` followed by a letter is read as a saved handle and refused, so the `@artist` tag form cannot be used. Write the artist's name as a plain tag (the effect is weaker) and back it with style tags and a sentence describing the look.
- No image inputs, characters or references.

## Prompt structure

Tag conventions:

- Lowercase tags, with spaces instead of underscores (score tags keep theirs). Where Danbooru and Gelbooru spell a tag differently, use the Gelbooru spelling.
- You need only the tags that materially shape the image, not every relevant one.

Tag order (tags inside each group can be in any order):

```
<rating>, <count tag: 1girl, 1boy, 2girls, solo>, <character>, <series>, <artist name>, <general tags: hair, eyes, outfit, expression, pose, framing, background, light>
```

- Prose works too: at least two sentences (short prompts give unexpected results), normal capitalization for names. A hybrid opens with tags and continues in sentences.
- Thin prompts drift toward content nobody asked for; detail and an explicit rating keep it where the user wants it.

## Vocabulary

Standard Danbooru tags the model was trained on:

- **Framing**: `portrait`, `upper body`, `cowboy shot`, `full body`, `close-up`, `from above`, `from below`, `from side`, `from behind`, `dutch angle`, `wide shot`.
- **Gaze and pose**: `looking at viewer`, `looking away`, `looking back`, `sitting`, `standing`, `walking`, `arms up`, `hand on own hip`.
- **Light and time**: `backlighting`, `sunlight`, `rim lighting`, `light rays`, `sunset`, `night`, `starry sky`, `lens flare`.
- **Background**: `simple background`, `white background`, `gradient background`, `outdoors`, `indoors`, `cityscape`, `scenery`.
- **Meta and style**: `anime screenshot`, `official art`, `retro artstyle`, `sketch`, `lineart`, `flat color`.

**Era looks lean modern on Mage**: the fixed recent-year prefix and the `early, old` negatives pull against retro work. For an older look, use `retro artstyle`, `1990s \(style\)` or `anime screenshot` plus a sentence describing the era's palette and shading, and expect it to come out cleaner than a period piece.

**Non-anime looks are unreliable on Mage**: the negative list pushes away painting, crayon, graphite, abstract and cartoon looks. For painterly or western art, suggest another model.

## References, characters, and frames

- Characters are known by name (anime up to September 2025): name the character, then describe their visible appearance, every time. With two or more characters this is essential, or the model swaps their traits. Use the count tag (`2girls`, `1boy 1girl`) and give each character their own description.
- Escape the qualifier in character tags: `artoria pendragon \(fate\)`, not `artoria pendragon (fate)`.
- No image inputs. For the same character across a set, keep the same character tags, description and `seed`, and change only the scene tags.

## Text in the image

Weak by design: a single word, sometimes a short phrase; long text fails. Mage's negative list also suppresses `text bubble`, `speech bubble` and `artist name`, so comic balloons and signatures will not appear. Add lettering afterwards in an editor.

## Avoid

| Instead of | Write |
|---|---|
| `masterpiece, best quality, score_7, ...` again | Nothing: Mage adds them. Start with the rating |
| `@artist` tags (refused) | The artist name as a plain tag, plus style tags |
| `artoria pendragon (fate)` with weighting on | `artoria pendragon \(fate\)` |
| `(chibi:1.1)` | `(chibi:1.8)`: weights need to be strong here |
| A bare character name | The name plus hair, eyes and outfit |
| A one-line prose prompt | Two or more descriptive sentences, or a full tag list |
| Photorealism | Another model; Anima does not do realism |

## Examples

Tag prompt, one character, 4:5 (`negative_prompt`: `chromatic aberration, nsfw, explicit,`):

```
safe, 1girl, solo, oomuro sakurako, yuru yuri, nnn yryr, smile, open mouth, fang, one eye closed, long hair, brown hair, blunt bangs, brown eyes, santa costume, red capelet, fur trim, red gloves, santa hat, brown skirt, holding gift box, gift bag, looking at viewer, upper body, white background, simple background
```

Escaped series qualifiers, two characters, 3:2:

```
safe, 2girls, artoria pendragon \(fate\), tohsaka rin, fate/stay night, fate \(series\), artoria with blonde hair in a bun, green eyes, blue dress with silver armor, rin with long black twin tails, aqua eyes, red sweater, black skirt, standing back to back, looking at viewer, night, city lights, wind, cowboy shot
```

Prose with a named character, 2:3:

```
safe, 1girl. Digital artwork of Fern from Sousou no Frieren, with long purple hair and purple eyes, wearing a black coat over a white dress with puffy sleeves. She stands in a sunlit autumn forest, holding her staff loosely at her side and glancing back over her shoulder with a calm expression. Falling orange leaves, soft backlighting, clean lineart and flat color.
```

Weighted style, 1:1:

```
safe, 1girl, solo, (chibi:1.8), witch hat, oversized purple robe, long silver hair, holding a tiny broom, sparkles, pastel colors, simple background, full body
```

Retro look within Mage's prefix, 16:9:

```
safe, 1boy, solo, retro artstyle, 1990s \(style\), anime screenshot, spiky black hair, red jacket, motorcycle, neon city at night, rain, from side. A late-night chase shot with cel shading, film grain and a muted palette of teal and magenta.
```
