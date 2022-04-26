#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""


import requests


if __name__ == "__main__":
    reponse = requests.get('https://intranet.hbtn.io/status')

    print("Body response:")
    print("\t- type: {}".format(type(reponse.text)))
    print("\t- content: {}".format(reponse.text))
