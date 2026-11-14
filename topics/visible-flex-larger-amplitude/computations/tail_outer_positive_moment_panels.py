#!/usr/bin/env python3
"""True outer-source panels and the five positive R48 weighted integrals.

R26 certified physical widths anchor every original parent panel.  Finer
panels use elementary interval ranges times positive source length; no
binary quadrature, ODE, or recalibration is used.  Every result concerns
one fixed mathematical source and its same five exact integrals.

This prepares R44 continuous-candidate input.  It does not by itself
enclose a saved trajectory, solve its full mean, or prove a Darboux defect.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import arb, ctx
from closure_real_head_source_enclosure import exact_q, ball_record
from closure_real_head_green_enclosure import ball
from closure_real_outer_radius import OuterCell
from closure_split_joint_io import digest, read
from tail_r33_middle_ordered_physical import SourceValues
from tail_outer_weighted_compatible import (
    MOMENT_KEYS, cell_source_coordinate, positive_basis, intersection)


EXPECTED_RADIUS_SOURCE = "bab793b360f198a34b80fbccf4d725a963bc24f568e782ec9775f20c3925f5fe"
EXPECTED_REAL_SOURCE = "97ff78a171b284cd8d5acc8dc233bcfe1f0b7c428ce2fbbd5b7104bd0ecb8c47"
BASIS_CAPS = {"00": F(1), "10": F(4, 27), "01": F(1),
              "11": F(4, 27), "b": F(1, 16)}


class Subdivide(Exception):
    """An interval range, rather than the exact source, is too wide."""


def positive_hull(lower, upper, strict=False):
    """A nonnegative enclosure, including exact-zero partial integrals.

An Arb hull with a very small positive lower endpoint may round slightly
below zero.  For non-strict quantities a dyadic [0,2^e] hull is a valid
fallback with exactly representable zero, rather than claiming negativity.
"""
    lo, hi = max(arb(0), lower.lower()), upper.upper()
    if not lo <= hi or not hi >= 0:
        raise ArithmeticError("Inconsistent positive range")
    if hi == 0:
        if strict:
            raise Subdivide("A strict positive lower enclosure is unavailable")
        return arb(0)
    ans = lo.union(hi)
    if ans >= 0 and (not strict or ans > 0):
        return ans
    if strict:
        raise Subdivide("A rounded interval obscures true strict positivity")
    m, e = hi.man_exp()
    m, e = int(m), int(e)
    exponent = e+m.bit_length()-(1 if m & (m-1) == 0 else 0)
    return arb(0).union(arb(2)**exponent)


def add_moments(a, b):
    return {key: positive_hull((a[key]+b[key]).lower(),
                              (a[key]+b[key]).upper()) for key in MOMENT_KEYS}


def zero_moments():
    return {key: arb(0) for key in MOMENT_KEYS}


def possible_branches(cell, segment, left, right, recorded):
    if recorded is not None:
        return [(recorded[0], recorded[1])]
    x = exact_q(left).union(exact_q(right))
    raw, unused, cap, unused2 = cell.raw_cap(segment, x)
    z, L = raw-cap, exact_q(cell.p["capTransition"])
    if cell.n == 0 and segment["j"] == 8:
        return [("raw", None)]
    out = []
    if not z > -L:
        out.append(("raw", None))
    if not z < L:
        out.append(("cap", None))
    if not (z < -L or z > L):
        if not z > 0:
            out.append(("transition-low", None))
        if not z < 0:
            out.append(("transition-high", None))
    if not out:
        raise ArithmeticError("No possible exact source branch remains")
    return out


def source_range(cell, segment, left, right, recorded, log_span):
    x = exact_q(left).union(exact_q(right))
    branches = possible_branches(cell, segment, left, right, recorded)
    logw = ell = rx = None
    for branch, sign in branches:
        g, dg = cell.profile(segment, x, branch)
        value = cell.integrand(segment, x, branch, sign)
        logw = g if logw is None else logw.union(g)
        ell = dg if ell is None else ell.union(dg)
        rx = value if rx is None else rx.union(value)
    if not all(v.is_finite() for v in (logw, ell, rx)):
        raise Subdivide("A source formula range is not finite")
    if logw.upper()-logw.lower() > log_span:
        raise Subdivide("Refine the whole-panel logarithmic w range")
    wl, wu = logw.lower().exp().lower(), logw.upper().exp().upper()
    w = positive_hull(wl, wu, strict=True)
    j, head = segment["j"], cell.head
    rox_lo = (segment["length"]*(segment["log_r0"]+
              segment["length"]*exact_q(left)/head.sqrt12).exp()/head.sqrt12).lower()
    if j % 2 == 0:
        weight_lo = cell.weights[j//2].exp().lower()
    else:
        first = (j-1)//2
        weight_lo = min(cell.weights[first].exp().lower(),
                        cell.weights[first+1].exp().lower())
    warp_floor = (head.alpha*weight_lo/(1+wu*wu)).lower()
    if cell.n == 0 and j == 8:
        # r_x/ro_x is a convex combination of j0 and alpha*weight/E,
        # plus a nonnegative curvature term.  Both coefficients are true
        # source quantities; naive interval cancellation is not a zero.
        ratio = exact_q(cell.p["rCut"])/exact_q(cell.p["oldCut"])
        lower = (rox_lo*min(arb(1), ratio.lower(), warp_floor)).lower()
    else:
        lower = (rox_lo*warp_floor).lower()
    rx = positive_hull(max(lower, rx.lower()), rx.upper(), strict=True)
    lengths = [s["length"] for s in cell.segments]
    u, ux = cell_source_coordinate(lengths, j, x)
    # Actual u is in[0,1] by this exact source-coordinate definition.
    u = intersection(u, arb(0).union(arb(1)))
    basis = positive_basis(u)
    basis = {key: positive_hull(max(arb(0), value.lower()),
                                min(value.upper(), exact_q(BASIS_CAPS[key]).upper()))
             for key, value in basis.items()}
    return dict(log_w=logw, log_w_x=ell, w=w, radius_x=rx, u=u, u_x=ux,
                basis=basis, possible_branches=[name for name, unused in branches])


def refine_parent(cell, segment, parent, *, log_span, u_span, max_level, max_panels,
                  rss_limit_kib):
    left, right = F(parent["left"]), F(parent["right"])
    width = ball(parent["width"])
    pending, out = [(left, right, 0)], []
    while pending:
        a, b, level = pending.pop()
        try:
            g = source_range(cell, segment, a, b, parent["branch_sign"], log_span)
            if g["u"].upper()-g["u"].lower() > u_span:
                raise Subdivide("Refine the normalized source-coordinate range")
            if a == left and b == right:
                dw = width
            else:
                raw = g["radius_x"]*exact_q(b-a)
                dw = positive_hull(raw.lower(), min(raw.upper(), width.upper()), strict=True)
            moments = {
                key: positive_hull((dw*g["w"]*g["basis"][key]).lower(),
                                   (dw*g["w"]*g["basis"][key]).upper())
                for key in MOMENT_KEYS}
            out.append(dict(segment=segment["j"], left=a, right=b, width=dw,
                            moments=moments, **g))
            if len(out) % 128 == 0 and resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > rss_limit_kib:
                raise MemoryError("Outer moment subdivision exceeded its stated RSS cap")
            if len(out)+len(pending) > max_panels:
                raise ArithmeticError("Explicit outer panel budget exhausted")
        except Subdivide:
            if level >= max_level:
                raise ArithmeticError("Source range remains unresolved at the subdivision limit")
            middle = (a+b)/2
            pending.extend([(middle, b, level+1), (a, middle, level+1)])
    if out[0]["left"] != left or out[-1]["right"] != right or any(
            a["right"] != b["left"] for a, b in zip(out, out[1:])):
        raise AssertionError("Refined parent panels do not cover the same interval")
    # These constraints all refer to the exact same R26 parent width.
    pre = [arb(0)]
    for g in out:
        pre.append(pre[-1]+g["width"])
    post = [arb(0)]*(len(out)+1)
    for i in range(len(out)-1, -1, -1):
        post[i] = post[i+1]+out[i]["width"]
    intersection(pre[-1], width)
    for i, g in enumerate(out):
        narrowed = intersection(g["width"], width-pre[i]-post[i+1])
        g["width"] = positive_hull(narrowed.lower(), narrowed.upper(), strict=True)
        g["moments"] = {
            key: positive_hull((g["width"]*g["w"]*g["basis"][key]).lower(),
                               (g["width"]*g["w"]*g["basis"][key]).upper())
            for key in MOMENT_KEYS}
    return out


def cell_panels(cell, row, inner, outer, *, log_span, u_span, max_level, max_panels,
                rss_limit_kib):
    parents = []
    for s in row["segments"]:
        if s["segment"] != len({g["segment"] for g in parents}):
            raise ValueError("R26 source segments are out of order")
        for panel in s["panels"]:
            parents.append(dict(segment=s["segment"], record=panel,
                                width=ball(panel["width"])))
    pre = [arb(0)]
    for g in parents:
        pre.append(pre[-1]+g["width"])
    post = [arb(0)]*(len(parents)+1)
    for i in range(len(parents)-1, -1, -1):
        post[i] = post[i+1]+parents[i]["width"]
    intersection(inner+pre[-1], outer)
    leaves = []
    for i, parent in enumerate(parents):
        pl = intersection(inner+pre[i], outer-post[i])
        pr = intersection(inner+pre[i+1], outer-post[i+1])
        children = refine_parent(
            cell, cell.segments[parent["segment"]], parent["record"],
            log_span=log_span, u_span=u_span, max_level=max_level,
            max_panels=max_panels-len(leaves), rss_limit_kib=rss_limit_kib)
        before = [arb(0)]
        for g in children:
            before.append(before[-1]+g["width"])
        after = [arb(0)]*(len(children)+1)
        for j in range(len(children)-1, -1, -1):
            after[j] = after[j+1]+children[j]["width"]
        for j, g in enumerate(children):
            rl = intersection(pl+before[j], pr-after[j])
            rr = intersection(pl+before[j+1], pr-after[j+1])
            g.update(radius_left=rl, radius_right=rr,
                     radius=positive_hull(rl.lower(), rr.upper(), strict=True),
                     original_parent=i)
        leaves.extend(children)
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > rss_limit_kib:
            raise MemoryError("Outer moment cell assembly exceeded its stated RSS cap")
    total = zero_moments()
    for g in leaves:
        total = add_moments(total, g["moments"])
    if not all(total[key] > 0 for key in MOMENT_KEYS):
        raise ArithmeticError("The five full-cell positive moments need tighter ranges")
    suffix = [zero_moments() for unused in range(len(leaves)+1)]
    for i in range(len(leaves)-1, -1, -1):
        suffix[i] = add_moments(leaves[i]["moments"], suffix[i+1])
    prefix = zero_moments()
    for i, g in enumerate(leaves):
        after = add_moments(prefix, g["moments"])
        g["prefix_moments"] = {key: positive_hull(prefix[key].lower(), after[key].upper())
                               for key in MOMENT_KEYS}
        g["suffix_moments"] = {key: positive_hull(suffix[i+1][key].lower(), suffix[i][key].upper())
                               for key in MOMENT_KEYS}
        prefix = after
    return leaves, total


def record_panel(g):
    out = dict(segment=g["segment"], x_left=str(g["left"]), x_right=str(g["right"]),
               original_parent=g["original_parent"], possible_branches=g["possible_branches"])
    for key in ("width", "radius_left", "radius_right", "radius", "radius_x",
                "w", "log_w", "log_w_x", "u", "u_x"):
        out[key] = ball_record(g[key])
    for name in ("moments", "prefix_moments", "suffix_moments"):
        out[name] = {key: ball_record(g[name][key]) for key in MOMENT_KEYS}
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("ready", "radius-ledger", "out-prefix"):
        p.add_argument("--"+name, type=Path, required=True)
    p.add_argument("--first-cell", type=int, default=0)
    p.add_argument("--last-cell", type=int, default=11)
    p.add_argument("--log-span", default="1/8")
    p.add_argument("--u-span", default="1/32")
    p.add_argument("--precision", type=int, default=192)
    p.add_argument("--max-level", type=int, default=40)
    p.add_argument("--max-panels", type=int, default=20000)
    p.add_argument("--rss-limit-mib", type=int, default=120)
    args = p.parse_args()
    if not 0 <= args.first_cell <= args.last_cell <= 11:
        raise ValueError("Only the exact outer twelve cells are covered")
    if F(args.log_span) <= 0 or not 0 < F(args.u_span) <= 1:
        raise ValueError("Use strictly positive log/source-coordinate panel budgets")
    ctx.prec = args.precision
    started = time.monotonic()
    ready, ledger = read(args.ready), read(args.radius_ledger)
    hashes = {str(path): digest(path) for path in (args.ready, args.radius_ledger)}
    if (ledger["status"] != "complete" or not ledger["complete_outer_radius"]
            or ledger["ready_sha256"] != hashes[str(args.ready)]
            or ledger["source_sha256"] != EXPECTED_RADIUS_SOURCE
            or ledger["real_head_source_sha256"] != EXPECTED_REAL_SOURCE):
        raise ValueError("The completed exact R26 source/radius identity differs")
    source_hashes = {name: digest(Path(__file__).with_name(name)) for name in
                    (Path(__file__).name, "closure_real_outer_radius.py",
                     "closure_real_head_source_enclosure.py", "tail_r33_middle_ordered_physical.py",
                     "tail_outer_weighted_compatible.py")}
    if (source_hashes["closure_real_outer_radius.py"] != EXPECTED_RADIUS_SOURCE
            or source_hashes["closure_real_head_source_enclosure.py"] != EXPECTED_REAL_SOURCE):
        raise ValueError("A mathematical source formula changed")
    head = SourceValues(ready)
    head.params = ready["rationalDeepModel"]["physicalParameters"]
    rows = {r["cell"]: r for r in ledger["cells"]}
    if sorted(rows) != list(range(12)):
        raise ValueError("All outer cells are needed to anchor the true radii")
    nodes = {12: ball(ledger["node12"])}
    for n in range(11, -1, -1):
        nodes[n] = nodes[n+1]+ball(rows[n]["width"])
    nodes[0] = intersection(nodes[0], ball(ledger["outer_radius"]))
    entries = []
    for n in range(args.first_cell, args.last_cell+1):
        path = args.out_prefix.with_name(args.out_prefix.name+f"-cell{n:03d}.json.gz")
        temporary = path.with_name(path.name+".partial")
        if path.exists() or temporary.exists():
            raise FileExistsError("Use fresh output names; incomplete prior work must remain visible")
        cell = OuterCell(head, n)
        leaves, total = cell_panels(
            cell, rows[n], nodes[n+1], nodes[n], log_span=exact_q(F(args.log_span)),
            u_span=exact_q(F(args.u_span)), max_level=args.max_level, max_panels=args.max_panels,
            rss_limit_kib=1024*args.rss_limit_mib)
        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if rss > 1024*args.rss_limit_mib:
            raise MemoryError("Outer moment construction exceeded its stated RSS cap")
        meta = dict(status="True positive source moments and continuous-background enclosures only",
                    author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", cell=n,
                    inner_radius=ball_record(nodes[n+1]), outer_radius=ball_record(nodes[n]),
                    total_positive_moments={key: ball_record(total[key]) for key in MOMENT_KEYS},
                    basis_order=list(MOMENT_KEYS),
                    moment_definition="Integral r_u*w*(q00,q10,q01,-q11,u^2(1-u)^2)du = integral w*basis dr on the same true source",
                    coordinate_definition="One normalized unwarped source length across all nine unequal source segments",
                    source_range_method="Exact elementary interval ranges, with all possible cap branches retained and strictly positive analytic r_x floor",
                    physical_width_method="Saved exact R26 parent widths; positive range-times-length subwidths constrained by the same parent total",
                    partial_moment_method="Monotone positive prefix/suffix ranges on each whole panel",
                    input_hashes=hashes, source_hashes=source_hashes,
                    precision_bits=ctx.prec, log_span=args.log_span, u_span=args.u_span,
                    mathematical_moments_same_in_every_panel=True,
                    candidate_mean_solved=False, continuous_Darboux_defect_paid=False,
                    true_radial_trajectory_enclosed=False, new_ODE_or_binary_quadrature=0)
        # Stream JSON rows; no second large serialized copy is retained.
        with gzip.open(temporary, "wt", encoding="utf-8") as f:
            header = json.dumps(meta, separators=(",", ":"))
            f.write(header[:-1]+',"panels":[')
            for i, leaf in enumerate(leaves):
                if i % 256 == 0 and resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 1024*args.rss_limit_mib:
                    raise MemoryError("Outer moment output exceeded its stated RSS cap")
                if i:
                    f.write(",")
                json.dump(record_panel(leaf), f, separators=(",", ":"))
            f.write("]}\n")
        if temporary.stat().st_size >= 5_000_000:
            raise ValueError("One cell package exceeds the per-file repository cap")
        temporary.rename(path)
        item = dict(cell=n, path=str(path), panels=len(leaves), bytes=path.stat().st_size,
                    sha256=digest(path), seconds=time.monotonic()-started, peak_RSS_KiB=rss)
        entries.append(item)
        print(json.dumps(dict(event="outer_moment_cell", **item)), flush=True)
        del leaves, total, cell
    summary = dict(status="Completed stated outer source-moment range; no saved-trajectory or nonlinear defect assertion",
                   cells=entries, input_hashes=hashes, source_hashes=source_hashes,
                   seconds=time.monotonic()-started,
                   peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    path = args.out_prefix.with_name(args.out_prefix.name+"-summary.json")
    if path.exists():
        raise FileExistsError("Use a fresh summary name")
    path.write_text(json.dumps(summary, indent=2)+"\n")
    print(json.dumps(dict(event="completed", summary=str(path), cells=len(entries))), flush=True)


if __name__ == "__main__":
    main()
