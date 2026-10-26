# Wan Video v2.2 (`wan_22`)

An open-weights video model from text or a start frame (opt-in), cheap and silent, with a faster Lightning variant. It was trained on footage labelled for lighting, composition, contrast and colour, so it responds well to explicit cinematography terms.

## Variants

| `model_id` | Use it for |
|---|---|
| `wan22-video` (default) | The better result of the two |
| `wan22-video-lightning` | Faster, cheaper drafts |

- `resolution` 240p (default), 360p, 480p, 720p. `aspect_ratio` 21:9 to 9:21.
- `num_frames` 81 (default) plays at 16 frames per second, about 5 seconds. Other lengths use 4n+1 frames (49 is about 3 seconds).
- Leave `num_inference_steps`, `guidance_scale` and `flow_shift` at their defaults unless the user asks.
- Inputs: `prompt`, optional `first_image`, `negative_prompt`. No last frame, no references, no characters.

## How Mage sends your prompt

- `prompt` goes to the model as written. Write it in English.
- **No sound.** The clip is silent: never write dialogue, voices, music or sound effects.
- `negative_prompt`: the model's standard negative list is always applied (garish colours, overexposure, a static frame, blurry detail, subtitles, a painted look, low quality, deformed hands and faces, extra limbs, a cluttered background, people walking backwards). Whatever you send is added after it, so add only what is specific to this shot.
- The prompt is read up to roughly 350 words. Aim for 60 to 200 words from text, under 100 from a first frame.

## Prompt structure

**Text to video**, in this order:

```
<Up to 4 cinematic tags, comma-separated.> <Subject with appearance details: looks, expression, count, pose.> <The action, told as a process from start to finish.> <Background details, with something in it moving.>
```

- Pick at most 4 tags from **Vocabulary**; you need not use every kind. Default to day time, medium or wide shot, center composition.
- Enrich the subjects the user named, but never add subjects they did not ask for (no people in a landscape).
- Tell the action as it unfolds: "she reaches for the cup, lifts it, and blows across the surface". If the request has no action, add one, and give the background motion too (clouds drifting, leaves stirring).
- No literary atmosphere sentences ("the scene is full of life and tension").
- A named style goes first, before anything else. For a non-photographic style (2D illustration, anime), drop the cinematic tags.
- Write "a clear blue sky" rather than just "sky": a bare sky tends to blow out.
- If the prompt already has a camera move, skip the camera-angle tag.

**From a first frame**: motion only. Keep the subject's actions and the camera moves ("the camera pans up", "moves from left to right"); drop any description of what the frame already shows. If the user gave only an action ("dancing"), name the subject from the frame ("the girl in the yellow dress dances"). Under 100 words.

## Vocabulary

| Kind | Tags |
|---|---|
| Time | Day time, Night time, Dawn time, Sunrise time |
| Light source | Daylight, Artificial lighting, Moonlight, Practical lighting, Firelight, Fluorescent lighting, Overcast lighting, Sunny lighting (say where it comes from: a window, a lamp) |
| Light quality | Soft lighting, Hard lighting |
| Light angle | Top lighting, Side lighting, Underlighting, Edge lighting |
| Colour | Warm colors, Cool colors, Mixed colors; low or high saturation, high contrast |
| Shot size | Extreme close-up, Close-up, Medium close-up, Medium shot, Medium wide shot, Wide shot, Extreme wide shot |
| Camera angle | Over-the-shoulder, Low angle, High angle, Dutch angle, Aerial, Overhead |
| Composition | Center, Balanced, Left-heavy, Right-heavy, Symmetrical, Short-side |

- **Lens**: long focus, medium focus, wide-angle, ultra-wide fisheye, tilt-shift.
- **Camera moves and their meaning**: push in for intimacy or tension, pull back to reveal, tracking to travel with the subject, orbit for importance (keep the arc under 45 degrees, or space distorts), static for stillness.
- **Styles**: felt, 3D cartoon, pixel art, puppet animation, claymation, black-and-white animation, tilt-shift miniature, time-lapse.

## References, characters, and frames

- One optional `first_image`: the clip opens on it and takes its shape. No last frame, references or characters.
- Name the subject as the frame shows it, then write only what moves and how the camera behaves.
- Always give an action, even a small one (a head turn, steam rising, leaves stirring): a frame with no described motion tends to come out nearly static.

## Text in the image

Text is unreliable. A short name tag or sign word in quotes sometimes holds ("a name tag reading 'Mia'"); add anything that must be readable afterwards in an editor.

## Avoid

| Problem | Write instead |
|---|---|
| A clip that barely moves | The action as a process, plus background motion |
| Mood adjectives instead of detail | Concrete looks, actions and light |
| More than 4 cinematic tags | The 4 that matter |
| Sound, dialogue or music | Nothing: the model is silent |
| Re-describing a first frame | Motion and camera only |
| Fast cuts or several scenes | One continuous shot |

## Examples

**Text to video** (`wan22-video`, 480p):

```
Edge lighting, medium close-up shot, daylight, left-heavy composition. A girl of about 11 sits cross-legged in a field of tall grass with two fluffy small donkeys standing behind her. She wears a simple floral dress, her hair in twin braids, and smiles as she reaches out and gently touches the wild flowers beside her. The donkeys flick their ears and lower their heads toward her shoulder. The grass sways in a light breeze under a clear blue sky.
```

**Night interior** (`wan22-video`):

```
Right-heavy composition, warm colors, night time, firelight. An eye-level close-up of a woman in a brown jumper, a colourful bead necklace and a pink knitted hat, seated at a black table. She looks just left of the camera and talks animatedly, her left hand rising and falling with her words. White candles burn on the table, their flames flickering; behind her, dark shelves fade into shadow.
```

**From a first frame** (`wan22-video-lightning`):

```
A model car rolls across the wooden board from right to left, bumps over a seam, and continues past the grass and wooden blocks. The camera tracks slowly with it.
```

**Stylised** (`wan22-video`):

```
Tilt-shift photography. A high-angle view of a busy city intersection at night: cars and pedestrians stream across as the traffic lights change, shop signs flicker along both streets, and buses turn slowly at the corner like toy models.
```
