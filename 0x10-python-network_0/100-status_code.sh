#!/bin/bash
# displays only the status code of the response
curl -o /dev/null -sI -w "%{http_code}" "$1"
