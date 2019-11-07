from itertools import count


def fibo_gen():
    for el in count(1):
        if el > 15:
            break
        yield el


f = 1
for el in fibo_gen():
    f *= el

print(f)