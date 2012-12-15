#coding=utf-8
__author__ = 'zhulixin'
import string
print string.lowercase
print string.uppercase
map = {'a' : 1, 'b' : 2, 'c' : 3}
print map.fromkeys(("d", "e"))
print map.items()
print map.values()
print map.pop('b')
print map



__author__ = 'Administrator'
# 可能以0开头的值用字符串类型，不用int类型
print 0142

# 字典的创建
phonebook = {'Alice' : '2341', 'Beth' : '9102', 'Cecil' : '3258'}
items = [('name', 'Gumby'), ('age', 42)]

# dict是一个类，与list， tuple，str一样，不是一个函数
# 将list转化成字典
d = dict(items)
print d
print d['name']

# 通过关键字来创建字典
d = dict(name='Gumby', age=42)
print d
print len(d)

#x = []
#x[42] = 'Foobar'
x = {}
x[42] = 'Foobar'
print x

# 字符串格式化第二个参数用字典，则第一个参数用%(key)s来表示
print "Cecil's phone number is %(Cecil)s." % phonebook
# 可用string.Template类实现下面的
template = '''<html><head><title>%(title)s</title></head/>
<body><h1>%(title)s</h1><p>%(text)s</p></body>'''
data = {'title' : 'My Home Page', 'text' : 'Welcome to my home page!'}
print template % data

# 字典clear方法,返回None，删除字典中的所有元素,原有的字典成了{}
d = {}
d['name'] = 'Gumby'
d['age'] = 42
print d
return_value = d.clear()
print return_value
print d

# 字典的copy方法,实现的是浅拷贝
x = {'username' : 'admin', 'machines' : ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print y # {'username': 'mlh', 'machines': ['foo', 'baz']}
print x # {'username': 'admin', 'machines': ['foo', 'baz']}
from copy import deepcopy
d = {}
d['name'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['name'].append('Clive')
print c # {'name': ['Alfred', 'Bertrand', 'Clive']}
print dc # {'name': ['Alfred', 'Bertrand']}

# fromkeys方法使用指定的键建立新的字典，每个键的值为None
print {}.fromkeys(['name', 'age'])
print dict.fromkeys(['name', 'age'])
print dict.fromkeys(['name', 'age'], '(unknown)')

# get方法访问字典的项，如果用[]访问，不存在则error，用get访问不存在则不会error,返回None
d = {}
# print d['name']
print d.get('name')
print d.get('name', 'N/A')

# has_key查询字典是否含有某个key， 相当于 k in d
d = {}
print d.has_key('name')
d['name'] = 'Eric'
print d.has_key('name')
print 'name' in d

# items方法返回字典的所有项，以列表形式返回，iteritems返回字典的一个迭代对象
d = {'title' : 'Python Web Site', 'url' : 'http://www.python.org', 'spam' : 0}
print d.items() # [('url', 'http://www.python.org'), ('spam', 0), ('title', 'Python Web Site')]
it = d.iteritems()
print it    # <dictionary-itemiterator object at 0x00BC0C30>
print list(it)

# keys返回键的列表， iterkeys返回键的迭代

# pop方法获得对应键的值，并将这个键值删除
d = {'x' : 1, 'y' : 2}
print d.pop('x')
print d

# popitem方法会随机弹出字典中的项,返回键，值组成的元组
# 字典没有append方法
d = {'url' : 'http://www.python.org', 'spam' : 0, 'title' : 'Python Web Site'}
print d.popitem()
print d

# setdefault,如果字典含有某个key，则返回这个key的值，如果没有某个key，则设置这个key的值，并返回这个值
# 他的第二个参数默认为None
d = {}
print d.setdefault('name', 'N/A')
print d

# update, 如果不含有参数字典的键，则将参数加入到字典，如果含有，则更新字典
d = {'title' : 'Python Web Site', 'url' : 'http://www.python.org',
     'changed' : 'Mar 14 22:09;15 Met 2009'}
x = {'title2' : 'Python Language Site'}
d.update(x)
d.update(url2='http://www.google.com')
print d

# values和itervalues,返回字典的值的列表和迭代对象
d = {}
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 1
print d.values()

