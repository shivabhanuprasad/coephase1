# Count Vowels in a Word, using a for loop
word=input("Enter word :")
word=word.lower()
vowelc=0
for char in word:
    if char in 'aeiou':
        vowelc+=1
print("no,of vowels in the given word :",vowelc)