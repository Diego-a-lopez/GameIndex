import requests
from bs4 import BeautifulSoup
from datetime import datetime
"""
url = 'https://store.steampowered.com/games/'
page = requests.get(url)
"""

url = 'https://store.steampowered.com/agecheck/app/1091500/Cyberpunk_2077/'
response = requests.get(url)

print (response.url)
if '/agecheck' in response.url:
			
	redir= response.url.replace("/agecheck", "")
				
	print(redir)
				
	response = requests.get(url=redir,
	cookies={'mature_content': '1'})


print (response.url)
