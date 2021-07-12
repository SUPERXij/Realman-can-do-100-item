# a = [1,4,6,9,13,16,19,28,40,100],现输入一个数，要求按原来的规律将它插入数组中
a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100]
b = []
n = int(input("请输入一个整数："))
if n >= 100:
    for i in range(10):
        b.append(a[i])
    b.append(n)
else:
    for i in range(10):
        if a[i] < n < a[i + 1]:
            for j in range(i+1):
                b.append(a[j])
            b.append(n)
            for j in range(i+1, 10):
                b.append(a[j])
print(b)

