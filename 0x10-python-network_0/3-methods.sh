#!/usr/bin/bash
# Display all HTTP methods allowed by the provided URL

# Check if URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a HEAD request to the provided URL using curl
# -s: Silent mode, hides the progress meter
# -I: Send a HEAD request instead of a GET request, to retrieve only the headers
# "$1": Takes the first argument provided to the script as the URL
# Then grep extracts the "Allow" header, which lists allowed HTTP methods
# Finally, awk is used to print all HTTP methods listed in the header
curl -sI "$1" | grep -i "Allow" | awk '{print substr($0, index($0,$2))}'
