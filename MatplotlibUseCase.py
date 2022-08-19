'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-08-19 16:49:01
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-08-19 17:50:40
FilePath: /Python-tools/MatplotlibUseCase.py
Description: 

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''

import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np
import pandas as pd
import matplotlib.ticker as mtick
from matplotlib.pylab import MultipleLocator

def draw_curve():
    file_path = '/Users/peixinhua/Downloads/Comfortable data calculate.xlsx'
    excel_df = pd.read_excel(file_path)
    x = excel_df['Interval']
    y1 = excel_df['太慢了，接受不了']
    y2 = excel_df['有点慢，能够接受']
    y3 = excel_df['刚刚好']
    y4 = excel_df['有点快，能够接受']
    y5 = excel_df['太快了，接受不了']
    
    fig,ax = plt.subplots()
    ax.plot(np.array(x),np.array(y1) * 100,label= '太慢了，接受不了')
    ax.plot(np.array(x),np.array(y2) * 100,label= '有点慢，能够接受')
    ax.plot(np.array(x),np.array(y3) * 100,label= '刚刚好')
    ax.plot(np.array(x),np.array(y4) * 100,label= '有点快，能够接受')
    ax.plot(np.array(x),np.array(y5) * 100,label= '太快了，接受不了')
    
    fmt = '%0.1f%%'
    yticks = mtick.FormatStrFormatter(fmt)
    # 把x轴的刻度间隔设置为200，并存在变量里
    x_major_locator= MultipleLocator(100)
    #设置y轴的刻度间隔为10，并存在变量里
    y_major_locator= MultipleLocator(10)
    ax.xaxis.set_major_locator(x_major_locator)
    ax.yaxis.set_major_locator(y_major_locator)
    ax.set_xlim(250,5050)
    # ax.set_xlim(np.array(x))
    ax.set_ylim(0,100)
    ax.yaxis.set_major_formatter(yticks)
    ax.set_xlabel('Unit ms')
    ax.set_ylabel('Proportion')
    ax.set_title('Robot comfortable response time of Mexico')
    ax.legend()
    ax.grid(True)
    plt.xticks(rotation=-60)
    plt.show()

if __name__ == '__main__':
    draw_curve()