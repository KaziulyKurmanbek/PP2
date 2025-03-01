import string
for letter in string.ascii_uppercase:
        filename = f"{letter}.txt"
        try:
            with open(filename, "x") as file:
                file.write(f"This is file {filename}\n")
            print(f"Created file: {filename}")
        except FileExistsError:
            print(f"File {filename} already exists. Skipping creation.")