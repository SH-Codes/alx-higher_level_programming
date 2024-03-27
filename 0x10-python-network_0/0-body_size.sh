#!/bin/bash

# Check if URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to URL and get the size of the response body in bytes
response=$(curl -sI "$1")
if [ -z "$response" ]; then
    echo "Error: Unable to retrieve response from the server."
    exit 1
fi

# Check if Content-Length header exists in the response
content_length=$(echo "$response" | grep -i 'Content-Length' | awk '{print $2}' | tr -d '\r')
if [ -z "$content_length" ]; then
    echo "Error: Content-Length header not found in the response."
    echo "Response body:"
    echo "$response"
    exit 1
fi

echo "Size of the response body: $content_length bytes"

