import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://store.steampowered.com/app/2195250/EA_SPORTS_FC_24/'
url = 'https://store.steampowered.com/app/1637320?snr=1_4_4__40_2'
url = 'https://store.steampowered.com/app/1245620/ELDEN_RING/'
#url = 'https://store.steampowered.com/app/1573280/WW2_Rebuilder/?snr=1_4_4__43_1'
#headers = {'Accept-Language': 'es-ES,es;q=0.9'}
#page = requests.get(url, headers=headers)
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

#div = soup.find(id = "appHubAppName")

#print(div.text)

#col_div = soup.find(id = "appHubAppName")

div_element = soup.find('div', {'id': 'genresAndManufacturer'})
    
if div_element:
	
	
	"""
	spanish

	# Extract and format the fields
	titulo = div_element.find('b', string='Título:').next_sibling.strip()

	genero_span = div_element.find('b', string='Género:').find_next('span')
	genero_links = genero_span.find_all('a')
	genero = [link.get_text(strip=True) for link in genero_links]
			
	desarrollador = div_element.find('b', string='Desarrollador:').find_next('a').get_text(strip=True)
	editor = div_element.find('b', string='Editor:').find_next('a').get_text(strip=True)
	editor_element = div_element.find('b', string='Editor:')
	editores = []

	if editor_element:
		editor_div = editor_element.find_parent('div', class_='dev_row')
		if editor_div:
			editor_links = editor_div.find_all('a')
			editores = [link.get_text(strip=True) for link in editor_links]
		
	franquicia = div_element.find('b', string='Franquicia:').find_next('a').get_text(strip=True)


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
	print(f"Desarrollador: {desarrollador}")
	print(f"Editor: {editores}")
	print(f"Franquicia: {franquicia}")
	print(f"Fecha de lanzamiento: {fecha_lanzamiento}")
	print(f"Precio: {price}")
	"""

	"""
	english
	"""
	if div_element:
		
		#print(div_element)
		"""
		item = GameItem()
		soup = BeautifulSoup(response.body, 'lxml')
		
		div_element = soup.find('div', {'id': 'genresAndManufacturer'})
		
		div_element = soup.find('div', {'id': 'genresAndManufacturer'})
		"""
		Title = div_element.find('b', string='Title:').next_sibling.strip()
		
		#Lista de generos
		
		genre_span = div_element.find('b', string='Genre:').find_next('span')
		genre_links = genre_span.find_all('a')
		genre = [link.get_text(strip=True) for link in genre_links]
			
		#Lista de desarrolladores
		
		developers_element = div_element.find('b', string='Developer:')
		
		developers = []

		if developers_element:
			developers_div = developers_element.find_parent('div', class_='dev_row')
			if developers_div:
				developers_links = developers_div.find_all('a')
				developers = [link.get_text(strip=True) for link in developers_links]
		
		
		#Lista de editores
		
		publisher_element = div_element.find('b', string='Publisher:')
		
		publishers = []

		if publisher_element:
			publisher_div = publisher_element.find_parent('div', class_='dev_row')
			if publisher_div:
				publisher_links = publisher_div.find_all('a')
				publishers = [link.get_text(strip=True) for link in publisher_links]	
		
		#Lista de franquicias

		franchise_element = div_element.find('b', string='Franchise:')
		franchise = []

		if franchise_element:
			franchise_div = franchise_element.find_parent('div', class_='dev_row')
			if franchise_div:
				franchise_links = franchise_div.find_all('a')
				franchise = [link.get_text(strip=True) for link in franchise_links]

		#Fecha de lanzamiento
		
		release_date_str = div_element.find('b', string='Release Date:').next_sibling.strip()
		release_date = datetime.strptime(release_date_str, '%d %b, %Y')
		
		
		#Elementos fuera del div
		
		price_element = soup.find('div', class_='game_purchase_price')
		
		discount_element = soup.find('div', class_='discount_original_price')
		
		#Descripcion
		
		description = soup.find('div', class_="game_description_snippet").get_text(strip=True)
		
		#Imagenes
		
		header_image = soup.find('img', class_='game_header_image_full')['src']
		
		div_images_list = soup.find('div', id= "highlight_strip_scroll").find_all('img')
		
		images_list = []
		
		for element in div_images_list:
			images_list.append(element['src'])
			
				
		if price_element:
			price = float(price_element.get_text(strip=True).replace(",", ".").replace("€", ""))
		elif discount_element:
			price = float(discount_element.get_text(strip=True).replace(",", ".").replace("€", ""))
		else:
			price = "-1"
			
		"""
		item['Title']= Title
		item['Descrition']= description
		item['Price']= price
		item['Genre'] = genre
		item['Developers']= developers
		item['Editors']= editors
		item['Franchise']= franchise
		item['Release_date']= release_date
		item['Header_Image']= header_image
		item['Image_List']= images_list
		item['Url']= response.url
		"""
		
		score = soup.find('div', id= "game_area_metascore").find_next('div').get_text(strip=True)
		reviews= [review.find_next('span').get_text(strip=True) for review in soup.find_all('div', class_= "summary_section")]
		reviews= soup.find('div', class_= "summary_section").find_next('span').get_text(strip=True)
		
		for review in soup.find_all('div', class_= "summary_section"):
			print(review.find_next('span').get_text(strip=True))
			print(review.find_next('span').find_next('span').get_text(strip=True))
			
		print(f"Título: {Title}")
		print(f"Descripción: {description}")
		print(f"Precio: {price}")
		print(f"Género: {genre}")
		print(f"Desarrollador: {developers}")
		print(f"Editor: {publishers}")
		print(f"Franquicia: {franchise}")
		print(f"Fecha de lanzamiento: {release_date}")
		print(f"reviews:{reviews}")
		print(f"puntuación:{score}")

	#print(page.url)
	
	#print(div_element)

