def fib(n):
    """Print a Fibonacci series up to n."""
    a,b=0,1
    while a < n:
        print(a,end=' ')
        a,b=b,a+b
        
#调用
fib(2000)
#重命名
f=fib
print()
f(100)
#没有 return 语句的函数确实会返回一个值，
#虽然是一个相当令人厌烦的值（指 None ）。这个值被称为 None （这是一个内建名称）。
#如果 None 值是唯一被书写的值，那么在写的时候通常会被解释器忽略（即不输出任何内容）。
#如果你确实想看到这个值的输出内容，请使用 print() 函数
print()#换行
print(fib(0))
#定义一个返回斐波那契数列的列表
def fiblist(n):
    result = []
    a,b=0,1
    while a < n:
        result.append(a)
        a,b=b,a+b
    return result
#调用一下
flist=fiblist(100)
print(flist)
