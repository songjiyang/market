# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from items import *
class TutorialPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item,UserItem):
            data = '%s;%s;%s;%s;%s;%s\n'%(item['shopid'].encode('utf-8'),item['name'][0].encode('utf-8'),item['sex'][0].encode('utf-8'),item['birth'].encode('utf-8'),item['love'].encode('utf-8'),item['star'].encode('utf-8'),)
            with open('user.dat','a') as f:
                f.writelines(data)
        elif isinstance(item,ShopItem):
            data = '%s;%s;%s;%s;%s\n' % (
            item['id'].encode('utf-8'), item['name'].encode('utf-8'), item['region'].encode('utf-8'),
            item['address'].encode('utf-8'), item['type'].encode('utf-8'))
            with open('shop.dat', 'a') as f:
                f.writelines(data)
        return item

    def close_spider(self, spider):
        pass