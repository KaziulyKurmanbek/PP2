# pi = 4(1 - 1/3 + 1/5 - 1/7 + 1/9 ...)
p = 0
i = 1
while i in range(10):
    p += (((-1)**(i+1))* (4/(i*2-1)))
    i+=1
print(p)
