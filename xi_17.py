import string
s = input("请输入一个字符串:\n")
letters, space, digit, others = 0, 0, 0, 0
for i in s:
    if i.isalpha():
        letters += 1
    elif i.isspace():
        space += 1
    elif i.isdigit():
        digit += 1
    else:
        others += 1
print('char = %d,space = %d,digit = %d,others = %d' % (letters, space, digit, others))