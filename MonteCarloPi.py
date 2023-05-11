from random import uniform
from math import sqrt
radius = 50
totalDots = 100000
insideDots = 0
for i in range(totalDots):
    x = uniform(-radius, radius)
    y = uniform(-radius, radius)
    if sqrt(x**2+y**2) <= radius:
        insideDots += 1
print(f'Pi = {4*insideDots/totalDots}')
