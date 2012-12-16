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



class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

s = ArithmeticSequence(1, 2)
len(s)

