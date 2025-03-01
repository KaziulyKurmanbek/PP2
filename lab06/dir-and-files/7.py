filename = str(input("filename: "))
try:
    with open(f"/Users/qurmanbek/Desktop/GitHub/PP2/lab06/dir-and-files/{filename}", 'r') as orig:
        content = orig.read()
    with open(f"/Users/qurmanbek/Desktop/GitHub/PP2/lab06/dir-and-files/copy.txt", 'w') as copy:
        copy.write(content)
except FileExistsError:
    print(f"Error: The file '{filename}' does not exist.")
