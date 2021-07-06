def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


i = int(input("请输入月份："))
n = i // 3
print(fib(n))
