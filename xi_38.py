# 求一个3*3矩阵主对角线元素之和。
a = []
sum = 0.0
for i in range(3):
    a.append([])
    for j in range(3):
        a[i].append(int(input("矩阵 %d * %d 输入数字:" % (i+1, j+1))))
for i in range(3):
    sum += a[i][i]
for i in range(3):
    print(a[i])
print("矩阵主对角线元素之和为%d" % sum)