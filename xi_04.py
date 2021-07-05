# 输入日期，判断是今年哪一天
month, day = map(int, input('输入日期:').split())
months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print("data error")
print("%d月%d日是今年的第%d天" % (month, day, sum + day))
