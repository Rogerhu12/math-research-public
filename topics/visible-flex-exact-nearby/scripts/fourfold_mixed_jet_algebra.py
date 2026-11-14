"""Normalized jets in R[u,v]/(u**6,v**3), with generic interval coefficients.

The coefficient type supplies +,-,*,/ and directed sin/cos/exp for its constant
term. Integer zeros remain exact so the nilpotent part has zero constant term.
"""
from __future__ import annotations

from fractions import Fraction
import math


class Jet:
    nx = 5
    np = 2

    def __init__(self, coefficients=None):
        self.c = [[0 for _ in range(self.np + 1)] for _ in range(self.nx + 1)]
        if coefficients is not None:
            for i, row in enumerate(coefficients):
                for j, value in enumerate(row):
                    self.c[i][j] = value

    @classmethod
    def constant(cls, value):
        result = cls()
        result.c[0][0] = value
        return result

    def copy(self):
        return self.__class__([row[:] for row in self.c])

    def __getitem__(self, ij):
        i, j = ij
        return self.c[i][j]

    def __setitem__(self, ij, value):
        i, j = ij
        self.c[i][j] = value

    def __add__(self, other):
        if not isinstance(other, Jet):
            other = self.constant(other)
        return self.__class__([[self[i, j] + other[i, j]
                               for j in range(self.np + 1)]
                              for i in range(self.nx + 1)])

    __radd__ = __add__

    def __neg__(self):
        return self.__class__([[-self[i, j] for j in range(self.np + 1)]
                              for i in range(self.nx + 1)])

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if not isinstance(other, Jet):
            return self.__class__([[self[i, j] * other
                                   for j in range(self.np + 1)]
                                  for i in range(self.nx + 1)])
        result = self.__class__()
        for i in range(self.nx + 1):
            for j in range(self.np + 1):
                total = 0
                for k in range(i + 1):
                    for ell in range(j + 1):
                        left, right = self[k, ell], other[i - k, j - ell]
                        if isinstance(left, int) and left == 0:
                            continue
                        if isinstance(right, int) and right == 0:
                            continue
                        total = total + left * right
                result[i, j] = total
        return result

    __rmul__ = __mul__

    def inverse(self):
        constant = self[0, 0]
        constant_inverse = (constant.reciprocal() if hasattr(constant, "reciprocal")
                            else Fraction(1)/constant if isinstance(constant, (int, Fraction))
                            else 1/constant)
        nu = self.copy()
        nu[0, 0] = 0
        ratio = -nu * constant_inverse
        result = term = self.constant(1)
        for _ in range(1, self.nx + self.np + 1):
            term = term * ratio
            result = result + term
        return result * constant_inverse

    def __truediv__(self, other):
        if isinstance(other, Jet):
            return self * other.inverse()
        def divide(value):
            if isinstance(value, int) and value == 0:
                return 0
            if isinstance(value, (int, Fraction)) and isinstance(other, (int, Fraction)):
                return Fraction(value)/other
            return value/other
        return self.__class__([[divide(self[i, j]) for j in range(self.np + 1)]
                              for i in range(self.nx + 1)])

    def __rtruediv__(self, other):
        return self.inverse() * other

    def __pow__(self, exponent):
        if not isinstance(exponent, int):
            raise TypeError("integer jet powers only")
        if exponent < 0:
            return self.inverse() ** (-exponent)
        result = self.constant(1)
        factor = self
        while exponent:
            if exponent & 1:
                result = result * factor
            exponent //= 2
            if exponent:
                factor = factor * factor
        return result

    def derivative(self, axis=0):
        result = self.__class__()
        if axis == 0:
            for i in range(self.nx):
                for j in range(self.np + 1):
                    result[i, j] = (i + 1) * self[i + 1, j]
        elif axis == 1:
            for i in range(self.nx + 1):
                for j in range(self.np):
                    result[i, j] = (j + 1) * self[i, j + 1]
        else:
            raise ValueError("axis must be x=0 or parameter=1")
        return result

    def sincos(self, constant_sincos):
        sine, cosine = constant_sincos(self[0, 0])
        nu = self.copy()
        nu[0, 0] = 0
        sin_result = self.constant(sine)
        cos_result = self.constant(cosine)
        term = self.constant(1)
        ds = [sine, cosine, -sine, -cosine]
        dc = [cosine, -sine, -cosine, sine]
        for k in range(1, self.nx + self.np + 1):
            term = (term * nu)/k
            sin_result = sin_result + term * ds[k % 4]
            cos_result = cos_result + term * dc[k % 4]
        return sin_result, cos_result

    def exp(self, constant_exp):
        nu = self.copy()
        nu[0, 0] = 0
        result = term = self.constant(1)
        for k in range(1, self.nx + self.np + 1):
            term = (term * nu)/k
            result = result + term
        return result * constant_exp(self[0, 0])


def exact_algebra_check():
    """Nontrivial exact tests of all 18 coefficients, including mixed orders."""
    linear = Jet()
    linear[1, 0] = Fraction(2)
    linear[0, 1] = Fraction(3)
    sine, cosine = linear.sincos(lambda _: (Fraction(0), Fraction(1)))
    reciprocal = (1 + linear).inverse()
    exponential = linear.exp(lambda _: Fraction(1))
    for i in range(6):
        for j in range(3):
            degree = i + j
            coefficient = Fraction(2**i * 3**j, math.factorial(i) * math.factorial(j))
            expected_sine = (0 if degree % 2 == 0 else
                             (-1) ** ((degree - 1) // 2) * coefficient)
            expected_cosine = (0 if degree % 2 else
                               (-1) ** (degree // 2) * coefficient)
            expected_reciprocal = ((-1)**degree * math.factorial(degree) * coefficient)
            assert sine[i, j] == expected_sine, ("sin", i, j)
            assert cosine[i, j] == expected_cosine, ("cos", i, j)
            assert reciprocal[i, j] == expected_reciprocal, ("inverse", i, j)
            assert exponential[i, j] == coefficient, ("exp", i, j)
    return True


if __name__ == "__main__":
    assert exact_algebra_check()
    print("all 18 exact mixed coefficients verified")
