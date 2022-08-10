'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-08-10 10:09:25
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-08-10 10:13:20
FilePath: /Python-tools/GetClass&FunctionName.py
Description: 

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''

import sys

class Test(object):
    def test_function(self):
        print('class name:',{self.__class__.__name__})
        print('function name:',{sys._getframe().f_code.co_name})

if __name__ == "__main__":
    test = Test()
    test.test_function()