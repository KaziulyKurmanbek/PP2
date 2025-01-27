setq = {'BMW', 'Mers', 'Toyota'}
print(setq)


print(sorted(setq))

while True:
    item = input("Add-> ")
    if item.lower() == "exit":
        print("Final set:", sorted(setq) )
        break
    setq.add(item)
    print("Current set:", sorted(setq)) 
