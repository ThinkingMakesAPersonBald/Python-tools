# '''
# Author: xinhua.pei xinhua.pei@airudder.com
# Date: 2023-06-01 00:35:34
# LastEditors: xinhua.pei xinhua.pei@airudder.com
# LastEditTime: 2023-06-01 00:42:07
# FilePath: /Python-tools/SplitWordAndOthers.py
# Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
# '''
# import pandas as pd
# import re
# import os

# root_path = '/Users/peixinhua/Desktop'

# # 读取Excel文件
# filename = 'Book5.xlsx'
# df = pd.read_excel(os.path.join(root_path,filename), engine='openpyxl')

# # 自定义一个函数来分割单元格中的单词和其他内容
# def split_words_and_other(cell_value):
#     if isinstance(cell_value, str):
#         words = re.findall(r'\b\w+\b', cell_value)  # 提取单词
#         other = re.sub(r'\b\w+\b', '', cell_value)  # 提取其他内容
#         print('word', words)
#         return words, other
#     else:
#         return None, None

# # 对每个单元格应用 split_words_and_other 函数
# df_split = df.applymap(split_words_and_other)

# # 将结果保存到新的Excel文件中
# output_filename = 'split_excel_output.xlsx'
# with pd.ExcelWriter(os.path.join(root_path,output_filename), engine='openpyxl') as writer:
#     df_split.to_excel(writer, index=False)

import openpyxl
import re

# 打开Excel文件
workbook = openpyxl.load_workbook('example.xlsx')

# 选择第一个工作表
worksheet = workbook.active

# 定义单词的正则表达式
word_regex = re.compile('\w+')

# 遍历每个单元格，并提取其中的单词
for row in worksheet.iter_rows():
    for cell in row:
        if cell.value is not None:
            words = word_regex.findall(str(cell.value))
            for word in words:
                print(word)