import math
import random
c = float(2)
h = 0.00001
g1=random.uniform(0,2)
while pow(g1,2) > c or pow((g1+1),2) < c:
    g1=random.uniform(0,2)
while c - pow(g1,2) > 0.0001:
    g1 += h
print(g1)

min = 0
max = c
g2=random.uniform(0,2)
while abs(pow(g2,2) - c) > 0.0001:
    if pow(g2,2) > c:
        max = g2
    else:
        min = g2
    g2 = (max + min)/2
print(g2)

g3 = c/2
while abs(pow(g3,2) - c) > 0.0001:
    g3 = (g3+(c/g3))/2
print(g3)