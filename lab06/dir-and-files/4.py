file_name = 'test.txt'

file = open(f"/Users/qurmanbek/Desktop/GitHub/PP2/lab06/dir-and-files/{file_name}")

sum = 0 

for line in file:
    sum+=1
print(sum)