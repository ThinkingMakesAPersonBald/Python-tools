'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-08-31 17:16:14
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-09-01 11:32:38
FilePath: /Python-tools/PandasOperateExcel.py
Description: 

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''

from posixpath import split
from urllib.robotparser import RobotFileParser
import pandas as pd
import os

dire_path = '/Users/peixinhua/Downloads/New action revoke'
original_file_path = 'result.csv'
merge_file_path = 'Indonesia Mexico Philippine action revoke annotation.xlsx'
output_file_name = 'output.xlsx'
robot_vs_country = 'robot vs country.xlsx'

original_df = pd.read_csv(os.path.join(dire_path,original_file_path))
merge_df = pd.read_excel(os.path.join(dire_path,merge_file_path))

def raw_data_processing():
    # remove blank row
    original_df = original_df.dropna(axis=0,how= 'all')
    # remove all \t
    original_df.replace(to_replace=[r"\\t|\\n|\\r","\t|\n|\r"],value=['',''],regex= True,inplace= True)
    # remove call start and action end row
    # original_df.drop(original_df[(original_df['Event'] == 'CallStart') | (original_df['Event'] == 'Action End')].index)
    # filer event equal 发生revoke CallID
    filer_df = original_df[original_df['Event'] == '发生 Revoke']
    filer_callid_list = list(filer_df['CallID'].drop_duplicates())
    # print('filer_callid_list {}'.format(len(filer_callid_list)))
    # just get need pandas dataframe data
    result_df = pd.DataFrame(columns= original_df.columns)
    for callid in filer_callid_list:
        temp_df = original_df[original_df['CallID'] == callid]
        temp_df = temp_df.drop(temp_df[(temp_df['Event'] == 'CallStart') 
                                        | (temp_df['Event'] == 'Action End') 
                                        | (temp_df['Event'] == 'SpeakStart') 
                                        | (temp_df['Event'] == 'SpeakEnd') 
                                        | (temp_df['Event'] == 'Start Revoke')
                                        | (temp_df['Event'] == 'End Revoke')].index)
        
        result_df = result_df.append(temp_df)
        # print('temp_df {} result_df {}'.format(temp_df,result_df))
    print('original_df2 {}'.format(result_df))
    result_df.to_excel(os.path.join(dire_path,output_file_name))

def merge_robot_message():
    robot_vs_country_path = os.path.join(dire_path,robot_vs_country)
    robot_vs_country_df = pd.read_excel(robot_vs_country_path)
    robot_message_path = os.path.join(dire_path,merge_file_path)
    robot_message_df = pd.read_excel(robot_message_path)
    left_join = pd.merge(robot_message_df,robot_vs_country_df,on= 'company',how='inner')
    robot_message_df = left_join[['callid','robotname','company','day','Country']]
    robot_message_df = robot_message_df.rename(columns={'callid':'CallID'})
    # join output message
    output_path = os.path.join(dire_path,output_file_name)
    output_df = pd.read_excel(output_path)
    # output message merge robot message
    merge_df = pd.merge(output_df,robot_message_df,on='CallID',how='inner')
    # data decomposition
    split_dict = {'Indonesia':['Shopee','Julo'],
                'Mexico':['Opay','OKAYMOBILE2'],
                'Philippine':['Finupp','OLP']
                    }
    for country in split_dict.keys():
        split_df = merge_df[merge_df['Country'] == country]
        path = os.path.join(dire_path,'{}_annotation.xlsx'.format(country))
        split_df.to_excel(path)
    print('robot_message_df {}'.format(merge_df))



if __name__ == '__main__':
    # if output file exist handle data
    output_path = os.path.join(dire_path,output_file_name)
    if os.path.isfile(output_path):
        merge_robot_message()
    else:
        raw_data_processing()
        