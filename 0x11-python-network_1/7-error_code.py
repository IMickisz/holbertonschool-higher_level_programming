#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the
body of the response.
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    reponse = requests.get(argv[1])
    if reponse.status_code < 400:
        print(reponse.text)
    else:
        print("Error code: {}".format(reponse.status_code))
