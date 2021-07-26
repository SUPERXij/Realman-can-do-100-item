# 输入一个奇数，然后判断最少几个9除于该数的结果为整数。
n = int(input("输入一个奇数:"))
for i in range(1, 10**10):
    if(10**i-1) % n == 0:
        print("最少%d个9" % i)
        print("即%d / %d = %d" % (10**i-1, n, (10**i-1)/n))
        if i > 0:
            break
