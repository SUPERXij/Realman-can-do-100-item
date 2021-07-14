# 求输入数字的平方，如果平方运算后小于 50 则退出。
def sq(x):
    return x * x


i = True
while i:
    a = int(input("请输入数字："))
    print(("运算结果为: %d" % (sq(a))))
    if sq(a) >= 50:
        i = True
    else:
        i = False


