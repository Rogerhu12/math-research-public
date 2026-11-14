#!/usr/bin/env python3
"""Bounded-memory true outer moments, one R26 parent panel at a time.

The frozen source/range/refinement formulas are unchanged. A first parent
pass computes total moments and parent suffix totals. A second identical
parent pass emits one leaf at a time with valid positive prefix/suffix
enclosures. Source/radius/moment payload hashes must agree between passes.
No complete-cell leaf array or complete-cell prefix/suffix matrix is kept.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import resource
import sys

from flint import arb
import tail_outer_positive_moment_panels as original
import tail_outer_positive_moment_groups as writer
from tail_outer_compact_completed_panels import stripped, canonical
from closure_split_joint_io import digest


EXPECTED_ORIGINAL = "d5fb54fe3e0e8db26cabe83fbab6c59ef9f085ce98d2ad26afe9453b50a25d9b"
EXPECTED_WRITER = "a0575cf86ec70ce3b2f5455b81403a53647c2a574cb66661bf62b24e17278405"
STATS = dict(first_pass_parents=[], second_pass_parents=[],
             both_passes_complete=False, complete_cell_leaf_array_retained=False)


def memory_gate(limit, stage):
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    STATS["peak_RSS_KiB"] = rss
    STATS["last_stage"] = stage
    if rss > limit:
        raise MemoryError("The parent-stream true moments exceeded their owned RSS cap")


def base_record(g):
    """Exactly the old source/radius/moment record, before partial moments."""
    out = dict(segment=g["segment"], x_left=str(g["left"]),
               x_right=str(g["right"]), original_parent=g["original_parent"],
               possible_branches=g["possible_branches"])
    for key in ("width", "radius_left", "radius_right", "radius", "radius_x",
                "w", "log_w", "log_w_x", "u", "u_x"):
        out[key] = stripped(original.ball_record(g[key]))
    out["moments"] = {key: stripped(original.ball_record(g["moments"][key]))
                      for key in original.MOMENT_KEYS}
    return out


class StreamingLeaves:
    """Sequential-index view needed by the unchanged compact serializer."""
    def __init__(self, length, iterator):
        self.length, self.iterator = length, iter(iterator)
        self.index, self.current = -1, None

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if index == self.index:
            return self.current
        if index != self.index+1 or not 0 <= index < self.length:
            raise IndexError("The bounded source stream permits only sequential reads")
        self.current = next(self.iterator)
        self.index = index
        return self.current


def streamed_cell_panels(cell, row, inner, outer, *, log_span, u_span,
                         max_level, max_panels, rss_limit_kib):
    parents = []
    for source in row["segments"]:
        if source["segment"] != len({g["segment"] for g in parents}):
            raise ValueError("R26 source segments are out of order")
        for panel in source["panels"]:
            parents.append(dict(segment=source["segment"], record=panel,
                                width=original.ball(panel["width"])))
    pre = [arb(0)]
    for parent in parents:
        pre.append(pre[-1]+parent["width"])
    post = [arb(0)]*(len(parents)+1)
    for i in range(len(parents)-1, -1, -1):
        post[i] = post[i+1]+parents[i]["width"]
    original.intersection(inner+pre[-1], outer)

    def parent_children(i, remaining):
        parent = parents[i]
        pl = original.intersection(inner+pre[i], outer-post[i])
        pr = original.intersection(inner+pre[i+1], outer-post[i+1])
        children = original.refine_parent(
            cell, cell.segments[parent["segment"]], parent["record"],
            log_span=log_span, u_span=u_span, max_level=max_level,
            max_panels=remaining, rss_limit_kib=rss_limit_kib)
        # basis is no longer used after the original parent width constraint.
        for g in children:
            del g["basis"]
        before = [arb(0)]
        for g in children:
            before.append(before[-1]+g["width"])
        after = [arb(0)]*(len(children)+1)
        for j in range(len(children)-1, -1, -1):
            after[j] = after[j+1]+children[j]["width"]
        for j, g in enumerate(children):
            rl = original.intersection(pl+before[j], pr-after[j])
            rr = original.intersection(pl+before[j+1], pr-after[j+1])
            g.update(radius_left=rl, radius_right=rr,
                     radius=original.positive_hull(rl.lower(), rr.upper(), strict=True),
                     original_parent=i)
        memory_gate(rss_limit_kib, "one-parent-real-ranges")
        return children

    total, counts, expected, reverse_totals = original.zero_moments(), [], [], []
    count = 0
    for i in range(len(parents)):
        children = parent_children(i, max_panels-count)
        fingerprint = hashlib.sha256()
        for g in children:
            total = original.add_moments(total, g["moments"])
            fingerprint.update(canonical(base_record(g)))
        reverse_total = original.zero_moments()
        for g in reversed(children):
            reverse_total = original.add_moments(g["moments"], reverse_total)
        counts.append(len(children))
        count += len(children)
        expected.append(fingerprint.hexdigest())
        reverse_totals.append(reverse_total)
        STATS["first_pass_parents"].append(dict(parent=i, panels=len(children),
            mathematical_payload_sha256=fingerprint.hexdigest()))
        print(json.dumps(dict(event="true_moment_first_parent", cell=cell.n,
            parent=i, source_segment=parents[i]["segment"], panels=len(children),
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)), flush=True)
        del children, g
        memory_gate(rss_limit_kib, "first-parent-released")
    if not all(total[key] > 0 for key in original.MOMENT_KEYS):
        raise ArithmeticError("The same five exact total moments need tighter ranges")
    parent_suffix = [original.zero_moments() for unused in range(len(parents)+1)]
    for i in range(len(parents)-1, -1, -1):
        parent_suffix[i] = original.add_moments(reverse_totals[i], parent_suffix[i+1])
    del reverse_totals

    def leaves():
        prefix, emitted = original.zero_moments(), 0
        for i in range(len(parents)):
            children = parent_children(i, max_panels-emitted)
            if len(children) != counts[i]:
                raise ArithmeticError("The repeated exact parent partition changed")
            suffix = [original.zero_moments() for unused in range(len(children)+1)]
            suffix[-1] = parent_suffix[i+1]
            for j in range(len(children)-1, -1, -1):
                suffix[j] = original.add_moments(children[j]["moments"], suffix[j+1])
            fingerprint = hashlib.sha256()
            for j, g in enumerate(children):
                fingerprint.update(canonical(base_record(g)))
                after = original.add_moments(prefix, g["moments"])
                g["prefix_moments"] = {
                    key: original.positive_hull(prefix[key].lower(), after[key].upper())
                    for key in original.MOMENT_KEYS}
                g["suffix_moments"] = {
                    key: original.positive_hull(suffix[j+1][key].lower(), suffix[j][key].upper())
                    for key in original.MOMENT_KEYS}
                prefix = after
                emitted += 1
                if j+1 == len(children):
                    if fingerprint.hexdigest() != expected[i]:
                        raise ArithmeticError("A real source/radius/moment value changed between passes")
                    STATS["second_pass_parents"].append(dict(parent=i,
                        panels=len(children), mathematical_payload_sha256=fingerprint.hexdigest(),
                        identical_to_first_pass=True))
                    if i+1 == len(parents):
                        STATS["both_passes_complete"] = emitted == count
                memory_gate(rss_limit_kib, "second-parent-partial-moments")
                yield g
                # Once emitted, no full-cell row is retained by this helper.
                children[j] = None
                suffix[j] = None
            del children, suffix, g
        if emitted != count:
            raise ArithmeticError("A real parent leaf was omitted")

    return StreamingLeaves(count, leaves()), total


def main():
    if digest(Path(original.__file__)) != EXPECTED_ORIGINAL:
        raise ValueError("The frozen mathematical source changed")
    if digest(Path(writer.__file__)) != EXPECTED_WRITER:
        raise ValueError("The actually executed compact serializer changed")
    original.cell_panels = streamed_cell_panels
    old_stripped = writer.stripped
    def augmented_metadata(value):
        if (isinstance(value, dict)
                and value.get("status") == "True positive source moments and continuous-background enclosures only"):
            value["source_hashes"][Path(__file__).name] = digest(Path(__file__))
            value["streaming_source_method"] = (
                "Same frozen source/refine_parent/radius constraints, two parent passes; "
                "same ordered forward total; positive suffix sums grouped by actual parent. "
                "The true five integrals and compatible candidate are unchanged; "
                "roundoff enclosures need not be bitwise identical to the all-leaf suffix sum.")
            value["first_pass_parent_payloads"] = STATS["first_pass_parents"]
        return old_stripped(value)
    writer.stripped = augmented_metadata
    failure = None
    try:
        writer.main()
    except BaseException as error:
        failure = dict(type=type(error).__name__, message=str(error))
        raise
    finally:
        if "--out-prefix" in sys.argv:
            prefix = Path(sys.argv[sys.argv.index("--out-prefix")+1])
            out = prefix.with_name(prefix.name+"-streaming-accounting.json")
            if not out.exists():
                out.write_text(json.dumps(dict(
                    status="Actual two-pass source accounting; resource exit and final manifest determine success",
                    source_sha256=digest(Path(__file__)), original_sha256=EXPECTED_ORIGINAL,
                    serializer_sha256=EXPECTED_WRITER, statistics=STATS, failure=failure,
                    new_ODE_or_binary_quadrature=0, exact_radial_solution_claimed=False), indent=2)+"\n")


if __name__ == "__main__":
    main()
