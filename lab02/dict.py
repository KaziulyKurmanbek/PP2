student = {
    'name' : 'Gafur',
    'age' : 18 ,
    'major' : 'A & C'
}
print(student)

for x in student.keys():
    print(x)
for i in student.values():
    print(i)
for q, w in student.items():
    print(f"{q}: {w}")