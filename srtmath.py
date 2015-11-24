import numpy as np
import scipy as sp

class Point(object):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
    __radd__ = __add__
    
    def __iadd__(self, other):
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            self.z += other.z
            return self
    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        if isinstance(other, Vector):
            return Point(self.x - other.x, self.y - other.y, self.z - other.z)
    def __isub__(self,other):
        if isinstance(other, Vector):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
            return self
    
class Vector(object):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def length_squared(self):
        return self.x**2 + self.y**2 + self.z**2
    def length(self):
        return (self.length_squared())**(1/2)
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
             raise TypeError("unsupported operand type(s) for : '{}' and '{}'").format(self.__class__, type(other))
    __radd__ = __add__
    def __iadd__(self, other):
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            self.z += other.z
            return self
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
             raise TypeError("unsupported operand type(s) for : '{}' and '{}'").format(self.__class__, type(other))
    __radd__ = __add__
    def __isub__(self, other):
        if isinstance(other, Vector):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
            return self
    def __mul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)
    __rmul__ = __mul__
    def __imul__(self, other):
        self.x *= other
        self.y *= other
        self.z *= other
        return self
    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)
    
def dot(v1, v2):
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

def absdot(v1, v2):
    return abs(dot(v1,v2))

def cross(v1, v2):
    return Vector( (v1.y*v2.z - v1.z*v2.y),
                   (v1.z*v2.x - v1.x*v2.z),
                   (v1.x*v2.y - v1.y*v2.x) )
def normalize(v):
    return v * (1/v.length())

def distance(p1, p2):
    return ((p2-p1)).length()

def distance_squared(p1, p2):
    return ((p2-p1)).length_squared()

class Ray(object):
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
        self.depth = 0
        self.time = 0
        self.mint = 0
        self.maxt = float("inf")
    def __call__(self, *args):
        return self.origin + self.direction * args[0]
        
def quadratic(a, b, c):
    discrim = b**2 - 4 * a * c
    if discrim < 0:
        return (False, 0, 0)
    rootd = discrim**(1/2)
    if b < 0:
        q = -0.5*(b - rootd)
    else:
        q = -0.5*(b + rootd)
    t0 = q / a
    t1 = c / q
    if t1 > t0:
        tmp = t1
        t1 = t0
        t0 = 1
    return (True, t0, t1)
