# 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

k = str(input("请输入一个数字:"))
n = 0
for i in range(len(k) // 2):
    if k[i] != k[len(k)-i-1]:
        n = 1
        break
if n == 0:
    print ("这是一个回文数!")
else:
    print ("这不是一个回文数!")




