# _*_ coding: utf-8 _*_
from functools import reduce
def str2float(s):
	global num1
	global n
	n = 0
	num1 = 1
	def char1num(m):
		d = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':'.'}
		return d[m]
	def f(x,y):
		global n
		if y=='.':
			n = 1
			return x
		if n==0:
			return x*10+y
		if n==1:
			global num1
			num=num1
			num1=num1+1
			while num>0:
				y=y/10
				num=num-1
			return x+y
	return reduce(f,map(char1num,s))
print('str2float(\'123.456\')=',str2float('123.456'))
if abs(str2float('123.456')-123.456)<0.00001:
	print('测试成功!')
else:
	print('测试失败！')
print(str2float('0.123456789'))
print(str2float('0.000001223'))
	