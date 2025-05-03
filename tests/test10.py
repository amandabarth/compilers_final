class Phone:
    areacode: int
    middle: int
    end: int

number = Phone(123,456,7890)
if number.areacode < 999:
    print(number.areacode)
else:
    print(False)
if number.middle < 9999:
    print(number.middle)
else:
    print(False)
if number.end < 9999:
    print(number.end)
else:
    print(False)