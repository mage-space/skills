# Media inputs

## Where inputs come from

| Source | How to pass it |
|---|---|
| A public link to the file itself | The https URL, as is. Mage downloads it (60 s, 3 redirects, 100 MB). |
| A small local image (under about 3 MB) | A data URL: `data:image/png;base64,...`. |
| A larger local file, on a machine where you can run commands | `create_upload` with the file's `content_type`, then PUT the file to `upload_url` with exactly the returned `headers`, then pass the returned `url`. |
| An earlier Mage result | Its `result.url`. |
| A saved character or reference | `@handle` in the prompt, not a field. |
| A file attached to the chat | Not possible: it never reaches Mage. Ask for a direct link, or use a shell and `create_upload`. |

Formats: images JPEG or PNG; video MP4, MOV, or WebM; audio MP3 or WAV. Inputs and results are deleted after 30 days.

Upload example:

```bash
curl -X PUT -T clip.mp4 \
  -H 'Content-Type: video/mp4' \
  -H 'x-goog-content-length-range: 0,104857600' \
  '<upload_url>'
```

## Fields by model

| Model | Reference images | Frames | Source video |
|---|---|---|---|
| Mango, Guava, GPT Image 2.5 Flare | `image`, `additional_images` | none | none |
| Cherry (all variants) | `image`, `additional_images` | none | `videos` |
| Lemon | `image`, `additional_images` | `first_image`, `last_image` | `videos` |
| Seed Audio | `image` (one) | none | none |

`get_model` returns the exact fields (`image_inputs`, `video_inputs`) and the image budget (`max_images`), which characters and references mentioned in the prompt share.

## Patterns

- **Edit an image:** pass it in `image` with Mango 3 and describe only the change. Mango 3 keeps everything else in place.
- **Combine images:** put each in `image` / `additional_images` and name them in the prompt with `@image1`, `@image2`: "The model from @image1 holding the bag from @image2 on the street from @image3."
- **Image to video, exact first frame:** Lemon with `first_image`, and optionally `last_image` for where it ends.
- **Image to video, highest quality:** Cherry 2 Pro with the image in `image`. The clip follows the reference but does not start on it pixel for pixel.
- **Edit a video:** Cherry 2 Pro or Lemon with the clip in `videos`, and a prompt describing the change ("Change her jacket to red leather. Keep the motion, framing, and timing."). The price depends on the clip's length, measured on submit; `estimate_cost` answers `requires_media_measurement`.
- **Score a picture:** Seed Audio with the image in `image` and a prompt for the kind of sound.
