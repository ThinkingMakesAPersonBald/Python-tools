'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-08-25 13:51:01
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-08-25 16:52:15
FilePath: /Python-tools/DialogueEffectCompare.py
Description: AIRudder 对话效果数据对比

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''

import os
from re import I
from turtle import screensize
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
    draw_chart(show_df= filter_df)
    # print('filter_df {} \n'.format(filter_df))

def draw_chart(show_df: pd.DataFrame):
    print('filter_df {} \n'.format(show_df))
    x_axis_data = show_df['day'][5:]
    y_axis_daya = show_df['count']
    plt.subplots_adjust(hspace=0.5)
    # plot 1:
    # xpoints = np.array([0,6])
    # ypoints = np.array([0,100])
    plt.subplot(2,2,1)
    # plt.plot(xpoints,ypoints)
    plt.title('plot 1')
    plt.xticks(rotation=-60)
    plt.plot(x_axis_data,y_axis_daya)
    # plot 2:
    # x = np.array([1,2,3,4])
    # y = np.array([1,4,9,16])
    plt.subplot(2,2,2)
    # plt.plot(x,y)
    plt.title('plot 2')
    plt.xticks(rotation=-60)
    plt.plot(x_axis_data,y_axis_daya)

    # plot 3:
    plt.subplot(2,2,3)
    plt.title('plot 3')
    plt.xticks(rotation=-60)
    plt.plot(x_axis_data,y_axis_daya)

    # plot 4:
    plt.subplot(2,2,4)
    plt.title('plot 4')
    plt.xticks(rotation=-60)
    plt.plot(x_axis_data,y_axis_daya)

    # overview
    
    plt.suptitle('RUNOOB subplot Test')
    plt.show()


if __name__ == '__main__':
    read_excel_data()
    # draw_chart()
    