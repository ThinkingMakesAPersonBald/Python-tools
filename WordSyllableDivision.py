'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2023-06-05 21:53:00
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2023-06-06 00:19:39
FilePath: /Python-tools/WordSyllableDivision.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# import os
# import pyphen
# from openpyxl import load_workbook

# root_path = '/Users/peixinhua/Desktop'
# file_name = 'example.xlsx'

# # 初始化音节分割工具
# dic = pyphen.Pyphen(lang='en_US')

# # 加载Excel文件
# wb = load_workbook(os.path.join(root_path,file_name))
# ws = wb['Sheet1']

# # 遍历A列中的单元格，逐个进行音节分割
# for row in ws.iter_rows(min_row=1, min_col=1, values_only=True):
#     words = str(row[0]).split()
#     syllables_list = []
#     for word in words:
#         syllables = dic.inserted(word).split('-')
#         syllables_list.extend(syllables)
#     syllables_str = '-'.join(syllables_list)
#     print(syllables_str)
#     #将分割后的结果填充在B列
#     ws.cell(row=row[0].row, column=2, value=syllables_str)

# #保存Excel文件
# wb.save(os.path.join(root_path,'example_with_syllables.xlsx'))

# import os
# import pyphen
# from openpyxl import load_workbook

# root_path = '/Users/peixinhua/Desktop'
# file_name = 'example.xlsx'

# # 初始化音节分割工具
# dic = pyphen.Pyphen(lang='en_US')

# # 加载Excel文件
# wb = load_workbook(os.path.join(root_path,file_name))
# ws = wb['Sheet1']

# # 遍历A列中的单元格，逐个进行音节分割
# for col in ws.iter_cols(min_row=1, min_col=1, max_col=1, values_only=True):
#     for cell in col:
#         words = str(cell).split()
#         syllables_list = []
#         for word in words:
#             syllables = dic.inserted(word).split('-')
#             syllables_list.extend(syllables)
#         syllables_str = '-'.join(syllables_list)
#         print(syllables_str)
#         # 将分割后的结果填充在B列
#         # ws.cell(row=cell.row, column=2, value=syllables_str)

# # 保存Excel文件
# # wb.save(os.path.join(root_path,'example_with_syllables.xlsx'))


# import os
# import pyphen
# import pandas as pd

# root_path = '/Users/peixinhua/Desktop'
# file_name = 'example.xlsx'

# # 初始化音节分割工具
# dic = pyphen.Pyphen(lang='en_US')

# # 加载Excel文件
# df = pd.read_excel(os.path.join(root_path,file_name), sheet_name='Sheet1')

# # 对A列中的单词进行音节分割
# syllables_list = []
# for word in df['A']:
#     words = str(word).split()
#     syllables = []
#     for word in words:
#         temp = dic.inserted(word).split('-')
#         word_syllables = '-'.join(temp)
#     syllables_list.append(word_syllables)
#     print(syllables_list)
    
# # 将分割后的结果填充在B列
# df['B'] = syllables_list

# # 保存Excel文件
# df.to_excel(os.path.join(root_path,'example_with_syllables.xlsx'), index=False)

import os
import pyphen
import pandas as pd

root_path = '/Users/peixinhua/Desktop'
file_name = 'example.xlsx'

# 初始化音节分割工具
dic = pyphen.Pyphen(lang='en_US')

# 加载Excel文件
df = pd.read_excel(os.path.join(root_path,file_name), sheet_name='Sheet1')

# 对A列中的单词进行音节分割
result_list = []
for word in df['A']:
    syllables_list = []
    words = str(word).split()
    for word in words:
        syllables = dic.inserted(word).split('-')
        syllables_list.append('-'.join(syllables))
    result_list.append(' '.join(syllables_list))
    
# 将分割后的结果填充在B列
df['B'] = result_list

# 保存Excel文件
df.to_excel(os.path.join(root_path,'example_with_syllables.xlsx'), index=False)