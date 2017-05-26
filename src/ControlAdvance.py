#break 语句和 C 中的类似，用于跳出最近的一级 for 或 while 循环
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
#Continue

for num in range(2,10):
    if num %2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

#pass 语句什么也不做。它用于那些语法上必须要有什么语句，但程序什么也不做的场合
while True:
    pass
#通常用于创建最小结构的类
#pass 可以在创建新代码时用来做函数或控制体的占位符。可以让你在更抽象的级别上思考。pass 可以默默的被忽视:
def initlog(*args):
    pass