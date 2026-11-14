#!/usr/bin/env python3
"""Pay an actual R33 physical density and infinite-frequency source window.

Consumes the real low46 anisotropic box and real radius/mu columns. No
radial integration or nonlinear numerical solve is performed. The retained
low46 and modes >= cutoff are kept distinct from the unpaid middle window.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import arb, ctx
from closure_real_head_source_enclosure import exact_q, ball_record, power2
from closure_real_head_green_enclosure import load_json, ball, endpoint


def up(x):
    return x.upper()


def record_rows(rows):
    return [{k: ball_record(v) if isinstance(v, arb) else v for k, v in row.items()} for row in rows]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--box", type=Path, required=True)
    p.add_argument("--reference", type=Path, required=True)
    p.add_argument("--columns", type=Path, required=True)
    p.add_argument("--ready", type=Path, required=True)
    p.add_argument("--source-ledger", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--cutoff", type=int, default=8192)
    args = p.parse_args()
    ctx.prec = 192
    began = time.monotonic()
    if args.cutoff < 94 or args.cutoff % 2:
        raise ValueError("An even frequency cutoff above the 46 low modes is required")
    docs, hashes = {}, {}
    for name in ("box", "reference", "columns", "ready", "source_ledger"):
        path = getattr(args, name)
        docs[name], raw = load_json(path)
        hashes[str(path)] = hashlib.sha256(raw).hexdigest()
    box, reference, columns, ready, paid = (docs[n] for n in
        ("box", "reference", "columns", "ready", "source_ledger"))
    if not all(box["gates"].values()) or not all(paid["checks"].values()):
        raise ValueError("The actual box and R22 source conditions must be paid")
    if box["modes"] != list(range(2,93,2)):
        raise ValueError("All 46 low modes must be retained")
    if hashes[str(args.ready)] not in paid["input_hashes"].values():
        raise ValueError("The R22 paid ledger belongs to another source")
    for doc in (box, reference):
        if hashes[str(args.ready)] not in doc["input_hashes"].values():
            raise ValueError("A supplied proof package belongs to another source")
    if hashes[str(args.reference)] not in box["input_hashes"].values():
        raise ValueError("The anisotropic box names another reference")
    if hashes[str(args.columns)] not in reference["input_hashes"].values():
        raise ValueError("The real column package is not one of the reference inputs")
    expected = list(range(12,225))
    if any([r["cell"] for r in docs[name][key]] != expected
           for name,key in (("box","rows"),("reference","cell_rows"),("columns","cell_rows"))):
        raise ValueError("Exactly the same 213 physical cells are required")
    params = ready["rationalDeepModel"]["physicalParameters"]
    rc = exact_q(params["rCuff"])
    R = rc*257/256
    d0 = exact_q(params["delta0"])
    ln2, sqrt12 = arb(2).log(), arb(12).sqrt()
    rows = []
    for b, r, col in zip(box["rows"], reference["cell_rows"], columns["cell_rows"]):
        n = b["cell"]
        # Every chosen envelope coefficient is a fixed outward dyadic bound.
        X = up(ball(b["total_radius_multiple"])*ball(r["reference_X"]))
        delta = d0*power2(-n)
        tv = arb(5*(n+9))
        analytic_width = 163*delta+11*power2(21)*(delta.log()*7/4).exp()
        true_width = up((endpoint(col["r_outer"]["upper"])-endpoint(col["r_inner"]["lower"]))/rc)
        width = min(up(analytic_width), true_width)
        if not width > 0:
            raise ValueError("A positive true-width upper bound is required")
        B = up((tv/width).sqrt())
        a = up(1+2*B/9)
        mu_lo, mu_hi = endpoint(col["mu"]["lower"]), endpoint(col["mu"]["upper"])
        w_min = mu_lo*delta/(2*R**7)
        amplitude = up(X*(a*R**3/w_min+sqrt12*mu_hi/(rc**4*w_min**2)))
        density = up(amplitude*(tv+width))
        beta = up(B*width+tv/B)
        eta = up(tv+4*width)
        rows.append(dict(cell=n, canonical_total_envelope=X, B=B, Q_coefficient=a,
            mu_lower=mu_lo, mu_upper=mu_hi, normalized_width_upper=width,
            TV_log_w_upper=tv, w_lower=w_min,
            V_over_w_upper=amplitude, density_integral_upper=density,
            beta_integral_upper=beta, eta_integral_upper=eta))
    jump_checks = []
    for outer, inner in zip(rows[:-1], rows[1:]):
        jump_checks.append(dict(outer_cell=outer["cell"], inner_cell=inner["cell"],
            B_contracts_outward=bool(outer["B"] <= inner["B"]),
            V_Q_part_increases_outward=bool(
                outer["canonical_total_envelope"]*outer["Q_coefficient"] >=
                inner["canonical_total_envelope"]*inner["Q_coefficient"]),
            V_Xi_part_increases_outward=bool(
                outer["canonical_total_envelope"]*outer["mu_upper"] >=
                inner["canonical_total_envelope"]*inner["mu_upper"])))
    if not all(all(v for k,v in c.items() if k.endswith("outward")) for c in jump_checks):
        raise ValueError("The piecewise physical norm is not contractive at a cell interface")
    density = up(sum((r["density_integral_upper"] for r in rows), arb(0)))
    k = up(4*density)
    M = args.cutoff
    sigma = arb(1)/8
    rounding_margin = power2(-128)
    tau = (1+212*ln2/4-sigma-rounding_margin).lower()
    tau_far = tau
    nodes = {225: tau}
    for i in range(len(rows)-1,-1,-1):
        r = rows[i]
        cost = up(r["beta_integral_upper"]+r["eta_integral_upper"]/M+r["density_integral_upper"]/k)
        outer_tau = (tau-cost).lower()
        if i:
            outer_tau = min(outer_tau, (1+(i-1)*ln2/4-sigma-rounding_margin).lower())
        r.update(tau_inner=tau, tau_outer=outer_tau,
            reference_tau=1+i*ln2/4, minimum_strip_buffer=sigma,
            sufficient_strip_cost=cost,
            available_strip_drop=(tau-outer_tau).lower())
        if not (tau+sigma <= (1+i*ln2/4).lower() or
                tau+sigma < 1+i*ln2/4):
            raise ValueError("The continuous strip exceeds the actual low46 reference strip")
        if not tau-outer_tau >= cost:
            raise ValueError("An assigned cell strip drop is insufficient")
        nodes[r["cell"]] = outer_tau
        tau = outer_tau
    if not tau > 0:
        raise ValueError("No positive shallow strip remains")
    gamma = up(2*k*(1+arb(1)/M))
    Astar = max(r["V_over_w_upper"] for r in rows)
    last = rows[-1]
    Xfar, Bfar = last["canonical_total_envelope"], last["B"]
    wflo, wfhi = last["mu_lower"]/R**7, last["mu_upper"]/rc**7
    Vlo = Xfar*(last["Q_coefficient"]*rc**3+sqrt12*last["mu_upper"]/(R**4*wfhi))
    Vhi = Xfar*(last["Q_coefficient"]*R**3+sqrt12*last["mu_upper"]/(rc**4*wflo))
    S = exact_q(params["epsilonScale"])/rc**10*((d0*power2(-224)).log()*11/2).exp()
    gap = 38-tau_far
    eD = up(Vhi/(S*Bfar*rc**3)*max(
        (gap*m).exp()/(m*(1+m)) for m in range(2,93,2)))
    bD = up(2*S/Vlo*(R**3*(Bfar+1)+sqrt12*last["mu_upper"]/(rc**4*wflo))*(1+3/gap)**3)
    low_state_bound = arb(213)
    high_radius = power2(-190)
    safe_total = low_state_bound+1
    z_bound = power2(-2200)
    CD = power2(1967)
    high_source_at_zero = up(16*gamma*low_state_bound**2*(-M*sigma).exp())
    high_far_at_zero = up(bD*CD*z_bound**2)
    high_lipschitz = up(64*gamma*safe_total)
    high_map = up(high_source_at_zero+high_far_at_zero+high_lipschitz*high_radius)
    gates = dict(
        all_contractive_norm_jumps=True,
        all_cell_strip_costs_paid=True,
        continuous_strip_stays_below_reference_minus_one_eighth=True,
        positive_shallow_strip=bool(tau > 0),
        complete_mean_working_domain=bool(Astar*safe_total < arb(1)/64),
        nonlinear_deep_graph_domain=bool(ball(box["complete_far_z_bound"]) < z_bound),
        high_window_self_map=bool(high_map < high_radius),
        high_window_contraction=bool(high_lipschitz < arb(1)/2))
    if not all(gates.values()):
        raise ValueError("An advertised high-window gate did not pass")
    result = dict(
        status="Verified physical density and complete infinite window m >= cutoff; middle-frequency source window remains unpaid",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        cutoff=M, cell_range=[12,224], precision_bits=ctx.prec,
        physical_envelope="V_n(r)=Xbar_n*((1+2*B_n/9)*r^3+sqrt(12)*mu_upper_n/(r^4*w(r)))",
        physical_envelope_coefficients="The stored Q_coefficient is rounded upward from 1+2*B_n/9.",
        canonical_box=box["domain"],
        low_state_bound=ball_record(low_state_bound),
        norm_order="Sum Fourier modes after separate radial suprema of both physical components; no sup/sum interchange.",
        continuous_strip_definition="On each cell use the normalized integral of B/r+abs(lambda)/B+(abs(lambda)+4/r)/M+c*V/(k*w); scale its integral to the assigned endpoint drop. This scale is at least one.",
        buffer=ball_record(sigma), endpoint_rounding_margin=ball_record(rounding_margin),
        tau_deep=ball_record(tau_far), tau_shallow=ball_record(tau),
        density_integral_upper=ball_record(density), k=ball_record(k),
        beta_integral_upper=ball_record(sum((r["beta_integral_upper"] for r in rows),arb(0))),
        eta_integral_upper=ball_record(sum((r["eta_integral_upper"] for r in rows),arb(0))),
        Astar_upper=ball_record(Astar), gamma_high=ball_record(gamma),
        far_evaluation_bound=ball_record(eD), far_evaluation_log2=ball_record(eD.log()/ln2),
        far_high_lift_bound=ball_record(bD), far_high_lift_log2=ball_record(bD.log()/ln2),
        high_window=dict(radius=ball_record(high_radius), radius_log2=-190,
            source_from_low_at_zero=ball_record(high_source_at_zero),
            source_from_low_at_zero_log2=ball_record(high_source_at_zero.log()/ln2),
            nonlinear_far_at_zero=ball_record(high_far_at_zero),
            nonlinear_far_at_zero_log2=ball_record(high_far_at_zero.log()/ln2),
            Lipschitz_upper=ball_record(high_lipschitz), map_upper=ball_record(high_map),
            map_over_radius=ball_record(high_map/high_radius),
            mean_root="The complete R33 holonomy root is used for every low-plus-high input.",
            scope="For any fixed finite reference supported in |m|<cutoff with wide-strip physical norm <=213 and R18 low height <=2^-2200, the complete m>=cutoff high equation has a unique solution in this ball. This does not solve the intervening modes or the low equations."),
        gates=gates, rows=record_rows(rows), norm_jump_checks=jump_checks,
        input_hashes=hashes,
        source_hashes={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in
            [Path(__file__).name,"closure_real_head_source_enclosure.py","closure_real_head_green_enclosure.py"]},
        radial_integrations=0, nonlinear_numerical_solves=0,
        elapsed_seconds=time.monotonic()-began,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        complete_full_frequency_head_paid=False,
        outer_cells_0_to_11_included=False,
        unpaid_middle_window=[94,M-2],
        limits=[
            "The low46 box is for the stated q003 real reference; it is not the stronger stored prefix trajectory.",
            "The new high solution need not satisfy the projected low equations with the low reference held fixed.",
            "Every intermediate even frequency from 94 to cutoff-2 remains a separate source Green problem.",
            "Actual strong outer-prefix matching, full curvature transfer and closed reach are independent."])
    encoded=(json.dumps(result,indent=2)+"\n").encode()
    if len(encoded) >= 1_000_000 and args.out.suffix != ".gz":
        raise ValueError("Use a compressed output for an expanded ledger")
    if args.out.suffix == ".gz":
        encoded=gzip.compress(encoded,mtime=0)
    if len(encoded) >= 5_000_000:
        raise ValueError("The repository single-file limit was exceeded")
    args.out.write_bytes(encoded)
    print(json.dumps(dict(output=str(args.out),gates=gates,
        density=result["density_integral_upper"]["display"],
        gamma_high=result["gamma_high"]["display"],tau_shallow=result["tau_shallow"]["display"],
        high_map_over_radius=result["high_window"]["map_over_radius"]["display"],
        elapsed_seconds=result["elapsed_seconds"],peak_RSS_KiB=result["peak_RSS_KiB"])))


if __name__ == "__main__":
    main()
