from srtmath import *
class Sphere(object):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def intersect(self, ray):
        oc = ray.origin - self.center
        a = ray.direction.length_squared()
        b = 2*(dot(ray.direction, oc))
        c = oc.length_squared() - self.radius**2
        b, t0, t1 = quadratic(a,b,c)
        if b == False:
            return (False, 0, 0, Vector())
        n = normalize(self.center - ray(t0))
        return (True, t0, t1, n)

class Plane(object):
    def __init__(self, p, n):
        self.p = p
        self.n = n
    def intersect(self, ray):
        dn = dot(ray.direction, self.n)
        if dn == 0:
            return (False, 0, 0, Vector())
        t = dot(self.p - ray.origin, self.n)/dot(ray.direction, self.n)
        return (True, t, t, self.n)
        