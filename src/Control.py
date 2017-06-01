#if elif 是 else if 缩写
x = int(input("Please enter an integer: "))
if x<0:
    x=0
    print("<0")
elif x==0:
    print("0")
elif x==1:
    print("1")
elif x>1:
    print(">1")

#for
words=['cat','window','defenestrate']
for w in words:
    print(w,len(w))

#range()函数
for i in range(5):
    print(i)

#注意不包含9
for j in range(5,9):
    print(j)
    
#可以设定步进值
for k in range(0,10,3):
    print(k,end=',')
#空行
print('')
#去掉结尾,的一个方法
print('，'.join(map(str,range(5,10))))

for k in range(-10,-100,-30):
    print(k)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i,a[i])
#序列直接打印的话
print(range(10))

#list() 函数是另外一个（ 迭代器 ），它从可迭代（对象）中创建列表
print(list(range(5)))