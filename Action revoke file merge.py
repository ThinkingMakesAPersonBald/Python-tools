'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-09-06 16:03:51
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-09-09 17:01:00
FilePath: /Python-tools/Action revoke file merge.py
Description: merge indonesia action revoke annotation xlsx files

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''
from heapq import merge
import os
from turtle import left
import pandas as pd
import openpyxl

dire_path = '/Users/peixinhua/Downloads/Meaningful interrupt & action revoke coverage accounting'

file_list = os.listdir(dire_path)

dfs = []
for file_name in file_list:
    if '.xlsx' in file_name:
        path = os.path.join(dire_path,file_name)
        temp_df = pd.read_excel(path)
        name = file_name.split('.')[0]
        temp_df.insert(0,'file_name',name)
        if 'revoke' in name:
            temp_df.insert(2,'revoke type','revoke')
        elif '打断v3' in name:
            temp_df.insert(2,'interrupt type','interrupt')
        # if temp_df.columns[-1] == 'count(DISTINCT call_id)':
        #     temp_df.insert(4,'count(DISTINCT call_id)',0)
        # print('temp_df:\n',temp_df)
        dfs.append(temp_df)

concat_df = pd.concat(dfs[3:5])  
# print('concat_df:\n',concat_df)

for df in dfs:
    df = pd.DataFrame(df)
    if  'revoke type' in df.columns:
        merge_df = df[['robot_id','revoke type']]
        # temp_df = pd.merge(concat_df,merge_df,how= left,on='robot_id')
        concat_df =  concat_df.merge(merge_df,how='left',on='robot_id')
        print(merge_df,concat_df)
    if  'interrupt type' in df.columns:
        merge_df = df[['robot_id','interrupt type']]
        # temp_df = pd.merge(concat_df,merge_df,how= left,on='robot_id')
        concat_df = concat_df.merge(merge_df,how='left',on='robot_id')
        print(concat_df)
# print('concat_df:\n',concat_df)

output_path = os.path.join(dire_path,'output.xlsx')
concat_df.to_excel(output_path)
    


        


