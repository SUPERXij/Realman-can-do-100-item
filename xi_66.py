# 输入3个数a,b,c，按大小顺序输出。
a = int(input("请输入数字a："))
b = int(input("请输入数字b："))
c = int(input("请输入数字c："))


def swap(n, m):
    return m, n


if a > b:
    a, b = swap(a, b)
if a > c:
    a, c = swap(a, c)
if b > c:
    b, c = swap(b, c)

print(a, b, c)
