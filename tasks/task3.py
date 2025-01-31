num = int(input())
students=[]
for i in range(num):
    name = str(input())
    score = float(input())
    students.append([name, score])
students.sort(key=lambda x:x[1])
max1 = students[0][1]
max2 = students[0][1]
for a in students:
    if a[1]>max1:
        max2=max1
        max1=a[1]
    elif a[1] > max2 and a[1]<max1:
        max2 = a[1]
for a in students:
    if a[1]==max2:
        print(a[0])

# GPT :
num = int(input())
students = []

# Read input
for _ in range(num):
    name = input()
    score = float(input())
    students.append([name, score])  # Corrected list storage

# Sort students by score
students.sort(key=lambda x: x[1])

# Find unique sorted scores
unique_scores = sorted(set(score for _, score in students))

# Find second lowest score
if len(unique_scores) < 2:
    print("No second lowest score")
else:
    second_lowest = unique_scores[1]

    # Collect students with second lowest score
    second_lowest_students = sorted([name for name, score in students if score == second_lowest])

    # Print names in alphabetical order
    for student in second_lowest_students:
        print(student)
