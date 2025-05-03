class Triangle:
    a: int
    b: int
    c: int

t = Triangle(3, 4, 5)
if t.a + t.b < t.c:
    print(True)
else:
    print(False)