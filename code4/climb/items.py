# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ClimbItem(scrapy.Item):
    # define the fields for your item here like:

    rank = scrapy.Field()

    name = scrapy.Field()

    king = scrapy.Field()

    pic = scrapy.Field()

    dir = scrapy.Field()

    intro = scrapy.Field()

    pass
