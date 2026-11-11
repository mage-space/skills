# Prompt templates

Replace every `[bracket]`, keep the locked-details string word for word, and write LEFT or RIGHT only for features that have a side. `@kai`, `@kai-look`, `@mira` stand for the handles `create_character` and `create_reference` returned.

Mage rewrites mentions and numbers every image before the model reads the prompt: your `image` first, then `additional_images`, then each mentioned character, then each mentioned reference, in order of first mention. `@kai` becomes "character from image N" and `@kai-look` "outfit from image N". Lemon and Cherry call the `videos` "Video 1", "Video 2"; write those names yourself. Mention each handle once, bound to a name ("Kai (@kai)"), and use the name after that.

## Master

Mango 4, `aspect_ratio: "2:3"`, `resolution: "2K"`; the user's design or photo as `image` when there is one.

```text
Full-body [photorealistic / 3D animated film / anime] portrait of one original [age, kind of character], standing upright in a relaxed neutral pose, facing the camera, arms at the sides, feet slightly apart, the whole body in frame including the shoes. [Hair: colour, length, style]. [Face: shape, eyes, skin]. [Locked detail 1 with its side]. [Locked detail 2 with its side]. [Locked detail 3]. Wearing [top, bottom, shoes, accessories, with colours and materials]. Seamless light grey studio background, soft even lighting, no shadows on the backdrop, sharp focus head to toe. One person only, no props. No text, no logos. This image fixes appearance only.
```

## Sheet

Mango 4, the master as `image`, `aspect_ratio: "16:9"`, `resolution: "2K"`.

```text
Turn the character in image 1 into a clean character reference sheet on a seamless light grey background. Keep the face, [hair], [locked details with their sides] and [outfit] identical to image 1. Two rows. Top row: three full-body views at the same scale in the same neutral pose: front, right side profile, back. Bottom row: three head-and-shoulders close-ups at the same scale: front, three-quarter, side profile. Even studio lighting, panels aligned and evenly spaced, the same colours in all six. No text, no labels, no arrows, no logos.
```

## Split frame

Mango 4, the master as `image`, `aspect_ratio: "16:9"`, `resolution: "2K"`.

```text
Create a 16:9 split-frame reference of the character in image 1 on a seamless light grey background. Keep the face, [hair], [locked details with their sides] and [outfit] identical to image 1. Left third: the full body head to toe, neutral pose facing the camera, small enough that [the shoes] and [the hair] fit with a margin. Right two-thirds: a large head-and-shoulders close-up of the same character facing the camera, the face filling most of the area, with sharp detail on the eyes, skin and [the detail that matters most]. A thin vertical gap divides the two areas. The same even lighting on both. No text, no labels, no logos.
```

## Turntable

Lemon, reference mode: `image` = the split frame, `aspect_ratio: "16:9"`, `resolution: "720p"`, `audio: false`, `duration: "10"` (or `"6"`). Image 1 is the split frame, so `@kai` reads as image 2 and `@kai-look` as image 3. No `first_image`: Lemon takes frames or references, never both, and only references carry the sheet's back view.

```text
Generate single shot. The video follows image 1, adopting its layout, background and lighting: a full-body figure in the left third, a large head-and-shoulders close-up in the right two-thirds, a thin vertical divider, a seamless light grey studio. Both figures are Kai (@kai), wearing @kai-look: [locked-details string]. The outfit reference shows how he looks from the side and the back; match it as he turns, and never show its panels. Locked-off static camera: no camera movement, no zoom, no cuts. Character turntable reference. Both figures rotate in place through one complete, smooth, constant-speed 360-degree turn, clockwise, in perfect sync, ending facing the camera again. The full-body figure on the left turns on its vertical axis, showing the front, one side, the back, the other side and the front again, keeping the neutral standing pose with relaxed arms. The head-and-shoulders close-up on the right turns at exactly the same speed: front, profile, back of the head, other profile, front. [Locked detail 1] stays on [his/her/their] [LEFT/RIGHT] side and [locked detail 2] on [his/her/their] [LEFT/RIGHT] side throughout. [Hair] and [outfit] stay the same. Calm neutral expression, no talking. Even studio lighting, seamless light grey background; both figures keep their places and the divider stays fixed. No dialogue, no music.
```

## Image scene

Mango 4 at the delivery aspect; add the master as `image` for a back view or a profile.

```text
Kai (@kai) wearing @kai-look: [locked-details string]. The outfit reference also shows his hair and build from the side and back; ignore the grey studio background and the panel layout of every reference. [Scene: place, time of day, light and its direction, what he does, where he is in frame, camera angle and lens]. [Style]. No text, no logos.
```

## Video scene, turntable route

Lemon, reference mode: `videos: [turntable]`, `image`: the master, `resolution: "720p"`, `duration` so that the turntable's seconds plus `duration` stay at or under 30. Image 1 is the master, so `@kai` reads as image 2 and `@kai-look` as image 3.

```text
[One sentence: genre, mood, pacing].
Kai (@kai), wearing @kai-look, is the [man / woman / animated character] in Video 1 and image 1: [locked-details string]. Video 1 shows him turning through every angle and image 1 shows him head to toe; use them only for his appearance. Nothing else from them appears on screen: ignore the grey studio background and the split-screen layout.
Shot 1 [0-3s]: wide, from behind: Kai walks away from the camera toward [something], showing the back of his hair and outfit.
Shot 2 [3-7s]: he stops and the camera orbits a slow half circle around him, passing his left side, his front, then his right side.
Shot 3 [7-10s]: close-up: he turns and looks straight into the lens.
Sound: [ambience], no dialogue, no music.
Style: [lighting and colour], cinematic, realistic skin texture.
```

## Video scene, Cherry 2 Pro

`image`: the master; `@kai` and `@kai-look` in the prompt; no reference video; `Shot N` paragraphs with no timestamps.

```text
Kai (@kai), wearing @kai-look, is the [man] in image 1: [locked-details string]. The outfit reference also shows his hair and build from the side and back. Ignore the grey studio backgrounds and the panel layout of the references. Scene: [place, time of day, light].
Shot 1: [framing and camera]. Kai [one clear action].
Shot 2: [framing and camera]. Kai [one clear action, ending state].
Sound: [ambience], no dialogue, no music.
```

## Two characters (video, Lemon)

`videos`: both turntables (6 s each), `image` and `additional_images`: both masters. Image 1 is Kai's master and image 2 Mira's, so `@kai` reads as image 3 and `@mira` as image 4.

```text
Two characters meet in one scene. Kai (@kai) is the [kind] in Video 1 and image 1: [Kai's locked string], wearing [outfit]. Mira (@mira) is the [kind] in Video 2 and image 2: [Mira's locked string], wearing [outfit]. Kai and Mira are two different people and must not look alike; each look stays locked to its own references, with no mixing or swapping. Ignore the grey studio backgrounds and split-screen layouts of the references; nothing else from them appears on screen.
Shot 1 [0-3s]: wide: [how they first appear].
Shot 2 [3-6s]: over Mira's shoulder: [Kai approaches].
Shot 3 [6-10s]: medium two-shot in profile: [one simple interaction].
Sound: [sounds], no dialogue, no music.
```

## Outfit change

Mango 4, the master as `image`, `aspect_ratio: "2:3"`.

```text
Keep the character in image 1 identical: the face, [hair], [locked details with their sides] and body. Change only the outfit to [top, bottom, shoes, accessories, colours, materials]. The same relaxed neutral standing pose facing the camera, the whole body head to toe, the same seamless light grey studio background and soft even lighting. No text, no logos.
```

## A still matched to real footage

For a character who must sit inside the look of real or phone footage. Mango 4 at the delivery aspect; `image` and `additional_images`: two or three frames of the source scene; `@kai` and `@kai-look`. Before writing it, note where the main light comes from, how soft and what colour it is, and the shadows it casts.

```text
One natural frame from a [handheld phone / camcorder] video, [aspect], [time of day and weather] in [setting]. Kai (@kai) is [build, natural proportions], with [locked-details string], wearing @kai-look. Use images 1 and 2 only for the camera perspective, the place and the light; do not copy the outfit reference's grey background. Rebuild his face, ears, hair, neck and body as one person under the scene's light: [main light direction and softness], with the shadows under his brow, nose and chin falling the same way as the shadows on his body and the ground. [Camera position and distance]: he is [pose and place in frame]. [Source-matched exposure, colour and lens softness]. Keep fine roots and the part visible beside highlights, with no painted dark band along the hairline. No text, no captions, no watermark, one scene, no collage.
```

Animate it on Lemon as `first_image` (no mentions) for a fixed shot, or on Cherry 2 Pro as `image` with `@kai`. Give the clip one connected action: attention, action, contact, release, reaction, settle.

## Recast

Magejutsu, `mode: "motion_transfer"`, the source in `videos`, `image`: the character (a scene still or the master), `additional_images`: the face crop, then the sheet.

```text
Recast [the person to replace, by position] throughout the source as Kai. Image 1 is Kai as he should appear, defining his proportions and wardrobe. Image 2 is the authoritative face. Image 3 shows the same person from several angles, for identity, profile and hair only; ignore its studio background, outfit and panel layout. Keep [locked-details string] in front, three-quarter and profile views. Follow the source's performance, camera, timing and shot order. Rebuild the whole person under the source's light, with face, hair, neck and body lit as one. [Audio and on-screen text instructions].
```
