#!/usr/bin/env python3
"""Complete same-candidate finite-Horner/full-J audits of original pieces.

The selected pieces retain the original whole-piece R48 height definition.
The five true integrals, bubble enclosures and shared physical two jets are
reproduced exactly before auditing.  Original true source leaves are reused;
no new source quadrature, radial ODE, BVP or Node calculation is introduced.
Complete mean roots and their actual derivatives use the original R64 gates.
R77 additionally bounds only the zero-frequency defect, retaining all modes.
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
from closure_real_head_green_enclosure import ball
from closure_real_head_source_enclosure import exact_q, ball_record
from closure_real_outer_radius import OuterCell
from closure_split_joint_io import read, digest, iter_array
from tail_r33_middle_ordered_physical import SourceValues
from tail_outer_segment_candidate_domain import local_moments, endpoint as original_endpoint
from tail_outer_positive_moment_panels import MOMENT_KEYS, source_range, add_moments, zero_moments
from tail_outer_weighted_compatible import normalized_endpoint_jet, make_weighted_candidate
from tail_outer_candidate_domain import nonnegative_integral
from tail_outer_centered_quartic_fields_v2 import weighted_panel_fields, finite, intersection
from tail_outer_general_mean_bounds import general_mean_and_defect
from tail_outer_substage_span_refinement import (
    finite_complete_J, MINIMUM_FIELDS, compact_ball, rounded_dyadic)


EXPECTED = {
    "tail_outer_segment_candidate_domain.py": "836074abfdc5758822633a591d5ed4eb0cdf1aae6d018f486308f20c2330f32f",
    "tail_outer_remaining_segment_bounds.py": "f2d937d63d2425023629fd962d6356b373d28166d3d93fedb41791b4130ac765",
    "tail_outer_centered_quartic_fields_v2.py": "671f6b0c02b3a59dcac79129dc8e73cff4baebe9ec477ee5509e3425f9fb086b",
    "tail_outer_substage_span_refinement.py": "85bf30e818e7ab92107a5f5a537225afb9273877327bf6e0092b303b01a1b5d8",
    "tail_outer_general_mean_bounds.py": "4b16b860eb89d7b8f19d7f8ff05642ea0122b0a2016d4be623d5483430023a5c",
}


def endpoint(cell, j, side, node):
    x, segment = F(side), cell.segments[j]
    if cell.classify(segment, x, x) is not None:
        return original_endpoint(cell, j, side, node)
    g = source_range(cell, segment, x, x, None, exact_q(F(1, 8)))
    w = intersection(g["w"], ball(node["w"]))
    ell = intersection(g["log_w_x"], ball(node["wr"])*g["radius_x"]/w)
    jets = {key: {int(m): ball(v) for m, v in node["shared_physical_jets"][key].items()}
            for key in ("H", "Hr", "Hrr")}
    return normalized_endpoint_jet(jets["H"], jets["Hr"], jets["Hrr"],
        w=w, radius_u=g["radius_x"], log_w_u=ell)


def r77(full, r64, w):
    dsmall = min(arb(1), finite(r64["real_D_lower"]).lower())
    emax = (1+w.upper()*w.upper()).upper()
    qD = finite(r64["bounds"]["full_D_nonconstant_W1"]).upper()
    if not dsmall > 0 or not emax >= 1 or not qD >= 0:
        raise ArithmeticError("R77 requires the existing complete real branch")
    coefficient = (arb(3)/2*emax*emax*qD/(dsmall*dsmall*dsmall)).upper()
    b = full["bounds"]
    other = (b["finite_J_retained_nonmean_l1_Darboux_upper"]+
             b["finite_J_outside_saved_height_l1_Darboux_upper"]).upper()
    mean = min(b["finite_J_mean_l1_Darboux_upper"], (coefficient*other).upper())
    return dict(R77_mean_multiplier=coefficient,
        R77_mean_physical_Darboux_upper=mean,
        R77_full_physical_Darboux_upper=min(
            r64["bounds"]["actual_Darboux_defect_abs"],
            b["finite_J_l1_Darboux_upper"], (other+mean).upper()))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("cell-manifest", "nodes", "ready", "prior", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--segments", default="0,1,2,4,6")
    parser.add_argument("--rss-limit-mib", type=int, default=40)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("Use a new complete original-piece audit output")
    selected = list(map(int, args.segments.split(",")))
    if sorted(set(selected)) != selected or not set(selected) <= {0, 1, 2, 4, 6}:
        raise ValueError("Use the original pieces that were not replaced by substage candidates")
    ctx.prec = 192
    start = time.monotonic()
    def memory():
        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if peak > 1024*args.rss_limit_mib:
            raise MemoryError("The original-piece observed RSS gate was exceeded")
        return peak
    source_hashes = {name: digest(Path(__file__).with_name(name)) for name in EXPECTED}
    if source_hashes != EXPECTED:
        raise ValueError("A frozen mathematical input source changed")
    source_hashes[Path(__file__).name] = digest(__file__)
    inputs = {str(p): digest(p) for p in (args.cell_manifest, args.nodes, args.ready, args.prior)}
    material, nodes, ready, prior = map(read, (args.cell_manifest, args.nodes, args.ready, args.prior))
    if (not all(material["checks"].values()) or not all(prior["gates"].values())
            or not nodes["complete_original_segment_node_cover"]
            or not nodes["saved_cut_height_exactly_preserved"]
            or not prior["all_remaining_candidate_coefficient_enclosures_bitwise_checked"]
            or material["cell"] != 0 or nodes["cell"] != 0 or prior["cell"] != 0):
        raise ValueError("The complete original same-candidate background and node records are required")
    for p in (args.cell_manifest, args.nodes, args.ready):
        if prior["input_hashes"].get(str(p)) != inputs[str(p)]:
            raise ValueError("The original candidate input identity changed")
    for name, checksum in prior["source_hashes"].items():
        if digest(Path(__file__).with_name(name)) != checksum:
            raise ValueError("An original candidate dependency changed: "+name)
        source_hashes[name] = checksum
    modes, tau = nodes["modes"], F(nodes["tau"])
    if modes != prior["modes"] or nodes["tau"] != prior["tau"]:
        raise ValueError("The complete angular convention changed")
    weights = {m: ((1+m)*(exact_q(tau)*m).exp()).upper() for m in modes}
    head = SourceValues(ready)
    head.params = ready["rationalDeepModel"]["physicalParameters"]
    cell = OuterCell(head, 0)
    for j in selected:
        group = next(row for row in material["groups"] if row["source_segment"] == j)
        path = Path(group["path"])
        if digest(path) != group["sha256"] or prior["input_hashes"].get(str(path)) != group["sha256"]:
            raise ValueError("A true original material stream changed")
        inputs[str(path)] = group["sha256"]
    records, count = [], 0
    for j in selected:
        group = next(row for row in material["groups"] if row["source_segment"] == j)
        path = Path(group["path"])
        if digest(path) != group["sha256"] or prior["input_hashes"].get(str(path)) != group["sha256"]:
            raise ValueError("A true original material stream changed")
        inputs[str(path)] = group["sha256"]
        moments, total = [], zero_moments()
        for row in iter_array(path, "panels"):
            mm = local_moments(row)
            moments.append(mm)
            total = add_moments(total, mm)
        if len(moments) != group["panels"]:
            raise ValueError("The original positive measure is incomplete")
        suffix = [zero_moments() for unused in range(len(moments)+1)]
        for i in range(len(moments)-1, -1, -1):
            suffix[i] = add_moments(moments[i], suffix[i+1])
        candidate = make_weighted_candidate(endpoint(cell, j, 0, nodes["rows"][j]),
            endpoint(cell, j, 1, nodes["rows"][j+1]), total)
        old = next(row for row in prior["segments"] if row["segment"] == j)
        if ({key: ball_record(v) for key, v in total.items()} != old["total_local_positive_moments"]
                or {str(m): ball_record(v) for m, v in candidate["bubble_coefficient"].items()}
                    != old["bubble_coefficients"]):
            raise ValueError("The original exact candidate coefficient enclosures changed")
        output = args.out.with_name(args.out.stem+f"-segment{j}.jsonl.gz")
        if output.exists():
            raise FileExistsError("Do not overwrite a preserved original-piece stream")
        bounds, minima = {}, {}
        prefix, covered, local = zero_moments(), F(0), 0
        with gzip.open(output, "xt", compresslevel=6) as stream:
            stream.write(json.dumps(dict(kind="header", segment=j, modes=modes,
                complete_J_cosine_modes=list(range(0, 2*max(modes)+1, 2)),
                input_hashes=inputs, source_hashes=source_hashes,
                same_whole_piece_candidate=True), separators=(",", ":"))+"\n")
            for i, g in enumerate(iter_array(path, "panels")):
                left, right = F(g["x_left"]), F(g["x_right"])
                if left != covered or not left < right <= 1:
                    raise ValueError("The true original source leaf cover is incomplete")
                after = add_moments(prefix, moments[i])
                # Preserve the original positive_hull arithmetic before
                # applying the already proved nonnegative-domain intersection.
                from tail_outer_positive_moment_panels import positive_hull
                before_boxes = {key: nonnegative_integral(ball_record(positive_hull(
                    prefix[key].lower(), after[key].upper()))) for key in MOMENT_KEYS}
                after_boxes = {key: nonnegative_integral(ball_record(positive_hull(
                    suffix[i+1][key].lower(), suffix[i][key].upper()))) for key in MOMENT_KEYS}
                H, K, Kx = weighted_panel_fields(candidate,
                    u=exact_q(left).union(exact_q(right)), u_x=arb(1),
                    prefix_moments=before_boxes, suffix_moments=after_boxes)
                geometry = {key: ball(g[key]) for key in ("w", "radius_x", "log_w_x")}
                radius = ball(g["radius"])
                answer = general_mean_and_defect(H, K, Kx, modes=modes, weights=weights,
                    radius=radius, radius_x=geometry["radius_x"], w=geometry["w"],
                    log_w_x=geometry["log_w_x"])
                if not answer["gate"]:
                    raise ArithmeticError("An original candidate full R64 gate failed: "+str((j, i, answer.get("failure"))))
                full = finite_complete_J(H, K, Kx, radius=radius, g=geometry,
                    r64=answer, cutoff=max(modes), weights=weights)
                values = dict(answer["bounds"], **full["bounds"], **r77(full, answer, geometry["w"]))
                witness = dict(segment=j, panel=i, source_left=str(left), source_right=str(right))
                for key, value in values.items():
                    finite(value)
                    if key not in bounds or value.upper() > bounds[key]["value"]:
                        bounds[key] = dict(value=value.upper(), witness=witness)
                for key in MINIMUM_FIELDS:
                    value = finite(answer[key]).lower()
                    if not value > 0:
                        raise ArithmeticError("A real/analytic mean domain margin failed")
                    if key not in minima or value < minima[key]["value"]:
                        minima[key] = dict(value=value, witness=witness)
                row = dict(kind="complete_original_piece_R64_J_R77_leaf", **witness,
                    original_parent=g["original_parent"], same_candidate_complete_mean=True,
                    source={key: compact_ball(value) for key, value in (
                        ("radius", radius), ("radius_x", geometry["radius_x"]),
                        ("w", geometry["w"]), ("log_w_x", geometry["log_w_x"]),
                        ("physical_conversion_factor", full["physical_conversion_factor"]))},
                    bounds_upper={key: rounded_dyadic(value, upper=True) for key, value in values.items()},
                    gates_lower={key: rounded_dyadic(answer[key], upper=False) for key in MINIMUM_FIELDS},
                    full_J_cosine_intervals=[compact_ball(full["coefficients"][m])
                        for m in range(0, 2*max(modes)+1, 2)],
                    actual_nonmean_jet_cosine_intervals={key:[compact_ball(2*v[m].real) for m in modes]
                        for key, v in (("H", H), ("Kbar", K), ("Kbar_x", Kx))})
                stream.write(json.dumps(row, separators=(",", ":"))+"\n")
                prefix, covered = after, right
                moments[i], suffix[i] = None, None
                count += 1
                local += 1
                if count % 32 == 0:
                    memory()
            if covered != 1 or local != group["panels"]:
                raise ValueError("The selected whole original piece was not fully covered")
            stream.write(json.dumps(dict(kind="complete_original_piece_trailer", segment=j,
                panels=local, complete_source_cover=True), separators=(",", ":"))+"\n")
        record = dict(segment=j, panels=local, output=str(output), output_sha256=digest(output),
            original_total_moments_and_bubble_enclosures_identical=True,
            bounds={key:dict(value=ball_record(v["value"]), witness=v["witness"]) for key,v in bounds.items()},
            minima={key:dict(value=ball_record(v["value"]), witness=v["witness"]) for key,v in minima.items()})
        records.append(record)
        print(json.dumps(dict(event="complete_original_piece_finite_J_R77", segment=j,
            panels=local, complete_J_upper=str(bounds["finite_J_l1_Darboux_upper"]["value"]),
            R77_upper=str(bounds["R77_full_physical_Darboux_upper"]["value"]),
            seconds=time.monotonic()-start, peak_RSS_KiB=memory())), flush=True)
        recovery = args.out.with_name(args.out.stem+"-recovery.json")
        recovery.write_text(json.dumps(dict(scope="Completed pieces only; not the final requested full cover",
            input_hashes=inputs, source_hashes=source_hashes, segments=records), indent=2)+"\n")
    complete = [r["segment"] for r in records] == selected
    result = dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", scope=__doc__,
        status="Complete selected original-piece same-candidate finite-J/R77 audit",
        cell=0, modes=modes, tau=str(tau), selected_segments=selected, panels=count, segments=records,
        input_hashes=inputs, source_hashes=source_hashes, precision_bits=192,
        gates=dict(all_requested_original_pieces_complete=complete,
            all_original_total_moments_and_bubbles_identical=True,
            shared_physical_two_jets_and_true_metric_unchanged=True,
            full_R64_mean_and_actual_derivatives_every_leaf=True,
            every_finite_J_mode_retained=True, full_R77_candidate_constraint_every_leaf=True),
        new_source_integrals_or_radial_ODEs=0, exact_outer_solution_or_inverse_claimed=False,
        elapsed_seconds=time.monotonic()-start, peak_RSS_KiB=memory())
    with args.out.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps(dict(event="complete_original_piece_audits", output=str(args.out),
        panels=count, gates=result["gates"], peak_RSS_KiB=result["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
