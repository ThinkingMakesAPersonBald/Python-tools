'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-08-07 11:45:47
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-08-07 11:54:21
FilePath: /Quantitative-trading-main/Singleton.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from threading import RLock

class Singleton(object):

    single_lock = RLock()

    def __init__(self, name):
        if hasattr(self, 'name'):
            return
        self.name = name

    def __new__(cls, *args, **kwargs):
        with Singleton.single_lock:
            if not hasattr(Singleton, '_instance'):
                Singleton._instance = object.__new__(cls)
        return Singleton._instance        
if __name__ == '__main__':
    object_1 = Singleton('First create')
    object_2 = Singleton('Second create')
    print(object_1 is object_2)
    print(id(object_1))
    print(id(object_2))