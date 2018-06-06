#!/usr/bin/env python
# _*_ coding:utf-8 _*
import re
s=re.split(r'\s+','ab  b s  s')
print(s)

print(re.split(r'[\s\,\;\_]+','a b , c;;d_e_,f'))

# test=input('请输入:')
# if re.match(r'^\d{3}\-\d{3,8}',test):
#     print('your input %s is ok!'%test)
# else:
#     print('error!')

#正则表达式提取子串 用（）标识要提取的的分组（Group）
m=re.match(r'(\d{3})-(\d{3,8})$','010-123456')
print(m.group(0))
print(m.group(1))
print(m.group(2))


re_telephone=re.compile(r'^(\d{3})-(\d{3,8})$')
test2='999-12345'
print(re_telephone.match(test2))
print(re_telephone.match(test2).groups())
print(re_telephone.match(test2).group())