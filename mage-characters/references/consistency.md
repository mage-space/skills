# Consistency across a set

## Keep these fixed

- **Handles.** Use the same `@handle` every time; don't re-describe the face in words, which fights the reference.
- **Style line.** Write one style sentence ("warm film photograph, 35mm, soft natural light") and repeat it verbatim in every prompt.
- **Aspect ratio and model.** A set made with one model and ratio looks like one shoot.
- **Wardrobe.** Save the outfit as an `outfit` reference and mention it, or describe it identically each time.

## Vary these

- The action, the location, the camera angle, the time of day. One change per image reads clearest.

## Patterns

- **Storyboard:** number the scenes and generate them in one batch with the same handles and style line.
- **Same character, many outfits:** save each outfit as a reference: "@nova wearing @blazer", "@nova wearing @raincoat".
- **Two characters together:** name both and place them: "@nova on the left laughing, @kai on the right holding two coffees."
- **Character in a video:** Cherry 2 Pro with the handle in the prompt. Give them a single clear action and, if they speak, the exact words in quotes.
- **Match an earlier image exactly:** pass that result's URL in `image` alongside the handle, and say "same setting and lighting as @image1".

## When identity drifts

- Use Mango 3 rather than a cheaper variant.
- Make the face bigger in frame: medium close-up instead of a wide shot.
- Remove competing people from the prompt.
- Replace the saved portrait with a clearer one: delete the character and create it again with a better image (the handle becomes free once deleted).
