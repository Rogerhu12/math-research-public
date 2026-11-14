#!/usr/bin/env python3
"""Substitute complete tighter audits of identical component candidates.

All arithmetic is exact stdlib Fraction arithmetic.  The complete cell's
original shared physical two-jets, height, metric and scalar mean are retained.
Only physical Darboux upper bounds and their actual covering interval counts
are replaced.  Source-x residuals are never added to physical-r residuals.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import resource
import time


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for data in iter(lambda: stream.read(65536), b""):
            digest.update(data)
    return digest.hexdigest()


def dyadic(value):
    return F(value[0])*F(2)**value[1]


def upper(value):
    x = value["upper"]
    return F(int(x["mantissa"]))*F(2)**int(x["binary_exponent"])


def encoded(value):
    d = value.denominator
    if d & (d-1):
        raise ValueError("Expected an exact dyadic output")
    return [value.numerator, -(d.bit_length()-1)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--audit", type=Path, action="append", required=True)
    parser.add_argument("--stream-check", type=Path, action="append", required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists() or len(args.audit) != len(args.stream_check):
        raise ValueError("Use a new output and one exact stream check per audit")
    started = time.monotonic()
    base = json.loads(args.base.read_text())
    if not all(base["gates"].values()) or base["cell"] != 0:
        raise ValueError("The base must be the complete compatible cell0 candidate")
    hashes = {str(args.base): sha(args.base)}
    for path, checksum in base["input_hashes"].items():
        if sha(path) != checksum:
            raise ValueError("An original component or shared endpoint input changed")
    selected = {}
    for apath, cpath in zip(args.audit, args.stream_check):
        audit, check = (json.loads(path.read_text()) for path in (apath, cpath))
        hashes[str(apath)], hashes[str(cpath)] = sha(apath), sha(cpath)
        if (not all(audit["gates"].values()) or not all(check["gates"].values())
                or not audit["same_exact_candidate_and_background"]
                or not audit["whole_segment_maximum_recomputed"]
                or check["input_hashes"].get(str(apath)) != hashes[str(apath)]
                or audit["segment"] != check["segment"]
                or audit["modes"] != base["modes"] or audit["tau"] != base["tau"]
                or audit["segment"] in selected):
            raise ValueError("A substitution is not a complete same-candidate audit")
        component = next(row for row in base["components"]
                         if row["segment"] == audit["segment"])
        if audit["input_hashes"].get(component["path"]) != component["sha256"]:
            raise ValueError("The new audit did not consume the identical old component")
        for path, checksum in base["original_endpoint_input_hashes"].items():
            if path in audit["original_candidate_input_hashes"] and (
                    audit["original_candidate_input_hashes"][path] != checksum):
                raise ValueError("The true background or original physical field changed")
        selected[audit["segment"]] = (apath, cpath, audit, check)
    components = []
    for old in base["components"]:
        value = upper(old["bounds"]["actual_Darboux_defect_abs"]["value"])
        row = dict(segment=old["segment"], candidate_path=old["path"],
            candidate_sha256=old["sha256"], candidate_definition_unchanged=True,
            physical_Darboux_upper=encoded(value), continuous_panels=old["panels"],
            origin="Unchanged complete component certificate",
            witness=old["bounds"]["actual_Darboux_defect_abs"]["witness"])
        if old["segment"] in selected:
            apath, cpath, audit, check = selected[old["segment"]]
            new = dyadic(check["per_panel_minimum_global_upper"])
            if new < value:
                row.update(physical_Darboux_upper=encoded(new),
                    continuous_panels=check["continuous_panels"],
                    origin="Complete finite-J/R64 same-candidate audit",
                    audit=str(apath), audit_sha256=hashes[str(apath)],
                    exact_stream_check=str(cpath), stream_check_sha256=hashes[str(cpath)],
                    witness=check["witness"])
            else:
                row["audit_did_not_improve_original_complete_bound"] = True
        components.append(row)
    if [r["segment"] for r in components] != list(range(9)):
        raise ValueError("The nine original source segments are not completely covered")
    largest = max(components, key=lambda row: dyadic(row["physical_Darboux_upper"]))
    out = dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", scope=__doc__,
        status="Complete same cell0 candidate with substituted tighter physical audits",
        cell=0, modes=base["modes"], tau=base["tau"], components=components,
        total_continuous_panels=sum(r["continuous_panels"] for r in components),
        full_cell_physical_Darboux_upper=largest["physical_Darboux_upper"],
        largest_bound_segment=largest["segment"], witness=largest["witness"],
        gates=dict(original_complete_candidate_and_shared_physical_two_jets=True,
            all_substitutions_consume_exact_same_component=True,
            all_new_audits_and_exact_stream_checks_complete=True,
            complete_nine_source_segment_cover=True,
            unchanged_complete_mean_definition=True,
            only_common_physical_Darboux_units_compared=True),
        input_hashes=hashes, unchanged_original_input_hashes=base["input_hashes"],
        complete_mean_height=base["complete_mean_height"],
        source_sha256=sha(__file__), new_candidate_or_source_integrals=0,
        exact_outer_solution_or_Green_Schur_certificate=False,
        other_geometry_or_curvature_bounds_recomputed=False,
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with args.out.open("x") as stream:
        json.dump(out, stream, indent=2)
        stream.write("\n")
    print(json.dumps(dict(event="complete_same_candidate_audit_composition",
        panels=out["total_continuous_panels"], full_cell_upper=out["full_cell_physical_Darboux_upper"],
        largest_segment=out["largest_bound_segment"], gates=out["gates"],
        output=str(args.out), peak_RSS_KiB=out["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
