# 一个整数，它加上100是一个完全平方数，再加168也是个完全平方数

PerfectSquare_list = []
i = 0
while i <= 40:
    PerfectSquare = i * i
    PerfectSquare_list.insert(i, PerfectSquare)
    i += 1

for num1 in PerfectSquare_list:
    for num2 in PerfectSquare_list:
        if num1 - 100 == num2 - 168:
            print("这个整数为%d" %(num1-100))


