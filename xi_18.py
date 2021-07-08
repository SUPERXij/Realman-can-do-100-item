a, n = map(int, input('输入a,n:').split())
b, s = 0, 0
k = []
for i in range(1, n+1):
    b = a * 10 ** (i - 1) + b
    s += b
    k.append(b)

print("%d =" % s, end=" ")

for i in range(1, n+1):
    if i == n:
        print('%d' % k[i-1])
    else:
        print('%d +' % k[i-1], end=" ")
