a, n = map(int, input('输入a,n:').split())
b, s = 0, 0
for i in range(1, n+1):
    b = a * 10 ** (i - 1) + b
    s += b
print("%d =" % s, end=" ")
b, s = 0, 0
for i in range(1, n+1):
    b = a * 10 ** (i - 1) + b
    s += b
    if i == n:
        print('%d' % b)
    else:
        print('{} +'.format(b), end=" ")
