from math import *

class Vec2d(object):

    def __init__(self, x=0., y=0.):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return "(x, y) : (%.2f, %.2f)" % (self.x, self.y)

    def toString(self):
        return "pos : (%.2f, %.2f)" % (self.x, self.y)

    def __add__(self, v):
        return Vec2d(self.x+v.x, self.y+v.y)
    def __sub__(self, v):
        return Vec2d(self.x-v.x, self.y-v.y)
    def __iadd__(self, v):
        return Vec2d(self.x+v.x, self.y+v.y)

    def add(self, v):
        if isinstance(v, Vec2d):
            self.x += v.x
            self.y += v.y
        elif isinstance(v, (float, int)):
            self.x += v
            self.y += v
        else:
            print 'Not an instance'
            return

    def multiply(self, factor):
        return Vec2d(self.x*factor, self.y*factor)

    def norm(self):
        return sqrt(self.x**2 + self.y**2)

    def rot(self, theta):
        # rotate the vector by an angle theta (in radian)
        x = self.x
        y = self.y
        self.x = x*cos(theta) - y*sin(theta)
        self.y = x*sin(theta) + y*cos(theta)

    def normalize(self):
        n = self.norm()
        self.x /= n
        self.y /= n

    def modulo(self, (W, H)):
        self.x = self.x % W
        self.y = self.y % H

