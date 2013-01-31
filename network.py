#coding=utf-8
__author__ = 'zhulixin'

# Foundations of Python Network Programming
# 通过socket模块
# urllib和urllib2
import urllib
#webpage = urllib.urlopen("https://github.com")
#print webpage.readline()

#webpage = urllib.urlopen("file:f:\\test.txt")
#webpage = urllib.urlopen("file:f:/test.txt")
#print webpage.readline()

#　urllib.urlretrieve('http://www.google.com', 'f:/google.html')

print urllib.quote('abc def=gh')    # abc%20def%3Dgh
print urllib.quote_plus('abd def=gh')   # abd+def%3Dgh

print urllib.unquote('abd+def%3Dgh')    # abd+def=gh
print urllib.unquote_plus('abd+def%3Dgh')   # abd def=gh
print urllib.urlencode({'query': 'test'})  # query=test

# asynchat  asyncore的增强版本
# asyncore  异步套接字处理程序
# cgi       基本的CGI支持
# Cookie    Cookie对象操作，主要用于服务器
# cookielib 客户端cookie支持
# email     E-mail消息支持（包括MIME）
# ftplib    FTP客户端模块
# gopherlib gopher客户端模块
# httplib   HTTP客户端模块
# imaplib   IMAP4客户端模块
# mailbox   读取几种邮箱的格式
# mailcap   通过mailcap文件访问MIME配置
# mhlib     访问MH邮箱
# nntplib   NNTP客户端模块
# poplib    POP客户端模块
# robotparser  支持解析WEB服务器的robot文件
# SimpleXMLRPCServer    一个简单的XML-RPC服务器
# smtpd     SMTP服务器模块
# smtplib   SMTP客户端模块
# telnetlib TELNET客户端模块
# urlparse  支持解释URL
# xmlrpclib XML-RPC的客户端支持


# SocketServer是BaseHTTPServer,SimpleHTTPServer,CGIHTTPServer,SimpleXMLRPCServer和DocXMLRPCServer基础
# SocketServer包含4个基本的类：针对TCP套接字流的TCPServer，
# 针对UDP数据报套接字的UDPServer，
# 针对性不强的UnixStreamServer和UnixDatagramServer

# 分叉（fork），windows不支持
# 线程（thread），
# 异步IO（asynchronous IO） （select模块）
# http://stackless.com  http://www.eve-online.com
# select模块的select和poll(只能在linux中用)

# Twisted http://twistedmatrix.com



