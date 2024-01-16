#!/bin/bash

# Replace this path with the path to the specific folder
FOLDER_PATH="/Users/jerin/Documents/Projects"

# Initialize a counter
COUNT=0

echo "🔍 Searching Flutter Projects in $FOLDER_PATH"

# Save the current directory
CURRENT_DIR=$(pwd)

# Find each pubspec.yaml file and run flutter clean in its directory
find "$FOLDER_PATH" -name 'pubspec.yaml' | while read file; do
    COUNT=$((COUNT+1))
    DIR=$(dirname "$file")
    echo "🧹 $COUNT) Running 'flutter clean' in $DIR"
    cd "$DIR"
    flutter clean
    cd "$CURRENT_DIR"
    echo -e "-----------------\n"
done

# Print the count
echo "✅ Found $COUNT Flutter Projects!"
