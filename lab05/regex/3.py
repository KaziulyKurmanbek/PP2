import re
text = "/Users/qurmanbek/Desktop/GitHub/PP2/lab05/regex/row.txt"
with open(text, 'r') as file:
    string = file.read().strip()
pattern = "\b[a-z]+_[a-z]+\b"
result = re.findall(pattern, string)
if result:
    print(result)
else:
    print("Not found") 