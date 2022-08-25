'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-08-25 13:51:01
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-08-25 16:17:35
FilePath: /Python-tools/DialogueEffectCompare.py
Description: AIRudder 对话效果数据对比

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''

import os
from turtle import screensize
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import *
import pandas as pd

data_dire_path = '/Users/peixinhua/Downloads'
file_name = 'Meaningful interrupt & Action revoke数据20220824.xlsx'
robot_list_file_name = 'AB test robot list.xlsx'


def read_excel_data():
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
def get_robot_data(control_robot_id,test_robot_id,test_type,scenes):
    original_df = pd.read_excel(os.path.join(data_dire_path,file_name))
    filter_df = original_df[(original_df['robot_id']==control_robot_id) | (original_df['robot_id']==test_robot_id)]
    print('filter_df {} \n'.format(filter_df))

def draw_chart():
    fig, (ax1,ax2) = plt.subplots(2,1)
    # make a little extra space between the subplots
    fig.subplots_adjust(hspace=0.5)

    dt = 0.01
    t = np.arange(0,30,dt)
    # Fixing random state for reproducibility
    np.random.seed(19680801)
    # white noise 1
    nse1 = np.random.randn(len(t))
    # white noise 1
    nse2 = np.random.randn(len(t))
    r = np.exp(-t / 0.05)
    # colored noise 1
    cnse1 = np.convolve(nse1,r,mode='same') * dt
    # colored noise 2
    cnse2 = np.convolve(nse2,r,mode='same') * dt

    # two signals with a coherent part and a random part
    s1 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse1
    s2 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse2

    ax1.plot(t,s1,t,s2)
    ax1.set_xlim(0,5)
    ax1.set_xlabel('time')
    ax1.set_ylabel('s1 and s2')
    ax1.grid(True)

    cxy, f = ax2.csd(s1,s2,256,1. / dt)
    ax2.set_ylabel('CSD (db)')

    plt.show()


if __name__ == '__main__':
    # read_excel_data()
    draw_chart()
    