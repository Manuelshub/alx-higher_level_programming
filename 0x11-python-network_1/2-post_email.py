#!/usr/bin/python3
"""Script that sends a POST request to the passed URL with the
    email as a parameter.
    Usage: ./2-post_email.py <url> <email>
"""
import sys
import urllib.parse
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    data = {}
    data['email'] = sys.argv[2]
    url_values = urllib.parse.urlencode(data).encode('ascii')

    req = urllib.request.Request(url, url_values)
    with urllib.request.urlopen(req) as response:
        hbtn_page = response.read()
        print(hbtn_page.decode('utf-8'))
