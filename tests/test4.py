class Point:
    x : int
    y : int

class Line:
    start : Point
    end : Point

p1 = Point(0,0)
p2 = Point(3,3)
line = Line(p1, p2)

print(line.start)
print(line.end)
