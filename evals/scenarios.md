# Trigger scenarios

Requests that should (✓) and should not (✗) load each skill. Use them to check a description change: paste each into an agent with only the skills installed, and note which skill it reaches for. Don't run the generations; stop at the quote.

## mage-generate
- ✓ "Make a picture of a fox in the snow."
- ✓ "Animate this image into a 5-second clip: <link>"
- ✓ "Make 30 seconds of lo-fi music."
- ✗ "Make product photos of my candle." → mage-product-photoshoot

## mage-characters
- ✓ "Save this photo as a character called Kai."
- ✓ "Keep the same face in all of these images."
- ✗ "Change the background of this photo." → mage-generate

## mage-product-photoshoot
- ✓ "Studio and lifestyle shots of my sneaker: <link>"
- ✓ "Make a Pinterest pin of my candle."
- ✗ "Amazon main image on white for my mug." → mage-marketplace-cards

## mage-marketplace-cards
- ✓ "Amazon listing images for this blender."
- ✓ "A+ content for my serum."
- ✗ "An Instagram carousel of my serum." → mage-product-photoshoot

## mage-ad-multiplier
- ✓ "Five variations of this ad with different models."
- ✓ "Ten headline variants of this ad."
- ✗ "Make this ad 9:16." → mage-ad-resizer

## mage-ad-resizer
- ✓ "Resize this ad for Stories and a banner."
- ✗ "Translate this ad into French." → mage-ad-localizer

## mage-ad-localizer
- ✓ "Spanish and German versions of this ad."
- ✗ "Translate this document." → not a Mage skill

## mage-ugc-video
- ✓ "A UGC review video of my protein bar."
- ✓ "Someone unboxing my product for TikTok."
- ✗ "A narrated video about the Roman Empire." → mage-faceless-video

## mage-faceless-video
- ✓ "A faceless YouTube Short about black holes."
- ✓ "A stickman video explaining inflation."
- ✗ "A thumbnail for my video about black holes." → mage-youtube-thumbnail

## mage-youtube-thumbnail
- ✓ "A MrBeast-style thumbnail for my video."
- ✓ "A Shorts cover with my face looking shocked."
- ✗ "Make the video itself." → mage-generate or mage-faceless-video

## mage-face-swap
- ✓ "Put the face from this photo onto this one: <link> <link>"
- ✗ "Swap her face in this video." → mage-video-face-swap

## mage-character-swap
- ✓ "Replace the person in this image with my character: <link> <link>"
- ✗ "Just change the face." → mage-face-swap

## mage-outfit-swap
- ✓ "Dress her in this outfit: <link> <link>"
- ✗ "Catalog shots of this jacket on a white background." → mage-product-photoshoot

## mage-inpaint
- ✓ "Remove the cup from the table in this photo: <link>"
- ✗ "Add more detail to the whole image." → mage-refine

## mage-refine
- ✓ "Fix the hands in this image: <link>"
- ✗ "Light it from the left instead." → mage-relight

## mage-relight
- ✓ "Relight this with warm, hard light from the upper left: <link>"
- ✗ "Show it from the side." → mage-angles

## mage-angles
- ✓ "Show this image from a low angle on the right: <link>"
- ✗ "Front, side, and back views of my character on one sheet." → mage-character-sheet

## mage-character-builder
- ✓ "Build a character: a woman with red wavy hair, green eyes, and freckles."
- ✗ "Save this photo as a character called Kai." → mage-characters

## mage-character-muse
- ✓ "Start from this image and try the Freckled and Mature faces: <link>"
- ✗ "Make a character with blue hair and an athletic build." → mage-character-builder

## mage-character-sheet
- ✓ "Make a character sheet from this image: <link>"
- ✗ "One back view of this scene." → mage-angles

## mage-recreate
- ✓ "What prompt would recreate this image? <link>"
- ✗ "Fix the eyes in this image." → mage-refine

## mage-video-editor
- ✓ "Change her jacket to red leather in this clip: <link>"
- ✗ "Put my character's face on the person in this clip." → mage-video-face-swap

## mage-video-face-swap
- ✓ "Swap @nova's face into this video: <link>"
- ✗ "Replace the whole person, outfit and all." → mage-video-character-swap

## mage-video-character-swap
- ✓ "Replace the dancer in this video with @nova: <link>"
- ✗ "Make @nova dance to this song." → mage-music-video

## mage-lipsync
- ✓ "Make this portrait say this audio: <link> <link>"
- ✗ "A UGC review video of my protein bar." → mage-ugc-video

## mage-music-video
- ✓ "Make @nova and @kai perform this track: <link>"
- ✗ "Make @nova read this voiceover." → mage-lipsync

## mage-scene-builder
- ✓ "A dinner date scene with @nova and @kai."
- ✗ "A video of @nova walking on a beach." → mage-generate

## Behavior checks

For any skill, the agent should:

1. Quote the price in Gems before a batch or a video, and wait for a yes.
2. Ask for a link when the user attaches a file in a chat, instead of pretending Mage can read it.
3. Never invent product facts, results, reviews, or quotes.
4. Deliver links with short labels, and say they expire in 30 days.
5. In the app skills, send the app's prompt word for word and start from the app's default model and settings.
