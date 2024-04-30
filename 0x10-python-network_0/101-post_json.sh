#!/bin/bash
# Sent json data
url="$1"; file="$2"; curl -X POST -H "Content-Type: application/json" -d "$file" -s "$url"
