import scrapy

class WordhitItem(scrapy.Item):
	word = scrapy.Field()
	hits = scrapy.Field()