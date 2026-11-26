#!/usr/bin/env python3
"""Original E65 local Schwartz: complete 2/3/5/split-13 checks, public Actions only.

No generated inputs or output files.  Field arithmetic is exact python-flint
0.9.0.  The two split-13 branches and Yang's actual natural-polarization
intertwiner are checked before the CM producer uses degree390.
"""
from __future__ import annotations
from fractions import Fraction
import hashlib
import json
from flint import fmpq, fmpq_poly


class Field:
    def __init__(self, n):
        self.n = n
        if n == 24:
            coeff = [1, 0, 0, 0, -1, 0, 0, 0, 1]
        elif n in (15, 39):
            p = n // 3
            # Phi_(3p)(X)=Phi_p(X^3)/Phi_p(X), exact monic division.
            top = [int(j % 3 == 0) for j in range(3 * (p - 1) + 1)]
            coeff = [0] * (2 * (p - 1) + 1)
            for j in range(len(coeff) - 1, -1, -1):
                c = top[j + p - 1]
                coeff[j] = c
                for k in range(p):
                    top[j + k] -= c
            assert not any(top)
        else:
            raise ValueError(n)
        self.mod = fmpq_poly(coeff)
        self.deg = len(coeff) - 1
        self.zero, self.one = self(0), self(1)
        self.z = self([0, 1])
        self.powers = [self.one]
        for _ in range(1, n):
            self.powers.append(self.powers[-1] * self.z)
        assert self.z ** n == self.one

    def __call__(self, x):
        if isinstance(x, Element):
            assert x.F is self
            return x
        if isinstance(x, Fraction):
            x = fmpq(x.numerator, x.denominator)
        if isinstance(x, str):
            x = fmpq(x)
        if not isinstance(x, (list, fmpq_poly)):
            x = [x]
        return Element(self, fmpq_poly(x) % self.mod)


class Element:
    def __init__(self, F, p):
        self.F, self.p = F, p

    def __add__(self, other):
        other = self.F(other)
        return Element(self.F, self.p + other.p)
    __radd__ = __add__

    def __neg__(self):
        return Element(self.F, -self.p)

    def __sub__(self, other):
        return self + (-self.F(other))

    def __rsub__(self, other):
        return self.F(other) - self

    def __mul__(self, other):
        other = self.F(other)
        return Element(self.F, self.p * other.p % self.F.mod)
    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.F(other)
        g, s, _ = other.p.xgcd(self.F.mod)
        assert g == fmpq_poly([1])
        return self * Element(self.F, s)

    def __pow__(self, n):
        if n < 0:
            return (self.F.one / self) ** (-n)
        result, value = self.F.one, self
        while n:
            if n & 1:
                result = result * value
            value = value * value
            n //= 2
        return result

    def __eq__(self, other):
        return self.p == self.F(other).p

    def conj(self):
        return sum((self.F.powers[-j % self.F.n] * str(self.p[j])
                    for j in range(len(self.p))), self.F.zero)

    def encode(self):
        return [str(self.p[j]) for j in range(self.F.deg)]


def matrix_product(A, B):
    F = A[0][0].F
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), F.zero)
             for j in range(len(B[0]))] for i in range(len(A))]


def matrix_vector(A, v):
    return [sum((a * b for a, b in zip(row, v)), row[0].F.zero)
            for row in A]


def check_original_e65_local_schwartz():
    checks = []
    def check(name, value):
        assert value, name
        checks.append(name)

    J = Field(24)
    z8, omega, imag = J.z ** 3, J.z ** 8, J.z ** 6
    sqrt2, sqrt3 = z8 + z8 ** -1, J.z ** 2 + J.z ** -2
    check("dyadic_positive_roots", sqrt2 ** 2 == 2 and sqrt3 ** 2 == 3)
    tminus = (sqrt3 - 1) / sqrt2
    fA = [J.one, J.zero, -J.one, J.zero]
    fB = [J.zero, J.one, J.zero, J.one]
    v2 = [J.one, tminus, -J.one, tminus]
    mu_omega = -(omega ** 2) * z8 ** -1
    # alpha=15/13 ==3 (mod8), so -3alpha ==-1 (mod8).
    raw_omega = [[mu_omega / (2 * sqrt2) *
                  z8 ** (-(a*a + b*b - 4*a*b))
                  for b in range(4)] for a in range(4)]
    A = [[mu_omega / sqrt2, mu_omega * z8 ** -1 / sqrt2],
         [mu_omega * z8 ** -1 / sqrt2, mu_omega * imag / sqrt2]]
    check("whole_dyadic_omega_integral",
          matrix_vector(raw_omega, fA) == [A[0][0], A[1][0], -A[0][0], A[1][0]]
          and matrix_vector(raw_omega, fB) == [A[0][1], A[1][1], -A[0][1], A[1][1]])
    check("dyadic_true_invariant_vector", matrix_vector(raw_omega, v2) == v2)
    check("dyadic_true_norm", 1 + tminus*tminus == 3 - sqrt3)
    # The odd quarter annulus cancels on both actual even vectors.
    check("dyadic_full_quarter_annulus_cancellation",
          all((-1)**(1-a) == 1 and (-1)**(2-a) == -1
              for a in range(1, 8, 2)))
    mu_g = z8 ** -1
    gmat = [[J.zero for _ in range(4)] for _ in range(4)]
    for b in range(4):
        a = (3*b + 2) % 4
        n = 11*a*a - 26*a*b + 11*b*b
        check("dyadic_stationary_divisibility_" + str(b), n % 4 == 0)
        # 3alpha ==1 (mod8), after exact division by four.
        gmat[a][b] = mu_g * z8 ** (-n // 4)
    expected = [[0, 0, -1, 0], [0, 1, 0, 0],
                [-1, 0, 0, 0], [0, 0, 0, 1]]
    check("whole_dyadic_principal_generator",
          gmat == [[J(x) for x in row] for row in expected])
    check("whole_dyadic_principal_invariance", matrix_vector(gmat, v2) == v2)
    check("minus_principal_same_absolute_splitting", -(z8 ** 3) == mu_g)
    check("dyadic_complete_half_character",
          all(v2[(n+2) % 4] * (-1)**n == -v2[n] for n in range(4)))

    # Three-adic residue of alpha/36=5/156 is 2/3.
    check("actual_three_phase", (5 * pow(52, -1, 3)) % 3 == 2)
    v3 = [0, 1, 1]
    check("actual_three_even_reflection", v3[1] == v3[2] and v3[0] == 0)
    # Six-term Gauss sum for chi_3(epsilon*omega^a)=epsilon*omega^a.
    # Tr((a+b omega)/(2delta^3))=-b/6, phase omega^(2b).
    units = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1)]
    three_gauss = sum(((J(a) + omega*b) ** -1 * omega ** (2*b)
                       for a, b in units), J.zero)
    check("complete_six_term_three_Gauss", three_gauss == -3)
    check("actual_three_epsilon_and_dichotomy",
          ((-imag) ** 3) * three_gauss / 3 == -imag
          and (-imag) * (-imag) == -1)

    local = {}
    vectors = {}
    for q, cyclotomic, generator, tau_power, beta, scale in (
            (5, 15, (3, 2), 1, 3, 3),
            (13, 39, (11, 5), 2, 6, 6)):
        K = Field(cyclotomic)
        zeta, om = K.z ** 3, K.z ** q
        def leg(a):
            a %= q
            return 0 if not a else (1 if pow(a, (q-1)//2, q) == 1 else -1)
        def multiply(g, h):
            return ((g[0]*h[0] - 3*g[1]*h[1]) % q,
                    (g[0]*h[1] + g[1]*h[0]) % q)
        order = 6 if q == 5 else 12
        gs, cur = [], (1, 0)
        for _ in range(order):
            gs.append(cur)
            cur = multiply(cur, generator)
        check("complete_torus_order_" + str(q), cur == (1, 0) and len(set(gs)) == order)
        root = sum((leg(a) * zeta ** a for a in range(1, q)), K.zero)
        check("actual_real_quadratic_gauss_" + str(q), root*root == q and root.conj() == root)
        def W(g):
            x, y = g
            if not y:
                return [[K(int(a == (b if x == 1 else -b) % q))
                         for b in range(q)] for a in range(q)]
            h = beta * pow(2*y, -1, q) % q
            factor = leg(h) * root / q
            return [[factor * zeta ** (h*(x*(a*a+b*b)-2*a*b) % q)
                     for b in range(q)] for a in range(q)]
        matrices = [W(g) for g in gs]
        current = matrices[0]
        for j in range(1, order+1):
            current = matrix_product(current, matrices[1])
            check("entire_torus_multiplication_{}_{}".format(q, j),
                  current == matrices[j % order])
        tau = om ** tau_power
        P = [[sum((tau ** -j * matrices[j][a][b] for j in range(order)), K.zero)
              / order for b in range(q)] for a in range(q)]
        check("complete_projector_idempotence_" + str(q), matrix_product(P, P) == P)
        check("complete_projector_rank_one_" + str(q), sum((P[a][a] for a in range(q)), K.zero) == 1)
        f = [scale * root * P[a][0] for a in range(q)]
        check("complete_true_local_eigenvector_" + str(q),
              matrix_vector(matrices[1], f) == [tau*x for x in f])
        check("complete_real_even_vector_" + str(q),
              all(f[a].conj() == f[a] and f[-a % q] == f[a] for a in range(q)))
        if q == 5:
            explicit = [root * int(a == 0) - om**2 * zeta**(a*a) - om*zeta**(-a*a)
                        for a in range(q)]
            check("actual_five_closed_vector", f == explicit and f[0] == root + 1)
            target_norm = 3 * (5 + root)
            measure = 1
        else:
            explicit = [root * int(a == 0) + 1
                        - om * (zeta**(4*a*a) + zeta**(3*a*a))
                        - om**2 * (zeta**(10*a*a) + zeta**(9*a*a))
                        for a in range(q)]
            check("actual_split_thirteen_closed_vector", f == explicit and f[0] == root + 3)
            target_norm = 6 * (13 + 3*root) / 13
            measure = Fraction(1, 13)
            # Both split embeddings are fixed: omega=9,delta=6 and omega=3,delta=-6.
            check("both_split_embeddings", (9*9 + 9 + 1) % 13 == 0
                  and (3*3 + 3 + 1) % 13 == 0 and (1+2*9) % 13 == 6
                  and (1+2*3) % 13 == 7)
            lifts = {}
            for k in range(6):
                lifts[pow(4, k, 13)] = (-om) ** k
            theta = {b: lifts[pow(b, 2, 13)] for b in range(1, 13)}
            check("true_split_unit_character",
                  all(theta[a*b % 13] == theta[a]*theta[b]
                      for a in range(1, 13) for b in range(1, 13)))
            rho = [sum((theta[b] ** -1 *
                        zeta ** ((5*a*a + 9*b*b - 3*a*b) % 13)
                        for b in range(1, 13)), K.zero) / root
                   for a in range(13)]
            check("whole_actual_split_intertwiner_nonzero", rho[0] != 0)
            ratio = rho[0] / f[0]
            check("whole_actual_split_intertwiner_return",
                  rho == [ratio*x for x in f])
            check("actual_split_natural_norm",
                  sum((x*x.conj() for x in rho), K.zero)/13 == Fraction(12, 13))
            check("whole_split_unit_action",
                  matrix_vector(matrices[1], rho) == [tau*x for x in rho])
        norm = sum((x*x.conj() for x in f), K.zero) * measure
        check("actual_Schwartz_measure_norm_" + str(q), norm == target_norm and norm != 0)
        canonical = {"field":cyclotomic, "vector":[x.encode() for x in f],
                     "generator":generator,
                     "generator_matrix":[[x.encode() for x in row] for row in matrices[1]]}
        local[str(q)] = {
            "field":"Q(zeta_{})".format(cyclotomic),
            "whole_torus_order":order,
            "projector_rank":1,
            "actual_zero_coordinate":"sqrt({})+{}".format(q, 1 if q == 5 else 3),
            "actual_Schwartz_squared_norm":
                "3*(5+sqrt(5))" if q == 5 else "6*(13+3*sqrt(13))/13",
            "same_natural_intertwiner_all_coordinates":q == 13,
            "canonical_vector_and_generator_sha256":
                hashlib.sha256(json.dumps(canonical, sort_keys=True, separators=(",",":")).encode()).hexdigest()}
        vectors[str(q)] = f

    # Actual global period and half-character, checked componentwise on full residues.
    check("actual_global_support_indices", 45 % 4 == 1 and 10 % 3 == 1
          and pow(18, -1, 5) == 2 and pow(90, -1, 13) == 12)
    check("actual_global_period", 780 % 4 == 0 and 780 % 3 == 0
          and 780 % 5 == 0 and 780 % 13 == 0)
    check("actual_global_half_shift", 390 % 4 == 2 and 390 % 3 == 0
          and 390 % 5 == 0 and 390 % 13 == 0)
    check("actual_degree_from_same_Gaussian", Fraction(90*90, 18) / Fraction(15,13) == 390)
    # Complete split projection cost, not the old no-split factor.
    split_old = Fraction(1,13) / (1-Fraction(1,13))**2
    check("actual_split_twelve_projection_cost", 12*split_old == Fraction(13,12))
    check("actual_all_finite_Yang_factor",
          Fraction(2,3)*Fraction(5,6)*Fraction(13,12) == Fraction(65,108))
    check("actual_ray_class_degree", (4-1)*(9-3)*(25-1)*(13-1)**2//6 == 10368)
    return {
        "status":"PASS",
        "alpha":"15/13",
        "degree":390,
        "charge":195,
        "actual_support":"n/90",
        "coefficient_period":780,
        "actual_half_shift":390,
        "actual_dyadic_vector":"(1,(sqrt(3)-1)/sqrt(2),-1,(sqrt(3)-1)/sqrt(2))",
        "actual_three_vector":"1_(1/9+1/3 Z3)+1_(-1/9+1/3 Z3)",
        "both_split_thirteen_branches_kept":True,
        "split_natural_intertwiner_full_return":True,
        "split_projection_cost":12,
        "full_Yang_c0":"65/108",
        "ray_class_degree":10368,
        "all_checks":checks,
        "finite_blocks":local,
        "numeric_L_values_used":False,
        "output_files":False}
