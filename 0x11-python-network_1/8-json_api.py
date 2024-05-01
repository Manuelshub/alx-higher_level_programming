#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to a URL with
the letter as parameter.
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        data = {'q': ""}
    else:
        data = {'q': sys.argv[1]}
    req = requests.post(url, data=data)

    try:
        r = req.json()
        if r == {}:
            print("No result")
        else:
            print(f"[{r.get('id')}] {r.get('name')}")
    except ValueError:
        print("Not a valid JSON")
