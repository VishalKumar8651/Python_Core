'''Given a list of numbers, return the largest number without using max().

Example
Input: [4, 9, 1, 7]
Output: 9
'''

x =list(map(int,input("Enter a number").split()))
largest = x[0]
for i in x :
    if largest<i:
        largest= i
print(largest)