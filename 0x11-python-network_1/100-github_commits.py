#!/usr/bin/python3
"""
Script that prints the commit hash and the committer
"""
from requests.auth import HTTPBasicAuth
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)
    datas = response.json()

    count = 0
    for data in datas:
        if count == 10:
            break
        sha = data.get('sha')
        committer = data['commit']['author'].get('name')
        print(f"{sha}: {committer}")
        count += 1
