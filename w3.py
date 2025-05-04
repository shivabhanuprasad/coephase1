# sum of even numbers 
n = int(input("Enter a number: "))
esum = 0
number = 2  
while number <= n:
    esum += number
    number += 2  
print("Sum of even numbers:", esum)