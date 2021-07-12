# 输出指定范围内的素数
lower = int(input("“输入区间的最小值："))
higher = int(input("“输入区间的最大值："))
for i in range(lower, higher + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
