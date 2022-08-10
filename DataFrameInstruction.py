'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-08-10 12:43:30
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-08-10 13:26:24
FilePath: /Python-tools/DataFrameInstruction.py
Description: 

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''

import numpy as np
import pandas as pd

#测试数据。
df = pd.DataFrame(data = [['lisa','f',22],['joy','f',22],['tom','m','21']],index = [1,2,3],columns = ['name','sex','age'])
print(df)
# 增
# 按列增加
citys = ['ny','zz','xy']
#在第0列，加上column名称为city，值为citys的数值。
df.insert(0,'city',citys) 
jobs = ['student','AI','teacher']
#默认在df最后一列加上column名称为job，值为jobs的数据。
df['job'] = jobs 
#在df最后一列加上column名称为salary，值为等号右边数据。
# df.loc[:,'salary'] = ['1k','2k','2k','2k','3k']
# 按行增加
#若df中没有index为“4”的这一行的话，该行代码作用是往df中加一行index为“4”，值为等号右边值的数据。
#若df中已经有index为“4”的这一行，则该行代码作用是把df中index为“4”的这一行修改为等号右边数据。
df.loc[4] = ['zz','mason','m',24,'engineer']
df_insert = pd.DataFrame({
    'name':['mason','mario'],'sex':['m','f'],'age':[21,22]},index = [4,5])
#返回添加后的值，并不会修改df的值。ignore_index默认为False，意思是不忽略index值，即生成的新的ndf的index采用df_insert中的index值。
# 若为True，则新的ndf的index值不使用df_insert中的index值，而是自己默认生成。
ndf = df.append(df_insert,ignore_index = True) 

# 查
# 方法一：df['column_name'] 和df[row_start_index, row_end_index] 
df['name']
df['gender']
#选取多列，多列名字要放在list里
df[['name','gender']] 
#第0行及之后的行，相当于df的全部数据，注意冒号是必须的
df[0:]
#第2行之前的数据（不含第2行）    
df[:2] 
#第0行   
df[0:1]  
#第1行到第2行（不含第3行）
df[1:3]
#最后一行   
df[-1:]  
#倒数第3行到倒数第1行（不包含最后1行即倒数第1行，这里有点烦躁，因为从前数时从第0行开始，从后数就是-1行开始，毕竟没有-0） 
df[-3:-1] 
# 方法二：df.loc[index,column] 
# df.loc[index, column_name],选取指定行和列的数据
# 'Snow'
df.loc[0,'name'] 
#选取第0行到第2行，name列和age列的数据, 注意这里的行选取是包含下标的。
df.loc[0:2, ['name','age']]  
#选取指定的第2行和第3行，name和age列的数据        
df.loc[[2,3],['name','age']]     
#选取gender列是M，name列的数据     
df.loc[df['gender']=='M','name']    
#选取gender列是M，name和age列的数据  
df.loc[df['gender']=='M',['name','age']] 

# 方法三：iloc[row_index, column_index]
#第0行第0列的数据，'Snow'
df.iloc[0,0] 
#第1行第2列的数据，32        
df.iloc[1,2]         
#第1行和第3行，从第0列到第2列（不包含第2列）的数据
df.iloc[[1,3],0:2]   
#第1行到第3行（不包含第3行），第1列和第2列的数据
df.iloc[1:3,[1,2]]  

# 改
# 改行列标题
#尽管我们只想把’sex’改为’gender’，但是仍然要把所有的列全写上，否则报错。
df.columns = ['name','gender','age'] 
#只修改name和age。inplace若为True，直接修改df，否则，不修改df，只是返回一个修改后的数据。
df.rename(columns = {
    'name':'Name','age':'Age'},inplace = True) 
#把index改为a,b,c.直接修改了df。
df.index = list('abc')
#无返回值，直接修改df的index。
df.rename({1:'a',2:'b',3:'c'},axis = 0,inplace = True)
# 改数值
# <1>使用loc
#修改index为‘1’，column为‘name’的那一个值为aa。
df.loc[1,'name'] = 'aa'       
#修改index为‘1’的那一行的所有值。       
df.loc[1] = ['bb','ff',11]         
#修改index为‘1’，column为‘name’的那一个值为bb，age列的值为11。  
df.loc[1,['name','age']] = ['bb',11] 
# <2>使用iloc[row_index, column_index]
#修改某一无素
df.iloc[1,2] = 19        
#修改一整列      
df.iloc[:,2] = [11,22,33]     
#修改一整行
df.iloc[0,:] = ['lily','F',15] 

# 删
# 删除行
#删除index值为1和3的两行，
df.drop([1,3],axis = 0,inplace = False)
# 删除列
#删除name列。
df.drop(['name'],axis = 1,inplace = False)  
#删除name列。
del df['name']       
#删除age列，操作后，df都丢掉了age列,age列返回给了ndf。
ndf = df.pop('age')  
