import scrapy
import logging
from ..items import *

class MySpider(scrapy.Spider):
    name = 'dianping'
    allowed_domains = ['www.dianping.com']
    start_urls = [
        'http://www.dianping.com/handan/ch0/r3380p8'
    ]

    def parse(self, response):
        parse_code(response)
        shoplistHref = response.xpath('//a[contains(@data-click-name,"shop_title_click")]/@href')
        shopTitles = response.xpath('//a[contains(@data-click-name,"shop_title_click")]/@title')
        shopCates =  response.xpath('//a[@data-click-name="shop_tag_cate_click"]/span/text()')
        shopRegions = response.xpath('//a[@data-click-name="shop_tag_region_click"]/span/text()')
        shopAddress = response.xpath('//a[@data-click-name="shop_tag_region_click"]/following-sibling::span[1]/text()')
        for i in range(len(shoplistHref)):
            shopItem = ShopItem()
            shopItem['id'] = shoplistHref[i].extract().split('/')[-1]
            shopItem['name'] = shopTitles[i].extract()
            shopItem['region'] = shopCates[i].extract()
            shopItem['type'] = shopRegions[i].extract()
            shopItem['address'] = shopAddress[i].extract()
            logging.debug(shoplistHref[i].extract())
            yield shopItem
            yield scrapy.Request(shoplistHref[i].extract(),meta={'shopid': shopItem['id']}, callback=self.parseShop)

    def parseShop(self, response):
        parse_code(response)
        memberHref = response.xpath('//a[contains(@class,"avatar J-avatar")]/@href')
        logging.debug(memberHref)

        ck = {'_lxsdk_cuid': '1633d38ff6a29-0df713fc956769-3961430f-1fa400-1633d38ff6bc8', 'ctu': '131a9c474a5a29fb40cae328864e914a73ae4a156b4dcd45da90fb7ae4a0da8b', '__mta': '142540301.1526526979482.1526526979482.1526560601876.2', 'dper': 'd4e74a643cf3c30840493d2e62ce30c3da9b0565fdeea8dde376fc83fa23a0d55b3a35c99cd81054c423270933779e0559f3fa50f22ef7b41c561a3a01f37f9544705d9f43b61c9cf413b44a3529653f98d47130b21c716205a04f17109c58d2', '_lx_utm': 'utm_source%3DBaidu%26utm_medium%3Dorganic', 'll': '7fd06e815b796be3df069dec7836c3df', 's_ViewType': '10', 'uamo': '13501203276', 'cy': '27', '_lxsdk_s': '16380f28aa3-912-680-a17%7C%7C13', 'cye': 'handan', '_lxsdk': '1633d38ff6a29-0df713fc956769-3961430f-1fa400-1633d38ff6bc8', 'ua': 'dpuser_1244825374', '_hc.v': 'f6521c84-6605-f814-01d6-268855fbda1e.1525740536'}
        for url in memberHref:
            next_page = response.urljoin(url.extract())
            print(next_page)
            yield scrapy.Request(next_page,meta={'shopid': response.meta['shopid']},callback=self.parseSMember,cookies=ck)

    def parseSMember(self, response):
        parse_code(response)
        name = response.xpath('//h2[@class="name"]/text()').extract()
        sex = response.xpath('//i[contains(@class,"man")]/@class').extract()
        moreinfoTitle = response.xpath('//div[contains(@class,"user-message")]//li/em/text()')
        moreinfo = response.xpath('//div[contains(@class,"user-message")]//li/text()')
        md = {}
        for index in  range(len(moreinfo)):
            it = moreinfoTitle[index].extract()
            ic = moreinfo[index].extract()
            md[it] = ic
            logging.debug(md)
        item = UserItem()
        item['shopid']=response.meta['shopid']
        item['name']=name
        item['sex']=sex
        item['birth'] = md.has_key(u'\u751f\u65e5\uff1a') and md[u'\u751f\u65e5\uff1a'] or None
        item['love'] = md.has_key(u'\u604b\u7231\u72b6\u51b5\uff1a') and md[u'\u604b\u7231\u72b6\u51b5\uff1a'] or None
        item['star'] = md.has_key(u'\u661f\u5ea7\uff1a') and md[u'\u661f\u5ea7\uff1a'] or None
        return item

def parse_code(response):
    if 'verify.meituan.com' in response.url:
        logging.debug('****encounter rebotcode')
