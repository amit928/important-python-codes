def count(lst,value):
    i=0
    for item in lst:
        if(item==value):
            i+=1
    return i



lst = [3, 4, 5, 3, 5, 2, 3, 4, 5, 2, 1, 4, 2, 4, 3, 3, 3, 3, 5, 4, 4, 3, 5, 3, 2, 1, 3, 3, 2, 2, 3, 5, 5, 5, 2, 4, 5, 5, 5, 4, 3, 4]
print(count(lst, 1), count(lst, 2), count(lst, 3))