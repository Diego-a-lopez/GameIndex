import scrapy
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field

"""

"""
class TestCrawlingSpider(CrawlSpider):
	name = "Steamcrawler"
	allowed_domains = ["steampowered.com"]
	start_urls = ["https://store.steampowered.com/"]
	
	rules = (
		Rule(LinkExtractor(allow=r'tags/en/[^?/]+/$', deny=r'l=[^&/]+'), follow=True),
		Rule(LinkExtractor(allow='app/', deny=r'l=[^&/]+'), callback="parse_item",follow=True),
	)
	def parse_item(self, response):
		
		item = GameItem()
		soup = BeautifulSoup(response.body, 'lxml')
		
		div_element = soup.find('div', {'id': 'genresAndManufacturer'})
		
		div_element = soup.find('div', {'id': 'genresAndManufacturer'})

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
		else :
			franchise = ["none"]

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
			if (price_element.get_text(strip=True) == 'Free to Play'):
				price = float(0)
			else:
				price = float(price_element.get_text(strip=True).replace(",", ".").replace("€", ""))
		elif discount_element:
			price = float(discount_element.get_text(strip=True).replace(",", ".").replace("€", ""))
		else:
			price = "-1"
			
			
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
		
		return item


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
