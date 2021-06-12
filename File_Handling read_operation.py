# To read a file You have to open that first by using " open " function . 
# To read that file You have to use" read "function . 

f=open("my_details.txt","r")
# print(f.read())
# #The read function returns a string .

# print(f.read(100))  #It is only read 100 characters in the file . 

# print(f.readlines())
# #The readlines function returns all the data as a list . 

# print(f.readline())
# #This will return one line from the list .

# f=open("laptop_details.txt","r+") # In r+ we can do both read and write .
print(f.read())
f.write("My name is Amit Kumar Maliick")
