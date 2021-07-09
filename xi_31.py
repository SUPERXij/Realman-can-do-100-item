# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母
letter = str(input("请输入第一个字母："))
if letter == 'S':
    letter = str(input("请输入第二个字母："))
    if letter == 'a':
        print('Saturday')
    elif letter == 'u':
        print('Sunday')
    else:
        print('data error')

elif letter == 'F':
    print('Friday')

elif letter == 'M':
    print('Monday')

elif letter == 'T':
    letter = input("请输入第二个字母：")

    if letter == 'u':
        print('Tuesday')
    elif letter == 'h':
        print('Thursday')
    else:
        print('data error')

elif letter == 'W':
    print('Wednesday')
else:
    print('data error')