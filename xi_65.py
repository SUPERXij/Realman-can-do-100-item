# 一个最优美的图案
import math
from tkinter import *


class PTS:
    def __init__(self):
        self.x = 0
        self.y = 0


points = []


def line_to_demo():
    screenx = 400
    screeny = 400
    canvas = Canvas(width=screenx, height=screeny, bg='white')

    aspect_ratio = 0.85
    maxpts = 15
    h = screeny
    w = screenx
    xcenter = w / 2
    ycenter = h / 2
    radius = (h - 30) / (aspect_ratio * 2) - 20
    step = 360 / maxpts
    angle = 0.0
    for i in range(maxpts):
        rads = angle * math.pi / 180.0
        p = PTS()
        p.x = xcenter + int(math.cos(rads) * radius)
        p.y = ycenter - int(math.sin(rads) * radius * aspect_ratio)
        angle += step
        points.append(p)
    canvas.create_oval(xcenter - radius, ycenter - radius,
                       xcenter + radius, ycenter + radius)
    for i in range(maxpts):
        for j in range(i, maxpts):
            canvas.create_line(points[i].x, points[i].y, points[j].x, points[j].y)

    canvas.pack()
    mainloop()


line_to_demo()
