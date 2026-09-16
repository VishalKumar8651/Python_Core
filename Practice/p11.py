#Count vowels in a string.
x = input("Enter a word")
count =0
for i in x :
    if i in ('a','e','i','o','u'):
     count = count+1
print(count)


# Check if a string is a palindrome
for i in x:
    if(x == x[::-1]):
        print("Palindrome")
        break
    else:
        print("Not a Palindrome")
        break

# Remove all spaces from a string.
x = x.replace(" ", "")
print(x)


#Count occurance of each character
for i in x:
    print(i , "occurs for " ,x.count(i), "times")