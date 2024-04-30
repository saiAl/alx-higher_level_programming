#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    from urllib.request import urlopen
    with urlopen("https://alx-intranet.hbtn.io/status") as res:
        body = res.read()
        print("Body response:\n\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        if res.headers.get_content_charset() == "utf-8":
            print("\t- utf-8 content: OK")
