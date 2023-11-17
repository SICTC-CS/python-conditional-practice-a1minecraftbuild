import math

def DistanceFormula(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(DistanceFormula(1, 1, 2, 2))
print(DistanceFormula(2, 2, 4, 4))