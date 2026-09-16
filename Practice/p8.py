#Take 3 integers in a single line and print their sum

x= int(input("Enter x : ")) ; y= int(input("Enter y : ")); z= int(input("Enter z : ")); sum = x+y+z ; print("Sum is :" ,sum)

''' Print a number in this format:
Number = 10
Square = 100
'''


print("Number :" , x)
for i in range(2):
    print("Square :" ,x*x)
    break



#f-string
print(f"Sum of a , b and c is {sum}")