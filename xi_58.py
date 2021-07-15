# 画图，学用rectangle画方形。
from tkinter import *

root = Tk()
root.title('Canvas')
canvas = Canvas(root, width=400, height=400, bg='white')
x0 = 200
y0 = 200
y1 = 200
x1 = 200
for i in range(15):
    canvas.create_rectangle(x0, y0, x1, y1)
    x0 -= 10
    y0 -= 10
    x1 += 10
    y1 += 10

canvas.pack()
root.mainloop()
