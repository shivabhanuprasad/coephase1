#MERGE TWO SORTED LISTS
n=int(input("Enter no.of elements to insert into a list :"))
list1=[]
list2=[9,17,89,123,32]
for i in range (n+1):
    i=int(input("Enter values to insert :"))
    list1.append(i)
print(list1)
list1.sort()
print(list1)
list2.sort()
list1.extend(list2)
print(list1)