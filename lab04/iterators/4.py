def gen(a, b):
    while ( a <= b ):
        yield a**2
        a+=1
a = int(input("a: "))
b = int(input("b: "))
nums = gen(a, b)
for num in nums:
    print(num, end=" ")