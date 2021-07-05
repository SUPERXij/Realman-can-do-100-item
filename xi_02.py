i = int(input("请输入当月利润(万元)： "))
arr = [100, 60, 40, 20, 10, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]

price = 0
for raw in range(0, 6):
    if i > arr[raw]:
        price += (i-arr[raw])*rat[raw]
        i = arr[raw]
print("应发放奖金%d万元" % price)
