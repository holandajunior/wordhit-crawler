import scrapy
from scrapy.selector import Selector
from wordhit_crawler.items import WordhitItem

class WordHitSpider(scrapy.Spider):
	name = 'wordhitSpider'
	allowed_domains = ["www.google.com"]
	
	custom_settings = {
        'DOWNLOAD_DELAY': 6,
        'CONCURRENT_REQUESTS': 1
    }

	def start_requests(self):
		
		
		with open('google_urls.txt', 'rb') as f:
			lines = [line.strip() for line in f.read().decode('utf8').splitlines() if line.strip()]

		for line in lines:
			url, word = line.split(',')
			
			# url = infos[0]
			# word = infos[1]

			yield scrapy.Request(url=url, callback=self.parse, meta={'word': word})
			
	def parse(self, response):
		hitsText = Selector(response).xpath('//*[@id="resultStats"]/text()').extract()[0]
		hits = hitsText.split(' ')[1]
		word = response.meta['word']
		
		wordItem = WordhitItem()
		wordItem['word'] = word
		wordItem['hits'] = hits

		yield wordItem
		

		
