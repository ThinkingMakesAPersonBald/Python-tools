
import re

def simplify_defs(defs_str):

    pos_list = ['adj.', 'adv.', 'n.', 'num.', 'pron.', 'v.', 'art.', 'conj.', 'int.', 'prep.', 'abbr.']
    new_value = ''
    simplified_defs = {}
    for pos in pos_list:
        pos_defs = ''
        pos_regex = '{} (.*)'.format(pos)
        pos_match = re.search(pos_regex, defs_str)
        if pos_match:
            pos_defs = pos_match.group(1)
        if pos_defs:
            defs = pos_defs.split('；')
            if len(defs) > 2:
                simplified_defs[pos] = defs[:2]
            else:
                simplified_defs[pos] = defs
    # 重新排列每个词性的释义，以保持输出顺序与输入顺序相同
    for pos in defs_str.split(' '):
        if pos.startswith(tuple(pos_list)):
            new_value += f'{pos}{"；".join(simplified_defs[pos])} '
    return new_value.strip()

import pandas as pd

# 读取Excel文件
df = pd.read_excel('/Users/peixinhua/Downloads/example.xlsx')

# 对中文释义进行精简，并将结果存储在新的一列中
df['zh_CN_def_simplified'] = df['中文释义'].apply(simplify_defs)

# 保存Excel文件
df.to_excel('/Users/peixinhua/Downloads/example_simplified.xlsx', index=False)

