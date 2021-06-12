def sum_of_products(lst1, lst2):
    lst3=[]
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if(i==j):
                item=lst1[i]*lst2[j]
                lst3.append(item)
    sop=0
    for item in lst3:
        sop=sop+item;

    return sop

xx = [3, 1, 8, 9, 8, 0, 1, 5, 0, 4, 3, 4, 7, 1, 5, 4, 6, 6, 3, 9, 7, 9, 6, 2, 1]
yy = [9, 6, 4, 2, 6, 7, 2, 9, 6, 6, 9, 1, 7, 4, 3, 3, 4, 7, 8, 7, 3, 7, 7, 7, 3]
print(sum_of_products(xx, yy))

