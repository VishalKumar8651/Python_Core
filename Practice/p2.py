'''Write a function that counts the number of vowels (a, e, i, o, u) in a string.

Example
Input: "programming"
Output: 3
'''

x = input("Enter a word")
count =0
for i in x :
    if i in ('a','e','i','o','u'):
        count = count+1
print(count)

