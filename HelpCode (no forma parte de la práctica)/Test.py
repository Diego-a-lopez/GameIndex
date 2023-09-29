import requests
from bs4 import BeautifulSoup

page = requests.get('https://store.steampowered.com/app/2195250/EA_SPORTS_FC_24/')
soup = BeautifulSoup(page.text, 'html.parser')

div = soup.find(id = "appHubAppName")

print(div.text)

#print(page.text)


