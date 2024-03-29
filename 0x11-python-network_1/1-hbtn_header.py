#!usr/bin/python3

import urllib.request
import sys

# Get the URL from the command-line argument
url = sys.argv[1]

# Open the URL connection using a with statement
with urllib.request.urlopen(url) as response:
 # Retrieve the response headers
 headers = response.info()

 # Extract the X-Request-Id value from the headers
 x_request_id = headers.get("X-Request-Id")

 # Print the X-Request-Id value
 print("X-Request-Id:", x_request_id)
