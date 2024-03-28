#!/bin/bash

# Function to test a method and report success/failure
function test_method() {
  local method="$1"
  response=$(curl -s -o /dev/null -w "%{http_code}" -X "$method" "$url")
  if [[ $response -ge 200 && $response -lt 300 ]]; then
    echo "  * $method (Success: $response)"
  fi
}

# Check if a URL argument is provided
if [ -z "$1" ]; then
  echo "Error: Please provide a URL as an argument."
  exit 1
fi

# Define the URL from the argument
url="$1"

# List of common HTTP methods to test
methods=(GET HEAD POST PUT DELETE PATCH OPTIONS)

echo "Testing supported HTTP methods for $url:"

# Loop through each method and call the test function
for method in "${methods[@]}"; do
  test_method "$method"
done

# Informative message if no methods were successful
if [[ -z "$(echo "$methods")" ]]; then
  echo "Warning: No successful responses received for any method."
fi
