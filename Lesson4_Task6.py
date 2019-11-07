from itertools import count
from itertools import cycle


def generator1(n):
    for el in count(n):
        yield el

def generator2(my_list):
    for el in cycle(my_list):
        yield el


i = int(input("Введите начальное число: "))
g1 = generator1(i)

for el in g1:
    print(el)
    if el >= i + 10000:
        break

# ---------------------------------------
input("Нажмите Enter: ")
g2 = generator2(range(i))

j = 0
for el in g2:
    print(el)
    if j >= 10000:
        break
    j += 1
