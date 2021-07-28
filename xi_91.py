# 时间函数举例1
import time

print(time.ctime(time.time()))
print(time.asctime(time.localtime(time.time())))
# 格林尼治标准时间
print(time.asctime(time.gmtime(time.time())))