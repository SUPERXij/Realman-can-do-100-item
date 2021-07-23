# 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
def fx():
    n = int(input("请输入一个整数："))
    s = 0
    if n % 2 == 0:
        for i in range(2, n+1, 2):
            s += 1 / i
    else:
        for i in range(1, n+1, 2):
            s += 1 / i
    print(s)


fx()
