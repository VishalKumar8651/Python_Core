print("Hello World")

#we don't define the data type in python 
x =5
y='hello brother'
z =5.984
print(x+y+z)

#Conditional Statement
if(5>2):
     print("5 is greater than 2")
elif(5==2):
     print("this is not gonna print")
else:
     print("wow")

#Input From User

x = input("Enter the value of String x ") 
y =int(input("Enter the value of integer"))
z = float(input("Enter the decimal value of z"))
print("You have Entered :" +x ,y ,z )

#Control Statement:
#For Loop (integers)

print("Printing 0-4 :")
for i in range(5):
     print(i)
print("Printing 5 to 15: ")
for j in range(5,16):
     print(j)       #won't print 16
print("Printing 0 to 50 with +5 :")
for k in range(0,50,5):
     print(k)       #Print 0-50 with difference of 5 like --> 0,5,10,15,20.....
print("Printing 50 to 0 with 10 difference :")
for L in range(50,0,-10):
     print(L)       #Print --> 50,40,30,20,10


#For Loop for String
print("Printing hello world 5 times :") 
for p in range(5):
     print("Hello World")

#While loop no need to study just remember the syntaxx :---->

# count = 4 
# while count <=10:
#    print("fuck you")
# count++


#   * ENUMERATE *   #

fruits =['Mango','Banana','Apple']
for index,fruit in enumerate(fruits):
     print(index,fruit)
#This prints the index anf then fruit name together untill the loop is executed


#LOOP CONTROL STATEMENT
for i in range(5):
     if i==3:
          break
     print(i)
for i in range(10):
     if i==5:
          continue  
     print(i)
     #i = 5 will not be printed

