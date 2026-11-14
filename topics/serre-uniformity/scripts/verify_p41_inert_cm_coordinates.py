#!/usr/bin/env python3
"""R85: independent exact verification of kappa and inert-CM coordinate squares."""

from fractions import Fraction
from functools import reduce
import hashlib
from itertools import product
import json
from math import lcm
from pathlib import Path
import sys

sys.dont_write_bytecode = True
from verify_p41_twist_certificate import determinant_mod, krylov_rows
from verify_p41_cm_height_ratios import multiply, divide, evaluate_row_scaled, trim


def add(a, b):
    out = [Fraction(0)]*max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return trim(out)


def scale(poly, scalar):
    return trim([scalar*x for x in poly])


def modular_composition(poly, value, modulus):
    out = [Fraction(0)]
    for c in reversed(poly):
        out = divide(add(multiply(out, value), [c]), modulus)[1]
    return out


def check_rows(vleft, pleft, vright, pright, h6):
    degree = max(len(pleft), len(pright))-1
    scalar = lcm(*(c.denominator for c in pleft+pright))
    left = evaluate_row_scaled(vleft, pleft, h6, 6, degree, scalar)
    right = evaluate_row_scaled(vright, pright, h6, 6, degree, scalar)
    assert left == right


def polynomial(item, name):
    return [Fraction(x, item[f"{name}_denominator"])
            for x in reversed(item[f"{name}_numerator_descending"])]


def main(path):
    data = json.loads(path.read_text())
    assert (data["level"], data["weight"], data["star"], data["fricke"]) == (1681, 2, -1, 1)
    assert data["new"] and data["dimension"] == 54 and data["one_algebraic_square_root_no_point_sign"]
    assert (data["path_count"], data["base_pair_coefficient"], data["other_pair_coefficient"]) == (400, 40, 2)
    reference = path.with_name(data["hecke_reference"])
    assert hashlib.sha256(reference.read_bytes()).hexdigest() == data["hecke_reference_sha256"]
    prior = json.loads(reference.read_text())
    twist_reference = path.with_name(prior["twist_reference"])
    assert hashlib.sha256(twist_reference.read_bytes()).hexdigest() == prior["twist_reference_sha256"]
    v4 = json.loads(twist_reference.read_text())["twist4_exact"]
    h6 = prior["six_times_hecke_matrix"]
    inverse6 = pow(6, -1, 1009)
    hmod = [[x*inverse6 % 1009 for x in row] for row in h6]
    for i, discriminant in enumerate((3, 7)):
        row = data[f"twist{discriminant}_exact"]
        actual = determinant_mod(krylov_rows(row, hmod, 1009), 1009)
        assert actual == data["krylov_determinants_mod1009"][i] == (92, 483)[i]
        print(f"D=-{discriminant}: cyclic rank54, determinant mod1009={actual}")
    factors = [[Fraction(x) for x in reversed(item["factor_descending"])]
               for item in data["fields"]]
    total = reduce(multiply, factors, [Fraction(1)])
    for i, (item, f, earlier) in enumerate(zip(data["fields"], factors, prior["fields"]), 1):
        assert item["factor_descending"] == earlier["factor_descending"]
        kappa = polynomial(item, "kappa")
        root3, root7 = polynomial(item, "root3"), polynomial(item, "root7")
        minimal = [Fraction(x) for x in reversed(item["minimal_polynomial_half_kappa_descending"])]
        assert modular_composition(minimal, scale(kappa, Fraction(1, 2)), f) == [0]
        cofactor, remainder = divide(total, f)
        assert remainder == [0]
        check_rows(v4, multiply(kappa, cofactor), data["polarization_row_exact"], cofactor, h6)
        for discriminant, root, multiplier in ((3, root3, 1800), (7, root7, 200)):
            assert divide(root, f)[1] != [0]
            raw = divide(scale(multiply(kappa, multiply(root, root)), Fraction(1, multiplier)), f)[1]
            check_rows(v4, multiply(raw, cofactor), data[f"twist{discriminant}_exact"], cofactor, h6)
        root8 = polynomial(earlier, "root")
        nonzero = 0
        for s7, s8, s3 in product((-1, 1), repeat=3):
            xi = add([Fraction(80)], add(scale(root7, 108*s7),
                     add(scale(root8, 1080*s8), scale(root3, Fraction(16, 3)*s3))))
            nonzero += divide(xi, f)[1] != [0]
        assert nonzero == 8
        print(f"Factor{i}, degree{len(f)-1}: actual kappa, both exact coordinate squares; nonzero xi candidates {nonzero}/8")
    print("All rational identities passed; actual Mordell-Weil signs remain unselected.")


if __name__ == "__main__":
    default = Path(__file__).with_name("data") / "p41_inert_cm_certificate.json"
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else default)
