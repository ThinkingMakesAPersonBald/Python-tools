'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2023-06-01 01:17:22
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2023-06-03 00:33:01
FilePath: /Python-tools/New.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import pandas as pd
import pyphen
import os 

# 创建Pyphen对象，用于划分音节
dic = pyphen.Pyphen(lang='en')

root_path = '/Users/peixinhua/Desktop'
file_name = 'Junior high school Vocabulary 2182.csv'

# 读取CSV文件
df = pd.read_csv(os.path.join(root_path,file_name))

# # 遍历每个单词，并将其按照音节进行划分
# for word in df['word']:
#     syllables = dic.inserted(word).split('.')
#     print(syllables)

# 创建Pyphen对象，用于划分音节
dic = pyphen.Pyphen(lang='en')


# 新建一个DataFrame，用于存储划分后的结果
syllables_df = pd.DataFrame(columns=['word', 'syllables'])

# 遍历每个单词，并将其按照音节进行划分
for word in df['word']:
    syllables = dic.inserted(word).split('|')
    syllables_df = syllables_df.append({'word': word, 'syllables': '-'.join(syllables)}, ignore_index=True)

# 将划分后的结果保存到新的CSV文件中
syllables_df.to_csv(os.path.join(root_path,'syllables.csv'), index=False)