import math
n = float(input("Input number of sides: "))
a = float( input("Input the length of a side: "))
each_degree = (math.pi*(n-2))/(2*n)
each_area = math.tan(each_degree)* (a*a/4)
print(each_area * n)