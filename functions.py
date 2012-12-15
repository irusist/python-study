#coding=utf-8
__author__ = 'zhulixin'


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

