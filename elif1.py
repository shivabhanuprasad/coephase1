
#Create a program that takes two numbers and an operator (+, -, *, /) from the user and performs the corresponding operation.


a=int(input("Enter value :"))
b=int(input("Enter value : "))
result=0
op=input("Enter an operator(+,-,*,/) :")
if op =='+':
    result=a+b
    print(result)
elif op =='-':
    result=a-b
    print(result)
elif op =='*':
    result=a*b
    print(result)
elif op =='/':
    result=a/b
    print(result)

else:
    print("Invalid operation ")
