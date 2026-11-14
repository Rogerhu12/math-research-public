#!/usr/bin/env python3
"""Use R77 to enclose the same complete candidate's zero-frequency defect.

Only exact stdlib Fraction arithmetic and existing complete streams are used.
The field, its true derivatives, full scalar mean and metric are unchanged.
Every input leaf and signed Fourier coefficient remains part of the bound.
No root, angular sample, source integral or radial ODE is evaluated here.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import json
from pathlib import Path
import resource
import time

from tail_outer_span_stream_check import sha, dyadic, pair


EXPECTED_MEAN_SOURCE = "4b16b860eb89d7b8f19d7f8ff05642ea0122b0a2016d4be623d5483430023a5c"


def up(value, bits=48):
    """Exact upward dyadic with at most bits significant binary digits."""
    value = F(value)
    if value < 0:
        raise ValueError("Only nonnegative bounds are rounded upward")
    if value == 0:
        return [0, 0]
    n, d = value.numerator, value.denominator
    exponent = n.bit_length()-d.bit_length()
    if value < F(2)**exponent:
        exponent -= 1
    shift = exponent-bits+1
    scaled = value/F(2)**shift
    return [(scaled.numerator+scaled.denominator-1)//scaled.denominator, shift]


def abs_pair(value):
    left, right = pair(value)
    return max(abs(left), abs(right))


def limit(mib):
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if peak > 1024*mib:
        raise MemoryError("The explicit observed RSS limit was exceeded")
    return peak


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ("summary", "resource", "stream-check", "out"):
        parser.add_argument("--"+key, type=Path, required=True)
    parser.add_argument("--rss-limit-mib", type=int, default=40)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("Use a new mean-constraint output")
    start = time.monotonic()
    summary, usage, checked = (json.loads(p.read_text()) for p in
        (args.summary, args.resource, args.stream_check))
    inputs = {str(p): sha(p) for p in (args.summary, args.resource, args.stream_check)}
    if (usage["exitcode"] != 0 or usage["termination_signal"] is not None
            or not all(summary["gates"].values()) or not all(checked["gates"].values())
            or not summary["whole_segment_maximum_recomputed"]
            or not summary["same_exact_candidate_and_background"]
            or not summary["complete_mean_and_its_actual_derivative_retained"]
            or checked["input_hashes"].get(str(args.summary)) != inputs[str(args.summary)]
            or checked["input_hashes"].get(str(args.resource)) != inputs[str(args.resource)]
            or summary["first_part"] != 0 or summary["stop_part"] != 8):
        raise ValueError("A formally completed, checked compatible candidate is required")
    if summary["source_hashes"].get("tail_outer_general_mean_bounds.py") != EXPECTED_MEAN_SOURCE:
        raise ValueError("The stored complete 1-D norm's mathematical source changed")
    for name, checksum in summary["source_hashes"].items():
        if sha(Path(__file__).with_name(name)) != checksum:
            raise ValueError("A preserved numerical source changed: "+name)
    for path, checksum in summary["input_hashes"].items():
        if sha(path) != checksum:
            raise ValueError("A same-candidate input changed: "+path)
    proof = Path(__file__).resolve().parent.parent/"results/R77-complete-mean-defect-zero-mode.md"
    inputs[str(proof)] = sha(proof)
    modes = list(range(0, summary["complete_J_cutoff"]+1, 2))
    global_max, global_witness = F(-1), None
    old_max = F(0)
    max_mean, max_nonmean, max_coefficient = F(0), F(0), F(0)
    total = 0
    parts = []
    for index, part in enumerate(summary["parts"]):
        path = Path(part["output"])
        checksum = sha(path)
        if (index != part["part"] or checksum != part["output_sha256"]
                or checked["input_hashes"].get(str(path)) != checksum):
            raise ValueError("A checked complete stream changed")
        inputs[str(path)] = checksum
        covered, stop = F(index, 8), F(index+1, 8)
        count = 0
        part_max, part_witness = F(-1), None
        header = trailer = False
        with gzip.open(path, "rt") as stream:
            for line in stream:
                row = json.loads(line)
                if row["kind"] == "header":
                    if (header or count or row["part"] != index
                            or row["source_hashes"] != summary["source_hashes"]
                            or row["input_hashes"] != summary["input_hashes"]
                            or row["complete_J_cosine_modes"] != modes):
                        raise ValueError("The complete finite-field header changed")
                    header = True
                    continue
                if row["kind"] == "complete_substage_trailer":
                    if (trailer or not row["complete_source_cover"]
                            or row["accepted_panels"] != count or row["part"] != index):
                        raise ValueError("The complete substage trailer changed")
                    trailer = True
                    continue
                if row["kind"] != "accepted_complete_R64_and_J_panel" or not header or trailer:
                    raise ValueError("Unexpected continuous stream structure")
                left, right = F(row["source_left"]), F(row["source_right"])
                if left != covered or not left < right <= stop:
                    raise ValueError("The source leaf cover is incomplete")
                if (not row["same_candidate_complete_mean"]
                        or not row["outside_saved_J_has_no_c_or_cx"]
                        or len(row["full_J_cosine_intervals"]) != len(modes)
                        or any(dyadic(v) <= 0 for v in row["gates_lower"].values())):
                    raise ValueError("A full-mean, finite-mode or positive-domain gate is absent")
                bounds = {k: dyadic(v) for k, v in row["bounds_upper"].items()}
                wlo, whi = pair(row["source"]["w"])
                flo, fhi = pair(row["source"]["physical_conversion_factor"])
                dmin = dyadic(row["gates_lower"]["real_D_lower"])
                if not wlo > 0 or not flo > 0 or not dmin > 0:
                    raise ValueError("The common physical conversion or real branch is not positive")
                emax, dsmall = 1+whi*whi, min(F(1), dmin)
                # Frozen R64 domain() bounds ||1-D||_{W^1_tau}, including its
                # constant term.  This also bounds ||D-<D>||_infinity.  The
                # legacy field name alone is not used to infer that fact.
                delta_D = bounds["full_D_nonconstant_W1"]
                if delta_D < 0:
                    raise ValueError("A full D norm cannot be negative")
                coefficient = F(3, 2)*emax*emax*delta_D/(dsmall*dsmall*dsmall)
                coeffs = [abs_pair(v) for v in row["full_J_cosine_intervals"]]
                nonmean = min(fhi*sum(coeffs[1:], F(0)),
                    bounds["finite_J_retained_nonmean_l1_Darboux_upper"]+
                    bounds["finite_J_outside_saved_height_l1_Darboux_upper"])
                mean = min(fhi*coeffs[0], bounds["finite_J_mean_l1_Darboux_upper"],
                           coefficient*nonmean)
                previous = min(bounds["actual_Darboux_defect_abs"],
                               bounds["finite_J_l1_Darboux_upper"])
                improved = min(previous, mean+nonmean)
                witness = dict(part=index, bin=row["bin"], source_left=str(left),
                    source_right=str(right), old_physical_upper=up(previous),
                    nonmean_physical_upper=up(nonmean), new_mean_physical_upper=up(mean),
                    mean_from_nonmean_multiplier=up(coefficient),
                    Emax=up(emax), Dmin_exact_fraction=str(dmin),
                    full_one_minus_D_norm_upper=up(delta_D))
                if improved > part_max:
                    part_max, part_witness = improved, witness
                if improved > global_max:
                    global_max, global_witness = improved, witness
                old_max = max(old_max, previous)
                max_mean, max_nonmean = max(max_mean, mean), max(max_nonmean, nonmean)
                max_coefficient = max(max_coefficient, coefficient)
                count += 1
                covered = right
                if count % 64 == 0:
                    limit(args.rss_limit_mib)
        if not (header and trailer and covered == stop and count == part["panels"]):
            raise ValueError("An original whole substage is missing")
        total += count
        parts.append(dict(part=index, panels=count, physical_Darboux_upper=up(part_max),
                          witness=part_witness))
    if total != summary["total_accepted_panels"] or total != checked["continuous_panels"]:
        raise ValueError("The complete whole-segment leaf count changed")
    result = dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", scope=__doc__,
        status="Complete exact rational R77 mean-constraint postprocessing passed",
        cell=summary["cell"], segment=summary["segment"], modes=summary["modes"],
        tau=summary["tau"], continuous_panels=total, parts=parts,
        full_segment_physical_Darboux_upper=up(global_max), witness=global_witness,
        previous_complete_physical_Darboux_upper=up(old_max),
        complete_mean_contribution_upper=up(max_mean),
        complete_nonmean_contribution_upper=up(max_nonmean),
        largest_mean_multiplier_upper=up(max_coefficient),
        gates=dict(formal_original_exit0_and_exact_stream_check=True,
            full_original_source_and_input_identity=True, every_original_leaf_present=True,
            all_signed_finite_modes_retained=True, complete_mean_not_truncated=True,
            positive_real_domain_and_common_physical_units=True,
            exact_R75_candidate_identity_not_a_linearized_claim=True,
            exact_rational_R77_bound_every_leaf=True,
            previous_complete_bounds_preserved_as_minimum=True),
        input_hashes=inputs, source_sha256=sha(__file__),
        complete_one_minus_D_norm_semantics_source_sha256=EXPECTED_MEAN_SOURCE,
        identity="J0=-<(F(D)-F(<D>))J_perp>/<F(D)>, F(t)=t^(-3/2)",
        integer_power_multiplier="(3/2)*Emax^2*||D_perp||inf/min(1,Dmin)^3; saved ||1-D||W1 dominates the required norm",
        candidate_or_mean_or_metric_changes=0, new_Arb_roots_integrals_ODEs_or_angular_samples=0,
        exact_outer_solution_or_Green_Schur_inverse=False,
        elapsed_seconds=time.monotonic()-start, peak_RSS_KiB=limit(args.rss_limit_mib))
    with args.out.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps(dict(event="complete_R77_mean_constraint", output=str(args.out),
        panels=total, physical_Darboux_upper=result["full_segment_physical_Darboux_upper"],
        gates=result["gates"], peak_RSS_KiB=result["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
