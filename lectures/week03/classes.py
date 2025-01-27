class Person:
    name = "Mark"
    age = 27

person = Person()

print(type(person))

print(person.age)

person1 = Person()
person2 = Person()
person2.name = 'Ramazan'
person2.age = 70

print(person1.name, person1.age)
print(person2.name, person2.age)