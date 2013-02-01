__author__ = 'zhulixin'
def square(x):
    """Squares a number and returns the result.
    >>> square(2)
    4
    >>> square(3)
    9
    """
    return x*x

def product(x, y):
    return x * y

if __name__=='__main__':
    import doctest,my_math
    doctest.testmod(my_math)

