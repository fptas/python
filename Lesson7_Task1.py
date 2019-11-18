
class Matrix:
    def __init__(self, elements):
        m = len(elements)
        n = len(elements[0])
        for e in elements[1:]:
            if len(e) != n:
                print(f"Разное число столбцов в строках!")
                self.m, self.n, self.elements = 0, 0, []
                return
        self.elements = elements
        self.m = m
        self.n = n

    def __str__(self):
        result = ""
        for row in self.elements:
            for column in row:
                result += f"{column:>5}"
            result += "\n"
        return result

    def __add__(self, other):
        if self.m != other.m or self.n != other.n:
            print(f"Несоответсвие размерности матриц!")
            return self
        mylist = []
        for row in range(self.m):
            mylist.append([self.elements[row][column] + other.elements[row][column] for column in range(self.n)])
        return Matrix(mylist)



matrix_1 = Matrix([
    [11, 12, 13],
    [21, 22, 23],
    [331, 332, 333]
])

print(matrix_1)


matrix_2 = Matrix([
    [11, 12, 14],
    [21, 22, 24],
    [331, 332, 334]
])

print(matrix_2)

print(matrix_1 + matrix_2)