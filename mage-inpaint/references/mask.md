# Painting the mask

The Inpaint app sends one image: the original with the region to change painted over in red at 50% opacity, at the original's full size, saved as a JPEG at maximum quality. This script makes the same image. It needs Python with Pillow (`pip install pillow`).

```python
#!/usr/bin/env python3
"""mask.py SOURCE OUTPUT SHAPE [SHAPE ...]

Paint red at 50% opacity over regions of SOURCE and save OUTPUT as a JPEG.
A SHAPE is rect:x1,y1,x2,y2 or ellipse:x1,y1,x2,y2 or poly:x1,y1,x2,y2,x3,y3,...
with every coordinate a fraction of the width (x) or height (y), from 0 to 1.
"""
import sys

from PIL import Image, ImageDraw, ImageOps

source, output, shapes = sys.argv[1], sys.argv[2], sys.argv[3:]
image = ImageOps.exif_transpose(Image.open(source)).convert("RGB")
width, height = image.size
mask = Image.new("L", image.size, 0)
draw = ImageDraw.Draw(mask)
for shape in shapes:
    kind, _, numbers = shape.partition(":")
    values = [float(n) for n in numbers.split(",")]
    points = [(values[i] * width, values[i + 1] * height) for i in range(0, len(values), 2)]
    if kind == "rect":
        draw.rectangle(points, fill=128)
    elif kind == "ellipse":
        draw.ellipse(points, fill=128)
    elif kind == "poly":
        draw.polygon(points, fill=128)
    else:
        sys.exit(f"unknown shape: {kind}")
red = Image.new("RGB", image.size, (255, 0, 0))
Image.composite(red, image, mask).save(output, "JPEG", quality=100, subsampling=0)
print(f"{output}: {width}x{height}")
```

```bash
python3 mask.py photo.jpg masked.jpg ellipse:0.08,0.70,0.42,0.90
```

It prints the image's width and height, which also give the aspect ratio.

## Choosing the region

- Look at the image and place the shape yourself from what the user described ("the cup", "his left hand"). Coordinates are fractions: `0,0` is the top-left corner and `1,1` the bottom-right.
- Mask a little wider than the object, about 10% on every side, so the model has room to blend. Masking too tightly is the most common mistake.
- Include whatever has to be redrawn with it: the fingers around a held object, a shadow, a reflection.
- Measure the region on this image. The coordinates in the example above are only an example.
- Use an ellipse for hands, faces, and round objects, a rectangle for signs and screens, a polygon for anything awkward. Several shapes can go in one call.
- Open `masked.jpg` and check the red covers the whole object before uploading. Adjust and rerun if it doesn't.
- If the user gave a mask of their own (white on black, same size as the image), composite that instead: `Image.composite(red, image, user_mask.convert("L").point(lambda v: 128 if v > 127 else 0))`.

## Uploading it

Pass the masked image as a data URL when the file is under about 3 MB. Otherwise call `create_upload` with `content_type: "image/jpeg"`, PUT the file to `upload_url` with exactly the returned `headers`, and pass the returned `url` as `image`:

```bash
curl -X PUT -T masked.jpg -H 'Content-Type: image/jpeg' \
  -H 'x-goog-content-length-range: 0,104857600' '<upload_url>'
```
