#!/usr/bin/env python3
"""Choose an exact finite terminal K from a complete Arb Fourier head.

This is only a proposal. Its defining finite matrix is solved with Arb to avoid
binary64 high-mode noise; the independent full Laurent certificate must still
pay every frequency, both exponential tails and both K' transport multipliers.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path
import time
from flint import arb, acb, acb_poly, arb_mat, ctx

from fourfold_codazzi_phase_complete_transport_cover import read, decode_state, PRODUCER, ROOT
import fourfold_codazzi_phase_Wiener_transport_lift as lift_source
import fourfold_codazzi_phase_full_transport_Taylor as producer
from fourfold_codazzi_phase_terminal_postcomposition import powers
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--wiener-lift", type=Path, required=True)
    p.add_argument("--post-modes", type=int, default=48)
    p.add_argument("--exp-degree", type=int, default=24)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    if args.out.exists():
        raise FileExistsError("preserve every actual exact terminal proposal")
    started = time.monotonic()
    ctx.prec = 320
    d = read(args.wiener_lift)
    if (not d["complete"] or not d["whole_negative_domain"]
            or d["germ_count"] != 169 or d["original_producer_sha256"] != PRODUCER
            or d["root_contract_sha256"] != ROOT or d["source_sha256"] != sha(lift_source.__file__)):
        raise ValueError("the actual completed169 Wiener terminal is required")
    J, order, N = args.post_modes, args.exp_degree, 64
    if not 1 <= J <= 96 or not 1 <= order <= 64:
        raise ValueError("the declared finite proposal sizes are outside this implementation")
    state = decode_state(d["exact_terminal_phase_state"], N)
    full = order*N+J
    matrices, means = [], []
    for side in state:
        coeff = [producer.cplx(z) for z in side]
        coeff[N] = 0
        matrices.append(powers(acb_poly(coeff), order))
        means.append(side[N][0])
    A, rhs = arb_mat(2*J, 2*J), arb_mat(2*J, 1)
    for n in range(1, J+1):
        c = producer.cplx((state[1][N+n][0]-state[0][N+n][0],
                           state[1][N+n][1]-state[0][N+n][1])) if n <= N else acb(0)
        rhs[n-1, 0], rhs[J+n-1, 0] = -c.real, -c.imag
    mean_sin, mean_cos = [], []
    for j in range(1, J+1):
        sides = []
        for wp, mean in zip(matrices, means):
            taylor = acb_poly([])
            scale = acb(1)
            for n, w in enumerate(wp):
                taylor += w.left_shift(N*(order-n))*scale
                scale *= acb(0, 4*j)/(n+1)
            sides.append(taylor.left_shift(J+j)*acb(0, 4*j*exact_arb(mean)).exp())
        difference = sides[1]-sides[0]
        center = difference[full]
        mean_sin.append((center-center.conjugate())*acb(0, exact_arb(Fraction(-1, 2))))
        mean_cos.append((center+center.conjugate())/2)
        for n in range(1, J+1):
            positive, reflected = difference[full+n], difference[full-n].conjugate()
            sine = (positive-reflected)*acb(0, exact_arb(Fraction(-1, 2)))
            cosine = (positive+reflected)/2
            A[n-1, j-1], A[J+n-1, j-1] = sine.real, sine.imag
            A[n-1, J+j-1], A[J+n-1, J+j-1] = cosine.real, cosine.imag
    solved = A.solve(rhs)
    values = [producer.mid(solved[k, 0]) for k in range(2*J)]
    a, b = values[:J], values[J:]
    exact_vector = arb_mat([[exact_arb(x)] for x in values])
    residual = A*exact_vector-rhs
    defect = sum((abs(residual[k, 0]) for k in range(2*J)), arb(0)).upper()
    mean = exact_arb(state[1][N][0]-state[0][N][0])
    for j in range(J):
        mean += exact_arb(a[j])*mean_sin[j].real+exact_arb(b[j])*mean_cos[j].real
    if not mean.is_finite() or not defect.is_finite():
        raise ArithmeticError("the actual finite proposal solve is not finite")
    output = dict(kind="exact_dyadic_terminal_proposal_from_complete_Arb_head",
        complete=True, source_sha256=sha(__file__), wiener_lift_sha256=sha(args.wiener_lift),
        post_modes=J, exponential_degree=order, arithmetic_bits=320,
        exact_postcomposition_sine_coefficients=list(map(str, a)),
        exact_postcomposition_cosine_coefficients=list(map(str, b)),
        exact_proposed_terminal_rotation=str(producer.mid(mean)),
        finite_defining_head_residual_l1=record(defect),
        proposed_finite_terminal_mean=record(mean),
        all_actual_phase_modes_used=True,
        only_a_proposal_not_a_conjugacy_or_true_return_certificate=True,
        full_unprojected_Laurent_tail_and_transport_fees_still_required=True,
        seconds=time.monotonic()-started)
    save(args.out, output)
    print(dict(complete=True, modes=J, head_defining_residual=defect.str(12),
        proposed_mean=mean.str(24), seconds=output["seconds"]), flush=True)


if __name__ == "__main__":
    main()
