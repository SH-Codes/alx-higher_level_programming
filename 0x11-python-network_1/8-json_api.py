#!/usr/bin/env python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.
Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
import sys
import requests

def main():
    if len(sys.argv) > 2:
        print("Usage: ./8-json_api.py <letter>")
        sys.exit(1)

    letter = sys.argv[1] if len(sys.argv) == 2 else ""
    payload = {"q": letter}

    try:
        response = requests.post("http://0.0.0.0:5000/search_user", data=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors

        json_response = response.json()
        if not json_response:
            print("No result")
        else:
            print("[{}] {}".format(json_response.get("id"), json_response.get("name")))
    except requests.RequestException as e:
        print(f"Error occurred: {e}")
        sys.exit(1)
    except ValueError:
        print("Not a valid JSON")
        sys.exit(1)

if __name__ == "__main__":
    main()
