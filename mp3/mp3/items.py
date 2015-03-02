
from scrapy.item import Item, Field


class PostItem(Item):
  
    url = Field()
    link = Field()