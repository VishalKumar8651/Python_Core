#Swap
x = int(input("Enter x"))
y = int(input("Enter y"))
temp =y
y=x
x=temp
print("x :", x)
print("y :", y)

#Swap without Temp

a =5
b =6
a = a+b
b = a-b
a=a-b
print("a = ",a)
print("b = ",b)