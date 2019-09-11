# Program to add tuple, which contains values from 
# two lists of same size, to an empty set.


# Function to add tuples to set
def create(list1,list2,set1):
    for (i,j) in zip(list1,list2):
        set1.add((i,j))


# List 1 
list1 = [int (x) for x in input().split()]

# List 2
list2 = [int (x) for x in input().split()]

# Empty set 
set1 = set()

create(list1, list2, set1)

# Printing set 
print(set1)
