#!/usr/bin/python3
""" Script that fetches 'https://alx-intranet.hbtn.io/status' """
import urllib.request


if __name__ == '__main__':
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as hbtn_page:
        page = hbtn_page.read()
        page_fmt = page.decode('utf-8')
        print('Body response:')
        print('\t- type:', type(page))
        print('\t- content', page)
        print('\t- utf8 content:', page_fmt)
