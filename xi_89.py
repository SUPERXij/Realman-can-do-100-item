# 某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，
# 加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，
# 再将第一位和第四位交换，第二位和第三位交换。
a = []
b = []
n = 0
for i in range(4):
    a.append(int(input("请输入第%d个整数：" % (i+1))))
for i in range(4):
    n = a[i] + 5
    b.append(n % 10)
b[0], b[1], b[2], b[3] = b[3], b[2], b[1], b[0]
for i in range(4):
    print(a[i], end="")
print()
for i in range(4):
    print(b[i], end="")


