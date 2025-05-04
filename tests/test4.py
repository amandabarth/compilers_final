class Point:
    x : int
    y : int

class Line:
    start : Point
    end : Point

def sum_point(p: Point) -> int:
    return p.x + p.y

p1 = Point(0,0)
p2 = Point(3,3)
line = Line(p1, p2)

ps = line.start
pe = line.end

print(sum_point(ps))
print(pe.x)
