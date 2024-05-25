#!/bin/bash

# Define the target directory
TARGET_DIR="./pngs"

# Create the target directory if it does not exist
mkdir -p "$TARGET_DIR"

# Create 20 empty .png files
for i in {1..20}
do
  touch "$TARGET_DIR/empty_$i.png"
done

echo "20 empty .png files have been created in $TARGET_DIR."