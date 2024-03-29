#!/bin/bash

# Check if a URL argument is provided
if [ -z "$1" ]; then
  echo "Error: Please provide a URL as an argument."
  exit 1
fi

# Define the URL from the argument
url="$1"

# Set the header value
header_name="X-School-User-Id"
header_value="98"

# Send GET request with header using curl
response=$(curl -s -H "$header_name: $header_value" "$url")

# Check for errors
if [[ $? -ne 0 ]]; then
  echo "Error: Failed to send GET request to $url."
  exit 1
fi

# Display the response body
echo "Response body:"
echo "$response"
