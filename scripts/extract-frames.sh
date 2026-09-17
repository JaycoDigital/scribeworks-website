#!/usr/bin/env sh
# Extract the fit-out clip as WebP frame sequences for the scroll-driven
# canvas (src/components/home/Film.astro). Two sizes: large for desktop,
# small for phones. The clip's last third is a still frame, so we take the
# first 6.5s at 24fps and append the final frame. ffmpeg writes PNG, Pillow
# converts to WebP (this ffmpeg build has no libwebp).
set -e
cd "$(dirname "$0")/.."
SRC=media-src/fit-out-master.mp4
TMP=$(mktemp -d)
ffmpeg -v error -y -i "$SRC" -t 6.5 "$TMP/%03d.png"
last=$(ls "$TMP" | sort | tail -1 | sed 's/\.png//')
next=$(printf '%03d' $((10#$last + 1)))
ffmpeg -v error -y -sseof -0.05 -i "$SRC" -frames:v 1 "$TMP/$next.png"
python3 - "$TMP" <<'PY'
import sys, os, glob
from PIL import Image
tmp = sys.argv[1]
sets = {'lg': (1920, 76), 'sm': (960, 74)}
for name, (w, q) in sets.items():
    out = f'public/media/frames/{name}'
    os.makedirs(out, exist_ok=True)
    for f in os.listdir(out): os.remove(os.path.join(out, f))
    total = 0
    for i, src in enumerate(sorted(glob.glob(f'{tmp}/*.png'))):
        im = Image.open(src).convert('RGB')
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        dst = f'{out}/{i:03d}.webp'
        im.save(dst, 'WEBP', quality=q, method=6)
        total += os.path.getsize(dst)
    print(f'{name}: {i+1} frames, {total/1048576:.1f} MB, {im.size[0]}x{im.size[1]}')
PY
rm -rf "$TMP"
