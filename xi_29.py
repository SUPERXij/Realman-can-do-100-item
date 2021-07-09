# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
def output(s, l):
    if l == 0:
        return
    print(s[l - 1], end=" ")
    output(s, l - 1)
    # print(l)


s = input('请输入一个不多于5位的正整数:')
l = len(s)
while l > 5:
    s = input("请输入有效数字:")
    l = len(s)
else:
    print("%d 位数：" % l, end="")
    output(s, l)



