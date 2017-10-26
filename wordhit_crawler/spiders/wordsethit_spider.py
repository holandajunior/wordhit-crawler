import scrapy
from scrapy.selector import Selector
from wordhit_crawler.items import WordhitItem

class WordHitSpider(scrapy.Spider):
	name = 'wordhitSpider'
	allowed_domains = ["www.google.com"]
	
	custom_settings = {
        'DOWNLOAD_DELAY': 4,
        'CONCURRENT_REQUESTS': 2
    }

	def start_requests(self):
		base_url = "https://www.google.com/search?q={}"	
		
		with open('google_urls.txt', 'rb') as f:
			lines = [line.strip() for line in f.read().decode('utf8').splitlines() if line.strip()]

		sizeLines = len(lines)

		for idx1 in range(sizeLines):
			word1 = lines[idx1]
			
			for idx2 in range(sizeLines):
				word2 = lines[idx2]

				words = word1 + '+' + word2
				completeUrl = base_url.format(words)

				yield scrapy.Request(url=completeUrl, callback=self.parse, meta={'words': words})
			
	def parse(self, response):
		hitsText = Selector(response).xpath('//*[@id="resultStats"]/text()').extract()[0]
		hits = hitsText.split(' ')[1]
		word = response.meta['words']
		
		wordItem = WordhitItem()
		wordItem['word'] = word
		wordItem['hits'] = hits

		yield wordItem
		

		
