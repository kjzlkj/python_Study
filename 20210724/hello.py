# list
from typing import Dict


l = ['a','b',1,2]

# 取单个值
# print(l[0])   # 按照索引取值  'a'
# print(l[-1])  # 

# 取多个值
# print(l[-2:])
# print(l[2:4])

l.append('c')
print(l)

# Dict
tinydict = {'name': 'runoob',
            'code':[1,2],  # 键值对  key - value
            'site': 'www.runoob.com'
            }

print (tinydict.keys())
print (tinydict.values())

a = """
这是多行注释，用三个双引号
这是多行注释，用三个双引号 
这是多行注释，用三个双引号
"""
print(type(a))