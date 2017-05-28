#默认参数值
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)

#这个函数可以通过几种不同的方式调用:
#只给出必要的参数:
ask_ok('Do you really want to quit?')
#给出一个可选的参数:
ask_ok('OK to overwrite the file?', 2)
#或者给出所有的参数:
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
#默认值在函数 定义 作用域被解析，如下所示:
i = 5
def f(arg=i):
    print(arg)
i = 6
f()

#默认值只被赋值一次。这使得当默认值是可变对象时会有所不同
def fe(a, L=[]):
    L.append(a)
    return L
print(fe(1))
print(fe(2))
print(fe(3))

#如果你不想让默认值在后续调用中累积，你可以像下面一样定义函数:
def ff(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
