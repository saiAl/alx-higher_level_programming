#!/usr/bin/bash
#  script that takes in a URL, sends a GET request to the URL
# and displays the body of the response

body=$(curl -sL "$1")
echo "$body"