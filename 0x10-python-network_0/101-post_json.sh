#!/bin/bash
# Sent json data
curl -X POST -H "Content-Type: application/json" "$1" -d @"$2"
