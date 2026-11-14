#!/usr/bin/env python3
"""Continuous strong-domain scan of one actual R48 outer-cell candidate.

Reads the complete true positive-moment groups, all saved M20 Q/L endpoint
coefficients, and the same real source. The missing endpoint second jets
are the explicit finite-polynomial definition in tail_outer_weighted_endpoint.
No interpolated ODE right-hand side is substituted for the true candidate
derivative. This first pass tests P/K/analytic leading gates throughout the
cell; it does not pretend to have computed the full continuous Darboux defect.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import resource
import time

from flint import arb, ctx
from closure_real_head_source_enclosure import exact_q, ball_record
from closure_real_head_green_enclosure import ball, endpoint
from closure_split_joint_io import read, digest, iter_array
from closure_real_outer_radius import OuterCell
from tail_r33_middle_ordered_physical import SourceValues
from tail_outer_weighted_endpoint import finite_saved_endpoint
from tail_outer_weighted_compatible import (
    intersection, cell_source_coordinate, normalized_endpoint_jet,
    make_weighted_candidate, weighted_panel_fields)


def nonnegative_integral(record, *, strict=False):
    """Use the proven nonnegative integral domain without editing old data."""
    lo, hi = endpoint(record["lower"]), endpoint(record["upper"])
    if not lo <= hi or not hi >= 0:
        raise ArithmeticError("Invalid actual positive-integral enclosure")
    value = ball(record)
    if value >= 0 and (not strict or value > 0):
        return value
    if strict:
        raise ArithmeticError("A full positive moment needs a strict stored lower bound")
    # The precise real moment is nonnegative by O1. Enclose the intersection
    # with[0,infinity) by an exactly representable midpoint/radius ball.
    # Unlike arb(0).union(U), the tuple constructor does not enlarge a
    # dyadic radius. Round U upward to24 significant bits before using it.
    if hi == 0:
        return arb(0)
    m, e = hi.upper().man_exp()
    m, e = int(m), int(e)
    shift = max(0, m.bit_length()-24)
    if shift:
        m, e = (m+(1 << shift)-1) >> shift, e+shift
    value = arb((m, e-1), (m, e-1))
    if not value >= 0 or value.upper() < hi:
        raise ArithmeticError("The exact nonnegative endpoint constructor failed")
    return value


def endpoint_candidate(cell, side, node, raw_state, saved_port, radius, tau, degree):
    segment = cell.segments[0 if side == "inner" else 8]
    x = F(0 if side == "inner" else 1)
    kind = cell.classify(segment, x, x)
    if kind is None:
        raise ArithmeticError("The exact endpoint source branch remains undecided")
    logw, ell = cell.profile(segment, exact_q(x), kind[0])
    w = logw.exp()
    rx = cell.integrand(segment, exact_q(x), kind[0], kind[1])
    if not w > 0 or not rx > 0:
        raise ArithmeticError("The true endpoint radial source is not regular")
    intersection(w, ball(saved_port["w"]))
    intersection(radius, ball(saved_port["radius"]))
    M = len(saved_port["candidate_L_orthonormal_cosine"])-1
    if len(raw_state) != 2*M:
        raise ValueError("The full saved height/momentum endpoint spectrum is required")
    jet = finite_saved_endpoint(
        raw_state[:M], saved_port["candidate_L_orthonormal_cosine"],
        radius=radius, radius_x=rx, w=w, log_w_x=ell,
        spacing=2, tau=tau, inverse_degree=degree)
    unused, ux = cell_source_coordinate([s["length"] for s in cell.segments],
                                        segment["j"], exact_q(x))
    candidate = normalized_endpoint_jet(
        jet["H"], jet["Hr"], jet["Hrr"], w=w,
        radius_u=rx/ux, log_w_u=ell/ux)
    report = dict(node=node, side=side, source_cell=cell.n,
                  source_segment=segment["j"], source_x=str(x),
                  same_true_background_point=True,
                  true_source_radius=ball_record(radius),
                  true_source_w=ball_record(w), **jet["report"])
    return candidate, report


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("cell-manifest", "port-candidates", "response", "ready", "out"):
        p.add_argument("--"+name, type=Path, required=True)
    p.add_argument("--tau", default="1/64")
    p.add_argument("--inverse-degree", type=int, default=8)
    p.add_argument("--rss-limit-mib", type=int, default=120)
    args = p.parse_args()
    if args.out.exists():
        raise FileExistsError("Use a fresh candidate-domain output")
    ctx.prec = 192
    began = time.monotonic()
    paths = [getattr(args, key) for key in
             ("cell_manifest", "port_candidates", "response", "ready")]
    hashes = {str(path): digest(path) for path in paths}
    data, ports, packet, ready = map(read, paths)
    if not all(data["checks"].values()):
        raise ValueError("The complete true moment package must pass its stated checks")
    meta = data["original_metadata"]
    if hashes[str(args.ready)] not in meta["input_hashes"].values():
        raise ValueError("The true background source differs")
    for path in (args.response, args.ready):
        if hashes[str(path)] not in ports["input_hashes"].values():
            raise ValueError("The full finite Q/L candidates belong to another saved response/source")
    cp = packet["response"]["checkpoint"]
    if (not packet["response"]["converged"] or cp["parameters"]["modes"] != 20
            or cp["parameters"]["physicalDepth"] != 12 or len(cp["rawStates"]) != 13):
        raise ValueError("This entry point requires the full actual13-port M20 response")
    n = data["cell"]
    if not 0 <= n <= 11 or sorted(g["source_segment"] for g in data["groups"]) != list(range(9)):
        raise ValueError("All nine original source segments are required")
    rows = {r["physical_node"]: r for r in ports["rows"]}
    tau = F(args.tau)
    if tau < 0:
        raise ValueError("Use a nonnegative fixed analytic width")
    head = SourceValues(ready)
    head.params = ready["rationalDeepModel"]["physicalParameters"]
    cell = OuterCell(head, n)
    inner, outer = ball(meta["inner_radius"]), ball(meta["outer_radius"])
    left, left_report = endpoint_candidate(
        cell, "inner", n+1, cp["rawStates"][n+1], rows[n+1], inner, tau, args.inverse_degree)
    right, right_report = endpoint_candidate(
        cell, "outer", n, cp["rawStates"][n], rows[n], outer, tau, args.inverse_degree)
    moments = {key: nonnegative_integral(value, strict=True)
               for key, value in meta["total_positive_moments"].items()}
    candidate = make_weighted_candidate(left, right, moments)
    modes = sorted(candidate["left"]["H"])
    weights = {m: ((1+m)*(exact_q(tau)*m).exp()).upper() for m in modes}
    worst = {name: dict(value=arb(0), witness=None) for name in
             ("P_tau", "K_tau", "R_tau", "R_zero", "Kx_tau", "nonmean_L_tau")}
    leading_min, mean_all, work_all = None, True, True
    segments, count = [], 0
    for group in sorted(data["groups"], key=lambda row: row["source_segment"]):
        path = Path(group["path"])
        if digest(path) != group["sha256"]:
            raise ValueError("A full true moment group changed")
        hashes[str(path)] = group["sha256"]
        segment_count, segment_R, segment_P, segment_K = 0, arb(0), arb(0), arb(0)
        for i, g in enumerate(iter_array(path, "panels")):
            if g["segment"] != group["source_segment"]:
                raise ValueError("A true source group contains another segment")
            prefix = {key: nonnegative_integral(value) for key, value in g["prefix_moments"].items()}
            suffix = {key: nonnegative_integral(value) for key, value in g["suffix_moments"].items()}
            H, K, Kx = weighted_panel_fields(
                candidate, u=ball(g["u"]), u_x=ball(g["u_x"]),
                prefix_moments=prefix, suffix_moments=suffix)
            r, w = ball(g["radius"]), ball(g["w"])
            if not r > 0 or not w > 0 or not w <= arb(1)/2:
                raise ArithmeticError("The actual source positivity/slope-cap domain failed")
            values = {name: arb(0) for name in worst}
            for m in modes:
                h, k, kx = 2*H[m].real, 2*K[m].real, 2*Kx[m].real
                for field in (H, K, Kx):
                    if not field[m].imag.contains(0):
                        raise ArithmeticError("The specified even cosine candidate lost reality")
                pp = abs(m*h/(r*w)).upper()
                kk, kxx = abs(k).upper(), abs(kx).upper()
                values["P_tau"] += weights[m]*pp
                values["K_tau"] += weights[m]*kk
                values["Kx_tau"] += weights[m]*kxx
                values["R_zero"] += (1+m)*(pp+kk)
                values["nonmean_L_tau"] += weights[m]*abs(k-(1+w*w)*m*m*h/(r*w)).upper()
            values["R_tau"] = values["P_tau"]+values["K_tau"]
            values = {key: value.upper() for key, value in values.items()}
            witness = dict(segment=g["segment"], panel=i, original_parent=g["original_parent"],
                           x_left=g["x_left"], x_right=g["x_right"],
                           radius=g["radius"], w=g["w"])
            for key, value in values.items():
                if value > worst[key]["value"]:
                    worst[key] = dict(value=value, witness=witness)
            good = values["R_tau"] < arb(1)/32
            mean_all &= bool(good)
            work_all &= bool(values["R_tau"] < arb(1)/64)
            if good:
                margin = (1-4*values["R_tau"]**2-values["nonmean_L_tau"]).lower()
                if leading_min is None or margin < leading_min:
                    leading_min = margin
            segment_R = max(segment_R, values["R_tau"])
            segment_P = max(segment_P, values["P_tau"])
            segment_K = max(segment_K, values["K_tau"])
            segment_count += 1
            count += 1
            if count % 128 == 0 and resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 1024*args.rss_limit_mib:
                raise MemoryError("The actual candidate-domain scan exceeded its RSS cap")
        if segment_count != group["panels"]:
            raise ValueError("A full true source group was not scanned")
        segments.append(dict(segment=group["source_segment"], panels=segment_count,
                             R_tau=ball_record(segment_R), P_tau=ball_record(segment_P),
                             K_tau=ball_record(segment_K)))
        print(json.dumps(dict(event="candidate_domain_segment", cell=n,
                              segment=group["source_segment"], panels=segment_count,
                              R_tau=str(segment_R), seconds=time.monotonic()-began)), flush=True)
    if count != data["panels"]:
        raise ValueError("The entire real cell was not scanned")
    result = dict(
        status="Complete true-panel domain bounds of the specified actual R48 candidate",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", cell=n,
        panels=count, tau=str(tau), modes=modes, inverse_degree=args.inverse_degree,
        endpoints=[left_report, right_report],
        bubble_coefficients={str(m): ball_record(v) for m, v in candidate["bubble_coefficient"].items()},
        worst={key: dict(value=ball_record(value["value"]), witness=value["witness"])
               for key, value in worst.items()}, segments=segments,
        gates=dict(complete_mean_small_branch=mean_all, R33_working_domain=work_all,
                   R44_Wiener_leading=mean_all and leading_min is not None and leading_min > 0),
        leading_lower=ball_record(leading_min) if mean_all and leading_min is not None else None,
        mean_bound_used="Only if R_tau<1/32: the complete R33 mean root has |c|<=4R_tau^2; no finite angular projection is substituted",
        partial_moment_handling="Exact saved intervals preserved; evaluation encloses their intersection with the proved nonnegative integral domain using exact dyadic midpoint/radius",
        first_height_compatibility_exact_by_R48=True,
        full_mean_radial_derivative_evaluated=False,
        continuous_Darboux_defect_paid=False,
        exact_radial_solution_claimed=False,
        input_hashes=hashes,
        source_hashes={name: digest(Path(__file__).with_name(name)) for name in
                       (Path(__file__).name, "tail_outer_weighted_endpoint.py",
                        "tail_outer_weighted_compatible.py", "tail_outer_compatible_mean_defect.py",
                        "closure_real_outer_radius.py", "tail_r33_middle_ordered_physical.py")},
        elapsed_seconds=time.monotonic()-began,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(dict(event="complete", output=str(args.out), gates=result["gates"],
                          panels=count, seconds=result["elapsed_seconds"],
                          peak_RSS_KiB=result["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
