#!/bin/bash
# displays all HTTP methods the server will accept
body=$(curl -s -i -X OPTION "$1" | grep "Allow:") && echo "${body#*Allow: }"
