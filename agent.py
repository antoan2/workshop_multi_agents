import Tkinter as Tk
import random
from geometry import Vec2d

class agent(object):
     
    def __init__(self, canvas, pos=Vec2d(10, 10), speed=Vec2d(1, 1)):

        self.a = Vec2d(0, 100)
        self.speed = speed
        self.pos = pos
        self.dt = 0.02
        self.size = 4

        self.canvas = canvas
        self.id = self.canvas.create_oval(self.getBox(self.size),
                                fill='brown')

        self.W = self.canvas.winfo_reqwidth()
        self.H = self.canvas.winfo_reqheight()
        self.center = Vec2d(self.W / 2., self.H / 2.)

    def move(self):

        self.pos.add(self.speed.multiply(self.dt))
        self.speed.add(self.a.multiply(self.dt))
        r = self.pos - self.center
        toCenter = Vec2d(r.x, r.y)
        toCenter.normalize()
        if self.id == 1:
            print -1e6 / (1e-1 + r.norm()**2)
        self.a = toCenter.multiply(max(-400, -1e6 / (1e-1 + r.norm()**2)))

        #self.pos.modulo((self.W, 10000))
        self.draw()
    
    def draw(self):
        self.canvas.coords(self.id, self.getBox(self.size))
        #self.canvas.coords(self.r_eye_id, self.getBox(2, (-2, 4)))
        #self.canvas.coords(self.l_eye_id, self.getBox(2, (2, 4)))

    def getBox(self, r, (tx, ty)=(0, 0)):
        return (self.pos.x-r + tx, self.pos.y-r + ty,
                    self.pos.x+r + tx, self.pos.y+r + ty)
