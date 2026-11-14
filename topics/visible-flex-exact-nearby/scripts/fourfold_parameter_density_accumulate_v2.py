#!/usr/bin/env python3
"""Full signed R82 accumulation, with R86 spatial and real-parameter fees.

The finite source of order zero remains the certified central reference
defect.  On a real parameter interval its actual source and its approximation
error acquire eta times the UNIFORM first-parameter source, at every spatial
derivative order.  No central source majorant is silently used on the box.

All product frequencies are retained.  A prefix is labelled a prefix; only
the exact 550-segment partition ending at pi/2 is a complete forward leg.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import math
from pathlib import Path
import time
from flint import arb, acb, ctx

from fourfold_forward_density_pipeline_Q1024_v3 import (
    decode_ball, encode_ball, save, upper,
)
from fourfold_parameter_density_leaf import load_positive_rectangle
from fourfold_parameter_ordered_defect import (
    advance_parameter_integrals, add_rows, row_norms,
)
from fourfold_parameter_spatial_norms import parameter_spatial_rows
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_domain_cover_verify import Time
from fourfold_saved_circle_field_multidomain_budget import read


def records(values):
    return list(map(ball_record, values))


def center_zero_spatial(report, width):
    """Common true/finite source and error integral bounds, orders 0,1,2."""
    S, s = Fraction(report["label_strip"]), Fraction(width)
    if not 0 <= s < S:
        raise ValueError("a genuine spatial strip loss is required")
    E = upper(report["R72_inputs"]["integrated_approximation_error_E"])
    native = report.get("R86_spatial_inputs")
    if native and Fraction(native["spatial_derivative_strip"]) == s:
        finite = list(map(upper, native["finite_integrated_derivative_majorants"]))
        fees = list(map(upper, native["true_error_integrated_derivative_sup_fees"]))
        common = list(map(upper, native["common_true_and_finite_integrated_spatial_majorants"]))
        method = "same completed g0 report: full finite spatial-row norms"
    elif "density_exact_rectangle" in report:
        meta = report["density_exact_rectangle"]
        if sha(meta["path"]) != meta["sha256"]:
            raise ValueError("the saved complete g0 rectangle changed")
        _, rows = load_positive_rectangle(meta["path"])
        bounds = parameter_spatial_rows(rows, E, S, s)
        finite = list(map(upper, bounds["finite_integrated_spatial_derivative_moduli"]))
        fees = list(map(upper, bounds["actual_error_derivative_fees"]))
        common = list(map(upper, bounds["true_integrated_spatial_derivative_SUP_moduli"]))
        method = "all finite coefficients reloaded from the same g0 rectangle"
    else:
        values = list(map(upper, report["R72_inputs"]["finite_time_coefficient_A_norms"]))
        n0 = sum((2*v/(i+1) for i, v in enumerate(values)), arb(0)).upper()
        gap = exact_arb(S-s)
        factors = [arb(1)] + [(arb(j)/(arb(1).exp()*gap))**j for j in (1, 2)]
        finite = [(n0*v).upper() for v in factors]
        fees = [(math.factorial(j)*E/gap**j).upper() for j in range(3)]
        common = [(a+b).upper() for a, b in zip(finite, fees)]
        method = "complete A_S row norms with sup_k k^j exp(-gap*k) loss"
    if any(len(row) != 3 for row in (finite, fees, common)):
        raise ValueError("three spatial derivative orders are required")
    return finite, fees, common, dict(method=method,
        source_error_strip=str(S), spatial_strip=str(s),
        finite_integrated_sup_majorants=records(finite),
        integrated_true_minus_finite_sup_errors=records(fees),
        common_integrated_true_and_finite_sup_majorants=records(common))


def check_leaf(entry, descriptor_sha, center, eta, S, inner, spatial):
    path, zero_path = Path(entry["path"]), Path(entry["g0_report_path"])
    if sha(path) != entry["sha256"] or sha(zero_path) != entry["g0_report_sha256"]:
        raise ValueError("a completed parameter or g0 leaf changed")
    report, zero = read(path), read(zero_path)
    if not (report.get("complete") and report.get("complete_continuous_parameter_densities_proved")
            and zero.get("complete") and zero.get("complete_continuous_true_density_proved")):
        raise ValueError("only complete continuous source certificates may be accumulated")
    identity = report["identity"]
    ref = identity["reference"]
    if (ref != zero["identity"]["reference"]
        or ref["retarget_descriptor_sha256"] != descriptor_sha
        or ref["leg"] != "forward"
        or int(ref["segment"]) != int(entry["segment"])
        or list(map(Fraction, ref["normalized_subspan"])) != list(map(Fraction, entry["normalized_subspan"]))
        or not identity.get("fixed_reference_independent_of_parameter")):
        raise ValueError("the complete parameter sources use different reference coordinates")
    if (report["reference_certificate_sha256"] != entry["g0_report_sha256"]
        or bool(identity["whole_real_parameter_tube"]) != bool(eta)
        or list(map(Fraction, identity["exact_parameter_interval"])) != [center-eta, center+eta]):
        raise ValueError("actual parameter interval or central g0 witness differs")
    if (Fraction(report["label_strip"]) != S or Fraction(report["inner_strip"]) != inner
        or Fraction(report["spatial_derivative_strip"]) != spatial
        or Fraction(zero["label_strip"]) != S or Fraction(zero["inner_strip"]) != inner):
        raise ValueError("the source strip contracts differ")
    for j, item in enumerate(report["density"], 1):
        if item["parameter_order"] != j or not item["complete_spatial_jet_inputs"]["proved"]:
            raise ValueError("a complete actual spatial source is absent")
        jet = item["complete_spatial_jet_inputs"]
        if Fraction(jet["source_error_strip"]) != S or Fraction(jet["finite_spatial_norm_strip"]) != spatial:
            raise ValueError("parameter spatial source width differs")
    return report, zero


from fourfold_monotone_source_prefix import observed_prefix_ready


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=Path, required=True)
    parser.add_argument("--descriptor", type=Path, default=Path(
        "data/phase_ring_continuation/step5_retargeted_reference/descriptor.json"))
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--bits", type=int, default=256)
    parser.add_argument("--follow", action="store_true")
    parser.add_argument("--wait-seconds", type=float, default=15)
    parser.add_argument("--stop-file", type=Path)
    args = parser.parse_args()
    if not 0 < args.wait_seconds <= 60:
        raise ValueError("wait interval must lie in (0,60]")
    ctx.prec = args.bits
    descriptor, descriptor_sha = read(args.descriptor), sha(args.descriptor)
    gridmeta = descriptor["old_forward_reference"]
    if sha(gridmeta["path"]) != gridmeta["sha256"]:
        raise ValueError("the finite reference time partition changed")
    grid = read(gridmeta["path"])
    if grid["segment_count"] != 550:
        raise ValueError("expected the complete 550-segment time grid")
    center = Fraction(descriptor["target_exact_delta_fraction"])
    args.directory.mkdir(parents=True, exist_ok=True)
    C = [[acb(0)] for _ in range(3)]
    D = [[acb(0)] for _ in range(3)]
    processed, evidence, prefix_replays = [], [], []
    last = Time(Fraction(0), Fraction(-1, 2))
    central_A = [arb(0) for _ in range(3)]
    central_E = [arb(0) for _ in range(3)]
    A = [[arb(0) for _ in range(3)] for _ in range(3)]
    E = [[arb(0) for _ in range(3)] for _ in range(3)]
    finite = [[arb(0) for _ in range(3)] for _ in range(3)]
    local = [arb(0) for _ in range(3)]
    outer_moduli, outer_errors = [arb(0) for _ in range(3)], [arb(0) for _ in range(3)]
    scope = None
    started, cpu = time.monotonic(), time.process_time()
    dependencies = {name: sha(Path(__file__).with_name(name)) for name in (
        "fourfold_parameter_ordered_defect.py", "fourfold_parameter_spatial_norms.py",
        "fourfold_forward_density_pipeline_Q1024_v3.py", "fourfold_parameter_density_leaf.py",
        "fourfold_phase_domain_cover_verify.py", "fourfold_monotone_source_prefix.py")}
    while True:
        raw = args.index.read_bytes()
        import json
        index = json.loads(gzip.decompress(raw) if args.index.suffix == ".gz" else raw)
        eta = Fraction(index["uniform_parameter_half_width"])
        S, inner, spatial = map(Fraction, (index["label_strip"], index["inner_strip"], index["spatial_strip"]))
        current_scope = (eta, S, inner, spatial)
        if (index["descriptor_sha256"] != descriptor_sha or eta < 0
            or bool(index["whole_real_parameter_tube"]) != bool(eta)
            or not 0 <= inner < spatial < S
            or scope is not None and current_scope != scope):
            raise ValueError("the accumulating source scope changed")
        scope = current_scope
        entries = index["leaves"]
        if not observed_prefix_ready(entries, processed, complete=bool(index.get("complete"))):
            witness = dict(input_index_sha256=hashlib.sha256(raw).hexdigest(),
                observed_leaves=len(entries), retained_leaves=len(processed),
                all_overlapping_entries_identical=True,
                no_new_integral_or_certificate_published=True)
            if not prefix_replays or prefix_replays[-1] != witness:
                prefix_replays.append(witness)
            if not args.follow or args.stop_file and args.stop_file.exists():
                return
            time.sleep(args.wait_seconds)
            continue
        added = False
        for entry in entries[len(processed):]:
            report, zero = check_leaf(entry, descriptor_sha, center, eta, S, inner, spatial)
            ref = report["identity"]["reference"]
            segment = int(entry["segment"])
            left, right = map(Fraction, entry["normalized_subspan"])
            if not 0 <= segment < 550 or not 0 <= left < right <= 1:
                raise ValueError("invalid source partition cell")
            ta, tb = map(Time.parse, grid["exact_time_endpoints"][segment:segment+2])
            begin, end = ta+(tb-ta).scale(left), ta+(tb-ta).scale(right)
            if begin != last:
                raise ValueError("chronological source partition has a gap or overlap")
            data = report["R82_local_inputs"]
            if data["same_g0_certificate_sha256"] != entry["g0_report_sha256"]:
                raise ValueError("local integrals use a different g0 witness")
            first = [[decode_ball(z) for z in row] for row in data["first_coefficients"]]
            second = [[decode_ball(z) for z in row] for row in data["retained_local_second_coefficients"]]
            C, D = advance_parameter_integrals(C, D, first, second)
            for j, fee in enumerate(data["remaining_local_J0_J1_J2_fees"]):
                local[j] += upper(fee)
            f0, e0, a0, zero_evidence = center_zero_spatial(zero, spatial)
            actual = [None, None, None]
            errors = [None, None, None]
            fin = [f0, None, None]
            for j, item in enumerate(report["density"], 1):
                jets = item["complete_spatial_jet_inputs"]
                actual[j] = list(map(upper, jets["true_integrated_spatial_derivative_SUP_moduli"]))
                errors[j] = list(map(upper, jets["actual_error_derivative_fees"]))
                fin[j] = list(map(upper, jets["finite_integrated_spatial_derivative_moduli"]))
                outer_moduli[j] += upper(item["true_integrated_modulus"])
                outer_errors[j] += upper(item["true_integrated_error"])
            transfer = [(exact_arb(eta)*v).upper() for v in actual[1]]
            actual[0] = [(a+b).upper() for a, b in zip(a0, transfer)]
            errors[0] = [(a+b).upper() for a, b in zip(e0, transfer)]
            for j in range(3):
                central_A[j] += a0[j]
                central_E[j] += e0[j]
                for order in range(3):
                    A[order][j] += actual[order][j]
                    E[order][j] += errors[order][j]
                    finite[order][j] += fin[order][j]
            outer_transfer = exact_arb(eta)*upper(report["density"][0]["true_integrated_modulus"])
            outer_moduli[0] += upper(zero["R72_inputs"]["common_integrated_majorant_A"])+outer_transfer
            outer_errors[0] += upper(zero["R72_inputs"]["integrated_approximation_error_E"])+outer_transfer
            evidence.append(dict(segment=segment, normalized_subspan=[str(left), str(right)],
                parameter_report_path=entry["path"], parameter_report_sha256=entry["sha256"],
                g0_report_path=entry["g0_report_path"], g0_report_sha256=entry["g0_report_sha256"],
                center_g0_spatial=zero_evidence,
                real_parameter_g0_spatial_transfer_fees=records(transfer),
                exact_begin=dict(rational=str(begin.q), pi_coefficient=str(begin.p)),
                exact_end=dict(rational=str(end.q), pi_coefficient=str(end.p))))
            last = end
            processed.append(entry)
            added = True
        whole = bool(index.get("complete") and index.get("whole_forward_leg")
            and index.get("completed_segments") == 550 and last == Time(Fraction(0), Fraction(1, 2)))
        if added or whole:
            identity = dict(retarget_descriptor_sha256=descriptor_sha,
                target_exact_delta_fraction=str(center), exact_parameter_half_width=str(eta),
                exact_parameter_interval=list(map(str, (center-eta, center+eta))),
                fixed_reference_independent_of_parameter=True, whole_real_parameter_tube=bool(eta),
                label_strip=str(S), inner_strip=str(inner), spatial_strip=str(spatial),
                exact_begin=dict(rational="0", pi_coefficient="-1/2"),
                exact_end=dict(rational=str(last.q), pi_coefficient=str(last.p)))
            coeff = dict(kind="complete_finite_parameter_chronological_coefficients", identity=identity,
                C=[[encode_ball(z) for z in row] for row in C],
                D=[[encode_ball(z) for z in row] for row in D],
                all_product_frequencies_retained=True, normalized_label_frequency_k=True,
                no_extra_physical_factor_four=True)
            coefficient_path = args.directory/"coefficients.json.gz"
            save(coefficient_path, coeff)
            finite_sums = [add_rows(a, b) for a, b in zip(C, D)]
            norms = [[row_norms(row, exact_arb(inner))[0] for row in rows] for rows in (C, D, finite_sums)]
            output = dict(kind="actual_parameter_chronological_prefix_with_full_spatial_fees",
                proved=True, complete=whole, whole_forward_leg=whole,
                source_sha256=sha(__file__), dependency_sha256=dependencies, identity=identity,
                input_index_path=str(args.index), input_index_snapshot_sha256=hashlib.sha256(raw).hexdigest(),
                completed_segments=index["completed_segments"], completed_leaves=len(processed),
                coefficients=dict(path=str(coefficient_path), sha256=sha(coefficient_path),
                    bytes=coefficient_path.stat().st_size, C_positive_counts=list(map(len, C)),
                    D_positive_counts=list(map(len, D))),
                signed_zero_modes_C=[encode_ball(row[0]) for row in C],
                signed_zero_modes_D=[encode_ball(row[0]) for row in D],
                finite_C_D_and_sum_A_inner_norms=[records(row) for row in norms],
                omitted_local_integral_fees_A_inner=records(local),
                outer_integrated_common_source_sup_moduli=records(outer_moduli),
                outer_integrated_source_approximation_sup_errors=records(outer_errors),
                spatial_integrated_common_source_sup_moduli_by_parameter_order=[records(row) for row in A],
                spatial_integrated_source_approximation_sup_errors_by_parameter_order=[records(row) for row in E],
                spatial_integrated_finite_source_sup_majorants_by_parameter_order=[records(row) for row in finite],
                central_g0_integrated_common_spatial_sup_moduli=records(central_A),
                central_g0_integrated_spatial_error_fees=records(central_E),
                uniform_g0_transfer=dict(proved=True, actual_parameter_half_width=str(eta),
                    formula_A="A_j(box) <= A_j(center)+eta*B_j(box)",
                    formula_E="E0_j(box) <= E0_j(center)+eta*B_j(box)",
                    fees=records([(exact_arb(eta)*v).upper() for v in A[1]]),
                    orders=[0, 1, 2], central_finite_g0_unchanged=True,
                    only_real_parameter_mean_value_used=True),
                source_error_contract="integrated SUP on the stated strip; finite row norms are A norms; no same-width error promotion",
                chronological_definition="C_i=int ghat_i; D_i=int sum_j binom(i,j) ghat_j,x int_earlier ghat_(i-j)",
                all_cross_segment_g1_g1_and_g0_g2_terms_retained=True,
                every_local_retained_2J11_included=True,
                compatible_controller_prefix_replays=prefix_replays,
                leaves=evidence, wall_seconds=time.monotonic()-started, cpu_seconds=time.process_time()-cpu,
                limitations=["No endpoint composition, twist nonvanishing, or KAM conclusion is asserted.",
                    "Complete is false until the exact whole forward time partition is covered.",
                    "The omitted local fees and R86 true-flow/source-transfer errors remain payable."])
            save(args.directory/"report.json.gz", output)
            print(dict(stage="full_parameter_chronological_accumulator", complete=whole,
                segments=index["completed_segments"], leaves=len(processed),
                half_width=str(eta), C1_zero=str(C[1][0]), D2_zero=str(D[2][0]),
                report_sha256=sha(args.directory/"report.json.gz")), flush=True)
        if whole or not args.follow or args.stop_file and args.stop_file.exists():
            return
        time.sleep(args.wait_seconds)


if __name__ == "__main__":
    main()
