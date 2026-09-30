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

## Behavior checks

For any skill, the agent should:

1. Quote the price in Gems before a batch or a video, and wait for a yes.
2. Ask for a link when the user attaches a file in a chat, instead of pretending Mage can read it.
3. Never invent product facts, results, reviews, or quotes.
4. Deliver links with short labels, and say they expire in 30 days.
