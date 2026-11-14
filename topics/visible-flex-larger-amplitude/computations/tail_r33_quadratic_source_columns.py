#!/usr/bin/env python3
"""Positive frequency columns for the complete Darboux quadratic main part.

This module keeps input/output modes, the two physical components, and
the separate radial materials d1=V^2/(r*w), dl=abs(lambda)*V^2/w.
The centre caps are COMPLEX Fourier coefficients, not cosine amplitudes.
Their exponential weight has already been included, separately by mode
and component before any radial supremum.  The mean and the pointwise
inverse are not dropped: remainder_constants() supplies their complete
strong-norm bounds from the accompanying proof.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from flint import arb, ctx
from closure_real_head_source_enclosure import ball_record


CAP_KEYS = ("A", "C", "U2", "S", "T")


def expand_real_centre(positive_caps):
    """Expand already halved, positive complex Fourier magnitude caps.

    A cosine coefficient must first be divided by2.  This function adds
    the conjugate mode; it performs no additional rescaling.
    """
    result = {}
    for mode, caps in positive_caps.items():
        if not isinstance(mode, int) or mode <= 0 or mode % 2:
            raise ValueError("Supply only positive even centre frequencies")
        if set(caps) != set(CAP_KEYS):
            raise ValueError("Need separate A,C,U2,S,T magnitude caps")
        result[mode] = dict(caps)
        result[-mode] = dict(caps)
    return result


def quadratic_mode_columns(output_mode, centre_caps, *, B, w_squared, tau):
    """Return true positive DQ columns for one NONZERO output frequency.

    centre_caps[j][name] bounds
      sup_panel exp(tau(s)*abs(j))*abs(name_j(s)).
    A=partial_theta(u2)-u1/B, C=u2+partial_theta(u1)/B,
    S=partial_theta(u1)/B, T=u1/B.  C should use the exact
    canonical Xi expression, retaining its cancellation of Q.

    An entry column[b]['d1'][ell] or ['dlambda'][ell] multiplies
      x_b,ell=(1+abs(b))*sup_cell exp(tau(s)*abs(b))*abs(v_b,ell(s)).
    The output Green norm already includes its own (1+abs(output_mode)).
    Every centre frequency is explicit; no sup/sum exchange is used.
    """
    if not isinstance(output_mode, int) or output_mode == 0 or output_mode % 2:
        raise ValueError("Output must be a nonzero even frequency")
    B, w_squared, tau = arb(B), arb(w_squared), arb(tau)
    if not B >= 1 or not w_squared >= 0 or not w_squared <= arb(1)/4:
        raise ValueError("Need B>=1 and the paid w^2<=1/4 background")
    if not tau >= 0:
        raise ValueError("The real analytic width must be nonnegative")
    E = 1+w_squared
    result = {}
    for j, caps in centre_caps.items():
        if not isinstance(j, int) or j == 0 or j % 2:
            raise ValueError("Centre modes must be explicit nonzero even integers")
        if set(caps) != set(CAP_KEYS):
            raise ValueError("Need exactly the five separately controlled caps")
        cc = {key: arb(caps[key]).upper() for key in CAP_KEYS}
        if any(not value >= 0 for value in cc.values()):
            raise ValueError("Magnitude caps must be nonnegative")
        b = output_mode-j
        if b == 0:
            continue  # The input state has no independent mean component.
        exponent = abs(output_mode)-abs(j)-abs(b)
        if exponent > 0:
            raise AssertionError("The Fourier triangle inequality failed")
        omega = (exponent*tau.lower()).exp().upper()
        factor = (2*omega/(1+abs(b))).upper()
        d1 = [(factor*E*cc["A"]/B).upper(),
              (factor*E*abs(b)*cc["A"]).upper()]
        dlambda = [
            (factor*(abs(b)*cc["C"]/B+w_squared*(
                abs(b)*(cc["U2"]+cc["S"])/B+cc["T"]/B))).upper(),
            (factor*(cc["C"]+w_squared*cc["S"])).upper()]
        result[b] = dict(centre_mode=j, triangle_factor=omega,
                         d1=d1, dlambda=dlambda)
    return result


def remainder_constants():
    """Complete mean/inverse remainder, in the two material strong norms.

    On Astar*X<=1/32:
      R=f-Q=Pperp[d1*a*R1 + sign(lambda)*dlambda*a*Rl],
      ||R1||<=4 X^3, ||Rl||<=27 X^3.
    On Astar*X<=1/64 the derivative bounds are32 X^2 and216 X^2.
    All Fourier modes are retained in these remainders.
    """
    return dict(value_domain=Fraction(1, 32),
                derivative_domain=Fraction(1, 64),
                d1_value=4, dlambda_value=27,
                d1_derivative=32, dlambda_derivative=216,
                full_quadratic_value=Fraction(3, 2),
                full_quadratic_derivative=3)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = 192
    f = Fraction
    checks = {
        "denominator_coefficient": f(5, 4)+4*f(1, 32) == f(11, 8),
        "denominator_below_half": f(11, 8)*f(1, 32) < f(1, 2),
        "d1_remainder_below4": f(5, 4)*2*f(11, 8) == f(55, 16) < 4,
        "lambda_mean_numerator": 10+16*f(1, 32) == f(21, 2),
        "lambda_remainder_below27": 2*f(21, 2)+4*f(11, 8) == f(53, 2) < 27,
        "cauchy_d1": 8*4 == 32,
        "cauchy_dlambda": 8*27 == 216,
        "quadratic_radial_constant": f(5, 4) < f(3, 2),
        "quadratic_lambda_constant": 1+f(16, 9)*f(1, 4) == f(13, 9) < f(3, 2),
        "quadratic_derivative_constant": 2*f(13, 9) < 3,
        "low_output_support": all(abs(m-j) <= 184
            for m in range(-92, 93, 2) if m
            for j in range(-92, 93, 2) if j),
    }
    # This small interface example records exact input/output support and
    # angular normalization.  It is not substituted for any real centre.
    demo = quadratic_mode_columns(92, expand_real_centre({2: {
        "A": arb(1)/2, "C": arb(1)/2, "U2": arb(1)/2,
        "S": arb(1)/2, "T": arb(1)/2}}),
        B=arb(592), w_squared=arb(1)/2**100, tau=arb(3)/4)
    result = dict(
        status="Exact rational remainder constants and signed Fourier interface; no actual Green or full contraction claim",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        checks=checks,
        constants={k: str(v) for k, v in remainder_constants().items()},
        complex_fourier_convention="A real cosine coefficient must first be halved; both signed modes are then retained",
        source_materials=["V^2/(r*w)", "abs(lambda)*V^2/w"],
        example_output_mode=92,
        example_columns={str(b): {
            "centre_mode": c["centre_mode"],
            "triangle_factor": ball_record(c["triangle_factor"]),
            "d1": [ball_record(v) for v in c["d1"]],
            "dlambda": [ball_record(v) for v in c["dlambda"]]}
            for b, c in demo.items()},
        actual_source_or_Green_integration=False,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    if not all(checks.values()):
        raise AssertionError("A stated rational inequality or frequency support failed")
    args.ledger.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(dict(output=str(args.ledger), checks=checks,
                          input_modes=sorted(demo))), flush=True)


if __name__ == "__main__":
    main()
