list = []
for i in range(1, 6):       #[1, 6)
    list.append(i)
print(list)

list.clear()

list = [x for x in range(1, 6)]
print(list)

other = [x * 2 for x in range(1,6) if x%2 == 1]
print(other)