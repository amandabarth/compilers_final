class Rectangle(tuple):
    base: int
    height: int

def perimeter(r: Rectangle) -> int:
    return r[0] + r[1]+ r[0] + r[1]

rec1 = Rectangle((3, 6))
print(perimeter(rec1))