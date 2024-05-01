#!/usr/bin/python3
"""Script that sends a request to a URL and displays the body of
    the response (decoded in utf-8).
"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError


if __name__ == '__main__':
    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req) as respose:
            hbtn_read = response.read()
            print(hbtn_read.decode('ascii'))
    except HTTPError as e:
        print(f'Error code: {e.code}')
