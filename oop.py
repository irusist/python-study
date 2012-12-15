#coding=utf-8
__author__ = 'zhulixin'
__metaclass = type # 使用新式类


class Person:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greeting(self):
        print "Hello,world! I'm %s." % self.name
foo = Person()
bar = Person()
foo.setName('Luke Skywalker')
bar.setName('Anakin Skywalker')
foo.greeting()    # Hello,world! I'm Luke Skywalker.
bar.greeting()   # Hello,world! I'm Anakin Skywalker.
print foo.name  # Luke Skywalker]
bar.name = 'Yoda'
bar.greeting()  # Hello,world! I'm Yoda.


# 将方法赋值为函数
class Class:
    def method(self):
        print 'I have a self!'


def function():
    print "I don't..."
instance = Class()
instance.method()   # I have a self!
instance.method = function
instance.method()   # I don't...


# 将一个变量绑定到一个实例的方法中,可以调用它
class Bird:
    song = 'Squaawk!'        # 构造方法初始化

    def sing(self):
        print self.song
bird = Bird()
bird.sing()  # Squaawk!
birdsong = bird.sing
birdsong()      # Squaawk!


# 在方法的前面加__,表示私有方法
class Secretive:
    def __inaccessible(self):
        print "Bet you can't see mee..."

    def accessible(self):
        print "The secret message is:"
        self.__inaccessible()
s = Secretive()
# 以下抛出AttributeError，不能访问私有的属性
# s.__inaccessible()

# The secret message is:
# Bet you can't see mee...
s.accessible()

# 可以通过('_' + 类名 + 私有方法名)来访问私有方法
s._Secretive__inaccessible()   # Bet you can't see mee...

# 通过from A import *的语句不能导入A模块中_和__开头的属性(包括属性和方法)


# 在类的定义执行相应代码
class C:
    print 'Class C being defined'
C()  # Class C being defined


# 在类的下面定义的语句只有在第一次实例化时执行，他的变量是类的成员变量，所有实例共享
class MemberCounter:
    print 'aa'
    members = 0

    def init(self):
        MemberCounter.members += 1
m1 = MemberCounter()
m1.init()
# aa
# 1
print MemberCounter.members
m2 = MemberCounter()
m2.init()
print MemberCounter.members   # 2

# 类属性的重新赋值
m1.members = 'two'
print m1.members  # two
print m2.members  # 2


# 继承
class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


# SPAMFilter类继承Filter类
class SPAMFilter(Filter):
    # override父类的init方法
    def init(self):
        self.blocked = ['SPAM']

f = Filter()
f.init()
print f.filter([1, 2, 3])  # [1, 2, 3]
s = SPAMFilter()
s.init()
# SPAMFilter继承了Filer类的filter方法
print s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM'])   # ['eggs', 'bacon']


# 内建的issubclass()函数判断第一个参数是否为第二个参数的子类
print issubclass(SPAMFilter, Filter)  # True
print issubclass(Filter, SPAMFilter)  # Flase


# __bases__属性表示一个一个类的基类
print SPAMFilter.__bases__   # (<class __main__.Filter at 0x00BADC00>,)
print Filter.__bases__      # ()

# 内建的isinstance()函数判断第一个参数是否是第二个参数的实例
# 相当于java的instanceof，会对应到他的所有父类
s = SPAMFilter()
print isinstance(s, SPAMFilter)     # True
print isinstance(s, Filter)         # True
print isinstance(s, str)            # Flase

# __class__属性表示一个对象属于的类
print s.__class__        # __main__.SPAMFilter
# 使用__metaclass__ = type或从object继承的方式类定义的新式类，可以用type(s)来查看实例的类
# print type(s)


# 多个超类
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print 'Hi, my value is', self.value


class TalkingCalculator(Calculator, Talker):
    pass

tc = TalkingCalculator()
tc.calculate('1+2*3')
tc.talk()      # Hi, my value is 7


# 如果一个类的多个超类有相同方法，则继承语句的前面的类的方法会覆盖后面类的方法
# 如果一个类的多个超类共享一个超类，则查找给定方法或特性时访问超类的顺序称为MRO(Method Resolution Order,方法判定顺序),算法很复杂

# 内建的hasattr()函数判断一个实例是否有某个属性(属性和方法)
print hasattr(tc, 'talk')   # True(方法)
print hasattr(tc, 'value')  # True(属性)
print hasattr(tc, 'fnord')  # Flse
# 内建的callable()函数判断一个特性能否被调用
# 在python3.0中，用hasattr(x, '__call__')类代替callable(x)
print callable(getattr(tc, 'talk', None))   # True(方法）
print callable(getattr(tc, 'value', None))  # False(属性)
# <bound method TalkingCalculator.talk of <__main__.TalkingCalculator instance at 0x00BC40F8>>
print getattr(tc, 'talk', None)
print getattr(tc, 'value', None)    # 7
print callable(getattr(tc, 'fnord', None))  # False


# getattr()用来获取对象的特性，setattr()用来设置对象的特性
setattr(tc, 'name', 'Mr.Gumby')
print tc.name   # Mr.Gumby

# __dict__特性得到对象内所有存储的值,只是属性，没有方法
print tc.__dict__    # {'name': 'Mr.Gumby', 'value': 7}

# 从sequence中随机选择一个元素
import random
print random.choice([1, 2, 3])












