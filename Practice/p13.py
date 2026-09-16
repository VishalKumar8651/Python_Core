#TUPLES & LIST


#Convert a list to a tuple and print its length

list = [1 , 2 ,3 ,"abc"]
tuple = tuple(list)
print(type(list))
print(type(tuple))

#Find common elements between two sets.

set1 = { 1 , 2 , 4, 5}
set2 = { 6 , 7 ,  2, 0}
print(set1.intersection(set2))



#Check if an element exists in a tuple

tuple1 = (1 , 2, 3 ,4, 4,6,1)
target = 5
for i in range(len(tuple1)):
    if(i==target):
        print("Target found")
        break


#Remove duplicates using a set.
print(set(list))
print(set(tuple1))