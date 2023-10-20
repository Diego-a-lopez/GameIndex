import scrapy
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import FormRequest
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field

"""

"""
class SteamCrawlingSpider(CrawlSpider):
	name = "Steamcrawler"
	allowed_domains = ["steampowered.com"]
	
	#Crawl juegos mas relevantes y las 40 etiqueas mas importantes
	
	start_urls = ["https://store.steampowered.com/search/?category1=998"
		"https://store.steampowered.com/search/?category1=998&tags=492",
		"https://store.steampowered.com/search/?category1=998&tags=19",
		"https://store.steampowered.com/search/?category1=998&tags=21",
		"https://store.steampowered.com/search/?category1=998&tags=597",
		"https://store.steampowered.com/search/?category1=998&tags=122",
		"https://store.steampowered.com/search/?category1=998&tags=599",
		"https://store.steampowered.com/search/?category1=998&tags=9",
		"https://store.steampowered.com/search/?category1=998&tags=4182",
		"https://store.steampowered.com/search/?category1=998&tags=493",
		"https://store.steampowered.com/search/?category1=998&tags=113",
		"https://store.steampowered.com/search/?category1=998&tags=3871",
		"https://store.steampowered.com/search/?category1=998&tags=4191",
		"https://store.steampowered.com/search/?category1=998&tags=4166",
		"https://store.steampowered.com/search/?category1=998&tags=1684",
		"https://store.steampowered.com/search/?category1=998&tags=1742",
		"https://store.steampowered.com/search/?category1=998&tags=4305",
		"https://store.steampowered.com/search/?category1=998&tags=3859",
		"https://store.steampowered.com/search/?category1=998&tags=1664",
		"https://store.steampowered.com/search/?category1=998&tags=3964",
		"https://store.steampowered.com/search/?category1=998&tags=3834",
		"https://store.steampowered.com/search/?category1=998&tags=128",
		"https://store.steampowered.com/search/?category1=998&tags=701",
		"https://store.steampowered.com/search/?category1=998&tags=4726",
		"https://store.steampowered.com/search/?category1=998&tags=4667",
		"https://store.steampowered.com/search/?category1=998&tags=3839",
		"https://store.steampowered.com/search/?category1=998&tags=3993",
		"https://store.steampowered.com/search/?category1=998&tags=699",
		"https://store.steampowered.com/search/?category1=998&tags=4085",
		"https://store.steampowered.com/search/?category1=998&tags=4106",
		"https://store.steampowered.com/search/?category1=998&tags=12095",
		"https://store.steampowered.com/search/?category1=998&tags=1773",
		"https://store.steampowered.com/search/?category1=998&tags=6650",
		"https://store.steampowered.com/search/?category1=998&tags=4136",
		"https://store.steampowered.com/search/?category1=998&tags=3942",
		"https://store.steampowered.com/search/?category1=998&tags=1774",
		"https://store.steampowered.com/search/?category1=998&tags=1654",
		"https://store.steampowered.com/search/?category1=998&tags=4345",
		"https://store.steampowered.com/search/?category1=998&tags=1667",
		"https://store.steampowered.com/search/?category1=998&tags=4004",
		"https://store.steampowered.com/search/?category1=998&tags=5350",
		"https://store.steampowered.com/search/?category1=998&tags=1697",	
	]
	
	rules = (
		Rule(LinkExtractor(allow='/app/(.+)/', restrict_css='#search_result_container'), callback='parse_item'),
	)

	def parse_item(self, response):
		
		item = GameItem()
		
		if '/agecheck' in response.url:
			
			redir= response.url.replace("/agecheck", "")
			
			response = requests.get(url=redir,
				cookies={'mature_content': '1'})
			soup = BeautifulSoup(response.text, 'html.parser')
		
		else:
			soup = BeautifulSoup(response.body, 'lxml')
		
		if not '?l=' in response.url:
			
			#div con información
			
			div_element = soup.find('div', {'id': 'genresAndManufacturer'})
			
			#Título del juego

			Title = div_element.find('b', string='Title:').next_sibling.strip()
			
			#Lista de generos
			
			genre_element = div_element.find('b', string='Genre:')
			
			genre = [] # por defecto lista vacia
		
			if genre_element: # si hay lista de generos
				genre_span = genre_element.find_next('span')
				genre_links = genre_span.find_all('a')
				genre = [link.get_text(strip=True) for link in genre_links]
				
				
			#Lista de desarrolladores
			
			developers_element = div_element.find('b', string='Developer:')
			
			developers = [] # por defecto lista vacia

			if developers_element: #si hay desarrolladores (este campo debería estar siempre lleno pero por si acaso que no de fallo)
				developers_div = developers_element.find_parent('div', class_='dev_row')
				if developers_div:
					developers_links = developers_div.find_all('a')
					developers = [link.get_text(strip=True) for link in developers_links]
			
			
			#Lista de editores
			
			publisher_element = div_element.find('b', string='Publisher:')
			
			publishers = [] # por defecto lista vacia

			if publisher_element: #si hay editores
				
				publisher_div = publisher_element.find_parent('div', class_='dev_row')
				
				if publisher_div:
					
					publisher_links = publisher_div.find_all('a')
					publishers = [link.get_text(strip=True) for link in publisher_links]	
			
			#Lista de franquicias

			franchise_element = div_element.find('b', string='Franchise:')
			franchise = []

			if franchise_element: #si hay franquicia
				
				franchise_div = franchise_element.find_parent('div', class_='dev_row')
				
				if franchise_div:
					
					franchise_links = franchise_div.find_all('a')
					franchise = [link.get_text(strip=True) for link in franchise_links]
					
			else : # si no se le pone 'none' 
				
				franchise = ["none"]

			#Fecha de lanzamiento
			
			release_date = div_element.find('b', string='Release Date:').next_sibling.strip()

			
			
			
			#Elementos fuera del div
			
			# precio del juego
			
			price_element = soup.find('div', class_='game_purchase_price') # precio normal
			
			discount_element = soup.find('div', class_='discount_original_price') # precio con descuento
				
			if price_element:
				
				if price_element.get_text(strip=True).lower() in ('free to play', 'free'): 
					price = float(0)
					
				else:
					try:
						price = float(price_element.get_text(strip=True).replace(",", ".").replace("€", ""))
					except:
						print(f"error : {price_element.get_text} is not a number")
						price = float(0)

			elif discount_element:
				
				price = float(discount_element.get_text(strip=True).replace(",", ".").replace("€", ""))

			else:
				price = float(0)
				
				
			#Descripcion
			
			description_div = soup.find('div', class_="game_description_snippet")
			
			if description_div:
				description = description_div.get_text(strip=True)
			else: 
				description = ""
			
			#Imagenes
			
			header_image_element = soup.find('img', class_='game_header_image_full')
			
			if header_image_element:
				
				header_image= header_image_element['src']
				
			else:
				header_image = ""
			
			div_images_list_element = soup.find('div', id= "highlight_strip_scroll")
			
			images_list = []
			
			if div_images_list_element:
				
				div_images_list = div_images_list_element.find_all('img')
					
				for element in div_images_list:
					
					images_list.append(element['src'])
					
			score_element = soup.find('div', id= "game_area_metascore")
			score = "none"
			
			if score_element:
				score = score_element.find_next('div').get_text(strip=True)
				
			reviews_element = soup.find('div', class_= "summary_section")
			
			reviews = "No user reviews"
			
			if reviews_element:
				reviews = reviews_element.find_next('span').get_text(strip=True)

			
			
			#pasar toda la información al game item
			item['Title']= Title
			item['Descrition']= description
			item['Price']= price
			item['Genre'] = genre
			item['Developers']= developers
			item['Publishers']= publishers
			item['Franchise']= franchise
			item['Release_date']= release_date
			item['Header_Image']= header_image
			item['Image_List']= images_list
			item['Url']= response.url
			item['Score']= score
			item['Reviews']= reviews
			
			return item
			
"""

"""

class GameItem(Item):
	
	Title = Field()
	Descrition = Field()
	Price = Field()
	Genre = Field()
	Developers = Field()
	Publishers = Field()
	Franchise = Field()
	Release_date = Field()
	Header_Image = Field()
	Image_List = Field()
	Url = Field()
	Score = Field()
	Reviews = Field()
