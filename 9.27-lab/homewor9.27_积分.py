import math
import random
S = 1*2
n = 10000
c = 0
for i in range(n):
    x = random.uniform(0,1)
    y = random.uniform(0,2)
    if y <= pow(x,3) + pow (x,2):
        c += 1

I = (c/n)*S
print(I)
