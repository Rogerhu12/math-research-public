#!/usr/bin/env python3
"""Unconditional fixed Thue computation used in R266, not a height search.

Requires cypari2.  PARI's thueinit(..., 1) certifies the number-field input
unconditionally; thue returns the complete integral solution set.
"""

import argparse
import json
from pathlib import Path

from cypari2 import Pari


def mul(a, b):
    # Z[w], w^2 + w + 1 = 0.
    r, s = a
    t, u = b
    return (r * t - s * u, r * u + s * t - s * u)


def cube(a):
    return mul(mul(a, a), a)


def norm(a):
    r, s = a
    return r * r - r * s + s * s


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("R266-fixed-thue-certificate.json"),
    )
    args = parser.parse_args()
    pari = Pari()
    polynomial = pari("x^3 - 3*x + 1")
    tnf = pari.thueinit(polynomial, 1)
    solutions = {
        str(rhs): sorted(
            tuple(map(int, row)) for row in pari.thue(tnf, rhs).python()
        )
        for rhs in (1, 3)
    }
    expected = {
        "1": [(-3, -2), (-1, -1), (0, 1), (1, 0), (1, 3), (2, -1)],
        "3": [(-1, -2), (-1, 1), (2, 1)],
    }
    assert solutions == expected
    for rhs, pairs in solutions.items():
        for u, v in pairs:
            assert u**3 - 3 * u * v**2 + v**3 == int(rhs)

    units = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1)]
    candidates_one = set()
    for u, v in solutions["1"]:
        for sign in (1, -1):
            candidates_one.add((sign * u, sign * v))
            candidates_one.add((sign * v, sign * u))
    values_one = set()
    for gamma in candidates_one:
        for unit in units:
            a, b = mul(unit, cube(gamma))
            if b == -1:
                y = norm(gamma)
                assert a * a + a + 1 == y**3
                values_one.add((a, y))
    assert sorted(values_one) == [(-19, 7), (-1, 1), (0, 1), (18, 7)]

    # F(2u-v,u+v) = 3 G(u,v),
    # G(u,v)=u^3-6u^2v+3uv^2+v^3.
    candidates_three = set()
    for x, y in solutions["3"]:
        assert (x + y) % 3 == 0 and (2 * y - x) % 3 == 0
        u, v = (x + y) // 3, (2 * y - x) // 3
        assert u**3 - 6 * u * u * v + 3 * u * v * v + v**3 == 1
        for sign in (1, -1):
            candidates_three.add((sign * u, sign * v))
            candidates_three.add((sign * v, sign * u))
    values_three = set()
    for gamma in candidates_three:
        for unit in units:
            a, b = mul((1, -1), mul(unit, cube(gamma)))
            if b == -1:
                y = norm(gamma)
                assert a * a + a + 1 == 3 * y**3
                values_three.add((a, y))
    assert sorted(values_three) == [(-2, 1), (1, 1)]

    payload = {
        "result": "R266",
        "method": "PARI thueinit(polynomial,1), complete thue solution sets",
        "conditional_on_GRH": False,
        "pari_version": pari("version()").python(),
        "polynomial": str(polynomial),
        "polynomial_discriminant": int(pari.poldisc(polynomial)),
        "complete_thue_solutions": solutions,
        "complete_x2_plus_x_plus_1_eq_y3": sorted(values_one),
        "complete_x2_plus_x_plus_1_eq_3y3": sorted(values_three),
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, separators=(",", ":")))


if __name__ == "__main__":
    main()
