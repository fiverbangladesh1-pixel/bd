#!/bin/bash
# usage: sheet.sh name t1 t2 ... (up to 5)
n=$1; shift; node render.js stills $(IFS=,; echo "$*") || exit 1
ins=""; for t in "$@"; do ins="$ins -i out/s_$t.jpg"; done
ffmpeg -v error -y $ins -filter_complex "hstack=inputs=$#,scale=-1:900" out/sheet_$n.jpg
