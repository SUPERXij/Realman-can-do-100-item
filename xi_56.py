# 画图，学用circle画圆形。
from tkinter import *

canvas = Canvas(width=400, height=400, bg='white')
canvas.pack(expand=YES, fill=BOTH)
k = 1
j = 1
for i in range(0, 10):
    canvas.create_oval(200 - k, 200 - k, 200 + k, 200 + k, width=1)
    k += j
    j += 5

mainloop()
