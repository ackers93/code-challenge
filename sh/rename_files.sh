#!/bin/bash

# Change to the portfolio directory
cd /Users/ackers/Desktop/code/VCWD/pineworks-construction/src/assets/portfolio

# Create an array of all image files sorted by name
files=($(ls -1 *.jpg *.JPG | sort))

# Counter for new filenames
counter=1

# Rename each file
for file in "${files[@]}"; do
    # Get the file extension
    extension="${file##*.}"
    
    # Create new filename with leading zeros
    new_name=$(printf "%03d.%s" $counter $extension)
    
    # Rename the file
    mv "$file" "$new_name"
    echo "Renamed $file to $new_name"
    
    # Increment counter
    ((counter++))
done

echo "All files renamed successfully!" 