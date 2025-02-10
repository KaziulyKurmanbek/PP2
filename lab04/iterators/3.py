def gen(stop):
    start = 0
    while( start <= stop ):
        if( start % 3 == 0 or start % 4 == 0):
            yield start
        start+=1
n = int(input("Number N: "))
nums = gen(n)
for num in nums:
    print(num)