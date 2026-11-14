#!/usr/bin/env python3
"""Local-only exact physical-defect consumer for the frozen R102 reference.

Read the original gzip streams directly from the local filesystem.
Never fetch, encode, split, or transmit binary primary data through API tools.
Default: refine only part 0 (37 leaves); the seven already paid coarse bounds
remain the original formal summary bounds.  --parts all reads all 1740 leaves.
No source evaluation, root solve, Fourier sampling, Arb, ODE, or Node is used.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12--13.
Prepared source; no local execution is claimed until a new resource says so.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

EXPECTED = {
    "summary": "806fdb96b9aa6eafd921c07518a5b52218180d2182f7b8d18abb8e3d695638e4",
    "resource": "912ad6200027fdb445cd3e8636c1f6cd404a3480d2c013b6c4722e6888016820",
    "stream_check": "2c33f3a08428ed0573d61ed8bafd0fb64636c4e5c9487b8c419cf2f57abc7f2a",
    "budget": "d01b7310f9d76fa5d5d56f44805c67fedf7be776a78435803943edcda424bc6f",
    "mean_source": "4b16b860eb89d7b8f19d7f8ff05642ea0122b0a2016d4be623d5483430023a5c",
    "finite_J_source": "85bf30e818e7ab92107a5f5a537225afb9273877327bf6e0092b303b01a1b5d8",
    "verified_parser_source": "cb8714409d0fbe6209b58cd2de867fd79e785464089e8ba151163b16ddfb6262",
}
PART_COUNTS = [37, 53, 125, 208, 304, 257, 256, 500]
PART_SHA = [
    "2ed331b98bd0004e2824088f2542483703a5e1fb9dfcdaa9105a863c2b6ba20a",
    "af56ac6810d1226234d2232594be5e58b35cc6f69d3ee9b9021ac0234c8b77ff",
    "a560755a9f860fe0a2828f56de36a3ed557a5b24ecb1e5213dde03539758142f",
    "5181dce29cefe73de6e00ee06f6c03182b7d8ecd5114395f3d48d634ea901605",
    "a398383644f2d077d0ea10d86f41784b02284fc71f1ba5f700787d57e0603441",
    "8842ecd64dba441d60fa360761471f2026d16e83d9a9a485256ae4d8c3a9e7da",
    "53cfb3121234f41e433991de2bb08b664c4e2b9b91b863cc53bc0cc4475862a6",
    "a2b0836b2603993aaa6aa828168f817184bab4ddaf278c96be90774420070676",
]


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def dyadic(value):
    # The existing local stream schema was read in its text producer/checker.
    if (not isinstance(value, list) or len(value) != 2
            or any(not isinstance(v, int) for v in value)):
        raise ValueError("A stream dyadic must be [integer mantissa, exponent]")
    return F(value[0])*F(2)**value[1]


def pair(value):
    lo, hi = map(dyadic, value)
    if lo > hi:
        raise ValueError("Reversed source interval")
    return lo, hi


def budget_dyadic(value):
    if (not isinstance(value, list) or len(value) != 2
            or not isinstance(value[0], str) or not isinstance(value[1], int)):
        raise ValueError("Wrong exact text budget dyadic")
    return F(int(value[0]))*F(2)**value[1]


def summary_upper(part, name):
    v = part["bounds"][name]["value"]["upper"]
    return F(int(v["mantissa"]))*F(2)**v["binary_exponent"]


def up(value, bits=64):
    value = F(value)
    if value < 0:
        raise ValueError("A positive upper bound became negative")
    if not value:
        return [0, 0]
    exponent = value.numerator.bit_length()-value.denominator.bit_length()
    if value < F(2)**exponent:
        exponent -= 1
    shift = exponent-bits+1
    scaled = value/F(2)**shift
    return [(scaled.numerator+scaled.denominator-1)//scaled.denominator, shift]


def exact_pair(value):
    return [str(value.numerator), str(value.denominator)]


def rss_limit(mib):
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if peak > mib*1024:
        raise MemoryError("The explicit RSS observation limit was exceeded")
    return peak


def resolve(topic, value):
    path = Path(value)
    return path if path.is_absolute() else topic/path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", type=Path, default=Path(__file__).resolve().parent.parent)
    for name in ("summary", "resource", "stream-check", "budget", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--parts", choices=("0", "all"), default="0")
    parser.add_argument("--rss-limit-mib", type=int, default=40)
    args = parser.parse_args()
    topic = args.topic.resolve()
    output = resolve(topic, args.out)
    if output.exists():
        raise FileExistsError("Use a fresh output; do not overwrite a primary or earlier result")
    started = time.monotonic()
    inputs = {}
    loaded = {}
    for key in ("summary", "resource", "stream_check", "budget"):
        path = resolve(topic, getattr(args, key))
        checksum = sha(path)
        if checksum != EXPECTED[key]:
            raise ValueError("An exact input text identity changed: "+key)
        inputs[str(path)] = checksum
        loaded[key] = json.loads(path.read_text())
    summary, usage, checked, budget = (
        loaded[k] for k in ("summary", "resource", "stream_check", "budget"))
    summary_name, usage_name = str(args.summary), str(args.resource)
    # The old stream check stores the original topic-relative names.  Resolve
    # its keys as paths and compare content identity, never rewrite that file.
    def checked_hash(relative):
        direct = checked["input_hashes"].get(str(relative))
        if direct is not None:
            return direct
        matches = [v for k, v in checked["input_hashes"].items()
                   if resolve(topic, k).resolve() == resolve(topic, relative).resolve()]
        if len(matches) != 1:
            raise ValueError("No unique original checked input identity: "+str(relative))
        return matches[0]
    if (usage["exitcode"] != 0 or usage["termination_signal"] is not None
            or not all(summary["gates"].values()) or not all(checked["gates"].values())
            or checked_hash(summary_name) != EXPECTED["summary"]
            or checked_hash(usage_name) != EXPECTED["resource"]
            or summary["cell"] != 0 or summary["segment"] != 7
            or summary["phase"] != "formal-complete"
            or summary["first_part"] != 0 or summary["stop_part"] != 8
            or not summary["same_exact_candidate_and_background"]
            or not summary["complete_mean_and_its_actual_derivative_retained"]
            or not summary["whole_segment_maximum_recomputed"]
            or summary["total_accepted_panels"] != 1740
            or checked["continuous_panels"] != 1740):
        raise ValueError("The original full candidate was not formally preserved")
    if (budget["input_hashes"]["summary"] != EXPECTED["summary"]
            or not all(budget["gates"].values())
            or budget["parameters"]["chosen_joint_A1_nonmean_field_epsilon"]
               != {"numerator": "1", "denominator": "512"}):
        raise ValueError("R102 target identity changed")
    if summary["source_hashes"]["tail_outer_general_mean_bounds.py"] != EXPECTED["mean_source"]:
        raise ValueError("Different complete mean source")
    if summary["source_hashes"]["tail_outer_substage_span_refinement.py"] != EXPECTED["finite_J_source"]:
        raise ValueError("Different actual derivative/full-J source")
    for name, checksum in summary["source_hashes"].items():
        path = topic/"computations"/name
        if sha(path) != checksum:
            raise ValueError("Restore the preserved producer before consuming: "+str(path))
        inputs[str(path)] = checksum
    parser_path = topic/"computations/tail_outer_span_stream_check.py"
    if sha(parser_path) != EXPECTED["verified_parser_source"]:
        raise ValueError("The original stream schema checker changed")
    inputs[str(parser_path)] = EXPECTED["verified_parser_source"]
    for name, checksum in summary["input_hashes"].items():
        path = resolve(topic, name)
        if sha(path) != checksum:
            raise ValueError("A frozen candidate/background input changed: "+name)
        inputs[str(path)] = checksum
    modes = list(range(0, summary["complete_J_cutoff"]+1, 2))
    if modes != list(range(0, 81, 2)) or summary["modes"] != list(range(2, 41, 2)):
        raise ValueError("The complete mean/finite frequency support changed")
    selected = {0} if args.parts == "0" else set(range(8))
    total, parts = 0, []
    for index, part in enumerate(summary["parts"]):
        if (part["part"] != index or part["panels"] != PART_COUNTS[index]
                or part["output_sha256"] != PART_SHA[index]
                or not part["complete_source_cover"]):
            raise ValueError("The original part manifest changed")
        cap = budget_dyadic(budget["chosen"][index]["strict_available_dH_enclosure"]["lo"])
        if budget["chosen"][index]["part"] != index or cap <= 0:
            raise ValueError("Wrong strict conditional defect budget")
        coarse = (summary_upper(part, "physical_nonmean_second_source_W1")/3
                  + summary_upper(part, "mean_physical_hrr_minus_background_abs"))
        if index not in selected:
            parts.append(dict(part=index, original_panels=part["panels"],
                stream_read_this_run=False, bound_origin="original formal R64 summary",
                physical_R_H_upper=up(coarse), exact_upper=exact_pair(coarse),
                R102_strict_budget_lower=exact_pair(cap),
                conditional_budget_paid=coarse < cap))
            continue
        path = resolve(topic, part["output"])
        checksum = sha(path)
        if checksum != PART_SHA[index] or checked_hash(part["output"]) != checksum:
            raise ValueError("A local primary no longer matches its formal stream check")
        inputs[str(path)] = checksum
        header = trailer = False
        count, covered, stop = 0, F(index, 8), F(index+1, 8)
        maximum, worst = F(-1), None
        source_count = {"direct_complete_J_R77": 0, "complete_Darboux_R77": 0,
                        "same_leaf_complete_RK": 0}
        with gzip.open(path, "rt") as stream:
            for line in stream:
                row = json.loads(line)
                if row["kind"] == "header":
                    if (header or count or row["part"] != index
                            or row["source_hashes"] != summary["source_hashes"]
                            or row["input_hashes"] != summary["input_hashes"]
                            or row["complete_J_cosine_modes"] != modes):
                        raise ValueError("Wrong complete finite-field header")
                    header = True
                    continue
                if row["kind"] == "complete_substage_trailer":
                    if (trailer or not row["complete_source_cover"]
                            or row["accepted_panels"] != count or row["part"] != index):
                        raise ValueError("Wrong complete substage trailer")
                    trailer = True
                    continue
                if row["kind"] != "accepted_complete_R64_and_J_panel" or not header or trailer:
                    raise ValueError("Unknown local primary record")
                left, right = F(row["source_left"]), F(row["source_right"])
                if left != covered or not left < right <= stop:
                    raise ValueError("A complete source leaf is missing or duplicated")
                if (not row["same_candidate_complete_mean"]
                        or not row["outside_saved_J_has_no_c_or_cx"]
                        or len(row["full_J_cosine_intervals"]) != 41
                        or any(dyadic(v) <= 0 for v in row["gates_lower"].values())):
                    raise ValueError("A real mean/denominator/full-frequency gate failed")
                bounds = {k: dyadic(v) for k, v in row["bounds_upper"].items()}
                if any(v < 0 for v in bounds.values()):
                    raise ValueError("A saved norm bound became negative")
                rlo, rhi = pair(row["source"]["radius"])
                rxlo, rxhi = pair(row["source"]["radius_x"])
                wlo, whi = pair(row["source"]["w"])
                flo, fhi = pair(row["source"]["physical_conversion_factor"])
                Llo = dyadic(row["gates_lower"]["real_L_lower"])
                Dlo = dyadic(row["gates_lower"]["real_D_lower"])
                if min(rlo, rxlo, wlo, flo, Llo, Dlo) <= 0:
                    raise ValueError("The shared physical conversion is not positive")
                Ehi, dsmall = 1+whi*whi, min(F(1), Dlo)
                multiplier = F(3, 2)*Ehi**2*bounds["full_D_nonconstant_W1"]/dsmall**3
                coeffs = [max(map(abs, pair(v))) for v in row["full_J_cosine_intervals"]]
                Jperp = sum(coeffs[1:], F(0))
                Jmean = min(coeffs[0], multiplier*Jperp)
                Jfull = min(sum(coeffs, F(0)), bounds["complete_J_l1"],
                            bounds["full_finite_J_W1"], Jperp+Jmean)
                direct = whi*Jfull/(rxlo*Llo)
                Dperp = min(fhi*Jperp,
                    bounds["finite_J_retained_nonmean_l1_Darboux_upper"]
                    + bounds["finite_J_outside_saved_height_l1_Darboux_upper"])
                Dmean = min(fhi*coeffs[0], bounds["finite_J_mean_l1_Darboux_upper"],
                            multiplier*Dperp)
                Dfull = min(bounds["actual_Darboux_defect_abs"],
                            bounds["finite_J_l1_Darboux_upper"], Dperp+Dmean)
                converted = rhi*Ehi**2*Dfull/(wlo*Llo)
                same_leaf_RK = (bounds["physical_nonmean_second_source_W1"]/3
                    + bounds["mean_physical_hrr_minus_background_abs"])
                alternatives = {"direct_complete_J_R77": direct,
                    "complete_Darboux_R77": converted, "same_leaf_complete_RK": same_leaf_RK}
                chosen = min(alternatives, key=alternatives.get)
                value = alternatives[chosen]
                source_count[chosen] += 1
                if value > maximum:
                    maximum = value
                    worst = dict(part=index, bin=row["bin"], source_left=str(left),
                        source_right=str(right), bound_choice=chosen,
                        alternatives_upper={k: up(v) for k, v in alternatives.items()},
                        complete_J_l1_R77_upper=up(Jfull), original_J_mean_upper=up(coeffs[0]),
                        R77_J_mean_upper=up(Jmean), mean_from_nonmean_multiplier_upper=up(multiplier),
                        source_intervals={k: row["source"][k]
                            for k in ("radius", "radius_x", "w", "physical_conversion_factor")},
                        real_L_lower_exact=exact_pair(Llo), real_D_lower_exact=exact_pair(Dlo))
                count += 1
                covered = right
                if count % 32 == 0:
                    rss_limit(args.rss_limit_mib)
        if not (header and trailer and covered == stop and count == part["panels"]):
            raise ValueError("The entire requested original substage was not read")
        if maximum < 0:
            raise ArithmeticError("The complete local maximum was not computed")
        # Saved stream dyadics may round outward more than the part summary.
        # Both are valid bounds of the same whole-part physical quantity.
        local_maximum = maximum
        maximum = min(maximum, coarse)
        total += count
        parts.append(dict(part=index, original_panels=part["panels"], local_leaves=count,
            stream_read_this_run=True, complete_original_substage_cover=True,
            bound_origin="same local leaf complete J/L and complete R77 mean",
            physical_R_H_upper=up(maximum), exact_upper=exact_pair(maximum),
            R102_strict_budget_lower=exact_pair(cap), conditional_budget_paid=maximum < cap,
            local_leaf_maximum_before_partwise_minimum=up(local_maximum),
            partwise_original_coarse_upper_was_used=(coarse < local_maximum),
            coarse_summary_upper=up(coarse), all_local_minima_refer_to_one_candidate=True,
            selected_bound_counts=source_count, witness=worst))
        print(json.dumps(dict(event="complete_local_R102_part", part=index, leaves=count,
            physical_R_H_upper=up(maximum), conditional_budget_paid=maximum < cap,
            peak_RSS_KiB=rss_limit(args.rss_limit_mib))), flush=True)
    if total != sum(PART_COUNTS[i] for i in selected):
        raise ValueError("Wrong complete local leaf count")
    result = dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        schema="r102-local-original-physical-defect-v1", status="completed exact local postprocessing",
        cell=0, segment=7, original_total_leaves=1740, original_parts=8,
        requested_parts=sorted(selected), locally_read_leaves=total,
        all_1740_primary_leaves_read_this_run=(total == 1740), parts=parts,
        joint_field_error_epsilon="1/512", target_curvature="33/4",
        all_conditional_defect_budgets_paid=all(p["conditional_budget_paid"] for p in parts),
        complete_mean_and_all_finite_J_modes_retained=True,
        complete_same_candidate_physical_R_H_units=True,
        candidate_or_metric_or_parameter_changes=0,
        true_solution_existence_or_field_error_paid=False,
        new_integrals_Arb_Node_ODE_or_samples=0,
        binary_primary_access="local filesystem gzip only; no API transfer",
        gates=dict(original_formal_exit0=True,original_stream_check_passed=True,
            all_original_producer_and_candidate_hashes_verified=True,
            all_requested_original_leaves_and_signed_modes_present=True,
            complete_real_mean_and_denominators_positive=True,
            exact_fraction_R77_and_R99_conversion=True,
            all_minima_compare_the_same_candidate_and_same_physical_quantity=True,
            untouched_parts_use_only_the_original_formal_summary=True),
        input_hashes=inputs,source_sha256=sha(__file__),
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=rss_limit(args.rss_limit_mib))
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x") as stream:
        json.dump(result, stream, separators=(",", ":"))
        stream.write("\n")
    print(json.dumps(dict(event="complete_local_R102_physical_defect", output=str(output),
        local_leaves=total, all_conditional_defect_budgets_paid=result["all_conditional_defect_budgets_paid"],
        peak_RSS_KiB=result["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
