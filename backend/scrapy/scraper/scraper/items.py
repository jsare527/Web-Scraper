# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GenericItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    img = scrapy.Field()
