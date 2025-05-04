#removing duplicates from a string
s = input("Enter a string: ")
result = ""
for char in s:
    if char not in result:
        result += char
print("Without duplicates:", result)
