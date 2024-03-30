#!/usr/bin/env python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.
Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

def main():
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <GitHub username> <GitHub password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    try:
        response = requests.get("https://api.github.com/user", auth=HTTPBasicAuth(username, password))
        response.raise_for_status()  # Raise an exception for HTTP errors

        user_data = response.json()
        print(user_data.get("id"))
    except requests.RequestException as e:
        print(f"Error occurred: {e}")
        sys.exit(1)
    except ValueError:
        print("Not a valid JSON")
        sys.exit(1)

if __name__ == "__main__":
    main()
