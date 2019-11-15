"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

mlist = ["Один", "Два", "Три", "Четыре"]


with open("Task4_in.txt", "r") as fobjin:
    with open("Task4_out.txt", "w") as fobjout:
        for line in fobjin:
            word, symbol, num = line.split()
            num = int(num)
            print(f"{mlist[num-1]} {symbol} {num}", file = fobjout)
