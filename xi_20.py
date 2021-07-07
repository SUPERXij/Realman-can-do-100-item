# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
height = float(input("起始高度:")) # 起始高度
times = int(input("落地次数："))  # 次数

times_height = []
s = []
for i in range(1, times + 1):
    if i == 1:
        s.append(height)
    else:
        s.append(2 * height)
    height /= 2
    times_height.append(height)

print("它在第 %d 次落地时，共经过%f米" % (times, sum(s)))
print("第 %d 次反弹 %f m高" % (times, times_height[times-1]))