'''
Author: xinhua.pei
Date: 2022-10-31 13:21:17
LastEditors: xinhua.pei
LastEditTime: 2022-11-03 10:30:56
FilePath: /Python-tools/DrawAChart.py
Description: 

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''
'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-10-31 11:31:07
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-10-31 14:15:31
FilePath: /Python-tools/DrawAChart.py
Description: Draw charts from exle data

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''


from cProfile import label
import os
from turtle import color
import matplotlib
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Arial Unicode MS']
from matplotlib.pylab import datestr2num
import pandas as pd
import numpy as np
# show all mac system fonts
# from matplotlib.font_manager import FontManager
# fm = FontManager()
# mat_fonts = set(f.name for f in fm.ttflist)
# print(mat_fonts)
root_path = '/Users/peixinhua/Downloads'
file_name = 'open_mouth_rate.xlsx'

def load_data_from_xlsx():
    file_path = os.path.join(root_path,file_name)
    original_df = pd.read_excel(file_path)
    # print(original_df.head(10))
    draw_chart(original_df)

def draw_chart(df: pd.DataFrame):
    # # x = df['day'].drop_duplicates(keep='first',inplace=False).reset_index()
    # # x = x.drop('index',axis=1)
    # # x = list(x.drop(columns=['index']).values)
    # # x = range(len(x))
    female_df = df[df['callee_gender'] == 'female'].reset_index()
    male_df = df[df['callee_gender'] == 'male'].reset_index()
    show_df = pd.DataFrame(columns=['day','female','male'])
    show_df['day'] = female_df['day']
    show_df['female'] = female_df['open_mouth_rate']
    show_df['male'] = male_df['open_mouth_rate']
    print(show_df)
    plt.figure(figsize=(10,5))
    plt.title('性别配对与开口率关联性分析(DPD=0)')
    plt.xlabel('日期')
    plt.ylabel('开口率')
    female_df = df[df['callee_gender'] == 'female']
    male_df = df[df['callee_gender']=='male']
    # x_data = female_df['day']
    plt.plot_date(show_df['day'],show_df['female'])
    plt.plot_date(show_df['day'],show_df['male'])
    # plt.legend([show_df['female'],show_df['male']])
    plt.grid(True)
    plt.show()
    # female_df.plot('day','open_mouth_rate')
    # male_df.plot('day','open_mouth_rate')
    # plt.show()
    

    # print(show_df.head(100))
    # # df = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range('1/1/2000', periods=1000), columns=list('ABCD'))
    # # print(df.head(10))
    # show_df = show_df.cumsum()
    # show_df.plot()
    # plt.show()

def main():
    load_data_from_xlsx()


if __name__ == '__main__':
    main()