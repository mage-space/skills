# Shot routes on Mage

Read each model's fields once with `get_model` before its first call, price every line with `estimate_cost`, and use the original's aspect ratio (most viral videos are `9:16`). Model ids below are what `list_models` returns today.

## Recast a take: Magejutsu

For one continuous take of 4 to 30 seconds whose motion is the point: a dance, a transition, a stunt, a product being handled. It keeps the motion, camera, cuts, and timing, and rebuilds the people (`motion_transfer`) or swaps an object, outfit, or place (`object_swap`).

1. **Cut the stretch**, re-encoding so it starts on a frame: `ffmpeg -ss 3.2 -to 15.8 -i video.mp4 -c:v libx264 -crf 17 -pix_fmt yuv420p -c:a aac stretch.mp4`. A source outside the variant's window is refused, not trimmed.
2. **Upload it** with `create_upload` and use the returned `url`.
3. **References:** one clear photo per replaced person (sharp, front-facing; full-length for a dancer), or a saved `@handle`; a product alone on white for `object_swap`. Every visible person needs one, or the original's face stays.
4. **Generate** (`magejutsu`):

   ```json
   {
     "model_id": "magejutsu",
     "videos": ["<stretch url>"],
     "image": "<photo url>",
     "mode": "motion_transfer",
     "resolution": "720p",
     "prompt": "Image 1 replaces the dancer in the white hoodie. Keep the camera, the timing, and the room as filmed."
   }
   ```

   For a product: `"mode": "object_swap"`, `"prompt": "Image 1 replaces the bottle on the counter. Keep the hands and everything else as filmed."`

| `model_id` | Source | Use it when |
|---|---|---|
| `magejutsu` | 4–30 s | The default and most faithful; people and objects |
| `magejutsu-lite` | 4–15 s | Cheaper and faster; weaker on expressions, lip sync, and small faces |
| `magejutsu-feather` | 4–15 s | Cheapest; people only, 480p or 720p, least faithful |

Magejutsu returns the original soundtrack (it guides the lip sync). Replace it in the cut with the new music, so none of the original's sound reaches the result. A take where someone speaks keeps their mouth on the old words: rebuild talking shots instead, with the user's lines.

## Rebuild a shot: keyframe, then video

1. **Keyframe** on Mango 4 (`mango`, `"model_id": "mango-v4"`, the original's `aspect_ratio`), product photo in `image`:

   ```text
   <shot size and camera angle from the timeline>: @nova <action> in <setting>,
   <light from reel/look.md>, <look: smartphone footage | glossy 3D render |
   cel animation | stop-motion clay>. Keep the product from image 1 exact:
   shape, colors, label, logo.
   ```

   Show the keyframes before any video; fix one here, where it costs a few Gems.

2. **Video** on Cherry 2 Pro (`cherry`, `"model_id": "cherry-2-pro"`, `"resolution": "720p"`, `aspect_ratio` as the original, `duration` the smallest option at or above the shot's length), keyframe in `image`, product photo in `additional_images`:

   ```text
   Vertical smartphone video. [Medium shot, handheld, slight push in]
   @nova lifts the bottle from image 2 off the counter and turns the label
   to the camera, smiling. She says: "<new line>". End with the label facing
   the lens. Room tone, no music, no subtitles or on-screen text.
   ```

   Captions and music go on in the cut, so ask for none in the clip.

3. **Shots that share a set and cast** (the same `G1` group in `reel/timeline.md`) go in one Cherry 2 Pro clip, one shot per 3 to 5 seconds, each written as `Shot 2: [framing, camera move] action, line, end state`. Cut them apart in the assembly.

4. **Short shots.** Cherry's shortest clip is 4 seconds: generate 4 and trim, or fold the shot into its group. Lemon (`lemon`) goes down to 2 seconds and takes an exact `first_image` (and `last_image`), for a shot that must start or end on a given frame; it can't mix frames with reference images, so put the product in the keyframe.

| Original shot | Look to ask for | Notes |
|---|---|---|
| Filmed footage | Smartphone footage: handheld drift, the scene's own light, a little grain, ordinary gestures | Or the user films it from `reel/look.md`'s framing and light |
| AI-generated video | Match the original's style words from `reel/shots/<n>.md` | The cheapest to remake: everything is generated anyway |
| 3D render, 2D animation | Name the look (glossy product render, flat cel animation) | |
| Stop motion | "Stop-motion clay animation" | Step it afterwards: `ffmpeg -i in.mp4 -vf fps=12 out.mp4` |
| A talking avatar | The user's `@character` speaking the line | Their saved voice speaks it (`use_character_voices` stays on) |
| A still with a push or pan | A Mango 4 still | Move it in ffmpeg (`references/assembly.md`) |
| Text, charts, UI | Build it in code (an HTML page recorded with a headless browser, or a template tool), or a still with exact text on GPT Image 2.6 Flare (`gpt_image_2`, `gpt-image-2.6-flare`) | Text in generated video garbles |

## Sound

- **Music** on Seed Audio (`seed_audio`, `"model_id": "seed-audio-1.0"`, `duration` the next option above the remake's length):

  ```text
  Instrumental <genre> at <BPM> BPM in <key>, <mood>, building at <s> s and
  dropping at <s> s, no vocals.
  ```

  Take the tempo, key, and section changes from `reel/sound.md`. Never name the original song or an artist.

- **Voice-over:** the line in quotes with the voice described (age, tone, pace) on Seed Audio, or the character's saved voice through Cherry 2 Pro.
- **Sound effects:** one Seed Audio clip per kind ("a short bright pop, 0.3 seconds"), placed at the times `reel/sound.md` lists.

## Prices

Quote each line with `estimate_cost`; for a recast, upload the stretch first so its length can be measured. Rough order on 2026-11-11: a Mango 4 keyframe 42 Gems, a 4-second Cherry 2 Pro clip at 720p about 1,400, a 10-second Magejutsu recast at 720p about 4,300 (Lite 3,600, Feather 1,400), a Seed Audio track under 120. Always use the live quote.
