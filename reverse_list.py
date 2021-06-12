# Using function reversing a list

# def reverse_list(lst):
#     new_list=[]
#     for item in lst:
#         new_list=[item]+new_list
#     print(new_list)

# lst=[1,2,3,4]
# reverse_list(lst)

# Using simple list tricks reversing a list

# lst=[1,2,3,4]
# print(lst[::-1])

# Using only for loop reversing a list

lst=[3,2,4,5]
for i in range(len(lst)-1,-1,-1):
    print(lst[i])

