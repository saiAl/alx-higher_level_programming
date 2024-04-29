#!/bin/bash
# displays all HTTP methods the server will accept
res=$(curl -sI 0.0.0.0:5000/route_4 | grep "^Allow" | cut -d ':' -f 2 | xargs) && echo "$res"
