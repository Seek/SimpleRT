from srtmath import *
from srtshapes import *
import numpy as np
import scipy.misc
import time
WIDTH = 1280
HEIGHT = 720
SPHERE_COLOR = [0,255,0]
if __name__ == "__main__":
    objects = []
    objects.append(Sphere(Point(), 500))
    # objects.append(Plane(Point(0, 0, 750), Vector(0,0,-1)))
    light = Point(0, 700, 1000)
    image = np.zeros((WIDTH, HEIGHT, 3), dtype = np.uint8)
    startT = time.clock()
    print('Began rendering at {0}'.format(startT))
    for i in range(WIDTH):
        for j in range(HEIGHT):
            #Generate a ray at the current pixel
            r = Ray(Point(i, j, -1000), Vector(0,0,1))
            tHit = float("inf")
            normal = None
            b = False
            for obj in objects:
                b, t0, t1, n = obj.intersect(r)
                if b:
                    if t0 < tHit:
                        tHit = t0
                        normal = n
            #Calculate path to light
            if not b:
                image[i,j,0] = 0
                image[i,j,1] = 0
                image[i,j,2] = 0
                break
            p = r(tHit)
            tol = normalize(p - light)
            c = max(dot(normal, tol), 0)
            image[i,j,0] = c * SPHERE_COLOR[0]
            image[i,j,1] = c * SPHERE_COLOR[1]
            image[i,j,2] = c * SPHERE_COLOR[2]
    print('This render took {0} seconds'.format(time.clock() - startT))
    scipy.misc.imsave('./render.png', image)
