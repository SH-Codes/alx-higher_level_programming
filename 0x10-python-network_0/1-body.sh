#!/bin/bash
# Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

# Uses curl to send a GET request to the provided URL
# -s: Silent mode, hides the progress meter
# -L: Follow redirects if the server redirects the request
# "$1": Takes the first argument provided to the script as the URL
curl -sL "$1"
