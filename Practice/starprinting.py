# *
# **
# ***
# ****
# *****
for i in range(1,6):
    for j in range(1,i):
        print("*" , end=" ")
    print()


#1
#1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#      *
#     *  *
#    *  *  *
#  *   *   *  *

for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        print("*", end="")

    print()
print()

# A 
# A B 
# A B C 
# A B C D 
# A B C D E 

for i in range (1,6): 
    ch =65 
    for j in range(i):
            print (chr(ch), end =" ")
            ch+=1
    print()


    #Palindrome code


    for i in range(1, 5):
    # increasing numbers
        for j in range(1, i + 1):
            print(j, end="")
    
        # decreasing numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")
    
        print("")


#len Function to find length of string

print("\n")
ch = 'Ahan'
print("lenght of string is :" ,len(ch))