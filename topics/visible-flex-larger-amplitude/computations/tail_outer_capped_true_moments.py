#!/usr/bin/env python3
"""Rigorous branchwise Taylor refinement of the SAME local R48 moments.

This entry uses the actual capped OuterCell profile and warp integrand,
including its recorded calibration and cap transitions. It does not use the
uncapped cells10/11 formula. Native local source x is the Hermite coordinate;
the global-cell moment fields in the old material file are not substituted.
Each original leaf receives the same five true integrals with tighter bounds.
No height candidate, endpoint, metric, radius trajectory or ODE is changed.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import json
from pathlib import Path
import resource
import time

from flint import arb, arb_series, ctx
from closure_real_head_source_enclosure import exact_q, ball_record
from closure_real_head_green_enclosure import ball
from closure_real_outer_radius import OuterCell
from closure_split_joint_io import read, digest, iter_array
from tail_r33_middle_ordered_physical import SourceValues
from tail_outer_segment_candidate_domain import local_moments
from tail_outer_positive_moment_panels import (
    MOMENT_KEYS, BASIS_CAPS, source_range, Subdivide, possible_branches)
from tail_outer_candidate_domain import nonnegative_integral
from tail_outer_centered_quartic_fields_v2 import finite, intersection


EXPECTED = {
    "closure_real_outer_radius.py": "bab793b360f198a34b80fbccf4d725a963bc24f568e782ec9775f20c3925f5fe",
    "tail_r33_middle_ordered_physical.py": "ac1bb495b33a37f7f88b6b7258a88a466c205cb452141668b6c454f88386008e",
    "tail_outer_segment_candidate_domain.py": "836074abfdc5758822633a591d5ed4eb0cdf1aae6d018f486308f20c2330f32f",
    "tail_outer_positive_moment_panels.py": "d5fb54fe3e0e8db26cabe83fbab6c59ef9f085ce98d2ad26afe9453b50a25d9b",
    "tail_outer_centered_quartic_fields_v2.py": "671f6b0c02b3a59dcac79129dc8e73cff4baebe9ec477ee5509e3425f9fb086b",
}


def bases(x):
    y = 1-x
    return dict(zip(MOMENT_KEYS, (y*y*(1+2*x), x*y*y,
        x*x*(3-2*x), x*x*y, x*x*y*y)))


def series(cell, segment, base, span, order, kind):
    x = arb_series([base, span], prec=order+2)
    branch, sign = kind
    logw, unused = cell.profile(segment, x, branch)
    w = logw.exp()
    gx = span*cell.integrand(segment, x, branch, sign)
    phi = bases(x)
    return {"width": gx, **{key: w*gx*phi[key] for key in MOMENT_KEYS}}


def taylor(cell, segment, left, right, order, kind, tolerance):
    x0, span = exact_q(left), exact_q(right-left)
    whole = x0.union(exact_q(right))
    pc = series(cell, segment, x0, span, order, kind)
    dc = series(cell, segment, whole, span, order, kind)
    out, maximum = {}, arb(0)
    for key in ("width",)+MOMENT_KEYS:
        center = sum((finite(pc[key][k])/(k+1) for k in range(order)), arb(0))
        error = (abs(finite(dc[key][order])).upper()/(order+1)).upper()
        value = finite(center+(-error).union(error))
        if not value > 0 or not error < tolerance*value.lower():
            raise Subdivide("Refine the true capped-moment Taylor remainder")
        out[key] = value
        maximum = max(maximum, (error/value.lower()).upper())
    return out, maximum


def unresolved(cell, segment, left, right):
    # The exact measure is nonnegative. The actual source branch/sign union
    # supplies an upper bound on a small strip containing any unresolved root.
    g = source_range(cell, segment, left, right, None, exact_q(F(1, 8)))
    span = exact_q(right-left)
    width = finite((g["radius_x"].upper()*span).upper())
    weighted = finite((g["w"].upper()*width).upper())
    return {"width": nonnegative_integral(ball_record(arb(0).union(width))),
        **{key: nonnegative_integral(ball_record(arb(0).union(
            (weighted*exact_q(BASIS_CAPS[key])).upper()))) for key in MOMENT_KEYS}}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("ready", "cell-manifest", "prior", "out-prefix"):
        p.add_argument("--"+name, type=Path, required=True)
    p.add_argument("--segment", type=int, default=1)
    p.add_argument("--order", type=int, default=16)
    p.add_argument("--precision", type=int, default=224)
    p.add_argument("--remainder-bits", type=int, default=48)
    p.add_argument("--unresolved-bits", type=int, default=120)
    p.add_argument("--max-subpanels", type=int, default=200000)
    p.add_argument("--rss-limit-mib", type=int, default=40)
    a = p.parse_args()
    if not (a.segment == 1 and a.order >= 8 and a.precision >= a.unresolved_bits+64
            and a.remainder_bits >= 24):
        raise ValueError("This first actual capped application is original cell0/segment1")
    summary_path = Path(str(a.out_prefix)+"-summary.json")
    target = Path(str(a.out_prefix)+"-integrals.jsonl.gz")
    recovery = Path(str(a.out_prefix)+"-recovery.json")
    if any(path.exists() for path in (summary_path, target, recovery)):
        raise FileExistsError("Use a fresh actual moment prefix")
    ctx.prec, ctx.cap, ctx.threads = a.precision, a.order+2, 1
    started = time.monotonic()
    source_hashes = {name:digest(Path(__file__).with_name(name)) for name in EXPECTED}
    if source_hashes != EXPECTED:
        raise ValueError("A true mathematical source changed")
    source_hashes[Path(__file__).name] = digest(__file__)
    inputs = {str(path):digest(path) for path in (a.ready, a.cell_manifest, a.prior)}
    ready, material, prior = map(read, (a.ready, a.cell_manifest, a.prior))
    if (material["cell"] != 0 or prior["cell"] != 0
            or not all(material["checks"].values()) or not all(prior["gates"].values())
            or prior["input_hashes"].get(str(a.ready)) != inputs[str(a.ready)]
            or prior["input_hashes"].get(str(a.cell_manifest)) != inputs[str(a.cell_manifest)]):
        raise ValueError("The original same-metric positive measure is required")
    head = SourceValues(ready)
    head.params = ready["rationalDeepModel"]["physicalParameters"]
    cell = OuterCell(head, 0)
    segment = cell.segments[a.segment]
    group = next(g for g in material["groups"] if g["source_segment"] == a.segment)
    old_path = Path(group["path"])
    if digest(old_path) != group["sha256"] or prior["input_hashes"].get(str(old_path)) != group["sha256"]:
        raise ValueError("An original complete source group changed")
    inputs[str(old_path)] = group["sha256"]
    old_total = next(s for s in prior["segments"] if s["segment"] == a.segment)["total_local_positive_moments"]
    tolerance = arb(2)**(-a.remainder_bits)
    tiny = F(1, 2**a.unresolved_bits)
    counts = dict(original_leaves=0, taylor_subpanels=0, unresolved_subpanels=0,
        rejected_taylor=0, branch_subdivisions=0)
    total = {key:arb(0) for key in ("width",)+MOMENT_KEYS}
    root_caps = {key:arb(0) for key in total}
    largest_remainder = arb(0)
    def memory():
        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if peak > 1024*a.rss_limit_mib:
            raise MemoryError("Observed capped-moment RSS exceeded its explicit gate")
        return peak
    def checkpoint(error=None):
        recovery.write_text(json.dumps(dict(status="Completed original leaves only; no final full-piece claim",
            input_hashes=inputs, source_hashes=source_hashes, counts=counts,
            running_total={k:ball_record(v) for k,v in total.items()}, error=error,
            elapsed_seconds=time.monotonic()-started), indent=2)+"\n")
    covered = F(0)
    try:
        with gzip.open(target, "xt", compresslevel=6) as stream:
            stream.write(json.dumps(dict(kind="header", cell=0, segment=a.segment,
                local_R48_coordinate="native original source x, not normalized sum of nine lengths",
                input_hashes=inputs, source_hashes=source_hashes), separators=(",", ":"))+"\n")
            for i, old in enumerate(iter_array(old_path, "panels")):
                left, right = F(old["x_left"]), F(old["x_right"])
                if old["segment"] != a.segment or left != covered or not left < right <= 1:
                    raise ValueError("The original native-source leaves do not cover exactly")
                old_moments = local_moments(old)
                values = {key:arb(0) for key in total}
                accepted = []
                stack = [(left, right, 0)]
                while stack:
                    ll, rr, depth = stack.pop()
                    kind = cell.classify(segment, ll, rr)
                    if kind is None and rr-ll <= tiny:
                        value = unresolved(cell, segment, ll, rr)
                        tag = dict(kind="complete branch/sign union", left=str(ll), right=str(rr))
                        counts["unresolved_subpanels"] += 1
                        for key in root_caps:
                            root_caps[key] += value[key].upper()
                    elif kind is None:
                        mid = (ll+rr)/2
                        stack.extend([(mid,rr,depth+1),(ll,mid,depth+1)])
                        counts["branch_subdivisions"] += 1
                        continue
                    else:
                        try:
                            value, error = taylor(cell, segment, ll, rr, a.order, kind, tolerance)
                            largest_remainder = max(largest_remainder, error)
                        except (Subdivide, ArithmeticError):
                            if depth >= a.unresolved_bits+8:
                                raise ArithmeticError("The true branch Taylor budget was exhausted")
                            mid = (ll+rr)/2
                            stack.extend([(mid,rr,depth+1),(ll,mid,depth+1)])
                            counts["rejected_taylor"] += 1
                            continue
                        tag = dict(kind="branch Taylor", branch=kind[0], sign=kind[1],
                                   left=str(ll), right=str(rr))
                        counts["taylor_subpanels"] += 1
                    accepted.append(tag)
                    for key in values:
                        values[key] += value[key]
                    if counts["taylor_subpanels"]+counts["unresolved_subpanels"] > a.max_subpanels:
                        raise ArithmeticError("The explicit positive quadrature budget was exhausted")
                at = left
                for part in accepted:
                    if F(part["left"]) != at:
                        raise ValueError("The real branch/root partition has a gap or overlap")
                    at = F(part["right"])
                if at != right:
                    raise ValueError("A full old material leaf has not been integrated")
                values["width"] = intersection(finite(values["width"]), ball(old["width"]))
                for key in MOMENT_KEYS:
                    # The original row['moments'] uses global-cell bases.
                    # Only the frozen local_moments definition is the same R48 candidate.
                    values[key] = intersection(finite(values[key]), old_moments[key])
                if any(not value > 0 for value in values.values()):
                    raise ArithmeticError("A whole positive original leaf lacks a strict lower bound")
                for key in total:
                    total[key] += values[key]
                stream.write(json.dumps(dict(kind="complete_true_local_moment_leaf", panel=i,
                    x_left=str(left), x_right=str(right), original_parent=old["original_parent"],
                    width=ball_record(values["width"]),
                    moments={key:ball_record(values[key]) for key in MOMENT_KEYS},
                    true_partition=accepted), separators=(",", ":"))+"\n")
                counts["original_leaves"] += 1
                covered = right
                if i == 0 or (i+1) % 64 == 0:
                    checkpoint()
                    print(json.dumps(dict(event="capped_true_moment_progress", completed=i+1,
                        counts=counts, seconds=time.monotonic()-started, peak_RSS_KiB=memory())), flush=True)
            if covered != 1 or counts["original_leaves"] != group["panels"]:
                raise ValueError("The whole original source piece is incomplete")
            stream.write(json.dumps(dict(kind="complete_true_local_moment_trailer",
                complete_original_piece=True, counts=counts), separators=(",", ":"))+"\n")
    except BaseException as error:
        checkpoint(dict(type=type(error).__name__, message=str(error)))
        raise
    for key in MOMENT_KEYS:
        total[key] = intersection(finite(total[key]), ball(old_total[key]))
    if target.stat().st_size >= 5_000_000:
        raise ArithmeticError("The complete primary exceeds the repository single-file limit")
    result = dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", scope=__doc__,
        status="Complete same true capped local-source moments refined by branch Taylor and positive root strips",
        cell=0, segment=a.segment, counts=counts,
        parameters=dict(order=a.order, precision=a.precision, remainder_bits=a.remainder_bits,
            unresolved_bits=a.unresolved_bits, max_subpanels=a.max_subpanels,
            rss_limit_mib=a.rss_limit_mib),
        input_hashes=inputs, source_hashes=source_hashes,
        output=str(target), output_sha256=digest(target), bytes=target.stat().st_size,
        total_width=ball_record(total["width"]),
        total_local_positive_moments={key:ball_record(total[key]) for key in MOMENT_KEYS},
        old_total_local_positive_moments=old_total,
        full_unresolved_strip_upper={key:ball_record(value.upper()) for key,value in root_caps.items()},
        maximum_relative_Taylor_remainder=ball_record(largest_remainder),
        gates=dict(same_capped_source_and_warp_functions=True,
            complete_original_native_x_leaf_cover=True,
            all_branch_sign_decisions_certified_or_complete_union=True,
            true_ordered_Taylor_derivative_remainders=True,
            every_true_integral_intersects_original_same_local_measure=True,
            all_five_complete_integrals_strictly_positive=True,
            candidate_definition_and_physical_endpoint_data_unchanged=True),
        candidate_mean_defect_or_Green_not_recomputed=True,
        elapsed_seconds=time.monotonic()-started, peak_RSS_KiB=memory())
    with summary_path.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps(dict(event="complete_capped_true_moments", output=str(summary_path),
        counts=counts, Ib=ball_record(total["b"]), gates=result["gates"],
        seconds=result["elapsed_seconds"], peak_RSS_KiB=result["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
