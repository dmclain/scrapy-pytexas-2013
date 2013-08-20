# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class PytexasItem(Item):
    # define the fields for your item here like:
    # name = Field()
    title = Field()
    time = Field()
    speaker = Field()
    description = Field()
