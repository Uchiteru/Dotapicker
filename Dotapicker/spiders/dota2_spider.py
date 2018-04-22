# -*- coding: utf-8 -*-
import scrapy
from Dotapicker.items import DotapickerItem
import datetime

class DotaSpiderSpider(scrapy.Spider):
    name = 'dota2_spider'
    allowed_domains = ['dota2.gamepedia.com']
    start_urls = ['https://dota2.gamepedia.com/Heroes']

    def parse(self, response):
        base_url = 'https://dota2.gamepedia.com/'
        for hero_url in response.xpath('//*[@id="mw-content-text"]/table[1]/tr[*]/td[1]//div//@href').extract():
            counter_url = base_url+hero_url+"/Counters"
            next_page =  counter_url
            yield scrapy.Request(next_page, callback=self.parse_items)
    #データ抽出関数定義
    def parse_items(self, response): # response に、ウェブサイトの情報が入っている
        item = DotapickerItem()  # items.pyで指定したクラス
        item['hero'] = response.xpath('//*[@id="contentSub"]/span/a/@title').extract()
        item['bad'] = response.xpath('//*[@id="mw-content-text"]/div/div[contains(@style,"box-shadow:0px 0px 2px 4px red")]//@title').extract()
        item['wellwith'] = response.xpath('//*[@id="mw-content-text"]/div/div[contains(@style,"box-shadow:0px 0px 2px 4px skyblue")]//@title').extract()
        item['good'] = response.xpath('//*[@id="mw-content-text"]/div/div[contains(@style,"box-shadow:0px 0px 2px 4px chartreuse")]//@title').extract()
        yield item