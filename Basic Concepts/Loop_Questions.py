#Q5 ------->#Printing Tabale of n

n = int(input("Enter the number"))
for i in range(1,10):
    print(n,"x",i,"=", 5*i)


#Q6 -----> Printing indivisual character of String
inputQ6 = input("Enter the String")
for i in inputQ6:
    print(i)


#Q7 --> printing string as it is using loop
fruit = 'banana','apple','mango','guava'
for i in fruit:
    print(i)

#Q8 ----> Strings with Index 
fruits = 'banana','apple','mango','guava'
for index, f1 in enumerate(fruits):
    print(index,f1)

#Q8(i)----> String with index starting with 1

fruitts = 'banana','apple','mango','guava'
for index, f1 in enumerate(fruitts):
    index+=1
    print(index,f1)

#Q9 ---> Printing Vowels of Letter
UserInput = input("Enter The String")
for ch in UserInput:
    if ch in "aeiou":
        print(ch)

#Q10---> Printing square of Even numbers in Vertical form
square =[]
for i in range(2,11):
    if i%2==0:
        square.append(i*i)
print(square)
#REVISION
# 1)
#FACTORIAL
n=int(input("Enter number"))
fact =1
for i in range(1,n+1):
    fact=fact*i
print(fact)
# 2) 
#Prime Numbers
while True:
    Num1 = int(input("Enter the number"))
    count = 0
    if Num1==0 or Num1== 1:
        print("Not A Prime Number")
    else :
        for i in range(1,Num1+1):
            if Num1%i==0 :
             count = count+1
             
        if count>2:
            print("Not a prime number ")
        else :
            print("It's a prime number")

#Q3

