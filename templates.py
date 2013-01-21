# coding=utf-8
__author__ = 'zhulixin'
import fileinput,re

# 匹配括号中的字段
field_pat = re.compile(r'\[(.+?)\]')

# 收集的变量
scope = {}


def replacement(match):
    code = match.group(1)
    try:
        # 如果字段可以求值，返回
        return str(eval(code, scope))
    except SyntaxError:
        # 否则执行相同作用域内的赋值语句
        exec code in scope
        # 返回空字符串
        return ''

# 将所有文本以一个字符串获取
lines = []
for line in fileinput.input():
    lines.append(line)
text = ''.join(lines)

# 将field模式的所有匹配项都替换掉
print field_pat.sub(replacement, text)


#执行的时候将赋值放入一个模板文件，取值放到另一个文件,避免产生额外的空行
# templates.txt
# [name1 = 'aa']
# [name2 = 'bbb]
# text.txt
# [name1] [name2]



