#!/usr/bin/env python3
"""R281: an actual nonzero conductor-one class jet, with both 389 orientations.

The actual eigenfunction and its uniqueness certificate are the published R276
input.  This script does not modify or rerun R276.  It reconstructs every new
optimal embedding and every ideal-class action by exact quaternion arithmetic.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, isqrt
from pathlib import Path
import json
import sympy as sp

checks = []


def check(name, value):
    if not value:
        raise AssertionError(name)
    checks.append(name)


def norm(v):
    a, b, c, d = v
    return a*a+2*b*b+4*c*c+2*d*d+a*c+a*d+2*b*c+b*d+c*d


def trace(v):
    return 2*v[0]+v[2]+v[3]


def orth(v):
    a, b, c, d = map(F, v)
    return a+c/2+d/2, b+c/2+d/4, c/2, d/4


def from_orth(v):
    a, b, c, d = v
    ans = a-c-2*d, b-c-d, 2*c, 4*d
    assert all(x.denominator == 1 for x in ans)
    return tuple(map(int, ans))


def mul(v, w):
    a, b, c, d = orth(v)
    e, f, g, h = orth(w)
    return from_orth((a*e-2*b*f-13*c*g-26*d*h,
                      a*f+b*e+13*c*h-13*d*g,
                      a*g+c*e-2*b*h+2*d*f,
                      a*h+d*e+b*g-c*f))


def conj(v):
    return trace(v)-v[0], -v[1], -v[2], -v[3]


def mm(A, B, m):
    a, b, c, d = A
    e, f, g, h = B
    return ((a*e+b*g) % m, (a*f+b*h) % m,
            (c*e+d*g) % m, (c*f+d*h) % m)


def ma(A, B, m):
    return tuple((a+b) % m for a, b in zip(A, B))


def scale(a, A, m):
    return tuple(a*x % m for x in A)


ONE = (1, 0, 0, 1)


def matrix(v, m):
    # These two splittings are the same as in R276.
    A, C = (0, 1) if m == 3 else (1, 185)
    assert m in (3, 389) and (A*A+2*C*C+13) % m == 0
    ii, jj = (0, -2 % m, 1, 0), (A, 2*C % m, C, -A % m)
    kk = mm(ii, jj, m)
    e3 = scale(pow(2, -1, m), ma(ma(ONE, ii, m), jj, m), m)
    e4 = scale(pow(4, -1, m), ma(ma(scale(2, ONE, m), ii, m), kk, m), m)
    out = (0, 0, 0, 0)
    for coefficient, basis in zip(v, (ONE, ii, e3, e4)):
        out = ma(out, scale(coefficient, basis, m), m)
    assert (out[0]*out[3]-out[1]*out[2]-norm(v)) % m == 0
    return out


def line(a, b, m):
    if b % m == 0:
        assert a % m
        return m
    return a*pow(b, -1, m) % m


def action(A, x, m):
    a, b, c, d = A
    return line(a if x == m else a*x+b, c if x == m else c*x+d, m)


def kernel(A, m):
    a, b, c, d = A
    assert (a*d-b*c) % m == 0 and any(A)
    return line(-b, a, m) if a or b else line(-d, c, m)


def reduced_forms(D):
    out = []
    for a in range(1, isqrt((-D)//3)+1):
        for b in range(-a, a+1):
            if (b*b-D) % (4*a):
                continue
            c = (b*b-D)//(4*a)
            if c < a or ((abs(b) == a or a == c) and b < 0):
                continue
            out.append((a, b, c))
    return out


base_path = Path(__file__).with_name("check-actual-heegner-theta-p11-p13-and-p-class.json")
base = json.loads(base_path.read_text())
data = base["actual_eigenfunctions"][0]
phi = data["phi"]
p, q, N, D = 11, 13, 389, -2267
c = (1-D)//4
check("actual_R276_eigenline_input", base["all_passed"] and data["q"] == q
      and data["p"] == p and data["node_representatives"] == list(range(N+1)))
for ell in (2, 3, 5):
    check(f"same_actual_Hecke_T{ell}_eigenvalue",
          all((sum(phi[j] for j in targets)-base["E389_aq"][str(ell)]*phi[i]) % p == 0
              for i, targets in enumerate(data["sparse_Hecke_operators"][str(ell)])))
check("D_fundamental_and_legal_local_conditions",
      sp.isprime(-D) and D % 4 == 1 and D % p
      and sp.kronecker_symbol(D, N) == 1
      and sp.kronecker_symbol(D, q) == -1
      and sp.kronecker_symbol(D, 3) == 1)
forms = reduced_forms(D)
check("all_reduced_forms_class_number_11", len(forms) == p)
check("norm3_class_is_not_principal", -D > 12 and isqrt(3)**2 != 3)
check("class_generator_principal_relation",
      324**2+324*11+c*11**2 == 3**11 and 324 % 3 == 0
      and (324+11) % 3 != 0)
check("389_orientation_ideal_relation",
      24**2+24+c == 3*N and 24 % 3 == 0 and 25 % 3 != 0)
r = (-10, -11, 4, 17)
check("actual_maximal_order_embedding", trace(r) == 1 and norm(r) == c)
check("actual_N_matrix", matrix(r, N) == (375, 369, 175, 15))
orientations = [x for x in range(N+1) if action(matrix(r, N), x, N) == x]
check("both_original_389_orientations", orientations == [2, 189])
check("orientation_eigenvalues_match_ideals",
      [(matrix(r, N)[2]*x+matrix(r, N)[3]) % N for x in orientations] == [365, 25])
steps = [(0, 1, 0, -1), (1, -1, 0, 0),
         (1, 1, 0, -1), (1, 1, 0, 0)]
check("all_norm3_isogeny_ideals", all(norm(a) == 3 for a in steps)
      and len({kernel(matrix(a, 3), 3) for a in steps}) == 4)
by_kernel = {kernel(matrix(a, 3), 3): a for a in steps}
outputs = []
expected = ([4, 7, 5, 7, 4, 5, 4, 5, 5, 4, 5],
            [4, 6, 4, 7, 6, 7, 6, 6, 7, 6, 7])
for index, origin in enumerate(orientations):
    states = []
    s, x = r, origin
    for j in range(p):
        a = by_kernel[kernel(matrix(s, 3), 3)]
        states.append({"j": j, "embedding": s, "point": x,
                       "value": phi[x], "norm3_step": a})
        ss = mul(mul(a, s), conj(a))
        assert all(t % 3 == 0 for t in ss)
        s = tuple(t//3 for t in ss)
        x = action(matrix(a, N), x, N)
    check(f"orientation_{origin}_all_class_labels_distinct",
          len({(tuple(t["embedding"]), t["point"]) for t in states}) == p)
    check(f"orientation_{origin}_class_action_returns_exactly", (s, x) == (r, origin))
    check(f"orientation_{origin}_all_embeddings_and_level_orientations",
          all(trace(t["embedding"]) == 1 and norm(t["embedding"]) == c
              and action(matrix(t["embedding"], N), t["point"], N) == t["point"]
              for t in states))
    values = [t["value"] for t in states]
    moments = [sum(comb(j, k)*a for j, a in enumerate(values)) % p for k in range(p)]
    check(f"orientation_{origin}_full_actual_coefficients", values == expected[index])
    check(f"orientation_{origin}_nonzero_second_jet",
          moments[:3] == [0, 0, 4 if index == 0 else 7])
    outputs.append({"origin": origin, "states": states, "theta_coefficients": values,
                    "all_binomial_moments": moments})
check("exact_conjugate_389_transport",
      all((outputs[1]["theta_coefficients"][j]
           +outputs[0]["theta_coefficients"][(j+1) % p]) % p == 0 for j in range(p)))
check("actual_negative_observer_functional_equation",
      all(expected[0][j] == expected[0][(4-j) % p] for j in range(p)))
check("torsion_is_zero_from_two_good_reductions",
      3+1-base["E389_aq"]["3"] == 6
      and (13+1)**2-base["E389_aq"]["13"]**2 == 187
      and sp.gcd(6, 187) == 1 and 187 % 3 and 6 % 13)
old_class = [sum(row) % p for row in base["p_class_source"]["raw_coefficients_class_then_local"]]
old_moments = [sum(comb(j, k)*a for j, a in enumerate(old_class)) % p for k in range(p)]
check("R276_D_minus1307_class_norm_is_genuinely_fourth_order",
      old_class == [4, 10, 7, 7, 10, 4, 10, 7, 1, 7, 10]
      and old_moments[:5] == [0, 0, 0, 0, 1]
      and base["E389_aq"]["43"] % p == 1)
output = {"result": "R281", "all_passed": True, "check_count": len(checks),
          "checks": checks, "base_certificate": base_path.name,
          "D": D, "p": p, "q": q, "class_number": p,
          "reduced_forms": forms, "eta_polynomial": [c, -1, 1],
          "norm3_principal_relation": {"alpha": [324, 11], "norm": 3**11},
          "norm3_times389_relation": {"alpha": [24, 1], "norm": 3*N},
          "both_orientations": outputs,
          "R276_class_norm": {"D": -1307, "coefficients": old_class,
                              "all_binomial_moments": old_moments}}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(output, indent=2)+"\n")
print(f"PASS: {len(checks)} exact checks; {path.name}")
