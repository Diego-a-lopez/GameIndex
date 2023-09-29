from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


"""

"""
class TestCrawlingSpider(CrawlSpider):
	name = "mycrawler"
	allowed_domains = ["toscrape.com"]
	start_urls = ["http://books.toscrape.com/"]
	
	rules = (
		Rule(LinkExtractor(allow="catalogue/category")),
		Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item")
	)

	def parse_item(self, response):
		yield {
			"title": response.css(".product_main h1::text").get(),
			"price": response.css(".price_color::text").get(),
			#"availability": response.css(".availability::text")[2].get().replace("\n","").replace(" ", "")
		}

"""

"""
"""
class CrawlingSpider(CrawlSpider):
	name = "Pokecrawler"
	
	allowed_domains = [""]
	start_urls = []
	
	rules = (
		Rule(LinkExtractor(allow="")),
	)
	
	def parse_item(self, response):
		yield{
			"id": response.css().get(),
			"nombre": response.css().get(),
			
			"PS": response.css().get(),
			"AT": response.css().get(),
			"AT-ESP": response.css().get(),
			"DEF": response.css().get(),
			"DEF-ESP": response.css().get(),
			"VEL": response.css().get(),
			
			"generación": response.css().get(),
			"tipos": response.css().get(),
			"peso": response.css().get(),
			"altura": response.css().get(),
			"abilidades": response.css().get(),
			"movimientos": response.css().get(),
			
		}
"""
