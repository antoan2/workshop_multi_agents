import Tkinter as Tk
import random
from geometry import Vec2d

class agent(object):
     
    def __init__(self, canvas, pos=Vec2d(10, 10), speed=Vec2d(1, 1)):
        self.pos = pos
        self.speed = speed
        self.speed.normalize()
        self.dt = 0.02

        self.canvas = canvas
        self.id = self.canvas.create_oval(self.getBox(5),
                                outline='red',
                                fill='blue')
        self.r_eye_id = self.canvas.create_oval(self.getBox(2, (-2, -4)),
                                outline='red',
                                fill='blue')
        self.l_eye_id = self.canvas.create_oval(self.getBox(2, (2, -4)),
                                outline='red',
                                fill='blue')

        self.W = self.canvas.winfo_reqwidth()
        self.H = self.canvas.winfo_reqheight()

    def move(self):
        self.speed.rot(0.5*(2*random.random() - 1))
        self.pos.add(self.speed.multiply(100*self.dt))
        self.pos.modulo((self.W, self.H))
        self.draw()
    
    def draw(self):
        self.canvas.coords(self.id, self.getBox(5))
        self.canvas.coords(self.r_eye_id, self.getBox(2, (-2, 4)))
        self.canvas.coords(self.l_eye_id, self.getBox(2, (2, 4)))

    def getBox(self, r, (tx, ty)=(0, 0)):
        return (self.pos.x-r + tx, self.pos.y-r + ty,
                    self.pos.x+r + tx, self.pos.y+r + ty)
