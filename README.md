#### 这个系统分为爬虫，分析，和显示三个模块，爬取数据模块不是特别的完善，因为用户信息作为大众点评的核心信息，有很好的反爬虫机制，所以爬取的时候只能手动切换Cookie和降低访问频率来爬取数据。

- 爬取命令 ，找到对应文件位置

	e:

	cd market\scrapy\tutorial

	scrapy crawl dianping

	会在当前目录增加数据文件，user.dat,shop.dat

	注意事项：爬取前更改url，当爬取无反应的时候换cookie
- 分析数据

	e:

	cd market\scrapy\tutorial

	ipython

	%run iptest.py

	会显示图像,也会在static/images/下面生成region_age_count.png，region_sex_count.png，region_count.png，供页面显示用
- 访问页面

	在项目下run manage.py ,页面访问[地址](http://127.0.0.1:8000/market/index#)。