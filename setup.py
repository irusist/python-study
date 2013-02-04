__author__ = 'zhulixin'


#from distutils.core import setup
#setup(name='Hello',
#    version='1.0',
#    description='A simple example',
#    author='Magus Lie Hetland',
#    py_modules=['package-test'])


from distutils.core import setup
import py2exe
setup(console=['package-test.py'])

