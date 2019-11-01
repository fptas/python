my_list = input("Введите значения списка через пробел: ").split(" ")
i = 0


l = len(my_list)
while i < (l - l % 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    i += 2
print(my_list)