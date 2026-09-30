# Portrait guide

The saved image is what every later generation copies. One strong portrait beats a busy one.

## What works

- **One subject**, face visible, eyes open, looking at or near the camera.
- **Head and shoulders**, or head to waist for a character whose clothes matter.
- **Even, soft light.** No harsh shadows across the face, no colored gels.
- **Plain background**: studio gray, white, or a soft blur.
- **Sharp and large**: at least 1024 px on the short side, JPEG or PNG.
- **Their usual look**: glasses, hair, and makeup as they normally appear.

## What fails

- Group photos, or a second face in the background.
- Sunglasses, masks, hats that hide the hairline, hands over the face.
- Heavy filters, beauty smoothing, extreme wide-angle selfies.
- Tiny faces in a full-body shot.
- Collages or multi-view character sheets: models may copy the grid.

## Generating a portrait

Photoreal person, Guava 2 Pro, `4:5`:

```
Studio headshot of a woman in her late 20s with short curly black hair and
freckles, wearing a mustard knit sweater, looking at the camera with a soft
smile. Plain warm-gray backdrop, 85mm lens, soft key light from the left,
gentle fill, sharp focus on the eyes, natural skin texture.
```

Illustrated character or mascot, Mango 3, `1:1`:

```
Character portrait of a friendly robot barista with a rounded copper body,
glowing teal eyes, and a small green apron, facing the viewer, centered, plain
off-white background, soft even lighting, clean 3D animated-film style.
```

Show the portrait and let the user approve or adjust it before saving.

## Voices

A character's voice is a clip of up to 10 seconds of natural speech, one speaker, no music. To make one with Seed Audio (`duration: "10"`):

```
A warm, slightly raspy male voice in his 40s with a light Irish accent, relaxed
and friendly, says: "Morning! I saved you the corner table, same as always."
```

Pass the result's `url` as `voice` when you call `create_character`.
