from math import gcd

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Знаменатель не может быть равен нулю")
        common = gcd(a, b)
        self.a = a // common
        self.b = b // common

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_a = self.a * other.a
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_a = self.a * other.b - other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.a * other.b == self.b * other.a

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.a * other.b > self.b * other.a

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.a * other.b < self.b * other.a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

# Тесты
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 7, 6'

f_d = f_b * f_a
assert str(f_d) == 'Fraction: 1, 3'

f_e = f_a - f_b
assert str(f_e) == 'Fraction: 1, 6'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True

f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True

print('OK')
