#!/usr/bin/env python3
"""Exact actual Heegner theta certificates for R276.

All finite Shimura sets, Hecke operators, CM embeddings, and ring-class labels
are constructed here. Dense matrices are only used in memory for finite-field
linear algebra; the output saves the orders, sparse operators, eigenvectors,
nonzero rank minors, CM labels, and true group-ring moments.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb, isqrt
from pathlib import Path
import json
import sympy as sp
from flint import nmod_mat

N = 389
checks = []


def check(name, value):
    if not value:
        raise AssertionError(name)
    checks.append(name)


def mm(A, B, m):
    a, b, c, d = A
    e, f, g, h = B
    return ((a*e+b*g) % m, (a*f+b*h) % m,
            (c*e+d*g) % m, (c*f+d*h) % m)


def ma(A, B, m):
    return tuple((a+b) % m for a, b in zip(A, B))


def scale(a, A, m):
    return tuple(a*x % m for x in A)


IDENTITY = (1, 0, 0, 1)


def line(a, b, m):
    if b % m == 0:
        assert a % m
        return m
    return a * pow(b, -1, m) % m


def action(A, x, m):
    a, b, c, d = A
    return line(a if x == m else a*x+b,
                c if x == m else c*x+d, m)


def kernel(A, m):
    a, b, c, d = A
    assert (a*d-b*c) % m == 0 and any(A)
    return line(-b, a, m) if a or b else line(-d, c, m)


@lru_cache(None)
def ap(q):
    if q == 2:
        count = 1 + sum((y*y+y-x*x*x-x*x+2*x) % 2 == 0
                        for x, y in product(range(2), repeat=2))
    else:
        count = 1
        for x in range(q):
            d = (1 + 4*(x*x*x+x*x-2*x)) % q
            count += 1 + (0 if not d else 1 if pow(d, (q-1)//2, q) == 1 else -1)
    return q + 1 - count


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


class Order:
    def __init__(self, q):
        self.q = q
        self.m = 2 if q == 13 else 1
        assert q in (7, 13)

    def norm(self, v):
        a, b, c, d = v
        if self.q == 13:
            return a*a+2*b*b+4*c*c+2*d*d+a*c+a*d+2*b*c+b*d+c*d
        return a*a+b*b+2*c*c+2*d*d+a*c+b*d

    def trace(self, v):
        return 2*v[0]+v[2]+(v[3] if self.q == 13 else 0)

    def orth(self, v):
        a, b, c, d = map(F, v)
        if self.q == 13:
            return (a+c/2+d/2, b+c/2+d/4, c/2, d/4)
        return (a+c/2, b+d/2, c/2, d/2)

    def from_orth(self, v):
        a, b, c, d = v
        if self.q == 13:
            ans = (a-c-2*d, b-c-d, 2*c, 4*d)
        else:
            ans = (a-c, b-d, 2*c, 2*d)
        assert all(x.denominator == 1 for x in ans)
        return tuple(map(int, ans))

    def mul(self, v, w):
        a, b, c, d = self.orth(v)
        e, f, g, h = self.orth(w)
        m, q = self.m, self.q
        return self.from_orth((a*e-m*b*f-q*c*g-m*q*d*h,
                               a*f+b*e+q*c*h-q*d*g,
                               a*g+c*e-m*b*h+m*d*f,
                               a*h+d*e+b*g-c*f))

    def conj(self, v):
        return (self.trace(v)-v[0], -v[1], -v[2], -v[3])

    @lru_cache(None)
    def norm_elements(self, n, representatives=True):
        q, m = self.q, self.m
        cb = isqrt(4*n//q)
        db = isqrt((16 if q == 13 else 4)*n//(m*q))
        raw = set()
        for c in range(-cb, cb+1):
            for d in range(-db, db+1):
                if q == 13:
                    bound = isqrt(16*n//m)
                    shift, den = 2*c+d, 4
                else:
                    bound = isqrt(4*n//m)
                    shift, den = d, 2
                lo = -((-(-bound-shift))//den)
                hi = (bound-shift)//den
                for b in range(lo, hi+1):
                    B = c+d if q == 13 else c
                    C = self.norm((0, b, c, d))-n
                    disc = B*B-4*C
                    if disc < 0 or isqrt(disc)**2 != disc:
                        continue
                    rt = isqrt(disc)
                    for a2 in {-B+rt, -B-rt}:
                        if a2 % 2:
                            continue
                        v = (a2//2, b, c, d)
                        assert self.norm(v) == n
                        raw.add(v)
        if not representatives:
            return tuple(sorted(raw))
        if q == 13:
            return tuple(sorted(v for v in raw if next(x for x in v if x) > 0))
        return tuple(sorted({min(v, self.mul((0, 1, 0, 0), v),
                                 tuple(-x for x in v),
                                 tuple(-x for x in self.mul((0, 1, 0, 0), v)))
                             for v in raw}))

    @lru_cache(None)
    def embedding(self, ell):
        m, q = self.m, self.q
        ii = (0, -m % ell, 1, 0)
        for a, c in product(range(ell), repeat=2):
            if (a*a+m*c*c+q) % ell:
                continue
            jj = (a, m*c % ell, c, -a % ell)
            kk = mm(ii, jj, ell)
            if q == 13:
                e3 = scale(pow(2, -1, ell), ma(ma(IDENTITY, ii, ell), jj, ell), ell)
                e4 = scale(pow(4, -1, ell), ma(ma(scale(2, IDENTITY, ell), ii, ell), kk, ell), ell)
            else:
                e3 = scale(pow(2, -1, ell), ma(IDENTITY, jj, ell), ell)
                e4 = scale(pow(2, -1, ell), ma(ii, kk, ell), ell)
            return (IDENTITY, ii, e3, e4), (a, c)
        raise AssertionError((q, ell))

    def matrix(self, v, ell):
        basis, _ = self.embedding(ell)
        ans = (0, 0, 0, 0)
        for a, b in zip(v, basis):
            ans = ma(ans, scale(a, b, ell), ell)
        assert (ans[0]*ans[3]-ans[1]*ans[2]-self.norm(v)) % ell == 0
        return ans


def order_certificate(O):
    basis = [tuple(int(i == j) for i in range(4)) for j in range(4)]
    products = [[O.mul(v, w) for w in basis] for v in basis]
    gram = sp.Matrix([[O.trace(v) for v in row] for row in products])
    check(f"order_{O.q}_multiplication_and_discriminant", abs(gram.det()) == O.q**2)
    units = O.norm_elements(1, False)
    check(f"order_{O.q}_all_units", len(units) == (2 if O.q == 13 else 4))
    for n in (2, 3):
        check(f"order_{O.q}_all_norm_{n}_ideals_principal",
              len(O.norm_elements(n)) == n+1)
    # Minkowski gives sqrt(8*q)/pi. The following rational bound avoids pi numerics.
    bound = 4 if O.q == 13 else 3
    check(f"order_{O.q}_Minkowski_bound", 8*O.q < 9*bound**2)
    return {"q": O.q, "multiplication_table": products,
            "trace_gram": [list(map(int, gram.row(i))) for i in range(4)],
            "units": units, "norm_2_representatives": O.norm_elements(2),
            "norm_3_representatives": O.norm_elements(3),
            "Minkowski_strict_integer_bound": bound}


def eigenfunction(O, p):
    if O.q == 13:
        representative = {x: x for x in range(N+1)}
    else:
        ii = O.embedding(N)[0][1]
        representative = {x: min(x, action(ii, x, N)) for x in range(N+1)}
    reps = sorted(set(representative.values()))
    index = {x: i for i, x in enumerate(reps)}
    n = len(reps)
    operators = {}
    constraints = []
    for ell in (2, 3, 5):
        moves = [[index[representative[action(O.matrix(a, N), x, N)]]
                  for a in O.norm_elements(ell)] for x in reps]
        operators[str(ell)] = moves
        if ell != 5:
            for i, targets in enumerate(moves):
                row = [0]*n
                for j in targets:
                    row[j] += 1
                row[i] -= ap(ell)
                constraints.append([x % p for x in row])
    A = nmod_mat(constraints, p)
    X, nullity = A.nullspace()
    check(f"q_{O.q}_p_{p}_T2_T3_common_kernel_dimension_one", nullity == 1)
    phi = [int(X[i, 0]) for i in range(n)]
    first = next(i for i, x in enumerate(phi) if x)
    phi = [x*pow(phi[first], -1, p) % p for x in phi]
    for ell in (2, 3, 5):
        check(f"q_{O.q}_p_{p}_T{ell}_actual_E389_eigenvalue",
              all((sum(phi[j] for j in targets)-ap(ell)*phi[i]) % p == 0
                  for i, targets in enumerate(operators[str(ell)])))
    transposed_rref, rank = A.transpose().rref()
    rows = [next(j for j in range(2*n) if transposed_rref[i, j]) for i in range(rank)]
    cols = [j for j in range(n) if j != first]
    determinant = int(nmod_mat([[constraints[i][j] for j in cols] for i in rows], p).det())
    check(f"q_{O.q}_p_{p}_nonzero_rank_minor", rank == n-1 and determinant != 0)
    return {"p": p, "q": O.q, "node_count": n,
            "node_representatives": reps, "N_embedding_parameters": O.embedding(N)[1],
            "sparse_Hecke_operators": operators, "phi": phi,
            "rank_certificate": {"rows": rows, "columns": cols, "determinant_mod_p": determinant},
            "normalization_first_nonzero_index": first}, representative, index


def torus_labels(O, r, ell):
    R = O.matrix(r, ell)
    for a in range(ell):
        generator = ma(scale(a, IDENTITY, ell), R, ell)
        orbit, cur = [], ell
        while cur not in orbit:
            orbit.append(cur)
            cur = action(generator, cur, ell)
        if len(orbit) == ell+1:
            return {x: j for j, x in enumerate(orbit)}, a
    raise AssertionError("non-split torus has no generator")


def moments(theta, p):
    return [sum(comb(j, k)*a for j, a in enumerate(theta)) % p for k in range(3)]


def class_one_source(O, data, representative, index, D, ell, r, origin, expected):
    p = data["p"]
    check(f"D_{D}_class_number_one", len(reduced_forms(D)) == 1)
    check(f"D_{D}_optimal_maximal_embedding", O.trace(r) == 1 and O.norm(r) == (1-D)//4)
    check(f"D_{D}_original_389_orientation", action(O.matrix(r, N), origin, N) == origin)
    labels, gen = torus_labels(O, r, ell)
    elts = O.norm_elements(ell)
    check(f"D_{D}_all_{ell}_isogenies", len(elts) == ell+1)
    points, values, embeddings = [None]*(ell+1), [None]*(ell+1), [None]*(ell+1)
    kernels = set()
    for a in elts:
        ker = kernel(O.matrix(a, ell), ell)
        kernels.add(ker)
        j = labels[ker]
        x = representative[action(O.matrix(a, N), origin, N)]
        points[j] = x
        values[j] = data["phi"][index[x]]
        embeddings[j] = O.mul(O.mul(a, r), O.conj(a))
    check(f"D_{D}_all_CM_labels_kept", len(kernels) == ell+1 and None not in points)
    theta = [sum(values[j] for j in range(ell+1) if j % p == a) % p for a in range(p)]
    found = moments(theta, p)
    check(f"D_{D}_actual_low_moments", found == expected)
    sign = 1 if O.q == 13 else -1
    shifts = [a for a in range(p) if all((theta[j]-sign*theta[(a-j) % p]) % p == 0 for j in range(p))]
    check(f"D_{D}_whole_theta_functional_equation", len(shifts) == 1)
    return {"D": D, "ell": ell, "p": p, "q": O.q, "r": r, "origin": origin,
            "local_embedding_parameters": O.embedding(ell)[1], "torus_generator_a_plus_r": gen,
            "full_CM_points": points, "full_CM_values": values,
            "full_CM_order_embeddings": embeddings, "norm_ell_representatives": elts,
            "theta_Cp_coefficients": theta, "moments": found,
            "functional_equation_reflection_shift": shifts[0]}


def pclass_source(O, data, representative, index):
    D, ell, p, r, origin = -1307, 43, 11, (1, 13, 0, -1), 135
    c = (1-D)//4
    forms = reduced_forms(D)
    check("D_minus1307_class_number_11", len(forms) == 11)
    check("D_minus1307_norm3_class_relation", 420**2+420+c == 3**11)
    check("D_minus1307_maximal_CM_embedding", O.norm(r) == c and O.trace(r) == 1)
    check("D_minus1307_original_389_orientation", action(O.matrix(r, N), origin, N) == origin)

    def finite_mul(v, w):
        a, b = v
        d, e = w
        return ((a*d-c*b*e) % ell, (a*e+b*d+b*e) % ell)
    n, a, ans = (ell*ell-1)//p, (420 % ell, 1), (1, 0)
    while n:
        if n & 1:
            ans = finite_mul(ans, a)
        a = finite_mul(a, a)
        n //= 2
    check("D_minus1307_full_p_class_extension_splits", ans == (1, 0))
    labels, gen = torus_labels(O, r, ell)
    initial = [None]*(ell+1)
    for a in O.norm_elements(ell):
        j = labels[kernel(O.matrix(a, ell), ell)]
        initial[j] = (O.mul(O.mul(a, r), O.conj(a)), action(O.matrix(a, N), origin, N))
    check("D_minus1307_initial_44_CM_embeddings_distinct", len(set(initial)) == 44)
    by_kernel = {kernel(O.matrix(a, 3), 3): a for a in O.norm_elements(3)}
    states = initial[:]
    allstates, points, values = [], [], []
    coeff = [[0]*p for _ in range(p)]
    for i in range(p):
        allstates += states
        points.append([x for s, x in states])
        values.append([data["phi"][index[representative[x]]] for s, x in states])
        for j in range(ell+1):
            coeff[i][j % p] = (coeff[i][j % p]+values[-1][j]) % p
        nextstates = []
        for s, x in states:
            a = by_kernel[kernel(O.matrix(s, 3), 3)]
            ss = O.mul(O.mul(a, s), O.conj(a))
            assert all(x % 3 == 0 for x in ss)
            ss = tuple(x//3 for x in ss)
            assert O.norm(ss) == ell*ell*c and O.trace(ss) == ell
            nextstates.append((ss, action(O.matrix(a, N), x, N)))
        states = nextstates
    check("D_minus1307_all_484_actual_CM_embeddings_distinct", len(set(allstates)) == 484)
    initial_index = {state: i for i, state in enumerate(initial)}
    shifts = {(initial_index[state]-j) % (ell+1) for j, state in enumerate(states)}
    check("D_minus1307_actual_class_generator_return_shift", shifts == {11})
    constant = sum(map(sum, coeff)) % p
    linear = [sum(coeff[i][j]*(j if k == 0 else i) for i, j in product(range(p), repeat=2)) % p
              for k in range(2)]
    quadratic = [[sum(coeff[i][j]*(j if k == 0 else i)*(j if l == 0 else i)
                      for i, j in product(range(p), repeat=2)) % p
                  for l in range(2)] for k in range(2)]
    check("D_minus1307_actual_total_quadratic_jet", constant == 0 and linear == [0, 0]
          and quadratic == [[8, 8], [8, 0]])
    observations = []
    for b in range(p):
        theta = [0]*p
        for i, j in product(range(p), repeat=2):
            theta[(j+b*i) % p] = (theta[(j+b*i) % p]+coeff[i][j]) % p
        found = moments(theta, p)
        check(f"D_minus1307_actual_ramified_quotient_b_{b}", found == [0, 0, (4+8*b) % p])
        observations.append({"b": b, "theta": theta, "moments": found})
    check("D_minus1307_nonzero_total_quadratic_determinant", int(sp.Matrix(quadratic).det()) % p == 2)
    check("D_minus1307_whole_theta_reflection",
          all((coeff[i][j]-coeff[(5-i) % p][(1-j) % p]) % p == 0
              for i, j in product(range(p), repeat=2)))
    return {"D": D, "p": p, "q": 13, "ell": ell, "class_number": 11,
            "reduced_forms": forms, "r": r, "origin": origin,
            "local_embedding_parameters": O.embedding(ell)[1], "torus_generator_a_plus_r": gen,
            "full_CM_points": points, "full_CM_values": values,
            "full_CM_order_embeddings": [s for s, x in allstates],
            "norm3_class_generator_return_shift": 11,
            "raw_coefficients_class_then_local": coeff,
            "constant": constant, "linear_moments": linear,
            "quadratic_moment_matrix_local_then_class": quadratic,
            "all_ramified_quotients": observations}


O13, O7 = Order(13), Order(7)
order_data = [order_certificate(O13), order_certificate(O7)]
E13, reps13, index13 = eigenfunction(O13, 11)
E7, reps7, index7 = eigenfunction(O7, 13)
cases = [class_one_source(O13, E13, reps13, index13, -7, 131,
                          (0, 0, 0, 1), 0, [0, 0, 4]),
         class_one_source(O7, E7, reps7, index7, -11, 233,
                          (0, -1, 1, 0), 189, [0, 4, 8])]
class_case = pclass_source(O13, E13, reps13, index13)

for D, ell, p, q, sign in [(-7, 131, 11, 13, -1),
                           (-11, 233, 13, 7, 1),
                           (-1307, 43, 11, 13, -1)]:
    check(f"actual_local_conditions_{D}_{ell}",
          int(sp.kronecker_symbol(D, N)) == 1
          and int(sp.kronecker_symbol(D, ell)) == -1
          and int(sp.kronecker_symbol(D, q)) == -1
          and D % p and (ell+1) % p == 0 and (ell+1) % (p*p)
          and ap(ell) % p and ap(p) % p not in (0, 1, p-1)
          and (ap(q)-sign*(q+1)) % p == 0 and q*q % p != 1)
check("residual_image_11_irreducible_Frobenius_2", pow((ap(2)**2-8) % 11, 5, 11) == 10)
check("residual_image_13_irreducible_Frobenius_3", pow((ap(3)**2-12) % 13, 6, 13) == 12)

output = {"result": "R276", "all_passed": True, "check_count": len(checks), "checks": checks,
          "E389_aq": {str(q): ap(q) for q in (2, 3, 5, 7, 11, 13, 43, 131, 233)},
          "orders": order_data, "actual_eigenfunctions": [E13, E7],
          "class_number_one_sources": cases, "p_class_source": class_case}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(output, indent=2)+"\n")
print(f"PASS: {len(checks)} exact arithmetic checks; {path.name}")
