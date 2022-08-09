'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-08-09 19:40:53
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-08-09 20:21:22
FilePath: /Python-tools/SqlalchemyExample.py
Description: 

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''
from enum import unique
from operator import index
from sqlalchemy import *
import sqlalchemy as sa

sql_user    = 'root'
sql_passwd  = '123456789'
sql_host    = 'localhost'
sql_port    = 3306
sql_db_name = 'mysql'

connect_info = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    sql_user,
    sql_passwd,
    sql_host,
    sql_port,
    sql_db_name)
engine = sa.create_engine(connect_info)

metadata = MetaData()

print(sa.__version__)

insp = sa.inspect(engine)
insp.has_table("team", schema="dbo")

#1、 设置主键
test1 = Table(
    'test1', metadata,
	Column('id', INTEGER, primary_key=True)
)



# # 2、索引

# test2 = Table(
#     'test2', metadata,
#     Column('id',INTEGER, index= True)
# )

# # 3、唯一约束

# test3 = Table{
#     'test3', metadata,
#     Column('id',INTEGER,unique= True)
# }

# # 4、联合唯一约束

# test4 = Table(
#     'test4', metadata,
#     Column('id', INTEGER, primary=True),
# 	Column('col1', String(20)),
# 	Column('col2', Numeric(20, 4)),
# 	UniqueConstraint('col1', 'col2', name='idx_col1_col2')
# )

# #5、联合主键约束
# # 方法一：
# test5 = Table(
#     'test5',metadata,
#     Column('id',INTEGER),
#     Column('coll', String(20)),
#     PrimaryKeyConstraint('id','coll', name= 'idx_id_col1')
# )
# # 方法二：

# test6 = Table(
#     'test6', metadata,
#     Column('id', INTEGER, primary_key = True),
#     Column('coll', String(20), primary_key = True)
# )