
str = input("Enter a string: ")
ccount = {}
for char in str:
    if char in ccount:
        ccount[char] += 1  
    else:
        ccount[char] = 1   

print("Character frequencies:")
for char in ccount:
    print(f"{char}: {ccount[char]}")
