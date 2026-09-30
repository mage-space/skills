# Styles and prompts

## Style menu

Each style has a STYLE descriptor. Repeat it word for word in the style key and every clip.

| Style | STYLE descriptor | Good for |
|---|---|---|
| Stickman cartoon | Simple black stick figures with round heads and expressive poses on a flat off-white background, thick marker lines, a few flat accent colors, hand-drawn comic timing | History, stories, humor |
| Paper diorama | Layered cut-paper diorama, visible paper edges and fibers, soft shadows between layers, handcrafted miniature set, warm tabletop lighting | History, nature, travel |
| Pastel flat 2D | Flat 2D vector illustration in soft pastel colors, rounded shapes, no outlines, gentle gradients, minimal clean composition | Explainers, self-improvement, tech |
| Hand-drawn ink | Loose black ink and wash on cream paper, visible pen strokes, sparse watercolor accents, sketchbook feel | Philosophy, biographies, essays |
| Claymation | Stop-motion clay figures and sets, fingerprints in the clay, slightly jerky stop-motion movement, soft studio light | Kids, stories, science |
| Whiteboard | Black marker drawings appearing on a clean whiteboard, simple icons and arrows, a few red and blue highlights | Business, how-to, education |
| Watercolor | Soft watercolor painting, bleeding edges, paper texture, muted natural palette, dreamy atmosphere | Stories, poetry, nature |
| Pixel art | 16-bit pixel art, limited palette, crisp pixels, retro game scenes | Gaming, internet history, tech |
| Low-poly 3D | Low-poly 3D scenes with flat-shaded facets, bright simple palette, clean isometric camera | Science, space, geography |
| Vintage newsreel | Black-and-white illustrated newsreel look, film grain, vignette, archival poster graphics (drawn, not photographs) | History, wars, inventions |

Every descriptor ends with the realism ban: **"non-photorealistic, illustrated, no live action, no realistic human faces."**

## Style key recipe (Mango 3)

```
<STYLE descriptor>. A representative scene from the video: <the most iconic
moment of the topic>. <Aspect> composition with clear focal point and space
around it. Non-photorealistic, illustrated, no live action, no realistic human
faces. No text, no captions, no watermark.
```

With style images from the user, pass them in `image` / `additional_images` and add: "Match the rendering style, palette, and texture of @image1; do not copy its subjects."

## Clip prompt template (Cherry 2 Pro)

```
STYLE: Match the visual style of @image1 exactly: <STYLE descriptor>.
SCENE: <one scene that shows this block's line: subject, action, setting>.
MOTION: <camera move: slow push in / gentle pan / static> and <what animates:
figures walk, paper layers slide, ink draws itself>.
NARRATION: An off-screen narrator <voice description or @voice-handle> says:
"<exact narration line for this block>"
SOUND: <ambience or soft music bed>, no other voices, no dialogue on screen.
Non-photorealistic, illustrated, no live action, no realistic human faces, no
captions, no text, no watermark.
```

Rules:
- One scene and one main action per block.
- The narration is spoken over the scene; characters on screen don't lip-sync.
- Mention the style key as `@image1` in every block, and the saved narrator voice by the same `@handle` in every block.
- Keep narration lines inside the block's length (about 2.5 words a second).

## Narrator voice sample (Seed Audio, 10 s)

```
<Voice: a calm, warm male narrator in his 40s with a neutral American
accent, documentary pacing>, says: "Some stories are bigger than the people
who lived them. This is one of them."
```

Save the result with `create_reference` (`kind: "audio"`, a name like "Narrator") and use its handle in every clip.

## Structure that works

- **Hook (block 1):** a surprising claim, a question, or the end of the story first.
- **Build (middle blocks):** one fact or event per block, in order, each raising the next question.
- **Payoff (last block):** the answer, the twist, or the takeaway, then a short sign-off.
