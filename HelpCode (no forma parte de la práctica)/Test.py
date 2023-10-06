import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://store.steampowered.com/app/2195250/EA_SPORTS_FC_24/'
url = 'https://store.steampowered.com/app/1637320?snr=1_4_4__40_2'
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
			
	desarrollador_elements = div_element.find_all('b', string='Desarrollador:')
	desarrolladores = [element.find_next('a').get_text(strip=True) for element in desarrollador_elements]
	
	editor_elements = div_element.find_all('b', string='Editor:')
	editores = [element.find_next('a').get_text(strip=True) for element in editor_elements]

	franquicia_elements = div_element.find_all('b', string='Franquicia:')
	franquicias = [element.find_next('a').get_text(strip=True) for element in franquicia_elements]


	fecha_lanzamiento_str = div_element.find('b', string='Fecha de lanzamiento:').next_sibling.strip()
	
	fecha_lanzamiento = datetime.strptime(fecha_lanzamiento_str, '%d %b %Y')
	
	price_element = soup.find('div', class_='game_purchase_price')
	
	discount_element = soup.find('div', class_='discount_original_price')
	
	#Game Image
	
	imagen_cabecera = soup.find('img', class_='game_header_image_full')['src']
	descripcion = soup.find('div', class_="game_description_snippet").get_text(strip=True)
	images_list = soup.find('div', id= "highlight_strip_scroll").find_all('img')
	
	lista_imagenes = []
	
	for element in images_list:
		lista_imagenes.append(element['src'])
			
	if price_element:
		price = float(price_element.get_text(strip=True).replace(",", ".").replace("€", ""))
	elif discount_element:
		price = float(discount_element.get_text(strip=True).replace(",", ".").replace("€", ""))
	else:
		price = "Precio no disponible"

	# Print the formatted output
	print(f"Título: {titulo}")
	print(f"Descripción: {descripcion}")
	print(f"Género: {genero}")
	print(f"Desarrollador: {desarrolladores}")
	print(f"Editor: {editores}")
	print(f"Franquicia: {franquicias}")
	print(f"Fecha de lanzamiento: {fecha_lanzamiento}")
	print(f"Precio: {price}")

