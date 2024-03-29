#!/usr/bin/env python3
"""
Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""

import sys
import urllib.request
from urllib.error import URLError


def get_x_request_id(url):
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            x_request_id = response.headers.get("X-Request-Id")
            if x_request_id:
                return x_request_id
            else:
                return "X-Request-Id header not found in the response."
    except URLError as e:
        return f"Error occurred: {e}"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    x_request_id = get_x_request_id(url)
    print(x_request_id)
