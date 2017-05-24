squares=[1,4,9,16,25]
print(squares)
#列表可以被索引和切片
print(squares[0])
print(squares[-3:])
#拼接操作
print(squares + [36, 49, 64, 81, 100])
#列表允许修改元素
squares[3]=10
print(squares)
#append()方法
squares.append(100)
squares.append(3**3)
print(squares)
#可以对切片赋值，此操作可以改变列表的尺寸，或清空它
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
#赋值
letters[2:5] = ['C', 'D', 'E']
print(letters)
#改变尺寸
letters[2:5] = []
['a', 'b', 'f', 'g']
print(letters)
#清空
letters[:] = []
print(letters)
#内置函数 len() 同样适用于列表
print(len(letters))
#列表可以嵌套
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

#生成斐波那契数列
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b#注:a=b b=a+b
#用一个逗号结尾就可以禁止输出换行
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b