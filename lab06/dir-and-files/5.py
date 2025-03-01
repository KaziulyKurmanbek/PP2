file_name = 'text.txt'

file = open(f"/Users/qurmanbek/Desktop/GitHub/PP2/lab06/dir-and-files/{file_name}, w")

content = str(input("write content: "))

file.write(content)