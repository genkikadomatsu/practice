#!/bin/bash

# Read user input for the file name
echo "Enter the problem number:"
read filename

# Add ".py" extension to the file name
filename="$filename.py"

# Check if the file exists
if [ -e "$filename" ]; then
  echo "File '$filename' already exists."
else
  # Create the file
  touch "$filename"
  echo "File '$filename' created."
fi
echo "Opening '$filename' in VSCode..."
code $filename
