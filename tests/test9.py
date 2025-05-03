class Dog:
    fluffy: bool
    large: bool
    nice: bool

cali = Dog(True, False, False)
tony = Dog(True, True, True)

if cali.fluffy and cali.nice:
    print(True)
else:
    print(False)

if tony.fluffy and tony.large:
    print(True)
else:
    print(False)