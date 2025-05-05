class Square:
    a: Point
    b: Point
    c: Point
    d: Point

class Point:
    x : int
    y : int

s1 = Square(Point(3, 3), Point(1,1), Point(3,1), Point(1,3))
p1 = s1.a
print(p1.x)
print(p1.y)
