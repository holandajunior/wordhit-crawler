import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem

class MongoPipeline(object):

	def __init__(self):
		connection = pymongo.MongoClient(
			settings['MONGODB_SERVER'],
			settings['MONGODB_PORT']
		)

		db = connection[settings['MONGODB_DB']]
		self.collection = db[settings['MONGODB_COLLECTION']]

	def process_item(self, item, spider):
		
		if item['hits']:
			self.collection.update_one({'word': item['word']}, {'$set': {'hits': item['hits']}})
			return item
		else:
			raise DropItem("Missing hits field in %s" % item)