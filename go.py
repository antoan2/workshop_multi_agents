from Tkinter import *
from math import *
import random
import time
from geometry import Vec2d
from agent import agent

root = Tk()
root.title("Blobs")
root.resizable(0, 0)

frame = Frame(root, bd=5, relief=SUNKEN)
frame.pack()

W, H = 1000, 600
canvas = Canvas(frame, width=W, height=H, bd=0, highlightthickness=0, background='black')
canvas.create_oval((W/2.-4, H/2.-4, W/2.+4, H/2.+4), fill='goldenrod')
canvas.create_oval((W/2.-2, H/2.-2, W/2.+2, H/2.+2), fill='orange red')
for i in range(300):
    x = random.random()*W
    y = random.random()*H
    canvas.create_oval((x-1, y-1, x+1, y+1), fill='white')
canvas.pack()

items = []
normeSpeed = 60
distToCenter = 250
for i in range(2000):
    posRandom = 2*3.14*random.random()
    items.append(agent(canvas,
                        Vec2d(W/2. + distToCenter*cos(posRandom) + 10*(2*random.random()-1),
                              H/2. + distToCenter*sin(posRandom) + 10*(2*random.random()-1)),
                        Vec2d(normeSpeed*sin(posRandom) + 10*(2*random.random()-1),
                                -normeSpeed*cos(posRandom) + 10*(2*random.random()-1))))
                        #Vec2d(normeSpeed*(2*random.random()-1), normeSpeed*(2*random.random() - 1))))
    #items.append(agent(canvas,
                        #Vec2d(520, 300),
                        #Vec2d(0, 0)))

root.update() # fix geometry

# loop over items

try:
    while 1:
        t1 = time.time()
        for agent in items:
            agent.move()
        root.update_idletasks() # redraw
        root.update() # process events
        t2 = time.time()
        #print t2 - t1
        time.sleep(max(0.02 - (t2 - t1), 0))
except TclError:
    pass # to avoid errors when the window is closed
