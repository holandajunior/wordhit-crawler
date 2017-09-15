import scrapy
from scrapy.selector import Selector

class WordHitSpider(scrapy.Spider):
	name = 'wordhitSpider'
	allowed_domains = ["www.bing.com"]
	start_urls = ['https://www.google.com.br/search?q=teste&oq=teste', 'https://www.google.com.br/search?q=teste&oq=teste']

	custom_settings = {
        'DOWNLOAD_DELAY': 4,
        'CONCURRENT_REQUESTS': 1
    }

	def parse(self, response):
		hitsText = Selector(response).xpath('//*[@id="resultStats"]/text()').extract()[0]
		hits = hitsText.split(' ')[1]
		print(hits)
		

		
