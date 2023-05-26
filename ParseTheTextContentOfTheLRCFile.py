import chardet
import re
import os
root_dictionary = '/Users/peixinhua/Downloads'
file_name = "1.lrc"
# use chardet detect file encode format
with open(os.path.join(root_dictionary,file_name), 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']
# open file and read the connect
with open(os.path.join(root_dictionary,file_name),encoding= encoding) as f:
    lrc_text = f.read()
# parse the lrc content
lyrics = re.findall(r'\[(\d{2}):(\d{2}).(\d{2})\](.*?)\n',lrc_text)
# map all the time and content text, feedback a list of contain/include all mapping result 
# change the time to second, and save the content and time(second) in a dictionary list
# initialize a new dictionary
lyrics_dict = []
for match in lyrics:
    minute = int(match[0])
    second = int(match[1])
    millisecond = int(match[2])
    time = minute * 60 + second + millisecond / 1000
    text = match[3]
    lyrics_dict.append({'time':time,'text':text})
# print the result
print('Lyrics:')
for line in lyrics_dict:
    print(line['time'],line['text'])