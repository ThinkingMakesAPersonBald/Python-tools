'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-08-12 10:18:29
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-08-12 10:21:15
FilePath: /Python-tools/OsUseCase.py
Description: 

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''

from genericpath import isdir
from importlib.resources import path
import os
if os.path.isdir(path):
    print("it's a directory")
elif os.path.isfile(path):
    print("it's a normal file")
else:
    print("it's a special file(socket,FIFO,device file)")