def binary_search(l1,element):
    if len(l1)==0:
        return False
    else:
        mid=len(l1)//2
        if(element<l1[mid]):
            return binary_search(l1[:mid], element)
        elif(element>l1[mid]):
            return binary_search(l1[mid+1:], element)
        else:
            return True


l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,19,34,46,78,123,345,456,7891345,12349,123401] # The list should be in sorted form for binary searching .
element=34
print(binary_search(l1,element))
