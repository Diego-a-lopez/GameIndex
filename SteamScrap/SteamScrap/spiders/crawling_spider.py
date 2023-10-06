import scrapy
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request

"""

"""
class TestCrawlingSpider(CrawlSpider):
	name = "Steamcrawler"
	allowed_domains = ["steampowered.com/"]
	start_urls = ["https://store.steampowered.com/"]
	
	rules = (
		Rule(LinkExtractor(allow="app/"), callback="parse_item"),
	)

	def parse_item(self, response):
		
		item = scrapy.Item()
		soup = BeautifulSoup(response.body, 'lxml')
		
		div_element = soup.find('div', {'id': 'genresAndManufacturer'})
		
		
		print (div_element)
		print (div_element.find('b', string='Título:'))
		
		

		titulo = div_element.find('b', string='Título:').next_sibling.strip()
		
		#Lista de generos
		
		genero_span = div_element.find('b', string='Género:').find_next('span')
		genero_links = genero_span.find_all('a')
		genero = [link.get_text(strip=True) for link in genero_links]
			
		#Lista de desarrolladores
			
		desarrollador_elements = div_element.find_all('b', string='Desarrollador:')
		desarrolladores = [element.find_next('a').get_text(strip=True) for element in desarrollador_elements]
		
		#Lista de editores
		
		editor_elements = div_element.find_all('b', string='Editor:')
		editores = [element.find_next('a').get_text(strip=True) for element in editor_elements]
		
		#Lista de franquicias

		franquicia_elements = div_element.find_all('b', string='Franquicia:')
		franquicias = [element.find_next('a').get_text(strip=True) for element in franquicia_elements]

		#Fecha de lanzamiento
		
		fecha_lanzamiento_str = div_element.find('b', string='Fecha de lanzamiento:').next_sibling.strip()
		fecha_lanzamiento = datetime.strptime(fecha_lanzamiento_str, '%d %b %Y')
		
		
		#Elementos fuera del div
		
		price_element = soup.find('div', class_='game_purchase_price')
		
		discount_element = soup.find('div', class_='discount_original_price')
		
		#Descripcion
		
		descripcion = soup.find('div', class_="game_description_snippet").get_text(strip=True)
		
		#Imagenes
		
		imagen_cabecera = soup.find('img', class_='game_header_image_full')['src']
		
		images_list = soup.find('div', id= "highlight_strip_scroll").find_all('img')
		
		lista_imagenes = []
		
		for element in images_list:
			lista_imagenes.append(element['src'])
			
				
		if price_element:
			precio = float(price_element.get_text(strip=True).replace(",", ".").replace("€", ""))
		elif discount_element:
			precio = float(discount_element.get_text(strip=True).replace(",", ".").replace("€", ""))
		else:
			precio = "-1"
			
			
		item['Título']= titulo
		item['Descripción']= descripcion
		item['Precio']= precio
		item['Desarrolladores']= desarrolladores
		item['Editores']= editores
		item['Franquicias']= franquicias
		item['Fecha de lanzamiento']= fecha_lanzamiento
		item['Imágen_Cabecera']= imagen_cabecera
		item['Lista_Imagenes']= lista_imagenes
		item['Url']= response.URL
		
		return item
