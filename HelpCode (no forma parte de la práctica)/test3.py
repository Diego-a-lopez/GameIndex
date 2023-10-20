




"""
import urllib.request

url = 'https://store.steampowered.com/search/'

fname = "webpage.html"

get = urllib.request.urlopen(url)
html = get.read()

#print(page.text)

with open(fname, "w", encoding="utf-8") as f:
    f.write(html)
f.close()
"""

import requests

url = 'https://store.steampowered.com/search/'

page = requests.get(url)

#print(page.text)

f = open("webpage.html", "wb")
f.write(page.content)
f.close()

