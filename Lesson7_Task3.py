

class Cell:

    def __init__(self, num_nucleuses):
        self.num_nucleuses = num_nucleuses

    def __add__(self, other):
        return Cell(self.num_nucleuses + other.num_nucleuses)

    def __sub__(self, other):
        if self.num_nucleuses <= other.num_nucleuses:
            print(f"Вычитание невозможно!")
            return None
        return Cell(self.num_nucleuses - other.num_nucleuses)

    def __mul__(self, other):
        return Cell(self.num_nucleuses * other.num_nucleuses)

    def __truediv__(self, other):
        if other.num_nucleuses == 0:
            print(f"Деление на 0 невозможно!")
            return None
        return Cell(self.num_nucleuses // other.num_nucleuses)

    def make_order(self, other, num_per_row):
        n_full = other.num_nucleuses // num_per_row
        n_nonfull = other.num_nucleuses % num_per_row
        s = ''
        while n_full > 0:
            s += '\n' + ('*' * num_per_row)
            n_full -= 1
        if n_nonfull > 0:
            s += '\n' + ('*' * n_nonfull)
        return s[1:]


cell_1 = Cell(5)
cell_2 = Cell(3)

cell_3 = (cell_1 * cell_2 * cell_2 + cell_1 - cell_2) / cell_2

print(cell_1.make_order(cell_3, 9))
print("12345678901234567890")
print(cell_1.make_order(cell_3, 20))
