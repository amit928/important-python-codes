# Format

# n1=300
# n2=234
# print("The value of n1 is {} and n2 is {}".format(n1,n2))
# print("The value of n1 is {v1} and n2 is {v2}".format(v1=n1,v2=n2))
# print("The value of n1 is {} and n2 is {}".format(n2,n1))  #Reverse

# Capitalize and upper ,lower,title

# s="amit Kumar Mallick"
# s=s.capitalize()
# print(s)   #Amit kumar mallick  will be the output
# print(s.capitalize())
# print(s.upper())
# print(s.isupper())
# print(s.islower())
# print(s.istitle())

# Split and Join

# s="amit,kumar,mallick,python"

# print(s.split()) #It will take  all the element in to a list 
# print(s.split(","))

# l=s.split(",")
# print((" ").join(l))  #It will join the list 

# .........maketrans and translate..............

# a="amit"
# b="wxyz"

# c="amit kumar mallick"
# table=str.maketrans(a,b)
# result=c.translate(table)
# print(result)

l=[1,2,3,4,5]
# l.append([4,5,6,7,8,9])
# print(l)
l.extend([10,20,30,40])
print(l)