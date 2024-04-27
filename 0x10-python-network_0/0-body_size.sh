#!/usr/bin/bash
# Bash script that takes in a URL, sends a request to that URL

body=$(curl -sI "$1" | grep -i Content-Length)
len=$(echo "$body" | grep -o -E '[0-9]+')
echo "$len"
