for n in range(2, 1001):
    k = []
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
            k.append(i)
    if s == n:
        print("%d是一个完数" % n)
        print("%d =" % n, end=" ")
        c = len(k)
        for i in k:
            if i == k[c-1]:
                print("%d" % i)
            else:
                print("%d +" % i, end=" ")
        print()
