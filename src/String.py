#\转义字符
from ctypes.wintypes import WORD
print("输出\"'")
#使用原始字符串，第一个引号前加r
print(r'C:\files\txt')
#文本分成多行用"""三引号
#行尾换行符会被自动包含到字符串中，但是可以在行尾加上 \ 来避免这个行为
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
#字符串可以由 + 操作符连接(粘到一起)，可以由 * 表示重复
print(3*"a"+"bbb")
#相邻的两个字符串文本自动连接在一起但不能用于字符串表达式
print("Py""thon")
#字符串也可以被截取(检索)。，字符串的第一个字符索引为 0
word = "Python"
print(word[0]+word[5])
#索引也可以是负数，这将导致从右边开始计算
print(word[-1]+word[-2]+word[-6])
#字符串可以切片
print(word[0:2])
print(word[2:5])
print(word[:4])
print(word[4:])
print(word[-2:])
print("""切片时的索引是在两个字符 之间 。
左边第一个字符的索引为 0，
而长度为 n 的字符串其最后一个字符的右界索引为 n""")
#Python字符串不可以被更改 — 它们是 不可变的 。因此，赋值给字符串索引的位置会导致错误
#如果你需要一个不同的字符串，你应该创建一个新的
#内置函数 len() 返回字符串长度
print("the length of word is "+str(len(word)))#str转字符串