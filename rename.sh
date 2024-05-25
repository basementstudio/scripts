#!/bin/bash

# Default zero padding width
zero_padding_width=2

# Parse arguments
while getopts ":z:" opt; do
    case $opt in
        z) zero_padding_width=$OPTARG ;;
        \?) echo "Invalid option -$OPTARG" >&2; exit 1 ;;
    esac
done
shift $((OPTIND -1))

# Check if the correct number of arguments is passed
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 [-z zero_padding_width] src_path target_pattern"
    echo "Example: $0 -z 4 /path/to/source /path/to/destination/Comp_%n.png"
    exit 1
fi

src_path=$1
target_pattern_with_path=$2

# Check if the source directory exists
if [ ! -d "$src_path" ]; then
    echo "Source directory does not exist: $src_path"
    exit 1
fi

# Extract the directory path from the target pattern
target_directory=$(dirname "$target_pattern_with_path")

# Check if the target directory exists
if [ ! -d "$target_directory" ]; then
    echo "Target directory does not exist: $target_directory"
    exit 1
fi

# Extract the target pattern without the path
target_pattern=$(basename "$target_pattern_with_path")

# Check if there are any files in the source directory
if [ "$(ls -A "$src_path")" ]; then
    counter=1
    for file in "$src_path"/*; do
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
        # Move the file to the target directory with the new name
        mv "$file" "${target_directory}/${new_file}"
        echo "Renamed and moved: $file -> ${target_directory}/${new_file}"
        counter=$((counter + 1))
    done
else
    echo "No files found in the source directory."
fi