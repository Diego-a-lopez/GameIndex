from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


"""

"""
class TestCrawlingSpider(CrawlSpider):
	name = ">Steamcrawler"
	allowed_domains = ["steampowered.com"]
	start_urls = ["https://store.steampowered.com/"]
	
	rules = (
		Rule(LinkExtractor(allow="/app",), callback="parse_item")
	)

	def parse_item(self, response):
		item = scrapy.Item()
		soup = BeautifulSoup(response.body, 'lxml')
		
		div = soup.find(id="")
