#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response (decoded
in utf-8)"""


if __name__ == "__main__":
    from urllib import parse, request
    from sys import argv

    values = {'email': argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8", "replace"))
