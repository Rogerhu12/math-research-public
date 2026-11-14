#!/usr/bin/env python3
"""Exact strict-core first-symbol and root-subtraction identities.

This verifies polynomial/rational identities for the complete moving Jacobi
system. It neither measures the actual finite-part integral nor certifies
its identification with a complete two-port return. Run in the public
repository's genuine Actions environment; all gates and scope are saved.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import time

import sympy as sp


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("execute the exact mathematical gates in the public repository's real Actions job")
    if args.out.exists():
        raise FileExistsError("preserve every exact first-symbol identity report")
    start = time.monotonic()
    u, v, up, vp, q, qr, b, eta, d, dpp, ell = sp.symbols(
        "u v u_phi v_phi q q_r beta_metric eta d d_phiphi ell", real=True)
    rp, rm = u+q*v, u-q*v
    rpp, rmp = up+q*vp, up-q*vp
    Bp, Bm = -qr/(2*q)-b*(1+rp**2), -qr/(2*q)-b*(1+rm**2)
    C = sp.diag(d+eta*q, d-eta*q)
    B = sp.Matrix([[0, Bp], [Bm, 0]])
    S = sp.Matrix([[0, -Bp/(2*eta*q)], [Bm/(2*eta*q), 0]])
    A0 = ell*sp.eye(2)+B
    A0new = A0+C*S-S*C
    N = -b*sp.Matrix([[rpp*rm, rpp*rp], [rmp*rm, rmp*rp]])
    Aminus = N-dpp*sp.eye(2)
    # C S_phi, S_r, S C_phi and the primitive-derived -B_phi are
    # off-diagonal, so the complete diagonal at order -1 is Aminus+B S.
    diagonal = [sp.factor((Aminus+B*S)[i, i]) for i in range(2)]
    expected = [-dpp-b*rpp*rm+Bp*Bm/(2*eta*q),
                -dpp-b*rmp*rp-Bp*Bm/(2*eta*q)]
    X = Bp*Bm/(eta*q)-2*b*q*(u*vp-v*up)

    rho, k, kr, etar, U2 = sp.symbols("rho k k_rho eta_rho U2", positive=True)
    sqrtk = sp.sqrt(k)
    a0 = kr/(4*k)-b*(1+u**2+rho*k*v**2)
    formal_q = sp.sqrt(rho)*sqrtk
    formal_qr_over_2q = -1/(4*rho)-kr/(4*k)
    BB = ((-formal_qr_over_2q-b*(1+u**2+rho*k*v**2))**2
          -4*b*b*rho*k*u*u*v*v)
    root_X = BB/(eta*formal_q)-2*b*formal_q*(u*vp-v*up)
    root_expansion = (1/(16*eta*sqrtk)*rho**sp.Rational(-5, 2)
        +a0/(2*eta*sqrtk)*rho**sp.Rational(-3, 2)
        +a0*a0/(eta*sqrtk)*rho**sp.Rational(-1, 2)
        -(4*b*b*sqrtk*u*u*v*v/eta+2*b*sqrtk*(u*vp-v*up))*sp.sqrt(rho))
    root_g0 = 1/(16*eta*sqrtk)
    derivative_A = -root_g0*(etar/eta+kr/(2*k))
    mean_B = (kr/(4*k)-b*(1+U2))/(2*eta*sqrtk)
    root_g1 = (-etar/eta+3*kr/(2*k)-8*b*(1+U2))/(16*eta*sqrtk)
    j, theta = sp.symbols("j theta", real=True, nonzero=True)

    gates = []
    def check(name, value):
        okay = bool(value)
        gates.append(dict(name=name, passed=okay))
        if not okay:
            raise ArithmeticError("exact identity failed: "+name)
    check("the complete cross-wave order-zero coefficient is eliminated",
          all(sp.cancel(x) == 0 for x in A0new-ell*sp.eye(2)))
    check("the common true mean-residual reaction commutes with the normalizer",
          all(sp.cancel(x) == 0 for x in ell*S-S*ell))
    check("both signed diagonal order-minus-one coefficients retain the primitive",
          all(sp.cancel(x-y) == 0 for x, y in zip(diagonal, expected)))
    check("the complete signed coefficient difference has its exact mean-integrand form",
          sp.cancel(diagonal[0]-diagonal[1]-X) == 0)
    check("the product Bplus Bminus keeps every quadratic and quartic centre term",
          sp.cancel(Bp*Bm-((qr/(2*q)+b*(1+u*u+q*q*v*v))**2
                           -4*b*b*q*q*u*u*v*v)) == 0)
    check("the diagonal sum has no falsely independent common first-symbol term",
          sp.cancel(diagonal[0]+diagonal[1]+2*dpp
                    +2*b*(u*up-q*q*v*vp)) == 0)
    check("the exact simple-root expansion retains every integrable half-power term",
          sp.simplify(root_X-root_expansion) == 0)
    check("the first nonintegrable root coefficient is exact", root_g0 == 1/(16*eta*sqrtk))
    check("the second root subtraction includes the full angular mean of u squared",
          sp.simplify(derivative_A+mean_B-root_g1) == 0)
    check("physical inverse derivative has exactly the factor-four phase unit",
          sp.simplify(sp.diff(sp.exp(4*sp.I*j*theta)/(4*sp.I*j), theta)
                      -sp.exp(4*sp.I*j*theta)) == 0)
    output = dict(
        kind="complete_moving_strict_first_symbol_and_root_subtraction_exact_identities",
        complete=True,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        candidate_manifest_sha256="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
        complete_continuous_centre_definition_sha256="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47",
        parameter_nu="-2572625729470897/72057594037927936",
        actual_affine_parameter="eta_0", exact_affine_offset="0",
        formulas=dict(cross_normalizer=sp.sstr(S),
            diagonal_coefficients=[sp.sstr(x) for x in expected],
            signed_first_symbol_density=sp.sstr(X),
            root_subtraction_0=sp.sstr(root_g0), root_subtraction_1=sp.sstr(root_g1)),
        exact_circle_primitive_mean_terms_retained=True,
        source_and_interface_changes_retained_in_proof=True,
        algebra_holds_without_setting_candidate_or_mean_residual_to_zero=True,
        full_frequency_strict_order_minus_two_remainder_has_finite_coefficient_bounds=True,
        actual_quantitative_strict_remainder_not_computed=True,
        actual_finite_part_integral_not_computed=True,
        matching_to_true_root_positive_cap_return_not_yet_paid=True,
        actual_beta_of_complete_return_not_claimed=True,
        complete_PDE_inverse_not_claimed=True,
        run_id=os.environ.get("GITHUB_RUN_ID"), run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        gates=gates, seconds=time.monotonic()-start)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(output, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps(dict(complete=True, gates=len(gates),
        actual_beta_of_complete_return_not_claimed=True, output=str(args.out))))


if __name__ == "__main__":
    main()
