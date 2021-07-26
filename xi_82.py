# 八进制转换为十进制
n = 0
p = input('输入八进制数:')
for i in range(len(p)):
    n = n * 8 + ord(p[i]) - ord('0')
print(n)
