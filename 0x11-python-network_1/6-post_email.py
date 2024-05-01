#!/usr/bin/python3
"""Script that snds a POST request to the passed URL with the
    email as a parameter
    Usage: ./6-post_email.py <url> <email>
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    req = requests.post(url, data=data)
    print(req.text)
