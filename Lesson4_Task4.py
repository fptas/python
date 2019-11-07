
list1 = [1, 2, 3, 4, 5, 3, 14, 5]
list2 = [list1[i] for i in range(len(list1)) if i == list1.index(list1[i])]


print(list2)

