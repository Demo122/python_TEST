import math
def quadratic(a,b,c):
	ques='%sx^2+%sx+%s'%(a,b,c)
	ques=ques.replace('+-','-')
	ques=ques.replace('1x','x')
	print('求解：%s'%ques)
	if isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)):
		tag=b*b-4*a*c
		if tag>0:
			print('该一元二次方程有两个不同的解，分别为：')
			x1=(-b+math.sqrt(tag))/(2*a)
			x2=(-b-math.sqrt(tag))/(2*a)
			print('x1=%f'%x1)
			print('x2=%f'%x2)
			return (x1,x2)
		elif tag==0:
			print('该一元二次方程有一个解为：')
			x1=-b/(2*a)
			print('x1=%f'%x1)
			return x1
		else:
			print('该一元二次方程有两个复数解为: ')
			t1=-b/(2*a)
			t2=math.sqrt(-tag)/(2*a)
			x1=str(t1)+'+'+str(t2)+'i'
			x2=str(t1)+'-'+str(t2)+'i'
			print('x1=%s'%x1)
			print('x2=%s'%x2)
			return (x1,x2)
	else:
		raise TypeError('请输入正确类型的方程系数')

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
	print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
	print('测试失败')
else:
	print('测试成功')