def counts(lst):
    cnts = {}
    for item in lst:
        if item not in cnts:
            cnts[item] = 1
        else:
            cnts[item] = cnts[item] + 1
    return cnts

lst = [4, 1, 3, 1, 2, 1, 3, 2, 4, 4, 3, 1, 2, 3, 1, 1, 1, 1, 4, 2, 5, 3, 4, 2, 3, 1, 2, 5, 5, 2, 3, 1, 3, 5, 2, 2, 5, 3, 3, 2, 3, 1]
print(counts(lst))