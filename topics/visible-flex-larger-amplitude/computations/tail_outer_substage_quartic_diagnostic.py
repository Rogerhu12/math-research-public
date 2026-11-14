#!/usr/bin/env python3
"""Targeted exact-point and interval audit of one same-candidate quartic.

Use a formally completed span audit only to select its actual witness.
Rebuild the unchanged R48 candidate from the original true moments and
physical two-jets; record every normalized endpoint and quartic coefficient.
Compare the original basis and intersected centered evaluation on the witness,
its two halves, and its three boundary/midpoint points, retaining the original
bin's full primitive enclosure, complete R64 scalar mean and all finite J modes.
No source integral, radial ODE, saved state reconstruction or Node is run.
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
from closure_real_outer_radius import OuterCell
from tail_r33_middle_ordered_physical import SourceValues
from tail_outer_positive_moment_panels import source_range, MOMENT_KEYS
from tail_outer_candidate_domain import nonnegative_integral
from tail_outer_weighted_compatible import (
    intersection, normalized_endpoint_jet, make_weighted_candidate,
    weighted_panel_fields as basis_fields)
from tail_outer_centered_quartic_fields import (
    weighted_panel_fields as centered_fields, quartic_coefficients,
    rational_identity_checks)
from tail_outer_general_mean_bounds import general_mean_and_defect
from tail_outer_substage_span_refinement import finite_complete_J


def rec(values):
    return {str(key): ball_record(value) for key, value in values.items()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("candidate", "ready", "audit", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--field", default="finite_J_l1_Darboux_upper")
    parser.add_argument("--rss-limit-mib", type=int, default=40)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("Use a new same-quartic witness diagnostic")
    ctx.prec = 192
    began = time.monotonic()
    checks = rational_identity_checks()
    hashes = {str(p): digest(p) for p in (args.candidate, args.ready, args.audit)}
    data, ready, audit = map(read, (args.candidate, args.ready, args.audit))
    if (not all(data["gates"].values()) or not all(audit["gates"].values())
            or audit["input_hashes"].get(str(args.candidate)) != hashes[str(args.candidate)]
            or audit["input_hashes"].get(str(args.ready)) != hashes[str(args.ready)]
            or data["input_hashes"].get(str(args.ready)) != hashes[str(args.ready)]):
        raise ValueError("Completed same-candidate and fixed-background identities are required")
    for table in (data["source_hashes"], audit["source_hashes"]):
        for name, checksum in table.items():
            if digest(Path(__file__).with_name(name)) != checksum:
                raise ValueError("An executed source changed: "+name)
    witness = audit["bounds"][args.field]["witness"]
    j, k, v = (witness[name] for name in ("segment", "part", "bin"))
    if j != data["segment"] or data["cell"] != 0:
        raise ValueError("The source witness is outside this original candidate")
    modes, tau = data["modes"], F(data["tau"])
    cutoff = max(modes)
    part = data["parts"][k]
    nodes = [data["nodes"][k], data["nodes"][k+1]]
    bins = [row for row in data["bins"] if row["part"] == k]
    del data, audit
    a, b, h = F(k, 8), F(k+1, 8), F(1, 8)
    lo, hi = F(witness["source_left"]), F(witness["source_right"])
    midpoint = (lo+hi)/2
    if not a <= lo < hi <= b:
        raise ValueError("The witness has a different source coordinate")
    head = SourceValues(ready)
    head.params = ready["rationalDeepModel"]["physicalParameters"]
    cell = OuterCell(head, 0)
    segment = cell.segments[j]
    endpoint_records = []
    def endpoint(node):
        x = F(node["source_x"])
        g = source_range(cell, segment, x, x, None, exact_q(F(1, 8)))
        w = intersection(g["w"], ball(node["w"]))
        ell = intersection(g["log_w_x"], ball(node["wr"])*g["radius_x"]/w)
        jets = {key: {int(m): ball(value) for m, value in
                     node["shared_physical_jets"][key].items()}
                for key in ("H", "Hr", "Hrr")}
        jet = normalized_endpoint_jet(jets["H"], jets["Hr"], jets["Hrr"], w=w,
            radius_u=exact_q(h)*g["radius_x"], log_w_u=exact_q(h)*ell)
        endpoint_records.append(dict(source_x=str(x), w=ball_record(w),
            radius_x=ball_record(g["radius_x"]), log_w_x=ball_record(ell),
            physical_jets={key: rec(value) for key, value in jets.items()},
            normalized_jets={key: rec(value) for key, value in jet.items()}))
        return jet
    total = {key: ball(part["total_true_positive_moments"][key]) for key in MOMENT_KEYS}
    candidate = make_weighted_candidate(endpoint(nodes[0]), endpoint(nodes[1]), total)
    for m, value in candidate["bubble_coefficient"].items():
        candidate["bubble_coefficient"][m] = intersection(
            value, ball(part["bubble_coefficients"][str(m)]))
    polynomial_records = {str(m): [ball_record(c) for c in
                          quartic_coefficients(candidate, m)] for m in modes}
    def sums(indices):
        return {key: sum((ball(bins[i]["values"][key]) for i in indices), arb(0))
                for key in ("width", *MOMENT_KEYS)}
    pl, ph = sums(range(v)), sums(range(v+1))
    sl, sh = sums(range(v+1, 8)), sums(range(v, 8))
    def moments(low, high):
        return {key: nonnegative_integral(ball_record(
            max(arb(0), low[key].lower()).union(min(high[key].upper(), total[key].upper()))))
                for key in MOMENT_KEYS}
    prefix, suffix = moments(pl, ph), moments(sl, sh)
    rl, rr = ball(nodes[0]["radius"]), ball(nodes[1]["radius"])
    radius = intersection(rl+pl["width"], rr-sh["width"]).union(
             intersection(rl+ph["width"], rr-sl["width"]))
    weights = {m: ((1+m)*(exact_q(tau)*m).exp()).upper()
               for m in range(0, 2*cutoff+1, 2)}
    cases = (("whole", lo, hi), ("left_half", lo, midpoint),
             ("right_half", midpoint, hi), ("left_endpoint", lo, lo),
             ("midpoint", midpoint, midpoint), ("right_endpoint", hi, hi))
    reports = []
    for label, left, right in cases:
        g = source_range(cell, segment, left, right, None, exact_q(F(1, 8)))
        u = exact_q((left-a)/h).union(exact_q((right-a)/h))
        variants = []
        for method, fields in (("original_five_basis", basis_fields),
                               ("same_quartic_centered_intersection", centered_fields)):
            H, K, Kx = fields(candidate, u=u, u_x=1/exact_q(h),
                             prefix_moments=prefix, suffix_moments=suffix)
            r64 = general_mean_and_defect(H, K, Kx, modes=modes, weights=weights,
                radius=radius, radius_x=g["radius_x"], w=g["w"], log_w_x=g["log_w_x"])
            if not r64["gate"]:
                raise ArithmeticError("A subset of the actual witness lost its complete mean gate")
            full = finite_complete_J(H, K, Kx, radius=radius, g=g, r64=r64,
                                     cutoff=cutoff, weights=weights)
            lower = max(arb(0), (full["physical_conversion_factor"].lower()*
                        abs(full["coefficients"][2]).lower()/2).lower())
            variants.append(dict(method=method, actual_derivative_not_PDE=True,
                fields_cosine={name: rec({m: 2*poly[m].real for m in modes})
                               for name, poly in (("H", H), ("Kbar", K), ("Kbar_x", Kx))},
                complete_R64_bounds=rec(r64["bounds"]),
                full_finite_J_bounds=rec(full["bounds"]),
                complete_J_cosine=rec(full["coefficients"]),
                actual_nonmean_Hrr_cosine=rec(full["Hrr"]),
                physical_Darboux_m2_coefficient_lower=ball_record(lower)))
        reports.append(dict(scope=label, source_left=str(left), source_right=str(right),
            source=rec({"radius": radius, "w": g["w"], "radius_x": g["radius_x"],
                        "log_w_x": g["log_w_x"], "local_u": u}),
            primitive="The original complete positive bin prefix/suffix; no new partial integral",
            variants=variants))
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > args.rss_limit_mib*1024:
            raise MemoryError("The targeted existing-candidate audit exceeded its RSS cap")
    out = dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", scope=__doc__,
        status="Complete targeted interval/point comparison of the identical candidate",
        cell=0, segment=j, part=k, bin=v, witness=witness,
        endpoint_normalized_and_physical_jets=endpoint_records,
        monomial_quartic_coefficients=polynomial_records,
        exact_polynomial_identity_checks=checks, reports=reports,
        exact_same_candidate_and_complete_mean=True,
        input_hashes=hashes, new_source_integrals=0, new_radial_ODE_or_Node=False,
        new_whole_segment_maximum_claimed=False,
        source_hashes={name: digest(Path(__file__).with_name(name)) for name in (
            Path(__file__).name, "tail_outer_centered_quartic_fields.py",
            "tail_outer_substage_span_refinement.py",
            "tail_outer_weighted_compatible.py", "tail_outer_general_mean_bounds.py",
            "tail_outer_positive_moment_panels.py", "tail_outer_candidate_domain.py",
            "closure_real_outer_radius.py", "tail_r33_middle_ordered_physical.py")},
        elapsed_seconds=time.monotonic()-began,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if args.out.suffix != ".gz":
        raise ValueError("Compress the complete finite field and point records")
    with gzip.open(args.out, "xt") as stream:
        json.dump(out, stream, indent=2)
        stream.write("\n")
    if args.out.stat().st_size >= 5_000_000:
        raise ValueError("The targeted field package exceeds the per-file limit")
    print(json.dumps(dict(event="complete", output=str(args.out), cases=len(reports),
        seconds=out["elapsed_seconds"], peak_RSS_KiB=out["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
