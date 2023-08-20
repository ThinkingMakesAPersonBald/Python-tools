'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2023-06-20 23:13:26
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2023-06-21 00:35:13
FilePath: /Python-tools/AnalyticalOfflineDictionary.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

import os
root_path = '/Users/peixinhua/Desktop/牛津高阶英汉双解词典(第9版)_v20191111'
file_name = '牛津高阶英汉双解词典(第9版).mdx'

from readmdict import MDX, MDD  # pip install readmdict
from pyquery import PyQuery as pq    # pip install pyquery
from bs4 import BeautifulSoup

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
# print(html)

# 从html中提取需要的部分，这里以the little dict字典为例。到这一步需要根据自己查询的字典html格式，自行调整了。
doc = pq(html)
test = doc('sn-gs')
# coca2 = doc('div[class="coca2"]').text().replace('\n','')
# meaning = doc("""div[class="dcb"]""").text()
# test = doc('div[class="licontent"]').text().replace('\n','')
print(test.text().replace('\n',' '))




# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """

# soup = BeautifulSoup(html, 'lxml')

# print(soup.h-g eid="hello_hg_1".string)

# print(soup.title)           # <title>The Dormouse's story</title>
# print(type(soup.title))     # <class 'bs4.element.Tag'>
# print(soup.title.string)    # The Dormouse's story
# print(soup.head)            # <head><title>The Dormouse's story</title></head>
# print(soup.p)               # <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
