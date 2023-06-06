'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2023-03-12 17:30:51
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2023-03-12 18:09:11
FilePath: /Python-tools/ModifyTheNameOfASpecialTypeFile.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os

rootFolder = '/Users/peixinhua/Desktop/1级33册 copy'

def main():
    index = 0
    firstLevelFolders = os.listdir(rootFolder)
    for folderName in firstLevelFolders:
        index = index + 1
        if not folderName.startswith('.'):
            wholeFolderName = os.path.join(rootFolder,folderName)
            for file in os.listdir(wholeFolderName):
                if file.endswith('.mp3'):
                    oldName = os.path.join(wholeFolderName,file)
                    newName = os.path.join(wholeFolderName,folderName + '.'+ file)
                    print(newName)
                    os.rename(oldName,newName)
    pass

if __name__ == '__main__':
    main()