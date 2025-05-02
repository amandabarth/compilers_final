class Point:
    x : int
    y : int

class Line:
    start : Point
    end : Point

def difference_x(l: Line) -> int:
    l_end = l.end
    l_start = l.start
    return l_end.x - l_start.x

def difference_y(l: Line) -> int:
    l_end = l.end
    l_start = l.start
    return l_end.y - l_start.y

p1 = Point(1,2)
p2 = Point(5, 5)
line = Line(p1,p2)
print(difference_x(line))
print(difference_y(line))