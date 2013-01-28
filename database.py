# coding=utf-8
__author__ = 'zhulixin'

# http://python.org/peps/pep-0249.html

# python db api模块特性的3个全局变量：
# apilevel 所使用的Python DB API版本，可以为1.0或2.0，如果该变量不存在，则为1.0
# threadsafety 模块的线程安全等级，取值0—3的整数，0表示线程完全不共享模块，3表示模块是完全线程安全的
#　1表示线程本身可以共享模块但不对连接共享
# paramstyle 在SQL查询中使用的参数风格,表示在执行多次类似查询的时候，参数如何被拼接到SQL查询中。
#　‘format’表示标准的字符串格式，可以在参数中进行拼接的地方插入%s
#　‘pyformat’表示扩展的格式代码，用作字典拼接，如%(foo)
#　‘qmark’使用问号，‘numeric’使用:1或:2，‘named’表示:foobar，foobar为参数名


# 在DB API中使用的异常     超类
# StandardError                             所有异常的泛型基类
# Warning               StandardError       在非致命错误发生时引发
# Error                 StandardError       所有错误条件的泛型超类
# InterfaceError        Error               关于接口而非数据库的错误
# DatabaseError         Error               与数据库相关的错误的基类
# DataError             DatabaseError       与数据库相关的问题，比如值超出范围
# OperationalError      DatabaseError       数据库内部操作错误
# IntegrityError        DatabaseError       关系完整性受到影响，比如键检查失败
# InternalError         DatabaseError       数据库内部错误，比如非法游标
# ProgrammingError      DatabaseError       用户编程错误，比如未找到表
# NotSupportedError     DatabaseError       请求不支持的特性（比如回滚）

# connect函数的常用参数
# dsn      数据源名称，给出该参数表示数据库依赖，必选的
# user     用户名，可选的
# password，用户密码，可选的
# host，主机名，可选的
# database，数据库名，可选的


# 连接对象方法
# close(),关闭连接后，连接对象和它的游标均不可用
# commit(),如果支持的话就提交挂起的事务，否则不做任何事
# rollback(),回滚挂起的事务（可能不可用）
# cursor()，返回连接的的游标对象


# 游标对象方法
# callproc(name,[,params])  使用给定的名称和参数（可选）调用已命名的数据库程序
# close()  关闭游标之后，游标不可用
# execute(oper[,params])    执行SQL操作，可能使用参数
# executemany(oper,pseq)    对序列中的每个参数执行SQL操作
# fetchone()        把查询的结果集中的下一行保存为序列，或者None
# fetchmany([size])获取查询结果集中的多行，默认尺寸为arraysize
# fetchall()将所有（剩余）的行作为序列的序列
# nextset()调至下一个可用的结果集（可选）
# setinputsizes(sizes)为参数预先定义内存区域
# setoutputsize(size[,col]) 为获取的大数据值设定缓冲区尺寸

# 游标对象特性
# description   结果列描述的序列，只读
# rowcount      结果中的行数，只读
# arraysize     fetchmany中返回的行数，默认为1


# DB API构造函数和特殊值
# Date(year, month, day)   　创建保存日期值的对象
# Time(hour, minute, second)    创建保存时间值的对象
# Timestamp(y, mon, d, h, min, s) 创建保存时间戳的对象
# DateFromTicks(ticks) 创建保存自新纪元以来秒数的日期值对象
# TimeFromTicks(ticks) 创建保存自新纪元以来秒数的时间值对象
# TimestampFromTicks(ticks) 创建保存来自新纪元以来秒数的时间戳对象
# Binary(string)    创建保存二进制字符串值的对象
# STRING    描述基于字符串列的类型（CHAR)
# BINARY    描述二进制列（比如LONG,RAW， BLOBs）
# NUMBER    描述数字列
# DATETIME  描述日期/时间列
# ROWID 描述行ID列
import sqlite3
conn = sqlite3.connect('test.db')
curs = conn.cursor()
curs.execute('drop table user')
curs.execute('''create table user(id text primary key, name text)''')
query = 'insert into user values(?, ?)'
vals = ['1', 'test']
curs.execute(query, vals)
conn.commit()
conn.close()

conn = sqlite3.connect('test.db')
curs = conn.cursor()
query = 'select * from user'
curs.execute(query)
# curs.fetchall()返回一个list的元组，外面的list表示每条数据，内部的元组表示每条数据的列。
print curs.fetchall()      # [(u'1', u'test')]
# curs.description]是返回一个元组的元组，外层的元组表示每个字段，内部的元组表示每个字段的不同属性，第一个为字段名
print [f[0] for f in curs.description]  #　['id', 'name']
for data in curs.fetchall():
    print data

conn.commit()
conn.close()




