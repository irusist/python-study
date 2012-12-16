#coding=utf-8
__author__ = 'zhulixin'
# raise Exception
# raise Exception('hyperdrive overload')
import exceptions
# dir列出某个模块的内容,列出的内容都可以用raise
print dir(exceptions)
# raise WindowsError

# Exception             所有异常的基类
# AttributeError        特性引用或赋值失败时引发
# IOException           试图打开不存在文件（包括其他情况）时引发
# IndexException        在使用序列不存在的索引时引发
# KeyException          在使用映射中不存在的键时引发
# NameError             在找不到名字（变量）时引发
# SyntaxError           在代码为错误形式时引发
# TypeError             在内建操作或函数应用于错误类型的对象时引发
# ValueError            在内建操作或函数应用于正确类型的对象，但是该对象使用不合适的值时引发
# ZeroDivisionError     在除法或模除操作的第二个参数为0时引发



# 创建自己的异常类要继承自Exception或者他的子类
class SomeCustomException(Exception):
    pass


# 捕获异常try/except
try:
    x = 10
    y = 0
    print x / y
except ZeroDivisionError:
    print "The second number can't be zero!"


# 抛出异常后返回的是None
class MuffledCalculator:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print 'Division  by zero is illegal'
            else:
                raise
calculator = MuffledCalculator()
# print calculator.calc('10/0')

calculator.muffled = True
# Division  by zero is illegal
# None
print calculator.calc('10/0')


# That wasn't a number, was it?
try:
    x = 2
    y = 'a'
    print x / y
except ZeroDivisionError:
    print "The second number can't be zero!"
except TypeError:
    print "That wasn't a number, was it?"


#　用元组来捕获多个异常
# Your numbers were bogus...
try:
    x = 2
    y = 'b'
    print x / y
except (ZeroDivisionError, TypeError, NameError):
    print 'Your numbers were bogus...'


# 获得异常对象
# integer division or modulo by zero
try:
    x = 1
    y = 0
    print x / y
# 在python3.0用except(ZeroDivisionError, TypeError) as e:
except (ZeroDivisionError, TypeError), e:
    print e


# 捕获所有的异常
# Something wrong happened...
try:
    x = 1
    y = 0
    print x / y
except:
    print 'Something wrong happened...'


# 在try/except后加else
# A simple task
# Ah... It went as planned.
try:
    print 'A simple task'
except:
    print 'What? Something went wrong?'
else:
    print 'Ah... It went as planned.'


#while True:
#    try:
#        x = input('Enter the  first number: ')
#        y = input('Enter the second number: ')
#        value = x / y
#        print 'x / y is ', value
#    except Exception, e:
#        print 'Invalid input: ', e
#        print 'Please try again'
#    else:
#        break


# 用了finally还是会抛出异常
#x = None
#try:
#    x = 1 / 0
#finally:
#    print 'Cleaning up...'
#    del x

# 以下直接抛出异常，不会打印出a,
# print 'a' + var

# 会打印出a，然后再抛出异常
# print 'a', var


# 过滤警告
import warnings
warnings.filterwarnings('error')


try:
    print 'before'
    1 / 0
except:
    print 'exception'
finally:
    print 'finally'




