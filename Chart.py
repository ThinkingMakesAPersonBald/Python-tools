'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-08-10 15:14:25
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-08-10 15:31:54
FilePath: /Python-tools/Chart.py
Description: 

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''
# #导matplotlib包
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif']=['SimHei']# 设置中文编码
# 准备数据
#主：eurcny和date数据个数要相等
# 汇率
eurcny=[6.8007,6.8007,6.8015,6.8015,6.9060,
        6.8036,6.8025,6.7877,6.7835,6.7858,
        6.7077,6.7463,6.7519,6.7595,6.7669,
        6.7511,6.7511,6.7539,6.3344,6.4432,
        6.7899]
#日期
date=[3,4,5,6,7,
      8,9,10,11,12,
      13,14,15,16,17,
      18,19,20,21,23,24]
#设置画布
plt.figure(dpi=80,figsize=(18,8))

#画图
plt.plot(
    date,eurcny,c='red',#红色
    linestyle='--',#‘--’虚线
    linewidth=2,#
    marker='o',#“o”,实心yuan
    markersize=10,#实心元大小
    markerfacecolor='g',#实心元颜色
    alpha=0.5#透明度
)
#设置网格
plt.grid(linewidth=1,alpha=0.7)
#设置标题
plt.title("汇率曲线",fontsize=26)
#x轴
plt.xlabel("日期",fontsize=16)
#y轴
plt.ylabel("汇率",fontsize=16)
#保存
plt.savefig('t4_rate.png')
#显示
plt.show()



# import matplotlib.pyplot as plt
# import numpy as np

# # plt.style.use('_mpl-gallery')

# # make data
# x = np.linspace(0, 10, 100)
# y = 4 + 2 * np.sin(2 * x)

# # plot
# fig, ax = plt.subplots()

# ax.plot(x, y, linewidth=2.0)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))

# plt.show()