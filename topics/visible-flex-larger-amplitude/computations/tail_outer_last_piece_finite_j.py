"""Full finite-J audit of the preserved physical-r last R48 piece.

Read the already paid true background and true positive-moment boxes. The
same exact unknown moments define the same candidate; no midpoint is chosen.
Use finite integer Horner for its actual k and k_r, retain the complete R64
mean, and keep every residual cosine coefficient through twice the cutoff.
No source quadrature, source profile evaluation, radial ODE or Node is run.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import json
from pathlib import Path
import resource
import time

from flint import arb, ctx
from closure_split_joint_io import read, digest
from closure_real_head_green_enclosure import ball
from closure_real_head_source_enclosure import exact_q, ball_record
from tail_outer_weighted_compatible import (
    normalized_endpoint_jet, make_weighted_candidate, MOMENT_KEYS)
from tail_outer_centered_quartic_fields_v2 import (
    weighted_panel_fields, intersection, rational_identity_checks)
from tail_outer_positive_moment_panels import positive_hull
from tail_outer_candidate_domain import nonnegative_integral
from tail_outer_segment_candidate_domain import primitive
from tail_outer_general_mean_bounds import general_mean_and_defect
from tail_outer_substage_span_refinement import finite_complete_J


def rec(values):
    return {str(key): ball_record(value) for key, value in values.items()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("candidate", "nodes", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--parts", type=int, default=16)
    parser.add_argument("--rss-limit-mib", type=int, default=40)
    args = parser.parse_args()
    if args.out.exists() or args.out.suffix != ".gz":
        raise FileExistsError("Use a fresh compressed candidate audit")
    if args.parts < 1:
        raise ValueError("A complete positive partition is required")
    ctx.prec = 192
    started = time.monotonic()
    old, nodes = map(read, (args.candidate, args.nodes))
    hashes = {str(p): digest(p) for p in (args.candidate, args.nodes)}
    if (old["cell"] != 0 or old["segment"] != 8 or nodes["cell"] != 0
            or not all(old["gates"].values())
            or not old["source_background_unchanged"]
            or not old["shared_physical_endpoint_two_jets"]
            or not old["exact_saved_cut_height_preserved"]
            or old["modes"] != nodes["modes"] or old["tau"] != nodes["tau"]
            or old["input_hashes"].get(str(args.nodes)) != hashes[str(args.nodes)]):
        raise ValueError("The completed original physical-r candidate is required")
    for path, checksum in old["input_hashes"].items():
        if digest(Path(path)) != checksum:
            raise ValueError("An original real-background/candidate input changed: "+path)
    for name, checksum in old["source_hashes"].items():
        if digest(Path(__file__).with_name(name)) != checksum:
            raise ValueError("An original executed candidate source changed: "+name)
    source_sha = digest(Path(__file__).with_name("tail_outer_last_piece_physical_radius.py"))
    if source_sha != "9ef12e10a6ab3eaf5b66375e0edeeb082ce8d9c2126782574e3aa739c831d9c3":
        raise ValueError("The preserved physical-r construction changed")
    checks = rational_identity_checks()
    bg = {name: ball(value) for name, value in old["background"].items()}
    rl, rr, width, w, wr = (bg[name] for name in
        ("radius_left", "radius_right", "width", "w_range", "wr_intersected_R31"))
    if not width > 0 or not w > 0:
        raise ArithmeticError("Positive physical measure is missing")
    ell = wr/w
    left, right = nodes["rows"][8], nodes["rows"][9]
    def endpoint(node):
        jets = {name: {int(m): ball(v) for m, v in
                      node["shared_physical_jets"][name].items()}
                for name in ("H", "Hr", "Hrr")}
        wi, wri = ball(node["w"]), ball(node["wr"])
        return normalized_endpoint_jet(jets["H"], jets["Hr"], jets["Hrr"],
            w=wi, radius_u=width, log_w_u=width*wri/wi)
    total = {key: ball(old["total_true_positive_moments"][key]) for key in MOMENT_KEYS}
    candidate = make_weighted_candidate(endpoint(left), endpoint(right), total)
    for m, value in candidate["bubble_coefficient"].items():
        candidate["bubble_coefficient"][m] = intersection(
            value, ball(old["bubble_coefficients"][str(m)]))
    def moments(lower, upper):
        return {key: nonnegative_integral(ball_record(positive_hull(
            (width.lower()*w.lower()*exact_q(lower[key])).lower(),
            (width.upper()*w.upper()*exact_q(upper[key])).upper())))
            for key in MOMENT_KEYS}
    modes, tau = old["modes"], F(old["tau"])
    cutoff = max(modes)
    weights = {m: ((1+m)*(exact_q(tau)*m).exp()).upper()
               for m in range(0, 2*cutoff+1, 2)}
    whole = primitive(F(1))
    maxima, minima, rows = {}, {}, []
    for index in range(args.parts):
        a, b = F(index, args.parts), F(index+1, args.parts)
        pa, pb = primitive(a), primitive(b)
        before = moments(pa, pb)
        after = moments({key: whole[key]-pb[key] for key in MOMENT_KEYS},
                        {key: whole[key]-pa[key] for key in MOMENT_KEYS})
        u = exact_q(a).union(exact_q(b))
        radius = intersection(rl+width*u, rr-width*(1-u))
        H, K, Kr = weighted_panel_fields(candidate, u=u, u_x=1/width,
                                        prefix_moments=before, suffix_moments=after)
        r64 = general_mean_and_defect(H, K, Kr, modes=modes, weights=weights,
            radius=radius, radius_x=arb(1), w=w, log_w_x=ell)
        if not r64["gate"]:
            raise ArithmeticError("The same-candidate complete mean gate failed")
        full = finite_complete_J(H, K, Kr, radius=radius,
            g=dict(w=w, radius_x=arb(1), log_w_x=ell), r64=r64,
            cutoff=cutoff, weights=weights)
        for key, value in {**r64["bounds"], **full["bounds"]}.items():
            if key not in maxima or value > maxima[key]["value"]:
                maxima[key] = dict(value=value, panel=index, u_left=str(a), u_right=str(b))
        for key in ("mean_sign_margin", "mean_derivative_lower", "real_y_lower",
                    "real_N_lower", "real_D_lower", "real_S_lower", "real_L_lower",
                    "Wiener_L_lower"):
            value = r64[key]
            if key not in minima or value < minima[key]["value"]:
                minima[key] = dict(value=value, panel=index)
        rows.append(dict(panel=index, u_left=str(a), u_right=str(b),
            radius=ball_record(radius), source_coordinate="physical r; r_x=1",
            full_R64_mean_domain_gate=True, full_finite_J_bounds=rec(full["bounds"]),
            complete_J_cosine=rec(full["coefficients"]),
            actual_nonmean_Hrr_cosine=rec(full["Hrr"])))
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > args.rss_limit_mib*1024:
            raise MemoryError("The finite-J physical-r audit exceeded its observed RSS cap")
    packet = dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", scope=__doc__,
        status="Complete same-candidate physical-r last-piece full finite-J audit",
        cell=0, segment=8, modes=modes, tau=str(tau), rows=rows,
        bounds={key: {**value, "value": ball_record(value["value"])}
                for key, value in maxima.items()},
        minima={key: {**value, "value": ball_record(value["value"])}
                for key, value in minima.items()},
        gates=dict(same_original_candidate_and_true_background=True,
            all_positive_moments_and_endpoint_jets_retained=True,
            complete_physical_radius_cover=len(rows)==args.parts,
            complete_R64_mean_and_inverse_domain=True,
            actual_radial_derivatives_not_PDE_substitutes=True,
            all_finite_residual_modes_through_twice_cutoff=True),
        finite_horner_checks=checks, input_hashes=hashes,
        original_candidate_input_hashes=old["input_hashes"],
        source_hashes={name: digest(Path(__file__).with_name(name)) for name in (
            Path(__file__).name, "tail_outer_centered_quartic_fields_v2.py",
            "tail_outer_centered_quartic_fields.py", "tail_outer_weighted_compatible.py",
            "tail_outer_general_mean_bounds.py", "tail_outer_substage_span_refinement.py",
            "tail_outer_last_piece_physical_radius.py", "tail_outer_segment_candidate_domain.py")},
        new_source_quadrature=0, new_source_profile_evaluation=0,
        new_radial_ODE_or_Node=False, exact_outer_solution_claimed=False,
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with gzip.open(args.out, "xt") as stream:
        json.dump(packet, stream, indent=2)
        stream.write("\n")
    if args.out.stat().st_size >= 5_000_000:
        raise ValueError("The full-angle last-piece package exceeds the file limit")
    print(json.dumps(dict(event="complete", output=str(args.out), panels=len(rows),
        gates=packet["gates"], maximum=packet["bounds"]["finite_J_l1_Darboux_upper"],
        seconds=packet["elapsed_seconds"], peak_RSS_KiB=packet["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
