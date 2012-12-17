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


