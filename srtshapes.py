from srtmath import *
class Sphere(object):
    def __init__(origin, radius):
        self.origin = origin
        self.radius = radius
    def intersect(self, ray):
        a = ray.direction.length_squared()
        b = 2*(ray.direction.x * ray.origin.x + ray.direction.y * ray.origin.y + ray.direction.z * ray.origin.z)
        c = ray.origin.x**2 + ray.origin.y**2 + ray.origin.z**2 - self.radius**2
        b, t0, t1 = quadratic(a,b,c)
        if b == False:
            return (False, 0)
        return (True, t0)