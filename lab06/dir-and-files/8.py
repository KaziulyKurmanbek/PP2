import os
filename = str(input("filename: "))
file = f"/Users/qurmanbek/Desktop/GitHub/PP2/lab06/dir-and-files/{filename}"
if os.access(file, os.F_OK):
    os.remove(file)
else:
    print("file does not exist!")