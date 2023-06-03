import chardet
import re
import os

def parse_content_accumulation(file_name: str):
    # use chardet detect file encode format
    with open(os.path.join(root_directory,file_name), 'rb') as f:
        result = chardet.detect(f.read())
        encoding = result['encoding']
    # open file and read the connect
    with open(os.path.join(root_directory,file_name),encoding= encoding) as f:
        lrc_text = f.read()
    # parse the lrc content
    lyrics = re.findall(r'\[(\d{2}):(\d{2}).(\d{2})\](.*?)\n',lrc_text)
    # map all the time and content text, feedback a list of contain/include all mapping result 
    # change the time to second, and save the content and time(second) in a dictionary list
    # initialize a new dictionary
    # lyrics_dict = []
    # all_content = ''
    for match in lyrics:
        minute = int(match[0])
        second = int(match[1])
        millisecond = int(match[2])
        time = minute * 60 + second + millisecond / 1000
        text = match[3]
        # all_content += text + '\n'
        with open(os.path.join('/Users/peixinhua/Downloads/New concept English(1~4 MP3 & lrc)',save_file_name),'a') as f:
            f.write(text + '\n')
        # lyrics_dict.append({'time':time,'text':text})
        # lyrics_dict.append({'text':text})
    # print the result
    # print('Lyrics:'+lyrics_dict['text'])
    # for line in lyrics_dict:
        # print(line['time'],line['text'])
root_directory = '/Users/peixinhua/Downloads/New concept English(1~4 MP3 & lrc)/新概念英语第一册 lrc'
lrc_files = [] # initialize a empty list for saveing lrc file names
sorted_list = []
# taversal all files and subdirectory in directory
for root, dirs, files in os.walk(root_directory):
    # taversal all file
    for file_name in files:
        # if the file format is lrc, pick them out
        if file_name.endswith('.lrc'):
            lrc_files.append(int(file_name.split('.')[0]))
            sorted_list = sorted(lrc_files)
save_file_name = 'New concept English 1.txt'
for index in sorted_list:
    name = str(index) + '.lrc'
    parse_content_accumulation(name)

    