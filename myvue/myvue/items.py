# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyvueItem(scrapy.Item):
	
    title = scrapy.Field()
    shorDescription = scrapy.Field()
    starCast = scrapy.Field()
    runningTime = scrapy.Field()
    showTiming = scrapy.Field()
    image_or_videoURL = scrapy.Field()

