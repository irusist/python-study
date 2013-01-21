#coding=utf-8
__author__ = 'zhulixin'
import sys
print sys.path

# windwos
# 表示除了在默认的目录中，还需要从以下的目录寻找模块
sys.path.append("E:\projects\ideaProject\exercise\python-study");
# 第一次执行输出Hello, world!
import hello

# linux不能用sys.path.append('~/python')
sys.path.append('/home/yourusername/python')
#sys.path.expanduser('~/python')

# 再次导入就不会执行
import hello

# 一般将模块存放在site-packages目录中。

print __name__      # __main__
print hello.__name__    # hello

# pprint模块打印格式化的数据
import pprint
pprint.pprint(sys.path)

# dir,help,__all,__doc__,__file__
import copy
print dir(copy)
print copy.__all__   # ['Error', 'copy', 'deepcopy']
print help(copy.deepcopy)
print copy.deepcopy.__doc__
print copy.__file__

# sys模块
print sys.argv  # 命令行参数，包括脚本名称
# sys.exit()
print sys.modules
# sys.path
print sys.platform
# sys.stdin sys.stdout sys.stderr


# os模块
import os
print os.environ['PYTHONPATH']
# os.system("ls")
print os.sep
print os.pathsep
print os.linesep
print os.urandom(21)
# os.startfile("")   # 打开文件所在的文件夹（system的参数不能有空格，要用引号包含，startfile参数可以有空格）


# webbrowser模块
import webbrowser
# webbrowser.open("https://github.com")

# fileinput模块
import fileinput
# 可以读取参数传入文件，将每一行作为一个迭代器，可以用for来迭代
# 如python some.py f1.txt f2.txt
print fileinput.input()
fileinput.filename()
fileinput.lineno()
fileinput.filelineno()
fileinput.isfirstline()
fileinput.isstdin()
fileinput.nextfile()
# fileinput.close()

# set模块
print set(range(10))    # set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# set取唯一的值
print set([0, 1, 2, 3, 0, 3])   # set([0, 1, 2, 3])
a = set([1, 2, 3])
b = set([2, 3, 4])
print a.union(b)    # set([1, 2, 3, 4])
print a | b         # set([1, 2, 3, 4])  __or__实现
c = a & b           # __and__实现
print c             # set([2, 3])
print c.issubset(a)     # True
print c <= a            # True  __le__实现
print c.issuperset(a)   # False
print c >= a            # False __ge__实现
print a.intersection(b) # set([2, 3])交集
print a.difference(b)    # set([1])在a中但是不在b中
print a - b              # set([1])  __sub__实现
print a.symmetric_difference(b)     # set([1, 4])相当于(a | b) - (a & b)
print a ^ b             # #set([1, 4]) __xor__实现（异或），相当于symmetric_difference
print a.copy()          #  set([1, 2, 3])
print a.copy() is a     # False

mySet = [set([0, 1, 2, 3, 4]), set([1, 2, 3, 4, 5])]
print reduce(set.union, mySet)  # set([0, 1, 2, 3, 4, 5])


# frozenset
# 不能用set作为另一个set的值
a = set()
b = set()
# a.add(b)    # 异常，以为set是可变的集合
a.add(frozenset(b)) #   用frozenset方法创建一个不可变的集合，通常作用于set的值和dict的键


# heapq模块
# heappush(压入堆）
# heappop(弹出堆最顶层元素)
# heapify(seq)组建堆
# heapreplace(item)，弹出堆最小元素，将新元素推入，比heappop再heappush更搞笑
# nlargest(n,iter),nsmallest(n,iter)利用堆算法返回第n大和第n小的元素
import heapq
from random import shuffle
data = range(10)
shuffle(data)
heap = []
for n in data:
    heapq.heappush(heap, n)
print heap

print heapq.heappop(heap)       # 0
print heapq.heappop(heap)       # 1

heap = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
heapq.heapify(heap)
print heap          #  [0, 1, 5, 3, 2, 7, 9, 8, 4, 6]

print heapq.heapreplace(heap, 0.5)  # 0
print heap          # [0.5, 1, 5, 3, 2, 7, 9, 8, 4, 6]
print heapq.heapreplace(heap, 10)   # 0.5
print heap          # [1, 2, 5, 3, 6, 7, 9, 8, 4, 10]

# collections模块
from collections import deque
q = deque(range(5))
q.append(5)
q.appendleft(6)
print q             # deque([6, 0, 1, 2, 3, 4, 5])
print q.pop()       # 5
print q.popleft()   # 6
q.rotate(3)
print q             # deque([2, 3, 4, 0, 1])
q.rotate(-1)
print q             # deque([3, 4, 0, 1, 2])


# time模块
# python日期元组字段含义
# 0：年，1：月，2：日，3：时，4：分，5：秒（0-61），6：周，7，儒历日（1~366），8：夏时令（0,1,-1）
import time
# 将时间元组转换为字符串
print time.asctime()    # Mon Jan 21 13:21:44 2013
# time.struct_time(tm_year=2013, tm_mon=1, tm_mday=21, tm_hour=13, tm_min=24, tm_sec=20, tm_wday=0, tm_yday=21, tm_isdst=0)
# 全球统一时间用gtime
# 将秒数转化为日期元组
print time.localtime()

# 将日期元组转化为新纪元开始的秒数（与localtime相反）
#　print time.mktime()

# 让解释器等待秒数
# time.sleep()

# 将asctime格式化过的字符串转换为日期元组
# time.strptime()

# 返回新纪元到现在的秒数
print time.time()      # 1358746351.27

# datetime模块支持日期和时间的算法，timeit对代码段执行时间计时


# random模块
import random
# 返回[0, 1)内的数
print random.random()
# 返回0到2的4次方的随机数
print random.getrandbits(4)
# 返回2与4之间的随机实数
print random.uniform(2, 4)
# 返回1到10之间step为2的随机整数
print random.randrange(1, 10, 2)
# 从指定序列中随机选择一个
print random.choice([1, 8, 3, 9])
# 随机排序一个序列
random.shuffle([1, 2, 5, 3, 9])
# 从一个序列中随机选择2个不相同的元素
print random.sample([2, 3, 5, 6, 1], 2)

# 获取2008年1月1日到2009年一月一日的某一天
# -1表示一周中的某天，一年中的某天，夏令时
date1 = (2008, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = time.mktime(date1)
date2 = (2009, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = time.mktime(date2)
random_time = random.uniform(time1, time2)
print time.asctime(time.localtime(random_time))

# 3个骰子，一共6点，投一次的点数
num = 3
sides = 6
sum = 0
for i in range(num):
    sum += random.randrange(sides) + 1
print 'The result is', sum


values = range(1, 11) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['%s of %s' % (v, s) for v in values for s in suits]
random.shuffle(deck)
pprint.pprint(deck[:12])



# shelve模块
import shelve
s = shelve.open('test.dat')
s['x'] = ['a', 'b', 'c']
tmp = s['x']
tmp.append('d')
s['x'] = tmp
print s['x']   # ['a', 'b', 'c', 'd']
s.close()

# re模块
# compile(pattern[,flags]) 根据包含正则表达式的字符串创建模式对象
# search(pattern, string[,flags])在字符串中寻找模式,一旦找到子字符串，函数返回MatchObject（值为True），否则返回None（值为False）
# match(pattern,string[,flags])在字符串开始处匹配模式
# split(pattern,string[,maxsplit=0])根据模式的匹配项来分割字符串
# findall(pattern,string)列出字符串中模式的所有匹配项,返回一个list
# sub(pat,repl,string[,count=0]将字符串中所有pat的匹配项用repl替换
# escape(string)将字符串中所有特殊正则表达式字符转义
import re
print re.split('o(o)', 'foobar')  # ['f', 'o', 'bar']
some_text = 'alpha, beta,,,,gamma delta'
print re.split('[, ]+', some_text, maxsplit=2)   # ['alpha', 'beta', 'gamma delta']
print re.split('[, ]+', some_text, maxsplit=1)   # ['alpha', 'beta,,,,gamma delta']


pat = '[a-zA-Z]+'
text = '"Hm... Err -- are you sure?" he said, sounding insecure.'
# ['Hm', 'Err', 'are', 'you', 'sure', 'he', 'said', 'sounding', 'insecure']
print re.findall(pat, text)

pat = r'[.?\-".]+' # .在[]内不表示任意字符
print re.findall(pat, text)     # ['"', '...', '--', '?"', '.']

pat = '{name}'
text = 'Dear {name}...'
print re.sub(pat, 'Mr. Gummby', text)  # Dear Mr. Gummby...

print re.escape('www.python.org')  # www\.python\.org
print re.escape('But where is the ambiguity?')  # But\ where\ is\ the\ ambiguity\?


# 匹配对象方法
# group([group1, ...])返回第几组的元素，默认为第0组，返回整个字符串
# start([group])返回group组开始索引
# end([group]) 返回group组中的结束索引 + 1
# span([group])返回group组的start和end组成的元组
m = re.match(r'www\.(.*)\..{3}', 'www.python.org')
print m.group(1)      # python
print m.start(1)      # 4
print m.end(1)           # 10
print m.span(1)        # (4, 10)


# 在sub方法中用\n表示pattern的第几组元素
emphasis_pattern = r'\*([^\*]+)\*'
# Hello, <em>world</em>!
print re.sub(emphasis_pattern, r'<em>\1</em>', 'Hello, *world*!')

# 在*和+后面加上?表示非贪婪模式，默认是贪婪模式，尽可能多得匹配模式

# functools模块
# difflib模块计算2个序列的相似程度
# hashlib在加密和安全方面
# csv模块
# timeit模块衡量代码片段运行时间
# profile模块和pstats模块用于代码片段效率全面分析
# trace模块提供代码总的分析（哪部分执行，哪部分没执行),用于测试
# datetime用于时间追踪
# itertools将可迭代对象链接起来，创建返回无限连续整数的迭代器
# logging
# getopt和optparse
# cmd编写命令行解释器






































