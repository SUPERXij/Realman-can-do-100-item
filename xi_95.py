# 字符串日期转换为易读的日期格式。
from dateutil import parser
dt = parser.parse("Aug 28 2021 11:00AM")
print(dt)
