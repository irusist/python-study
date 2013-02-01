#coding=utf-8
__author__ = 'zhulixin'

# doctest模块
# unittest模块
# py.test(http://pytest.org/latest/)
# nose(http://code.google.com/p/python-nose)
# unittest的GUI(http://pyunit.sourceforge.net/)
# python源码检查
# tabnanny
# PyCheck(http://pychecker.sourceforge.net/)
# PyLint(http://www.pylint.org/     http://www.logilab.org/)

# 程序分析
# timeit模块用于分析小段程序
# profile模块
# hotshot 模块
import profile
from my_math import product
profile.run('product(1, 2)')

