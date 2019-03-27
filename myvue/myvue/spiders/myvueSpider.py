# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from myvue.items import myvueItem


class MyvuespiderSpider(scrapy.Spider):
    name = 'myvueSpider'
    allowed_domains = ['myvue.com']

    def start_requests(self):
        locality = "Aberdeen"
        url = "https://www.myvue.com/cinema/%s/whats-on"%str(locality)
        yield SplashRequest(url=url, callback=self.parse)

    def parse(self, response):

        divList = response.xpath('//*[@class="filmlist__item"]/div')
        item = myvueItem()

        for div in divList:
            item['title'] = div.xpath("./div[2]/a/span/text()").extract_first()
            item['shorDescription'] = div.xpath("./div[2]/p/text()").extract_first()
            item['starCast'] = div.xpath("./div[2]/div[1]/dl[1]/dd/text()").extract_first()
            item['runningTime'] = div.xpath("./div[2]/div[1]/dl[2]/dd/text()").extract_first()
            item['showTiming'] = "|".join(div.xpath("./div[3]/div/div/div/ul/li/a/@title").extract())
            item['image_or_videoURL'] = div.xpath("./div[1]/a/@data-videourl").extract_first()
            yield item
