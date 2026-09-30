# Card recipes

Start every prompt with the product lock:

> The exact product from @image1: identical shape, proportions, colors, materials, label, logo, and printed text.

Quote every word of on-image text exactly, and keep each line short. Text cards use GPT Image 2.5 Flare.

**Style line for text cards** (write once per set, repeat verbatim):

> Clean marketplace infographic style: <background: soft white / light <brand color>>, <accent color> icons and dividers, bold modern sans-serif headlines, high contrast, generous spacing.

---

## main_image (Mango 3, 1:1)

```
<Product lock>
A single unit centered on a pure white background (RGB 255,255,255), the whole
product in frame and filling about 85% of it, front three-quarter view, soft
even studio lighting, a faint natural contact shadow, crisp focus. No props,
no text, no other objects.
```

## infographic (Flare, 1:1)

```
<Product lock>
<Style line>. The product large at the <center / left>, with <3–5> callouts
connected by thin lines to the relevant parts:
"<Callout 1>", "<Callout 2>", "<Callout 3>". Title at the top: "<Title>".
```

## multi_angle (Mango 3, 1:1)

```
<Product lock>
Three views of the same product side by side on a white background: front,
side, and back, equal size and spacing, soft studio light, consistent shadows.
```

If the back isn't visible in the reference, show front, three-quarter, and top instead, and say so.

## detail_shot (Mango 3, 1:1)

```
<Product lock>
Macro close-up of <the texture / the cap / the stitching / the label detail>,
shallow depth of field, soft raking light revealing material quality.
```

## lifestyle (Mango 3, 1:1)

```
<Product lock>
The product in use <in the setting where it's used>, <how it's used>, natural
light, believable home or outdoor context, the product clearly visible and in
focus.
```

## whats_in_box (Mango 3, 1:1)

```
<Product lock>
Knolling flat lay on a white surface of everything included: <item list from
the user>, neatly arranged at right angles with equal spacing, overhead view.
```

Only include what the user says is in the box.

## aplus_hero_banner (Flare, 21:9)

```
<Product lock>
<Style line>. Wide brand banner: the product on the right third in <scene or
backdrop>, brand name "<Brand>" and the line "<Brand line>" on the left.
```

## aplus_pain_points (Flare, 16:9)

```
<Style line>. Two panels. Left, muted: "<Problem>" with a simple illustration
of it. Right, bright: the product from @image1 with "<Solution>".
```

## aplus_features (Flare, 16:9)

```
<Style line>. Title "<Title>". The product from @image1 in the center, with
<3–4> feature tiles around it, each an icon and a short label: "<Feature 1>",
"<Feature 2>", "<Feature 3>".
```

## aplus_ingredients (Flare, 16:9)

```
<Style line>. Title "<Title>". The product from @image1 with <3–4> named
ingredients or materials shown as real objects (<list>), each labeled
"<name>: <one-line benefit from the user>".
```

## aplus_efficacy (Flare, 16:9)

Only with results the user supplies and can support.

```
<Style line>. Title "<Title>". <2–3> large figures with labels, exactly:
"<result 1>", "<result 2>". Small footnote: "<source or study note from the
user>". The product from @image1 at the side.
```

## aplus_how_to_use (Flare, 16:9)

```
<Style line>. Three numbered steps left to right, each a simple photo-style
panel of the product from @image1 in use with a caption: "1. <Step>",
"2. <Step>", "3. <Step>".
```

## aplus_endorsement (Flare, 16:9)

Only with real quotes the user supplies, attributed as they specify.

```
<Style line>. <1–3> quote cards: "<quote>" — <attribution>. The product from
@image1 beside them. No star ratings.
```
