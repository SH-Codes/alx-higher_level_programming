#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request

def get_x_request_id(url):
    """Fetches and returns the X-Request-Id header value for the given URL."""
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        return response.headers.get("X-Request-Id")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    x_request_id = get_x_request_id(url)
    if x_request_id:
        print(x_request_id)
    else:
        print("X-Request-Id header not found in the response.")

