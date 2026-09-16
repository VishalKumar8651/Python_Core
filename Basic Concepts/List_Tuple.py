#Creating a list entered by user
a =[]
for i in range(3):
    a.append(input("Enter the name of fruits"))
print(a)
#Input and Sorting the List
a =[]
for i in range(7):
    a.append(input("Enter the marks"))
a.sort()
print(a)
#Sum of elements of Lists
a = [1,2,3,4]
sum =0
for i in range(len(a)):
    sum += a[i]
print(sum)
print(type(a))
#Counting the number of specific element in a tuple
a =(7,0,8,0,0,9)
print(a.count(0))
