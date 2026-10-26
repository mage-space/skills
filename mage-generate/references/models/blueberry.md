# Blueberry (`blueberry`)

A video model that fills the motion between a first and a last frame, with generated sound (opt-in). Blueberry 2 (`blueberry-v2`) is the current version. It also takes text alone, and one audio clip that drives the soundtrack and lip sync.

## Variants

| `model_id` | Frames | Shots | Prompt length |
|---|---|---|---|
| `blueberry-v2` (default) | First frame, or first and last frame | Reads single or multi-shot from your prose | Up to 5,000 characters |
| `blueberry` | First frame only | Multi-shot only with a first frame, `shot_type: "multi"` and `prompt_extend: true` | Up to 1,500 characters |

- Both: `resolution` 720p (default) or 1080p, `duration` 2 to 15 seconds (default 4), `aspect_ratio` 16:9, 4:3, 1:1, 3:4, 9:16 for text to video; a first frame sets the shape itself.
- Use `blueberry-v2` unless the user asks for the older one.

## How Mage sends your prompt

- `prompt` goes to Blueberry as written, with `first_image` and, on `blueberry-v2`, `last_image`.
- **A last frame only works with a first frame.** Sent alone, it is dropped and the clip is made from text.
- One saved audio clip may be mentioned (`@handle`). Its sound becomes the clip's soundtrack: speech in it is lip-synced, motion follows its rhythm, a clip longer than the video is cut, a shorter one leaves silence at the end. In the prompt the mention reads as `[Audio 1]`; say what it is and who performs it ("the boy raps along to @verse").
- No characters or references: describe people by how they look.
- `prompt_extend` (default false) has Blueberry rewrite your prompt with its own model; leave it off when you wrote the shot. `shot_type` (default `"single"`) matters only on `blueberry` with a first frame.
- `negative_prompt` (up to 500 characters) passes through though `get_model` does not list it.
- Sound is always generated: voices, effects and music made to fit the picture. Shape or silence it in the prompt.

## Prompt structure

**First and last frame**: the two images fix the start and the end; the prompt is the journey between them. Describe what happens, in order, and how the camera moves. When the two frames differ a lot, name the bridge: a camera move ("the camera rises from eye level to a top-down view") or a subject move ("she runs forward into the light"). Do not describe the frames' looks again.

**First frame only**: motion and camera only. "Fixed camera" holds the framing while the subject moves.

**Text to video**: subject (described) + scene (described) + motion (how big, how fast) + light source, lighting, shot size, angle, lens and camera move + style + sound.

**Several shots** (`blueberry-v2`): an overall sentence, then numbered, timed shots:

```
<Overall: theme, mood, pacing.> Shot 1 [0-2s]: <shot>. Shot 2 [2-4s]: <shot>. Shot 3 [4-7s]: <shot>.
```

`blueberry-v2` decides single or multi-shot by itself when you do not say. Start with `Generate single shot.` to keep one continuous take, which first-to-last-frame clips nearly always want.

## Vocabulary

- **Light source**: daylight, firelight, overcast light, practical light, moonlight, fluorescent, mixed light. **Quality**: soft, hard, side, rim, backlight, top light, high or low contrast.
- **Shot size**: close-up, medium close-up, medium, medium full, wide, establishing shot. **Angle**: eye level, over-the-shoulder, high, low, top-down, aerial. **Lens**: telephoto, wide-angle, fisheye, tilt-shift.
- **Moves**: push in (tension), pull back (reveal), tracking (travel with the subject), orbit (importance; keep under 45 degrees), fixed (stillness), "drone fly-through, then rises fast and tilts up" for scale.
- **Styles**: felt, 3D cartoon, pixel art, puppet animation, claymation, black-and-white animation, time-lapse.

## References, characters, and frames

- The output takes the first frame's shape: make the last frame the same shape and size, with the same subject and setting unless the move between them changes them.
- A loop: the same image as first and last frame, with motion that returns to where it began.
- Longer sequences: the last frame of one clip becomes the first frame of the next.
- No characters or references here. For a recurring person, make both frames on an image model that takes saved characters (Mango 3), then animate between them.

## Audio and dialogue

- **Lines**: `The fox says in a smooth, cynical voice: "..."`, with emotion, tone, speed, timbre and accent. Quoted lines are spoken as written; without one, Blueberry may improvise.
- **Two speakers**: fixed labels for each, never pronouns; the speaker's action before the line; a voice description per speaker; timing words between lines ("Immediately, the woman replies: ...").
- **Sound effects**: source, material, action, ambience ("a dull crack as the pumpkin splits, a soft hiss of mist"). **Music**: the kind and the mood.
- **Silence**: "No dialogue." and "No background music."
- **With an audio clip**: say what the soundtrack is and that nothing else is added: "The audio is entirely the rap from @verse, with no other dialogue or noise."

## Text in the image

Exact text renders only approximately: keep it to a short quoted word on a sign, and add anything that must be readable afterwards in an editor.

## Avoid

| Problem | Write instead |
|---|---|
| A cut in a first-to-last-frame clip | `Generate single shot.` first |
| A jump instead of a transition | Name the camera or subject move that links the frames |
| Re-describing what the frames show | The action between them |
| A last frame sent without a first frame | Both frames, or none |
| A long chain of actions in 4 seconds | One main action and one reaction, or a longer `duration` |

## Examples

**First to last frame** (`blueberry-v2`, 5 s):

```
Generate single shot. At sunrise a small dew-covered pumpkin sits in a pumpkin patch. Suddenly it cracks open with a loud crack; a warm light pours from the split as it falls apart, releasing a puff of white mist, and a small rabbit blinks in the center. Fixed camera. A dull crack, a soft hiss of mist, birdsong.
```

**A move that bridges two different frames** (`blueberry-v2`, 4 s):

```
Generate single shot. The small black cat looks up at the sky with curiosity. The camera rises steadily from eye level and ends looking straight down on the cat's upturned face. Quiet garden ambience.
```

**First frame driven by an audio clip** (`blueberry-v2`, 8 s):

```
A graffiti boy made of spray paint peels himself off a concrete wall under a railway bridge at night and raps fast to @verse, hitting a classic, high-energy rapper pose on every beat. A single street lamp lights him. The audio is entirely the rap, with no other dialogue or noise.
```

**Text to video in shots** (`blueberry-v2`, 10 s):

```
A calm vision of a future city and its gardens. Shot 1 [0-2s]: Wide shot of a rooftop garden, floating plants swaying in the breeze. Shot 2 [2-4s]: A robot gardener trims a hedge with precise, graceful movements. Shot 3 [4-7s]: Sunlight streams through a glass dome and lights the whole garden. Shot 4 [7-10s]: The camera pulls back to reveal the vast city, the garden one small part of it. Soft ambient synth music, birdsong.
```
