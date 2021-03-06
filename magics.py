#coding=utf-8
__author__ = 'zhulixin'

# Alex Martelli	Python技术手册 python in a nutshell
# http://code.google.com/p/vitess/
# http://www.juvenxu.com/2011/08/05/infoq-maven-time-to-upgrade-to-maven3/
# http://stackoverflow.com/questions/1979957/maven-dependency-for-servlet-3-0-api
# http://lotusyu.iteye.com/
# http://www.iteye.com/topic/1114835
# http://www.iteye.com/news/22836-aviator-2-1-1-released
# http://stackoverflow.com/tags/scala/info
# http://timyang.net/erlang/erlang-programming/
# http://www.myoops.org/cocw/mit/Global/all-courses.htm#Electrical Engineering and Computer Science
# https://groups.google.com/forum/?fromgroups=#!forum/cn-clojure
# http://hbtc2012.hadooper.cn/
# http://hbase.apache.org/team-list.html
# http://ftp.twaren.net/Linux/CentOS/5.8/isos/i386/
# http://justjavac.iteye.com/?page=35
# https://my.vmware.com/group/vmware/evalcenter?p=vmware-workstation9&source=evap#
# http://developer.51cto.com/art/201106/270812.htm
# http://code.google.com/p/gerrit/
# http://www.python.org/ftp/python/
# http://ftp.python.org/ftp/python/2.7.3/
# https://github.com/tumblr
# http://twitter.github.com/effectivescala/index-cn.html
# https://github.com/dabloem
# https://chrome.google.com/webstore/category/home?hl=zh-CN

# http://mathworld.wolfram.com/Graph.html
# http://mathworld.wolfram.com/Tree.html
# http://xlinux.nist.gov/dads//HTML/tree.html
# http://xlinux.nist.gov/dads//HTML/graph.html


# 实例化一个类时，会调用__init__方法，相当于构造方法
# __del__方法在对象被垃圾回收的时候调用，相当于java的finalize方法
class FooBar:
    def __init__(self, value):
        self.somevar = value

f = FooBar('This is a constructor argument')
print f.somevar     # This is a constructor argument


# 重写构造方法
class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print 'Aaaah...'
            self.hungry = False
        else:
            print 'No, thanks!'
b = Bird()
b.eat()     # Aaaah...
b.eat()     # No, thanks!

class SomeBird(Bird):
    def __init__(self):
        #　Bird.__init__(self)  # 此处调用父类的构造方法
        # super(SomeBird, self).__init__()  # 调用哦super
        self.sound = 'Squawk!'

    def sing(self):
        print self.sound
sb = SomeBird()
sb.sing()           #  Squawk!

# 因为重写了构造方法，而且在重写的方法中没有调用super,没有hungry属性
# AttributeError: SomeBird instance has no attribute 'hungry'
#　sb.eat()


# __getitem__(self, key)方法用于获取元素,如s[1]
# __setitem__(self, key, value)方法用于设置元素，如s[2] = 3,不能修改的对象不能有这方法
# __len__(self)方法用于获取元素长度,如len(s)，如果__len__()返回0，并且没有重写__nonzero__，
#　对象会被当作一个布尔变量中的假值（空的列表，元组，字符串，字典也一样）
# __delitem__(self, key)方法用于删除元素，如del s[2],不能修改的对象不能有这方法


# 对于一个序列，如果键是负数，那么要从末尾开始计数
# 如果键时不合适的类型（如对序列使用字符串做键）会引发一个TypeError异常(python语言标准索引应该为int或long)
# 如果序列的索引是正确的类型，但超出了范围，应该引发一个IndexError异常
def checkIndex(key):
    if not isinstance(key, (int, long)):
        raise TypeError
    if key < 0:
        raise IndexError


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        """Get an item from the arithemetic sequence."""
        checkIndex(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + self.step * key

    def __setitem__(self, key, value):
        checkIndex(key)
        self.changed[key] = value
s = ArithmeticSequence(1, 2)
print s[4]  # 9

# TypeError
# print s['a']

# IndexError
# print s[-1]

s[4] = 2
print s[4]  # 2
print s[5]  # 11

# AttributeError
# del s[5]

# AttributeError
# len(s)


class CounterList(list):
    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)
cl = CounterList(range(10))
print cl     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cl.reverse()
print cl     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
del cl[3:6]
print cl     # [9, 8, 7, 3, 2, 1, 0]
print cl.counter  # 0
print cl[4] + cl[2]     # 9
print cl.counter        # 2


class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self, size):
        self.width, self.height = size

    def getSize(self):
        return self.width, self.height
r = Rectangle()
r.width = 10
r.height = 5
print r.getSize()         # (10, 5)
r.setSize((150, 100))
print r.getSize()         # (150, 100)
print r.width             # 150


# property(getSize, setSize),第一个参数是get方法，第二个参数是set方法
# property有4个参数：
# fget: 对应get方法，内部用__get__(self)实现，相当于class.property
# fset: 对应set方法，内部用__set__(self, value)实现，相当于class.property = value
# fdel: 对应del方法，内部用__del__(self)实现，相当于del class.property
# doc:  说明性文档
__metaclass__ = type
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self, size):
        self.width, self.height = size

    def getSize(self):
        return self.width, self.height

    size = property(getSize, setSize)
r = Rectangle()
r.width = 10
r.height = 5
print r.size      # 调用getSize方法(property的get方法)
r.size = 150, 100    # 调用setSize方法(property的set方法)
print r.width           # 150


# 静态方法和类方法
__metaclass__ = type
class MyClass:
    @staticmethod
    def smeth():
        print 'This is a static method'

    @classmethod
    def cmeth(cls):
        print 'This is a class method of', cls
MyClass.smeth()     # This is a static method
MyClass.cmeth()     # This is a class method of <class '__main__.MyClass'>
cls = MyClass()
# 可以在类的实例上调用静态方法和类方法
cls.smeth()         # This is a static method
cls.cmeth()         # This is a class method of <class '__main__.MyClass'>


# __getattribute__(self, name):当特性name被访问时自动被调用（只能在新式类中使用）
# __getattr__(self, name)：当特性name被访问且对象没有相应的特性时被自动调用
# __setattr__(self, name, value)：当试图给特性name赋值时会被自动调用.
# __delattr__(self, name)：当试图删除特性name时被自动调用
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, key, value):
        print 'setattr', key
        if key == 'size':
            self.width, self.height = value
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        print 'getattr'
        if item == 'size':
            return self.width, self.height
        else:
            raise AttributeError
# setattr width
# setattr height
rt = Rectangle()
# setattr size
# setattr width
# setattr height
rt.size = 6, 9
# getattr
# (6, 9)
print rt.size
#　9
print rt.height


# 实现__iter__方法的类表示是可迭代的，可用在for语句中
# __iter__方法返回迭代器，迭代器必须实现next方法，如果next方法被调用，迭代器没有返回值，则抛出StopIteration异常
# (在python3.0中迭代器必须实现__next__方法，可以通过next(iterator)来获取下一个值
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self
# 1597
fibs = Fibs()
for f in fibs:
    if f > 1000:
        print f
        break

# 内建函数iter可以从迭代对象(有__iter__方法)中获取迭代器
it = iter([1, 2, 3])
print it.next()  # 1
print it.next()  # 2


# 内建的list函数将可迭代的对象(有__iter__方法)转化为list
class TestIterator:
    value = 0

    def next(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value

    def __iter__(self):
        return self
ti = TestIterator()
print list(ti)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 包含yield语句的函数是生成器(使用yield语句每次产生一个值，函数会被冻结，停在那等待被激活
# 函数被激活后就从停止的那点开始执行)
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element
nested = [[1, 2], [3, 4], [5]]
# <generator object flatten at 0x017F7AA8>
print flatten(nested)
# 1
# 2
# 3
# 4
# 5
for num in flatten(nested):
    print num
print list(flatten(nested))   # [1, 2, 3, 4, 5]


# 生成器推导式(用()而不用[])
g = ((i + 2) ** 2 for i in range(2, 27))
# <generator object <genexpr> at 0x01880B70>
print g
print g.next()  # 16
# 可以将生成器推导式放在函数作为参数，而不用另外加括号
print sum(i ** 2 for i in range(10))    # 285


# 递归生成器
def flatten(nested):
    print nested
    try:
        try:
            '' + nested
        except TypeError:
            pass
        else:
            raise TypeError

        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested
# [1, 2, 3, 4, 5, 6, 7, 8]
print list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8]))
# ['foo', 'bar', 'baz']
print list(flatten(['foo', ['bar', ['baz']]]))


# send(message) 使得(yield value)表达式返回值message,通常用于改变参数的值
# close方法用于结束生成器，如果再close之后，再去生成值，则会抛出RuntimeError
# 可以用append来模拟生成器
def repeat(value):
    while True:
        new = (yield value)
        print new
        if new is not None:
            value = new
r = repeat(42)
r.next()    # 42
print  r.send("Hello")


# 八皇后问题
# state代表之前的皇后的位置，如state[0]=3，表示第一个皇后放在水平位置为4的地方
# nextX表示下一个皇后应该放的水平位置
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


# num表示一共要放多少个皇后
# state表示已经放好的皇后位置
# 处理如果是放最后一个皇后的情况
def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos, ) + result

print list(queens(3))  # []
# [(1, 3, 0, 2), (2, 0, 3, 1)]
print list(queens(4))




