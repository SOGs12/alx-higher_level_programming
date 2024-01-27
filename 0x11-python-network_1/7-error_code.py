#!/usr/bin/python3
"""Display response body
"""

import requests
from sys import argv

if __name__ == '__main__':

    url = argv[1]

    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError as err:
        print('Error code: {}'.format(err.response.status_code))
