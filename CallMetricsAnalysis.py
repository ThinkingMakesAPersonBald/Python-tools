'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-09-15 14:37:45
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-09-15 17:01:50
FilePath: /Python-tools/CallMetricsAnalysis.py
Description: 根据call 数据明细，统计对应的平均通话时长、平均对话轮次、Intention 分布比例

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''
import os
import pandas as pd
import warnings


root_path = '/Users/peixinhua/Downloads/Action revoke'
content_dict = {}
warnings.simplefilter("ignore")

def judge_file_format():
    file_list = os.listdir(root_path)
    for name in file_list:
        if '.xlsx' in name:
            load_file_content(file_name= name)

def load_file_content(file_name: str):
    file_path = os.path.join(root_path,file_name)
    print(file_path)
    content_df = pd.read_excel(file_path)
    content_df.insert(0,'file name',file_name)
    content_dict[file_name] = content_df

def get_valid_data_list()->pd.DataFrame:
    key_day = ''
    for key in list(content_dict.keys()):
        if 'experiment' in key:
            key_day = key
    day_list = content_dict[key_day]['dt'].drop_duplicates(keep= 'first',inplace= False)
    filter_valid_data(day_list)

def filter_valid_data(data_df: pd.DataFrame):
    temp_dict = {}
    for key in list(content_dict.keys()):
        if 'experiment' not in key:
            temp_df = pd.DataFrame(content_dict[key]) 
            save_df = pd.DataFrame()
            for index,row in data_df.iteritems():
                save_df = save_df.append(temp_df[temp_df['dt'] == row])
                # print(save_df)
            temp_dict[key] = save_df
        else:
            temp_dict[key] = content_dict[key]
    data_statistics(temp_dict)

'''
description: 计算均值和数据分布
return {*}
'''
def data_statistics(para: dict):
    merge_list = []
    for key in list(para.keys()):
        temp_df = pd.DataFrame(para[key])
        avg_bill_sec = temp_df['bill_sec'].mean()
        avg_talk_round = temp_df['valid_talk_round'].mean()
        label_distributed = temp_df['label'].value_counts()
        labels = list(temp_df['label'].drop_duplicates(keep= 'first', inplace= False))
        length = len(temp_df)
        # 将所有数据整合在一个字典里
        merge_dict = {}
        # key_str = str(key).split['.'][0]
        merge_dict['name'] = key
        merge_dict['avg_bill_sec'] = avg_bill_sec
        merge_dict['avg_talk_round'] = avg_talk_round
        # 遍历获取所有label 占比
        # print('avg_bill_sec: {}\n avg_talk_round: {} \n label_distributed: {} \n labels {}'.format(avg_bill_sec,avg_talk_round,label_distributed,labels))
        for label in labels:
            count = label_distributed[label]
            rate = count / length
            name = label + '_rate'
            merge_dict[name] = rate
        merge_list.append(merge_dict)
    merge_df = pd.DataFrame(merge_list)
    merge_df.to_excel(os.path.join('/Users/peixinhua/Downloads/',root_path.split('/')[-1] + '.xlsx'))
    print(merge_df)
    



        
        


                

        





def main():
    judge_file_format()
    get_valid_data_list()
    

if __name__ == '__main__':
    main()


