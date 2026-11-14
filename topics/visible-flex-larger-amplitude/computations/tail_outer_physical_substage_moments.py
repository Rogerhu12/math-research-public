#!/usr/bin/env python3
"""True physical-r five moments for NEW candidates on saved shooting intervals.

The old source-x candidate supplies only the fixed actual metric, all original
source branch coverage and shared physical endpoint two-jets.  Its five moment
values and bubble coefficients are NOT reused as physical-r moments.  Every
new integral uses u=(r-r_left)/(r_right-r_left), with a certified primitive of
the actual r_x.  Analytic pieces use R85 Taylor composition; unresolved source
branch/sign strips use the full source union and positive range integrals.
All old files are retained.  This entry constructs no ODE solution.
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
from closure_split_joint_io import read, digest
from closure_real_head_green_enclosure import ball
from closure_real_head_source_enclosure import exact_q, ball_record
from closure_real_outer_radius import OuterCell
from tail_r33_middle_ordered_physical import SourceValues
from tail_outer_positive_moment_panels import (
    MOMENT_KEYS, BASIS_CAPS, source_range, positive_hull, Subdivide)
from tail_outer_capped_true_moments import bases
from tail_outer_physical_r_true_moments import integrate_coefficients
from tail_outer_centered_quartic_fields_v2 import finite, intersection
from tail_outer_candidate_domain import nonnegative_integral


EXPECTED = {
    "closure_real_outer_radius.py": "bab793b360f198a34b80fbccf4d725a963bc24f568e782ec9775f20c3925f5fe",
    "tail_r33_middle_ordered_physical.py": "ac1bb495b33a37f7f88b6b7258a88a466c205cb452141668b6c454f88386008e",
    "tail_outer_positive_moment_panels.py": "d5fb54fe3e0e8db26cabe83fbab6c59ef9f085ce98d2ad26afe9453b50a25d9b",
    "tail_outer_capped_true_moments.py": "88ca736fe426fc3aa9d7f09507aba4f11dd80ea7100dcbec346df6d542b53c6b",
    "tail_outer_physical_r_true_moments.py": "67ac79f49c47b4fc0cdef9d145decc955b6b6428c18e56150f3d299d1956c670",
    "tail_outer_centered_quartic_fields_v2.py": "671f6b0c02b3a59dcac79129dc8e73cff4baebe9ec477ee5509e3425f9fb086b",
    "tail_outer_candidate_domain.py": "17d6b7d85be80f8f40b3eec411ae49a73c51c6b624d030df57b94202a7d08690",
}


def pos(value, strict=False):
    value = finite(value)
    return positive_hull(value.lower(), value.upper(), strict=strict)


def unit_interval(value):
    return intersection(finite(value), arb(0).union(arb(1)))


def density_series(cell, segment, base, span, order, kind):
    branch, sign = kind
    x = arb_series([base, span], prec=order + 3)
    logw, unused = cell.profile(segment, x, branch)
    return logw.exp(), span * cell.integrand(segment, x, branch, sign)


def true_width(cell, segment, left, right, order, tolerance, kind, geometry):
    span = exact_q(right - left)
    positive_range = pos(geometry["radius_x"] * span, strict=True)
    if kind is None:
        return positive_range, None
    unused, point = density_series(cell, segment, exact_q(left), span, order, kind)
    unused, derivative = density_series(cell, segment,
        exact_q(left).union(exact_q(right)), span, order, kind)
    width, error = integrate_coefficients(point, derivative, order, tolerance)
    return pos(intersection(width, positive_range), strict=True), error


def physical_moment_series(cell, segment, base, span, offset, width, order, kind):
    w, gx = density_series(cell, segment, base, span, order, kind)
    primitive = arb_series([offset] + [finite(gx[k]) / (k + 1)
        for k in range(order + 1)], prec=order + 3)
    shapes = bases(primitive / width)
    return {key: w * gx * shapes[key] for key in MOMENT_KEYS}


def range_moments(geometry, span, offset_range, width):
    u = unit_interval(offset_range / width)
    shapes = bases(u)
    measure = pos(geometry["w"] * geometry["radius_x"] * span, strict=True)
    result = {}
    for key in MOMENT_KEYS:
        shape = intersection(shapes[key], arb(0).union(exact_q(BASIS_CAPS[key])))
        result[key] = pos(measure * shape)
    return result


def atomic(path, data):
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")
    temporary.replace(path)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ("candidate", "ready", "out-prefix"):
        p.add_argument("--" + key, type=Path, required=True)
    p.add_argument("--first-part", type=int, default=0)
    p.add_argument("--stop-part", type=int, default=8)
    p.add_argument("--order", type=int, default=16)
    p.add_argument("--precision", type=int, default=224)
    p.add_argument("--remainder-bits", type=int, default=48)
    p.add_argument("--max-u-span", default="1/64")
    p.add_argument("--max-rx-ratio", default="2")
    p.add_argument("--max-panels-per-part", type=int, default=8192)
    p.add_argument("--rss-limit-mib", type=int, default=40)
    a = p.parse_args()
    if (not 0 <= a.first_part < a.stop_part <= 8 or a.order < 8
            or a.precision < 192 or a.remainder_bits < 24
            or not 0 < F(a.max_u_span) <= F(1, 16) or F(a.max_rx_ratio) <= 1):
        raise ValueError("Use an explicit finite certified partition and precision")
    summary_path = Path(str(a.out_prefix) + "-summary.json")
    recovery_path = Path(str(a.out_prefix) + "-recovery.json")
    if any(path.exists() for path in (summary_path, recovery_path)):
        raise FileExistsError("Use a fresh physical-substage moment prefix")
    ctx.prec, ctx.cap, ctx.threads = a.precision, a.order + 3, 1
    started = time.monotonic()
    sources = {name: digest(Path(__file__).with_name(name)) for name in EXPECTED}
    if sources != EXPECTED:
        raise ValueError("A frozen actual-source or Taylor dependency changed")
    sources[Path(__file__).name] = digest(__file__)
    inputs = {str(path): digest(path) for path in (a.candidate, a.ready)}
    old, ready = read(a.candidate), read(a.ready)
    if (old["cell"] != 0 or not 0 <= old["segment"] < 8
            or not all(old["gates"].values()) or len(old["nodes"]) != 9
            or len(old["parts"]) != 8 or len(old["bins"]) != 64
            or not old["source_background_unchanged"]
            or not old["all_internal_shared_two_jets"]
            or old["input_hashes"].get(str(a.ready)) != inputs[str(a.ready)]):
        raise ValueError("The complete actual shared-jet source-x candidate is required")
    for path, checksum in old["input_hashes"].items():
        if digest(Path(path)) != checksum:
            raise ValueError("An actual candidate input changed: " + path)
    for name, checksum in old["source_hashes"].items():
        if digest(Path(__file__).with_name(name)) != checksum:
            raise ValueError("An actual candidate source changed: " + name)
    nodes, bins, segment_index = old["nodes"], old["bins"], old["segment"]
    modes, tau = old["modes"], old["tau"]
    original_inputs, original_sources = old["input_hashes"], old["source_hashes"]
    del old
    head = SourceValues(ready)
    head.params = ready["rationalDeepModel"]["physicalParameters"]
    cell = OuterCell(head, 0)
    segment = cell.segments[segment_index]
    tolerance = arb(2) ** (-a.remainder_bits)
    max_u, max_ratio = exact_q(F(a.max_u_span)), exact_q(F(a.max_rx_ratio))
    parts = []
    counts = dict(width_Taylor_leaves=0, complete_union_leaves=0,
        subdivisions=0, moment_refinement_rounds=0, final_panels=0)

    def memory():
        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if peak > 1024 * a.rss_limit_mib:
            raise MemoryError("The physical-substage observed RSS gate was exceeded")
        return peak

    def checkpoint(phase, **extra):
        atomic(recovery_path, dict(status="Completed physical moment parts only; no full candidate claim",
            phase=phase, parts=parts, counts=counts, input_hashes=inputs,
            source_hashes=sources, elapsed_seconds=time.monotonic() - started, **extra))

    try:
        for k in range(a.first_part, a.stop_part):
            left, right = F(k, 8), F(k + 1, 8)
            if (F(nodes[k]["source_x"]) != left or F(nodes[k + 1]["source_x"]) != right):
                raise ValueError("A shared true source endpoint changed")
            rl, rr = ball(nodes[k]["radius"]), ball(nodes[k + 1]["radius"])
            sbins = [row for row in bins if row["part"] == k]
            W = intersection(rr - rl,
                sum((ball(row["values"]["width"]) for row in sbins), arb(0)))
            if not W > 0:
                raise ArithmeticError("The shared physical substage has no positive width")
            initial = []
            at = left
            for binrow in sbins:
                for piece in binrow["source_parts"]:
                    ll, hh = F(piece["left"]), F(piece["right"])
                    if ll != at or not ll < hh <= right:
                        raise ValueError("An original real source branch interval was omitted")
                    initial.append((ll, hh, 0))
                    at = hh
            if at != right:
                raise ValueError("The original real source partition is incomplete")

            def make_row(ll, hh, depth):
                kind = cell.classify(segment, ll, hh)
                g = source_range(cell, segment, ll, hh, kind, exact_q(F(1, 8)))
                if (g["radius_x"].upper() > max_ratio * g["radius_x"].lower()
                        or g["radius_x"].upper() * exact_q(hh - ll) > max_u * W.lower()):
                    raise Subdivide("Refine the actual physical-u range and radial speed")
                width, error = true_width(cell, segment, ll, hh, a.order, tolerance, kind, g)
                return dict(left=ll, right=hh, depth=depth, kind=kind, width=width,
                    width_relative_remainder=error, g=g)

            def refine_entries(entries):
                output, pending = [], list(reversed(entries))
                while pending:
                    ll, hh, depth = pending.pop()
                    try:
                        row = make_row(ll, hh, depth)
                    except (Subdivide, ArithmeticError):
                        if depth >= 80:
                            raise ArithmeticError("The actual physical source partition budget was exhausted")
                        mid = (ll + hh) / 2
                        pending.extend([(mid, hh, depth + 1), (ll, mid, depth + 1)])
                        counts["subdivisions"] += 1
                        continue
                    output.append(row)
                    if len(output) + len(pending) > a.max_panels_per_part:
                        raise ArithmeticError("The physical substage leaf budget was exhausted")
                    memory()
                return output

            rows = refine_entries(initial)
            for round_index in range(24):
                widths = [row["width"] for row in rows]
                pre = [arb(0)]
                for width in widths:
                    pre.append(pre[-1] + width)
                post = [arb(0)] * (len(rows) + 1)
                for i in range(len(rows) - 1, -1, -1):
                    post[i] = post[i + 1] + widths[i]
                W = pos(intersection(W, pre[-1]), strict=True)
                offsets = [arb(0)] + [intersection(pre[i], W - post[i])
                    for i in range(1, len(rows))] + [W]
                failures = []
                for i, row in enumerate(rows):
                    lo, hi = offsets[i:i + 2]
                    row["offset_left"], row["offset_right"] = lo, hi
                    offset_range = pos(positive_hull(lo.lower(), hi.upper()))
                    ll, hh = row["left"], row["right"]
                    if row["kind"] is None:
                        row["moments"] = range_moments(row["g"], exact_q(hh - ll), offset_range, W)
                        row["moment_relative_remainder"] = None
                    else:
                        try:
                            pc = physical_moment_series(cell, segment, exact_q(ll), exact_q(hh - ll),
                                lo, W, a.order, row["kind"])
                            dc = physical_moment_series(cell, segment, exact_q(ll).union(exact_q(hh)),
                                exact_q(hh - ll), offset_range, W, a.order, row["kind"])
                            moments, errors = {}, []
                            for key in MOMENT_KEYS:
                                moments[key], error = integrate_coefficients(pc[key], dc[key], a.order, tolerance)
                                errors.append(error)
                            row["moments"] = moments
                            row["moment_relative_remainder"] = max(errors)
                        except (Subdivide, ArithmeticError):
                            failures.append(i)
                    memory()
                if not failures:
                    break
                marked, next_rows = set(failures), []
                for i, row in enumerate(rows):
                    if i not in marked:
                        next_rows.append(row)
                    else:
                        ll, hh, depth = row["left"], row["right"], row["depth"]
                        mid = (ll + hh) / 2
                        next_rows.extend(refine_entries([(ll, mid, depth + 1), (mid, hh, depth + 1)]))
                rows = next_rows
                if len(rows) > a.max_panels_per_part:
                    raise ArithmeticError("The physical moment refinement budget was exhausted")
                counts["moment_refinement_rounds"] += 1
                checkpoint("physical moment refinement", active_part=k, active_panels=len(rows))
            else:
                raise ArithmeticError("The physical moment Taylor rounds were exhausted")
            totals = {key: sum((row["moments"][key] for row in rows), arb(0)) for key in MOMENT_KEYS}
            if any(not totals[key] > 0 for key in MOMENT_KEYS):
                raise ArithmeticError("A complete physical positive moment has no positive lower endpoint")
            prefix = [{key: arb(0) for key in MOMENT_KEYS}]
            for row in rows:
                prefix.append({key: prefix[-1][key] + row["moments"][key] for key in MOMENT_KEYS})
            suffix = [None] * (len(rows) + 1)
            suffix[-1] = {key: arb(0) for key in MOMENT_KEYS}
            for i in range(len(rows) - 1, -1, -1):
                suffix[i] = {key: suffix[i + 1][key] + rows[i]["moments"][key] for key in MOMENT_KEYS}
            values = []
            for i in range(len(rows) + 1):
                values.append({key: (arb(0) if i == 0 else totals[key] if i == len(rows)
                    else pos(intersection(prefix[i][key], totals[key] - suffix[i][key])))
                    for key in MOMENT_KEYS})
            output = Path(str(a.out_prefix) + f"-part{k:02d}-moments.jsonl.gz")
            if output.exists():
                raise FileExistsError("An actual physical moment primary already exists")
            at = left
            with gzip.open(output, "xt", compresslevel=6) as stream:
                stream.write(json.dumps(dict(kind="header", cell=0, segment=segment_index, part=k,
                    physical_coordinate="u=(r-r_left)/true_width; never native source x",
                    NEW_candidate_moments=True, input_hashes=inputs, source_hashes=sources),
                    separators=(",", ":")) + "\n")
                for i, row in enumerate(rows):
                    if row["left"] != at or not at < row["right"] <= right:
                        raise ValueError("The final true source partition has a gap or overlap")
                    at = row["right"]
                    g, lo, hi = row["g"], row["offset_left"], row["offset_right"]
                    rlo, rhi = intersection(rl + lo, rr - (W - lo)), intersection(rl + hi, rr - (W - hi))
                    ulo = arb(0) if i == 0 else unit_interval(lo / W)
                    uhi = arb(1) if i + 1 == len(rows) else unit_interval(hi / W)
                    u = unit_interval(positive_hull(ulo.lower(), uhi.upper()))
                    kind = row["kind"]
                    counts["complete_union_leaves" if kind is None else "width_Taylor_leaves"] += 1
                    before = {key: pos(positive_hull(values[i][key].lower(), values[i + 1][key].upper()))
                        for key in MOMENT_KEYS}
                    after = {key: pos(positive_hull((totals[key] - values[i + 1][key]).lower(),
                        (totals[key] - values[i][key]).upper())) for key in MOMENT_KEYS}
                    rec = dict(kind="complete_new_physical_substage_moment_leaf", panel=i,
                        source_left=str(row["left"]), source_right=str(row["right"]),
                        branch_sign=kind, complete_branch_union=kind is None,
                        width=ball_record(row["width"]), u=ball_record(u),
                        radius=ball_record(positive_hull(rlo.lower(), rhi.upper(), strict=True)),
                        source_radius_x=ball_record(g["radius_x"]), w=ball_record(g["w"]),
                        log_w_r=ball_record(g["log_w_x"] / g["radius_x"]),
                        moments={key: ball_record(row["moments"][key]) for key in MOMENT_KEYS},
                        prefix_moments={key: ball_record(before[key]) for key in MOMENT_KEYS},
                        suffix_moments={key: ball_record(after[key]) for key in MOMENT_KEYS},
                        width_relative_remainder=(None if row["width_relative_remainder"] is None
                            else ball_record(row["width_relative_remainder"])),
                        moment_relative_remainder=(None if row["moment_relative_remainder"] is None
                            else ball_record(row["moment_relative_remainder"])))
                    stream.write(json.dumps(rec, separators=(",", ":")) + "\n")
                    if i % 64 == 0:
                        memory()
                if at != right:
                    raise ValueError("A physical substage endpoint is absent")
                stream.write(json.dumps(dict(kind="trailer", complete=True, panels=len(rows),
                    source_left=str(left), source_right=str(right)), separators=(",", ":")) + "\n")
            if output.stat().st_size >= 5_000_000:
                raise ArithmeticError("The physical moment primary exceeds the file limit")
            counts["final_panels"] += len(rows)
            parts.append(dict(part=k, source_left=str(left), source_right=str(right),
                panels=len(rows), true_width=ball_record(W),
                total_true_physical_moments={key: ball_record(totals[key]) for key in MOMENT_KEYS},
                original_shared_left_node=k, original_shared_right_node=k + 1,
                complete_branch_union_leaves=sum(row["kind"] is None for row in rows),
                output=str(output), output_sha256=digest(output), bytes=output.stat().st_size))
            checkpoint("complete physical moment part", active_part=k)
            print(json.dumps(dict(event="complete_physical_substage_moments", part=k,
                panels=len(rows), Ib=str(totals["b"]), seconds=time.monotonic() - started,
                peak_RSS_KiB=memory())), flush=True)
            del rows, widths, pre, post, offsets, prefix, suffix, values
    except BaseException as error:
        checkpoint("failed", error=dict(type=type(error).__name__, message=str(error)))
        raise
    result = dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", scope=__doc__,
        status="Complete requested true physical-r moments for NEW shared-jet substage candidates",
        cell=0, segment=segment_index, modes=modes, tau=tau,
        first_part=a.first_part, stop_part=a.stop_part, parts=parts, nodes=nodes, counts=counts,
        parameters=dict(order=a.order, precision=a.precision, remainder_bits=a.remainder_bits,
            max_u_span=a.max_u_span, max_rx_ratio=a.max_rx_ratio,
            max_panels_per_part=a.max_panels_per_part, rss_limit_mib=a.rss_limit_mib),
        gates=dict(complete_requested_source_partition=True, strict_monotone_physical_radius=True,
            full_actual_cap_blend_chi_j0_warp_and_source_retained=True,
            branch_Taylor_only_where_branch_and_sign_proved=True,
            every_unresolved_strip_uses_full_union_positive_range=True,
            true_primitive_composition_and_positive_prefix_suffix=True,
            all_original_shared_physical_two_jets_retained=True,
            physical_five_moments_not_source_x_moments=True),
        whole_segment_moment_cover=a.first_part == 0 and a.stop_part == 8,
        input_hashes=inputs, source_hashes=sources, original_candidate_input_hashes=original_inputs,
        original_candidate_source_hashes=original_sources,
        new_candidate_definition=True, original_source_x_candidate_unchanged_on_disk=True,
        new_radial_ODE_or_Node=False, candidate_R64_or_exact_solution_claimed=False,
        elapsed_seconds=time.monotonic() - started, peak_RSS_KiB=memory())
    with summary_path.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps(dict(event="complete_physical_substage_moments_all", output=str(summary_path),
        counts=counts, gates=result["gates"], seconds=result["elapsed_seconds"],
        peak_RSS_KiB=result["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
