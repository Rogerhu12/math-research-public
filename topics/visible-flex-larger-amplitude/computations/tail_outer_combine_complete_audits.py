#!/usr/bin/env python3
"""Compose completed original-piece and R77 bounds of identical candidates.

Only exact stdlib Fractions and saved records are used. All original shared
physical jets, height, full mean and metric are retained. Every newly used
original-piece leaf is checked; no source-x and physical-r units are mixed.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import json
from pathlib import Path
import resource
import time

from tail_outer_span_stream_check import sha, dyadic, pair, encode


def load(path):
    with (gzip.open(path, "rt") if path.suffix == ".gz" else path.open()) as stream:
        return json.load(stream)


def actual(path, resource_path):
    data, usage = load(path), load(resource_path)
    if (usage["exitcode"] != 0 or usage["termination_signal"] is not None
            or str(path) not in usage["command"] or not all(data["gates"].values())):
        raise ValueError("A formally completed audit is required")
    for name, checksum in data["input_hashes"].items():
        if sha(name) != checksum:
            raise ValueError("A complete audit input changed: "+name)
    if "source_hashes" in data:
        for name, checksum in data["source_hashes"].items():
            if sha(Path(__file__).with_name(name)) != checksum:
                raise ValueError("An actual numerical source changed: "+name)
    return data


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--base", type=Path, required=True)
    p.add_argument("--piece-audit", type=Path, action="append", default=[])
    p.add_argument("--piece-resource", type=Path, action="append", default=[])
    p.add_argument("--mean-audit", type=Path, action="append", default=[])
    p.add_argument("--mean-resource", type=Path, action="append", default=[])
    p.add_argument("--out", type=Path, required=True)
    a = p.parse_args()
    if (a.out.exists() or len(a.piece_audit) != len(a.piece_resource)
            or len(a.mean_audit) != len(a.mean_resource)):
        raise ValueError("Use a fresh output and one formal resource per audit")
    started = time.monotonic()
    base = load(a.base)
    if not all(base["gates"].values()) or base["cell"] != 0:
        raise ValueError("A completed whole-cell candidate is required")
    for name, checksum in base["input_hashes"].items():
        if sha(name) != checksum:
            raise ValueError("A base candidate audit changed")
    components = [dict(row) for row in base["components"]]
    if [row["segment"] for row in components] != list(range(9)):
        raise ValueError("All nine original pieces must be represented")
    inputs = {str(a.base): sha(a.base)}
    replacements = []
    for audit_path, usage_path in zip(a.piece_audit, a.piece_resource):
        data = actual(audit_path, usage_path)
        inputs[str(audit_path)], inputs[str(usage_path)] = sha(audit_path), sha(usage_path)
        if data["modes"] != base["modes"] or data["tau"] != base["tau"] or data["cell"] != 0:
            raise ValueError("A complete angular convention changed")
        for part in data["segments"]:
            j = part["segment"]
            old = components[j]
            if (not part["original_total_moments_and_bubble_enclosures_identical"]
                    or data["input_hashes"].get(old["candidate_path"]) != old["candidate_sha256"]):
                raise ValueError("An original-piece audit changed its exact candidate")
            path = Path(part["output"])
            if sha(path) != part["output_sha256"]:
                raise ValueError("An original-piece primary stream changed")
            inputs[str(path)] = part["output_sha256"]
            covered, count, maximum, witness = F(0), 0, F(-1), None
            header = trailer = False
            with gzip.open(path, "rt") as stream:
                for line in stream:
                    row = json.loads(line)
                    if row["kind"] == "header":
                        if (header or count or row["segment"] != j
                                or row["source_hashes"] != data["source_hashes"]
                                or row["input_hashes"] != data["input_hashes"]
                                or row["complete_J_cosine_modes"] != list(range(0, 2*max(data["modes"])+1, 2))):
                            raise ValueError("A complete original-piece header changed")
                        header = True
                        continue
                    if row["kind"] == "complete_original_piece_trailer":
                        if trailer or not row["complete_source_cover"] or row["panels"] != count:
                            raise ValueError("The whole-piece trailer is incomplete")
                        trailer = True
                        continue
                    if row["kind"] != "complete_original_piece_R64_J_R77_leaf" or not header or trailer:
                        raise ValueError("Unknown original-piece primary record")
                    left, right = F(row["source_left"]), F(row["source_right"])
                    if row["panel"] != count or row["segment"] != j or left != covered or not left < right <= 1:
                        raise ValueError("The original source cover is not exact and complete")
                    if (not row["same_candidate_complete_mean"]
                            or any(dyadic(v) <= 0 for v in row["gates_lower"].values())
                            or len(row["full_J_cosine_intervals"]) != max(data["modes"])+1):
                        raise ValueError("A complete mean, inverse or finite-mode gate failed")
                    for value in row["full_J_cosine_intervals"]:
                        pair(value)
                    b = row["bounds_upper"]
                    value = min(dyadic(b[key]) for key in (
                        "actual_Darboux_defect_abs", "finite_J_l1_Darboux_upper", "R77_full_physical_Darboux_upper"))
                    if value < 0:
                        raise ValueError("A physical absolute bound is negative")
                    if value > maximum:
                        maximum = value
                        witness = dict(segment=j, panel=count, source_left=str(left), source_right=str(right))
                    covered, count = right, count+1
            if not header or not trailer or covered != 1 or count != part["panels"]:
                raise ValueError("An original whole piece is missing")
            if maximum < dyadic(old["physical_Darboux_upper"]):
                old.update(physical_Darboux_upper=encode(maximum), continuous_panels=count,
                    origin="Same original candidate complete finite-Horner/full-J/R77 audit",
                    audit=str(audit_path), audit_sha256=inputs[str(audit_path)],
                    resource=str(usage_path), resource_sha256=inputs[str(usage_path)], witness=witness)
            replacements.append(dict(kind="complete original piece", segment=j, all_leaves_checked=count,
                whole_piece_upper=encode(maximum)))
    for audit_path, usage_path in zip(a.mean_audit, a.mean_resource):
        data = actual(audit_path, usage_path)
        inputs[str(audit_path)], inputs[str(usage_path)] = sha(audit_path), sha(usage_path)
        j = data["segment"]
        old = components[j]
        if (data["cell"] != 0 or data["modes"] != base["modes"] or data["tau"] != base["tau"]
                or data["input_hashes"].get(old.get("audit")) != old.get("audit_sha256")
                or data["continuous_panels"] != old["continuous_panels"]):
            raise ValueError("An R77 result does not concern the same complete component audit")
        value = dyadic(data["full_segment_physical_Darboux_upper"])
        if value < dyadic(old["physical_Darboux_upper"]):
            old.update(physical_Darboux_upper=encode(value),
                origin="Same complete candidate audit with exact rational R77 zero-mode constraint",
                mean_constraint_audit=str(audit_path), mean_constraint_sha256=inputs[str(audit_path)],
                mean_constraint_resource=str(usage_path), witness=dict(segment=j, **data["witness"]))
        replacements.append(dict(kind="full-leaf R77 postprocessing", segment=j,
            all_leaves_checked=data["continuous_panels"], whole_piece_upper=encode(value)))
    largest = max(components, key=lambda r: dyadic(r["physical_Darboux_upper"]))
    result = dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", scope=__doc__,
        status="Complete same cell0 candidate with actual original-piece and full-mean audits",
        cell=0, modes=base["modes"], tau=base["tau"], components=components,
        total_continuous_panels=sum(row["continuous_panels"] for row in components),
        full_cell_physical_Darboux_upper=largest["physical_Darboux_upper"],
        largest_bound_segment=largest["segment"], witness=largest["witness"],
        complete_mean_height=base["complete_mean_height"], replacements=replacements,
        gates=dict(formal_completed_same_candidate_audits_only=True,
            every_new_original_leaf_and_all_signed_modes_checked=True,
            all_complete_mean_and_inverse_margins_preserved=True,
            full_nine_piece_cover_and_shared_jets_unchanged=True,
            one_common_physical_Darboux_unit=True, no_new_candidate_or_metric=True),
        input_hashes=inputs, previous_input_hashes=base["input_hashes"], source_sha256=sha(__file__),
        new_source_integrals_or_Arb_or_ODEs=0, exact_outer_solution_claimed=False,
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with a.out.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps(dict(event="complete_additional_candidate_audits", output=str(a.out),
        gates=result["gates"], largest_segment=largest["segment"],
        full_cell_upper=result["full_cell_physical_Darboux_upper"],
        panels=result["total_continuous_panels"], peak_RSS_KiB=result["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
