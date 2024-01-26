#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url)
    print('Body response:')
    print('\t-', 'type:', type(res.text))
    print('\t-', 'content:', res.text)
