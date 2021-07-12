# 对10个数进行排序。
print('下面请输入10个数字:')
s = []
for i in range(1, 11):
    s.append(int(input('输入第%d个数字:' % i)))
print()

for i in range(9):
    for j in range(i + 1, 10):
        if s[i] < s[j]:
            s[i], s[j] = s[j], s[i]
for i in range(10):
    print(s[i], end=" ")
