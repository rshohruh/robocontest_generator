#!/bin/bash

# Prompt the user to enter the source directory
echo "Enter the source directory:"
read source_dir

# Verify if the entered directory exists
if [ ! -d "$source_dir" ]; then
    echo "Error: Source directory does not exist."
    exit 1
fi

# Set the destination directory
destination_dir="/home/rshohruh/Downloads/robocontest_generator/tests"

# Counter variable
counter=0

# Loop through each .in file in the source directory
for file in "$source_dir"/*.in; do
    # Increment the counter
    ((counter++))
    # Pad the counter with leading zeros
    padded_counter=$(printf "%03d" "$counter")
    # Get the file extension
    extension="${file##*.}"
    # Create the new filename
    new_filename="${padded_counter}.${extension}"
    # Copy the file to the destination directory with the new filename
    cp "$file" "${destination_dir}/${new_filename}"
done
