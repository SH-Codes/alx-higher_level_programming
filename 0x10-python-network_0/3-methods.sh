#!/usr/bin/bash
# Display all http methods

# Uses curl to send a HEAD request to the provided URL
# -s: Silent mode, hides the progress meter
# -I: Send a HEAD request instead of a GET request, to retrieve only the headers
# "$1": Takes the first argument provided to the script as the URL
# Then grep extracts the "Allow" header, which lists allowed HTTP methods
# Finally, cut is used to extract the HTTP methods from the header
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
