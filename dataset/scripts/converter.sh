#!/bin/bash

input="data/video/30_FPS/*"
fps=15

while getopts "p:r:" flag; do
    case "$flag" in
        p) path="$OPTARG";;
        r) fps="$OPTARG";;
    esac
done

for directory in $input; do
    if [ -d "$directory" ]; then
        subdirectory_name="${directory##*/}"

        mkdir -p "${path}/${subdirectory_name}"

        for file in "$directory"/*; do
            filename="${file##*/}"
            output_file="${path}/${subdirectory_name}/${filename}"

            if [ ! -f "$output_file" ]; then
                ffmpeg -i "$file" -filter:v fps=$fps "$output_file"
            fi
        done
    fi
done
