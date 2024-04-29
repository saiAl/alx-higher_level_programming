#!/bin/bash
# send POST request with data
curl --data-urlencode "email=test@gmail.com" --data-urlencode "subject=I will always be here for PLD" "$1"
