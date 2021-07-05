count = 0
for a in [1, 2, 3, 4]:
    for b in [1, 2, 3, 4]:
        for c in [1, 2, 3, 4]:
            if a != b and b != c and c != a:
                count += 1
                print(a, b, c, sep="")
print("能组成 %d 个互不相同且无重复数字的三位数" % count)


