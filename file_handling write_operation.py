# f=open("laptop_details.txt","w")
# f.write("Laptop Name : Acer \nRAM : 4GB \nProcessor : AMD A6 Alite")

f=open("laptop_details.txt","w+")
f.write("Laptop Name : Acer \nRAM : 4GB \nProcessor : AMD A6 Alite")
f.seek(0,0) #It is used to bring the cursor to the first position bcz after writting the datas the cursor go to the last position . 
print(f.read())