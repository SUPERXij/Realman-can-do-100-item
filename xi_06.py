def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


n = int(input("请输入n："))
print(fib(n))
