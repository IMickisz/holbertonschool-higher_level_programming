#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the body of the response
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.error
    from sys import argv

    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(e.status))
