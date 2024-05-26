#!/bin/bash

# Define the path to your Python script and the ID file
PYTHON_SCRIPT="newMovies.py"
ID_FILE="moviesID.txt"

# Check if the ID file exists
if [[ ! -f "$ID_FILE" ]]; then
  echo "ID file not found!"
  exit 1
fi

# Read the ID file line by line and pass each ID to the Python script
while IFS= read -r id
do
  python3 "$PYTHON_SCRIPT" "$id"
done < "$ID_FILE"
