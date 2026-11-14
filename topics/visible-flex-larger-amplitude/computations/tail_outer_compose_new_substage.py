#!/usr/bin/env python3
"""Replace one complete source segment by its verified eight-part candidate.

This is exact stored-evidence composition, using only stdlib arithmetic.  The
new segment is a different function.  Its bound is never minimized against
the former segment's bound on a leaf.  The original exterior nonmean physical
two-jets, background, full mean equation and all other segment functions are
preserved; the global mean height is integrated with one common constant.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from copy import deepcopy
from fractions import Fraction as F
import gzip
import json
from pathlib import Path
import resource
import time

from tail_outer_span_stream_check import sha, dyadic


def load(path):
    path = Path(path)
    with (gzip.open(path, "rt") if path.suffix == ".gz" else path.open()) as stream:
        return json.load(stream)


def verify_hashes(mapping):
    for path, checksum in mapping.items():
        if sha(path) != checksum:
            raise ValueError("A stored evidence dependency changed: " + path)


def verify_sources(data):
    for name, checksum in data.get("source_hashes", {}).items():
        if sha(Path(__file__).with_name(name)) != checksum:
            raise ValueError("An executed numerical source changed: " + name)


def completed(resource_path, target, script_name):
    usage = load(resource_path)
    command = usage["command"]
    if (usage["exitcode"] != 0 or usage["termination_signal"] is not None
            or "computations/" + script_name not in command
            or Path(command[command.index("--out") + 1]) != target):
        raise ValueError("A formal exit does not identify its complete output")
    return usage


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ("base", "candidate", "construction-resource", "nodes", "summary",
                "resource", "stream-check", "stream-resource", "mean", "mean-resource",
                "old-witness", "out"):
        parser.add_argument("--" + key, type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("Use a fresh new-candidate composition")
    started = time.monotonic()
    base, candidate, nodes, summary, checked, mean, old_witness = map(load,
        (args.base, args.candidate, args.nodes, args.summary, args.stream_check,
         args.mean, args.old_witness))
    segment = candidate["segment"]
    if (not 0 <= segment < 8 or candidate["cell"] != 0 or base["cell"] != 0
            or nodes["cell"] != 0 or summary["segment"] != segment
            or mean["segment"] != segment or old_witness["segment"] != segment):
        raise ValueError("The selected source segment identity changed")
    for data in (base, candidate, summary, checked, mean, old_witness):
        if not all(data["gates"].values()):
            raise ValueError("A complete mathematical evidence gate is missing")
        verify_hashes(data.get("input_hashes", {}))
    for data in (candidate, summary):
        verify_sources(data)
    completed(args.construction_resource, args.candidate,
              "tail_outer_checked_substage_candidate.py")
    completed(args.resource, args.summary, "tail_outer_centered_span_refinement_v2.py")
    completed(args.stream_resource, args.stream_check, "tail_outer_span_stream_check.py")
    completed(args.mean_resource, args.mean, "tail_outer_mean_constraint_stream.py")
    for result, filename in ((checked, "tail_outer_span_stream_check.py"),
                             (mean, "tail_outer_mean_constraint_stream.py")):
        if result["source_sha256"] != sha(Path(__file__).with_name(filename)):
            raise ValueError("The executed exact postprocessor source changed")
    common = ("modes", "tau")
    if any(any(data[key] != base[key] for key in common)
           for data in (candidate, nodes, summary, mean)):
        raise ValueError("The Fourier modes or analytic norm changed")
    if (candidate["input_hashes"].get(str(args.nodes)) != sha(args.nodes)
            or summary["input_hashes"].get(str(args.candidate)) != sha(args.candidate)
            or checked["input_hashes"].get(str(args.summary)) != sha(args.summary)
            or checked["input_hashes"].get(str(args.resource)) != sha(args.resource)
            or mean["input_hashes"].get(str(args.summary)) != sha(args.summary)
            or mean["input_hashes"].get(str(args.stream_check)) != sha(args.stream_check)):
        raise ValueError("The new candidate and its executed audit chain differ")
    for key in ("original_865_state_input_retained", "only_original_segment_candidate_replaced",
                "source_background_unchanged", "original_outer_endpoint_two_jets_reused_exactly",
                "all_internal_shared_two_jets", "actual_polynomial_derivative_used_for_all_residuals"):
        if candidate[key] is not True:
            raise ValueError("The construction's compatibility identity is absent: " + key)
    if (candidate["shooting_parts"] != 8 or len(candidate["nodes"]) != 9
            or len(candidate["parts"]) != 8 or len(candidate["bins"]) != 64
            or not nodes["complete_original_segment_node_cover"]):
        raise ValueError("The complete shared-node or positive-bin definition is absent")
    for index, node in enumerate(candidate["nodes"]):
        if (node["point"] != index or F(node["source_x"]) != F(index, 8)
                or set(node["shared_physical_jets"]) != {"H", "Hr", "Hrr"}):
            raise ValueError("A shared candidate node or its full physical two-jet is missing")
    exterior_fields = ("radius", "w", "wr", "shared_physical_jets",
                       "candidate_L_orthonormal_cosine", "finite_endpoint_definition")
    for point, original in ((0, segment), (8, segment + 1)):
        node = candidate["nodes"][point]
        if (not node["original_outer_endpoint_reused_exactly"]
                or any(node[key] != nodes["rows"][original][key] for key in exterior_fields)):
            raise ValueError("The original exterior physical two-jets were not reused exactly")
    for index, part in enumerate(candidate["parts"]):
        if (part["part"] != index or F(part["left"]) != F(index, 8)
                or F(part["right"]) != F(index + 1, 8)
                or not part["complete_mean_and_defect"] or part["first_failures"]):
            raise ValueError("The new compatible segment's full cover is incomplete")
    count = summary["total_accepted_panels"]
    if (summary["first_part"] != 0 or summary["stop_part"] != 8
            or not summary["whole_segment_maximum_recomputed"]
            or not summary["complete_mean_and_its_actual_derivative_retained"]
            or checked["continuous_panels"] != count or mean["continuous_panels"] != count):
        raise ValueError("The new segment's full finite-J and mean audit is incomplete")
    components = deepcopy(base["components"])
    if [row["segment"] for row in components] != list(range(9)):
        raise ValueError("The previous complete nine-piece cell is missing")
    for row in components:
        if sha(row["candidate_path"]) != row["candidate_sha256"]:
            raise ValueError("A retained component candidate changed")
    target = components[segment]
    if candidate["input_hashes"].get(target["candidate_path"]) != target["candidate_sha256"]:
        raise ValueError("The new construction did not start with this original piece")
    previous_target = deepcopy(target)
    new_upper = mean["full_segment_physical_Darboux_upper"]
    if not 0 <= dyadic(new_upper) < dyadic(target["physical_Darboux_upper"]):
        raise ValueError("This replacement does not improve its complete segment bound")
    target.update(candidate_path=str(args.candidate), candidate_sha256=sha(args.candidate),
        candidate_definition_unchanged=False,
        physical_Darboux_upper=new_upper, continuous_panels=count,
        origin="NEW compatible eight-part candidate, complete finite-Horner/J and R77 audit",
        audit=str(args.summary), audit_sha256=sha(args.summary),
        resource=str(args.resource), resource_sha256=sha(args.resource),
        mean_constraint=str(args.mean), mean_constraint_sha256=sha(args.mean),
        witness=dict(segment=segment, **mean["witness"]))
    largest = max(components, key=lambda row: dyadic(row["physical_Darboux_upper"]))
    named_inputs = [getattr(args, name.replace("-", "_")) for name in
        ("base", "candidate", "construction-resource", "nodes", "summary", "resource",
         "stream-check", "stream-resource", "mean", "mean-resource", "old-witness")]
    result = dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", scope=__doc__,
        status="Complete NEW nine-piece cell0 candidate after one compatible segment replacement",
        cell=0, modes=base["modes"], tau=base["tau"], components=components,
        total_continuous_panels=sum(row["continuous_panels"] for row in components),
        full_cell_physical_Darboux_upper=largest["physical_Darboux_upper"],
        largest_bound_segment=largest["segment"], witness=largest["witness"],
        replacement=dict(segment=segment, previous_component=previous_target,
            new_candidate=str(args.candidate), old_nonzero_defect_witness=str(args.old_witness),
            old_and_new_functions_not_pointwise_minimized=True,
            exterior_physical_two_jets_exactly_identical=True,
            complete_new_candidate_physical_Darboux_upper=new_upper),
        gates=dict(formal_complete_construction_and_all_audits=True,
            same_original_background_and_exterior_physical_two_jets=True,
            all_nine_shared_nodes_eight_parts_and_64_true_bins_present=True,
            complete_new_finite_J_and_R77_mean_audits=True,
            all_other_nonmean_segment_functions_and_defect_bounds_retained=True,
            no_minimum_between_bounds_of_different_candidates=True,
            replacement_improves_recorded_whole_segment_bound=True),
        complete_mean_height="One common integration constant; the new full mean is integrated across all pieces. Its value can change after the replaced piece, while its derivative two-jets glue uniquely by R64/R66.",
        previous_mean_height_semantics=base["complete_mean_height"],
        input_hashes={str(path): sha(path) for path in named_inputs},
        previous_input_hashes=base["input_hashes"], source_sha256=sha(__file__),
        new_source_integrals_or_Arb_or_ODEs=0, exact_outer_solution_claimed=False,
        Green_or_Schur_inverse_claimed=False, elapsed_seconds=time.monotonic() - started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with args.out.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps(dict(event="complete_new_candidate_composition", output=str(args.out),
        panels=result["total_continuous_panels"], largest_segment=largest["segment"],
        full_cell_upper=result["full_cell_physical_Darboux_upper"],
        replaced_segment_upper=new_upper, gates=result["gates"],
        peak_RSS_KiB=result["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
