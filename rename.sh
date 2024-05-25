#!/bin/bash

# Check if the correct number of arguments is passed
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 target_pattern zero_padding_width"
    echo "Example: $0 Comp_%n.png 4"
    exit 1
fi

target_pattern=$1
zero_padding_width=$2

# Check if there are any files in the directory
if [ "$(ls -A)" ]; then
    counter=1
    for file in *; do
        # Skip if it is a directory
        if [ -d "$file" ]; then
            continue
        fi

        # Extract the file extension
        extension="${file##*.}"
        # Replace %n in the target pattern with the formatted counter
        formatted_counter=$(printf "%0${zero_padding_width}d" "$counter")
        new_file=$(printf "%s" "$target_pattern" | sed "s/%n/$formatted_counter/")
        # Ensure the new filename includes the original extension
        if [[ $new_file != *".${extension}" ]]; then
            new_file="${new_file}.${extension}"
        fi
        mv "$file" "$new_file"
        echo "Renamed: $file -> $new_file"
        counter=$((counter + 1))
    done
else
    echo "No files found in the directory."
fi