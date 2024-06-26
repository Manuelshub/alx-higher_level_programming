#!/usr/bin/python3
"""
Script that takes my github credentials and uses Github API to
display my id.
"""
from requests.auth import HTTPBasicAuth
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    data = response.json()
    print(data.get("id"))
