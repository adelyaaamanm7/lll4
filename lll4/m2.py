import math
def trapezoid_area(height, base1, base2):
    return (1/2) * (base1 + base2) * height
height=float(input())
base1=float(input())
base2=float(input())
area = trapezoid_area(height, base1, base2)
print(area)