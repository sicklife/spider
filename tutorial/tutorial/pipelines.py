# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
from collections import OrderedDict
import json

class TutorialPipeline(object):
    def __init__(self):
        self.file = codecs.open('book.json', 'ab', 'utf=8')

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False, indent=4) + ",\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()