#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL
curl -sI "$1" | grep -i Content-Length | grep -o -E '[0-9]+'
