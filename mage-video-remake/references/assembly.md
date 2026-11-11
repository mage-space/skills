# Cutting the remake to the original's timeline

Download each result into `remake/` first (`curl -L -o remake/shot01.mp4 "<url>"`). Shot times come from `breakdown/ref/reel/timeline.md`: `#03 2.8-3.9` is shot 3, from 2.8 to 3.9 seconds. The examples are for 1080×1920 at 30 fps; use the original's size and frame rate (`REEL.md`'s `source`).

## 1. One clip per shot, at the shot's length

Count in frames, so the cuts land where the original's did: a shot from 2.8 s to 3.9 s at 30 fps runs from frame 84 to frame 117, so 33 frames. Pick the in-point inside the generated clip (where the action starts), and keep each clip's sound when it has dialogue:

```bash
ffmpeg -i remake/shot03.mp4 -vf "fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,trim=start_frame=6:end_frame=39,setpts=PTS-STARTPTS" \
  -af "atrim=start=0.2:end=1.3,asetpts=PTS-STARTPTS" -c:v libx264 -crf 17 -pix_fmt yuv420p -c:a aac -ar 48000 -ac 2 cut/03.mp4
```

- Never speed a clip up or slow it down to fit: trim it, or regenerate it longer.
- A clip without sound needs a silent track so every piece joins the same way: add `-f lavfi -i anullsrc=r=48000:cl=stereo` as a second input and `-shortest`, as in the still below.
- Several shots from one generated clip: cut each from its own start frame.
- A still with a push (a Mango 4 still for a 3-second shot):

  ```bash
  ffmpeg -loop 1 -i remake/still05.png -f lavfi -i anullsrc=r=48000:cl=stereo \
    -vf "scale=2160:-2,zoompan=z='min(zoom+0.0015,1.15)':d=90:s=1080x1920:fps=30" \
    -t 3 -c:v libx264 -crf 17 -pix_fmt yuv420p -c:a aac -shortest cut/05.mp4
  ```

## 2. Join them

```bash
for f in cut/*.mp4; do echo "file '$PWD/$f'"; done > cut/list.txt
ffmpeg -f concat -safe 0 -i cut/list.txt -c:v libx264 -crf 17 -pix_fmt yuv420p -c:a aac joined.mp4
```

The joined length should equal the original's, within a frame: `ffprobe -v error -show_entries format=duration -of csv=p=0 joined.mp4`.

## 3. Captions in the original's style

`breakdown/ref/packaging/subtitles.srt` has the original's caption times; `overlays.ass` has every text layer with its position, colors, outline, and entrance, at the original's size. Copy it, delete the lines that were part of the picture (text on a screen or a package), replace the rest with the user's words (the same length or shorter), and set an open-licensed font you have installed in place of `Sans`:

```bash
cp breakdown/ref/packaging/overlays.ass captions.ass   # edit the Dialogue lines' text and the Style's font
ffmpeg -i joined.mp4 -vf "ass=captions.ass" -c:v libx264 -crf 17 -pix_fmt yuv420p -c:a copy captioned.mp4
```

Keep captions out of the platform's buttons: on 1080×1920, between y 250 and y 1500 and at least 60 px from the sides.

## 4. Music and sound

Music only:

```bash
ffmpeg -i captioned.mp4 -i remake/music.mp3 -filter_complex "[1:a]atrim=0:21.0,afade=t=out:st=20.0:d=1[m]" \
  -map 0:v -map "[m]" -c:v copy -c:a aac -shortest final.mp4
```

Dialogue with music under it, the music dipping while people talk:

```bash
ffmpeg -i captioned.mp4 -i remake/music.mp3 -filter_complex \
  "[1:a]atrim=0:21.0,volume=0.5[m];[m][0:a]sidechaincompress=threshold=0.05:ratio=8:release=300[duck];[0:a][duck]amix=inputs=2:duration=first:normalize=0[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac final.mp4
```

Sound effects go in at their times from `reel/sound.md` with `adelay` (milliseconds) before the mix: `[2:a]adelay=4420|4420[fx1]`.

## 5. Check it against the original

```bash
ffmpeg -i video.mp4 -i final.mp4 -filter_complex "[0:v]scale=-2:960[a];[1:v]scale=-2:960[b];[a][b]hstack" -an compare.mp4
rea-video decompose final.mp4 -o breakdown/remake --lang en --no-stems
```

Compare `breakdown/remake/reel/timeline.md` with the original's: the same number of shots, cuts within a frame of the original's times, captions at the same moments. Look at `compare.mp4` for the hook's first two seconds especially. Tell the user where the remake differs on purpose.
