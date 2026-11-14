#!/usr/bin/env python3
"""Refine the continuous audit of the same eight-substage R48 candidate.

No source integral, radial ODE, endpoint jet, bubble, or candidate is changed.
The complete existing positive bins bound the height primitive on each of
their subsets.  Only the real source ranges and polynomial coordinate are
subdivided.  Each accepted interval satisfies the explicit positive r_x
relative-span criterion and the unchanged complete R64 mean/derivative gates.
All complete finite J coefficients through twice the saved height cutoff are
computed, with signed cosine enclosures streamed to one file per substage.
An audit of a finite compatible height is not an exact outer solution.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import json
import os
from pathlib import Path
import resource
import time

from flint import arb, acb, ctx
from closure_split_joint_io import read, digest
from closure_real_head_green_enclosure import ball
from closure_real_head_source_enclosure import exact_q, ball_record
from closure_real_outer_radius import OuterCell
from tail_r33_middle_ordered_physical import SourceValues
from tail_outer_positive_moment_panels import source_range, MOMENT_KEYS, Subdivide
from tail_outer_candidate_domain import nonnegative_integral
from tail_outer_weighted_compatible import (
    intersection, normalized_endpoint_jet, make_weighted_candidate,
    weighted_panel_fields)
from tail_outer_general_mean_bounds import general_mean_and_defect
from tail_r41_connection_polynomial import add, scale, product, derivative


MINIMUM_FIELDS = (
    "mean_sign_margin", "mean_derivative_lower", "real_y_lower", "real_N_lower",
    "real_D_lower", "real_S_lower", "real_L_lower", "Wiener_L_lower")


def rounded_dyadic(value, *, upper, bits=40):
    """Exact directed dyadic encoding; no floating exponent or cutoff."""
    edge = value.upper() if upper else value.lower()
    if not edge.is_finite():
        raise ArithmeticError("A nonfinite value cannot be serialized as evidence")
    m, e = edge.man_exp()
    m, e = int(m), int(e)
    shift = max(0, abs(m).bit_length()-bits)
    unit = 1 << shift
    r = -((-m)//unit) if upper else m//unit
    exponent = e+shift
    encoded = arb(r)*arb(2)**exponent
    if (upper and not encoded >= edge) or (not upper and not encoded <= edge):
        raise AssertionError("Directed dyadic serialization lost its enclosure")
    # Mantissas of 40 bits remain exact in JSON integer consumers as well.
    return [r, exponent]


def compact_ball(value):
    return [rounded_dyadic(value, upper=False),
            rounded_dyadic(value, upper=True)]


def cosine_coefficients(poly, cutoff):
    """Actual fields are real even; intersect both certified Fourier entries."""
    result = {}
    for m in range(0, cutoff+1, 2):
        q = poly.get(m, acb(0))
        if not q.imag.contains(0):
            raise ArithmeticError("The real even candidate lost its Fourier symmetry")
        if m:
            other = poly.get(-m, acb(0))
            if not other.imag.contains(0):
                raise ArithmeticError("A conjugate Fourier coefficient is inconsistent")
            result[m] = 2*intersection(q.real, other.real)
        else:
            result[m] = q.real
    if any(abs(m) > cutoff for m in poly):
        raise AssertionError("An unrecorded finite frequency was produced")
    return result


def cosine_norm(values, weights=None):
    return sum(((arb(1) if weights is None else weights[m])*abs(value)
                for m, value in values.items()), arb(0)).upper()


def finite_complete_J(H, k, kx, *, radius, g, r64, cutoff, weights):
    """Exact R64 numerator, keeping actual k_x and every scalar-mean term."""
    w, rx, ell = g["w"], g["radius_x"], g["log_w_x"]
    z = w*w
    E = 1+z
    P = scale(derivative(H), 1/(radius*w))
    T = derivative(P)
    U = add(derivative(k), scale(P, -1))
    lnm = add(k, scale(T, E))
    linear = add(kx, scale(add(scale(k, 2), T), ell))
    quadratic = add(product(lnm, kx), scale(product(U, U), -E*rx/radius),
        scale(add(product(k, k), scale(product(P, P), z), product(k, T)), ell))
    cmax = r64["bounds"]["complete_mean_abs"].upper()
    cxmax = r64["bounds"]["complete_mean_source_derivative_abs"].upper()
    c, cx = (-cmax).union(cmax), (-cxmax).union(cxmax)
    J = add(linear, quadratic, scale(linear, c), scale(lnm, cx),
            {0: acb(cx*(1+c)+ell*(2*c+c*c))})
    coeffs = cosine_coefficients(J, 2*cutoff)
    # High coefficients do not contain c or c_x, by the exact support identity.
    qcoeffs = cosine_coefficients(quadratic, 2*cutoff)
    for m in range(cutoff+2, 2*cutoff+1, 2):
        coeffs[m] = intersection(coeffs[m], qcoeffs[m])
    groups = {
        "mean": {0: coeffs[0]},
        "retained_nonmean": {m: value for m, value in coeffs.items()
                            if 0 < m <= cutoff},
        "outside_saved_height": {m: value for m, value in coeffs.items()
                                if m > cutoff}}
    factor = z/(radius*rx*E*E)
    values = {
        "complete_J_l1": cosine_norm(coeffs),
        "complete_J_W1_tau": cosine_norm(coeffs, weights),
        "finite_J_l1_Darboux_upper": (factor*cosine_norm(coeffs)).upper()}
    for name, group in groups.items():
        values["finite_J_"+name+"_l1_Darboux_upper"] = (
            factor*cosine_norm(group)).upper()
    Hrr = cosine_coefficients(scale(add(kx, scale(k, ell)), w/rx), cutoff)
    values["signed_actual_nonmean_Hrr_l1"] = cosine_norm(Hrr)
    values["signed_actual_nonmean_Hrr_W1_tau"] = cosine_norm(Hrr, weights)
    return dict(coefficients=coeffs, Hrr=Hrr, bounds=values,
                physical_conversion_factor=factor, c=c, cx=cx)


def update(table, key, value, witness, *, minimum=False):
    edge = value.lower() if minimum else value.upper()
    if key not in table or (
            edge < table[key]["value"] if minimum else edge > table[key]["value"]):
        table[key] = dict(value=edge, witness=witness)


def records(table):
    return {key: dict(value=ball_record(row["value"]), witness=row["witness"])
            for key, row in table.items()}


def atomic_json(path, value):
    temporary = path.with_name(path.name+".tmp")
    with temporary.open("w") as stream:
        json.dump(value, stream, indent=2)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("candidate", "ready", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--rx-ratio", default="2")
    parser.add_argument("--log-w-span", default="1/32")
    parser.add_argument("--u-span", default="1/32")
    parser.add_argument("--first-part", type=int, default=0)
    parser.add_argument("--stop-part", type=int, default=8)
    parser.add_argument("--max-level", type=int, default=28)
    parser.add_argument("--max-panels", type=int, default=100000)
    parser.add_argument("--rss-limit-mib", type=int, default=40)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("Use a fresh same-candidate continuous audit prefix")
    if not 0 <= args.first_part < args.stop_part <= 8:
        raise ValueError("Select complete substages of the eight-part candidate")
    ratio, logspan, uspan = map(F, (args.rx_ratio, args.log_w_span, args.u_span))
    if not ratio > 1 or not 0 < logspan <= F(1, 32) or not 0 < uspan <= F(1, 32):
        raise ValueError("Explicit positive source-span bounds are required")
    ctx.prec = 192
    began = time.monotonic()
    def memory_gate(stage):
        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if rss > 1024*args.rss_limit_mib:
            raise MemoryError("Owned continuous audit exceeded its RSS cap at "+stage)
        return rss
    hashes = {str(path): digest(path) for path in (args.candidate, args.ready)}
    data, ready = map(read, (args.candidate, args.ready))
    if (data["cell"] != 0 or not all(data["gates"].values())
            or data["input_hashes"].get(str(args.ready)) != hashes[str(args.ready)]
            or not data["actual_polynomial_derivative_used_for_all_residuals"]
            or len(data["parts"]) != 8 or len(data["nodes"]) != 9
            or len(data["bins"]) != 64):
        raise ValueError("A complete fixed-source eight-substage candidate is required")
    for name, checksum in data["source_hashes"].items():
        if digest(Path(__file__).with_name(name)) != checksum:
            raise ValueError("An executed candidate dependency changed: "+name)
    modes, tau, j = data["modes"], F(data["tau"]), data["segment"]
    if modes != list(range(2, 41, 2)) or not 0 <= j < 8:
        raise ValueError("This audit retains the actual complete twenty-mode candidate")
    cutoff = max(modes)
    weights = {m: ((1+m)*(exact_q(tau)*m).exp()).upper()
               for m in range(0, 2*cutoff+1, 2)}
    parts, nodes, bins = data["parts"], data["nodes"], data["bins"]
    original_gates = data["gates"]
    original_input_hashes = data["input_hashes"]
    del data
    head = SourceValues(ready)
    head.params = ready["rationalDeepModel"]["physicalParameters"]
    cell = OuterCell(head, 0)
    segment = cell.segments[j]
    source_names = (Path(__file__).name, "tail_outer_general_mean_bounds.py",
        "tail_outer_weighted_compatible.py", "tail_outer_positive_moment_panels.py",
        "tail_outer_candidate_domain.py", "tail_r41_connection_polynomial.py",
        "closure_real_outer_radius.py", "tail_r33_middle_ordered_physical.py")
    sources = {name: digest(Path(__file__).with_name(name)) for name in source_names}
    summary = dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        scope=__doc__, status="Recoverable continuous audit in progress",
        cell=0, segment=j, modes=modes, tau=str(tau),
        first_part=args.first_part, stop_part=args.stop_part,
        parameters=dict(precision_bits=192, rx_upper_lower_ratio=str(ratio),
            log_w_span=str(logspan), normalized_substage_u_span=str(uspan),
            max_level=args.max_level, max_panels=args.max_panels,
            rss_limit_mib=args.rss_limit_mib),
        input_hashes=hashes, original_candidate_input_hashes=original_input_hashes,
        source_hashes=sources, original_candidate_gates=original_gates,
        primitive_enclosure="Same complete saved positive bin prefix/suffix hull on every subset",
        same_exact_candidate_and_background=True, new_source_integrals=0,
        new_radial_ODE_or_Node_or_BVP=False, complete_J_cutoff=2*cutoff,
        complete_mean_and_its_actual_derivative_retained=True,
        accepted_exact_outer_solution=False, parts=[])
    recovery = args.out.with_name(args.out.stem+"-recovery.json")
    if recovery.exists():
        raise FileExistsError("The continuous audit recovery prefix already exists")
    global_bounds, global_minima = {}, {}
    total_leaves = total_subdivisions = 0
    def checkpoint(phase, **extra):
        summary.update(phase=phase, elapsed_seconds=time.monotonic()-began,
            total_accepted_panels=total_leaves, total_subdivisions=total_subdivisions,
            peak_RSS_KiB=memory_gate("checkpoint"),
            bounds=records(global_bounds), minima=records(global_minima), **extra)
        atomic_json(recovery, summary)
    def endpoint(row, h):
        x = F(row["source_x"])
        g = source_range(cell, segment, x, x, None, exact_q(F(1, 8)))
        w = intersection(g["w"], ball(row["w"]))
        ell = intersection(g["log_w_x"], ball(row["wr"])*g["radius_x"]/w)
        jets = {key: {int(m): ball(value) for m, value in
                     row["shared_physical_jets"][key].items()}
                for key in ("H", "Hr", "Hrr")}
        return normalized_endpoint_jet(jets["H"], jets["Hr"], jets["Hrr"], w=w,
            radius_u=exact_q(h)*g["radius_x"], log_w_u=exact_q(h)*ell)
    checkpoint("identity-and-source-checked")
    try:
        for k in range(args.first_part, args.stop_part):
            a, b = F(k, 8), F(k+1, 8)
            h = b-a
            part = parts[k]
            if (part["part"] != k or F(part["left"]) != a or F(part["right"]) != b
                    or F(nodes[k]["source_x"]) != a or F(nodes[k+1]["source_x"]) != b):
                raise ValueError("The saved substage endpoints are not the same interval")
            total = {key: ball(part["total_true_positive_moments"][key])
                     for key in MOMENT_KEYS}
            candidate = make_weighted_candidate(endpoint(nodes[k], h),
                                               endpoint(nodes[k+1], h), total)
            for m, value in candidate["bubble_coefficient"].items():
                candidate["bubble_coefficient"][m] = intersection(
                    value, ball(part["bubble_coefficients"][str(m)]))
            sbins = [row for row in bins if row["part"] == k]
            if len(sbins) != 8:
                raise ValueError("All eight true positive-integral bins are required")
            def sums(indices):
                return {key: sum((ball(sbins[i]["values"][key]) for i in indices), arb(0))
                        for key in ("width", *MOMENT_KEYS)}
            for key in MOMENT_KEYS:
                intersection(total[key], sums(range(8))[key])
            rl, rr = ball(nodes[k]["radius"]), ball(nodes[k+1]["radius"])
            intersection(rr-rl, sums(range(8))["width"])
            output = args.out.with_name(args.out.stem+f"-part{k:02d}.jsonl.gz")
            if output.exists():
                raise FileExistsError("A completed/partial substage stream already exists")
            temporary = output.with_name(output.name+".partial")
            if temporary.exists():
                raise FileExistsError("A recoverable partial substage stream already exists")
            local_bounds, local_minima = {}, {}
            count = 0
            covered_bins = []
            with gzip.open(temporary, "xt", compresslevel=6) as stream:
                header = dict(kind="header", part=k, source_left=str(a), source_right=str(b),
                    input_hashes=hashes, source_hashes=sources,
                    dyadic_encoding="Each [mantissa, exponent] is exact mantissa * 2**exponent; endpoints directed outward at 40 significant bits",
                    complete_J_cosine_modes=list(range(0, 2*cutoff+1, 2)),
                    original_positive_bin_primitive_hulls_retained=True,
                    all_J_coefficients_computed_without_angular_sampling=True,
                    status="Accept only with a matching complete trailer and final summary")
                stream.write(json.dumps(header, separators=(",", ":"))+"\n")
                for v, binrow in enumerate(sbins):
                    lo, hi = F(binrow["left"]), F(binrow["right"])
                    if (binrow["bin"] != v or lo != a+h*F(v, 8)
                            or hi != a+h*F(v+1, 8)):
                        raise ValueError("The true positive-bin partition is not complete")
                    source_parts = binrow["source_parts"]
                    if (F(source_parts[0]["left"]) != lo
                            or F(source_parts[-1]["right"]) != hi
                            or any(x["right"] != y["left"] for x, y in
                                   zip(source_parts, source_parts[1:]))):
                        raise ValueError("An original exact source branch interval was omitted")
                    pl, ph = sums(range(v)), sums(range(v+1))
                    sl, sh = sums(range(v+1, 8)), sums(range(v, 8))
                    def moments(low, high):
                        return {key: nonnegative_integral(ball_record(
                            max(arb(0), low[key].lower()).union(
                                min(high[key].upper(), total[key].upper()))))
                                for key in MOMENT_KEYS}
                    prefix, suffix = moments(pl, ph), moments(sl, sh)
                    rleft = intersection(rl+pl["width"], rr-sh["width"])
                    rright = intersection(rl+ph["width"], rr-sl["width"])
                    radius = rleft.union(rright)
                    pending, covered, bin_count = [(lo, hi, 0)], lo, 0
                    while pending:
                        left, right, level = pending.pop()
                        try:
                            g = source_range(cell, segment, left, right, None,
                                             exact_q(logspan))
                            if (right-left)/h > uspan:
                                raise Subdivide("Refine the unchanged polynomial coordinate")
                            if g["radius_x"].upper() > exact_q(ratio)*g["radius_x"].lower():
                                raise Subdivide("Refine the positive relative span of r_x")
                            u = exact_q((left-a)/h).union(exact_q((right-a)/h))
                            H, K, Kx = weighted_panel_fields(candidate, u=u, u_x=1/exact_q(h),
                                prefix_moments=prefix, suffix_moments=suffix)
                            r64 = general_mean_and_defect(H, K, Kx, modes=modes,
                                weights=weights, radius=radius, radius_x=g["radius_x"],
                                w=g["w"], log_w_x=g["log_w_x"])
                            if not r64["gate"]:
                                raise Subdivide("Retain the original full mean/domain gate: "+r64["failure"])
                        except Subdivide as error:
                            if level >= args.max_level:
                                raise ArithmeticError("Real source/root refinement limit: "+str(error))
                            midpoint = (left+right)/2
                            pending.extend([(midpoint, right, level+1),
                                            (left, midpoint, level+1)])
                            total_subdivisions += 1
                            continue
                        if left != covered:
                            raise AssertionError("Accepted intervals have a gap or overlap in ordered coverage")
                        covered = right
                        full = finite_complete_J(H, K, Kx, radius=radius, g=g,
                                                r64=r64, cutoff=cutoff, weights=weights)
                        witness = dict(segment=j, part=k, bin=v,
                                       source_left=str(left), source_right=str(right))
                        bound_values = dict(r64["bounds"], **full["bounds"],
                            R_tau=(r64["norms"][1]["P"]+r64["norms"][1]["K"]).upper(),
                            actual_rx_upper_lower_ratio=(g["radius_x"].upper()/g["radius_x"].lower()).upper())
                        for key, value in bound_values.items():
                            update(local_bounds, key, value, witness)
                            update(global_bounds, key, value, witness)
                        for key in MINIMUM_FIELDS:
                            update(local_minima, key, r64[key], witness, minimum=True)
                            update(global_minima, key, r64[key], witness, minimum=True)
                        row = dict(kind="accepted_complete_R64_and_J_panel", bin=v,
                            source_left=str(left), source_right=str(right), level=level,
                            source_branches=g["possible_branches"],
                            source={key: compact_ball(value) for key, value in (
                                ("radius", radius), ("radius_x", g["radius_x"]),
                                ("w", g["w"]), ("log_w_x", g["log_w_x"]),
                                ("physical_conversion_factor", full["physical_conversion_factor"]))},
                            bounds_upper={key: rounded_dyadic(value, upper=True)
                                          for key, value in bound_values.items()},
                            gates_lower={key: rounded_dyadic(r64[key], upper=False)
                                         for key in MINIMUM_FIELDS},
                            full_J_cosine_intervals=[compact_ball(full["coefficients"][m])
                                                    for m in range(0, 2*cutoff+1, 2)],
                            same_candidate_complete_mean=True,
                            outside_saved_J_has_no_c_or_cx=True)
                        stream.write(json.dumps(row, separators=(",", ":"))+"\n")
                        count += 1
                        bin_count += 1
                        total_leaves += 1
                        if total_leaves > args.max_panels:
                            raise ArithmeticError("The explicit complete-panel budget was exhausted")
                        if total_leaves % 32 == 0:
                            memory_gate("complete-Fourier-panel")
                    if covered != hi:
                        raise AssertionError("The full source bin was not covered")
                    covered_bins.append(dict(bin=v, left=str(lo), right=str(hi),
                                             accepted_panels=bin_count))
                    stream.flush()
                    checkpoint("complete-bin", active_part=k, complete_active_bins=covered_bins,
                               active_partial_stream=str(temporary))
                trailer = dict(kind="complete_substage_trailer", part=k,
                    complete_source_cover=True, accepted_panels=count,
                    covered_bins=covered_bins, bounds=records(local_bounds),
                    minima=records(local_minima), input_hashes=hashes)
                stream.write(json.dumps(trailer, separators=(",", ":"))+"\n")
            if temporary.stat().st_size >= 5_000_000:
                raise ValueError("Split a substage stream before the per-file size limit")
            temporary.replace(output)
            summary["parts"].append(dict(part=k, left=str(a), right=str(b),
                panels=count, complete_source_cover=True, output=str(output),
                output_sha256=digest(output), bytes=output.stat().st_size,
                bounds=records(local_bounds), minima=records(local_minima)))
            checkpoint("complete-substage", active_partial_stream=None)
            print(json.dumps(dict(event="complete_same_candidate_substage",
                segment=j, part=k, panels=count,
                finite_J_l1_Darboux_upper=ball_record(local_bounds["finite_J_l1_Darboux_upper"]["value"]),
                seconds=time.monotonic()-began, peak_RSS_KiB=memory_gate("part-written"))),
                flush=True)
        complete = args.first_part == 0 and args.stop_part == 8
        summary.update(status="Complete selected-source audit of the identical R48 candidate",
            gates=dict(complete_requested_substage_cover=len(summary["parts"])==args.stop_part-args.first_part,
                complete_original_segment_cover=complete,
                same_candidate_inputs_and_bubbles=True,
                all_original_positive_bins_retained=True,
                all_continuous_mean_and_inverse_domain_gates=True,
                actual_derivatives_and_all_finite_J_modes=True,
                every_rx_relative_span_gate=True),
            whole_segment_maximum_recomputed=complete)
        checkpoint("formal-complete")
        atomic_json(args.out, summary)
        print(json.dumps(dict(event="complete", output=str(args.out), panels=total_leaves,
            gates=summary["gates"], seconds=time.monotonic()-began,
            peak_RSS_KiB=memory_gate("complete-written"))), flush=True)
    except BaseException as error:
        summary.update(status="Incomplete recoverable audit; no new segment certificate",
                       failure=repr(error), whole_segment_maximum_recomputed=False)
        # Preserve existing completed substage files even after a resource gate.
        summary.update(elapsed_seconds=time.monotonic()-began,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            total_accepted_panels=total_leaves, total_subdivisions=total_subdivisions,
            bounds=records(global_bounds), minima=records(global_minima))
        atomic_json(recovery, summary)
        raise


if __name__ == "__main__":
    main()
