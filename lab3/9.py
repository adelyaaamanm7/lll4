import math
def sph(rad):
    return (4/3) * math.pi * rad**3 
rad = float(input())
volume = sph(rad)
print(f"Volume of sphere is: {volume}")