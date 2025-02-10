def gen(stop):
    start = 1
    while (start <= stop):
        yield start
        start+=1
n = int(input("Number N: "))
nums = gen(n)
for num in nums:
    print(num)