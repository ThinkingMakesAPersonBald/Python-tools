'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-08-16 13:03:45
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-08-16 13:16:56
FilePath: /Python-tools/PandasMergeExcelFile.py
Description: 

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''

import pandas as pd 
import os
import warnings

merge_dire = '/Users/peixinhua/Downloads/merge'
output_path = 'output.xlsx'
df_list = []

for f in os.listdir(merge_dire):
    print('123131231{}'.format(f))
    if '.xlsx' in f:
        with warnings.catch_warnings(record= True):
            warnings.simplefilter('always')
            f_df = pd.read_excel(merge_dire + os.sep + f)
            f_df.insert(0,'file name',f)
            print('f_df{}'.format(f_df))
            df_list.append(f_df)
    
print('merge data{}'.format(merge_dire))

merde_df = pd.concat(df_list)
merde_df.to_excel(merge_dire + os.sep + output_path)



