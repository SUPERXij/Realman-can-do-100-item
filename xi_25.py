# 求1+2!+3!+...+20!的和。
def sum_factorial(n):
    k = []
    for i in range(1, n + 1):
        m = 1
        for j in range(1, i + 1):
            m = m * j
        k.append(m)
    print(sum(k))


sum_factorial(20)



