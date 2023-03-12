'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-10-25 17:38:53
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-10-25 17:55:38
FilePath: /Python-tools/PandasMergeCSV.py
Description: Pandas merge csv files
Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''

import pandas as pd
import os
dire_path = '/Users/peixinhua/Downloads/Merge csv'
output_path = '/Users/peixinhua/Downloads'
def main():
    pd_list = []
    for f in os.listdir(dire_path):
        if '.csv' in f:
            file_path = os.path.join(dire_path,f)
            file_df = pd.read_csv(file_path)
            pd_list.append(file_df)
            # print(file_df)
            print(pd_list)
    meger_df = pd.concat(pd_list)
    output_file_path = "output.xlsx"
    print(meger_df)
    meger_df.to_excel(os.path.join(output_path,output_file_path))

if __name__ == "__main__":
    main()
