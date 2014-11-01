# -*- coding: utf-8 -*-

import scrapy
import re
import time
from scrapy.http import Request
from scrapy.spider import BaseSpider
from weixin.items import WeixinItem
from url_list import UrlList

class WeixinSpider(BaseSpider):
    name = 'weixin'
    start_urls = UrlList.url_list()

    def parse(self, response):
        time.sleep(2)
        
        sel_list = response.xpath("//div[@class='txt-box']")
        for sel in sel_list:
            item = WeixinItem()
            self.get_title(item,sel)
            self.get_link(item,sel)
            self.get_name(item,sel)
            self.get_timestamp(item,sel)
            yield item

        next_link = response.xpath("//a[@id='sogou_next']/@href").extract()
        if next_link:
            next_link = 'http://weixin.sogou.com/weixin' + next_link[0]
            current_page_index = response.xpath("//div[@id='pagebar_container']/span/text()").extract()
            if current_page_index and int(current_page_index[0]) <=3:
                print '-------------------------------'
                print current_page_index[0]
                yield Request(url=next_link, callback=self.parse)
    

    def get_title(self,item,selector):
        title = selector.xpath('h4/a').extract()
        if title:
            title = re.sub(r'(</?\w+[^>]*>)|(<![^>]*>)','',title[0])
            item['title'] = title
        
    def get_name(self,item,selector):
        name = selector.xpath("div[@class='s-p']/a/@title").extract()
        if name:
            item['name'] = name[0]
    
    def get_link(self,item,selector):
        link = selector.xpath("h4/a/@href").extract()
        if link:
            item['link'] = link[0]

    def get_timestamp(self,item,selector):
        timestamp= selector.xpath("div[@class='s-p']/script/text()").extract()
        if timestamp:
            timestamp = re.sub(r"(^[^(]*\(')|'\)","",timestamp[0])    
            item['timestamp'] = timestamp
         

    
    

