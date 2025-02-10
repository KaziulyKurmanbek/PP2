def gen(stop):
    start = 0
    while( start <= stop ):
        yield start
        start+=1
n = int(input("Number N: "))
nums = gen(n)
for num in nums:
    if num % 2 == 0:
        print(num, end=' ')