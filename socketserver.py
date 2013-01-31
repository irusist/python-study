__author__ = 'zhulixin'
from SocketServer import TCPServer, StreamRequestHandler


class Handler(StreamRequestHandler):
    def handle(self):
        # self.request返回的是客户端socket
        addr = self.request.getpeername()
        print 'Got connection from', addr
        #　self.wfile用于写入数据
        self.wfile.write('Thank you for connecting')

server = TCPServer(('', 1234), Handler)
server.serve_forever()

