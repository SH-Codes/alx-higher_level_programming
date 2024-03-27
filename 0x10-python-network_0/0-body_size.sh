#!/bin/bash

# Check if URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to URL and count the size of the response body in bytes
curl_output=$(curl -s "$1")
byte_count=$(echo -n "$curl_output" | wc -c)

echo "$byte_count"
