# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from store import NewsDB

class WeixinPipeline(object):
    def process_item(self, item, spider):
        NewsDB.weixin.insert(dict(item))
        return None
