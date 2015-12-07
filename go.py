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

W, H = 1000, 400
canvas = Canvas(frame, width=W, height=H, bd=0, highlightthickness=0)
canvas.pack()

items = []
for i in range(1000):
    items.append(agent(canvas,
                        Vec2d(random.random()*W, random.random()*H),
                        Vec2d(random.random()-0.5, random.random()-0.5)))

root.update() # fix geometry

# loop over items

try:
    while 1:
        t1 = time.time()
        for i in range(len(items)):
            items[i].move()
        root.update_idletasks() # redraw
        root.update() # process events
        t2 = time.time()
        #print t2 - t1
        time.sleep(max(0.02 - (t2 - t1), 0))
except TclError:
    pass # to avoid errors when the window is closed
