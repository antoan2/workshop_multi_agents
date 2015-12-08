from Tkinter import *
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
canvas = Canvas(frame, width=W, height=H, bd=0, highlightthickness=0)
canvas.pack()

items = []
normeSpeed = 100
for i in range(1000):
    items.append(agent(canvas,
                        Vec2d(W*random.random(), 0.5*H*random.random() + 0.2*H),
                        Vec2d(normeSpeed*(2*random.random()-1), normeSpeed*(2*random.random() - 1))))
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
