# coding=utf-8
__author__ = 'zhulixin'

# 屏幕抓取工具
# Tidy
# http://utidylib.berlios.de/
# http://www.egenix.com/products/python/mxExperimental/mxTidy/
# http://pkgs.org/download/python-tidy

# subprocess模块

# HTMLParser

from urllib import urlopen
from HTMLParser import HTMLParser
class Scraper(HTMLParser):
    in_h3 = False
    in_link = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h3':
            self.in_h3 = True

        if tag == 'a' and 'href' in attrs:
            self.in_link = True
            self.chunks = []
            self.url = attrs['href']

    def handle_data(self, data):
        if self.in_link:
            self.chunks.append(data)

    def handle_endtag(self, tag):
        if tag == 'h3':
            self.in_h3 = False

        if tag == 'a':
            if self.in_h3 and self.in_link:
                print '%s (%s)' % (''.join(self.chunks), self.url)
            self.in_link = False
text = urlopen("http://python.org/community/jobs").read()
parser = Scraper()
parser.feed(text)
parser.close()


# Beautiful Soup          http://www.crummy.com/software/BeautifulSoup/

# Ka-Ping Yee的scrape.py     http://zesty.ca/python

# http://wiki.python.org/moin/WebProgramming

# cgi  http://docs.python.org/2/library/cgi.html
# cgitb

# 将脚本放在cgi-bin的子目录中
# 脚本文件扩展名改为.cgi
# 在脚本头部加上#!/usr/bin/env python
# 在linux中，脚本文件放在public_html目录中
# #!usr/bin/env python
print 'Content-type: text/html'
print

print 'Hello World!'

# 用cgitb调试
#!usr/bin/env python
import cgitb;cgitb.enable()
print 'Content-type: text/html'
print

print 1/0
print 'Hello, world!'

# cgi获取输入

#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
name = form.getvalue('name', 'world')
print 'Content-type: text/plain'
print

print 'Hello, %s!' % name

# http://www.webreference.com/htmlform
# http://www.htmlhelp.com/faq/html/forms.html
# http://www.cs.tut.fi/~jkorpela/forms
# http://www.w3schools.com/html/html_forms.asp
# http://www.htmlgoodies.com/tutors/fm.html

#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
name = form.getvalue('name', 'world')

print """Content-type: text/html

<html>
    <head><title>Greeting Page</title></head>
    <body>
        <h1>Hello, %s!</h1>
        <form action='simple3.cgi'>Change name<input type='text' name='name' />
            <input type='submit' />
        </form>
    </body>
</html>""" % name


# mod_python模块      http://modpython.org
# CGI处理程序
# PSP处理程序（Python Server Page）
# http://webwareforpython.org
# http://zope.org
# http://clearsilver.net
# 发布处理程序（用URL调用python函数）
# http://example.com/script.py/func会调用script.py的func函数
# http://example.com/script.py会调用script.py的index函数
def index(req):
    return 'Hello, World!'

# http://example.com/script.py/greet?name=Gumby会显示Hello, Gumby!
def index(name='world'):
    return 'Hello, %s!' % name

# mod_python的__auth__,__access__

# Albatross     http://object-craft.com.au/projects/albatross
# CherryPy      http://cherrypy.org
# Django        http://djangoproject.com
# Plone         http://plone.org
# Pylons        http://pylonshq.com
# Quixote       http://quixote.ca
# Spyce         http://spyce.sf.net         spyce.sourceforge.net/
# TurboGears    http://turbogears.org
# web.py        http://webpy.org
# Webware       http://webwareforpython.org
# Zope          http://zope.org

# http://www.w3.org/RDF/
# RSS Atom http://tools.ietf.org/html/rfc428T
# http://code.google.com/p/feedparser/
# 远程调用：http://pypi.python.org/pypi/Pyro4    http://twistedmatrix.com/trac/
# json      http://deron.meranda.us/python/comparing_json_modules/
# SOAP(以前Simple Object Access Protocol)
# SOAP模块：Twisted  ZSI(http://pywebsvcs.sourceforge.net/)  SOAPy（http://soapy.sourceforge.net/）














