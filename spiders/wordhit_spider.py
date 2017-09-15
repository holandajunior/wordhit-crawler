import scrapy
from scrapy.selector import Selector

class WordHitSpider(scrapy.Spider):
	name = 'wordhitSpider'
	allowed_domains = ["www.bing.com"]
	
	custom_settings = {
        'DOWNLOAD_DELAY': 4,
        'CONCURRENT_REQUESTS': 1
    }

	def start_requests(self):
		urls = [
			'https://www.google.com.br/search?q=teste', 
			'https://www.google.com.br/search?q=project']

		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		hitsText = Selector(response).xpath('//*[@id="resultStats"]/text()').extract()[0]
		hits = hitsText.split(' ')[1]
		print(hits)
		

		
