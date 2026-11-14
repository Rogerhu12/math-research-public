#!/usr/bin/env python3
"""Recover a COMPLETE oversized outer moment JSON without recomputing it.

Only display strings are dropped. Every other header/row value is hashed
before and after streaming into nine source-segment packages. The complete
R26 parent partition and all exact dyadic width sums are checked again.
This is standard-library serialization and rational bookkeeping only.
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

import closure_split_joint_io as stream


def stripped(value):
    if isinstance(value, dict):
        return {k: stripped(v) for k, v in value.items() if k != "display"}
    if isinstance(value, list):
        return [stripped(v) for v in value]
    return value


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=True)+"\n").encode()


def fraction(endpoint):
    m, e = int(endpoint["mantissa"]), int(endpoint["binary_exponent"])
    return F(m << e, 1) if e >= 0 else F(m, 1 << (-e))


def endpoint(value):
    if value.denominator & (value.denominator-1):
        raise ValueError("A dyadic source endpoint lost its exact denominator")
    return dict(mantissa=str(value.numerator),
                binary_exponent=-(value.denominator.bit_length()-1))


def digest(path):
    return stream.digest(path)


def check_range(record, *, strict, nonnegative_lower=True):
    lo, hi = fraction(record["lower"]), fraction(record["upper"])
    if (not lo <= hi or hi < 0 or (nonnegative_lower and lo < 0)
            or (strict and lo <= 0)):
        raise ValueError("A previously claimed positive interval is not positive")
    return lo, hi


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("input", "radius-ledger", "out-prefix"):
        p.add_argument("--"+name, type=Path, required=True)
    p.add_argument("--rss-limit-mib", type=int, default=100)
    args = p.parse_args()
    began = time.monotonic()
    # The completed oversized file has a .partial suffix but gzip content.
    # This explicitly selects the public reader's opener only in this process;
    # no shared source file or payload value is edited.
    saved_opener = stream.opener
    stream.opener = lambda path: gzip.open(path, "rt")
    header = stream.metadata_without_array(args.input, "panels")
    header = stripped(header)
    n = header["cell"]
    ledger = json.loads(args.radius_ledger.read_text())
    ledger_hash = digest(args.radius_ledger)
    if header["input_hashes"].get(str(args.radius_ledger)) != ledger_hash:
        raise ValueError("The same completed R26 parent ledger is required")
    if not header["mathematical_moments_same_in_every_panel"]:
        raise ValueError("The original common-integral construction is required")
    for item in header["total_positive_moments"].values():
        check_range(item, strict=True)
    cell = next(row for row in ledger["cells"] if row["cell"] == n)
    parents = []
    for s in cell["segments"]:
        for row in s["panels"]:
            parents.append(dict(segment=s["segment"], left=F(row["left"]),
                                right=F(row["right"]), width=stripped(row["width"])))
    parent_state = {i: dict(left=p["left"], count=0, lower=F(0), upper=F(0))
                    for i, p in enumerate(parents)}
    original_hash = hashlib.sha256()
    original_hash.update(canonical(header))
    header_hash = hashlib.sha256(canonical(header)).hexdigest()
    entries, handle = [], None
    count = 0
    last_segment, last_x, last_parent = 0, F(0), 0
    segment_count = 0
    partial_boxes_with_negative_lower = 0

    def resource_check():
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 1024*args.rss_limit_mib:
            raise MemoryError("The pure serialization job exceeded its RSS cap")

    def open_group(segment):
        path = args.out_prefix.with_name(args.out_prefix.name+f"-segment{segment}.json.gz")
        if path.exists():
            raise FileExistsError("Use a fresh segment group name")
        raw = path.open("wb")
        compressed = gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0)
        text = io.TextIOWrapper(compressed, encoding="utf-8")
        small = dict(cell=n, source_segment=segment,
                     original_metadata_sha256=header_hash,
                     scope="All exact non-display row values retained; use the complete cell manifest",
                     panels=[])
        text.write(json.dumps(small, separators=(",", ":"))[:-3]+"[")
        return path, text, raw

    def close_group(state, number):
        path, text, raw = state
        text.write("]}\n")
        text.close()
        raw.close()
        if path.stat().st_size >= 5_000_000:
            raise ValueError("A source-segment package still exceeds5MB")
        entries.append(dict(source_segment=last_segment, path=str(path), panels=number,
                            bytes=path.stat().st_size, sha256=digest(path)))

    try:
        for item in stream.iter_array(args.input, "panels"):
            row = stripped(item)
            segment = row["segment"]
            a, b = F(row["x_left"]), F(row["x_right"])
            if segment != last_segment:
                if not segment == last_segment+1 or not last_x == 1 or not a == 0:
                    raise ValueError("The complete source segment coverage failed")
                close_group(handle, segment_count)
                handle, segment_count = None, 0
                last_segment, last_x = segment, F(0)
            if a != last_x or not a < b <= 1:
                raise ValueError("A source panel gap or overlap was found")
            if handle is None:
                handle = open_group(segment)
            parent = row["original_parent"]
            if parent not in parents_indices(len(parents)) or parent < last_parent or parent > last_parent+1:
                raise ValueError("The original R26 parent indexing changed")
            wanted, status = parents[parent], parent_state[parent]
            if wanted["segment"] != segment or status["left"] != a or not b <= wanted["right"]:
                raise ValueError("A child is not in its stated true parent")
            lower, upper = check_range(row["width"], strict=True)
            status.update(left=b, count=status["count"]+1,
                          lower=status["lower"]+lower, upper=status["upper"]+upper)
            for key in ("radius_left", "radius_right", "radius", "radius_x", "w", "u_x"):
                check_range(row[key], strict=True)
            for key in ("moments", "prefix_moments", "suffix_moments"):
                for value in row[key].values():
                    lower, unused = check_range(value, strict=False, nonnegative_lower=False)
                    partial_boxes_with_negative_lower += int(lower < 0)
            original_hash.update(canonical(row))
            if segment_count:
                handle[1].write(",")
            json.dump(row, handle[1], separators=(",", ":"))
            count += 1
            segment_count += 1
            last_x, last_parent = b, parent
            if count % 128 == 0:
                resource_check()
        if last_segment != 8 or last_x != 1:
            raise ValueError("The complete nine-segment cell was not written")
        close_group(handle, segment_count)
        handle = None
    finally:
        if handle is not None:
            handle[1].close()
            handle[2].close()
        stream.opener = saved_opener
    parent_checks = []
    for i, wanted in enumerate(parents):
        s = parent_state[i]
        lo, hi = check_range(wanted["width"], strict=True)
        if (not s["count"] or s["left"] != wanted["right"]
                or max(lo, s["lower"]) > min(hi, s["upper"])):
            raise ValueError("An exact parent-width sum constraint failed")
        parent_checks.append(dict(parent=i, source_segment=wanted["segment"],
                                  left=str(wanted["left"]), right=str(wanted["right"]),
                                  children=s["count"], original_width=wanted["width"],
                                  sum_child_width=dict(lower=endpoint(s["lower"]),
                                                       upper=endpoint(s["upper"])),
                                  complete_cover=True, sum_intersects_parent=True))
    replay = hashlib.sha256()
    replay.update(canonical(header))
    replay_count = 0
    for entry in entries:
        for row in stream.iter_array(Path(entry["path"]), "panels"):
            replay.update(canonical(stripped(row)))
            replay_count += 1
        resource_check()
    if replay_count != count or replay.hexdigest() != original_hash.hexdigest():
        raise ValueError("An exact non-display value changed during recovery")
    manifest = dict(
        status="Completed oversized outer moment result recovered losslessly except display strings",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", cell=n,
        original_completed_file=dict(path=str(args.input), bytes=args.input.stat().st_size,
                                     sha256=digest(args.input)),
        original_metadata=header, original_metadata_sha256=header_hash,
        exact_nondisplay_payload_sha256=original_hash.hexdigest(),
        exact_nondisplay_replay_sha256=replay.hexdigest(),
        groups=entries, panels=count, parent_constraints=parent_checks,
        checks=dict(all_nine_segments=True, all_parents_covered=True,
                    exact_parent_width_intersections=True,
                    all_five_total_moments_positive=True,
                    all_background_required_ranges_positive=True,
                    all_partial_integral_boxes_ordered=True,
                    all_nondisplay_values_exactly_preserved=True),
        partial_boxes_with_negative_lower=partial_boxes_with_negative_lower,
        partial_integral_domain=(
            "Actual five integrals are nonnegative by their positive source measure and basis. "
            "Some stored hulls extend below zero because Arb union adds radius; these exact "
            "original bounds remain unchanged. A later evaluator may intersect with the "
            "mathematically known nonnegative domain, but must not mistake this for new data."),
        source_sha256=digest(Path(__file__)),
        stream_helper_sha256=digest(Path(stream.__file__)),
        numerical_or_source_recomputation=False,
        continuous_Darboux_defect_paid=False,
        elapsed_seconds=time.monotonic()-began,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out = args.out_prefix.with_name(args.out_prefix.name+"-manifest.json")
    if out.exists():
        raise FileExistsError("Use a fresh manifest name")
    out.write_text(json.dumps(manifest, indent=2)+"\n")
    print(json.dumps(dict(event="complete", manifest=str(out), panels=count,
                          sha256=digest(out), seconds=manifest["elapsed_seconds"],
                          peak_RSS_KiB=manifest["peak_RSS_KiB"])), flush=True)


def parents_indices(count):
    return range(count)


if __name__ == "__main__":
    main()
