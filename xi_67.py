# 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
def inp(numbers):
    for i in range(6):
        numbers.append(int(input('输入一个数字:')))


def arr_max_min(array):
    num_max, num_min = 0, 0
    for i in range(1, len(array)-1):
        m = i
        if array[m] > array[num_max]:
            num_max = m
    k = num_max
    for i in range(1, len(array)-1):
        m = i
        if array[m] < array[num_min]:
            num_min = m
    j = num_min
    array[0], array[k] = array[k], array[0]
    array[5], array[j] = array[j], array[5]


def outp(numbers):
    for i in range(len(numbers)):
        print(numbers[i], end=" ")


if __name__ == '__main__':
    array = []
    inp(array)
    arr_max_min(array)
    print('计算结果:')
    outp(array)
