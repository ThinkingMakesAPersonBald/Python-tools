'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-08-25 13:51:01
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-08-26 10:21:36
FilePath: /Python-tools/DialogueEffectCompare.py
Description: AIRudder 对话效果数据对比

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''

from cProfile import label
import os
from re import I
from turtle import screensize, width
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# from matplotlib import *
import pandas as pd

data_dire_path = '/Users/peixinhua/Downloads'
file_name = 'Meaningful interrupt & Action revoke数据20220824.xlsx'
robot_list_file_name = 'AB test robot list.xlsx'


def read_excel_data():
    i = 1
    robot_list_df = pd.read_excel(os.path.join(data_dire_path,robot_list_file_name),sheet_name='Sheet2')
    for row in robot_list_df.index:
        # print('row {}'.format(robot_list_df.loc[row]))
        control_id = robot_list_df.loc[row]['Control group Robot ID']
        test_id = robot_list_df.loc[row]['Test group Robot ID']
        test_type = robot_list_df.loc[row]['Test type']
        scenes = robot_list_df.loc[row]['Scenes']
        get_robot_data(control_robot_id=control_id,
                        test_robot_id= test_id,
                        test_type= test_type,
                        scenes= scenes
        )
        i += 1
        if i > 1:
            return

def get_robot_data(control_robot_id,test_robot_id,test_type,scenes):
    original_df = pd.read_excel(os.path.join(data_dire_path,file_name))
    filter_df = original_df[(original_df['robot_id']==control_robot_id) | (original_df['robot_id']==test_robot_id)]
    draw_chart(show_df= filter_df,control_robot_id=control_robot_id,test_robot_id=test_robot_id)
    # print('filter_df {} \n'.format(filter_df))

def convert_day_format(value):
    '''
    description: 将YYYY-MM-DD转化为MM-DD
    return {*} MM-DD format time
    '''    
    new_value = value[5:]
    # print('new_value {}'.format(new_value))
    return new_value

def pretect_list_crash(values):
    if len(values) > 0:
        return values[0]
    return 0

def draw_chart(show_df: pd.DataFrame,control_robot_id,test_robot_id):
    # show_df.rename(columns={'count':'quantity'}, inplace= True)
    day_df = show_df['day']
    day_drop_duplicates =  day_df.drop_duplicates(keep="first", inplace=False)
    day_values = day_drop_duplicates.values
    x_axis_data = list(dict.fromkeys(day_drop_duplicates.apply(convert_day_format).values))
    control_y_axis = []
    test_y_axis = []
    for day in day_values:
        # number of call list data
        control_y = show_df['count'][(show_df['robot_id']==control_robot_id) & (show_df['day']==day)].values
        control_y_axis.append(pretect_list_crash(control_y))
        test_y = show_df['count'][(show_df['robot_id']==test_robot_id) & (show_df['day']==day)].values
        test_y_axis.append(pretect_list_crash(test_y))
    print(control_y_axis)
    print(test_y_axis)
    plt.subplots_adjust(hspace=0.5)
    # plot 1:
    plt.subplot(2,2,1)
    plt.title('plot 1')
    
    # plt.plot(x_axis_data,control_y_axis)
    # the wodth of the bars
    width = 0.35
    x = np.arange(len(x_axis_data))
    print('x:{}'.format(x))
    rects1 = plt.bar(x - width / 2,control_y_axis,width=width,label=control_robot_id)
    rects2 = plt.bar(x + width / 2,test_y_axis,width=width,label=test_robot_id)
    plt.legend()
    plt.bar_label(rects1,padding=3)
    plt.bar_label(rects2,padding=3)
    plt.xticks(ticks=x,labels=x_axis_data,rotation=60)
    plt.tight_layout()
    # plot 2:
    # plt.subplot(2,2,2)
    # plt.title('plot 2')
    # plt.xticks(rotation=60)
    # figure_one_y_axis = show_df['count']
    # plt.plot(x_axis_data,y_axis_daya)

    # plot 3:
    # plt.subplot(2,2,3)
    # plt.title('plot 3')
    # plt.xticks(rotation=60)
    # figure_one_y_axis = show_df['count']
    # plt.plot(x_axis_data,y_axis_daya)

    # plot 4:
    # plt.subplot(2,2,4)
    # plt.title('plot 4')
    # plt.xticks(rotation=60)
    # figure_one_y_axis = show_df['count']
    # plt.plot(x_axis_data,y_axis_daya)

    # overview    
    plt.suptitle('RUNOOB subplot Test')
    plt.show()


if __name__ == '__main__':
    read_excel_data()
    # draw_chart()
    
    