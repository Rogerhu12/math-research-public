#!/usr/bin/env python3
"""Exact coefficient and all-depth carry algebra for R463.

The analytic translation/distribution, divisor and norm assertions are
proved in the accompanying result.  This certificate checks the original
frame coefficient and generic algebra, with no scan of ordinary primes.
"""
import argparse
from fractions import Fraction as Q
import json
from pathlib import Path
import sympy as sp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    directory = Path(__file__).resolve().parent
    old = json.loads(
        (directory / "check-r455-pure-companion-arithmetic-test.json").read_text()
    )
    A = list(map(Q, old["sigma_A_coefficients"]))
    B = list(map(Q, old["x_B_coefficients"]))
    theta_z6 = B[1] + 2*A[1]
    assert theta_z6 == -Q(2, 15)
    q_z5_at_b1 = 17*6*theta_z6
    assert q_z5_at_b1 == -Q(68, 5)

    a, p, b, conn = sp.symbols("a p b connection_a", nonzero=True)
    lam = -1/a
    kap = p/a**2
    pi = p/a
    q5 = sp.Rational(q_z5_at_b1.numerator, q_z5_at_b1.denominator)*b
    R5 = sp.factor(q5*(a**6-p)/17)
    assert sp.expand(R5 + sp.Rational(4, 5)*b*(a**6-p)) == 0

    Cp, G, R = sp.symbols("Cprime G RC")
    QC = Cp-G
    dilation = pi*QC+17/a*R
    raw_carry = -lam*kap*Cp-lam*G-lam**2*dilation
    reduced_carry = -lam*(1+kap)*G+17*lam**3*R
    assert sp.factor(raw_carry-reduced_carry) == 0
    assert sp.factor(reduced_carry.subs({G:-conn, R:0})
                     - conn*lam*(1+kap)) == 0

    # N=p^n, A=bar(pi)^n, epsilon=(-1)^n.  The displayed generic
    # equality proves the algebra for every n, without a finite n check.
    An, N, eps = sp.symbols("A_n N epsilon", nonzero=True)
    raw_n = N/An**3*Cp-eps/An*G - (
        N/An*QC+17/An*R
    )/An**2
    reduced_n = (N/An**3-eps/An)*G-17/An**3*R
    assert sp.factor(raw_n-reduced_n) == 0

    companion = json.loads(
        (directory / "check-r460-original-odd-companion-carries.json").read_text()
    )
    for name, target in companion["whole_companion_targets"].items():
        target = list(map(sp.Rational, target))
        assert target[0] == 0 and target[1] != 0 and target[5] != 0

    result = {
        "normalization": {
            "a": "bar(pi0), p=a*pi0, lambda=-1/a, kappa=p/a^2",
            "frame": "F0=Theta^17, Theta=sigma(delta z)/(delta sigma(z))",
            "connection": "q=F0'/F0",
            "unit": "u_a=r_a(delta z)/r_a(z)=delta^(1-N(a))*Theta(a z)/Theta(z)^N(a)",
            "log_derivative": "R_a=u_a'/u_a",
        },
        "Theta_z6_at_b1": str(theta_z6),
        "q_z5": str(q5),
        "R_a_z5": str(R5),
        "R_a_times_C_z6": str(sp.factor(-conn*R5)),
        "R_a_times_pullback_C_z6": str(sp.factor(-conn*a*R5)),
        "one_layer_carry": str(sp.factor(reduced_carry)),
        "generic_depth_carry": str(reduced_n),
        "divisor": "[a]^*(T_plus+T_minus)-N(a)*(T_plus+T_minus)",
        "norm": "Norm_[a](u_a)=1 when (a,delta)=1",
        "origin_value": "u_a(O)=delta^(1-N(a))",
        "ordinary_origin_log": "-(p-1)/2 * log_p(3)",
        "nonfixed_poles_of_R_a": "2*(p-1), each residue +1",
        "fixed_residue_at_T_plus_and_T_minus": "1-p",
        "minimum_remaining_poles_after_multiplying_C": "2*p-29",
        "status": "original frame coefficient and complete symbolic carry identities verified",
    }
    encoded = json.dumps(result, ensure_ascii=False, indent=2)+"\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
        print(json.dumps({"status":result["status"],"output":str(args.output)}))
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()

