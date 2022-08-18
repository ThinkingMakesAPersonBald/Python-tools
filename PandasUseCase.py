'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-08-12 10:16:04
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-08-18 12:00:19
FilePath: /Python-tools/PandasUseCase.py
Description: 

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''

import os
import sys
import pandas as pd

file_dire = '/Users/peixinhua/Downloads/Comfortable response time'
output_path = '/Users/peixinhua/Downloads/output'
mapping_path = '/Users/peixinhua/Downloads/mapping'
g = os.walk(file_dire)
mapping_g = os.walk(mapping_path)
df_list = []

if not os.path.exists(output_path):
    os.makedirs(output_path)

for path, dir_list, file_list in g:
    for file_name in file_list:
        if ".xlsx" in file_name:
            print('file name {}'.format(file_name))
            df = pd.read_excel(os.path.join(path,file_name))
            value = file_name.split(".")
            df.insert(0,'file_name',value[0])
            df.insert(0,'gender','Female')
            df.insert(0,'value',df['File name'].str.split('.').str[0])
            df_list.append(df)

merge_df = pd.concat(df_list)
merge_df.to_excel(os.path.join(output_path,'output1.xlsx'))
print('merge_df {}'.format(merge_df))

mapping_df: pd.DataFrame
for path, dir_list, file_list in mapping_g:
    for file_name in file_list:
        if '.xlsx' in file_name:
            mapping_df = pd.read_excel(os.path.join(path,file_name))
            mapping_df['old_name'] = mapping_df['old_name'].str.split('/').str[-1]
            mapping_df['new_name'] = mapping_df['new_name'].str.split('/').str[-1]
            interval_df = mapping_df['old_name'].str.split('.').str[0].str[44:]
            mapping_df.insert(3,'interval',interval_df)
            mapping_df.insert(4,'value',mapping_df['new_name'].str.split('.').str[0])
            print('mapping_df {}'.format(mapping_df))
result = pd.merge(merge_df,mapping_df,how='left',on='value')
result.to_excel(os.path.join(output_path,'output2.xlsx'))
print("result {}".format(result))