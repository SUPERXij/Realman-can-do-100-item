def prime_factorization():
    n = int(input("请输入自然数："))
    print('{} ='.format(n), end=" ")
    while n != 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n //= i
                if n == 1:
                    print(i)
                else:
                    print('{} *'.format(i), end=" ")
                break


prime_factorization()
