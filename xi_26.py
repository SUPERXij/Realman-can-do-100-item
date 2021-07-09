# 利用递归方法求5!
def digui(n):
    # sum = 0
    if n == 0:
        sum = 1
    else:
        sum = n * digui(n - 1)
    return sum


print(digui(5))
