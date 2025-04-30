class Point:
    x : int
    y : int

class Line:
    start : Point
    end : Point

def difference(l: Line) -> tuple[int, int]:
    return l.end.x - l.start.x, l.end.y - l.start.y

p1 = Point(1,2)
p2 = Point(5, 5)
line = Line(p1,p2)
print(difference(line))