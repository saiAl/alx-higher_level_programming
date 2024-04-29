#!/bin/bash
# displays all HTTP methods the server will accept
res=$(curl -sI "$1" | grep "^Allow" | cut -d ':' -f 2 | xargs) && echo "$res"
