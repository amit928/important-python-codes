# Get the power of all elements in a dictionary

# d={i:i**2 for i in range(1,11)}
# print(d)

# Get the ASCII characters from the numbers in a dictionary

# d={x:chr(x) for x in range(97,123)}
# print(d)

l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
d={item:ord(item) for item in l}
print(d)