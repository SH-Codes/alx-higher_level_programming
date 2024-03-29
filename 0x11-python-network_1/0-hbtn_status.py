#!/usr/bin/python3
import urllib.request

# Define the target URL
url = "https://alx-intranet.hbtn.io/status"

# Open the URL connection using a with statement
with urllib.request.urlopen(url) as response:
    # Read the response body
    data = response.read().decode("utf-8")
# Display the response body with a tab before '-'
for line in data.splitlines():
    print("\t-", line)
