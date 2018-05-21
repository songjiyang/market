# -*- coding: utf-8 -*-

class transCookie:


    def __init__(self, cookie):
      self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = "_lxsdk_cuid=1633d38ff6a29-0df713fc956769-3961430f-1fa400-1633d38ff6bc8; _lxsdk=1633d38ff6a29-0df713fc956769-3961430f-1fa400-1633d38ff6bc8; _hc.v=f6521c84-6605-f814-01d6-268855fbda1e.1525740536; dper=d4e74a643cf3c30840493d2e62ce30c3da9b0565fdeea8dde376fc83fa23a0d55b3a35c99cd81054c423270933779e0559f3fa50f22ef7b41c561a3a01f37f9544705d9f43b61c9cf413b44a3529653f98d47130b21c716205a04f17109c58d2; ua=dpuser_1244825374; ctu=131a9c474a5a29fb40cae328864e914a73ae4a156b4dcd45da90fb7ae4a0da8b; uamo=13501203276; cy=27; cye=handan; s_ViewType=10; __mta=142540301.1526526979482.1526526979482.1526560601876.2; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; ll=7fd06e815b796be3df069dec7836c3df; _lxsdk_s=16380f28aa3-912-680-a17%7C%7C13"
    trans = transCookie(cookie)
    print trans.stringToDict()