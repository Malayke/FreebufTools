# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FreebufToolsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # tool_id = scrapy.Field()
    tool_desc = scrapy.Field()
    tool_release_date = scrapy.Field()
    tool_url = scrapy.Field()

