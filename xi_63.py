# 画椭圆。
from tkinter import*

x = 300
y = 300
top = y - 20
bottom = y - 20

canvas = Canvas(width=400, height=600, bg='white')
for i in range(20):
    canvas.create_oval(300 - top, 300 - bottom, 300 + top, 300 + bottom)
    top -= 5
    bottom += 5
canvas.pack()
mainloop()
