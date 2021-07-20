# 有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数
n = int(input("整数n为："))
m = int(input("后移m个位置："))
numbers = []

# 输入
for i in range(n):
    numbers.append(int(input('输入一个数字:')))


def move(array, n, m):
    array_end = array[n - 1]
    for i in range(n - 1, -1, - 1):
        array[i] = array[i - 1]
    array[0] = array_end
    m -= 1
    if m > 0:
        move(array, n, m)


# 输出
for i in range(n):
    print(numbers[i], end=" ")
print()
move(numbers, n, m)
for i in range(n):
    print(numbers[i], end=" ")

