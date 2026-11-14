#!/usr/bin/env python3
"""Recover R31's all-cell real-background curvature ledger.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
Only finite parameter checks and the cell-0 analytic log endpoints are used.
RealHead is never constructed, no radial integral or Node process is run.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace
from flint import arb, ctx
from closure_real_head_source_enclosure import exact_q, ball_record
from closure_real_outer_radius import OuterCell
from tail_cartesian_cut_interval import encode


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dyadic(record):
    return F(int(record["mantissa"]))*F(2)**record["binary_exponent"]


def run(ready_path, paid_path, port_path):
    ready = json.loads(ready_path.read_text())
    ready = ready.get("ready", ready)
    paid = json.loads(paid_path.read_text())
    ports = json.loads(port_path.read_text())
    assert all(paid["checks"].values())
    assert all(ports["checks"].values())
    assert digest(ready_path) in paid["input_hashes"].values()
    assert digest(ready_path) in ports["input_hashes"].values()
    assert digest(paid_path) in ports["input_hashes"].values()
    model = ready["rationalDeepModel"]
    params = model["physicalParameters"]
    rows = {x["n"]: x for x in ready["shallowSourceParameters"]["cells"]}
    d0 = F(model["exactSourceConstants"]["delta0"])
    c0 = F(model["exactSourceConstants"]["etaRatioAtN0"])
    rc = F.from_float(params["rCuff"])
    alpha = F.from_float(model["frozenWarpAlpha"])
    assert 4*c0*c0 > d0
    assert F(3,64) < rc < F(1,16) and alpha > 2
    assert params["orientation"] == 1 and params["protectCell"] == 160
    assert params["curvatureBound"] == 8 and params["capTransition"] == 2
    assert params["capMode"] == "cut-preserving"
    assert params.get("flatOuterThroughCell") is None
    assert params.get("rejoinR20At") is None
    cap = F.from_float(params["slopeCap"])
    assert cap == F.from_float(.02)
    pulses, valleys = params.get("pulseCaps", []), params.get("valleyCaps", [])
    for n in range(1,12):
        assert n >= len(pulses) or pulses[n] is None or pulses[n] == [params["slopeCap"]]*2
        assert n >= len(valleys) or valleys[n] is None or valleys[n] == params["slopeCap"]
    cap0 = max(cap, *map(F.from_float, pulses[0]), F.from_float(valleys[0]))
    assert cap0 == F.from_float(.4)
    for row in params.get("warpWeightLevels", []):
        if row is not None:
            assert len(row) == 5 and min(row) > 0 and row[0] == row[-1] == 1
    assert all(x == 0 for x in params["valleyControls"][7:])
    assert model["start"] == 160

    # The formulas in OuterCell are reused, but none of its integration
    # methods or the expensive RealHead constructor is called.
    head = SimpleNamespace(params=params, data=rows,
        rc=exact_q(rc), d0=exact_q(d0), c0=exact_q(c0),
        eps_phys=exact_q(params["epsilonScale"]), alpha=exact_q(alpha),
        a=arb(11)/4, sqrt12=arb(12).sqrt(), log2=arb(2).log())
    cell = OuterCell(head, 0)
    s7, s8 = cell.segments[7], cell.segments[8]
    A, B = s7["log_w0"], s7["jump"]
    c = exact_q(cap).log()
    assert B < 0 and cell.cap_values[3] == cell.cap_values[4] == params["slopeCap"]
    vertex = (c-(A-c)**2/(4*B)).exp()
    raw8 = s8["log_w0"].exp()
    assert vertex < exact_q(F(3,25))
    assert raw8 < exact_q(F(81,1000))
    cut_ratio = F.from_float(params["rCut"])/F.from_float(params["oldCut"])
    T = F(7)*F(81,1000)/(8*rc)
    assert cut_ratio > 5 and T < F(3,2)
    radius_lower = dyadic(ports["ports"]["12"]["radius"]["lower"])
    assert radius_lower > F(2501,50000)
    outer_angular = cap0/F(2501,50000)
    next_angular = cap/rc
    assert outer_angular < 8 and next_angular < F(401,1000)
    deep_derivative = F(3675,16384)+F(1,2**258)
    assert deep_derivative < F(9,40)
    monotonic = F(169,168)*F(27,32)
    assert monotonic < 1
    assert d0*F(1,2**159) < F(1,2**166)
    inputs = {str(p):digest(p) for p in (ready_path, paid_path, port_path)}
    return dict(
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        status="Exact all-cell R31 curvature bound for the R26 new real background",
        scope="Background only. No current nonlinear strong trajectory or old stored cut is certified.",
        input_hashes=inputs,
        source_revision=model["sourceRevision"],
        exact_parameters=dict(delta0=str(d0), eta0=str(c0), r_c=str(rc),
            warp_alpha=str(alpha), captured_oldCut=str(F.from_float(params["oldCut"]))),
        outer_cell0=dict(
            segment7_A=ball_record(A), segment7_B=ball_record(B),
            segment7_complete_log_blend_slope_upper=ball_record(vertex),
            segment8_raw_left_slope_upper=ball_record(raw8),
            segment7_target=encode(F(3,25)),
            segment8_target=encode(F(81,1000)),
            rCut_over_captured_oldCut=encode(cut_ratio),
            segment8_T_upper=encode(T),
            node12_radius_lower=encode(radius_lower),
            conservative_radius_lower=encode(F(2501,50000)),
            angular_curvature_upper=encode(outer_angular),
            radial_curvature_upper=8),
        outer_cells1to11=dict(slope_cap=encode(cap),
            angular_curvature_upper=encode(next_angular), radial_curvature_upper=8),
        cells12to158=dict(radial_curvature_upper=8, angular_curvature_upper=encode(F(1,192))),
        cells159onward=dict(raw_slope_derivative_upper=encode(deep_derivative),
            target=encode(F(9,40)), first_term_decay_ratio_upper=encode(monotonic),
            angular_curvature_upper=encode(F(1,192)), slope_and_derivative_tend_to_zero=True),
        all_cells_background_curvature_bound=8,
        real_background_curvature_paid=True,
        nonlinear_R23_strong_ball_paid=False,
        radial_integrations_performed=0,
        script_sha256=digest(Path(__file__)),
        outer_formula_sha256=digest(Path(__file__).with_name("closure_real_outer_radius.py")),
        source_formula_sha256=digest(Path(__file__).with_name("closure_real_head_source_enclosure.py")))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ready", type=Path, required=True)
    parser.add_argument("--paid-source", type=Path, required=True)
    parser.add_argument("--port-enclosure", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = 192
    result = run(args.ready, args.paid_source, args.port_enclosure)
    args.out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(dict(output=str(args.out),
        all_cells_background_curvature_bound=result["all_cells_background_curvature_bound"],
        segment7=result["outer_cell0"]["segment7_complete_log_blend_slope_upper"]["display"],
        segment8=result["outer_cell0"]["segment8_raw_left_slope_upper"]["display"],
        nonlinear_R23_strong_ball_paid=False)))


if __name__ == "__main__":
    main()
