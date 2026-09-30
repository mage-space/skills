# Mode recipes

Every prompt starts with the product lock and ends with the finish. Fill the slots in `<angle brackets>` from the interview and the reference image.

**Product lock** (first line of every prompt):

> The exact product from @image1: keep its shape, proportions, colors, materials, label, logo, and all printed text identical to the reference.

**Finish** (last line of every prompt):

> Commercial product photography, sharp focus on the product, realistic reflections and contact shadows, true-to-life color, 2K.

Across a set, vary the axes listed per mode. Keep everything else, including the style line, the same.

---

## product_shot

Studio packshot for a store or catalog.

```
<Product lock>
Centered on a seamless <white / light gray / <brand color>> studio sweep,
<front / three-quarter / top-down> view, softbox key light from <left>, large
fill card, subtle ground shadow, generous margins, nothing else in frame.
<Finish>
```

Vary: angle (front, three-quarter, top-down, detail of the cap or texture), background tone, a single prop (a sprig, a stone, water drops) only if the brand fits.
Pitfalls: extra products appearing; state "a single unit".

## lifestyle_scene

The product in use in a believable place.

```
<Product lock>
In <place: a sunlit kitchen counter / a gym bench / a wooden desk by a
window>, <how it's used or placed>, with <two or three context props>.
<Time of day> light, shallow depth of field, the product in the sharp focal
plane, lived-in but tidy, <brand mood> palette.
<Finish>
```

Vary: location, time of day, props, camera height. People optional: hands or a person out of focus.
Pitfalls: the product too small; say "the product fills about a third of the frame".

## closeup_with_person

Hands or a partial face demonstrating the product. Use Guava 2 Pro.

```
<Product lock>
Close-up of <a woman's hands / a man's hand / a model's cheek and jaw>
<holding / applying / pouring / opening> the product, natural skin texture,
<nail and skin details>, soft diffused daylight, 85mm macro, background
softly blurred <setting color>.
<Finish>
```

Vary: the gesture (holding, applying, opening, pouring), skin tones, framing.
Pitfalls: warped fingers; keep one simple gesture per image.

## moodboard_pin

Vertical, aesthetic, Pinterest-native. Aspect `2:3`.

```
<Product lock>
Styled <flat lay / vignette> for a Pinterest pin, vertical composition, the
product placed <upper third / center> among <textures and props matching the
aesthetic: linen, dried flowers, ceramic, stone>, <aesthetic> mood, soft
natural light, cohesive <two or three colors> palette, editorial styling.
<Finish>
```

Vary: prop story, palette, overhead vs 45° angle.

## hero_banner

Wide header with room for copy. Aspect `21:9` or `16:9`.

```
<Product lock>
Wide hero banner: the product on the <right / left> third, <scene or
backdrop>, the other side left as clean negative space for a headline,
<brand colors> gradient light, premium campaign look.
<Finish>
```

Only put text in the image when the user supplies it; then switch to GPT Image 2.5 Flare and add: `Headline "<text>" in <font style> on the negative-space side.`
Vary: product side, backdrop, color temperature.

## social_carousel

3–10 slides with one visual system. Write the style line once:

```
Style line: <palette>, <background type>, <light>, <type style if text>.
```

Slide prompts (one per slide, same style line):

1. Cover: the product large, bold composition.
2. Detail: texture or feature close-up.
3. In use: lifestyle moment.
4. Benefit: product with a prop that shows the benefit.
5. Closer: the product with a call to action (text via GPT Image 2.5 Flare).

Slides with text use GPT Image 2.5 Flare, with each line quoted exactly. Keep one aspect ratio for all slides.

## ad_creative_pack

Coordinated static ads. Ask for the offer and the headline copy, or propose two or three short headlines and let the user choose.

```
<Product lock>
Static ad for <platform>, <aspect>. <Angle: benefit / problem–solution /
social proof / offer>. The product <placement>, <scene or backdrop>.
Headline "<exact headline>" in <bold sans-serif, color> at the <top>;
subline "<exact subline>"; a <button-style> "<CTA>" at the bottom.
Clean layout, strong contrast, brand colors <colors>.
<Finish>
```

Use GPT Image 2.5 Flare when the ad carries text, Mango 3 when it's image-only. Vary: the angle and scene per variant; keep the brand colors and type style fixed.
Pitfalls: long copy; keep headlines under six words.

## virtual_try_on

Worn by a model. Use Guava 2 Pro. Pass the garment in `image`, and a model portrait or `@character` if the user has one.

```
The garment from @image1 worn by <model archetype: a woman in her 20s with
long dark hair / a tall man in his 30s with a buzz cut>, keeping the
garment's cut, fabric, color, pattern, and details identical. <Framing>,
<pose>, <setting>, <light>, fashion editorial photograph, 85mm, natural
skin texture, fabric drape and folds realistic.
```

Vary: pose, setting, framing. Keep the same model across a set: save them with `mage-characters`.
Pitfalls: pattern changes; say "the same print at the same scale".

## conceptual_product

Surreal, sculptural, CGI-feeling.

```
<Product lock>
<Concept: levitating above a still pool with a ring of splashing water /
frozen mid-explosion of <ingredient> / balanced on stacked pastel stone
blocks / emerging from a wave of <material>>. Studio-controlled lighting,
<color palette> backdrop, high-speed photography feel, hyper-real detail.
<Finish>
```

Vary: the concept, palette, and camera angle. Tie the concept to an ingredient or benefit when possible.

## restyle

Change the mood or season of an existing product image. Pass that image in `image`.

```
Restyle @image1 as <aesthetic / season>: change the <background, props,
light, and color grade> to <description>. Keep the product exactly as it is:
same position, shape, label, and colors. <Seasonal props>.
```

Keep the source aspect ratio. Vary the aesthetic or the season per variant.
