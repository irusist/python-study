print 'Hello, world!'


def fun0(func):
    def func2():
        print 'start func...'
        func()
        print 'end func...'
    return func2

@fun0
def func1():
    print 'function func1'

func1()
