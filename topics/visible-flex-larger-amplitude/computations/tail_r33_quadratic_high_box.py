#!/usr/bin/env python3
"""Reweight the complete high block with the proved quadratic constants.

The saved real Gamma matrices are unchanged.  R33 16.7 supplies the
complete-source majorant K(t)=3t+1.5t^2+216 A(t+t^2+t^3/3), including
the full mean and pointwise inverse.  The far parameter is allowed to be
independent of the fixed low field, in an explicitly stated R18 ball.
No new ODE, material integration or actual strong-surface solve occurs.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import arb, ctx
from closure_real_head_source_enclosure import ball_record
from closure_real_head_green_enclosure import load_json, ball


def majorant(t, A):
    return (3*t+arb(3)/2*t*t+216*A*(t+t*t+t*t*t/3)).upper()


def derivative(t, A):
    return (3*(1+t)+216*A*(1+t)**2).upper()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("density", "middle", "joint-reference", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--z-log2", type=int, default=-2200)
    parser.add_argument("--infinite-radius-log2", type=int, default=-120)
    args = parser.parse_args()
    ctx.prec = 192
    started = time.monotonic()
    docs, hashes = {}, {}
    for name in ("density", "middle", "joint_reference"):
        path = getattr(args, name)
        docs[name], raw = load_json(path)
        hashes[str(path)] = hashlib.sha256(raw).hexdigest()
    density, middle, previous = (docs[n] for n in
        ("density", "middle", "joint_reference"))
    dhash = hashes[str(args.density)]
    for doc in (middle, previous):
        if dhash not in doc["input_hashes"].values():
            raise ValueError("The actual physical envelope differs")
        if not all(doc["gates"].values()):
            raise ValueError("Use only completely paid input blocks")
    if not all(density["gates"].values()):
        raise ValueError("The density proof has unpaid gates")
    if hashes[str(args.middle)] not in previous["input_hashes"].values():
        raise ValueError("The high residual belongs to another real Gamma package")
    if args.z_log2 > -2200:
        raise ValueError("The chosen R18 full-graph radius has not been paid")
    if args.out.exists():
        raise FileExistsError("Use a fresh output; no old result is overwritten")
    cells = list(range(12, 225))
    dr = {r["cell"]: r for r in density["rows"]}
    mr = {r["cell"]: r for r in middle["cells"]}
    pr = {r["cell"]: r for r in previous["rows"]}
    if sorted(dr) != cells or sorted(mr) != cells or sorted(pr) != cells:
        raise ValueError("All213 source and target cells are required")
    gamma = {(r["output_cell"], s["source_cell"]): ball(s["gamma"])
        for r in middle["gamma_rows"] for s in r["sources"]}
    if len(gamma) != len(cells)*(len(cells)+1)//2:
        raise ValueError("The causal kernel is incomplete")
    A = {n: ball(dr[n]["V_over_w_upper"]) for n in cells}
    ghi = ball(density["gamma_high"])
    h = arb(2)**args.infinite_radius_log2
    far_ratio = arb(2)**(2*(args.z_log2-middle["z_log2"]))
    far = {n: (ball(mr[n]["far_boundary"])*far_ratio).upper() for n in cells}
    pure = {n: ball(pr[n]["refined_low_residual"]) for n in cells}
    base = {n: (pure[n]+far[n]).upper() for n in cells}
    deep = (ball(previous["deep_high_boundary"])*far_ratio).upper()
    pure_inf = ball(previous["wide_low_infinite_residual"])
    radii, slack, images = {}, {}, {}
    failure = None
    for n in reversed(cells):
        c = (base[n]+sum((gamma[n, j]*majorant(radii[j]+h, A[j])
                         for j in range(n+1, 225)), arb(0))).upper()
        value = arb(0)
        for unused in range(256):
            updated = (c+gamma[n, n]*majorant(value+h, A[n])).upper()
            if updated == value:
                break
            if updated > 1:
                break
            value = updated
        radius = (arb(101)/100*updated+arb(2)**-10000).upper()
        image = (c+gamma[n, n]*majorant(radius+h, A[n])).upper()
        if not image < radius or not A[n]*(1+radius+h) < arb(1)/64:
            failure = dict(cell=n, reason="Direct padded interval inclusion or complete mean domain failed",
                           radius=ball_record(radius), image=ball_record(image))
            break
        radii[n], images[n] = radius, image
        slack[n] = (radius-image).lower()
    weights, liprows, slopes = {}, {}, {}
    inf_image = inf_lip = z_column = None
    if failure is None:
        inf_image = (deep+pure_inf+ghi*sum(
            (majorant(radii[n]+h, A[n]) for n in cells), arb(0))).upper()
        slopes = {n: derivative(radii[n]+h, A[n]) for n in cells}
        target = arb(3)/4
        for n in reversed(cells):
            diagonal = gamma[n, n]*slopes[n]
            if not diagonal < target:
                failure = dict(cell=n, reason="Local derivative exceeds the metric target")
                break
            infinite_input = sum((gamma[n, j]*slopes[j]
                                  for j in range(n, 225)), arb(0))
            future = sum((gamma[n, j]*slopes[j]*weights[j]
                          for j in range(n+1, 225)), arb(0))
            weights[n] = max((radii[n]/h).upper(),
                (arb(101)/100*(infinite_input+future)/(target-diagonal)).upper(),
                arb(2)**-10000)
        if failure is None:
            liprows = {n: (sum((gamma[n, j]*slopes[j]*(weights[j]+1)
                              for j in range(n, 225)), arb(0))/weights[n]).upper()
                       for n in cells}
            inf_lip = (ghi*sum((slopes[n]*(weights[n]+1)
                              for n in cells), arb(0))).upper()
            # The independent far metric is |delta z|_38/z_*.
            # Full D'(z) <=4*C_D*z_* on the chosen R18 ball.
            z_column = max([4*deep]+[
                (4*far[n]/weights[n]).upper() for n in cells])
    gates = dict(middle_invariance=failure is None,
        infinite_invariance=inf_image is not None and inf_image < h,
        complete_mean_domain=failure is None,
        middle_metric=bool(liprows) and max(liprows.values()) < arb(3)/4,
        infinite_metric=inf_lip is not None and inf_lip < arb(3)/4)
    rows = []
    for n in cells:
        row = dict(cell=n, pure_low_residual=ball_record(pure[n]),
                   far_boundary=ball_record(far[n]), Astar=ball_record(A[n]))
        if n in radii:
            row.update(radius=ball_record(radii[n]), image=ball_record(images[n]),
                       map_slack=ball_record(slack[n]))
        if n in weights:
            row.update(metric_weight=ball_record(weights[n]),
                       local_full_source_derivative=ball_record(slopes[n]))
        if n in liprows:
            row["weighted_derivative_row"] = ball_record(liprows[n])
        rows.append(row)
    result = dict(status="Complete high response with the exact quadratic/full-remainder source majorant; low feedback remains open",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        independent_far_parameter=True, z_log2=args.z_log2,
        far_metric="|delta z|_38 / 2^z_log2; fixed low field and far parameter are independent inputs",
        complete_mean_and_pointwise_inverse=True,
        source_majorant="K_n(t)=3t+(3/2)t^2+216*A_n*(t+t^2+t^3/3)",
        source_derivative="K'_n(t)=3*(1+t)+216*A_n*(1+t)^2",
        gamma_source=str(args.middle), gamma_unchanged=True,
        low46_held_fixed=True, whole_head_closed=False, rows=rows,
        infinite_radius=ball_record(h),
        infinite_image=ball_record(inf_image) if inf_image is not None else None,
        infinite_weighted_derivative_row=ball_record(inf_lip) if inf_lip is not None else None,
        independent_far_map_column=ball_record(z_column) if z_column else None,
        deep_high_boundary=ball_record(deep), pure_low_infinite_residual=ball_record(pure_inf),
        gates=gates, failure=failure, input_hashes=hashes,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    encoded = (json.dumps(result, indent=2)+"\n").encode()
    if len(encoded) > 1_000_000:
        raise ValueError("Use a compact or gzip ledger if this grows above1MB")
    args.out.write_bytes(encoded)
    ln2 = arb(2).log()
    print(json.dumps(dict(output=str(args.out), gates=gates, failure=failure,
        max_middle_radius_log2=ball_record(max(radii.values()).log()/ln2) if radii else None,
        infinite_image_log2=ball_record(inf_image.log()/ln2) if inf_image is not None else None,
        independent_far_column_log2=ball_record(z_column.log()/ln2) if z_column else None,
        seconds=result["elapsed_seconds"], RSS_KiB=result["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
