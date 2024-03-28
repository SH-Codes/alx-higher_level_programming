#!/bin/bash

# Check if URL is provided
[ -z "$1" ] && { echo "Usage: $0 <URL>"; exit 1; }

# Send POST request with specified data and display response body
curl -s -X POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
