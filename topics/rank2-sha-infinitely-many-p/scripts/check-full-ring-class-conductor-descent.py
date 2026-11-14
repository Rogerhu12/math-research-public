#!/usr/bin/env python3
"""R304: full original CM conductor descent, using R296's existing p=11 field.

This verifies the actual entire conductor-3 and conductor-9 fibres and the
first prime-power norm correction. It adds no new target prime. General
conductor and Kummer assertions are proved in the accompanying note.
"""
from __future__ import annotations

import json
from math import comb, gcd
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
source = (HERE / "check-actual-heegner-theta-p11-p13-and-p-class.py").read_text()
ns: dict = {}
exec(compile(source.split("\nO13, O7 = Order(13), Order(7)")[0],
             "<R276 exact definitions>", "exec"), ns)
O = ns["Order"](13)
action, kernel, ma, scale = (ns[k] for k in ("action", "kernel", "ma", "scale"))
identity = ns["IDENTITY"]
base = json.loads((HERE / "check-closed-walk-and-full-hilbert-trace.json").read_text())
phi = json.loads((HERE / "check-actual-heegner-theta-p11-p13-and-p-class.json").read_text())["actual_eigenfunctions"][0]["phi"]
N, p, ell, D = 389, 11, 3, -6671
checks: list[str] = []


def check(name, truth):
    if not truth:
        raise AssertionError(name)
    checks.append(name)


def add_scalar(v, t):
    return (v[0]+t, *v[1:])


def convolution(a, b):
    out = [0]*p
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[(i+j) % p] = (out[(i+j) % p]+x*y) % p
    return out


def moments(t):
    return [sum(comb(j, k)*x for j, x in enumerate(t)) % p for k in range(3)]


def theta(rows):
    out = [0]*p
    for row in rows:
        label, point = row["maximal_C11_label"], row["N_point"]
        out[label] = (out[label]+phi[point]) % p
    return out


def residue13(r):
    a, b, c, d = r
    return ((a+7*c+7*d) % 13, (b+7*c+10*d) % 13)


rows1 = [{"embedding": r, "N_point": x, "maximal_C11_label": lab,
          "maximal_parent": j}
         for j, (r, x, lab) in enumerate(zip(base["full_88_embeddings"],
                                             base["full_88_N_points"],
                                             base["C11_labels"]))]
check("same_original_full_R296_source", base["all_passed"] and D == base["D"]
      and theta(rows1) == base["complete_theta"] and moments(theta(rows1)) == [0, 0, 9])
norm3 = O.norm_elements(3)
check("four_genuine_norm3_cyclic_isogenies", len(norm3) == 4
      and len({kernel(O.matrix(a, 3), 3) for a in norm3}) == 4)
check("same_original_T3_eigenvalue", ns["ap"](3) == -2 and all(
    (sum(phi[action(O.matrix(a, N), x, N)] for a in norm3)+2*phi[x]) % p == 0
    for x in range(N+1)))


def descend(rows, conductor, eigenvalue, norm):
    children, local_rows = [], []
    target_eigenvalue = (3*eigenvalue-1) % N
    target_norm = 9*norm-2
    for parent, row in enumerate(rows):
        r, x = tuple(row["embedding"]), row["N_point"]
        upward, downward = [], []
        for a in norm3:
            ara = O.mul(O.mul(a, r), O.conj(a))
            xx = action(O.matrix(a, N), x, N)
            if all(v % 3 == 0 for v in ara):
                upward.append(xx)
                continue
            rr = add_scalar(ara, -1)
            assert O.trace(rr) == 1 and O.norm(rr) == target_norm
            assert not all(v % 3 == 0 for v in add_scalar(rr, 1))
            assert kernel(ma(O.matrix(rr, N), scale(-target_eigenvalue, identity, N), N), N) == xx
            children.append({"embedding": rr, "N_point": xx,
                             "maximal_C11_label": row["maximal_C11_label"],
                             "maximal_parent": row["maximal_parent"],
                             "previous_parent": parent, "isogeny": a})
            downward.append(xx)
        assert len(downward) == (2 if conductor == 1 else 3)
        assert len(upward) == (2 if conductor == 1 else 1)
        assert (sum(phi[v] for v in upward+downward)+2*phi[x]) % p == 0
        local_rows.append({"parent": parent, "horizontal_or_up": upward, "down": downward})
    assert len({tuple(row["embedding"]) for row in children}) == len(children)
    return children, local_rows, target_eigenvalue, target_norm


rows3, fibres3, lam3, norm_eta3 = descend(rows1, 1, 322, 1668)
check("all_176_original_conductor3_fibres", len(rows3) == 176 and lam3 == 187 and norm_eta3 == 15010)
check("conductor3_optimal_class_number", len([f for f in ns["reduced_forms"](9*D)
      if gcd(gcd(f[0], f[1]), f[2]) == 1]) == len(rows3))
check("conductor3_q_orientation_and_original_level", all(residue13(row["embedding"]) == (7, 8) for row in rows3))
check("maximal_label_retained_in_every_fibre", all(sum(row["maximal_parent"] == j for row in rows3) == 2 for j in range(88)))

horizontal_labels = []
by_point_and_embedding = {tuple(row["embedding"]): row for row in rows1}
for row in rows1:
    hs = []
    for a in norm3:
        ara = O.mul(O.mul(a, tuple(row["embedding"])), O.conj(a))
        if all(v % 3 == 0 for v in ara):
            rr = tuple(v//3 for v in ara)
            hs.append((by_point_and_embedding[rr]["maximal_C11_label"]-row["maximal_C11_label"]) % p)
    horizontal_labels.append(sorted(hs))
check("true_horizontal_Artin_labels_plus_minus5", all(hs == [5, 6] for hs in horizontal_labels))

E1 = [0]*p
E1[0], E1[5], E1[6] = -2 % p, -1 % p, -1 % p
theta1, theta3 = theta(rows1), theta(rows3)
check("FULL_conductor3_trace_equals_exact_Euler_operator", theta3 == convolution(E1, theta1))
check("conductor3_second_jet_is_augmentation_times_original", moments(E1) == [7, 0, 8]
      and moments(theta3) == [0, 0, 8])

rows9, fibres9, lam9, norm_eta9 = descend(rows3, 3, lam3, norm_eta3)
check("all_528_original_conductor9_fibres", len(rows9) == 528 and lam9 == 171 and norm_eta9 == 135088)
check("conductor9_optimal_class_number", len([f for f in ns["reduced_forms"](81*D)
      if gcd(gcd(f[0], f[1]), f[2]) == 1]) == len(rows9))
E2 = [(-2*x) % p for x in E1]
E2[0] = (E2[0]-2) % p
theta9 = theta(rows9)
check("FULL_conductor9_trace_has_initial_degree_two_not_three", theta9 == convolution(E2, theta1))
check("conductor9_complete_second_jet", moments(E2) == [6, 0, 6] and moments(theta9) == [0, 0, 10])
wrong = E2.copy()
wrong[0] = (wrong[0]-1) % p
check("using_r_instead_of_r_minus_chi_really_fails", theta9 != convolution(wrong, theta1))

# General symbolic prime-power recurrence. H denotes the full horizontal
# Artin operator, not the number of its summands.
a, r, chi, H = sp.symbols("a r chi H")
S = [sp.Integer(1), a]
for n in range(2, 10):
    S.append(sp.expand(a*S[-1]-r*S[-2]))
En = [sp.Integer(1), a-H]
En.append(sp.expand(a*En[1]-(r-chi)))
for n in range(3, 10):
    En.append(sp.expand(a*En[-1]-r*En[-2]))
check("symbolic_all_prime_power_norm_factors_to_degree9", all(
    sp.expand(En[n]-(S[n]-H*S[n-1]+(chi*S[n-2] if n >= 2 else 0))) == 0
    for n in range(1, 10)))

T, b, m1, m2 = sp.symbols("T b m1 m2")
h2 = 2+b*b*T*T
for n in range(1, 10):
    ep = sp.expand(En[n].subs({chi:1, H:h2}))
    e0 = ep.subs(T, 0)
    assert sp.Poly(sp.expand((ep-e0)*(m1*T+m2*T*T)), T).coeff_monomial(T*T) == 0
check("symbolic_full_two_jet_scalar_after_augmentation_zero", True)

output = {"result": "R304", "all_passed": True, "check_count": len(checks), "checks": checks,
          "scope": "Same p=11,q=13,F=-6671; pays full conductor descent, not a new target prime.",
          "Euler_conductor3": E1, "Euler_conductor9": E2,
          "theta_maximal": theta1, "theta_conductor3": theta3, "theta_conductor9": theta9,
          "moments": {"maximal":moments(theta1), "conductor3":moments(theta3), "conductor9":moments(theta9)},
          "all_176_conductor3_classes": rows3, "all_528_conductor9_classes": rows9,
          "actual_fibres_1_to_3": fibres3, "actual_fibres_3_to_9": fibres9,
          "original_N_eigenvalues": {"1":322, "3":lam3, "9":lam9}}
target = Path(__file__).with_suffix(".json")
target.write_text(json.dumps(output, ensure_ascii=False, indent=2)+"\n")
print(f"PASS: {len(checks)} full original conductor-descent checks; {target.name}")
