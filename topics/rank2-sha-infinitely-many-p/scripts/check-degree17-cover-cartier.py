#!/usr/bin/env python3
"""Small exact Cartier audit for the fixed degree-17 theta candidate cover.

Only integer polynomial arithmetic modulo 11 is used. The target b_12 is the
already certified global rational coefficient after scaling E17 to E1.
"""
from fractions import Fraction


def mul(a, b, p):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j]+x*y) % p
    return out


def power(a, n, p):
    out = [1]
    while n:
        if n & 1:
            out = mul(out, a, p)
        a = mul(a, a, p)
        n >>= 1
    return out


def cartier(f, genus, p):
    coefficients = power(f, (p-1)//2, p)
    return [[coefficients[p*i-j] if 0 <= p*i-j < len(coefficients) else 0
             for j in range(1, genus+1)]
            for i in range(1, genus+1)]


def determinant2(a, p):
    return (a[0][0]*a[1][1]-a[0][1]*a[1][0]) % p


def elliptic_trace(coefficients, p):
    total = 0
    for x in range(p):
        value = sum(c*pow(x, j, p) for j, c in enumerate(coefficients)) % p
        if value:
            total += 1 if pow(value, (p-1)//2, p) == 1 else -1
    return -total


p = 11
# C4: y^2=x(x^4-1)(5x^4-2x^2+1).
f4 = [0, -1, 0, 2, 0, -4, 0, -2, 0, 5]
H4 = cartier(f4, 4, p)
expected = [[0, 6, 0, 10], [2, 0, 9, 0],
            [0, 8, 0, 6], [9, 0, 2, 0]]
assert H4 == expected
A = [[H4[i][j] for j in (1, 3)] for i in (0, 2)]
B = [[H4[i][j] for j in (0, 2)] for i in (1, 3)]
assert determinant2(A, p) == determinant2(B, p) == 0
AB = [[sum(A[i][k]*B[k][j] for k in range(2)) % p
       for j in range(2)] for i in range(2)]
assert AB == [[3, 8], [4, 7]]
assert (AB[0][0]+AB[1][1]) % p == 10

# C2: y^2=5x^6+3x^4-x^2+1.
H2 = cartier([1, 0, -1, 0, 3, 0, 5], 2, p)
assert H2 == [[9, 0], [0, 6]]
assert elliptic_trace([32, -8, 0, 1], p) == 6
assert elliptic_trace([5, 3, -1, 1], p) == -2

b12_E1 = Fraction(9313603, 50400*17**2)
assert b12_E1 == Fraction(32227, 50400)
b12_mod11 = b12_E1.numerator*pow(b12_E1.denominator, -1, p) % p
assert b12_mod11 == 7

print("C4 Cartier matrix:", H4)
print("CM blocks:", A, B)
print("Both block determinants are zero; AB has trace 10 modulo 11.")
print("C2 Cartier matrix:", H2)
print("Actual normalized b_12(E1) modulo 11:", b12_mod11)
print("The actual coefficient is a unit while the proposed determinants vanish.")
