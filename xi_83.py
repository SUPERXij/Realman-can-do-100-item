# 求0—7所能组成的奇数个数。
sum = 4
s = 4
for j in range(2, 9):
    # j为组成奇数的位数
    print("组成%d位数是%d个" % (j, s))
    if j <= 2:
        s *= 7
    else:
        s *= 8
    sum += s
print("一共能组成%d个奇数" % sum)

