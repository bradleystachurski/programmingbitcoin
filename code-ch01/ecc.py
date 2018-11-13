from unittest import TestCase
from tabulate import tabulate

class FieldElement:

    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = f'Num {num - 1} not in field range 0 to {prime - 1}'
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return f'FieldElement_{self.prime}({self.num})'

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        if other is None:
            return True
        return self.prime != other.prime or self.num != other.num

    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot subtract two numbers in different Fields')
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot multiply two numbers in different Fields')
        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)

    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot divide two numbers in different Fields')
        num = self.num * pow(other.num, self.prime - 2, self.prime) % self.prime
        return self.__class__(num, self.prime)

    def __gt__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot compare two numbers in different Fields')
        return self.num > other.num


class FieldElementTest(TestCase):

    def test_ne(self):
        a = FieldElement(2, 31)
        b = FieldElement(2, 31)
        c = FieldElement(15, 31)
        self.assertEqual(a, b)
        self.assertTrue(a != c)
        self.assertFalse(a != b)

    def test_add(self):
        a = FieldElement(2, 31)
        b = FieldElement(15, 31)
        self.assertEqual(a + b, FieldElement(17, 31))
        a = FieldElement(17, 31)
        b = FieldElement(21, 31)
        self.assertEqual(a + b, FieldElement(7, 31))

    def test_sub(self):
        a = FieldElement(29, 31)
        b = FieldElement(4, 31)
        self.assertEqual(a - b, FieldElement(25, 31))
        a = FieldElement(15, 31)
        b = FieldElement(30, 31)
        self.assertEqual(a - b, FieldElement(16, 31))

    def test_mul(self):
        a = FieldElement(24, 31)
        b = FieldElement(19, 31)
        self.assertEqual(a * b, FieldElement(22, 31))

    def test_pow(self):
        a = FieldElement(17, 31)
        self.assertEqual(a**3, FieldElement(15, 31))
        a = FieldElement(5, 31)
        b = FieldElement(18, 31)
        self.assertEqual(a**5 * b, FieldElement(16, 31))

    def test_div(self):
        a = FieldElement(3, 31)
        b = FieldElement(24, 31)
        self.assertEqual(a / b, FieldElement(4, 31))
        a = FieldElement(17, 31)
        self.assertEqual(a**-3, FieldElement(29, 31))
        a = FieldElement(4, 31)
        b = FieldElement(11, 31)
        self.assertEqual(a**-4 * b, FieldElement(13, 31))

def print_exercise_5():
    for l in (23, 29, 30, 31, 32):
        print(f'=============================\n'
              f'            l={l}\n'
              f'=============================\n')
        for k in (1, 3, 7, 13, 18):
            print(f'------------------------------\n'
                  f'            k={k}\n'
                  f'------------------------------\n')
            original_set = [FieldElement(i, l) for i in range(l)]
            mult_set = [FieldElement(i, l) * FieldElement(k, l) for i in range(l)]
            sorted_set = sorted(mult_set)
            subt_set = [sorted_set[i] - original_set[i] for i in range(l)]
            printable_set = []
            for i in range(l):
                printable_set.append([original_set[i], sorted_set[i], subt_set[i]])
            print(tabulate(printable_set, headers=["original", "mult", "diff"], showindex=True))

def print_exercise_7():
    print(f'=============================\n'
          f'          NON PRIME\n'
          f'=============================\n')
    for p in (4, 6, 8, 9, 10):
        print(f'=============================\n'
              f'            p={p}\n'
              f'=============================\n')
        original_set = [FieldElement(i, p) for i in range(p)]
        pow_set = [FieldElement(i, p) ** (p - 1) for i in range(p)]
        printable_set = []
        for i in range(p):
            printable_set.append([original_set[i], pow_set[i]])
        print(tabulate(printable_set, headers=["original", "pow"], showindex=True))

    print(f'=============================\n'
          f'            PRIME\n'
          f'=============================\n')
    for p in (7, 11, 17, 31, 43):
        print(f'=============================\n'
              f'            p={p}\n'
              f'=============================\n')
        original_set = [FieldElement(i, p) for i in range(p)]
        pow_set = [FieldElement(i, p) ** (p - 1) for i in range(p)]
        printable_set = []
        for i in range(p):
            printable_set.append([original_set[i], pow_set[i]])
        print(tabulate(printable_set, headers=["original", "pow"], showindex=True))

if __name__ == '__main__':
    pass # un/comment to see exercise results
    # print_exercise_5()
    # print_exercise_7()

