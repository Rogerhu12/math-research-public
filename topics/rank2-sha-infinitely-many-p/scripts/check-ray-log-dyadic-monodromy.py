#!/usr/bin/env python3
"""R258: exact sparse theta-group phases and logarithmic residue transport.

This checks fixed characteristic-zero identities. It does not scan target p.
The analytic/logarithmic argument and the actual theta frames are in R258.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as s


# Sparse Q[Z/16 x Z/16, xi]/(xi^16+1), in the basis Z^b X^a.
# ZX=xi^2 XZ; no dense matrix is constructed.
def mono(a, b, e=0, q=Q(1)):
    e %= 32
    if e >= 16:
        e -= 16
        q = -q
    return {(a % 16, b % 16, e): q} if q else {}


def add(*ds):
    out = {}
    for d in ds:
        for k, v in d.items():
            out[k] = out.get(k, Q(0)) + v
            if not out[k]:
                del out[k]
    return out


def mul(A, B):
    out = {}
    for (a, b, e), q in A.items():
        for (c, d, f), r in B.items():
            out = add(out, mono(a + c, b + d, e + f - 2 * a * d, q * r))
    return out


def scale(A, q):
    return {k: q * v for k, v in A.items() if q * v}


def adj(A):
    out = {}
    for (a, b, e), q in A.items():
        out = add(out, mono(-a, -b, -e - 2 * a * b, q))
    return out


def T(a, b):
    return mono(a, b, -a * b)


def main():
    I = s.I
    beta, betab = 4 - I, 4 + I
    r = s.cancel(beta / betab)
    P, Qp = beta / 16, -I * beta / 16  # Omega=1 in exact phase calculations.
    Tp, Tm, T0 = s.Rational(1, 2), I / 2, (1 + I) / 2
    wp, wm = I, 4 * I
    D = s.expand(beta * (Tm - Tp))
    assert s.simplify(betab * Tp - 8 * P - wp) == 0
    assert s.simplify(betab * Tm - 8 * Qp - wm) == 0
    assert s.simplify(D - T0 - (-2 + 2 * I)) == 0
    assert s.simplify(r * (8 * (Qp - P) + wm - wp) - D) == 0

    Id = mono(0, 0)
    Pi0 = add(*(mono(4 * a, 4 * b, 0, Q(1, 16))
                for a in range(4) for b in range(4)))
    half = scale(add(Id, scale(mono(8, 0), Q(-1)),
                     scale(mono(0, 8), Q(-1)), mono(8, 8)), Q(1, 4))
    four = add(*(T(e, h) for e in (-1, 1) for h in (-1, 1)))
    assert adj(four) == four
    assert mul(half, half) == half
    assert mul(Pi0, Pi0) == Pi0
    full = mul(Pi0, four)
    reduced = add(*(mul(mono(4 * a, 4 * b, 0, Q(1, 4)), T(e, h))
                    for e in (-1, 1) for h in (-1, 1)
                    for a in range(2) for b in range(2)))
    assert not mul(add(full, scale(reduced, Q(-1))), half)

    sparse = []
    explicit = {}
    for e in (-1, 1):
        for h in (-1, 1):
            for a in range(2):
                for b in range(2):
                    exponent = 16 * a * b + 4 * (b * e - a * h)
                    explicit = add(explicit, mul(mono(0, 0, exponent, Q(1, 4)),
                                                 T(e + 4 * a, h + 4 * b)))
                    sparse.append({
                        "epsilon": e, "eta": h, "a": a, "b": b,
                        "translation_P": e + 4 * a,
                        "translation_Q": h + 4 * b,
                        "coefficient_after_common_2_power":
                            "xi^%d/4" % (exponent % 32)})
    assert explicit == reduced

    # At the selected output point z_a + s + 4P + 4Q, the two actual
    # input divisors occur at (4,0), (0,4), modulo the kernel E[2].
    support_checks = []
    phase_rows = []
    for e in (-1, 1):
        for h in (-1, 1):
            contributors = []
            for ee in (-1, 1):
                for hh in (-1, 1):
                    for a in range(2):
                        for b in range(2):
                            x = (e + 4 - (ee + 4 * a)) % 8
                            y = (h + 4 - (hh + 4 * b)) % 8
                            if (x, y) in ((4, 0), (0, 4)):
                                contributors.append([ee, hh, a, b, x, y])
            assert contributors == [[e, h, 0, 1, 4, 0], [e, h, 1, 0, 0, 4]]
            support_checks.append({"epsilon": e, "eta": h,
                                   "contributors": contributors})

            ss = e * P + h * Qp
            tp, tm = ss + 4 * Qp, ss + 4 * P
            # The coefficient of z in the full Gaussian ratio is zero.
            linear = (4 * s.conjugate(tm - tp)
                      - 2 * s.conjugate(wm - wp)
                      + 2 * s.conjugate(D) * r)
            assert s.simplify(linear) == 0
            const = (-2 * (tm * s.conjugate(tm) - tp * s.conjugate(tp))
                     + 2 * (s.conjugate(wm) * tm - s.conjugate(wp) * tp)
                     - (wm * s.conjugate(wm) - wp * s.conjugate(wp)) / 2
                     + s.conjugate(D) * r * (-2 * tp + wp)
                     + D * s.conjugate(D) / 2)
            const = s.simplify(s.expand_complex(const))
            assert const == I * (-17 * e - 17 * h - 268) / 16
            # chi(wm)/chi(wp)=-1 and T_{-D}F=-i F x^-17 give i exp(68*pi*C).
            exponent = s.simplify(8 + 16 * 68 * const / I)
            assert exponent.is_Integer
            exponent = int(exponent) % 32
            expected = (24 - 4 * (e + h)) % 32
            assert exponent == expected
            # Include the two canonical-translation coefficients.
            combined = (exponent - 4 * (e + h)) % 32
            assert combined == (8 if e * h == 1 else 24)
            leading = 1 + I * e * h
            assert s.expand(leading * s.conjugate(leading)) == 2
            phase_rows.append({
                "epsilon": e, "eta": h,
                "Gaussian_constant_C": str(const),
                "ratio_gminus_gplus":
                    "xi^%d * x(v_plus)^(-17)" % exponent,
                "combined_variable_factor": "1 - (%s)*x(v_plus)^(-17)" %
                    str(I * e * h),
                "factor_at_x_minus_one": str(leading),
                "factor_norm": 2,
                "exact_log_zero_order": 17,
                "bare_second_covariant_derivative_log_zero_order": 15})

    # Exact DFT identity over Q(zeta_16): coefficients of xi^e.
    def root_sum(exponents):
        coeff = [0] * 16
        for exponent in exponents:
            exponent %= 32
            if exponent >= 16:
                coeff[exponent - 16] -= 1
            else:
                coeff[exponent] += 1
        return coeff
    for j in range(16):
        for k in range(16):
            v = root_sum([2 * (k - j) * a for a in range(16)])
            assert v == ([16] + [0] * 15 if j == k else [0] * 16)
    assert len({pow(3, a, 17) for a in range(16)}) == 16

    out = {
        "status": "PASS",
        "cyclotomic_convention": "xi=exp(pi*i/16), ZX=xi^2*XZ",
        "sparse_only_no_dense_matrix": True,
        "R_is_self_adjoint": True,
        "V_canonical_common_factor": "2^(-3/8)",
        "full_V_after_common_factor": "Pi0 * sum_{epsilon,eta=+-1} T_(epsilon P+eta Q)",
        "half_projector": "(1-X^8)(1-Z^8)/4",
        "sixteen_term_reduction_checked_on_half_minus_minus": True,
        "sixteen_actual_translations": sparse,
        "selected_support_checks": support_checks,
        "trace_period_plus_over_Omega": "I",
        "trace_period_minus_over_Omega": "4*I",
        "difference_of_F_arguments_over_Omega": str(D),
        "full_Gaussian_ratio_checks": phase_rows,
        "log_residue_common_factor":
            "2^(-11/8) * chi(a)^(-1) * xi^(4*epsilon) * g_plus(z)",
        "log_residue_variable_factor": "1-i*epsilon*eta*x(v_plus(z))^(-17)",
        "DFT_times_conjugate_transpose": "16*I_16",
        "ray_character_monodromy_rank_after_V": 16,
        "after_Qplus0": "same rank, by the actual eight-term identity Q0plus Qplus0=Pi0",
        "scope": "logarithmic residues; no commutation with Mellin and no central nonvanishing claimed",
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
