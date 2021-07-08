# a说他不和x比，c说他不和x,z比
for i in range(ord('x'), ord('z') + 1):
    for j in range(ord('x'), ord('z') + 1):
        if i != j:
            for k in range(ord('x'), ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print('比赛顺序为： a VS %s\t b VS %s\t c VS %s' % (chr(i), chr(j), chr(k)))

