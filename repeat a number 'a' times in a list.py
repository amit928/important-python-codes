def repeat_n(lst):
    result = []
    for element in lst:
        for i in range(element):
            result.append(element)
    return result
 
xx = [3, 1, 8, 9, 8, 0, 1, 5, 0, 4, 3, 4, 7, 1, 5, 4, 6, 6, 3, 9, 7, 9, 6, 2, 1]
print(repeat_n(xx)[30], repeat_n(xx)[50], repeat_n(xx)[70])