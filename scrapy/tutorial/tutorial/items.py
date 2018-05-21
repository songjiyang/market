# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class UserItem(scrapy.Item):
    shopid = scrapy.Field()
    name = scrapy.Field()
    sex = scrapy.Field()
    birth = scrapy.Field()
    love = scrapy.Field()
    star = scrapy.Field()

class ShopItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    region = scrapy.Field()
    type = scrapy.Field()
    address = scrapy.Field()
