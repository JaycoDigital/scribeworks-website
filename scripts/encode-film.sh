#!/usr/bin/env sh
# Re-encode the fit-out master for the scroll-scrubbed film section.
# Keyframe every 6 frames keeps seeks instant; CRF 19 is visually lossless
# (PSNR ~50 dB vs master) at roughly a fifth of the master's size.
set -e
cd "$(dirname "$0")/.."
ffmpeg -y -i media-src/fit-out-master.mp4 -an \
  -c:v libx264 -profile:v high -pix_fmt yuv420p \
  -x264-params keyint=6:min-keyint=6:scenecut=0 \
  -crf 19 -preset slow -movflags +faststart \
  public/media/fit-out-scrub.mp4
