#!/usr/bin/env python3
"""Exact, streaming comparison of two formally audited physical-r candidates.

Only already saved enclosures are consumed. This program does not integrate,
construct an ODE solution, or change the selected global candidate. A Fourier
lower bound refers to the continuous interval enclosure of an entire saved
leaf, never to a sampled midpoint. The original and carrier candidates are
different functions with the same real background and shared endpoint jets.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    path = Path(path)
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def dyadic(value):
    if isinstance(value, dict):
        m, e = int(value["mantissa"]), int(value["binary_exponent"])
    else:
        m, e = int(value[0]), int(value[1])
    return Q(m)*(Q(2)**e)


def ceil_dyadic(value, bits=40):
    if value < 0 or value.denominator & (value.denominator-1):
        raise ValueError("A nonnegative dyadic upper endpoint is required")
    if not value:
        return Q(0)
    shift = max(0, value.numerator.bit_length()-bits)
    unit = 1 << shift
    mantissa = (value.numerator+unit-1)//unit
    exponent = shift-(value.denominator.bit_length()-1)
    return Q(mantissa)*(Q(2)**exponent)


def ball(value):
    if isinstance(value, dict):
        return dyadic(value["lower"]), dyadic(value["upper"])
    return dyadic(value[0]), dyadic(value[1])


def qrecord(value):
    return dict(numerator=str(value.numerator), denominator=str(value.denominator),
                decimal_diagnostic=format(float(value), ".16g"))


def abs_lower(interval):
    lo, hi = ball(interval)
    if lo > hi:
        raise ValueError("An exact directed interval is reversed")
    return lo if lo > 0 else -hi if hi < 0 else Q(0)


def formal(summary, resource_path):
    record = read(resource_path)
    if record["exitcode"] != 0 or record["termination_signal"] is not None:
        raise ValueError("An audited candidate has no successful formal exit")
    command = record["command"]
    prefix = command[command.index("--out-prefix")+1]
    if Path(prefix+"-summary.json") != summary:
        raise ValueError("A formal exit belongs to a different output")
    return command


def option(command, name):
    return Path(command[command.index(name)+1])


def save(path, record):
    if path.exists():
        raise FileExistsError("Use a fresh comparison output")
    temporary = path.with_name(path.name+".tmp")
    with temporary.open("w", encoding="utf-8") as stream:
        json.dump(record, stream, indent=2, allow_nan=False)
        stream.write("\n")
    temporary.replace(path)


def inspect(summary, record, *, rss_limit):
    parts = []
    count = 0
    global_upper = Q(0)
    global_lower = Q(0)
    global_witness = None
    modes = [0]+list(record["modes"])+list(
        range(max(record["modes"])+2, 2*max(record["modes"])+1, 2))
    for part in record["parts"]:
        path = Path(part["path"])
        if digest(path) != part["sha256"]:
            raise ValueError("An audited primary does not match its formal summary")
        at = Q(part["source_left"])
        header = trailer = False
        local_count = 0
        high = Q(-1)
        low = Q(0)
        witness = low_witness = None
        with gzip.open(path, "rt", encoding="utf-8") as stream:
            for line in stream:
                row = json.loads(line)
                if row["kind"] == "header":
                    if header or local_count:
                        raise ValueError("Duplicate or late audited header")
                    if (row["mode"] != record["mode"]
                            or row["input_hashes"] != record["input_hashes"]
                            or row["source_hashes"] != record["source_hashes"]
                            or row["complete_J_cosine_modes"] != modes):
                        raise ValueError("Audited primary identity mismatch")
                    header = True
                    continue
                if row["kind"] == "trailer":
                    if trailer or not row["complete"] or row["panels"] != local_count:
                        raise ValueError("Audited primary trailer mismatch")
                    trailer = True
                    continue
                if (not header or trailer
                        or row["kind"] != "complete_new_physical_substage_R64_J_R77_leaf"
                        or row["part"] != part["part"] or row["panel"] != local_count
                        or row["mode"] != record["mode"] or not row["complete_mean"]):
                    raise ValueError("Audited leaf order or complete mean changed")
                left, right = Q(row["source_left"]), Q(row["source_right"])
                if left != at or not left < right <= Q(part["source_right"]):
                    raise ValueError("Audited continuous source cover has a gap or overlap")
                if any(dyadic(value) <= 0 for value in row["gates_lower"].values()):
                    raise ValueError("An original complete analytic-domain gate failed")
                bounds = row["bounds_upper"]
                upper = dyadic(bounds["R77_full_physical_Darboux_upper"])
                factor = ball(row["source"]["physical_conversion_factor"])[0]
                coefficients = row["full_J_cosine_intervals"]
                if factor <= 0 or len(coefficients) != len(modes):
                    raise ValueError("A physical Fourier conversion is missing")
                coefficient_lower, coefficient_mode = max(
                    (factor*abs_lower(value)/(2 if m else 1), m)
                    for m, value in zip(modes, coefficients))
                if coefficient_lower > upper:
                    raise ValueError("The original Fourier lower and complete upper bounds conflict")
                locator = dict(part=part["part"], panel=local_count,
                    source_left=str(left), source_right=str(right),
                    physical_u=row["physical_u"])
                if upper > high:
                    high = upper
                    witness = dict(locator, full_D_upper=qrecord(upper),
                        mean_upper=qrecord(dyadic(bounds["finite_J_mean_l1_Darboux_upper"])),
                        retained_nonmean_upper=qrecord(dyadic(
                            bounds["finite_J_retained_nonmean_l1_Darboux_upper"])),
                        outside_saved_height_upper=qrecord(dyadic(
                            bounds["finite_J_outside_saved_height_l1_Darboux_upper"])),
                        source=row["source"],
                        signed_full_J_cosine_intervals=coefficients)
                if coefficient_lower > low:
                    low = coefficient_lower
                    low_witness = dict(locator, Fourier_mode=coefficient_mode,
                        all_r_leaf_sup_angle_D_lower=qrecord(coefficient_lower))
                local_count += 1
                count += 1
                at = right
                if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 1024*rss_limit:
                    raise MemoryError("Comparison exceeded its explicit observation limit")
        if not (header and trailer and at == Q(part["source_right"])
                and local_count == part["panels"]):
            raise ValueError("An audited part has incomplete coverage")
        declared = ball(part["bounds"]["R77_full_physical_Darboux_upper"]["value"])[1]
        if not high <= ceil_dyadic(declared):
            raise ValueError("Primary exceeds the directed 40-bit encoding of its part bound")
        parts.append(dict(part=part["part"], panels=local_count,
            exact_source_interval=[part["source_left"], part["source_right"]],
            complete_D_upper=qrecord(high), saved_full_precision_D_upper=qrecord(declared),
            primary_bounds_are_outward_40bit_dyadics=True,
            strongest_continuous_fourier_lower=qrecord(low),
            worst_upper_leaf=witness, lower_witness=low_witness,
            mean_height_change_from_original_abs=part["mean_height_change_from_original_abs"]))
        if high > global_upper:
            global_upper, global_witness = high, witness
        global_lower = max(global_lower, low)
    if count != record["panels"]:
        raise ValueError("The complete requested candidate count changed")
    return dict(mode=record["mode"], panels=count, parts=parts,
        complete_requested_D_upper=qrecord(global_upper),
        strongest_continuous_fourier_lower=qrecord(global_lower),
        worst_upper_leaf=global_witness), global_upper


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("physical-summary", "physical-resource", "carrier-summary",
                 "carrier-resource", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--rss-limit-mib", type=int, default=96)
    args = parser.parse_args()
    started = time.monotonic()
    cp = formal(args.physical_summary, args.physical_resource)
    cc = formal(args.carrier_summary, args.carrier_resource)
    physical, carrier = read(args.physical_summary), read(args.carrier_summary)
    if physical["mode"] != "physical" or carrier["mode"] != "carrier":
        raise ValueError("Compare the physical reconstruction against its carrier variant")
    for key in ("cell", "segment", "modes", "tau", "nodes", "panels",
                "whole_original_segment_covered", "original_candidate_input_hashes"):
        if physical[key] != carrier[key]:
            raise ValueError("The two candidate origins differ: "+key)
    if not all(physical["gates"].values()) or not all(carrier["gates"].values()):
        raise ValueError("A complete candidate mathematical gate is missing")
    for record in (physical, carrier):
        if (not record["mean_height_uses_one_global_constant"]
                or not record["two_fixed_mean_endpoint_heights_not_implicitly_claimed"]
                or not record["endpoint_nonmean_two_jets_exact_by_construction"]):
            raise ValueError("The shared nonmean jets or single mean constant changed")
    pm, cm = option(cp, "--moment-summary"), option(cc, "--moment-summary")
    carrier_moments = read(cm)
    if (carrier_moments["original_physical_moment_summary"] != str(pm)
            or carrier_moments["original_physical_moment_summary_sha256"] != digest(pm)
            or carrier_moments["physical_candidate_audit"] != str(args.physical_summary)
            or carrier_moments["physical_candidate_audit_sha256"] != digest(args.physical_summary)
            or carrier["input_hashes"].get(str(cm)) != digest(cm)
            or physical["input_hashes"].get(str(pm)) != digest(pm)):
        raise ValueError("The carrier did not retain these exact physical moments and baseline")
    p, pu = inspect(args.physical_summary, physical, rss_limit=args.rss_limit_mib)
    c, cu = inspect(args.carrier_summary, carrier, rss_limit=args.rss_limit_mib)
    if [(x["part"],x["panels"],x["exact_source_interval"]) for x in p["parts"]] != [
            (x["part"],x["panels"],x["exact_source_interval"]) for x in c["parts"]]:
        raise ValueError("The two complete requested partitions differ")
    paths = (args.physical_summary, args.physical_resource,
             args.carrier_summary, args.carrier_resource, pm, cm, Path(__file__))
    result = dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        schema="formal-physical-carrier-comparison-v1",
        status="Complete exact postprocessing of already formally audited candidates",
        input_hashes={str(path):digest(path) for path in paths},
        cell=physical["cell"],segment=physical["segment"],modes=physical["modes"],
        tau=physical["tau"],whole_original_segment_covered=physical["whole_original_segment_covered"],
        physical=p,carrier=c,carrier_upper_strictly_smaller=cu<pu,
        exact_upper_bound_ratio=qrecord(cu/pu) if pu>0 else None,
        comparison_claim="Only the certified upper bounds are compared. The exact residual "
            "functions are different; no pointwise minimum or mixed candidate is constructed.",
        one_global_mean_constant_each_candidate=True,
        nonmean_endpoint_two_jets_shared_exactly=True,
        two_mean_endpoint_values_not_fixed_without_an_integral_constraint=True,
        strict_lower_scope="For every r in the stated continuous leaf, sup_theta |D(r,theta)| "
            "is at least factor_lower*|J_cos_m|_lower/2 for m>0, or the zero coefficient "
            "lower for m=0. This uses the Fourier coefficient inequality, not a point sample.",
        gates=dict(both_formal_audits_exit0=True,all_original_analytic_gates_retained=True,
            all_primary_hashes_and_continuous_covers_checked=True,
            same_metric_and_shared_endpoint_origins=True,same_original_physical_moments=True,
            distinct_candidate_functions_not_intersected=True,
            no_pointwise_minimum_across_candidates=True,
            no_global_candidate_selection_implicitly_changed=True),
        new_Arb_or_source_integration=False,new_ODE_or_BVP=False,
        exact_outer_solution_claimed=False,
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    save(args.out,result)
    print(json.dumps(dict(event="complete_formal_carrier_comparison",out=str(args.out),
        physical_D=p["complete_requested_D_upper"],carrier_D=c["complete_requested_D_upper"],
        certified_upper_improved=cu<pu,ratio=result["exact_upper_bound_ratio"],gates=result["gates"])),flush=True)


if __name__ == "__main__":
    main()
