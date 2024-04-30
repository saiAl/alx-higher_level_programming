#!/bin/bash
# Sent json data
curl -X POST -H "Content-Type: application/json" -s "$1" -d @"$2"
