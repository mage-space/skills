# Prompt guide

Mage's models reward concrete, visual prompts in plain sentences. Write what the camera sees. This guide covers what every model shares; each model's own file in `references/models/` covers what is particular to it (its structure, how it numbers inputs, its dialogue syntax, what to avoid) and wins where the two differ.

## The core split

The biggest split is **image vs video**, not tags vs prose.

- **Video models** get motion-first prompts that describe change over time: a short script, not a still frame. See **Video**; this is a hard rule.
- **The Stable Diffusion family** (Stable Diffusion XL, SDXL Plus, Stable Diffusion v1.5) gets short, tag-forward prompts.
- **Anima** has its own Danbooru-style tags and conventions (`references/models/anima.md`).
- **Every other image model** responds best to clear natural language with a few precise visual details.

## Images

Order the prompt as: image type (when there is one) → subject → action → setting → style or medium → light and color → framing.

- **Image type:** say what it is for first when that sets the mode: "Design a logo…", "A poster…", "A product photo for a listing…".
- **Subject:** who or what, with the details that matter (materials, colors, age, clothing).
- **Setting:** place, time of day, weather.
- **Composition:** framing (close-up, full body, overhead), lens (35mm, 85mm), angle, depth of field.
- **Light:** golden hour, softbox, rim light, neon, overcast. Name the source and direction.
- **Style:** photograph, film still, watercolor, 3D render, flat vector, anime.

Example: "A ceramic coffee cup on a sunlit oak table, steam rising, shot on 50mm at f/2, soft window light from the left, warm editorial photograph."

- **Length follows the model.** Short to medium prompts suit most models; Mango 3 and Guava reward long, exact descriptions (inventory a busy scene element by element, by where each sits), and SDXL reads only about 60 words. Say what matters most instead of stacking near-duplicate adjectives: twelve mood words lose to one light source, one lens and one style.
- **Phrase what you want**: "tack sharp" instead of "no blur", "empty street" instead of "no people". Where a model takes a negative list (Lemon's "Negative prompt list", Guava's `negative_prompt`), keep it to the specific things that must not appear.
- **Settings are fields.** Aspect ratio, resolution, "4K", duration and frame rate go in `config`, never in the prompt.
- **One call, one image.** For a set (a storyboard, a campaign), make one call per image with the same handles, style line and ratio, changing only the scene.

## Text in the image

Mango 3 renders short text natively in English, Chinese and 14 other languages; long copy that must be letter-perfect belongs on GPT Image 2.5 Flare. Put the exact words in double quotes and say where they go and how they look: `Headline "SUMMER SALE" in bold white sans-serif across the top third; below it "Up to 40% off" in smaller type.` Keep each line short. Never write a word with `@` in front of it (Mage reads it as a handle). Check the spelling in the result before delivering.

## Inputs in the prompt

- **Models that number their inputs** (Mango, Guava, GPT Image, Nano Banana, Grok, Cherry, Lemon, Plum, Raspberry, Berry): point at each input by its number, `@image1`, `@image2`, and say what to take from it: "the face and hair from @image1", "use only the layout and light of @image2". The model's file shows how Mage numbers your images, characters and references.
- **A single start frame**, or a model with no numbering: name the subject by what it visibly is ("the blonde woman in the red coat") and spend the prompt on what changes.
- **Never** write unnumbered pointers: "the reference", "the attached photo", "keep it consistent with the reference image".
- **Saved characters and references:** mention a handle once, bound to a name ("Ana (@ana) sits…"), then use the name.

## Edits

With a reference image, describe the change, not the whole picture again. Separate what changes from what stays.

- Good: "Replace the background with a foggy pine forest at dawn. Keep the person, pose, and clothing exactly the same."
- Bad: "A woman with brown hair in a red jacket standing in a forest."

Name what must not change ("keep the product label and logo unchanged") and the target by visible traits or position ("the person on the left"), never a pronoun. Add the physical consequence of the change: shadows, reflections, how it blends. For several images, point at them by number: "Dress the model in @image1 in the jacket from @image2." Change one thing per edit; restate what stays every time.

## Video

A video prompt is a time-based script. The most common failure is a prompt that reads like a photo caption: the clip comes out nearly static, or moves unpredictably. Decide what *happens* on screen and write it as ordered beats driven by verbs.

**Beats**, in the order they happen (join simultaneous things with "as" or "while"):

1. **Opening state:** subject, look, setting and starting pose, in one short clause.
2. **Primary motion:** the main action, led by a concrete verb (walks, turns, reaches, laughs, accelerates, collapses).
3. **Secondary motion or reaction:** what happens next, or what the world does in response (petals swirl, dust kicks up, the crowd parts).
4. **Camera:** how the shot moves or holds.
5. **Style, light and mood:** short supporting cues at the end, not the backbone.
6. **Sound**, for models that make it: ambience, effects, music, and any spoken line in quotes. Say "no dialogue" or "no background music" when you want none.

**Motion verbs:** walks, strides, runs, turns, tilts, leans, reaches, grabs, lifts, drops, opens, glances, smiles, exhales, steps forward, rises, falls, spins, drifts, pushes, pulls, flickers, ignites, shatters, scatters, ripples, unfurls, emerges. "Beautiful", "serene" and "majestic" describe a still; they generate no motion.

**Camera:**

- Hold: static camera, locked-off shot, tripod shot.
- Push and pull: slow push in, fast push in, slow pull back, dolly out.
- Pan and tilt: pan left, pan right, tilt up, tilt down, whip pan.
- Track: tracking shot, follow shot, side tracking, overhead tracking.
- Rig and feel: handheld, steadicam, gimbal, crane shot, aerial, drone pullback.
- Framing change: medium shot pushing to close-up, wide establishing to medium, over-the-shoulder.

One dominant camera move per shot, unless you are scripting a progression.

**From an image** (a first frame, or a still as the reference): the image is the opening state. Don't redescribe it; open with a short clause naming the subject and setting in visible terms, then spend the prompt on what changes. On Cherry, write `Use @image1 as the first frame.` as its own sentence (`references/models/cherry.md`).

Still-state prompt (bad): `A beautiful anime girl with long black hair stands under cherry blossoms in a blue school uniform, soft smile, petals falling, spring daylight, cinematic lighting.`

Motion-first rewrite (good): `An anime girl in a navy school uniform stands beneath blooming cherry blossoms. She looks up at the petals, then turns toward the camera and smiles softly as a breeze lifts strands of her hair. The camera slowly pushes in from a medium shot to a close-up. Bright spring daylight, soft cinematic anime lighting.`

Rules:

- Beats in timeline order; never describe the ending before the middle.
- Keep scene detail short: still-image adjectives drown the motion.
- One clear action per shot; a 4–5 second clip holds one or two beats.
- Script cuts only when the user wants several shots. Each model marks shots its own way: Cherry 2 Pro takes `Shot N` or whole-second ranges, the other Cherrys take `Shot N` only, Lemon takes `Shot 1 [0-3s]`. Read the model's file.
- Describe sound and dialogue only for a model that makes audio (Cherry, Lemon, Plum, Berry, Kiwi, Raspberry, Blueberry; Melon with `generate_audio`). Grok Video makes sound but no speech, and some open models, such as LTX Video, are silent: each model's file says which.
- No inline flags (`--duration`, `--ar`, `--camerafixed`): they are `config` fields.

## Likeness: keeping a person on model

When the same person (the user's character, a creator, a model) must look like themselves across stills and clips:

1. **Save them once.** Crop a tight, front-facing face from their reference (the face fills most of the frame, evenly lit), get it to a link (`create_upload` when you can run commands), and `create_character` from it. Mention the `@handle` in every shot, and on models that take reference images pass the face crop as `image` too: `Ana (@ana), her face exactly as in @image1, …`.
2. **Lock the face in a still first**, where it is cheap to check: the still with the `@handle`, the face crop and the scene, on Mango 3. Compare it with the reference feature by feature (face shape and length, eyes, nose, jaw, hairline, skin tone, build) if you can see images, or show both to the user. Fix the still before any video.
3. **Animate from the approved still**, as the video's reference image or first frame, with the `@handle` and the face crop. Describe what the still shows; never re-describe the face from memory.
4. **The user's own video, recast as their character:** an edit keeps the source's pixels, so the source person's face and body win over any reference. When the likeness matters more than the exact motion, generate from the approved still instead, describing the source's action, framing and timing, and say what that trades.
5. **Keep the face large.** Wide shots lose the likeness first: frame the person at medium or closer, or redo a wide shot that drifted closer in.
6. **Say only what you checked:** that a result matches the reference only after the comparison, naming what you compared; when a feature drifted, say which.

## Real, not "AI"

For UGC and anything that should pass for phone footage or a real photo:

- Light the face with the scene's own light: name its source and direction (window light from the left, the office's overhead lights) and the shadows it casts under the brow, nose and chin. Never a beauty light the scene does not have: a face brighter than its surroundings reads as fake.
- A phone camera, not a cinema one: handheld with a slight drift, arm's-length selfie or a friend's framing, a little off-center, natural exposure and a little grain, and no shallow depth of field unless asked.
- Ordinary behavior: small, specific gestures (fixing hair, glancing off camera, a half-laugh), not posed presenting to the lens.
- Skin with texture (pores, fine lines, uneven tone) and hair with flyaways. Leave out "flawless", "perfect skin" and "studio".

## Rewriting a prompt

- For video, find what is missing (usually a verb-led primary motion, a secondary beat and a camera move) and add those beats before polishing the words. For "more cinematic", reach for camera behavior and light before adjectives.
- For images, match the style to the model: tag-forward for the Stable Diffusion family, Anima's own tags for Anima, natural language for the rest.
- Keep the user's subjects, counts, events and exact words; add craft (camera, light, sound), not plot.
- Write the main prompt first. Add a negative prompt only when the user asks for one or the model's file calls for it.

## Audio

- **Speech:** quote the exact words, then the voice: "A warm female narrator, early 30s, British accent, calm and unhurried." On Eleven Speech, the preset `voice` is the voice and bracketed tags direct the delivery (`[whispers]`).
- **Music:** genre, tempo, instruments, mood, structure: "Lo-fi hip hop at 80 BPM, dusty drums, Rhodes chords, vinyl crackle, relaxed." Never name an artist or a song; describe the sound.
- **Sound effects:** the source, the space, and the timing: "Glass shattering on a tiled floor in a large echoing hall, one impact then debris settling."

Seed Audio and Eleven Music return exactly (or close to) the `duration` you set; Eleven Speech runs as long as the text.

## Aspect ratio

- `16:9`: landscape, YouTube, cinematic.
- `9:16`: vertical, Reels, TikTok, Shorts, Stories.
- `1:1`: square feed posts, avatars.
- `4:5`: portrait feed posts (Instagram, Facebook).
- `21:9`: ultra-wide banners.

Generate at the delivery ratio; never crop a 16:9 result to 9:16.

## Safety

Mage refuses content that breaks its policy. Don't ask for sexual content involving real people, depictions of real public figures in compromising situations, or copyrighted characters and logos you don't own. A `content_blocked` result is final for that prompt.
