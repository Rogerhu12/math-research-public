#!/usr/bin/env python3
"""Exact R31 curvature-transfer ledger and optional corrected-cut bound.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.

The deep statement is conditional on the real R23 strong ball and K_bg<=8.
An optional cut bound uses the explicitly R19-corrected binary-rational cut,
not the uncorrected radial response or a certified real-source trajectory.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path

from tail_cartesian_cut_interval import I, encode


def deep_ledger():
    sigma, small = F(1, 2**24), F(1, 2**16)
    epsilon = sigma*(4*small+4*(2+sigma)*small**2)
    perturbation = (4+5*sigma)*small+16*(2+sigma)*small**2
    curvature = 8*(1+perturbation)/(1-epsilon)
    nz2 = (1-epsilon)/(1+sigma)
    assert 0 < epsilon < 1
    assert curvature < F(8001, 1000) < F(33, 4)
    assert nz2 > F(99999994, 10**8)
    return {
        "scope": "Conditional exact full-frequency R23 implication. No current trajectory is asserted to satisfy the strong ball or real background curvature gate.",
        "w_squared_upper": encode(sigma),
        "relative_R_upper": encode(small),
        "epsilon_upper": encode(epsilon),
        "relative_Hessian_perturbation_upper": encode(perturbation),
        "principal_curvature_upper": encode(curvature),
        "normal_vertical_squared_lower": encode(nz2),
        "curvature_target": encode(F(8001, 1000)),
        "principal_target_passed": True,
        "R23_strong_ball_currently_paid_by_this_script": False,
        "real_background_curvature_currently_paid_by_this_script": False,
    }


def corrected_cut(packet, enclosure):
    j = packet["response"]["jets"]
    spacing = int(packet["config"]["spacing"])
    r, E, Ep, w, wr, pmean, qmean = [
        F.from_float(j[k]) for k in
        ("radius", "E", "Ep", "backgroundSlope", "backgroundSecond", "meanSlope", "meanSecond")]
    H, P, Q = [list(map(F.from_float, j[k])) for k in ("height", "slope", "second")]
    eta = F(enclosure["complete_second_correction"]["mean_shift_abs_upper"]["exact"])
    mu = F(enclosure["complete_second_correction"]["complete_second_correction_theta_derivative_bounds"][0]["exact"])
    modes = [spacing*(k+1) for k in range(len(H))]
    dp, dq = pmean-w, qmean-wr
    d = abs(dp)+sum(map(abs, P), F(0))+eta
    e = sum((m*abs(h) for m, h in zip(modes, H)), F(0))/r
    beta = 1-w*w/E
    epsilon = ((2*abs(w)*d+d*d)/E+e*e)/beta
    if beta <= 0 or epsilon >= 1:
        raise ValueError("Positive projection gate failed")
    connection = Ep/(2*E)
    A = (abs(dq-connection*dp)
         +sum((abs(q-connection*p) for q, p in zip(Q, P)), F(0))
         +mu+abs(connection)*eta)/E
    sqrtE_lower = I(E).sqrt().lo
    B = sum((m*abs(p-h/r) for m, p, h in zip(modes, P, H)), F(0))/(r*sqrtE_lower)
    C = (abs(dp)/E+sum((abs(p/E-m*m*h/r) for m, p, h in zip(modes, P, H)), F(0))
         +eta/E)/r
    root_beta_lower = I(beta).sqrt().lo
    root_one_minus_epsilon_lower = I(1-epsilon).sqrt().lo
    reference_rr = (wr-connection*w)/E
    reference_tt = w/(E*r)
    reference = max(abs(reference_rr), abs(reference_tt))/root_beta_lower
    spectral = F(A+C, 2)+I(F((A-C)**2, 4)+B*B).sqrt().hi
    curvature = (reference+spectral/root_beta_lower)/root_one_minus_epsilon_lower
    target = F(33, 4)
    return {
        "scope": "All-angle R31 bound for the exact mean/Q-corrected direct-stored cut only. It is not an entire radial-tail curvature bound.",
        "complete_mean_slope_correction_bound": encode(eta),
        "complete_second_correction_bound": encode(mu),
        "background_identity_discrepancy": {
            "E_minus_1_minus_w_squared": encode(E-1-w*w),
            "Ep_minus_2w_wr": encode(Ep-2*w*wr),
        },
        "beta": encode(beta), "epsilon_upper": encode(epsilon),
        "gradient_perturbation_bounds": [encode(d), encode(e)],
        "intrinsic_Hessian_entry_bounds": [encode(A), encode(B), encode(C)],
        "intrinsic_Hessian_operator_bound": encode(spectral),
        "reference_matrix_curvature_bound": encode(reference),
        "principal_curvature_upper": encode(curvature),
        "normal_vertical_squared_lower": encode(beta*(1-epsilon)),
        "target": encode(target), "target_passed": curvature <= target,
        "source_E_Ep_unchanged": True,
        "actual_radial_tail_certificate": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--cut-response", type=Path)
    parser.add_argument("--cartesian-enclosure", type=Path)
    args = parser.parse_args()
    if bool(args.cut_response) != bool(args.cartesian_enclosure):
        raise ValueError("Supply both corrected-cut dependency files or neither")
    output = {
        "author": "tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        "status": "Exact rational R31 implications; current whole-tail hypotheses remain separate",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "interval_helper_sha256": hashlib.sha256(
            (Path(__file__).parent/"tail_cartesian_cut_interval.py").read_bytes()).hexdigest(),
        "deep_implication": deep_ledger(),
    }
    if args.cut_response:
        raw = args.cut_response.read_bytes()
        packet = json.loads(gzip.decompress(raw) if args.cut_response.suffix == ".gz" else raw)
        encbytes = args.cartesian_enclosure.read_bytes()
        enclosure = json.loads(encbytes)
        digest = hashlib.sha256(raw).hexdigest()
        if enclosure["response_sha256"] != digest:
            raise ValueError("Corrected-cut enclosure has different response input")
        if not enclosure["represented_corrected_cut_cartesian_certificate"]:
            raise ValueError("The exact Cartesian cut construction was not certified")
        output["cut_input"] = str(args.cut_response)
        output["cut_input_sha256"] = digest
        output["cartesian_enclosure"] = str(args.cartesian_enclosure)
        output["cartesian_enclosure_sha256"] = hashlib.sha256(encbytes).hexdigest()
        output["corrected_cut"] = corrected_cut(packet, enclosure)
    args.out.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps({
        "output": str(args.out),
        "deep_curvature_upper": output["deep_implication"]["principal_curvature_upper"]["decimal"],
        "deep_nz2_lower": output["deep_implication"]["normal_vertical_squared_lower"]["decimal"],
        "corrected_cut_curvature_upper": output.get("corrected_cut", {}).get("principal_curvature_upper", {}).get("decimal"),
    }))


if __name__ == "__main__":
    main()
