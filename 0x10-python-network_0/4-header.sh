#!/bin/bash
# send a REQUEST with custom header
curl -H "X-School-User-Id: 98" -s "$1"
