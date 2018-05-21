# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import urllib2
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "houseSystem.settings")
django.setup()

# 导入所需要的模块
class houseCrawler():
    def url(self, url):
        html = self.request(url)  ##
        soup = BeautifulSoup(html.text, 'lxml',from_encoding="utf-8")
        return soup
    def parsehouseDetail(self,houseDetail):
        houseTitle = houseDetail.find_all('a', attrs={'class':'houseListTitle'})
        spanInfo = houseDetail.find_all('div', attrs={'class':'details-item'})[0].find_all('span')
        address = houseDetail.find_all('span', attrs={'class':'comm-address'})
        price= houseDetail.next_sibling.next_sibling.find_all('span', attrs={'class':'price-det'})
        unitPrice = houseDetail.next_sibling.next_sibling.find_all('span', attrs={'class':'unit-price'})
        imgSrc = houseDetail.previous_sibling.previous_sibling.find_all('img')[0].get('src')
        picture =  urllib2.urlopen(imgSrc).read()
        houseId =  str(houseTitle[0].get('href'))[37:48]
        pwd = os.getcwd();
        root= os.path.split(pwd)[0]
        filePath = os.path.join(root,'static\\housePicture\\%s.%s'%(houseId,'jpg'))
        fo = open(filePath,'wb')
        fo.write(picture)
        fo.flush()
        fo.close()
        hoinurl  = houseTitle[0].get('href')
        mainsoup = self.url(hoinurl)
        hoin = mainsoup.find_all('div', attrs={'class':'block-wrap'})[0].prettify()
        houseTitle = unicode(houseTitle[0].string).strip()
        houseScale =  unicode(spanInfo[0].string).strip()
        houseArea =  int(unicode(spanInfo[1].string[:-2]).strip())
        houseHeight =  unicode(spanInfo[2].string).strip()
        houseOld =  unicode(spanInfo[3].string).strip()
        houseOwner =  unicode(spanInfo[4].text.replace(u'\ue147','')).strip()
        apartName =  unicode(address[0].string.split(u'\xa0')[0]).strip()
        addressName =  unicode(address[0].string.split(u'\xa0')[2]).strip()
        priceNum = unicode(price[0].find_all('strong')[0].string).strip()
        priceUnit =  unicode(price[0].text.replace(priceNum,'')).strip()
        averageName =  unicode(unitPrice[0].string).strip()
        print '录入1条信息'
    def html(self, href):  ##获得图片的页面地址
        html = self.request(href)
        max_span = BeautifulSoup(html.text, 'lxml').find('div', attrs={'class':'pagenavi'}).find_all('span')[-2].get_text()
        # 这个上面有提到
        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            self.img(page_url)  ##调用img函数

    def img(self, page_url):  ##处理图片页面地址获得图片的实际地址
        img_html = self.request(page_url)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', attrs={'class':'main-image'}).find('img')['src']
        self.save(img_url)

    def save(self, img_url):  ##保存图片
        name = img_url[-9:-4]
        img = self.request(img_url)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    def mkdir(self, path):  ##创建文件夹
        path = path.strip()
        isExists = os.path.exists(os.path.join("E:\mzitu2", path))
        if not isExists:
            print('建了一个名字叫做', path, '的文件夹！')
            os.makedirs(os.path.join("E:\mzitu2", path))
            os.chdir(os.path.join("E:\mzitu2", path))  ##切换到目录
            return True
        else:
            print(path, '文件夹已经存在了！')
            return False

    def request(self, url):  ##这个函数获取网页的response 然后返回
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
            'referer':   "http://www.mzitu.com/100260/2"# 伪造一个访问来源
        }
        content = requests.get(url, headers=headers)
        return content


# 设置启动函数
def main():

    houseC = houseCrawler()  ##实例化
    for page in range(8,9):
        soup = houseC.url('https://taizhou.anjuke.com/sale/p%s/#filtersort'%page)  ##给函数all_url传入参数
        houseDetailList = soup.find_all('div', attrs={'class':'house-details'})
        for houseDetail in houseDetailList:
            houseC.parsehouseDetail(houseDetail)
def getRandomData(pageNum):

    houseC = houseCrawler()  ##实例化
    for page in range(pageNum):
        soup = houseC.url('https://taizhou.anjuke.com/sale/p%s/#filtersort'%page)  ##给函数all_url传入参数
        houseDetailList = soup.find_all('div', attrs={'class':'house-details'})
        for houseDetail in houseDetailList:
            houseC.parsehouseDetail(houseDetail)


main()