list1 = [4, 5, 8, 465, 7, 6, 9]
list2 = [list1[i] for i in range(1, len(list1)) if list1[i] > list1[i-1]]


print(list2)
