import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://store.steampowered.com/app/2195250/EA_SPORTS_FC_24/'
headers = {'Accept-Language': 'es-ES,es;q=0.9'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

#div = soup.find(id = "appHubAppName")

#print(div.text)

#col_div = soup.find(id = "appHubAppName")

div_element = soup.find('div', {'id': 'genresAndManufacturer'})
    
if div_element:
	# Extract and format the fields
	titulo = div_element.find('b', string='Título:').next_sibling.strip()

	genero_span = div_element.find('b', string='Género:').find_next('span')
	genero_links = genero_span.find_all('a')
	genero = [link.get_text(strip=True) for link in genero_links]
			
	desarrollador = div_element.find('b', string='Desarrollador:').find_next('a').get_text(strip=True)
	editor = div_element.find('b', string='Editor:').find_next('a').get_text(strip=True)
	franquicia = div_element.find('b', string='Franquicia:').find_next('a').get_text(strip=True)

	fecha_lanzamiento_str = div_element.find('b', string='Fecha de lanzamiento:').next_sibling.strip()
	
	fecha_lanzamiento = datetime.strptime(fecha_lanzamiento_str, '%d %b %Y')
	
	price_element = soup.find('div', class_='game_purchase_price')
	
	discount_element = soup.find('div', class_='discount_original_price')
			
	if price_element:
		price = price_element.get_text(strip=True)
	elif discount_element:
		price = discount_element.get_text(strip=True)
	else:
		price = "Precio no disponible"
			
	# Print the formatted output
	print(f"Título: {titulo}")

	print(f"Género: {genero}")
	print(f"Desarrollador: {desarrollador}")
	print(f"Editor: {editor}")
	print(f"Franquicia: {franquicia}")
	print(f"Fecha de lanzamiento: {fecha_lanzamiento}")
	print(f"Precio: {price}")

#print(page.text)


