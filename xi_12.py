# 101到200多少个质数
n, m = 0, 1
for i in range(101, 201):
    for j in range(2, i):
        if i % j == 0:
            m = 0
            break
    if m == 1:
        print(i)
        n += 1
    m = 1
print(n)

