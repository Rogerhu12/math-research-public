#!/usr/bin/env python3
"""New signed true-metric terminal-mean moments; public Actions only.

Read the old complete scalar-mean native and CP conclusions.  Reuse CP's
abar, bbar and H endpoint.  No old producer, H solve, mean retraction,
primitive, DFT, ordinary nu-source norm or nonmean inverse is called.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from math import comb
import os
from pathlib import Path
import time
import traceback

REPO = "Rogerhu12/math-research-public"
KIND = "R144_signed_true_metric_terminal_mean_moments_v1"
NATIVE = "e233ece0f264eb73f93dfe5b43c5d45b4d5d6db06da2418b9c20fb545a01889b"
CP = "0ce421d4a1e14a57915531261c531ce8231a8874aba5dfd704d37f67bb8d7641"
CANDIDATE = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
ALPHA = "6890507429876859/9007199254740992"
NU = "-2572625729470897/72057594037927936"
ETA = "-7789843107295549/4611686018427387904"
LEFT, MID, RIGHT = Fraction(1, 20), Fraction(23, 200), Fraction(9, 50)
PREFIX_NAMES = ("I_U", "E0", "E1", "E2", "A3")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False) + "\n").encode()


def atomic(path, value):
    raw = encode(value)
    require(len(raw) < 30000, "one complete small scalar outcome")
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_bytes(raw)
    os.replace(temporary, path)


def chi(x):
    require(LEFT <= x <= RIGHT, "exact compact polynomial coordinate")
    t = (x - LEFT) / (RIGHT - LEFT)
    return 4096 * t**6 * (1 - t)**6


def chi_mass(left, right, power):
    require(LEFT <= left < right <= RIGHT and power in (1, 3),
            "declared exact nonnegative polynomial mass")
    a, b = (left - LEFT) / (RIGHT - LEFT), (right - LEFT) / (RIGHT - LEFT)
    d = 6 * power
    result = (RIGHT - LEFT) * 4096**power * sum(
        (Fraction((-1)**j * comb(d, j), d + j + 1)
         * (b**(d+j+1) - a**(d+j+1)) for j in range(d+1)), Fraction(0))
    require(result > 0, "positive exact compact polynomial mass")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mean", type=Path, required=True)
    parser.add_argument("--cp", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO,
            "scientific arithmetic only in the authorized public Actions repository")
    require(not args.output.exists(), "preserve an existing completed or partial target")
    from flint import arb, ctx
    ctx.prec = 320
    began = time.monotonic()

    def rat(value):
        value = Fraction(value)
        return arb(value.numerator) / value.denominator

    def interval(lo, hi):
        return rat(lo).union(rat(hi))

    def old(value):
        result = arb(value["lower"]).lower().union(arb(value["upper"]).upper())
        require(result.is_finite(), "finite complete original row interval")
        return result

    def unpack(value):
        e = int(value["decimal_exponent"])
        scale = rat(Fraction(10)**e)
        middle = rat(int(value["midpoint_integer"])) * scale
        radius = rat(int(value["radius_integer"])) * scale
        return (middle-radius).lower().union((middle+radius).upper())

    def record(value):
        require(value.is_finite(), "finite new signed interval")
        middle, radius, exponent = value.mid_rad_10exp(75)
        result = dict(kind="complete_decimal_ball_v1",
                      mathematical_direction="enclosure",
                      midpoint_integer=str(int(middle)),
                      radius_integer=str(int(radius)),
                      decimal_exponent=str(int(exponent)))
        require(unpack(result).contains(value), "saved ball contains directed expression")
        return result

    def nonnegative(value):
        require(value.upper() >= 0, "saved range excludes its known nonnegative value")
        return max(arb(0), value.lower()).lower().union(value.upper())

    doc = dict(
        kind=KIND, source_sha256=sha(Path(__file__).read_bytes()),
        run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        identity=dict(candidate_sha256=CANDIDATE, mean_native_sha256=NATIVE,
                      cp_sha256=CP, exact_alpha=ALPHA, exact_nu=NU, exact_eta=ETA,
                      original_modes=32, original_rows=7721, original_mean_joins=6143,
                      original_affine_parameter_half_width="1/1000000000"),
        parameters=dict(arithmetic_bits=320, compact_interval=["1/20", "9/50"],
                        exact_derivative_sign_split="23/200",
                        xi_enclosure=["-1/1250000000000", "-7/10000000000000"],
                        waist_radius_enclosure=["1.06873282", "1.068732841"],
                        integrating_factor="H'=2 beta U H; H(0)=1",
                        integrating_factor_input="saved CP whole endpoint and monotonicity only",
                        moment_order=["M0", "M1", "M2"],
                        kappa_formula="a0*(M0+2*xi*M1+xi^2*M2)/2",
                        control_ratio_formula="-(M0+2*xi*M1+xi^2*M2)/(abar+2*xi*bbar)"),
        complete=False, proved=False, failure=None, stage="input",
        completed_original_rows=0, completed_original_mean_joins=0,
        completed_compact_rows=0, completed_signed_subcells=0,
        completed_compact_candidate_joins=0, current_compact_right="1/20",
        prefix_scope="not a complete moment",
        prefix_integrals={}, complete_new_scalars={}, old_saved_inputs={},
        gates=dict(kappa_nu_interval_excludes_zero="unknown"),
        scope=dict(exact_mean_compact_centre=True,
                   true_metric_parameter_not_density_parameter=True,
                   old_affine_box_only_encloses_its_fixed_centre=True,
                   all_original_compact_pieces_and_jumps_retained=True,
                   signed_derivative_mass_split_before_interval_multiplication=True,
                   old_positive_moments_read_only=True,
                   old_integrating_factor_target_read_only=True,
                   ordinary_candidate_derivatives_not_substituted_by_PDE=True,
                   nonzero_scalar_is_not_full_Schur=True,
                   physical_parameter_response_proved=False,
                   full_nonmean_inverse_proved=False,
                   final_topic_complete=False),
        old_scientific_targets_recomputed=0, old_producers_called=0,
        old_H_ODE_calls=0, old_mean_retraction_calls=0,
        old_ordinary_nu_source_norm_calls=0, primitive_or_DFT_calls=0,
        new_arrays_published=0, seconds=0)
    sums = {name: arb(0) for name in PREFIX_NAMES}

    def save():
        doc["seconds"] = time.monotonic() - began
        atomic(args.output, doc)

    try:
        save()
        mean_raw, cp_raw = args.mean.read_bytes(), args.cp.read_bytes()
        require(sha(mean_raw) == NATIVE and sha(cp_raw) == CP,
                "same complete original mean native and saved CP result")
        native, cp = json.loads(gzip.decompress(mean_raw)), json.loads(cp_raw)
        require(native["complete"] is True and native["failure"] is None
                and native["candidate_sha256"] == CANDIDATE
                and native["exact_amplitude"] == ALPHA and native["exact_nu"] == NU
                and native["candidate_metadata"]["modes"] == 32
                and native["original_parameter_half_width"] == "1/1000000000"
                and native["whole_original_affine_parameter_interval"] is True
                and native["all_exact_mean_interfaces_retained"] is True
                and len(native["rows"]) == 7721 and len(native["interfaces"]) == 6143,
                "complete original object and whole closed piece cover")
        require(cp["complete"] is True and cp["failure"] is None
                and cp["identity"]["original_candidate_sha256"] == CANDIDATE
                and cp["identity"]["exact_eta"] == ETA
                and cp["identity"]["exact_nu"] == NU
                and cp["completed_compact_cells"] == 1156,
                "same actual completed CP compact conclusions")
        saved = cp["complete_new_scalars"]
        abar, bbar = unpack(saved["abar"]), unpack(saved["bbar"])
        Hright = unpack(saved["H_at_compact_right"])
        mean_floor = unpack(saved["mean_abs_lower"]).lower()
        require(abar > 0 and bbar >= 0 and Hright > 1 and mean_floor > 0,
                "saved complete positive moments, H endpoint and mean floor")
        invH = (1 / Hright.upper()).lower().union(arb(1))
        doc["old_saved_inputs"] = {name: saved[name] for name in
                                  ("abar", "bbar", "H_at_compact_right", "mean_abs_lower")}
        rows, joins = native["rows"], native["interfaces"]
        join_map = {item["common_row"]: item for item in joins}
        previous_piece, rightmost = None, Fraction(0)
        doc["stage"] = "new_signed_compact_integrals"

        for index, row in enumerate(rows):
            left, right = map(Fraction, row["interval"])
            piece = int(row["candidate_piece"])
            require(row["common_row"] == index and left == rightmost and left < right,
                    "unchanged complete original common-row order")
            changed = previous_piece is not None and piece != previous_piece
            require((index in join_map) is changed, "every actual original candidate interface")
            if changed:
                item = join_map[index]
                require(piece == previous_piece + 1 and item["candidate_join"] == piece
                        and Fraction(item["radius"]) == left,
                        "original signed one-sided interface identity")
            doc["completed_original_rows"] = index + 1
            doc["completed_original_mean_joins"] += int(changed)
            rightmost, previous_piece = right, piece
            if right <= LEFT or left >= RIGHT:
                continue
            require(LEFT <= left < right <= RIGHT
                    and left == Fraction(doc["current_compact_right"]),
                    "whole compact support with every original piece and no crossing cut")
            target, state = row["actual_target"], row["scalar_mean"]
            a = old(target["a"])
            beta = nonnegative(old(target["beta"]))
            minusK = nonnegative(-old(target["K"]))
            gamma = old(target["gamma"])
            minusm = -old(state["actual_m"])
            require(a > 0 and gamma > 0 and minusm > 0,
                    "original actual metric and nonzero raw mean")
            ml = max(mean_floor, minusm.lower()).lower()
            require(ml <= minusm.upper(), "point mean floor compatible with the row")
            minusm = ml.union(minusm.upper())
            U = nonnegative(old(state["nonmean_u_square"]))
            V = nonnegative(old(state["nonmean_v_square"]))
            q = V / minusm**2
            rho = beta**2 / gamma**2
            rho_prime = 2 * beta * a**2 * minusK
            coefficient_U = rho * beta * U * invH
            coefficient_E = rho * q * invH
            coefficient_A3 = rho_prime * q * invH
            cuts = [left] + ([MID] if left < MID < right else []) + [right]
            for start, stop in zip(cuts, cuts[1:]):
                sums["I_U"] += coefficient_U * rat(chi_mass(start, stop, 1))
                sums["A3"] += coefficient_A3 * rat(chi_mass(start, stop, 3))
                ca, cb = chi(start), chi(stop)
                for n in range(3):
                    mass = (cb**(n+1) - ca**(n+1)) / (n+1)
                    require((stop <= MID and mass >= 0)
                            or (start >= MID and mass <= 0),
                            "one sign for the exact derivative mass")
                    sums["E"+str(n)] += coefficient_E * rat(mass)
                doc["completed_signed_subcells"] += 1
            doc["completed_compact_rows"] += 1
            doc["completed_compact_candidate_joins"] += int(changed and LEFT < left < RIGHT)
            doc["current_compact_right"] = str(right)
            doc["prefix_integrals"] = {name: record(value) for name, value in sums.items()}
            save()

        require(rightmost == Fraction(25, 8) and previous_piece == 6143
                and doc["completed_original_mean_joins"] == 6143
                and doc["completed_compact_rows"] == 1156
                and Fraction(doc["current_compact_right"]) == RIGHT,
                "complete original body identity and full new compact integrals")
        M0 = -2 * sums["I_U"] - abar / 2 - sums["E0"]
        M1 = -bbar - sums["E1"]
        M2 = -sums["A3"] - sums["E2"]
        xi = interval("-0.0000000000008", "-0.0000000000007")
        a0 = interval("1.06873282", "1.068732841")
        polynomial = M0 + 2 * xi * M1 + xi**2 * M2
        denominator = abar + 2 * xi * bbar
        require(denominator > 0, "same proved compact-control denominator")
        kappa_nu = a0 * polynomial / 2
        values = dict(sums, M0=M0, M1=M1, M2=M2,
                      normalized_metric_waist_polynomial=polynomial,
                      kappa_nu=kappa_nu, density_control_metric_derivative=-polynomial/denominator)
        doc["complete_new_scalars"] = {name: record(value) for name, value in values.items()}
        doc["gates"]["kappa_nu_interval_excludes_zero"] = bool(
            kappa_nu.lower() > 0 or kappa_nu.upper() < 0)
        doc["prefix_scope"] = "complete compact integrals; original piecewise data retained"
        doc["stage"], doc["complete"], doc["proved"] = "complete_signed_metric_mean_moments", True, True
        save()
        print(json.dumps(dict(complete=True, compact_rows=doc["completed_compact_rows"],
                              signed_subcells=doc["completed_signed_subcells"],
                              kappa_nu_interval_excludes_zero=doc["gates"]["kappa_nu_interval_excludes_zero"],
                              full_nonmean_inverse_proved=False), sort_keys=True), flush=True)
        return 0
    except Exception as exc:
        doc["failure"] = dict(type=type(exc).__name__, message=str(exc),
                              traceback=traceback.format_exc()[-6000:])
        doc["stage"] = "failed_with_true_saved_prefix"
        save()
        print(json.dumps(dict(complete=False, failure=doc["failure"],
                              completed_compact_rows=doc["completed_compact_rows"])), flush=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
