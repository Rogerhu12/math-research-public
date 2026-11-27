"""BNC necessary input: restore the completed DWTB whole exact row carrier.

Only the original8192-point unit-disk input, signed w2048 point carrier,
and192x96 proposal/row arrays are rematerialized. The completed DWT2 and
BR7 error/norm targets are never called. Every entire original SHA is a
hard acceptance condition; no changed carrier is silently substituted.
"""
from __future__ import annotations
import hashlib
import json
import os
from fractions import Fraction
from pathlib import Path

THREADS = ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
           "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def atomic(path, raw):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".partial")
    temporary.write_bytes(raw)
    os.replace(temporary, path)


def exact_string(api, value):
    require(value.is_finite() and value.is_exact(), "one complete exact original dyadic point")
    numerator, exponent = map(int, value.mid().man_exp())
    q = (Fraction(numerator*(1 << exponent)) if exponent >= 0
         else Fraction(numerator, 1 << (-exponent)))
    require(api.rational(q).is_exact() and api.rational(q) == value,
            "the complete rational representation preserves the original point")
    return str(q)


def restore(np, api, context, actual, whole_original_grid_raw, destination, progress):
    """Return the original96 complete rational row trials, never new row science."""
    require(actual["complete"] is actual["proved"] is True
            and actual["failure"] is None and actual["actual_returncode"] == 0
            and actual["saved_record_count"] == 9
            and actual["complete_w_mode_count"] == 2048
            and actual["complete_residual_row_count"] == 96,
            "all original DWTB9 must be genuinely complete before row restoration")
    require(os.environ.get("OPENBLAS_CORETYPE") == "Haswell"
            and all(os.environ.get(name) == "1" for name in THREADS),
            "the complete original deterministic row-proposal runtime")
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    parent = context["AS"]["actual"]
    grid_sha = sha(whole_original_grid_raw)
    grid_expected = parent["private_grid_receipt"]
    require(len(whole_original_grid_raw) == grid_expected["bytes"]
            and grid_sha == grid_expected["sha256"],
            "every byte of the original8192 raw192/G input, no replacement grid")
    grid_body = parse(whole_original_grid_raw)
    require(grid_body["kind"] == "AS_complete_original_G_raw_t_grid_v1"
            and grid_body["complete_count"] == len(grid_body["all_pairs"]) == 8192,
            "the entire original exact finite grid definition")
    grid = [(api.arb(a), api.arb(b)) for a, b in grid_body["all_pairs"]]
    api.midpoint_real = lambda value: value.mid()
    api.midpoint_complex = lambda value: api.acb(value.real.mid(), value.imag.mid())
    kernel = context["UDR_math"].UnitDiskPhaseInput(api, grid)

    def saved_upper(value):
        point = value.upper()
        require(point.is_finite() and point >= 0, "complete original disk upper")
        result = {"ball": point.str(60), "bound": "upper"}
        require(api.arb(result["ball"]).contains(point), "same whole original disk round trip")
        return result

    input_body = {"kind": "UDR_complete_unit_disk_dyadic_phase_input_v1",
        "whole_original_grid_sha256": grid_sha, "complete_nodes": 8192,
        "complete_mean_raw_radius_upper": saved_upper(kernel.raw_radius),
        "all_exact_u_sreal_simag_and_tau_balls": [
            [exact_string(api, kernel.u[m]), exact_string(api, kernel.s[m].real),
             exact_string(api, kernel.s[m].imag), kernel.tau[m].str(90)] for m in range(8192)],
        "phase_modulus_one_is_exact": True, "old_rectangular_power_recurrence_used": False}
    input_raw = canonical(input_body)
    expected = actual["unit_disk_input_receipt"]
    require(len(input_raw) == expected["bytes"] and sha(input_raw) == expected["sha256"],
            "whole original DWTB unit-disk input SHA, not a new input choice")
    input_path = destination/"input_original_DWTB_unit_disk.json"
    atomic(input_path, input_raw)
    require(input_path.read_bytes() == input_raw, "all original disk inputs saved and read")
    formal_input = parse(input_path.read_bytes())
    for m, (u, sr, si, tau) in enumerate(formal_input["all_exact_u_sreal_simag_and_tau_balls"]):
        formal_u = api.rational(Fraction(u))
        formal_s = api.acb(api.rational(Fraction(sr)), api.rational(Fraction(si)))
        formal_tau = api.arb(tau)
        require(formal_u == kernel.u[m] and formal_s == kernel.s[m]
                and formal_tau.contains(kernel.tau[m]), "the same entire formal input at every node")
        kernel.u[m], kernel.uabs[m], kernel.s[m], kernel.tau[m] = (
            formal_u, abs(formal_u).upper(), formal_s, formal_tau.upper())
    kernel.raw_radius = api.arb(formal_input["complete_mean_raw_radius_upper"]["ball"]).upper()
    input_sha = sha(input_raw)
    progress("same_DWTB_whole_unit_disk_input_restored", {"nodes": 8192, "sha256": input_sha})

    global_bounds = parent["global_bounds"]
    omega = api.arb(global_bounds["complete_exact_rotation_ball"])
    phase = api.arb(global_bounds["complete_original_source_phase_ball"])
    pairs = []
    for n in range(1, 2049):
        # Necessary signed INPUT reconstruction only. Neither the old mode
        # error fee nor its scalar accumulators/whole norm targets are called.
        disk = kernel.next()
        reference, unused_divisor = context["DWT_math"].complete_w_reference(api, n, disk, omega, phase)
        point = api.acb(reference.real.mid(), reference.imag.mid())
        pairs.append([exact_string(api, point.real), exact_string(api, point.imag)])
        if n % 64 == 0:
            progress("restoring_same_complete_DWTB_signed_w_input",
                     {"complete_input_modes": n, "total_input_modes": 2048,
                      "completed_old_DWT_BR_scientific_targets_called": 0})
    require(len(pairs) == 2048, "all original signed w point inputs before the row proposal")
    wbody = {"kind": "DWT_complete_direct_true_target_w_exact_trial_v1",
        "positive_modes": 2048, "all_positive_exact_pairs": pairs,
        "exact_mean": "0", "negative_modes_are_exact_conjugates": True,
        "same_original_w_equals_vi_minus_alpha": True,
        "whole_original_grid_sha256": grid_sha, "new_unit_disk_input_sha256": input_sha}
    wraw = canonical(wbody)
    expected_w = actual["private_w_trial_receipt"]
    require(len(wraw) == expected_w["bytes"] and sha(wraw) == expected_w["sha256"],
            "all2048 signed w modes match their original whole carrier SHA")
    wpath = destination/"input_original_DWTB_w.json"
    atomic(wpath, wraw)
    require(wpath.read_bytes() == wraw, "the entire matched original w point carrier saved/read")
    pairs = parse(wpath.read_bytes())["all_positive_exact_pairs"]

    phase_text = (phase-omega).str(90)
    require(phase_text == actual["complete_true_phase_a_ball"],
            "the entire original target phase a=b-Omega is unchanged")
    phase_a = api.arb(phase_text)
    trial_raw, selection = context["proposal"].choose_trial_bytes(np, pairs, float(phase_a.mid()))
    expected_trial = actual["private_trial_receipt"]
    require(selection == actual["trial_selection"] and len(trial_raw) == expected_trial["bytes"]
            and sha(trial_raw) == expected_trial["sha256"]
            and expected_trial["shape"] == [192, 96, 2] and expected_trial["dtype"] == "<f8",
            "every original192x96 trial coefficient and the original proposal identity")
    trial_path = destination/"input_original_DWTB_y.f64"
    atomic(trial_path, trial_raw)
    require(trial_path.read_bytes() == trial_raw, "the whole exact original row-proposal array saved/read")
    values = np.frombuffer(trial_path.read_bytes(), dtype="<f8").reshape(192, 96, 2)
    require(bool(np.isfinite(values).all()), "all complete original row coefficients are finite")
    rows = []
    for j in range(96):
        row = []
        for n in range(1, 193):
            a, b = (Fraction.from_float(float(value)) for value in values[n-1, j])
            row.append([str(a/(4*n)), str(b/(4*n))])
        rows.append(row)
    row_body = {"kind": "BR_complete_original_target_B_inverse_exact_row_trial_v1", "rows": 96,
        "positive_modes": 192, "all_positive_exact_pairs": rows, "exact_mean": "0",
        "negative_modes_are_exact_conjugates": True, "row_definition": "G*y_j; coefficient multiplier1/(4*n)"}
    row_raw = canonical(row_body)
    expected_rows = actual["private_row_trial_receipt"]
    require(len(row_raw) == expected_rows["bytes"] and sha(row_raw) == expected_rows["sha256"]
            and expected_rows["rows"] == 96 and expected_rows["positive_modes"] == 192,
            "the entire original exact rational row carrier SHA is mandatory")
    row_path = destination/"input_original_DWTB_rows.json"
    atomic(row_path, row_raw)
    require(row_path.read_bytes() == row_raw, "all96 entire rational row representatives saved/read")
    rows = parse(row_path.read_bytes())["all_positive_exact_pairs"]
    receipt = {"kind": "BNC_same_complete_DWTB_row_carrier_restoration_v1", "complete": True,
        "unit_disk_input": expected, "signed_w_trial": expected_w, "y_trial": expected_trial,
        "row_trial": expected_rows, "original_trial_selection": selection,
        "old_DWT_coefficient_error_targets_called": 0,
        "old_DWT_whole_error_targets_called": 0, "old_BR_residual_norm_targets_called": 0,
        "new_row_trial_selected": False, "all_complete_original_carrier_SHA_matched": True}
    progress("same_complete_DWTB_row_carrier_SHA_restored", {"rows": 96, "positive_modes": 192,
                                                         "sha256": sha(row_raw)})
    return rows, receipt
