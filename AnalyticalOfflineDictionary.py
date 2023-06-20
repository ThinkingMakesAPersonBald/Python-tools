'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2023-06-20 23:13:26
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2023-06-20 23:33:41
FilePath: /Python-tools/AnalyticalOfflineDictionary.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# from readmdict import MDX
# mdx = MDX(os.path.join(root_path,file_name))
# definition = mdx['hello']
# print(definition)
# print(mdx.name)
# print(mdx.version)
import os
root_path = '/Users/peixinhua/Desktop/牛津高阶英汉双解词典(第9版)_v20191111'
file_name = '牛津高阶英汉双解词典(第9版).mdx'

# from readmdict import MDX
# import pprint

# # Create an instance of the MDX class and pass the path to your .mdx file
# mdx = MDX(os.path.join(root_path,file_name))

# # Get a list of all the words in the dictionary
# words = mdx.keys()
# print(words)

from readmdict import MDX, MDD  # pip install readmdict
from pyquery import PyQuery as pq    # pip install pyquery

'''
# 如果是windows环境，运行提示安装python-lzo，但
> pip install python-lzo
报错“please set LZO_DIR to where the lzo source lives” ，则直接从 https://www.lfd.uci.edu/~gohlke/pythonlibs/#_python-lzo 下载 "python_lzo‑1.12‑你的python版本.whl" 
> pip install xxx.whl 
装上就行了，免去编译的麻烦
'''

# 加载mdx文件
# filename = "TLD.mdx"
filename = os.path.join(root_path,file_name)
headwords = [*MDX(filename)]       # 单词名列表
items = [*MDX(filename).items()]   # 释义html源码列表
if len(headwords)==len(items):
    print(f'加载成功：共{len(headwords)}条')
else:
    print(f'【ERROR】加载失败{len(headwords)}，{len(items)}')

# 查词，返回单词和html文件
queryWord = 'hello'
wordIndex = headwords.index(queryWord.encode())
word,html = items[wordIndex]
word,html = word.decode(), html.decode()

# 从html中提取需要的部分，这里以the litte dict字典为例。到这一步需要根据自己查询的字典html格式，自行调整了。
# doc = pq(html)
# coca2 = doc('div[class="coca2"]').text().replace('\n','')
# meaning = doc("""div[class="dcb"]""").text()
# print(coca2)
# print(meaning)
