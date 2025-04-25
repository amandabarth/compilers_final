class Point:
    x: int
    y: int
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(1, 3)
print(p1.x + p1.y)
