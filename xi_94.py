# 时间函数举例4,一个猜数游戏，判断一个人反应快慢。
import time
import random

play_it = input('你想参加猜数游戏吗?(\'y\' or \'n\')')
while play_it == 'y':
    small = 0
    big = 100
    c = input('请输入姓名:\n')
    i = random.randint(small, big)
    print("下面开始游戏！数字在0到100之间")
    start = time.time()
    guess = int(input('输入您猜的数:\n'))
    while guess != i:
        if guess > i:
            big = guess
            print('这个数更小一点，在 %d 和 %d 之间' % (small, big))
            guess = int(input('输入您猜的数:\n'))
        else:
            small = guess
            print('这个数更大一点，在 %d 和 %d 之间' % (small, big))
            guess = int(input('输入您猜的数:\n'))
    end = time.time()
    var = end-start
    print('总耗时 %6.3f' % var)
    if var < 15:
        print('无敌!')
    elif var < 25:
        print('一般般!')
    else:
        print('有点憨!')
    print('Congradulations')
    print('您猜的数字就是 %d' % i)
    break

