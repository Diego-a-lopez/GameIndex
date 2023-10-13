import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://store.steampowered.com/games/'
page = requests.get(url)
print(page.text)
