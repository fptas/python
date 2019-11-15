"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random


MINVAL, MAXVAL = 10, 20


ilist = [random.randint(MINVAL * 100, MAXVAL * 100) for i in range(random.randint(MINVAL, MAXVAL))]

with open("Task5.txt", "w") as fobj:
    print(" ".join(map(str, ilist)), file = fobj, end = "")

with open("Task5.txt", "r") as fobj:
    ll = list(map(int, fobj.readline().split()))
    print(f"Чисел в файле: {len(ll)}, Сумма чисел в файле: {sum(ll)}")