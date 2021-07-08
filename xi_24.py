# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和
a, b = 1, 2
k = []
for i in range(20):
    k.append(b / a)
    b, a = a + b, b
print(sum(k))
