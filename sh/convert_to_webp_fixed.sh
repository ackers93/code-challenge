2#!/bin/bash

# Convert all JPG images to WebP format while preserving orientation
echo "Converting images to WebP format with orientation preservation..."

# Convert all .jpg files
for file in *.jpg; do
    if [ -f "$file" ]; then
        echo "Converting $file to WebP..."
        magick "$file" -auto-orient -quality 85 "${file%.jpg}.webp"
    fi
done

# Convert all .JPG files
for file in *.JPG; do
    if [ -f "$file" ]; then
        echo "Converting $file to WebP..."
        magick "$file" -auto-orient -quality 85 "${file%.JPG}.webp"
    fi
done

echo "Conversion complete! All images have been converted to WebP format with proper orientation." 