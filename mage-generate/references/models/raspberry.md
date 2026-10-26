# Raspberry (`raspberry`)

A character video model (opt-in): up to 5 reference images of people, props and places, an optional first frame, the characters' saved voices, and generated sound. It casts a scene from references and has them act and speak.

## Variants

One variant, `raspberry`.

- `resolution` 720p (default) or 1080p, `duration` 2 to 15 seconds (default 4), `aspect_ratio` 16:9, 4:3, 1:1, 3:4, 9:16; a first frame sets the shape itself.
- Prompts up to 5,000 characters.

## How Mage sends your prompt

Raspberry picks its mode from the inputs:

| You send | Mode |
|---|---|
| References (`image`, `additional_images`, `@handles`), optionally `first_image` | Reference video: cast from the images |
| `first_image` only | The clip starts on the frame |
| Text only | Text to video |

- **Citing references**: Raspberry reads `Image 1`, `Image 2`... numbered in the order the images arrive. Mage sends your own `image` and `additional_images` first, then mentioned characters, then mentioned references (first-mention order), and rewrites `@mara` to `character from image 2`, `@denimjacket` to `outfit from image 3` (or `pose`, `location`, `object`). For your own images, write `Image 1` yourself. A first frame is not numbered.
- In reference mode, citing assets by number is the syntax; in first-frame and text clips, describe people by what they look like.
- **Voices**: a mentioned character's saved voice rides along with its image automatically (unless `use_character_voices: false`); nothing about it goes in the prompt. Write that character's lines and they come out in that voice. Write the lines in the same language as the voice sample.
- Up to 5 images in all: your images, characters and references together.
- `prompt_extend` is on unless you send `prompt_extend: false`: Raspberry then rewrites your prompt with its own model. `get_model` does not list it, but it passes through. Turn it off when you wrote the scene and its lines exactly. `negative_prompt` (up to 500 characters) passes through too.
- Sound is always generated.

## Prompt structure

**Reference video**: reference citation + action + scene + lines (optional) + music (optional).

```
<Who, by citation> <does what, in order> <where>. <Name> says: "<line>". <Music or "No background music.">
```

Two ways to place people: "Image 1 in Image 2" (the person from one image inside the place from another), or "the cat from Image 1 plays in the living room from Image 2".

**First frame**: the frame holds the look; write the motion, the camera and the sound.

**Text to video**: subject + scene + motion + light, shot size, angle, lens and camera move + style + sound.

**Several shots**: an overall sentence, then `Shot 1 [0-3s]: ...`, `Shot 2 [3-6s]: ...`. Raspberry reads the shot structure from prose and decides by itself when you do not say; start with `Generate single shot.` for one continuous take.

## Vocabulary

- **Light**: daylight, firelight, overcast, practical light, moonlight, mixed light; soft, hard, side, rim, backlight; dawn, sunset, night.
- **Shot size and angle**: close-up, medium close-up, medium, wide, establishing; eye level, over-the-shoulder, low, high, aerial.
- **Moves**: push in, pull back, tracking, orbit (under 45 degrees), fixed camera.
- **Styles**: realistic, 3D cartoon, claymation, puppet animation, pixel art.

## References, characters, and frames

- **One character per character image.** An image used for a main character must show only that person; crop group photos.
- **Places go in their own image.** Do not ask a character's image to supply the background; pass the location as a separate image and cite it.
- **Props**: their own image too, cited where they are used ("holds the guitar from Image 3").
- **First frame plus references**: the clip opens on the frame, and the references keep the people and props on model through the motion.
- **Storyboard sheet**: pass one multi-panel board as a reference and write the clip as shots. You need not describe every panel: give the key shots and Raspberry fills in the rest. One board per clip.

## Audio and dialogue

- **Lines**: `<Name> says: "..."`. Quoted lines are spoken as written; without any, Raspberry may improvise speech.
- **Several speakers**: a fixed label for each (the same citation or name every time, never "he" or "she" between lines), the speaker's action before the line, a voice description for a character with no saved voice ("in a raspy, deep voice"), and timing words between lines ("Then", "Immediately") so they do not overlap.
- **Silence**: "No dialogue." and "No background music."
- **Music and effects**: name the music's kind and mood ("a soothing country folk song"), and the sounds of the actions ("the guitar's strum, chair legs scraping").

## Text in the image

Text renders approximately. Keep any to a short quoted word on a sign and add anything that must be readable afterwards in an editor; otherwise write "No subtitles or on-screen text."

## Avoid

| Problem | Write instead |
|---|---|
| Two people blended into one | One person per character image, each cited separately |
| A background pulled from a portrait | A separate location image |
| Lines in a language the voice sample is not in | Lines in the voice's language |
| Pronouns between speakers' lines | The same label for a speaker every time |
| A wrong citation number | Recount: your images, then characters, then references |

## Examples

**Two saved characters, a prop and a place** (`@ines`, `@tomas` mentioned; `image` = guitar, `additional_images` = café; 10 s):

```
@ines sits on a stool in the café from Image 2, holding the guitar from Image 1, and plays a soothing country folk song. She says: "The sunshine is so nice today." @tomas walks past carrying two coffees, sets one on the table beside her, smiles and says: "That sounds lovely. Can you play it again?" Warm afternoon light through the front window, medium shot, slow push in.
```

Mage numbers this as: guitar image 1, café image 2, Ines image 3, Tomás image 4.

**One character, voice on, no music** (`@noor`, 6 s):

```
Generate single shot. @noor leans on a rain-streaked window in a dim apartment, turns to the camera and says quietly: "I'm not leaving tonight." Cool blue light from the street, a warm lamp behind her, medium close-up, fixed camera. Rain on the glass. No background music.
```

**From a first frame** (5 s):

```
She sets the teacup down, glances toward the door as it creaks open, and breaks into a smile. The camera pushes in slowly to a close-up. The door's creak, a soft clink of porcelain.
```
