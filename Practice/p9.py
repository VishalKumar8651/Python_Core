#Conditional Statement

#number is positive negative or zero;
x = int(input("Enter a number"))
if(x<0):
    print("X :" , x ,"is Negative")
    x = 0-x
    print(x)

elif(x>0):
    print("X :" , x ,"is positive")
else:
    print("X is Zero")



#Largest Among Numbers 
list = [1 , 2 , 3, 4]
n = len(list)
maxim =list[0]
for i in range (0,n):
    if(list[i]>maxim):
        maxim = list[i]

print(maxim)


#Calculator
while(True):

    print("1. Add")
    print("2.Minus")
    print("3.Multiply")
    print("4.Divison")

    def sum(a,b):
        ans = a+b
        print("Sum :", ans)

    def sub(a,b):
        ans = a-b
        print("Difference :",ans)

    def mul(a,b):
        ans = a*b
        print("Product :", ans)

    def div(a,b):
        ans = a/b
        print("Division :", ans)


    x = int(input("Enter the operation"))
    a = int(input("Enter the first element a "))
    b = int(input("Enter the second element b "))

    if(x==1):
        sum(a,b)
    elif(x==2):
        sub(a,b)
    
    elif(x==3):
        mul(a,b)
    
    elif(x==4):
        div(a,b)
    else:
        print("Enter Valid Operation")
    