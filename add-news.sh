#!/bin/bash

# FUSS News Creator Script
# Usage: ./add-news.sh "News Title" "Summary text"

if [ $# -lt 2 ]; then
    echo "Usage: $0 \"News Title\" \"Summary text\""
    echo "Example: $0 \"New Research Paper\" \"We published a paper on formal verification\""
    exit 1
fi

TITLE="$1"
SUMMARY="$2"
DATE=$(date +%Y-%m-%d)
FILENAME=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd '[:alnum:]-')

cat > "content/news/$DATE-$FILENAME.md" << EOF
---
title: "$TITLE"
date: $DATE
draft: false
tags: ["news"]
summary: "$SUMMARY"
---

$SUMMARY

<!-- Add more content here as needed -->
EOF

echo "Created news article: content/news/$DATE-$FILENAME.md"
echo "You can now edit the file to add more detailed content."
