'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-08-18 11:30:17
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-08-22 14:59:53
FilePath: /Python-tools/ExcelOperations.py
Description: 

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''

import pandas as pd 
import os
import warnings

merge_dire = '/Users/peixinhua/Downloads/annotation file Indonesia'
output_path = 'output.xlsx'
df_list = []

remove_file_path = ''

'''
description: 合并excel 文件
return {*} 合并为一整个的excel文案
'''
def merge_excel_file(dire_path='', output_file_name= ''):
    for f in os.listdir(dire_path):
        print('123131231{}'.format(f))
        if '.xlsx' in f:
            with warnings.catch_warnings(record= True):
                warnings.simplefilter('always')
                f_df = pd.read_excel(dire_path + os.sep + f)
                f_df.insert(0,'file name',f)
                print('f_df{}'.format(f_df))
                df_list.append(f_df)
        
    print('merge data{}'.format(dire_path))

    merde_df = pd.concat(df_list)
    merde_df.to_excel(dire_path + os.sep + output_file_name)

def remove_blank_row_or_column(input_file_path= '',output_file_path= '',row= False, column= False):
    if os.path.isfile(input_file_path):
        df = pd.read_csv(input_file_path)
        if row:
            df.dropna(axis=0,how= 'all')
        elif column:
            df.dropna(axis=1,how= 'all')
        if len(df) > 0:
            print(df)
            df.to_excel(output_file_path)

if __name__ == "__main__":
    # input_file_path = '/Users/peixinhua/Downloads/Action revoke case.csv'
    # output_file_path = '/Users/peixinhua/Desktop/output.xlsx'
    # remove_blank_row_or_column(input_file_path=input_file_path,output_file_path= output_file_path,row= True)
    # merge_excel_file()
    dire_path = '/Users/peixinhua/Downloads/action revoke annotation file Indonesia'
    output_file_name = 'output.xlsx'
    merge_excel_file(dire_path=dire_path,output_file_name=output_file_name)
