#!/usr/bin/env python3
"""Read the completed same-candidate streams and check exact coverage.

Only stdlib integers/Fractions are used.  This does not repeat the Arb source
evaluation.  It verifies the preserved stream hashes, all source intervals,
positive recorded root/denominator bounds, the complete signed finite
spectrum, and a per-panel minimum of the two separately valid physical
defect bounds.  All directed dyadics remain exact.
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


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def dyadic(value):
    if (not isinstance(value, list) or len(value) != 2
            or any(not isinstance(v, int) for v in value)):
        raise ValueError("A directed dyadic must be [integer mantissa, exponent]")
    return F(value[0])*F(2)**value[1]


def pair(value):
    lower, upper = map(dyadic, value)
    if lower > upper:
        raise ValueError("An interval has reversed endpoints")
    return lower, upper


def encode(value):
    denominator = value.denominator
    if denominator & (denominator-1):
        raise ValueError("The exact output is not dyadic")
    return [value.numerator, -(denominator.bit_length()-1)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", type=Path, required=True)
    parser.add_argument("--resource", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("Use a new exact stream-check output")
    started = time.monotonic()
    summary = json.loads(args.summary.read_text())
    execution = json.loads(args.resource.read_text())
    if (not all(summary["gates"].values()) or not summary["whole_segment_maximum_recomputed"]
            or execution["exitcode"] != 0 or execution["termination_signal"] is not None
            or summary["first_part"] != 0 or summary["stop_part"] != 8):
        raise ValueError("A formally completed whole-segment stream is required")
    files = {str(args.summary): sha(args.summary), str(args.resource): sha(args.resource)}
    mode_list = list(range(0, summary["complete_J_cutoff"]+1, 2))
    total_count = 0
    all_parts = []
    global_best = (F(-1), None)
    global_ratio = F(0)
    for k, part in enumerate(summary["parts"]):
        path = Path(part["output"])
        if k != part["part"] or sha(path) != part["output_sha256"]:
            raise ValueError("The completed stream order or SHA changed")
        files[str(path)] = part["output_sha256"]
        a, b = F(k, 8), F(k+1, 8)
        covered = a
        count = 0
        part_best = (F(-1), None)
        seen_header = seen_trailer = False
        per_bin = [0]*8
        with gzip.open(path, "rt") as stream:
            for line in stream:
                row = json.loads(line)
                kind = row["kind"]
                if kind == "header":
                    if (seen_header or count or row["part"] != k
                            or row["input_hashes"] != summary["input_hashes"]
                            or row["source_hashes"] != summary["source_hashes"]
                            or row["complete_J_cosine_modes"] != mode_list):
                        raise ValueError("A complete finite spectrum header changed")
                    seen_header = True
                elif kind == "accepted_complete_R64_and_J_panel":
                    if not seen_header or seen_trailer:
                        raise ValueError("A continuous record is outside its header/trailer")
                    left, right, v = F(row["source_left"]), F(row["source_right"]), row["bin"]
                    if (not 0 <= v < 8 or left != covered or not left < right
                            or not a+F(v, 64) <= left < right <= a+F(v+1, 64)):
                        raise ValueError("The accepted intervals do not cover their exact saved bin")
                    if not row["same_candidate_complete_mean"] or not row["outside_saved_J_has_no_c_or_cx"]:
                        raise ValueError("The complete mean or finite-band identity is absent")
                    rxlo, rxhi = pair(row["source"]["radius_x"])
                    if not rxlo > 0 or rxhi/rxlo > F(summary["parameters"]["rx_upper_lower_ratio"]):
                        raise ValueError("The outward stored r_x interval fails its relative-span gate")
                    global_ratio = max(global_ratio, rxhi/rxlo)
                    if any(dyadic(value) <= 0 for value in row["gates_lower"].values()):
                        raise ValueError("A complete mean or denominator gate is nonpositive")
                    if len(row["full_J_cosine_intervals"]) != len(mode_list):
                        raise ValueError("A retained or outside-height finite J coefficient is missing")
                    for coefficient in row["full_J_cosine_intervals"]:
                        pair(coefficient)
                    bounds = row["bounds_upper"]
                    old = dyadic(bounds["actual_Darboux_defect_abs"])
                    full = dyadic(bounds["finite_J_l1_Darboux_upper"])
                    if old < 0 or full < 0:
                        raise ValueError("A physical absolute bound is negative")
                    best = min(old, full)
                    witness = dict(segment=summary["segment"], part=k, bin=v,
                                   source_left=str(left), source_right=str(right),
                                   selected_bound="R64" if old <= full else "complete finite J",
                                   R64_upper=encode(old), complete_J_upper=encode(full))
                    if best > part_best[0]:
                        part_best = (best, witness)
                    if best > global_best[0]:
                        global_best = (best, witness)
                    covered = right
                    per_bin[v] += 1
                    count += 1
                elif kind == "complete_substage_trailer":
                    if (seen_trailer or not row["complete_source_cover"]
                            or row["part"] != k or row["accepted_panels"] != count
                            or row["input_hashes"] != summary["input_hashes"]):
                        raise ValueError("The substage trailer did not match its actual stream")
                    seen_trailer = True
                else:
                    raise ValueError("Unknown stream record")
        if not (seen_header and seen_trailer and covered == b
                and count == part["panels"] and min(per_bin) > 0):
            raise ValueError("A substage or a saved positive bin is incomplete")
        total_count += count
        all_parts.append(dict(part=k, left=str(a), right=str(b), accepted_panels=count,
            panels_by_bin=per_bin, per_panel_minimum_global_upper=encode(part_best[0]),
            witness=part_best[1]))
    if total_count != summary["total_accepted_panels"]:
        raise ValueError("The complete segment count differs from its preserved summary")
    result = dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", scope=__doc__,
        status="Exact stored-evidence coverage checks passed",
        input_hashes=files, source_sha256=sha(__file__),
        formal_numerical_resource=args.resource.as_posix(),
        cell=summary["cell"], segment=summary["segment"],
        complete_parts=8, complete_positive_bins=64, continuous_panels=total_count,
        parts=all_parts, per_panel_minimum_global_upper=encode(global_best[0]),
        witness=global_best[1],
        actual_stored_rx_ratio_max_exact_fraction=str(global_ratio),
        gates=dict(formal_actual_exit0=True, all_stream_hashes_match=True,
            exact_complete_source_cover=True, all_original_bins_present=True,
            all_stored_positive_root_and_inverse_margins=True,
            full_signed_cosine_spectrum_to_twice_height_cutoff=True,
            all_stored_relative_rx_span_gates=True,
            two_valid_physical_bounds_minimized_only_on_same_panel=True),
        new_Arb_or_source_evaluations=0, accepted_exact_outer_solution=False,
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with args.out.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps(dict(event="complete_stream_check", panels=total_count,
        gates=result["gates"], output=str(args.out),
        maximum_exact_dyadic=result["per_panel_minimum_global_upper"],
        peak_RSS_KiB=result["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
