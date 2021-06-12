# Square of all elements in the list

# l=[100,200,300,400,500]
# l2=[value*value for value in l]
# print(l2)

# All even numbers in the list 

# l=[10,15,20,25,30,35,40,45,50]
# l2=[value for value in l if value%2==0]
# print(l2)

# Length of each element in the list

# l=["sndi","usahdajs","wehid","wuiedhwid"]
# l2=[len(value) for value in l]
# print(l2)

# Nested for loop in list comprehensions

# l=[(i,j) for i in range(1,10) for j in range(100,110)]
# print(l)

# List of lists

# l=[[1,2,3,4],[3,4,5,6],[4,5,6,7]]
# l2=[val2 for val in l for val2 in val]
# print(l2)

# Print even or odd according to the element in the list

l=[23,24,25,4,56,67,78,89]
l2=["even" if val%2==0 else "odd" for val in l]
print(l2)