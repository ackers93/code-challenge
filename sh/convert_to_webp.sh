#!/bin/bash

# Convert all JPG images to WebP format
echo "Converting images to WebP format..."

# Convert all .jpg files
for file in *.jpg; do
    if [ -f "$file" ]; then
        echo "Converting $file to WebP..."
        convert "$file" -quality 85 "${file%.jpg}.webp"
    fi
done

# Convert all .JPG files
for file in *.JPG; do
    if [ -f "$file" ]; then
        echo "Converting $file to WebP..."
        convert "$file" -quality 85 "${file%.JPG}.webp"
    fi
done

echo "Conversion complete! All images have been converted to WebP format."
echo "Original JPG files are preserved. You can delete them manually if needed." 