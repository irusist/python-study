#coding=utf-8
__author__ = 'zhulixin'

fibs=[0,1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])
print fibs
import math
x = 1
y = math.sqrt
# callable用来判断函数是否可调用
print callable(x)
print callable(y)


def hello(name):
    return 'Hello, ' + name + '!'
print hello('world')
print hello('Gumby')


def fibs(num):
    result = [0,1]
    for i in range(num-2):
        result.append(result[-1] + result[-2])
    return result
print fibs(10)
print fibs(15)


# 文档字符串
def square(x):
    'Calculates the square of the number x.'
    return x*x
# __doc__返回一个方法的说明
print square.__doc__
# help函数返回一个方法的详细说明
print help(square)


# 没有返回值的函数
def test():
    print 'This is printed'
    return
    print 'This is not'
# 打印出This is printed
x = test()
# 打印出None
print x


def try_to_change(n):
    n = 'Mr.Gumby'

name = 'Mrs.Entity'
# 与java一样，不能改变参数的值
try_to_change(name)
print name  # Mrs.Entity


def change(n):
    n[0] = 'Mr.Gumby'
name = ['Mrs.Entity', 'Mrs.Thing']
print change(name)     # None(无返回值)
print name  # ['Mr.Gumby', 'Mrs.Thing']


def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


def lookup(data, label,name):
    return data[label].get(name)


def store(data, full_name):
    names = full_name.split()
    if len(names) == 2:names.insert(1,'')
    labels = 'first','middle','last'
    for label,name in zip(labels,names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]
MyName = {}
init(MyName)
store(MyName, 'Magnus Lie Hetland')
print lookup(MyName, 'last','Hetland') #  ['Magnus Lie Hetland']
store(MyName, 'Robin Hood')
store(MyName, 'Robin Locksley')
print lookup(MyName, 'first', 'Robin')  # ['Robin Hood', 'Robin Locksley']
store(MyName, 'Mr. Gummby')
# ['Robin Hood', 'Robin Locksley', 'Mr. Gummby']
print lookup(MyName, 'middle', '')

# 如果要改变一个值（int），可以将他放在list当中


def hello_1(greeting, name):
    print '%s, %s!' % (greeting, name)


def hello_2(name, greeting):
    print '%s, %s!' % (name, greeting)
hello_1('Hello', 'World') # Hello, World!
hello_2('Hello', 'World') # Hello, World!
# 关键字参数
hello_1(greeting='Hello', name="world") # Hello, World!
hello_2(greeting='Hello', name="world") # Hello, World!


def hello_3(greeting='Hello', name='world'):
    print '%s, %s!' % (greeting, name)
hello_3() #  Hello, world!
hello_3('Greetings')   # Greetings, world!
hello_3('Greetings', 'universe')  # Greetings, universe!
hello_3(name='Gummy')   # Hello, Gummy!


def hello_4(name, greeting='Hello', punctuation='!'):
    print '%s, %s%s' % (greeting, name, punctuation)
hello_4('Mars') # Hello, Mars!
hello_4('Mars', 'Howdy') # Howdy, Mars!
hello_4('Mars', 'Howdy', '...') # Howdy, Mars...
hello_4('Mars', punctuation='.')   # Hello, Mars.
# Top of the morning to ya, Mars!
hello_4('Mars', greeting='Top of the morning to ya')
# 以下语句会抛出异常，非关键字参数必须放在最前面(SyntaxError)
# hello_4(greeting='test','yours')

# 以下语句会抛出异常，当非关键字参数已经制定了一个参数，如果
# 再通过关键字参数指定这个参数的值，不会覆盖，而会抛出异常（TypeError)
# ('Mars', 'greeting', greeting='greeting2')

# 以下语句抛出异常，方法如果有没有指定默认值的参数，则必须在调用的时候传递值(TypeError)
# hello_4()


# 可变参数
def print_params(*params):
    print params
print_params('Testing')   # ('Testing',)
print_params(1, 2, 3)         # (1, 2, 3)


# params是除了第一个参数以外的所有参数组成的元祖，相当于匹配
def print_params2(title, *params):
    print title
    print params

# Params:
# (1, 2, 3)
print_params2('Params:', 1, 2, 3)

# 如果可变参数是空的，则打印出()（空元组）
# Nothing:
# ()
print_params2('Nothing:')


# 可变关键字参数(**表示可以通过关键字参数形式传递多个参数)
# 在方法内部将他转化为字典形式（*，在方法内将他转化为元组）
def print_param3(**params):
    print params
print_param3(x=1,y=2,z=3)   # {'y': 2, 'x': 1, 'z': 3}


# print x,y,z打印出用空格分隔的
def print_param4(x, y, z=3, *pospar, **keypar):
    print x,y,z
    print pospar
    print keypar

# 1 2 3
# (5, 6, 7)
# {'foo': 1, 'bar': 2}
print_param4(1, 2, 3, 5, 6, 7, foo=1, bar=2)
# 1 2 3
# ()
# {}
print_param4(1,2)


# 一次保存多个名字
def store(data, *full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(name) == 2:
            name.insert(1, '')
        labels = 'first', 'middle', 'last'
        for label,name in zip(labels,names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]


# 在方法定义*,则将传递进来的参数value1,value2,value3转化为kwds，在方法中kwds当做tuple来处理,
# 在方法定义**,则将传递进来的参数key1=value1,key2=value2转化为kwds,在方法中kwds当做dict来处理
def story(**kwds):
    return 'Once upon a time,there was a %(job)s called %(name)s.' % kwds


def power(x, y, *others):
    if others:
        print 'Received redundant parameters:', others
    return pow(x, y)


def interval(start, stop=None, step=1):
    """Imitates range() for step > 0"""
    if stop is None:
        start, stop = 0, start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result

# 在调用方法时只有2种形式：
# 1.无关键字参数: value1, value2, value3
# 2.关键字参数: key1=value1, key2=value2, key3=value3
print story(job='king', name='Gumby')   # Once upon a time,there was a king called Gumby.
# Once upon a time,there was a brave knight called Sir Robin.
print story(name='Sir Robin', job='brave knight')
params = {'job': 'language', 'name': 'python'}
# 在调用方法时，用*将传递进来的tuple，list类型的params转化为value1, value2, value3形式的
# 在调用方法时，用**将传递进来的dict类型的params转化为key1=value1, key2=value2, key3=value3形式
print story(**params)      # Once upon a time,there was a language called python.
del params['job']
# Once upon a time,there was a stroke of genius called python.
print story(job='stroke of genius', **params)
print power(2, 3)  # 8
print power(3, 2)  # 9
print power(y=3, x=2)  # 8
params = (5,) * 2
print power(*params)  # 3125
# Received redundant parameters: ('Hello, world',)
# 27
print power(3, 3, 'Hello, world')
print interval(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print interval(1, 5)   # [1, 2, 3, 4]
print interval(3, 12, 4)  # [3, 7, 11]
# Received redundant parameters: (5, 6)
# 81
print power(*interval(3, 7))



x = 1
# 内建的vars函数返回变量所对应的字典，这个产生的scope称为命名空间或作用域
scope = vars()
print scope['x']  # 1


# 每一个函数会在内部创建一个不同于全局变量的命名空间
# 用内建函数globals()创建全局的dict，用locals()创建局部的dict
def combine(parameter):
    print parameter + globals()['parameter']
parameter = 'berry'
combine('Shrub')      # Shrubberry

# 在函数内部，默认赋值的变量是局部变量，如果要申明成全局变量，则用global x进行申明
x = 1


def change_global():
    global x
    x += 1
change_global()
print x  # 2


# 函数的嵌套，在函数内部定义函数，并返回这个函数，这是closure(闭包）
def foo():
    def bar():
        print 'Hello,World!'
    bar()


def multiplier(factor):
    def multiplyByFactor(number):
        return number * factor
    return multiplyByFactor
print multiplier(5)(4) # 20

# 默认情况不能对全局变量进行赋值，nonlocal用global关键字类似，可以对外部变量进行赋值（不是全局变量）


# 递归
def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial(n - 1)
print factorial(3)  # 6


def power(x, n):
    if n == 1:
        return x
    else:
        return x * power(x, n - 1)
print power(2, 5)  # 32


# 二分查找
def search(sequence, number, lower=0, upper=None):
    if upper is None:
        upper = len(sequence) - 1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)
seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print seq   # [4, 8, 34, 67, 95, 100, 123]
print search(seq, 34)  # 2
print search(seq, 100)   # 5


# 对seq(list,tuple)处理的内建函数map,filter,reduce.apply
# 相当于[str(i) for i in range(10)]
print map(str, range(10))   # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def func(x):
    return x.isalnum()   # 不为空，并且只能是字母或数字
seq = ['foo', 'x41', '?!', '***', '43']
# 相当于[x for x in seq if x.isalnum()]
print filter(func, seq)    # ['foo', 'x41', '43']
print filter(lambda x:x.isalnum(), seq)   # ['foo', 'x41', '43']

numbers = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
print reduce(lambda x,y: x+y,numbers) # 1161
print sum(numbers)    # 1161

# 用function(*arg, **keywords)代替了
print apply(lambda x, y: x + y, (2, 3))  # 5

