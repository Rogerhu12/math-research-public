#!/usr/bin/env python3
"""R296: exact closed-walk, maximal class, and COMPLETE Hilbert theta checks.

The q=13 original E389 eigenfunction is used only at p=11.  The infinite
prime progression checked symbolically below concerns quadratic fields and
ideal classes, not level raising for those varying primes.
"""
from __future__ import annotations

import json
from math import comb, gcd
from pathlib import Path


HERE = Path(__file__).resolve().parent
# Reuse only R276's definitions. Its top-level computation/output is not run.
source = (HERE / "check-actual-heegner-theta-p11-p13-and-p-class.py").read_text()
namespace: dict = {}
exec(compile(source.split("\nO13, O7 = Order(13), Order(7)")[0],
             "<R276 exact definitions>", "exec"), namespace)
Order, action, kernel = (namespace[x] for x in ("Order", "action", "kernel"))
mm, ma, scale, identity = (namespace[x] for x in ("mm", "ma", "scale", "IDENTITY"))
O = Order(13)
N, p = 389, 11
I = (1, 0, 0, 0)
A = (0, 0, 0, 1)
EXCURSION = (1, 0, 1, 0, 1, 0, 0, 0, 0, 1)
edges = O.norm_elements(2)
edge_matrices = [O.matrix(a, N) for a in edges]
dual = (2, 1, 0)
checks: list[str] = []


def check(name: str, truth: bool) -> None:
    if not truth:
        raise AssertionError(name)
    checks.append(name)


def power(a, n):
    out = I
    while n:
        if n & 1:
            out = O.mul(out, a)
        a = O.mul(a, a)
        n >>= 1
    return out


def mat_power(a, n, modulus):
    out = identity
    while n:
        if n & 1:
            out = mm(out, a, modulus)
        a = mm(a, a, modulus)
        n >>= 1
    return out


def q_residue(a):
    # The residue field of the division order at 13 is F13[i], i^2=-2.
    return ((a[0] + 7*a[2] + 7*a[3]) % 13,
            (a[1] + 7*a[2] + 10*a[3]) % 13)


def qmul(a, b):
    return ((a[0]*b[0]-2*a[1]*b[1]) % 13,
            (a[0]*b[1]+a[1]*b[0]) % 13)


def qpower(a, n):
    out = (1, 0)
    while n:
        if n & 1:
            out = qmul(out, a)
        a = qmul(a, a)
        n >>= 1
    return out


data = json.loads((HERE / "check-actual-heegner-theta-p11-p13-and-p-class.json").read_text())
eigen = data["actual_eigenfunctions"][0]
check("original_E389_q13_p11_source", (eigen["q"], eigen["p"]) == (13, 11))
phi = eigen["phi"]
for ell, eigenvalue in ((2, -2), (3, -2), (5, -3)):
    mats = [O.matrix(a, N) for a in O.norm_elements(ell)]
    check(f"original_phi_Hecke_{ell}", all(
        (sum(phi[action(M, x, N)] for M in mats)-eigenvalue*phi[x]) % p == 0
        for x in range(N+1)))

B, excursion_points = I, [0]
for e in EXCURSION:
    B = O.mul(edges[e], B)
    excursion_points.append(action(edge_matrices[e], excursion_points[-1], N))
check("ten_edge_genuine_excursion", B == (-6, -21, 4, 18)
      and excursion_points[-1] == 0 and O.norm(B) == 2**10)
check("cyclic_nonbacktracking", all(EXCURSION[j+1] != dual[EXCURSION[j]]
      for j in range(9)) and EXCURSION[0] != dual[0] and EXCURSION[-1] != dual[0])
check("loop_A_at_original_N_level", action(edge_matrices[0], 0, N) == 0
      and O.norm(A) == 2 and O.trace(A) == 1)

alpha = O.mul(B, A)
eta = (alpha[0]+20, *alpha[1:])
D = -6671
check("eleven_cycle_alpha_maximal_order", alpha == (-36, -13, 21, 12)
      and O.norm(alpha) == 2**11 and O.trace(alpha) == -39
      and eta == (-16, -13, 21, 12) and O.trace(eta) == 1
      and O.norm(eta) == 1668 and D == -7*953
      and namespace["sp"].isprime(953) and gcd(*alpha[1:]) == 1)
forms = namespace["reduced_forms"](D)
check("complete_maximal_class_number_88", len(forms) == 88)
check("all_original_field_local_conditions", all(
    int(namespace["sp"].kronecker_symbol(D, ell)) == sign
    for ell, sign in ((2, 1), (13, -1), (389, 1))) and D % 11 != 0)

# The complete maximal-order embedding orbit, keeping the q orientation.
states = [r for r in O.norm_elements(1668, False)
          if O.trace(r) == 1 and q_residue(r) == q_residue(eta)]
check("all_88_oriented_maximal_embeddings", len(states) == 88 and q_residue(eta) == (7, 7))
index = {r: j for j, r in enumerate(states)}
origin = index[eta]
lam = O.matrix(eta, N)[3]
check("fixed_original_389_direction", lam == 322 and O.matrix(eta, N) == (68, 0, 1, 322))
points = [kernel(ma(O.matrix(r, N), scale(-lam, identity, N), N), N) for r in states]

# Formula (14) of R276 cannot be reduced at 2; use the genuine order algebra.
basis2 = ((1, 0, 0, 1), (0, 0, 1, 0), (0, 0, 0, 1), (1, 1, 0, 0))


def matrix(r, ell):
    if ell != 2:
        return O.matrix(r, ell)
    return tuple(sum(r[j]*basis2[j][k] for j in range(4)) % 2 for k in range(4))


std = [tuple(int(i == j) for i in range(4)) for j in range(4)]
check("actual_mod2_order_algebra_all_16_products", all(
    matrix(O.mul(v, w), 2) == mm(matrix(v, 2), matrix(w, 2), 2)
    for v in std for w in std))
check("actual_mod2_algebra_isomorphism", len({matrix(v, 2)
      for v in namespace["product"]((0, 1), repeat=4)}) == 16)


def ideal_permutation(ell, root):
    by_kernel = {kernel(matrix(a, ell), ell): a for a in O.norm_elements(ell)}
    out = []
    for r, x in zip(states, points):
        k = kernel(ma(matrix(r, ell), scale(-root, identity, ell), ell), ell)
        a = by_kernel[k]
        rr = O.mul(O.mul(a, r), O.conj(a))
        assert all(v % ell == 0 for v in rr)
        rr = tuple(v//ell for v in rr)
        j = index[rr]
        assert action(O.matrix(a, N), x, N) == points[j]
        out.append(j)
    assert sorted(out) == list(range(88))
    return out


def orbit(P, start):
    out, j = [], start
    while j not in out:
        out.append(j)
        j = P[j]
    assert j == start
    return out


P2, P3 = ideal_permutation(2, 0), ideal_permutation(3, 0)
orb2, orb3 = orbit(P2, origin), orbit(P3, origin)
check("genuine_class_actions_orders_and_commutation", len(orb2) == 11 and len(orb3) == 88
      and all(P2[P3[j]] == P3[P2[j]] for j in range(88)))
check("actual_class_relation_two_equals_three_power64", all(
    orbit(P3, j)[64] == P2[j] for j in range(88)))
labels = {j: 5*k % 11 for k, j in enumerate(orb3)}
check("actual_C11_character_not_arbitrary_cycle_phases", all(
    labels[P2[j]] == (labels[j]+1) % 11 and labels[P3[j]] == (labels[j]+5) % 11
    for j in range(88)))
chosen_points = [0] + excursion_points[:-1]
chosen_values = [phi[x] for x in chosen_points]
check("closed_word_equals_actual_Hilbert_ideal_orbit", [points[j] for j in orb2] == chosen_points)
partial_moments = [sum(comb(j, k)*v for j, v in enumerate(chosen_values)) % 11 for k in range(3)]
check("actual_selected_cycle_moments", partial_moments == [5, 8, 1])

theta = [0]*11
for j in range(88):
    theta[labels[j]] = (theta[labels[j]]+phi[points[j]]) % 11
moments = [sum(comb(j, k)*v for j, v in enumerate(theta)) % 11 for k in range(3)]
check("COMPLETE_Hilbert_theta_and_moments", theta == [9, 9, 7, 6, 7, 8, 3, 8, 7, 6, 7]
      and moments == [0, 0, 9])
check("complete_original_reflection", all(theta[j] == theta[(1-j) % 11] for j in range(11)))

remaining, cosets = set(range(88)), []
while remaining:
    start = min(remaining)
    cyc = orbit(P2, start)
    remaining.difference_update(cyc)
    values = [phi[points[j]] for j in cyc]
    ms = [sum(comb(j, k)*v for j, v in enumerate(values)) % 11 for k in range(3)]
    s = labels[start]
    shifted = [ms[0], (ms[1]+s*ms[0]) % 11,
               (ms[2]+s*ms[1]+comb(s, 2)*ms[0]) % 11]
    cosets.append({"origin_embedding":states[start], "Artin_phase":s,
                   "CM_points":[points[j] for j in cyc], "values":values,
                   "partial_moments":ms,"shifted_moments":shifted})
check("all_eight_cosets_with_true_phase_sum", len(cosets) == 8
      and [sum(c["shifted_moments"][k] for c in cosets) % 11 for k in range(3)] == moments)

# Fixed identities proving the geometric family for ALL primes in the AP.
M = 16296
check("genuine_fixed_progression_periods", M == 168*388//4 and gcd(11, M) == 1
      and qpower(q_residue(A), 168) == (1, 0)
      and mat_power(O.matrix(A, 389), 388, 389) == identity)
check("progression_inert_and_split_discriminant", D % 13 == 11 and D % 389 == 331
      and pow(11, 6, 13) == 12 and 135**2 % 389 == 331)
A10 = power(A, 10)
check("trace_projection_identity", A10 == (34, 0, 0, -11)
      and O.trace(B) == 10 and O.trace(O.mul(B, A)) == -39)
exclusion = []
for sign, expected_norm, expected_v2 in ((1, 74704, 4), (-1, 55202, 1)):
    num = tuple((-9 if j == 0 else 0)+88*A[j]-sign*7*A10[j] for j in range(4))
    nn, v2 = O.norm(num), 0
    temp = nn
    while temp % 2 == 0:
        temp //= 2
        v2 += 1
    check(f"maximal_principal_class_exclusion_sign_{sign}", nn == expected_norm and v2 == expected_v2)
    exclusion.append({"sign":sign,"numerator":num,"norm":nn,"valuation_at_conjugate_two":v2,
                      "only_possible_prime_length":10+v2})
check("last_possible_prime_exception_excluded", O.trace(power(A, 11)) == 67
      and O.trace(alpha) != -67)
num = O.trace(O.mul(O.mul(B, power(O.conj(A), 10)), A))
check("all_progression_primes_unramified_in_new_field", num == -1546
      and num*num-8*1024**2 == -4*23*113*577
      and all(r % M != 11 for r in (2, 7, 23, 113, 577)))

output = {"result":"R296", "all_passed":True, "check_count":len(checks), "checks":checks,
          "scope":"Original E389 theta only at p=11,q=13; varying-prime assertion is geometric class construction only.",
          "loop":A, "excursion_edges":EXCURSION,"excursion_points":excursion_points,
          "excursion_composition":B,"eleven_cycle_alpha":alpha,"D":D,
          "class_number":88,"reduced_forms":forms,"initial_eta":eta,
          "q_orientation":q_residue(eta),"N_eigenvalue":lam,"actual_mod2_basis":basis2,
          "full_88_embeddings":states,"full_88_N_points":points,"class_action_2":P2,
          "class_action_3":P3,"C11_labels":[labels[j] for j in range(88)],
          "selected_cycle_points":chosen_points,"selected_cycle_values":chosen_values,
          "selected_cycle_moments":partial_moments,"complete_theta":theta,
          "complete_moments":moments,"all_eight_cosets":cosets,
          "geometric_prime_progression":{"residue":11,"modulus":M},
          "maximal_class_principality_exclusion":exclusion}
target = Path(__file__).with_suffix(".json")
target.write_text(json.dumps(output,ensure_ascii=False,indent=2)+"\n")
print(f"PASS: {len(checks)} exact closed-walk/full-Hilbert checks; {target.name}")
