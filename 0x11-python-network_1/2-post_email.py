#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
"""


if __name__ == "__main__":
    from urllib import parse, request
    from sys import argv

    values = {'email': argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8", "replace"))
