#!/usr/bin/env python3
"""Exact arithmetic ledger for a rational, uncalibrated R64 deep tail.

This proves only the displayed ideal spectrum and linear Green constants.
It is not a nonlinear tail implementation or a closed-surface certificate.
All comparisons used for the PASS flags use fractions and integer roots.
Decimal values in the JSON are convenience summaries of those intervals.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
import math
from pathlib import Path


def iroot(n: int, k: int) -> int:
    if n < 0 or k < 1:
        raise ValueError("positive integer root required")
    lo, hi = 0, 1 << ((n.bit_length() + k - 1) // k)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**k <= n:
            lo = mid
        else:
            hi = mid
    return hi if hi**k == n else lo


class I:
    """Closed rational interval; arithmetic is exact before display."""

    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = self.lo if hi is None else F(hi)
        assert self.lo <= self.hi

    @staticmethod
    def wrap(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, y):
        y = I.wrap(y)
        return I(self.lo + y.lo, self.hi + y.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, y):
        return self + -I.wrap(y)

    def __rsub__(self, y):
        return I.wrap(y) - self

    def __mul__(self, y):
        y = I.wrap(y)
        p = [self.lo * y.lo, self.lo * y.hi,
             self.hi * y.lo, self.hi * y.hi]
        return I(min(p), max(p))

    __rmul__ = __mul__

    def __truediv__(self, y):
        y = I.wrap(y)
        assert not y.lo <= 0 <= y.hi
        return self * I(1 / y.hi, 1 / y.lo)

    def __rtruediv__(self, y):
        return I.wrap(y) / self

    def absolute(self):
        return I(0 if self.lo <= 0 <= self.hi else
                 min(abs(self.lo), abs(self.hi)),
                 max(abs(self.lo), abs(self.hi)))

    def root(self, k=2, bits=96):
        assert self.lo >= 0
        den = 1 << bits

        def below(q):
            t = (q.numerator << (bits * k)) // q.denominator
            return F(iroot(t, k), den)

        return I(below(self.lo), below(self.hi) + F(1, den))

    def display(self):
        return [float(self.lo), float(self.hi)]


def norm1(a):
    cols = [sum(a[i][j].absolute().hi for i in range(2))
            for j in range(2)]
    return max(cols)


def nu(j):
    return F(j * j * (4 * j * j - 1), 3)


def ideal_block(j, d, sqrt2):
    v = nu(j)
    alpha = F(65, 64)
    # The raw eigenvalues are -L and -S, with L*S=d.
    trace_abs = 65 * v * (1 + d / 64) - (1 + d)
    disc = trace_abs * trace_abs - 4 * d
    L = (trace_abs + disc.root()) / 2
    S = d / L
    if j == 1:
        # Exact identities avoid intervals crossing the central eigenvalue.
        L, S = I(64), d / 64
    exponent = 11 + j
    scale = I(F(1, 2 ** (exponent // 2)))
    if exponent % 2:
        scale = scale / sqrt2
    T = [[I(1 - 65 * v), I(alpha)],
         [d * (65 * v * (v - 1)), d * (1 - alpha * v)]]
    P = [[(T[i][k] + (S if i == k else 0)) / (-L + S)
          for k in range(2)] for i in range(2)]
    Ps = [[I(int(i == k)) - P[i][k] for k in range(2)]
          for i in range(2)]
    A = [[scale * T[i][k] for k in range(2)] for i in range(2)]
    return dict(j=j, nu=v, large=scale * L, small=scale * S,
                scale=scale, determinant=d * scale * scale,
                projection_large=norm1(P), projection_small=norm1(Ps),
                norm=norm1(A))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    d = I(F(1, 2048)).root(4)
    sqrt2 = I(2).root()
    stored_delta0 = F(3458764513820541, 576460752303423488)
    stored_c0 = F(3602879701896397, 72057594037927936)
    stored_source_pass = (F(3, 500) <= stored_delta0 < F(1, 128)
                          and F(9, 25) <= stored_c0**2 / stored_delta0 <= F(4, 9)
                          and stored_c0 <= F(1, 16))
    assert d.lo > F(1486, 10000) and d.hi < F(3, 20)
    assert sqrt2.lo > F(7, 5)

    # The simple ideal eigenvalue bounds reduce all modal comparisons to
    # integers: nu_j^2 / 2^(j-1), with an optional (65/64)^4 factor.
    unstable_pass = all(nu(j)**2 > 2**(j - 1) for j in range(2, 47))
    stable_boundary_pass = F(65, 64)**4 * nu(47)**2 < 2**46
    # nu(j+1)/nu(j) < sqrt(2), hence the squared sequence decreases for j>=12.
    ratio_start_pass = 2 * nu(12)**2 > nu(13)**2
    # Its ratio is a product of decreasing positive factors for j>=2:
    # ((j+1)/j)^2 * (2j+1)/(2j-1) * (2j+3)/(2j+1).

    rows = []
    green = F(4)  # All grouped high stable blocks have norm <=1/4.
    for j in range(1, 110):
        z = ideal_block(j, d, sqrt2)
        r, s = z["large"], z["small"]
        if j == 1:
            assert r.lo == r.hi == 1
            # 2^(-3/8)<4/5, proved by eighth powers of positive rationals.
            assert F(1, 8) < F(4, 5)**8
            term = 5 * z["projection_large"] + z["projection_small"] / (1 - s.hi)
            kind = "center plus stable"
        elif j <= 46:
            assert r.lo > 1 and s.hi < 1
            term = (z["projection_large"] / (r.lo - 1)
                    + z["projection_small"] / (1 - s.hi))
            kind = "unstable plus stable"
        else:
            assert r.hi < 1 and s.hi < 1
            # Sum powers of the entire 2x2 block by Cayley-Hamilton.
            # This retains cancellation between its almost parallel projectors.
            term = 1 + (z["norm"] + z["determinant"].hi) / ((1 - r.hi) * (1 - s.hi))
            kind = "grouped stable block"
        green += term
        rows.append(dict(j=j, nu=int(z["nu"]), type=kind,
                         large_abs_interval=r.display(), small_abs_interval=s.display(),
                         matrix_norm_upper=float(z["norm"]),
                         green_contribution_upper=float(term)))

    # Every ideal block j>=110 is contractive in the original matrix 1-norm.
    j = 110
    high_ideal_majorant = (F(260, 3) * j**4 + F(52, 3) * j**8) * F(5, 7 * 2**60)
    high_ideal_pass = high_ideal_majorant < F(1, 4)
    # The majorant j^8 2^(-j/2) decreases for j>=110 because log 2>2/3.
    assert F(8, 110) < F(1, 3)

    # From the explicit nine-factor product estimate in the accompanying note:
    # D_(2j) <= 2^20 j^12 and C_E <=2^61.
    # max_{x>0} x^12 2^(-x/2)=(24/(e log 2))^12 <(27/2)^12<2^46.
    polynomial_max_pass = F(27, 2)**12 < 2**46
    coefficient_pass = F(3 * 390 * 290 * 64, 27) < 2**20
    green_pass = green < 2**27

    # A safe full-frequency splitting index is J0=16384.  With beta<=h/4
    # the actual block bound is <2^46 * 2^-5 * (1+2J0)^308 *2^(-3J0/8).
    # Since 1+2J0<2^16 the following upper exponent is integer and exact.
    J0 = 16384
    actual_constant_majorant = 7 * (3**6 * 68**3 + 8 * 64**3 * 23**4 * 8)
    actual_constant_pass = actual_constant_majorant < 2**46
    high_actual_exponent = 46 - 5 + 16 * 308 - 3 * J0 // 8
    high_actual_pass = (high_actual_exponent <= -2
                        and F(616, 1 + 2 * J0) < F(1, 4))

    depths = []
    for N in [128, 160, 176, 192, 224, 256]:
        # sqrt(delta_N)<2^(-3-N/2), C_G<2^27, C_E<2^61.
        exponent = 85 - N // 2
        eta = F(2**exponent) if exponent >= 0 else F(1, 2**(-exponent))
        depths.append(dict(N=N, green_perturbation_upper=float(eta),
                           exact_upper=f"2^{exponent}", linear_gate=eta <= F(1, 4),
                           low_height_chart_gate=eta <= F(1, 2**27)))

    report = dict(
        status="proved exact-arithmetic linear ledger; nonlinear gates remain separate",
        model=dict(R=64, alpha="65/64", a="11/4", reference_delta0="3/500",
                   stored_delta0=str(stored_delta0), stored_eta_ratio=str(stored_c0),
                   eta_over_delta="fixed c0 * 2^(-n/2)", angular_loss="log(2)/4",
                   amplitude_exponent="11/2", forcing_exponent="3/8"),
        parameters=dict(free_modes=list(range(2, 93, 2)), free_dimension=46,
                        actual_high_block_index=J0, ideal_grouped_high_index=110),
        constants=dict(d_interval=d.display(), green_sum_upper=float(green),
                       green_bound="2^27", finite_block_drift_bound="2^61",
                       ideal_high_majorant_at110=float(high_ideal_majorant),
                       actual_high_upper_exponent=high_actual_exponent),
        exact_checks=dict(stored_source_parameters=stored_source_pass,
                          unstable_modes_2_to46=unstable_pass,
                          stable_from47=stable_boundary_pass and ratio_start_pass,
                          grouped_ideal_high=high_ideal_pass,
                          polynomial_drift_coefficient=coefficient_pass,
                          exponential_polynomial_maximum=polynomial_max_pass,
                          green_constant=green_pass,
                          actual_transfer_constant=actual_constant_pass,
                          actual_high_blocks=high_actual_pass),
        depths=depths, blocks=rows,
        limits=["This does not evaluate the nonlinear constants c_* and C_*.",
                "N=192 is a sufficient linear depth only; it is not a certified nonlinear starting depth.",
                "The 46-dimensional low-height chart includes forced higher Fourier traces.",
                "The old stored metric and the rational deep extension are different metrics.",
                "No amplitude, complete closed surface, or reach claim is made."])
    assert all(report["exact_checks"].values())
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(dict(output=str(args.out), exact_checks=report["exact_checks"],
                          constants=report["constants"], free_dimension=46)))


if __name__ == "__main__":
    main()
