'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-08-09 11:42:15
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-08-09 12:51:54
FilePath: /Python-tools/ModifyFileName.py
Description: 

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''

import os
import pandas as pd
import random

random.seed(0)
folder_path = '/Users/peixinhua/Downloads/responseOne'
output_path = '/Users/peixinhua/Downloads/output'
# get all files from target folder
file_list = os.listdir(folder_path)
new_name_list = []
old_name_list = []
random_list = random.sample(range(0,250),250)
# print('random list',len(random_list))

i = 0
for file in file_list:
    if '.wav' in file and i < len(random_list):
        old_name = folder_path + os.sep + file
        random_index = random_list[i]
        # print('random index:%s \n' % random_index)
        print('index:',i,len(random_list))
        new_name = output_path + os.sep + str(random_index) + '.wav'
        print('old name:',old_name,'new name:',new_name)
        old_name_list.append(old_name)
        new_name_list.append(new_name)
        os.rename(old_name,new_name)
        i += 1
        
data = {'old_name':old_name_list,'new_name':new_name_list}
df = pd.DataFrame(data)
df.to_excel(output_path + os.sep + 'result.xlsx')

# if __name__ == '__main__':