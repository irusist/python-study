#coding=utf-8
__author__ = 'zhulixin'
import string
print string.digits
print string.letters
print string.lowercase
print string.printable
print string.punctuation
print string.uppercase
print string.ascii_letters
print 'With a moo-moo here, and a moo-moo there'.find('moo')
title = "Monty Python's Flying Circus"
print title.find('Python')
print title.find('Monty')
print title.find('Flying')
print title.find('Zircus')
subject = "$$$ Get rich now!!! $$$"
print subject.find("$$$", 1)
print subject.find("!!!")
# 包括0，但是不包括19
print subject.find("!!!", 0, 19)
# string.rfind, string.index, string.rindex, string.count, string.startwith, string.endwith
#seq = [1, 2, 3, 4]
#print '+'.join(seq)
# join的参数只能是string的序列
seq = ['1', '2', '3', '4', '5']
print '+'.join(seq)
dirs = '', 'usr', 'bin', 'env'
print '/'.join(dirs)
print 'c:' + '\\'.join(dirs)
# islower, capitalize, swapcase, title, istitle, upper, isupper
print 'Trondleim Hammer Dance'.lower()
# 每个单词首字母大写
print "That's all folks".title()
print string.capwords("that's all folks")
# translate, expandtabs
print 'This is a test'.replace('is', 'eez')
# 如果不提供sep,则将分隔符（空格，制表，换行）作为分隔符
# rsplit, splitlines
print '1+2+3+4+5'.split('+')
print '/usr/bin/env'.split('/')
print 'Using the default'.split()
# lstrip rstrip
print '      internal whitespace is kept      '.strip()
print '*** SPAM * for * everyone!!! ***'.strip(' *!')

table = string.maketrans('cs', 'kz')
print len(table) # 256
# a到z将c替换成了k，s替换成了z
print table[97:123] # abkdefghijklmnopqrztuvwxyz
# 未替换
print string.maketrans('', '')[97:123] # abcdefghijklmnopqrstuvwxyz
# 第二个参数表示要删除的字符
print 'this is an incredible test'.translate(table, ' ')
# 将第一个参数先用第二个参数（默认为空格）进行分割，再进行capitalize（首字母大写），然后用第二个参数连接。
print string.capwords('aa+bb+cc+dd', '+')
print string.capwords('aa bb cc dd')