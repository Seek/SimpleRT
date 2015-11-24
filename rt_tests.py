import unittest
from srtmath import *

class TestRayMethods(unittest.TestCase):
    def setUp(self):
        self.p = Point(0,0,0)
        self.dir = Vector(0,0,1)
        self.r = Ray(self.p, self.dir)
    def test_call_method(self):
        t = self.r(2.0)
        self.assertIsInstance(t, Point)
        self.assertEqual(t.x, 0)
        self.assertEqual(t.y, 0)
        self.assertEqual(t.z, 2)
    
class TestPointMethods(unittest.TestCase):
    def setUp(self):
        self.p = Point(1,2,3)
        self.pp = Point(3,2,3)
    def test_add(self):
        t = self.p + Vector(2,2,3)
        self.assertEqual(t.x, 3)
        self.assertEqual(t.y, 4)
        self.assertEqual(t.z, 6)
    def test_iadd(self):
        self.p += Vector()
        self.assertEqual(self.p.x, 1)
        self.assertEqual(self.p.y, 2)
        self.assertEqual(self.p.z, 3)
    def test_sub(self):
        t = self.p - self.pp 
        self.assertIsInstance(t, Vector)
        self.assertEqual(t.x, -2)
        self.assertEqual(t.y, 0)
        self.assertEqual(t.z, 0)
        t = self.p - Vector(1,1,1)
        self.assertIsInstance(t, Point)
        self.assertEqual(t.x, 0)
        self.assertEqual(t.y, 1)
        self.assertEqual(t.z, 2)
    def test_isub(self):
        self.p -= Vector()
        self.assertEqual(self.p.x, 1)
        self.assertEqual(self.p.y, 2)
        self.assertEqual(self.p.z, 3)
    def test_distance(self):
        self.assertEqual(distance(self.p, self.pp), 2)
    def test_distance_sqaured(self):
        self.assertEqual(distance_squared(self.p, self.pp), 4)

class TestVectorMethods(unittest.TestCase):
    def setUp(self):
        self.v = Vector(1,2,3)
    def test_add(self):
        w = self.v + Vector(1,1,1)
        self.assertEqual(w.x, 2)
        self.assertEqual(w.y, 3)
        self.assertEqual(w.z, 4)
    def test_iadd(self):
        self.v += Vector()
        self.assertEqual(self.v.x, 1)
        self.assertEqual(self.v.y, 2)
        self.assertEqual(self.v.z, 3)
    def test_sub(self):
        w = self.v - Vector(1, 2, 3)
        self.assertEqual(w.x, 0)
        self.assertEqual(w.y, 0)
        self.assertEqual(w.z, 0)
    def test_isub(self):
        self.v -= Vector()
        self.assertEqual(self.v.x, 1)
        self.assertEqual(self.v.y, 2)
        self.assertEqual(self.v.z, 3)
    def test_mul(self):
        w = self.v * 0.5
        self.assertEqual(w.x, 1 * 0.5)
        self.assertEqual(w.y, 2 * 0.5)
        self.assertEqual(w.z, 3 * 0.5)
    def test_imul(self):
        self.v *= 1
        self.assertEqual(self.v.x, 1)
        self.assertEqual(self.v.y, 2)
        self.assertEqual(self.v.z, 3)
    def test_neg(self):
        w = -self.v
        self.assertEqual(w.x, -1)
        self.assertEqual(w.y, -2)
        self.assertEqual(w.z, -3)
    def test_dot(self):
        self.assertEqual(dot(Vector(1,1,1), Vector(3,3,3)), 9)
    def test_cross(self):
        w = cross(Vector(1,1,1), Vector(3,2,3))
        self.assertEqual(w.x, 1)
        self.assertEqual(w.y, 0)
        self.assertEqual(w.z, -1)
    def test_len_sq(self):
        self.assertEqual(self.v.length_squared(), 14)
    def test_len(self):
        self.assertEqual(self.v.length(), (14)**(1/2))
    def test_normalize(self):
        vn = normalize(self.v)
        self.assertEqual(vn.x, 1/(14)**(1/2))
        self.assertEqual(vn.y, 2/(14)**(1/2))
        self.assertEqual(vn.z, 3/(14)**(1/2))
if __name__ == '__main__':
    unittest.main()