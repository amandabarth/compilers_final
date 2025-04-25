class Square(int):
    base: int

def area(s:Square) -> int:
    return s.base * s.base

square1 = Square(3)
print(area(square1))