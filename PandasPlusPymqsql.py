'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-08-09 16:12:14
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-08-09 17:26:06
FilePath: /Python-tools/PandasPlusPymqsql.py
Description: 

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''

sql_user    = 'root'
sql_passwd  = '123456789'
sql_host    = 'localhost'
sql_port    = 3306
sql_db_name = 'mysql'

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import CHAR,INT

connect_info = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    sql_user,
    sql_passwd,
    sql_host,
    sql_port,
    sql_db_name)
engine = create_engine(connect_info)
# SQL query
sql = 'SELECT * FROM test'
# read data to DataFrame 'df'
df = pd.read_sql(sql= sql,con= engine)

print('df:',df)

# write df to table 'test'
data = {
    'name':['test3','test4','test5','test6'],
    'gender':[1,2,2,2]
}
df = pd.DataFrame(data)

df.to_sql(
    name= 'test',
    con= engine,
    if_exists= 'append',
    index= False,
    dtype={
        'id': INT(),
        'name': CHAR(length=2),
        'gender': INT()
    }
)

read_df = pd.read_sql_table(table_name='test',con= engine)
print('read df',read_df)