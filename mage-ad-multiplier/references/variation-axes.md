# Variation recipes

Every prompt is two parts: **the change**, then **the lock**. The lock is what makes variations comparable in a test: only the tested element differs.

**Static lock** (end of every static prompt):

> Keep everything else in @image1 exactly the same: the product, its label and logo, the layout and composition, the camera angle and framing, all text and its position, the brand colors, and the lighting direction.

**Video lock** (end of every video prompt):

> Keep the original motion, camera moves, framing, cuts, timing, product, logo, on-screen text, and audio exactly as they are.

---

## Talent

```
Replace the person in @image1 with <a new person: age, look, hair, style, or
@character>. Same pose, expression intent, and hand position on the product.
<Static lock>
```

For video: "Replace the presenter with <…>, matching their movements and timing." + video lock. Mention a saved `@character` for a specific person; they must have consented to their likeness being used.

## Wardrobe

```
Change only the outfit of the person in @image1 to <outfit description, or
@outfit-reference>. Same person, same pose.
<Static lock>
```

## Setting

```
Move the scene in @image1 to <new location: a sunlit Scandinavian living
room / a rooftop at dusk / a busy street market>, relit to match, with the
person and product in the same place in the frame.
<Static lock, minus "lighting direction">
```

## Background

```
Replace only the background of @image1 with <solid color / gradient /
texture>. Keep every foreground element and its edges untouched.
<Static lock>
```

## Color story

```
Restyle the set dressing and color grade of @image1 in a <palette: sage and
cream / electric blue and orange> palette. Do not recolor the product or the
logo.
<Static lock>
```

## Season

```
Make @image1 a <season / holiday> version: <seasonal props, weather, light>.
<Static lock>
```

## Headline

Use GPT Image 2.5 Flare.

```
In @image1, replace only the headline "<old headline>" with "<new headline>",
in the same font, weight, color, size, and position. Keep every other word,
the product, and the whole layout exactly the same.
```

Good headline sets change the angle, not the wording: a benefit ("Softer skin in 7 days" only if true), urgency ("Last chance this week"), social proof ("Loved by 10,000 runners" only if true), curiosity ("The bag everyone's asking about"), and the offer ("Free shipping, today only"). Keep them under six words; no claims the user can't support.

## Remix (two axes)

Combine two change sentences, then the lock: "Replace the person with … and change their outfit to …". Never more than two axes in one variation: a test can't tell what worked.

## Naming variations

Label each result by axis and choice ("Setting · rooftop at dusk") so the user can map results to test cells.
