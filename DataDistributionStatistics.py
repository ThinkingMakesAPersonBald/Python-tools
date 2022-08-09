'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-08-09 13:43:46
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-08-09 15:31:41
FilePath: /Python-tools/DataDistrubutionStatistics.py
Description: 

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data_path = '/Users/peixinhua/Downloads/nlu_100ms.csv'

df = pd.read_csv(data_path)
# print('max',df['Time out'].max(),'min',df['Time out'].min())
bins = [0,50,100,150,200,250,300,350,400,450]
labels = ['50ms','100ms','150ms','200ms','250ms','300ms','350ms','400ms','450ms']
df['分层'] = pd.cut(df['Time out'],bins,labels= labels)
aggResult = df.groupby(
    by= ['分层']
)
print('aggResult:',aggResult.sum())
test_df = pd.DataFrame(aggResult.sum())
print('test_df',test_df)
# pAggResult=round(
#         aggResult/aggResult.sum(),
#         2,
#         )*100
# print('pAggResult:',pAggResult)
# print(len(df['分层']))
# df['分层'].hist()
# plt.show()

# data['年龄分层']=pandas.cut(
#         data.年龄,
#         bins,
#         labels=labels
#         )
# 根据年龄分层进行分布分析

# aggResult=data.groupby(
#         by=['年龄分层']
#         )['年龄'].agg({
#                 '人数': numpy.size
#                 })
# # 使用百分比的形式进行数据的展示

# # 第一种

# pAggResult=round(
#         aggResult/aggResult.sum(),
#         2,
#         )*100

# # 第二种

# pAggResult['人数'].map('{:,.2f}%'.format)



# import pandas
# # 查看年龄的分布情况
# import numpy

# data=pandas.read_csv(data_path)


# aggResult=data.groupby(
#         by=['Time out']
#         )['年龄'].agg({
#                 '人数': numpy.size
#                 })

# # 分组查看
# # bins 分组的划分数组
# bins=[
#       min(data.年龄)-1,20,30,40,max(data.年龄)+1
#       ]
# # 分组的自定义标签

# labels=[
#         '20岁以及以下','21岁到30岁','31岁到40岁','41岁以上'
#         ]

# data['年龄分层']=pandas.cut(
#         data.年龄,
#         bins,
#         labels=labels
#         )
# # 根据年龄分层进行分布分析

# aggResult=data.groupby(
#         by=['年龄分层']
#         )['年龄'].agg({
#                 '人数': numpy.size
#                 })
# # 使用百分比的形式进行数据的展示

# # 第一种

# pAggResult=round(
#         aggResult/aggResult.sum(),
#         2,
#         )*100

# # 第二种

# pAggResult['人数'].map('{:,.2f}%'.format)