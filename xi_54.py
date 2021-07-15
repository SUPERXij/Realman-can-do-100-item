# 取一个整数a从右端开始的4〜7位。
def fx():
    a = int(input("请输入一个整数："))
    b = a >> 4
    c = ~(~0 << 4)
    d = b & c
    print('%o' % d)


fx()
