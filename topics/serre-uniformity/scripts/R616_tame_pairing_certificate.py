#!/usr/bin/env python3
"""Exact, constant-size QQ(zeta_3) certificate for R616 (no p scan)."""
from fractions import Fraction as F
import json
from pathlib import Path


class K:
    def __init__(self, a=0, b=0):
        if isinstance(a, K):
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = F(a), F(b)

    def __add__(self, t):
        t = K(t)
        return K(self.a + t.a, self.b + t.b)

    __radd__ = __add__

    def __neg__(self):
        return K(-self.a, -self.b)

    def __sub__(self, t):
        return self + (-K(t))

    def __mul__(self, t):
        t = K(t)
        return K(self.a * t.a - self.b * t.b,
                 self.a * t.b + self.b * t.a - self.b * t.b)

    __rmul__ = __mul__

    def conjugate(self):
        return K(self.a - self.b, -self.b)

    def __eq__(self, t):
        t = K(t)
        return self.a == t.a and self.b == t.b

    def out(self):
        return [str(self.a), str(self.b)]


def mat(rows):
    return [[K(x) for x in row] for row in rows]


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(a, s):
    return [[s * x for x in row] for row in a]


def kron(a, b):
    return [[a[i][j] * b[k][l]
             for j in range(len(a[0])) for l in range(len(b[0]))]
            for i in range(len(a)) for k in range(len(b))]


def hermitian(v, g, w):
    return mm([[x[0].conjugate() for x in v]], mm(g, w))[0][0]


def run():
    i = mat([[1, 0], [0, 1]])
    c = mat([[-1, -1], [1, 0]])
    s = mat([[0, 1], [1, 0]])
    g = mat([[2, 1], [1, 2]])
    w = mat([[2], [-1], [-1], [2]])
    z = K(0, 1)
    c2 = mm(c, c)
    assert mm(c2, c) == i
    assert mm(s, s) == i
    assert mm(mm(s, c), s) == c2
    for x in [c, s]:
        assert mm(mm(transpose(x), g), x) == g
        assert mm(kron(x, x), w) == w
    plus = scale(add(add(i, scale(c, z * z)), scale(c2, z)), F(1, 3))
    minus = scale(add(add(i, scale(c, z)), scale(c2, z * z)), F(1, 3))
    assert mm(plus, plus) == plus
    assert mm(minus, minus) == minus
    assert add(plus, minus) == i
    assert mm(c, plus) == scale(plus, z)
    assert mm(c, minus) == scale(minus, z * z)
    v1 = mm(kron(plus, minus), w)
    v2 = mm(kron(minus, plus), w)
    assert add(v1, v2) == w
    gg = kron(g, g)
    assert hermitian(w, gg, w) == 18
    assert hermitian(v1, gg, v1) == 9
    assert hermitian(v2, gg, v2) == 9
    assert hermitian(v1, gg, v2) == 0
    assert F(5393, 6150) - F(7, 20) == F(6481, 12300)
    assert F(13, 10) * 2 - F(1, 250) == F(649, 250)
    assert F(6, 7) < F(5393, 6150)
    assert F(1, 10) - F(29, 50) - F(7, 15) > -1
    result = {
        "status": "PASS",
        "scope": "constant-size exact finite H6 tensor and rational constants only",
        "field": "QQ[zeta]/(zeta^2+zeta+1)",
        "C": [[x.out() for x in row] for row in c],
        "S": [[x.out() for x in row] for row in s],
        "G": [[x.out() for x in row] for row in g],
        "invariant_tensor": [x[0].out() for x in w],
        "opposite_character_projections": [
            [x[0].out() for x in v1],
            [x[0].out() for x in v2],
        ],
        "squared_norms": ["18", "9", "9"],
        "mutual_inner_product": "0",
        "positive_primitive_mean_lower": "6481/12300",
        "negative_primitive_mean_lower": "649/250",
        "not_tested_or_claimed": [
            "no prime or L-value scan",
            "no numerical Gross-Zagier constant",
            "no p-adic height or regulator unit",
        ],
    }
    out = Path(__file__).with_name("R616-tame-pairing-certificate.json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "output": str(out),
                      "squared_norms": result["squared_norms"]}))


if __name__ == "__main__":
    run()
