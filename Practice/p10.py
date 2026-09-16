#Print numbers from 1 to 100, but skip multiples of 3.
for i in range(0,100):
    if(i%3!=0):
        print(i)



#Factorial
x = int(input("Enter the number"))
fact = 1
for i in range(x,1,-1):
    fact = fact *i
print("Factorial of ", x ,"is" ,fact)



# reverse the digit 
num = int(input("Enter number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print(rev)



#Another method 

#Converting int to string and reversing through slicing and then again converting it back to the int
x = 123
a = str(x)
print(a[::-1])
ans = int(a)
print(a)
