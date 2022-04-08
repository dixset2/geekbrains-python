from typing import List


class Matrix:
    def __init__(self, matrix_data: List[List]):
        self.__matrix = matrix_data

        m_rows = len(self.__matrix)
        self.__matrix_size = frozenset([(m_rows, len(row)) for row in self.__matrix])

        if len(self.__matrix_size) != 1:
            raise ValueError("Invalid matrix size")

    def __add__(self, other: "Matrix") -> "Matrix":
        if not isinstance(other, Matrix):
            raise TypeError(f"'{other.__class__.__name__}' "
                            f"incompatible object type")
        if self.__matrix_size != other.__matrix_size:
            raise ValueError(f"Matrix sizes difference")

        result = []

        for item in zip(self.__matrix, other.__matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])

        return Matrix(result)

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])


if __name__ == '__main__':
    matrix1 = Matrix([[2, 3], [4, 5]])
    print(matrix1, '\n')

    matrix2 = Matrix([[20, 30], [40, 50]])
    print(matrix2, '\n')

    print(matrix1 + matrix2)
#

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def expense(self):
        pass

    def __str__(self):
        return str(self.param)


class Coat(Clothes):

    @property
    def expense(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):

    @property
    def expense(self):
        return self.param * 2 + 0.3


a = Coat(48)
b = Suit(1.70)
print(a)
print(a.expense)
print(b.expense)
#
class Cell:
    def __init__(self, cell):
        self.cell = cell
        self.simbol = '*'

    def __str__(self):
        return str(f'Количество ячеек - {self.cell}')

    def __sub__(self, other):
        return Cell(abs(self.cell - other.cell))

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def __add__(self, other):
        return Cell(abs(self.cell + other.cell))

    def make_order(self, count):
        x = self.cell
        while x > 0:
            for k in range(1, count + 1):
                print(self.simbol, end='')
                x -= 1
                if x <= 0:
                    break
            print('\n', end='')


a = Cell(2)
b = Cell(5)
c = Cell(10)
d = Cell(3)

print(a + b)
print(a - b)
print(a * b)
print(c / d)

a.make_order(3)
b.make_order(3)
