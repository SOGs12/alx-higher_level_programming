#!/usr/bin/python3
"""Display response body
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    r = None  # Initialize the variable

    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        if r:
            print(f'Error code: {r.status_code}')
