#largest values of 3 numbers

a=int(input("Enter your A value :"))
b=int(input("Enter your  B value :"))
c=int(input("Enter your  C value :"))
if a>b and a>c:
    print(a,"A is greater")
elif a<b and c<b:
    print(b,"B is greater")
else:
    print(c,"C is greater")