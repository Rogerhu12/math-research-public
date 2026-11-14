#!/usr/bin/env python3
"""Exact finite certificates accompanying R271.

The proof is in R271. These checks cover the recovery determinant, full coset
pushforwards including a C_(p^2) class label, the real norm shift, and the
non-split ramified-quotient obstruction. No mathematical conjecture is tested.
"""
from pathlib import Path
from itertools import product
from math import comb
import json
import random
import sympy as s

checks = []


def check(name, value):
    if not value:
        raise AssertionError(name)
    checks.append(name)


determinants = []
for r in range(7):
    zero = (0,) * r
    units = [tuple(int(j == i) for j in range(r)) for i in range(r)]
    rows = [zero]
    for e in units:
        rows += [e, tuple(-v for v in e)]
    pairs = [(i, j) for i in range(r) for j in range(i + 1, r)]
    rows += [tuple(units[i][k] + units[j][k] for k in range(r))
             for i, j in pairs]

    def evaluate(b):
        out = [1]
        for bi in b:
            out += [2 * bi, bi * bi]
        out += [2 * b[i] * b[j] for i, j in pairs]
        return out

    mat = s.Matrix([evaluate(b) for b in rows])
    determinant = int(mat.det())
    check(f"quadratic_evaluation_determinant_rank_{r}",
          determinant == 2 ** (r * (r + 3) // 2))
    determinants.append({"class_p_rank": r, "size": len(rows),
                         "determinant": str(determinant)})

p = 7
exponents = (1, 2)
orders = (p,) + tuple(p ** e for e in exponents)
rng = random.Random(27120261113)
raw = {}
for _ in range(31):
    g = tuple(rng.randrange(n) for n in orders)
    raw[g] = (raw.get(g, 0) + rng.randrange(1, p)) % p
raw = {g: a for g, a in raw.items() if a}

constant = sum(raw.values()) % p
linear = [sum(a * g[i] for g, a in raw.items()) % p for i in range(3)]
quadratic = [[sum(a * g[i] * g[j] for g, a in raw.items()) % p
              for j in range(3)] for i in range(3)]

observations = []
for b in product(range(p), repeat=2):
    full = [0] * p
    for g, a in raw.items():
        j = (g[0] + b[0] * g[1] + b[1] * g[2]) % p
        full[j] = (full[j] + a) % p
    moment1 = sum(j * a for j, a in enumerate(full)) % p
    moment2 = sum(comb(j, 2) * a for j, a in enumerate(full)) % p
    w = (1,) + b
    predicted1 = sum(w[i] * linear[i] for i in range(3)) % p
    predicted2 = sum(w[i] * w[j] * quadratic[i][j]
                     for i in range(3) for j in range(3)) % p
    check(f"all_p_and_p_squared_class_labels_quotient_{b[0]}_{b[1]}",
          sum(full) % p == constant and moment1 == predicted1
          and (2 * moment2 + moment1) % p == predicted2)
    observations.append({"b": list(b), "moments": [constant, moment1, moment2]})

lookup = {tuple(o["b"]): (2 * o["moments"][2] + o["moments"][1]) % p
          for o in observations}
inv2, inv4 = pow(2, -1, p), pow(4, -1, p)
recovered = [[0] * 3 for _ in range(3)]
recovered[0][0] = lookup[(0, 0)]
for i in range(2):
    e = tuple(int(j == i) for j in range(2))
    me = tuple(-v % p for v in e)
    recovered[0][i + 1] = recovered[i + 1][0] = (
        inv4 * (lookup[e] - lookup[me])) % p
    recovered[i + 1][i + 1] = (inv2 * (
        lookup[e] + lookup[me] - 2 * lookup[(0, 0)])) % p
recovered[1][2] = recovered[2][1] = inv2 * (
    lookup[(1, 1)] - lookup[(1, 0)] - lookup[(0, 1)] + lookup[(0, 0)]) % p
check("six_actual_quotients_recover_all_six_quadratic_entries", recovered == quadratic)

T, Y = s.symbols("T Y")
norm = s.Poly(sum((1 + Y) ** j for j in range(p)), Y, modulus=p)
check("p_class_norm_is_top_augmentation_monomial", norm.as_expr() == Y ** (p - 1))
source = s.Poly(T ** 2, T, Y, modulus=p)
norm_source = s.Poly(norm.as_expr() * source.as_expr(), T, Y, modulus=p)
check("norm_source_has_exact_degree_p_plus_one",
      min(sum(m) for m in norm_source.monoms()) == p + 1)
check("actual_pushforward_keeps_second_moment", source.eval(Y, 0).as_expr() == T ** 2)
check("second_pushforward_after_norm_is_zero", norm_source.eval(Y, 0).is_zero)

# The norm embedding of k[C_p] in k[C_p x C_p] has one disjoint support per coset.
norm_embedding = s.zeros(p * p, p)
for i, j in product(range(p), repeat=2):
    norm_embedding[i * p + j, i] = 1
check("norm_embedding_remains_injective_when_p_divides_class_number",
      norm_embedding.rank() == p)

# Non-split G=C_(p^2), inertia t=g^p: all homomorphisms to F_p kill t.
check("nonsplit_cyclic_p_squared_has_no_ramified_degree_p_quotient",
      all((p * b) % p == 0 for b in range(p)))

# Two actual coset pushforwards differ on the source (s-1)^2.
hilbert_source = {(0, 0): 1, (0, 1): -2, (0, 2): 1}
hilbert_quotients = []
for b in (0, 1):
    pushed = [0] * p
    for (a, c), value in hilbert_source.items():
        pushed[(a + b * c) % p] = (pushed[(a + b * c) % p] + value) % p
    hilbert_quotients.append(pushed)
check("unramified_direction_square_hidden_by_one_quotient",
      hilbert_quotients[0] == [0] * p)
check("same_source_detected_by_another_ramified_quotient",
      sum(comb(j, 2) * a for j, a in enumerate(hilbert_quotients[1])) % p == 1)

J = s.Matrix([[1, 0, 0], [1, 1, 0], [0, 1, 1]])
check("unipotent_observation_has_order_p", (J ** p - s.eye(3)).applyfunc(lambda a: a % p) == s.zeros(3))
check("unipotent_observation_keeps_both_nontrivial_extensions",
      (J - s.eye(3)) ** 3 == s.zeros(3) and (J - s.eye(3)) ** 2 != s.zeros(3))

out = {
    "result": "R271",
    "check_count": len(checks),
    "all_passed": True,
    "checks": checks,
    "quadratic_evaluation_determinants": determinants,
    "full_class_example": {
        "p": p, "group_orders": list(orders),
        "raw_nonzero_label_count": len(raw),
        "constant": constant, "linear_moments": linear,
        "quadratic_moments": quadratic,
        "recovered_quadratic_moments": recovered,
        "all_ramified_quotient_moments": observations,
    },
    "norm_shift_example": {
        "source": "(t-1)^2", "class_group": "C_7",
        "norm_source": "(s-1)^6*(t-1)^2", "exact_total_degree": p + 1,
        "true_quotient_second_moment": 1,
        "wrong_norm_then_pushforward": 0,
    },
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(out, indent=2) + "\n")
print(f"PASS: {len(checks)} exact checks; {output.name}")
