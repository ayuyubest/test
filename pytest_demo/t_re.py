import re
# result = re.match(正则表达式，带匹配的字符串)
# . 匹配任意一个字符 除了\n
# [] 匹配里面的字符
# \d 匹配数字
# \D 匹配非数字
# re.match(".","&and")
re.match("[1234][a-z][A-Z]","1aZ9")