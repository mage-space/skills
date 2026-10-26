# Kiwi (`kiwi`)

Everyday video from text or a single start frame, with generated sound and nothing else to set up (opt-in). One continuous shot per clip, 5 or 10 seconds.

## Variants

One variant, `kiwi`.

- `duration` 5 (default) or 10 seconds. `resolution` 480p (default), 720p, 1080p. `aspect_ratio` 16:9, 4:3, 1:1, 3:4, 9:16; with a first frame the output takes the frame's shape.
- Inputs: `prompt` and an optional `first_image`. No last frame, no reference images, no characters, no voices.
- Keep the prompt under 1,500 characters.

## How Mage sends your prompt

- `prompt` reaches Kiwi as written. `@handles` are not supported on Kiwi; describe people by what they look like.
- `prompt_extend` is on unless you send `prompt_extend: false`: Kiwi then rewrites and enriches your prompt with its own model. `get_model` does not list it, but it passes through. Leave it on for a short idea; turn it off when you wrote the full shot and want your wording, timing and lines kept.
- `negative_prompt` (up to 500 characters) also passes through though not listed.
- The clip always has sound: voices, effects and music made to fit the picture. Shape it in the prompt.

## Prompt structure

**Text to video**: subject (described) + scene (described) + motion (described: how big, how fast, its effect) + aesthetic control (light source, lighting, shot size, angle, lens, camera move) + style + sound.

Most weak prompts skip the aesthetic control and the style and come out as a static camera in an undefined place. Always name the light, the shot size and the camera behaviour.

```
<Shot size, angle, lens, light source and quality, colour tone, composition.> <Subject with key looks> <does the action, step by step> in <setting with moving detail>. <Camera move.> <Style.> <Sound: voice line with emotion, effects, music.>
```

**First frame**: the image already holds the subject, scene and style. Write only the motion and the camera: what moves, in what order, and how the camera behaves. "Fixed camera" keeps the frame still while the subject moves.

**One shot only.** Kiwi makes a single continuous shot. Rapid scene changes inside one clip break it; make each scene its own clip and join them in the edit.

## Vocabulary

- **Light source**: daylight, firelight, overcast light, clear-sky light, practical light, moonlight, fluorescent, mixed light.
- **Light quality**: soft, hard, side, rim, backlight, top light, high or low contrast. **Time**: daytime, night, dawn, sunrise, sunset, dusk.
- **Shot size**: close-up, close shot, medium close-up, medium, medium full, wide, establishing shot.
- **Composition**: center, left-heavy, right-heavy, balanced, symmetrical. **Angle**: eye level, over-the-shoulder, high angle, low angle, top-down, aerial. **Lens**: telephoto, medium focal length, wide-angle, fisheye, tilt-shift.
- **Camera moves and what they say**: push in for intimacy or tension, pull back to reveal scale or isolation, tracking to travel with the subject, orbit for importance (keep the arc under 45 degrees, or space warps), fixed for stillness.
- **Styles**: felt, 3D cartoon, pixel art, puppet animation, claymation, black-and-white animation, tilt-shift miniature, time-lapse.

## References, characters, and frames

- One optional `first_image`: the clip opens on it and takes its shape. There are no other image inputs.
- Name the subject the way the frame shows it ("the man in the grey overcoat") and spend the rest on what moves.
- For a person who must recur across clips, make the first frame on an image model that takes saved characters (Mango 3), then start each Kiwi clip from it.

## Audio and dialogue

- **Voice**: the quoted line plus emotion, tone, speed, timbre and accent: `The old fisherman says in a slow, gravelly voice: "Tide's turning."` Quoted lines are kept word for word; without one, Kiwi improvises speech.
- **Sound effects**: the source, its material and action, and the ambience: "the crunch of paws on snow, the swish of the rolling snowball, the crack as it breaks".
- **Music**: the kind and the mood: "a light, warm nursery-rhyme piano score".
- **Silence**: "No dialogue." and "No background music." when you want them gone.
- **Two speakers**: give each a fixed label and never switch to pronouns; show the speaker's action before the line; give each a voice description; link lines with timing words ("Then the woman murmurs: ..."). Two or three short lines is the most a 5-second clip holds.

## Text in the image

Exact text renders only approximately. Keep it to one short word on a sign or a balloon, in quotes (`a neon sign reading "OPEN" flickers`), and do not depend on it. Add anything that must be readable afterwards in an editor.

## Avoid

| Problem | Write instead |
|---|---|
| A near-static clip | A described motion with speed and size, and a camera move |
| Several scenes in one clip | One scene per clip |
| A long chain of complex actions | One main action and one reaction |
| Restating a first frame's looks | Motion and camera only |
| Lip sync to a long, exact speech | One or two short quoted lines |

## Examples

**Text to video with sound** (10 s):

```
Medium shot, eye level, soft morning daylight, warm colours, center composition. A fluffy ginger kitten in a snowy back yard rolls a snowball with its front paws and pushes it forward clumsily. The snowball breaks apart; the kitten jumps back in surprise, sneezes, then creeps closer and nudges the pieces with its head, tumbling over. The camera tracks slowly at kitten height. The crunch of paws on snow, the swish of the rolling snowball, the crack as it breaks, a tiny sneeze, and a light, warm piano melody.
```

**A spoken line** (5 s):

```
Low angle, medium close-up, warm tones, mixed light from a green desk lamp and grey window light. In a cluttered detective's office, a fox in a brown trench coat and grey fedora sits in a leather chair turning yellowed pages. Rain streaks the window behind him. He raises his head, ears twitching, looks straight at the camera and says in a smooth, cynical voice: "The case was cold. Colder than a fish in winter." Steady rain on glass, pages rustling. No background music.
```

**From a first frame** (5 s):

```
The camera pulls back slowly as the two men climb the stairs; the man on the left steadies the man on the right with his hand, and both pause on the landing to catch their breath. Footsteps on stone, heavy breathing.
```

**Stylised** (5 s):

```
Tilt-shift miniature look, high angle over a busy city intersection at night. Cars and pedestrians stream through in toy-like motion as the traffic lights change and shop signs flicker along both sidewalks. The camera holds still. Soft city hum, distant horns.
```
