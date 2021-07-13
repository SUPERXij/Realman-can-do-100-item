class Static:

    StaticVar = 5

    def varfunc(self):
        self.StaticVar += 1
        print(self.StaticVar)


def varfunc():
    var = 0
    print('var = %d' % var)
    var += 1


for i in range(3):
    varfunc()
print(Static.StaticVar)
a = Static()
for i in range(3):
    a.varfunc()
