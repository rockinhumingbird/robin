import pandas as pd
import numpy as np
from pandas_datareader import data
from pandas.api.types import is_list_like
pd.core.common.is_list_like = pd.api.types.is_list_like
import fix_yahoo_finance as yf
yf.pdr_override()
import numpy as np
import datetime
yf.pdr_override()

%matplotlib inline
import matplotlib.pyplot as plt

data = yf.download('JPM','2018-01-01','2018-08-01')
data.Close.plot()
plt.show()

gafataDict={'g':'GOOG','a':'AMZN','Facebook':'FB',
            'APL':'AAPL','BABA':'BABA','TX':'TCEHY'}
start_date = '2017-01-01'
end_date = '2018-01-01'
babaDf=data.get_data_yahoo(gafataDict['BABA'],start_date, end_date)
googDf=data.get_data_yahoo(gafataDict['a'],start_date, end_date)
amazDf=data.get_data_yahoo(gafataDict['APL'],start_date, end_date)
fbDf=data.get_data_yahoo(gafataDict['Facebook'],start_date, end_date)
applDf=data.get_data_yahoo(gafataDict['APL'],start_date, end_date)
txDf=data.get_data_yahoo(gafataDict['TX'],start_date, end_date)
babaDf.head()
babaDf.index
babaDf.info()
babaDf.dtypes
babaDf.describe()
def change(column):
    buyPrice=column[0]
    curPrice=column[-1]#或者curPrice=column[column.size-1]
    Pricechange=(curPrice-buyPrice)/buyPrice
    PriceCh=Pricechange*100
    return PriceCh
#6家股票的涨跌幅
c1=babaDf['Close']
c2=googDf['Close']
c3=applDf['Close']
c4=amazDf['Close']
c5=fbDf['Close']
c6=txDf['Close']
'''
累计涨幅
'''
#获取收盘价Close这一列的数据
closeCol=txDf['Close']
#调用函数，获取涨跌幅
txChange=change(closeCol)

changeDf=pd.concat([pd.DataFrame([change(c1)],columns =[ 'baba'],index = ['涨跌幅']),
                    pd.DataFrame([change(c2)],columns = ['g'],index = ['涨跌幅']),
                    pd.DataFrame([change(c3)],columns = ['apl'],index = ['涨跌幅']),
                    pd.DataFrame([change(c4)],columns = ['amz'],index = ['涨跌幅']),
                    pd.DataFrame([change(c5)],columns = ['Facebook'],index = ['涨跌幅']),
                    pd.DataFrame([change(c6)],columns = ['tx'],index = ['涨跌幅'])
                   ],axis=1)

changeList = [changeDf.loc['涨跌幅','baba'],changeDf.loc['涨跌幅','g'],
              changeDf.loc['涨跌幅','apl'],changeDf.loc['涨跌幅','amz'],
              changeDf.loc['涨跌幅','Facebook'],changeDf.loc['涨跌幅','tx']]

gafataChangeSer=pd.Series(changeList,
                       index=['baba',
                              'g',
                              'apl',
                             'amz',
                            'Facebook',
                             'tx'])

print(gafataChangeSer)
plt.bar(range(6),gafataChangeSer,align = 'center',color = 'g',alpha = 0.9 )
plt.xticks(range(6),['baba','g','apl','amz','Facebook','tx'])
plt.ylabel('percent')
plt.title('6stockstotal')
#add datalabel to each bar
#enumerate() go through index and data
for x,y in enumerate(gafataChangeSer):
    plt.text(x,y+3,'%.2F' %y,ha='center')
plt.show()
#dayprice
CloseDf=pd.concat([googDf['Close'],#谷歌
                      amazDf['Close'],#亚马逊
                      fbDf['Close'],#Facebook
                      applDf['Close'],#苹果
                      babaDf['Close'],#阿里巴巴
                      txDf['Close']#腾讯 
                 ],axis=1)
#重命名列名为公司名称
CloseDf.columns=['G','amz','Facebook','APL','BABA','TX']

CloseDf.head()
CloseDf.plot(figsize=(10,8))
plt.title('dailyprice')
plt.ylabel('price')
plt.show()

ColDeDf = CloseDf.describe()
ColDeDf

ColStd = ColDeDf.loc['std'].sort_values()#sorting

plt.barh(range(6),ColStd,align = 'center',color = 'b',alpha = 0.9)
plt.yticks(range(6),['tx','apl','Facebook','baba','g','amz'])
plt.xlabel('std')
plt.title('6stockpricecomparison')
plt.show()
CloseDf.boxplot(figsize=(12,10))
plt.title('6boxplot')
plt.ylabel('price')
plt.show()








##quand
import matplotlib.pyplot as plt
import quandl
data2 = quandl.get("WIKI/JPM", start_date="2018-01-01", end_date="2018-08-01", api_key="GnyCuXsAZje9sc1_ExqN")
data2.Close.plot()
plt.show()

###use pip install iexfinannce
from iexfinance import get_historical_data
from datetime import datetime
start_date='2018-07-01'
end_date='2018-08-01'
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

data3 = get_historical_data('MSFT', start=start_date, end=end_date, output_format='pandas')
data3.close.plot()
plt.show()
##MINUTE LEVEL DATA
#!pip install alpha_vantage
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='', output_format='pandas')
data4, meta_data = ts.get_intraday(symbol='JPM',interval='1min', outputsize='compact')
print(data4.head())


###
data.head()
data.index
data.info()
data.dtypes
data.describe()
def change(column):
    buyPrice=column[0]
    curPrice=column[-1]#或者curPrice=column[column.size-1]
    Pricechange=(curPrice-buyPrice)/buyPrice
    PriceCh=Pricechange*100
    return PriceCh
c1=data['Close']

c2=data3['close']
closeCol=data['Close']
closeCol2=data3['close']

change1=change(closeCol)
change2=change(closeCol2)
#output change=7.14

from pandas_datareader import data
import fix_yahoo_finance as yf