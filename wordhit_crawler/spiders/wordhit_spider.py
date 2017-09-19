import scrapy
from scrapy.selector import Selector

class WordHitSpider(scrapy.Spider):
	name = 'wordhitSpider'
	allowed_domains = ["www.google.com"]
	
	custom_settings = {
        'DOWNLOAD_DELAY': 6,
        'CONCURRENT_REQUESTS': 1
    }

	def start_requests(self):
		
		urls = []

		with open('google_urls.txt', 'rb') as f:
			urls = [line.strip() for line in f.read().decode('utf8').splitlines() if line.strip()]

		for url in urls:
			word = url.split('=')[1]
			yield scrapy.Request(url=url, callback=self.parse, meta={'word': word})
			
	def parse(self, response):
		hitsText = Selector(response).xpath('//*[@id="resultStats"]/text()').extract()[0]
		hits = hitsText.split(' ')[1]
		word = response.meta['word']
		print({ 'word': word, 'hits': hits })
		

		
