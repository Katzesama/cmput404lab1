#!/usr/bin/evn python

import requests

print(requests.__version__)

r = requests.get("http://www.google.com")
print(r.status_code)
print(r.headers)

r = requests.get("https://raw.githubusercontent.com/Katzesama/cmput404lab1/master/main.py")
print(r.text)
