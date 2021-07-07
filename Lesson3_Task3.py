"""  3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
        и возвращает сумму наибольших двух аргументов.
"""

def my_func(a, b, c):
    if a <= b and a <= c:
        return b + c
    elif b <= c and b <= a:
        return a + c
    else:
        return a + b

print(f'my_func(1, 2, 3) = {my_func(1, 2, 3)}')
print(f'my_func(1, 3, 2) = {my_func(1, 3, 2)}')
print(f'my_func(2, 1, 3) = {my_func(2, 1, 3)}')
print(f'my_func(2, 3, 1) = {my_func(2, 3, 1)}')
print(f'my_func(3, 1, 2) = {my_func(3, 1, 2)}')
print(f'my_func(3, 2, 1) = {my_func(3, 2, 1)}')

