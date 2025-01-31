# pi = 4(1 - 1/3 + 1/5 - 1/7 + 1/9 ...)
import math
pi = 0
p = 0
i = 1
while i in range(10000000):
    p += 1/i**2  
    i+=1
pi = math.sqrt(p*6)
print(pi)