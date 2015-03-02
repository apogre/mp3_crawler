from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from mp3.items import *
import re

class Mp3Spider(CrawlSpider):
	name = "mp3"
	start_urls = ['https://mp3skull.to/']
	# start_urls = ['http://mp3skull.com/mp3/d_masiv.html']
	allowed_domains= ['mp3skull.to']
	rules = [
		# Rule(SgmlLinkExtractor(allow=[r'\w+']), follow=True),
		Rule(SgmlLinkExtractor(allow=[r'mp3/\w+']), follow= True,callback = 'parse_post')
	]


	def parse_post(self, response):
		item = PostItem()		
		item['link'] =response.xpath('//a[@style="color:green;"]/@href').extract()
		return item

	