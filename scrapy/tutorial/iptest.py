import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
#指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False
snames=['shopid','shopname','type','address','region']
shops = pd.read_table('shop.dat',sep=';',header=None,names=snames,encoding='utf-8')
unames = ['shopid','name','sex','birth','love','star']
users = pd.read_table('user.dat',sep=';',header=None,names=unames,encoding='utf-8')
data = pd.merge(shops,users)


region_count = data.pivot_table('shopid',index='region',aggfunc='count')
region_count.plot(kind='barh')
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(8, 4)
fig.show()
fig.savefig('../../marketAnalysis/static/images/region_count.png')



#不同街道性别分布图
region_sex_count = data.pivot_table('shopid',index='region',aggfunc='count',columns='sex')
region_sex_count = region_sex_count.div(region_sex_count.sum(1),axis=0)
region_sex_count.plot(kind='barh',stacked=True)
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(5, 4)
fig.show()
plt.savefig('../../marketAnalysis/static/images/region_sex_count.png')

#不同街道年龄分布图
data['year']=data['birth'].str.split('-',expand=True)[0]
data['year']=data['year'].astype(int)
data['year']=2018-data['year']
#对年龄进行分段
data['year'] = pd.cut(data['year'],[0,18,25,35,60,100])
region_age_count = data.pivot_table('shopid',index='region',columns='year',aggfunc='count')
region_age_count = region_age_count.div(region_age_count.sum(1),axis=0)
region_age_count.plot(kind='barh',stacked=True)
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(12.8, 6)
fig.show()
fig.savefig('../../marketAnalysis/static/images/region_age_count.png')