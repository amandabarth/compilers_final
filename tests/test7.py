class Square:
    a: Point
    b: Point
    c: Point
    d: Point

class Point:
    x : int
    y : int

s1 = Square(Point(3, 3), Point(1,1), Point(3,1), Point(1,3))
print(s1.a)
print(s1.b)
print(s1.c)
print(s1.d)