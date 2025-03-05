import math
def polygon_area(sides, length):
    if sides < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    return (sides * length**2) / (4 * math.tan(math.pi / sides))

sides = int(input())
length = int(input())

area = int(polygon_area(sides, length))
print(area)
