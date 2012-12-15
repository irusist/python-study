#coding=utf-8
__author__ = 'zhulixin'
# 用逗号隔开print语句的内容,打印出以空格分隔的字符串
print 'Age: ', 42
print 1,2,3
print (1,2,3)
name = 'Gumby'
salutation = 'Mr.'
greeting = 'Hello,'
print greeting, salutation,name

# import as
import math as foobar
print foobar.sqrt(4)
from math import sqrt as bar
print bar(4)

# 先令value=(1,2,3)，然后令x,y,z=value
x, y, z = 1,2,3
print x,y,z
x,y = y,x
print x,y
value = 1,2,3
x,y,z = value
print x,y,z
scoundrel = {'name' : 'Robin', 'girlfriend' : 'Marion'}
# 返回一个元组
key, value = scoundrel.popitem()
print key,value

# 以下语句都会抛出异常
# x,y,z = 1,2
# x,y = 1,2,3

x = 2
x += 2
print x

# False None 0 "" () [] {}都是假，其他的所有都是真
# False为0，True为1
print True == 1
print False == 0
print True + False + 23

# 用bool函数将其他值转换成True或False
print bool("I think, therefore I am")
print bool(42)
print bool('')
print bool(0)
print bool(())
print bool([])
print bool({})

name = 'dddGumbyd'
if name.endswith('Gumby'):
    print 'Hello, Mr. Gumby'
else:
    print 'Hello, stranger'

num = 2
if num > 0:
    print 'The number is positive'
elif num < 0:
    print 'The number is negative'
else:
    print 'The number is zero'

# 比较运算符
# 判断2个对象是否相等，使用is判断2个对象是否是同一个对象
x == y
x < y
x > y
x >= y
x <= y
x != y
# 同一运算符
x is y
x = y = [1,2,3]
z = [1,2,3]
print x == y #True
print x == z #True
print x is y #True
print x is z #False
x is not y
x in y
x not in y
# 0 < age < 10  #比较运算符的连接

# 字符串比较
print 'alpha' < 'beta' #True
print [1,2] < [2,1]      # True
print [2,[1,4]] < [2,[1,5]]    #True
# 查询字母的顺序
print ord('a') # 97
print chr(98)  # b

# and,or 连接2个布尔值,是逻辑与和逻辑或（有短路规则），not取反操作
print True and False
print True or False
print not False


print 1 if True else 2 # 1

# 断言assert
age = 10
assert 0 < age < 100
age = -1
# 以下抛出异常
#　assert 0 < age < 100,'The age must be realistic'

# while语句
x = 1
while x <= 10:
    print x
    x += 1

# for语句
words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print word

# range函数生成一个从start到end（不包括end）的列表（list），
print range(0,10)       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print range(10)         # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# xrange生成一个可迭代的对象，效率比range高
counter = xrange(10)
print counter[9]

# 对字典的遍历，得到的是key
d = {'x' : 1, 'y' : 2, 'z' : 3}
for key in d:
    print key, 'corresponds to', d[key]

print d.items()   # [('y', 2), ('x', 1), ('z', 3)]
#
for key, value in d.items():
    print key, 'corresponds to', value


# 并行迭代
names = ['name', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
# 生成对应元组当成一个元素，组成的列表
#  [('name', 12), ('beth', 45), ('george', 32), ('damon', 102)]
print zip(names, ages)
for name,age in zip(names, ages):
    print name, 'is', age, 'years old'

# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
# 不能用range替换xrange，因为用range的话，会计算所有的数字，而xrange只计算前5个数字
print zip(range(5), xrange(100000))


# enumerate函数生成以索引，值组成的元组为值组成的列表
strings = ['xxx', 'aaa', 'bbb', 'xxx', 'ccc']
for index,string in enumerate(strings):
    if 'xxx' in string:
        strings[index] = '[censored]'
print strings

# sorted,reversed函数
# sorted返回列表
print sorted([4,3,6,8,3])
print sorted('Hello,world!')
# reversed返回可迭代的对象
print reversed('Hello,world!')
# 将reversed的可迭代对象调用list函数转化成list
print list(reversed('Hello,world!'))
# 可以将reversed的可迭代对象在for语句中
for string in reversed('Hello,world!'):
    print string
# 可以用string.join来操作reversed的可迭代对象.生成一个新的字符串
print ''.join(reversed('Hello,world!'))


#  break语句跳出循环
from math import sqrt
for n in range(99,0,-1):
    root = sqrt(n)
    if root == int(root):
        print n
        break

# continue跳出当前循环继续,推荐优先使用break
# 推荐使用while True： break的语句
from math import sqrt


# 在for语句的后面加上else语句，表示没有执行过for语句就执行else，否则就不执行
for n in range(99,81,-1):
    root = sqrt(n)
    if root == int(root):
        print n
        break
else:
    print "Didn't find it"



# 列表推导式 [x*x for x in range(10)]生成一个列表
print [x*x for x in range(10)] # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print [x*x for x in range(10) if x % 3 ==0] # [0, 9, 36, 81]

# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
print [(x,y) for x in range(3) for y in range(3)]

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
# ['chris+clarice', 'arnold+alice', 'bob+bernice']
print [b + '+' + g for b in boys for g in girls if b[0] == g[0]]


# 将女孩第一个字母，和女孩名字组成一个字典
# 然后遍历男孩，效率比上一个要高
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print [b + '+' + g for b in boys for g in letterGirls[b[0]]]

# pass语句用来表示什么都不做

# del语句删除某个变量,删除的只是变量这个名称，并不是内存中的具体数据
# Python是通过垃圾回收来删除内存的值的，不能通过del
x = 1
del x
# NameError： name 'X' is not defined
# print x

x = ["hello", "world"]
y = x
y[1] = "python"
#　['hello', 'python']
print x
del x
# ['hello', 'python']
print y


# exec语句，无返回值
exec "print 'hello,world!'"

# 默认将sqrt存放在当前的命名空间中，这样sqrt就为1，覆盖了math的sqrt
from math import sqrt
exec "sqrt = 1"
# TypeError: 'int' object is not callable
# sqrt(4)

from math import sqrt
scope = {}
exec 'sqrt = 1' in scope
print sqrt(4)       # 2.0
print scope['sqrt'] # 1
print len(scope)   # 2
print scope.keys()   # ['__builtins__', 'sqrt']


# eval函数,有返回值
print eval("6 + 19 * 2")
exec "6 + 19 * 2" # 无返回值
# eval(raw_input(...)) 就相当于input(...)


scope = {}
scope['x'] = 2
scope['y'] = 3
print eval('x * y',scope)

scope = {}
exec 'x = 2' in scope
print eval('x * x', scope)