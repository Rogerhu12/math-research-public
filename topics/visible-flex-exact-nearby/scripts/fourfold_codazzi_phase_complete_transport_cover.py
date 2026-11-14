#!/usr/bin/env python3
"""Consume the exact chronological phase-transport checkpoints.

The complete consumer reuses every saved all-frequency residual; it does
not rerun the transport or discard its even mean. A prefix cannot confer
any true return, conjugacy-defect, or parameter-transversality conclusion.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path
import time

from flint import arb, acb_poly, ctx
import fourfold_codazzi_phase_full_transport_Taylor as producer
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha

PRODUCER = "3254a9225f4933ae11ffbfa1862a50ed1c7c585f03aa11e56606ad758ccc6961"
COVER = "94492bbafda1e5efb30b129e534171c9fc305524a2d972064e34e8894948bad3"
ROOT = "1910bdc2ee84cd23a7a92d94689d8cd90a3a5c25cf56caa3cc585159a9c5af43"
CANDIDATE = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
REPAIR = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
TERMS = (
    ("retained", "complete_retained_finite_residual"),
    ("unretained", "complete_unretained_finite_residual"),
    ("scalar", "complete_true_scalar_model_residual"),
)


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == ".gz" else raw)


def decode_state(encoded, modes):
    if len(encoded) != 2 or any(len(side) != 2 * modes + 1 for side in encoded):
        raise ValueError("a complete two-leg phase state is required")
    result = [[(Fraction(a), Fraction(b)) for a, b in side] for side in encoded]
    for side in result:
        if side[modes][1] != 0:
            raise ValueError("a phase mean is not real")
        for j in range(1, modes + 1):
            a, b = side[modes + j]
            if side[modes - j] != (a, -b):
                raise ValueError("the exact finite phase lacks conjugate symmetry")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--transport-dir", type=Path, required=True)
    parser.add_argument("--scalar-cover", type=Path, required=True)
    parser.add_argument("--root-contract", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--allow-prefix", action="store_true")
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("preserve every actual completed cover consumer")
    started = time.monotonic()
    ctx.prec = 320
    if sha(producer.__file__) != PRODUCER:
        raise ValueError("the original mathematical transport source changed")
    if sha(args.scalar_cover) != COVER or sha(args.root_contract) != ROOT:
        raise ValueError("the original complete scalar or root certificate changed")
    cover, root = read(args.scalar_cover), read(args.root_contract)
    if not cover["complete"] or not root["complete"] or cover["germ_count"] != 169:
        raise ValueError("the original complete scalar and root certificates are required")
    inputs = {g["germ_index"]: g for g in cover["germs"]}
    if sorted(inputs) != list(range(169)):
        raise ValueError("the original scalar cover does not contain every genuine germ")

    checkpoints = sorted(args.transport_dir.glob("transport-germ[0-9][0-9][0-9][0-9].json.gz"))
    if not checkpoints or len(checkpoints) > 169:
        raise ValueError("a nonempty actual prefix of at most169 germs is required")
    if not args.allow_prefix and len(checkpoints) != 169:
        raise ValueError("a whole-return consumer requires all169 completed chronological germs")
    cfg = None
    cursor = Fraction(0)
    totals = {name: arb(0) for name, _ in TERMS}
    count = 0
    rejected = 0
    maximum_depth = 0
    native = []
    previous_piece = -1
    for index, path in enumerate(checkpoints):
        if path.name != f"transport-germ{index:04d}.json.gz":
            raise ValueError("a transport germ is missing or out of chronological order")
        raw = path.read_bytes()
        doc = json.loads(gzip.decompress(raw))
        if cfg is None:
            cfg = doc["configuration"]
            if (cfg["source_sha256"] != PRODUCER or cfg["candidate_sha256"] != CANDIDATE
                    or cfg["derived_definition_sha256"] != REPAIR or cfg["root_contract_sha256"] != ROOT
                    or cfg["scalar_configuration"] != cover["configuration"]
                    or cfg["exact_eta_offset"] != "0" or cfg["whole_original_eta"]
                    or cfg["residual_strip"] != "1/32" or cfg["modes"] != 64
                    or cfg["time_degree"] != 12 or cfg["bits"] != 256
                    or cfg["full_output_frequency_bound"] != 128
                    or cfg["exact_initial_H_sine_coefficients"] != root["exact_H_sine_coefficients"]
                    or cfg["exact_initial_H_cosine_coefficients"] != root["exact_H_cosine_coefficients"]):
                raise ValueError("the original full-frequency transport configuration differs")
        if (doc["configuration"] != cfg or not doc["complete_requested_prefix"]
                or doc["last_complete_germ"] != index
                or doc["exact_all_polynomial_value_jumps"] != "0"
                or doc["exact_initial_polynomial_error"] != "0"):
            raise ValueError("a completed original source/configuration/continuity gate differs")
        a, b = map(Fraction, inputs[index]["exact_interval"])
        if a != cursor or b <= a or not doc["rows"]:
            raise ValueError("a complete transport germ leaves a gap or has no actual steps")
        local = {name: arb(0) for name, _ in TERMS}
        for row in doc["rows"]:
            left, right = map(Fraction, row["interval"])
            if (row["germ_index"] != index or row["scalar_native_sha256"] != inputs[index]["sha256"]
                    or left != cursor or right <= left or right > b
                    or not row["exact_initial_value_shared_with_previous_endpoint"]
                    or row["actual_candidate_piece"] < previous_piece
                    or not 0 <= row["actual_candidate_piece"] <= 2549
                    or len(row["polynomial_sha256"]) != 64):
                raise ValueError("an actual transport step changes input identity or radial cover")
            for name, key in TERMS:
                bound = box_from_record(row[key]).upper()
                if not bound.is_finite() or not bound >= 0:
                    raise ArithmeticError("a complete source residual bound is invalid")
                totals[name] += bound
                local[name] += bound
            if len(row["both_derivative_integrals"]) != 2:
                raise ValueError("a true coefficient-model fee omits one principal leg")
            maximum_depth = max(maximum_depth, row["depth"])
            previous_piece = row["actual_candidate_piece"]
            cursor = right
            count += 1
        if cursor != b or Fraction(doc["last_exact_radial_point"]) != b:
            raise ValueError("a complete germ omits its exact endpoint")
        state = decode_state(doc["exact_phase_state"], cfg["modes"])
        rejected += len(doc["rejected_cells"])
        native.append(dict(germ_index=index, path=str(path), sha256=sha(path),
            exact_interval=[str(a), str(b)], actual_steps=len(doc["rows"]),
            scalar_native_sha256=inputs[index]["sha256"],
            complete_reconsumed_residuals={name: record(value.upper()) for name, value in local.items()}))

    whole = len(checkpoints) == 169 and cursor == Fraction(root["exact_scalar_stop"])
    residual = sum(totals.values(), arb(0)).upper()
    modes = cfg["modes"]
    difference = acb_poly([producer.cplx((state[1][j][0] - state[0][j][0],
        state[1][j][1] - state[0][j][1])) for j in range(2 * modes + 1)])
    width = exact_arb(Fraction(1, 32))
    terminal_mean = state[1][modes][0] - state[0][modes][0]
    difference[modes] = 0
    nonmean = producer.angular_norm(difference, modes, width)
    fit = exact_arb(Fraction(root["exact_proposed_rotation"]))
    old = arb.pi() / 2 * (arb(612575) - arb(5).sqrt()) / 2228182
    new = arb.pi() / 2 * (arb(45217079201) - arb(5).sqrt()) / 164472125458
    terminal = {name: (nonmean + abs(exact_arb(terminal_mean) - value)).upper()
                for name, value in (("fit", fit), ("old", old), ("bounded7_new", new))}
    sliver = box_from_record(root["full_two_ray_conjugacy_defect_sliver"]).upper()
    defects = {name: (value + residual + sliver).upper() for name, value in terminal.items()} if whole else None
    # The exact terminal mean can serve as an arbitrary real target in
    # the proved transport formula. Subtract it BEFORE applying Cauchy;
    # target mismatch is constant and makes no angular-derivative fee.
    constant_free = (nonmean + residual + sliver).upper() if whole else None
    derivative = (64 * constant_free).upper() if whole else None
    gates = [dict(name=name, passed=bool(ok)) for name, ok in (
        ("the exact original source and scalar/root input identities are retained", cfg["source_sha256"] == PRODUCER),
        ("every consumed genuine germ occurs once in chronological order", len(native) == len(checkpoints)),
        ("all consumed radial intervals and complete two-leg model fees are retained", count > 0),
        ("every projected-out finite Fourier product is included", cfg["full_output_frequency_bound"] == 128),
        ("the even phase means and exact rational endpoint are retained", state[0][modes][1] == state[1][modes][1] == 0),
        ("the true parameter scope remains eta_0 and the unchanged compact nu", cfg["exact_eta_offset"] == "0"),
        ("the claimed output scope agrees with the actually complete radial coverage", whole or args.allow_prefix),
    )]
    report = dict(kind="actual_chronological_full_frequency_phase_transport_cover",
        complete=all(g["passed"] for g in gates), whole_negative_domain=whole,
        source_sha256=sha(__file__), original_producer_sha256=PRODUCER,
        scalar_cover_sha256=COVER, root_contract_sha256=ROOT,
        configuration=cfg, exact_processed_interval=["0", str(cursor)],
        complete_transport_germs=len(native), actual_steps=count,
        original_rejected_cell_count=rejected, maximum_adaptive_depth=maximum_depth,
        reconsumed_complete_residuals={name: record(value.upper()) for name, value in totals.items()},
        integrated_complete_true_transport_residual=record(residual),
        exact_all_polynomial_value_jumps="0", exact_initial_polynomial_error="0",
        exact_terminal_phase_state=producer.encode(state), exact_terminal_phase_mean=str(terminal_mean),
        complete_terminal_nonmean_norm=record(nonmean),
        complete_terminal_norms_by_target={name: record(value) for name, value in terminal.items()},
        root_sliver_bound=record(sliver), actual_input_strip="1/64", terminal_and_residual_strip="1/32",
        complete_actual_defects_by_target=None if defects is None else {name: record(value) for name, value in defects.items()},
        constant_free_true_defect_bound=None if constant_free is None else record(constant_free),
        complete_real_angular_derivative_defect_bound=None if derivative is None else record(derivative),
        Cauchy_angular_derivative_factor="64", target_shift_has_zero_derivative=True,
        new_target_true_E_below_one_millionth=bool(whole and defects["bounded7_new"] < exact_arb(Fraction(1, 10**6))),
        true_Ephi_below_one_ten_thousandth=bool(whole and derivative < exact_arb(Fraction(1, 10**4))),
        fitted_rotation_not_declared_true=True, true_conjugacy_itself_not_claimed=True,
        no_parameter_KAM_or_PDE_branch_or_global_inverse_claimed=True,
        exact_finite_transport_not_recomputed=True, germs=native, gates=gates,
        seconds=time.monotonic() - started,
    )
    save(args.out, report)
    print(dict(complete=report["complete"], whole=whole, germs=len(native), steps=count,
        full_residual=residual.str(20), terminal_nonmean=nonmean.str(20),
        new_target_defect=None if defects is None else defects["bounded7_new"].str(20),
        derivative=None if derivative is None else derivative.str(20), seconds=report["seconds"]), flush=True)
    if not report["complete"]:
        raise ArithmeticError("an actual chronological full-frequency phase-cover gate failed")


if __name__ == "__main__":
    main()
