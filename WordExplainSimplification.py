
import re
#correct function to resolve the explain simplification
def simplify_defs(defs_str):

    pos_list = ['adj.', 'adv.', 'n.', 'num.', 'pron.', 'v.', 'art.', 'conj.', 'int.', 'prep.', 'abbr.']
    new_value = ''
    for pos in pos_list:
        pos_defs = ''
        pos_regex = '{} (.*)'.format(pos)
        pos_match = re.search(pos_regex, defs_str)
        if pos_match:
            pos_defs = pos_match.group(1)
        if pos_defs:
            defs = pos_defs.split('；')
            if len(defs) > 2:
                simplified_defs = defs[:2]
            else:
                simplified_defs = defs
            new_value += f'{pos}{"；".join(simplified_defs)} '
        if not new_value.endswith(' '):
            new_value += ' '
    return new_value.strip()
# def simplify_defs(defs_str):

#     pos_list = ['adj.', 'adv.', 'n.', 'num.', 'pron.', 'v.', 'art.', 'conj.', 'int.', 'prep.', 'abbr.']
#     new_value = ''
#     for pos in pos_list:
#         pos_defs = ''
#         pos_regex = '{} (.*)'.format(pos)
#         pos_match = re.search(pos_regex, defs_str)
#         if pos_match:
#             pos_defs = pos_match.group(1)
#         if pos_defs:
#             defs = pos_defs.split('；')
#             if len(defs) > 2:
#                 simplified_defs = defs[:2]
#             else:
#                 simplified_defs = defs
#             new_value += f'{pos}{"；".join(simplified_defs)} '
#     return new_value.strip()

# 示例用法
defs_str = 'adv. 大约；将近；到处；（特定位置）四下；闲着；周围；掉头 prep. 关于；目的是；针对；忙于；因为；在……到处；在……四处；在……附近；在……（具有某种品质）；围绕；为……感到 adj. 在场的，可得到的；就要……的；四处走动的；有证据的，在起作用的 n. （About）（法）艾保特（姓氏）'
simplified_defs = simplify_defs(defs_str)
print(simplified_defs)

# import pandas as pd
# import re

# # 精简中文释义的函数
# def simplify_defs(defs_str):
#     pos_list = ['adj.', 'adv.', 'n.', 'num.', 'pron.', 'v.', 'art.', 'conj.', 'int.', 'prep.', 'abbr.']
#     new_value = ''
#     for pos in pos_list:
#         pos_defs = ''
#         pos_regex = '{} (.*)'.format(pos)
#         pos_match = re.search(pos_regex, defs_str)
#         if pos_match:
#             pos_defs = pos_match.group(1)
#         if pos_defs:
#             defs = pos_defs.split('；')
#             if len(defs) > 2:
#                 simplified_defs = defs[:2]
#             else:
#                 simplified_defs = defs
#             new_value += f'{pos}{"；".join(simplified_defs)} '
#         if not new_value.endswith(' '):
#             new_value += ' '
#     return new_value.strip()

# # 读取Excel文件
# df = pd.read_excel('/Users/peixinhua/Downloads/example.xlsx')

# # 对中文释义进行精简，并将结果存储在新的一列中
# df['zh_CN_def_simplified'] = df['中文释义'].apply(simplify_defs)

# # 保存Excel文件
# df.to_excel('/Users/peixinhua/Downloads/example_simplified.xlsx', index=False)

