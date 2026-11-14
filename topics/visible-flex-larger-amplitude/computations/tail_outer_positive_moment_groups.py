#!/usr/bin/env python3
"""Generate one true outer cell directly as nine compact source groups.

All mathematical source/range/integral routines are imported from the frozen,
actually executed cell11 source. Only serialization is new: omit display
strings, retain every exact endpoint, and replay the complete payload hash.
No deliberately oversized intermediate package is created.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import io
import json
from pathlib import Path
import resource
import time

from flint import ctx
import tail_outer_positive_moment_panels as original
from tail_outer_compact_completed_panels import (
    stripped, canonical, fraction, endpoint, check_range)
from closure_split_joint_io import read, digest, iter_array


EXPECTED_MATH = "d5fb54fe3e0e8db26cabe83fbab6c59ef9f085ce98d2ad26afe9453b50a25d9b"
EXPECTED_SERIALIZER = "51f458147dad592a180aa433dd007501efc2245673fcfaf0d1e76e49e3ac6c2b"


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("ready", "radius-ledger", "out-prefix"):
        p.add_argument("--"+name, type=Path, required=True)
    p.add_argument("--cell", type=int, required=True)
    p.add_argument("--log-span", default="1/8")
    p.add_argument("--u-span", default="1/32")
    p.add_argument("--precision", type=int, default=192)
    p.add_argument("--max-level", type=int, default=40)
    p.add_argument("--max-panels", type=int, default=20000)
    p.add_argument("--rss-limit-mib", type=int, default=120)
    args = p.parse_args()
    n = args.cell
    if not 0 <= n <= 11 or F(args.log_span) <= 0 or not 0 < F(args.u_span) <= 1:
        raise ValueError("A real outer cell and positive source subdivisions are required")
    for name, expected in (("tail_outer_positive_moment_panels.py", EXPECTED_MATH),
                           ("tail_outer_compact_completed_panels.py", EXPECTED_SERIALIZER)):
        if digest(Path(__file__).with_name(name)) != expected:
            raise ValueError("An imported frozen implementation changed: "+name)
    out = args.out_prefix.with_name(args.out_prefix.name+"-manifest.json")
    names = [out]+[args.out_prefix.with_name(args.out_prefix.name+f"-segment{j}.json.gz")
                  for j in range(9)]
    if any(path.exists() for path in names):
        raise FileExistsError("Every cell must use a fresh compact prefix")
    ctx.prec = args.precision
    began = time.monotonic()

    def memory_gate():
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 1024*args.rss_limit_mib:
            raise MemoryError("The compact true-moment job exceeded its stated RSS limit")

    ready, ledger = read(args.ready), read(args.radius_ledger)
    hashes = {str(path): digest(path) for path in (args.ready, args.radius_ledger)}
    if (ledger["status"] != "complete" or not ledger["complete_outer_radius"]
            or ledger["ready_sha256"] != hashes[str(args.ready)]
            or ledger["source_sha256"] != original.EXPECTED_RADIUS_SOURCE
            or ledger["real_head_source_sha256"] != original.EXPECTED_REAL_SOURCE):
        raise ValueError("The exact R26 background/radius identity differs")
    source_names = (
        Path(__file__).name, "tail_outer_positive_moment_panels.py",
        "tail_outer_compact_completed_panels.py", "closure_real_outer_radius.py",
        "closure_real_head_source_enclosure.py", "tail_r33_middle_ordered_physical.py",
        "tail_outer_weighted_compatible.py", "closure_split_joint_io.py")
    source_hashes = {name: digest(Path(__file__).with_name(name)) for name in source_names}
    if (source_hashes["closure_real_outer_radius.py"] != original.EXPECTED_RADIUS_SOURCE
            or source_hashes["closure_real_head_source_enclosure.py"] != original.EXPECTED_REAL_SOURCE):
        raise ValueError("The real source formulas changed")
    head = original.SourceValues(ready)
    head.params = ready["rationalDeepModel"]["physicalParameters"]
    rows = {row["cell"]: row for row in ledger["cells"]}
    if sorted(rows) != list(range(12)):
        raise ValueError("All twelve R26 source cells must anchor the same radii")
    nodes = {12: original.ball(ledger["node12"])}
    for k in range(11, -1, -1):
        nodes[k] = nodes[k+1]+original.ball(rows[k]["width"])
    nodes[0] = original.intersection(nodes[0], original.ball(ledger["outer_radius"]))
    cell = original.OuterCell(head, n)
    leaves, total = original.cell_panels(
        cell, rows[n], nodes[n+1], nodes[n],
        log_span=original.exact_q(F(args.log_span)), u_span=original.exact_q(F(args.u_span)),
        max_level=args.max_level, max_panels=args.max_panels,
        rss_limit_kib=1024*args.rss_limit_mib)
    memory_gate()
    metadata = stripped(dict(
        status="True positive source moments and continuous-background enclosures only",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", cell=n,
        inner_radius=original.ball_record(nodes[n+1]), outer_radius=original.ball_record(nodes[n]),
        total_positive_moments={key: original.ball_record(total[key]) for key in original.MOMENT_KEYS},
        basis_order=list(original.MOMENT_KEYS),
        moment_definition="Integral r_u*w*(q00,q10,q01,-q11,u^2(1-u)^2)du = integral w*basis dr on the same true source",
        coordinate_definition="One normalized unwarped source length across all nine unequal source segments",
        source_range_method="Frozen exact elementary interval ranges, all possible cap branches, positive analytic r_x floor",
        physical_width_method="Same exact R26 parent widths and positive range-times-length subwidth constraints",
        partial_moment_method="Same monotone positive prefix/suffix bounds on every whole panel",
        input_hashes=hashes, source_hashes=source_hashes,
        precision_bits=ctx.prec, log_span=args.log_span, u_span=args.u_span,
        mathematical_moments_same_in_every_panel=True,
        candidate_mean_solved=False, continuous_Darboux_defect_paid=False,
        true_radial_trajectory_enclosed=False, new_ODE_or_binary_quadrature=0, panels=[]))
    for value in metadata["total_positive_moments"].values():
        check_range(value, strict=True)
    metadata_hash = hashlib.sha256(canonical(metadata)).hexdigest()
    payload_hash = hashlib.sha256(canonical(metadata))
    parents = []
    for s in rows[n]["segments"]:
        for row in s["panels"]:
            parents.append(dict(segment=s["segment"], left=F(row["left"]),
                                right=F(row["right"]), width=stripped(row["width"])))
    states = [dict(left=row["left"], count=0, lower=F(0), upper=F(0)) for row in parents]
    groups, count, negative_partial = [], 0, 0
    last_parent = 0
    for j in range(9):
        path = names[j+1]
        group_count, position = 0, F(0)
        with path.open("wb") as raw:
            with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as compressed:
                with io.TextIOWrapper(compressed, encoding="utf-8") as output:
                    header = dict(cell=n, source_segment=j, original_metadata_sha256=metadata_hash,
                                  scope="Every exact non-display mathematical row value retained", panels=[])
                    output.write(json.dumps(header, separators=(",", ":"))[:-3]+"[")
                    while count < len(leaves) and leaves[count]["segment"] == j:
                        row = stripped(original.record_panel(leaves[count]))
                        a, b = F(row["x_left"]), F(row["x_right"])
                        if a != position or not a < b <= 1:
                            raise ValueError("The complete source panel cover has a gap or overlap")
                        parent = row["original_parent"]
                        if parent < last_parent or parent > last_parent+1 or parent >= len(parents):
                            raise ValueError("The R26 parent order changed")
                        wanted, state = parents[parent], states[parent]
                        if wanted["segment"] != j or state["left"] != a or not b <= wanted["right"]:
                            raise ValueError("A true source panel does not belong to its original parent")
                        lo, hi = check_range(row["width"], strict=True)
                        state.update(left=b, count=state["count"]+1,
                                     lower=state["lower"]+lo, upper=state["upper"]+hi)
                        for key in ("radius_left", "radius_right", "radius", "radius_x", "w", "u_x"):
                            check_range(row[key], strict=True)
                        for key in ("moments", "prefix_moments", "suffix_moments"):
                            for value in row[key].values():
                                lo, unused = check_range(value, strict=False, nonnegative_lower=False)
                                negative_partial += int(lo < 0)
                        payload_hash.update(canonical(row))
                        if group_count:
                            output.write(",")
                        json.dump(row, output, separators=(",", ":"))
                        position, last_parent = b, parent
                        count, group_count = count+1, group_count+1
                        if count % 128 == 0:
                            memory_gate()
                    if not group_count or position != 1:
                        raise ValueError("Every one of the nine source segments must be complete")
                    output.write("]}\n")
        if path.stat().st_size >= 5_000_000:
            raise ValueError("One compact source segment still exceeds the repository cap")
        groups.append(dict(source_segment=j, path=str(path), panels=group_count,
                           bytes=path.stat().st_size, sha256=digest(path)))
        print(json.dumps(dict(event="true_outer_source_group", cell=n, **groups[-1],
                              seconds=time.monotonic()-began,
                              peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)), flush=True)
    if count != len(leaves):
        raise ValueError("A complete true panel was not serialized")
    constraints = []
    for i, (wanted, state) in enumerate(zip(parents, states)):
        lo, hi = check_range(wanted["width"], strict=True)
        if (not state["count"] or state["left"] != wanted["right"]
                or max(lo, state["lower"]) > min(hi, state["upper"])):
            raise ValueError("The exact dyadic child-width sum misses its true R26 parent")
        constraints.append(dict(parent=i, source_segment=wanted["segment"],
                                left=str(wanted["left"]), right=str(wanted["right"]),
                                children=state["count"], original_width=wanted["width"],
                                sum_child_width=dict(lower=endpoint(state["lower"]),
                                                     upper=endpoint(state["upper"])),
                                complete_cover=True, sum_intersects_parent=True))
    # Release the computed panels before replaying the compressed serialization.
    del leaves, total, cell
    replay = hashlib.sha256(canonical(metadata))
    replay_count = 0
    for group in groups:
        for row in iter_array(Path(group["path"]), "panels"):
            replay.update(canonical(row))
            replay_count += 1
        memory_gate()
    if replay_count != count or replay.hexdigest() != payload_hash.hexdigest():
        raise ValueError("An exact non-display mathematical value changed in serialization")
    manifest = dict(
        status="True outer positive moments directly saved in nine complete compact groups",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", cell=n,
        original_metadata=metadata, original_metadata_sha256=metadata_hash,
        exact_nondisplay_payload_sha256=payload_hash.hexdigest(),
        exact_nondisplay_replay_sha256=replay.hexdigest(), groups=groups, panels=count,
        parent_constraints=constraints,
        checks=dict(all_nine_segments=True, all_parents_covered=True,
                    exact_parent_width_intersections=True, all_five_total_moments_positive=True,
                    all_background_required_ranges_positive=True,
                    all_partial_integral_boxes_ordered=True,
                    all_nondisplay_values_exactly_preserved=True),
        partial_boxes_with_negative_lower=negative_partial,
        partial_integral_domain="Actual integrals are nonnegative; any original slightly negative Arb hull endpoint is retained exactly and later intersected with the proved domain",
        frozen_mathematical_source_sha256=EXPECTED_MATH, source_sha256=digest(Path(__file__)),
        continuous_Darboux_defect_paid=False, elapsed_seconds=time.monotonic()-began,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out.write_text(json.dumps(manifest, indent=2)+"\n")
    print(json.dumps(dict(event="complete", manifest=str(out), cell=n, panels=count,
                          sha256=digest(out), seconds=manifest["elapsed_seconds"],
                          peak_RSS_KiB=manifest["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
