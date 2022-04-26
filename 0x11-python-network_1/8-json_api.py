#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) < 2:
        data = {'q': ""}
    else:
        data = {'q': argv[1]}
    reponse = requests.post('http://0.0.0.0:5000/search_user',
                            data=data)
    try:
        if reponse.json() == {}:
            print("No result")
        else:
            print("[{}] {}".format(reponse.json().get("id"),
                                   reponse.json().get("name")))
    except Exception:
        print("Not a valid JSON")
