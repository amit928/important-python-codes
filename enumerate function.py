l1=[3,2,4,5,7]
# for i,value in enumerate(l1):
#     print(i,value)

for i,value in enumerate(l1):
    if(value==5):
        print("Element is present at",i)
        break
else:
    print("Element is not present")
