# # Normal code............
# lotery=[2,3,4,5,6,7]
# lotery_copy=lotery 
# #  Here It just copy the variable name but don't creat another list . So the o/p will be same as the lotery_copy varibale . 
# lotery_copy[1]=12
# print(lotery_copy)
# print(lotery)

# Actual copying list code ..........

lotery=[3,2,5,7,9,1]
lotery_copy=lotery[:]
# Here the lotery[:] is already copying the the "lotery" list . And lotery_copy copy the list from lotery[:] . So the output is changed .
lotery_copy[1]=34
print(lotery)
print(lotery_copy)



