# Prompt guide

Mage's models reward concrete, visual prompts in plain sentences. Write what the camera sees.

## Images

Order the prompt as: subject → action → setting → composition → light → style.

- **Subject:** who or what, with the details that matter (materials, colors, age, clothing).
- **Setting:** place, time of day, weather.
- **Composition:** framing (close-up, full body, overhead), lens (35mm, 85mm), angle, depth of field.
- **Light:** golden hour, softbox, rim light, neon, overcast.
- **Style:** photograph, film still, watercolor, 3D render, flat vector, anime.

Example: "A ceramic coffee cup on a sunlit oak table, steam rising, shot on 50mm at f/2, soft window light from the left, warm editorial photograph."

Aim for one to four sentences. Very long prompts drift. Phrase what you want, not what you don't: "tack sharp" instead of "no blur", "empty street" instead of "no people".

## Text in the image

Use GPT Image 2.5 Flare. Put the exact words in double quotes and say where they go and how they look: `Headline "SUMMER SALE" in bold white sans-serif across the top third; below it "Up to 40% off" in smaller type.` Keep each line short. Check the spelling in the result before delivering.

## Edits

With a reference image, describe the change, not the whole picture again.

- Good: "Replace the background with a foggy pine forest at dawn. Keep the person, pose, and clothing exactly the same."
- Bad: "A woman with brown hair in a red jacket standing in a forest."

Name what must not change ("keep the product label and logo unchanged"). For several images, point at them with `@image1`, `@image2`: "Dress the model in @image1 in the jacket from @image2."

## Video

Describe the motion and the camera, then the sound.

- **Camera:** slow push in, dolly left, orbit, handheld, drone shot rising, static tripod.
- **Action:** one clear action per shot: "she turns and smiles", "waves crash against the rocks".
- **Sound:** Cherry and Lemon generate audio. Describe ambience, music, and any spoken line in quotes: `A barista says, "Your latte is ready."` Say "no dialogue" when you want none.
- **Shots:** for a multi-shot clip, number the shots with rough timings: "Shot 1 (0–4 s): … Shot 2 (4–8 s): …".

When animating an image (a Lemon first frame, or a Cherry reference), don't redescribe the frame. Describe what moves.

## Audio

- **Speech:** quote the exact words, then the voice: "A warm female narrator, early 30s, British accent, calm and unhurried."
- **Music:** genre, tempo, instruments, mood, structure: "Lo-fi hip hop at 80 BPM, dusty drums, Rhodes chords, vinyl crackle, relaxed."
- **Sound effects:** the source, the space, and the timing: "Glass shattering on a tiled floor in a large echoing hall, one impact then debris settling."

Set `duration` to the length you need; the MP3 is exactly that long.

## Aspect ratio

- `16:9`: landscape, YouTube, cinematic.
- `9:16`: vertical, Reels, TikTok, Shorts, Stories.
- `1:1`: square feed posts, avatars.
- `4:5`: portrait feed posts (Instagram, Facebook).
- `21:9`: ultra-wide banners.

## Safety

Mage refuses content that breaks its policy. Don't ask for sexual content involving real people, depictions of real public figures in compromising situations, or copyrighted characters and logos you don't own. A `content_blocked` result is final for that prompt.
