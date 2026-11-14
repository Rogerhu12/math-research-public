"""Exact stored-data composition of the same physical-r last-piece audit.

Only physical Darboux bounds change; no source-coordinate residuals are mixed.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import json
from pathlib import Path
import resource
import time

from tail_outer_replace_component_audits import sha, dyadic, upper, encoded


def load(path):
    with (gzip.open(path, "rt") if path.suffix == ".gz" else path.open()) as stream:
        return json.load(stream)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("base", "audit", "resource", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("Use a new completed same-candidate composition")
    start = time.monotonic()
    base, audit, usage = map(load, (args.base, args.audit, args.resource))
    hashes = {str(p): sha(p) for p in (args.base, args.audit, args.resource)}
    if (not all(base["gates"].values()) or not all(audit["gates"].values())
            or base["cell"] != 0 or audit["cell"] != 0 or audit["segment"] != 8
            or base["modes"] != audit["modes"] or base["tau"] != audit["tau"]
            or usage["exitcode"] != 0 or usage["termination_signal"] is not None
            or str(args.audit) not in usage["command"]):
        raise ValueError("Completed matching candidate audits are required")
    for data in (base, audit):
        for path, checksum in data["input_hashes"].items():
            if sha(path) != checksum:
                raise ValueError("A completed same-candidate input changed: "+path)
    for name, checksum in audit["source_hashes"].items():
        if sha(Path(__file__).with_name(name)) != checksum:
            raise ValueError("A finite-J source changed: "+name)
    components = [dict(row) for row in base["components"]]
    if [row["segment"] for row in components] != list(range(9)):
        raise ValueError("The base must contain all nine complete components")
    target = components[8]
    if audit["input_hashes"].get(target["candidate_path"]) != target["candidate_sha256"]:
        raise ValueError("The new audit does not use the identical physical-r candidate")
    rows = audit["rows"]
    at = F(0)
    maximum, witness = F(0), None
    for index, row in enumerate(rows):
        left, right = F(row["u_left"]), F(row["u_right"])
        if (row["panel"] != index or left != at or not left < right
                or not row["full_R64_mean_domain_gate"]
                or sorted(map(int, row["complete_J_cosine"])) !=
                list(range(0, 2*max(audit["modes"])+1, 2))):
            raise ValueError("The complete same-radius/full-angle cover is missing")
        value = upper(row["full_finite_J_bounds"]["finite_J_l1_Darboux_upper"])
        if value > maximum:
            maximum, witness = value, dict(segment=8, panel=index,
                physical_u_left=row["u_left"], physical_u_right=row["u_right"],
                source_coordinate="physical r; r_x=1")
        at = right
    if at != 1 or maximum != upper(audit["bounds"]["finite_J_l1_Darboux_upper"]["value"]):
        raise ValueError("The full physical-r maximum is not the recorded complete maximum")
    for record in audit["minima"].values():
        endpoint = record["value"]["lower"]
        if F(int(endpoint["mantissa"]))*F(2)**int(endpoint["binary_exponent"]) <= 0:
            raise ValueError("A complete mean/inverse margin is not strictly positive")
    if maximum < dyadic(target["physical_Darboux_upper"]):
        target.update(physical_Darboux_upper=encoded(maximum), continuous_panels=len(rows),
            origin="Complete same physical-r candidate finite-Horner/full-J audit",
            audit=str(args.audit), audit_sha256=hashes[str(args.audit)],
            resource=str(args.resource), resource_sha256=hashes[str(args.resource)],
            witness=witness)
    largest = max(components, key=lambda row: dyadic(row["physical_Darboux_upper"]))
    out = dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", scope=__doc__,
        status="Complete same cell0 candidate with tighter physical-r last-piece audit",
        cell=0, modes=base["modes"], tau=base["tau"], components=components,
        full_cell_physical_Darboux_upper=largest["physical_Darboux_upper"],
        largest_bound_segment=largest["segment"], witness=largest["witness"],
        total_continuous_panels=sum(row["continuous_panels"] for row in components),
        gates=dict(formal_physical_r_audit_exit0=True,
            exact_same_last_piece_candidate_and_true_metric=True,
            all_input_and_source_hashes_match=True,
            exact_complete_physical_radius_cover=True,
            all_complete_mean_and_inverse_margins_positive=True,
            all_finite_modes_through_twice_height_cutoff=True,
            complete_nine_segment_candidate_unchanged=True),
        input_hashes=hashes, unchanged_prior_input_hashes=base["input_hashes"],
        complete_mean_height=base["complete_mean_height"], source_sha256=sha(__file__),
        new_candidate_or_source_integrals=0, exact_outer_solution_claimed=False,
        other_geometry_or_curvature_bounds_recomputed=False,
        elapsed_seconds=time.monotonic()-start,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with args.out.open("x") as stream:
        json.dump(out, stream, indent=2)
        stream.write("\n")
    print(json.dumps(dict(event="complete_last_piece_composition", output=str(args.out),
        gates=out["gates"], full_cell_upper=out["full_cell_physical_Darboux_upper"],
        largest_segment=out["largest_bound_segment"], panels=out["total_continuous_panels"],
        peak_RSS_KiB=out["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
