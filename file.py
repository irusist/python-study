# coding=utf-8
__author__ = 'zhulixin'

f = open('hello.py')
print f.read(2)

f = open('hello.py')
print f.read()

f = open('hello.py')
print f.readline()

f = open('hello.py')
print f.readlines()

f = open('file.dat', 'w')
f.write('hello,world!')

f = open('file.dat', 'w')
f.writelines(['hello\n', 'world\n'])

f = open('file.dat', 'w')
f.seek(2)
f.write('test')
print f.tell()

for line in open('file.dat'):
    # print会产生额外的空行
    print line

# 要用with语句在python以前版本要用import __future from with_statement
# 在file类中有__enter__和__exit__方法
with open('file.dat') as file1:
    print file1.read()





