'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-08-25 13:51:01
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-08-26 14:39:41
FilePath: /Python-tools/DialogueEffectCompare.py
Description: AIRudder 对话效果数据对比

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''

from cProfile import label
import os
from re import I
from tkinter import font
from turtle import screensize, title, width
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
    value = 0
    if len(values) > 0:
        value = values[0]
    # if not isinstance(value,int):
    #     value = '%.2f'%value
    return value

def data_processing(show_df: pd.DataFrame,list_titles,control_robot_id,test_robot_id):
    # data analysis
    day_df = show_df['day']
    day_drop_duplicates =  day_df.drop_duplicates(keep="first", inplace=False)
    day_values = day_drop_duplicates.values
    x_axis_data = list(dict.fromkeys(day_drop_duplicates.apply(convert_day_format).values))
    # list_titles = ['count','avgbillsec noFG','avgtalkround noFG','A']
    return_dict = {}
    for title in list_titles:
        control_values = []
        test_values = []
        for day in day_values:
            # number of call list data
            control_value = show_df[title][(show_df['robot_id']==control_robot_id) & (show_df['day']==day)].values
            control_values.append(pretect_list_crash(control_value))
            test_value = show_df[title][(show_df['robot_id']==test_robot_id) & (show_df['day']==day)].values
            test_values.append(pretect_list_crash(test_value))
        control_key = title + '_control'
        test_key = title + '_test'
        return_dict[control_key] = control_values
        return_dict[test_key] = test_values
    return_dict['day'] = x_axis_data
    return return_dict
        

def draw_chart(show_df: pd.DataFrame,control_robot_id,test_robot_id):
    list_titles = ['count','avgbillsec noFG','avgtalkround noFG','A','E']
    return_dict = data_processing(show_df=show_df,list_titles=list_titles,control_robot_id=control_robot_id,test_robot_id=test_robot_id)
    x_axis_data = return_dict['day']
    # the wodth of the bars
    width = 0.45
    x = np.arange(len(x_axis_data))
    # plot common setting
    plt.subplots_adjust(hspace=0.1)
    plt.figure(dpi=72,figsize=(16,12))
    control_label = 'Control:{}'.format(control_robot_id)
    test_label = 'Test:{}'.format(test_robot_id)
    # plot 1:
    plt.subplot(3,2,1)
    plt.title(list_titles[0] + ' of call')
    count_rects1 = plt.bar(x - width / 2,return_dict['count_control'],width=width)
    count_rects2 = plt.bar(x + width / 2,return_dict['count_test'],width=width)
    # plt.legend()
    plt.bar_label(count_rects1,padding=3,rotation=90,fontsize= 8)
    plt.bar_label(count_rects2,padding=3,rotation=90,fontsize= 8)
    plt.xticks(ticks=x,labels=x_axis_data,rotation=60)
    plt.tight_layout()
    # plot 2:
    plt.subplot(3,2,2)
    plt.title(list_titles[1])
    avgbillsec_rects1 = plt.bar(x - width / 2,[float('{:.2f}'.format(i)) for i in return_dict['avgbillsec noFG_control']],width=width)
    avgbillsec_rects2 = plt.bar(x + width / 2,[float('{:.2f}'.format(i)) for i in return_dict['avgbillsec noFG_test']],width=width)
    # plt.legend()
    plt.bar_label(avgbillsec_rects1,padding=3,rotation=90,fontsize= 8)
    plt.bar_label(avgbillsec_rects2,padding=3,rotation=90,fontsize= 8)
    plt.xticks(ticks=x,labels=x_axis_data,rotation=60)
    plt.tight_layout()

    # plot 3:
    plt.subplot(3,2,3)
    plt.title(list_titles[2])
    avgtalkround_rects1 = plt.bar(x - width / 2,[float('{:.2f}'.format(i)) for i in return_dict['avgtalkround noFG_control']],width=width)
    avgtalkround_rects2 = plt.bar(x + width / 2,[float('{:.2f}'.format(i)) for i in return_dict['avgtalkround noFG_test']],width=width)
    # plt.legend()
    plt.bar_label(avgtalkround_rects1,padding=3,rotation=90,fontsize= 8)
    plt.bar_label(avgtalkround_rects2,padding=3,rotation=90,fontsize= 8)
    plt.xticks(ticks=x,labels=x_axis_data,rotation=60)
    plt.tight_layout()

    # plot 4:
    plt.subplot(3,2,4)
    plt.title(list_titles[3] + ' label rate')
    A_rects1 = plt.bar(x - width / 2,[float('{:.2f}'.format(i)) for i in return_dict['A_control']],width=width)
    A_rects2 = plt.bar(x + width / 2,[float('{:.2f}'.format(i)) for i in return_dict['A_test']],width=width)
    # plt.legend()
    plt.bar_label(A_rects1,padding=3,rotation=90,fontsize= 8)
    plt.bar_label(A_rects2,padding=3,rotation=90,fontsize= 8)
    plt.xticks(ticks=x,labels=x_axis_data,rotation=60)
    plt.tight_layout()

    # plot 5:
    plt.subplot(3,2,5)
    plt.title(list_titles[4] + ' label rate')
    A_rects1 = plt.bar(x - width / 2,[float('{:.2f}'.format(i)) for i in return_dict['E_control']],width=width,label=control_label)
    A_rects2 = plt.bar(x + width / 2,[float('{:.2f}'.format(i)) for i in return_dict['E_test']],width=width,label=test_label)
    plt.legend()
    plt.bar_label(A_rects1,padding=3,rotation=90,fontsize= 8)
    plt.bar_label(A_rects2,padding=3,rotation=90,fontsize= 8)
    plt.xticks(ticks=x,labels=x_axis_data,rotation=60)
    plt.tight_layout()

    # overview    
    file_name = 'Comparison of control & test effect({} vs {})'.format(control_robot_id,test_robot_id)
    out_put_file_name = './' + file_name + '.png'
    plt.suptitle(file_name)
    # out_put_path = '/Users/peixinhua/Downloads/image'
    # if os.path.exists(out_put_path):
    #     os.makedirs(out_put_path)
    # plt.savefig(os.path.join(out_put_path,file_name + '.jpg'))
    plt.savefig(out_put_file_name)
    plt.show()


if __name__ == '__main__':
    read_excel_data()
    # draw_chart()
    
    