'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2023-08-19 20:58:05
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2023-08-20 09:43:35
FilePath: /undefined/Users/peixinhua/Documents/微云同步文件夹/Code/python code/Dictionary/get example sentence from oxford.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from readmdict import MDX, MDD  # pip install readmdict
from pyquery import PyQuery as pq    # pip install pyquery
from bs4 import BeautifulSoup
import os
import glob
import pandas as pd
import traceback

# 加载mdx文件
filename = "/Users/peixinhua/Desktop/牛津高阶英汉双解词典(第9版)_v20191111/牛津高阶英汉双解词典(第9版).mdx"
headwords = [*MDX(filename)]       # 单词名列表
items = [*MDX(filename).items()]   # 释义html源码列表
if len(headwords)==len(items):
    print(f'加载成功：共{len(headwords)}条')
else:
    print(f'【ERROR】加载失败{len(headwords)}，{len(items)}')

def queryWordExample(queryWord):
    # 查词，返回单词和html文件
    wordIndex = headwords.index(queryWord.encode())
    word,html = items[wordIndex]
    word,html = word.decode(), html.decode()

    soup = BeautifulSoup(html,'lxml')
    tags = soup.find_all('x')
    text = ''
    for tag in tags:
        if tag and 'wd' in tag.attrs:
            wd_value = tag['wd']
            chn_element = tag.find('chn')
            if chn_element is not None:
                chn_text = chn_element.text.strip()
                text += wd_value + '|' + chn_text + '\n'
    print(text)
    return text

# 读取单词到DataFrame

desktopPath = '/Users/peixinhua/Desktop/Oxford dictionary/' 
wordsDataFrame = pd.read_excel(desktopPath + 'words.xlsx',header=None, names=('Index','words'))
total = len(wordsDataFrame) # 所有单词数量
outputDirectory = desktopPath + 'words_explain_output'
if not os.path.exists(outputDirectory):
    os.makedirs(outputDirectory)

def mergeAllFiles():
    outputCsvFile = 'output.csv'
    outputXlsxFile = 'output.xlsx'
    allFiles = glob.glob(os.path.join(outputDirectory,'words_with_explain_*.csv'))
    dataFromEachFiles = (pd.read_csv(f,sep=',') for f in allFiles)
    dataMerge = pd.concat(dataFromEachFiles,ignore_index=True,sort=True)
    dataMerge.to_csv(outputDirectory + '/' +outputCsvFile)
    dataMerge.to_excel(outputDirectory + '/' +outputXlsxFile)


count = 1
duration = 500

for pages in range(0, total // duration + 1):
    limit = (pages + 1) * duration
    if count >= limit:
        continue

    explainFile = outputDirectory + '/' + 'words_with_explain_' + str(pages) + '.csv'
    while count < limit and count < total:
        word = wordsDataFrame.loc[count, 'words']
        try:
            if word.encode() in headwords:  # 检查单词是否存在于headwords列表中
                example = queryWordExample(word)
                wordsDataFrame.loc[count, 'example'] = example or 'NA'
                print('Index: {}'.format(count), example)
            else:
                wordsDataFrame.loc[count, 'example'] = 'NA'  # 单词不存在，将example设置为'NA'
                print('Index: {}'.format(count), 'Word not found: {}'.format(word))
            
            count += 1
        except:
            traceback.print_exc()
            wordsDataFrame[pages * duration:count].to_csv(explainFile)
            exit(1)

    wordsDataFrame[pages * duration:count].to_csv(explainFile)
mergeAllFiles()