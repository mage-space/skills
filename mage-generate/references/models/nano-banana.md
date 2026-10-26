# Nano Banana (`nano_banana_v2`)

Google's image models on Mage (opt-in), for graphics with readable text and edits from up to 14 reference images, up to 4K. Strong at multi-image composites, keeping named characters consistent, and text-described edits. Google's safety filter applies.

## Variants

| `model_id` | Use it for | Resolutions |
|---|---|---|
| `nano-banana-v2.1` | The default: better quality, text, prompt adherence and character consistency, at a lower price | 1K, 2K, 4K |
| `nano-banana-v2` | 512 px drafts, or matching earlier work | 512, 1K, 2K, 4K |

Settings that change the result:

- `thinking_level`: `minimal` (default) or `high`. Same price, slower. The model plans the composition before drawing; use `high` for multi-step scenes, infographics, dense text and many references.
- `web_search` grounds the image in current facts (a recent event, today's weather, a real product); `image_search` looks up what a real place or object looks like. Each adds to the price. Image search does not return photos of people. Say what to look up in the prompt: "First search for reference images of the building, then draw it."
- `aspect_ratio`: 1:1 (default), 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9, and banner strips 4:1 and 8:1.
- Google's numbers for one image: faces stay recognizable for up to about 4 characters, objects keep their detail for up to about 10. Beyond that, build the scene in steps.

## How Mage sends your prompt

- One call, one turn: the images first (in Mage's order), then your prompt. There is no conversation memory between calls: "iterating" is a new call with the previous result as `image`, and the prompt must restate what to keep.
- Mage's image order: your `image`, then `additional_images`, then each `@handle` character, then each `@handle` reference. Mage rewrites the prompt to match: `@image1` becomes "image 1"; with one image of your own, a character `@ana` becomes "character from image 2" and a saved location `@loft` "location from image 3". All share the 14-image budget.
- `aspect_ratio` is sent on every call, edits included, and defaults to 1:1: for an edit, set the source's ratio or the result comes back square.
- The prompt reaches the model as written. No negative prompt, no mask upload.
- Any `@` followed by a letter is read as a saved handle and refused when none matches: no `@` in on-image text.

## Prompt structure

Write full narrative sentences, not keyword lists, and be specific. Open with a verb that names the operation (Create, Transform, Remove, Combine, Change) and say what the image is for ("a logo for a high-end, minimalist skincare brand" beats "a logo").

| Job | Formula |
|---|---|
| New image | [Subject] + [Action] + [Location or context] + [Composition] + [Style] |
| Photoreal | A photorealistic [shot type] of [subject] in [setting]. [Light]. Shot from [angle] with a [lens]. |
| With references | [Each image and its role] + [How they relate] + [The new scenario] |
| With search | [What to look up] + [What to work out from it] + [How to show it] |
| Edit | Using the provided image, change only [element] to [new element]. Keep everything else exactly the same, preserving the original style, lighting, and composition. |

- Complex scenes go step by step: "First, create a background of... Then, in the foreground, add... Finally, place..."
- Name the format in words as well as in `aspect_ratio`: "vertical social post", "widescreen backdrop", "square sticker".
- For options, run separate calls. Ask for "three variations side by side" only when one comparison sheet is the deliverable.

## Vocabulary

- **Framing**: wide-angle shot, macro shot, low-angle perspective, aerial view, 45-degree elevated shot, extreme close-up, medium-full shot, center-framed, top-down flat lay, perfectly isometric.
- **Lens and focus**: "low-angle shot with a shallow depth of field (f/1.8)", "50mm f/1.8 prime lens", wide-angle for scale, macro for detail.
- **Camera as a look**: action-cam (immersive, distorted), cheap disposable camera (raw, nostalgic flash), medium-format analog film, "as if on 1980s color film, slightly grainy".
- **Light**: three-point softbox setup, chiaroscuro with harsh high contrast, golden-hour backlighting with long shadows, soft diffused light from a named direction.
- **Color**: "cinematic color grading with muted teal tones", pronounced grain, high saturation.
- **Materials by name**: "navy blue tweed", "ornate elven plate armor etched with silver leaf patterns", "minimalist ceramic mug in matte black".
- **Graphic styles**: kawaii sticker with bold clean outlines, cel-shading, isometric infographic, risograph, halftone, Swiss or brutalist graphic design, chalk or ink sketch.

## References, characters, and frames

- **Name every character and object** and describe them once, then reuse the same name in every scene so the model can track them ("Maya, a woman with a short silver bob and a mustard raincoat"). With a saved `@handle`, add the visible traits after it.
- **Combine**: "Create a new image by combining the elements from the provided images. Take the blue armchair from image 1 and place it in the sunlit living room from image 2, matching its light and perspective."
- **Protect critical details** by describing them and saying they stay "completely unchanged": "Ensure the woman's face and features remain completely unchanged. The logo should look naturally printed on the fabric, following the folds of the shirt."
- **Text-described inpainting** (Google's playbook): there is no mask, so name the region in words, "change only the blue sofa", and list what stays: "Keep the pillows, the rug and the lighting unchanged."
- **Character turnaround** (Google's playbook): one angle per call. Start from the best front view; for each new angle, pass the front view plus the angles made so far, and ask for a single view: "A studio portrait of this man against a plain white background, in profile looking right. Same face, hair and clothing." Add a pose reference image for a complex pose. Save the cleanest front view with `create_character` for later shots.
- **Edit loop**: generate, then small follow-ups, one change each, with the previous result as `image`: "Keep everything the same, but make her expression more serious."
- **Sketch to render**: "Turn this rough pencil sketch of a sports car into a polished studio photo. Keep the body shape and wheel design, add chrome trim and a candy-red finish."
- **Keyframes for video**: make the start and end stills here, then animate them with Lemon (first and last frame).

## Text in the image

- **Write the text first, then render** (Google's playbook): settle the exact copy before the image call, written by you or agreed with the user, then put it in the prompt verbatim in quotes. Never let the model invent copy for a final.
- Give each line its own text and style: `The headline "SUMMER RUN" in heavy blocky condensed capitals; below it "Saturday 7 June, 8 am" in a light sans-serif.` Font names work as look cues ("Century Gothic", "Impact").
- Stop stray copy: "No other text", "no placeholder text, all text in English".
- Localize by writing the prompt in English, naming the target language and region, and quoting the exact translated copy. Best-supported: Arabic (Egypt), German, Spanish (Mexico), French, Hindi, Indonesian, Italian, Japanese, Korean, Portuguese (Brazil), Russian, Ukrainian, Vietnamese, Chinese.
- Dense text, menus, infographics: `thinking_level: "high"` and 2K.

## Avoid

| Instead of | Write |
|---|---|
| Comma-separated keywords | Sentences describing the scene |
| "no cars", "no people" | "an empty, deserted street"; short "No text" lines are fine |
| An edit with the default `aspect_ratio` | The source image's ratio |
| "Now make it warmer" with no image attached | The previous result as `image`, plus what stays the same |
| Six people with exact faces in one image | Up to about four, or build the group in steps |
| Asking for copy you have not written | The final words, quoted, line by line |

## Examples

Photoreal scene, 16:9:

```
A photorealistic wide-angle shot of a vibrant coral reef teeming with tropical fish. Crystal-clear turquoise water with sunbeams filtering down from the surface, lighting a sea turtle gliding over the coral. Shot from a low perspective with a wide-angle lens. Widescreen, 16:9.
```

Product shot, 1:1:

```
A high-resolution, studio-lit product photograph of a minimalist ceramic coffee mug in matte black on a polished concrete surface. Three-point softbox lighting with soft, diffused highlights and no harsh shadows. Slightly elevated 45-degree angle to show its clean lines. Ultra-realistic, sharp focus on the steam rising from the coffee. Square image.
```

Text-described edit, the living-room photo as `image`, its own aspect ratio:

```
Using the provided image of a living room, change only the blue sofa to a vintage brown leather chesterfield sofa. Keep the rest of the room, including the pillows on the sofa and the lighting, unchanged.
```

Magazine cover with exact copy, 3:4, `thinking_level: "high"`:

```
A photo of a glossy magazine cover. The minimal blue cover has the large bold words "NORTHBOUND" in a serif font that fills the width. No other text except the issue number "No. 12" and the date "Feb 2026" in the top corner, and a small barcode. In front of the title, a portrait of a woman in a sleek, minimal dress, playfully holding up a paper map. The magazine sits on a shelf against an orange plastered wall in a designer store.
```

References with roles, a napkin sketch as `@image1` and a fabric swatch as `@image2`:

```
Using the napkin sketch in @image1 as the structure and the fabric in @image2 as the texture, transform this into a high-fidelity 3D render of an armchair. Place it in a sun-drenched, minimalist living room.
```
