#!/usr/bin/env python3
"""Original pure Hurwitz coordinates: proved R981 residue/digit methods.

Mathematical execution is restricted to this public repository's GitHub Actions.
Local use is restricted to reading, AST parsing, and hashing this source.
The source is y^2=x^3+1, omega=dx/(2y), g2=0, g3=-4.
R973 balanced coefficients and its B values are consumed as fixed old data.
No original supersingular trace, same-h sigma product, or old c_n is recomputed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import multiprocessing
import os
from pathlib import Path
import queue
import sys
import time
import traceback


PRIMES = (41, 47, 227, 857)
EXACT_PRIMES = (41, 47)
OLD_R973 = {
    41: {"balanced_minus": 13, "B_minus": 11},
    47: {"balanced_minus": 4, "B_minus": 10},
    227: {"balanced_minus": 171, "B_minus": 179},
    857: {"balanced_minus": 317, "B_minus": 489},
}
MAX_BUDGET_SECONDS = 620.0
METHOD_PATH = "topics/serre-uniformity/results/R981-original-pure-Hurwitz-residue-compression.md"


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def digest(value):
    return hashlib.sha256(encoded(value)).hexdigest()


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def strip_p(value, p):
    valuation = 0
    while value % p == 0:
        value //= p
        valuation += 1
    return valuation, value


def rational_pair(value):
    return [str(value.numer()), str(value.denom())]


def rational_mod(value, p):
    numerator, denominator = int(value.numer()), int(value.denom())
    require(denominator % p != 0, f"nonintegral rational reduction at p={p}")
    return numerator % p * pow(denominator % p, -1, p) % p


def rational_valuation(value, p):
    numerator, denominator = int(value.numer()), int(value.denom())
    if numerator == 0:
        return None
    nv, _ = strip_p(abs(numerator), p)
    dv, _ = strip_p(denominator, p)
    return nv - dv


def index_contract(p):
    require(p >= 41 and p % 6 == 5 and p % 9 in (2, 5),
            "prime outside the original scope")
    r = 2 if p % 12 == 11 else 8
    a, n = r + 1, p - r
    specs = {
        "low": (a * (p - 1), a + 1, -a),
        "low_star": (a * (p - 1) + p + 1, a, -a - 1),
        "high": (n * (p - 1), 1 - r, a),
        "high_star": (n * (p - 1) + p + 1, -r, r),
    }
    if p in EXACT_PRIMES:
        for j in (3, 6):
            index = (p + 1 - j) * (p - 1) + p + 1
            specs[f"probe_j{j}"] = (index, 1 - j, j - 1)
    for label, (index, u, v) in specs.items():
        require(index % 6 == 0 and 6 <= index < p * p - 1,
                f"bad original index {label}, p={p}")
        require((index - 1) % p != 0, f"singular residue denominator {label}")
        require((1 - index - u - p * v) % (p * p) == 0,
                f"incorrect exponent decomposition {label}")
    return r, a, n, specs


def digit_inputs(p, cutoff):
    """R981 two-digit Lucas/Wilson construction, including the p resonance."""
    d, e = (p - 1) // 2, (5 * p - 1) // 6
    require(cutoff < (p * p - 1) // 6, "first nonintegral log term included")
    small = [1]
    for j in range(d):
        small.append(-small[-1] * (2 * j + 1) * pow(2 * j + 2, -1, p) % p)
    require(small[d] == 1, "low binomial normalization failed")
    A = [small[j] * pow(6 * j + 1, -1, p) % p for j in range(d + 1)]
    factorial = [1]
    for j in range(1, p):
        factorial.append(factorial[-1] * j % p)
    sign = -1 if (e + 1) % 2 else 1
    resonance = (sign * pow(pow(4, e, p), -1, p)
                 * factorial[2 * e - p]
                 * pow(factorial[e] * factorial[e] % p, -1, p)) % p
    require(resonance != 0, "resonance constant vanished")
    f = [0] * (cutoff + 1)
    C = [0] * (cutoff + 1)
    resonant_indices = []
    for i in range(cutoff // p + 1):
        require(2 * i + 1 < p, "upper digit bound failed")
        for b in range(min(d, cutoff - i * p) + 1):
            j = i * p + b
            f[j] = small[i] * A[b] % p
            C[j] = small[i] * small[b] % p
        j = i * p + e
        if j <= cutoff:
            require((6 * i + 5) % p != 0, "excluded q-th log term reached")
            f[j] = resonance * (2 * i + 1) * small[i] * pow(6 * i + 5, -1, p) % p
            resonant_indices.append(j)
    require(f[0] == C[0] == 1, "wrong constant coefficients")
    return f, C, A, {
        "resonance_constant": resonance,
        "resonance_count": len(resonant_indices),
        "resonance_indices_sha256": digest(resonant_indices),
        "A_coefficients": len(A),
        "upper_digit_coefficients": cutoff // p + 1,
        "A_sha256": digest(A),
    }


def stripped_inputs(p, cutoff):
    """Independent exact valuation/unit recurrence for binom(-1/2,j)."""
    f, C = [], []
    valuation, unit = 0, 1
    resonance_count = 0
    for j in range(cutoff + 1):
        require(valuation in (0, 1), f"unexpected central-binomial valuation at {j}")
        C.append(unit if valuation == 0 else 0)
        dv, denominator_unit = strip_p(6 * j + 1, p)
        fv = valuation - dv
        require(fv >= 0, f"nonintegral original log coefficient at {j}")
        f.append(unit * pow(denominator_unit % p, -1, p) % p if fv == 0 else 0)
        if dv:
            require(dv == 1 and valuation == 1, "unexpected denominator resonance")
            resonance_count += 1
        if j != cutoff:
            nv, numerator_unit = strip_p(2 * j + 1, p)
            dv, denominator_unit = strip_p(2 * j + 2, p)
            valuation += nv - dv
            unit = -unit * (numerator_unit % p) * pow(denominator_unit % p, -1, p) % p
    return f, C, resonance_count


def signed_power(poly, exponent, length):
    if exponent < 0:
        return poly.inverse_series_trunc(length).pow_trunc(-exponent, length)
    return poly.pow_trunc(exponent, length)


def bounded_residue(p, index, u, v, fpoly, Cpoly, Apoly):
    """One fixed power, one low Frobenius power, then a linear contraction."""
    M = index // 6
    ordinary = Cpoly.mul_low(signed_power(fpoly, u, M + 1), M + 1)
    frobenius = signed_power(Apoly, v, M // p + 1)
    coefficient = sum(int(frobenius[j]) * int(ordinary[M - p * j])
                      for j in range(M // p + 1)) % p
    return coefficient * pow((index - 1) % p, -1, p) % p


def positive_residue(p, index, fpoly, Cpoly):
    M = index // 6
    exponent = p * p + 1 - index
    require(exponent > 0, "positive exponent channel left its range")
    ordinary = fpoly.pow_trunc(exponent, M + 1)
    coefficient = int(Cpoly.mul_low(ordinary, M + 1)[M])
    return coefficient * pow((index - 1) % p, -1, p) % p


def lagrange_check(p, index, fpoly, target):
    M = index // 6
    coefficient = int(fpoly.pow_trunc(p * p + 2 - index, M + 1)[M])
    if (index - 2) % p == 0:
        return {
            "kind": "singular_N_minus_2",
            "coefficient_mod_p": coefficient,
            "check": coefficient == 0,
            "used_to_assign_G": False,
        }
    value = -2 * coefficient * pow((index - 1) * (index - 2) % p, -1, p) % p
    return {
        "kind": "nonsingular_lagrange",
        "value_mod_p": value,
        "check": value == target,
        "used_to_assign_G": False,
    }


def exact_wp_prefix(maximum, fmpq):
    """Independent rational source: wp''=6 wp^2, g3=-4."""
    zero = fmpq(0)
    x = [zero] * (maximum + 1)
    x[1] = fmpq(-1, 7)
    for j in range(2, maximum + 1):
        x[j] = sum((x[i] * x[j - i] for i in range(1, j)), zero)
        x[j] /= (6 * j + 1) * (j - 1)
    require(x[2] == fmpq(1, 637), "wrong original rational Laurent scale")
    return x


def mixed_probe(p, j, c_plus, G, beta):
    """Unproved candidate only: no equality or nonzero assertion is made."""
    factorial = 1
    for i in range(1, j - 1):
        factorial = factorial * i % p
    sign = -1 if (j + 1) % 2 else 1
    numerator = sign * factorial * c_plus * pow(beta, 1 - j, p) % p
    return {
        "j": j,
        "K_j": (p + 1 - j) * (p - 1) + p + 1,
        "c_plus_mod_p": c_plus,
        "numerator_mod_p": numerator,
        "G_K_j_mod_p": G,
        "xi_mod_p": numerator * pow(G, -1, p) % p if G else None,
        "status": "defined" if G else "zero_denominator",
        "claim": "unproved comparison probe",
    }


def one_prime(p, exact_x, nmod_poly):
    r, a, n, specs = index_contract(p)
    cutoff = max(spec[0] // 6 for spec in specs.values())
    f, C, A, metadata = digit_inputs(p, cutoff)
    alt_f, alt_C, alt_resonances = stripped_inputs(p, cutoff)
    require(f == alt_f and C == alt_C, f"p={p}: independent input constructions differ")
    require(metadata["resonance_count"] == alt_resonances, "resonance count mismatch")
    require(all(((6 * j + 1) * f[j] - C[j]) % p == 0 for j in range(cutoff + 1)),
            "original logarithm differential identity failed")
    fpoly, Cpoly, Apoly = nmod_poly(f, p), nmod_poly(C, p), nmod_poly(A, p)
    alt_fpoly, alt_Cpoly = nmod_poly(alt_f, p), nmod_poly(alt_C, p)
    values, cache = {}, {}
    for label, (index, u, v) in specs.items():
        if index not in cache:
            bounded = bounded_residue(p, index, u, v, fpoly, Cpoly, Apoly)
            direct = positive_residue(p, index, alt_fpoly, alt_Cpoly)
            lagrange = lagrange_check(p, index, alt_fpoly, bounded)
            check = bounded == direct and lagrange["check"]
            record = {
                "N": index, "M": index // 6,
                "bounded_u": u, "bounded_v": v,
                "G_mod_p": bounded, "G_over_N_mod_p": (
                    bounded * pow(index % p, -1, p) % p if index % p else None),
                "positive_exponent_value": direct,
                "positive_exponent": p * p + 1 - index,
                "lagrange": lagrange,
                "all_channels_agree": check,
                "is_unit": bounded != 0,
            }
            if p in EXACT_PRIMES:
                rational = exact_x[index // 6] / (index - 1)
                exact_residue = rational_mod(rational, p)
                record["exact_rational_mod_p"] = exact_residue
                record["exact_rational_valuation"] = rational_valuation(rational, p)
                record["exact_rational_sha256"] = digest(rational_pair(rational))
                record["exact_rational_agrees"] = exact_residue == bounded
                record["all_channels_agree"] = check and exact_residue == bounded
            cache[index] = record
        values[label] = cache[index]

    old = OLD_R973[p]
    sign_B = -1 if ((p + 1) // 6) % 2 else 1
    beta = sign_B * old["B_minus"] % p
    Bp = 12 * beta % p
    require(beta != 0, "consumed original B scale is zero")
    B_check = None
    if p in EXACT_PRIMES:
        B_check = rational_mod(exact_x[(p + 1) // 6], p) == beta
    reflections = {}
    for label, t in (("low", a), ("high", n)):
        expected = Bp * values[label]["G_mod_p"] * pow(12 * t % p, -1, p) % p
        observed = values[f"{label}_star"]["G_mod_p"]
        reflections[label] = {"t": t, "expected": expected, "observed": observed,
                              "check": expected == observed}

    c_plus = -old["balanced_minus"] % p
    probes = [mixed_probe(p, n, c_plus, values["low_star"]["G_mod_p"], beta)]
    if p in EXACT_PRIMES:
        probes.extend([
            mixed_probe(p, 3, pow(6, -1, p), values["probe_j3"]["G_mod_p"], beta),
            mixed_probe(p, 6, -pow(900, -1, p) % p, values["probe_j6"]["G_mod_p"], beta),
        ])
    defined = [row["xi_mod_p"] for row in probes if row["xi_mod_p"] is not None]
    candidate_equal = (len(defined) == len(probes) and len(set(defined)) == 1
                       if len(probes) > 1 else None)
    denominator_free_probe = None
    if p in EXACT_PRIMES:
        lhs = 25 * pow(beta, 3, p) * values["probe_j6"]["G_mod_p"] % p
        rhs = 4 * values["probe_j3"]["G_mod_p"] % p
        denominator_free_probe = {
            "identity": "25 beta^3 G_K6 = 4 G_K3",
            "lhs_mod_p": lhs, "rhs_mod_p": rhs,
            "difference_mod_p": (lhs - rhs) % p,
            "holds": lhs == rhs, "is_asserted": False,
        }
    checks = {
        "independent_log_inputs": True,
        "differential_identity": True,
        "all_computed_channels": all(row["all_channels_agree"] for row in values.values()),
        "Robert_low_reflection": reflections["low"]["check"],
        "Robert_high_reflection": reflections["high"]["check"],
        "small_B_scale": B_check,
        "registered_low_coordinate_nonzero": values["low"]["G_mod_p"] != 0,
    }
    all_checks = all(value is not False for value in checks.values())
    return {
        "kind": "original_pure_hurwitz_prime",
        "p": p, "r": r, "a": a, "n": n,
        "source": "y^2=x^3+1; omega=dx/(2y); g2=0,g3=-4",
        "normalization": "log(sigma(z)/z)=-sum G_N z^N/N; no factorial in G_N",
        "max_series_degree": cutoff,
        "unique_indices_computed": sorted(cache),
        "values": values,
        "consumed_R973": old,
        "balanced_plus_mod_p": c_plus,
        "Robert_Bp_mod_p": Bp, "beta_Bp_over_12_mod_p": beta,
        "reflection_checks": reflections,
        "mixed_comparison_probes": probes,
        "mixed_probe_all_equal": candidate_equal,
        "mixed_probe_equality_is_asserted": False,
        "mixed_probe_denominator_free": denominator_free_probe,
        "input_metadata": metadata,
        "log_coefficients_sha256": digest(f),
        "differential_coefficients_sha256": digest(C),
        "checks": checks, "all_checks": all_checks,
        "high_zero": values["high"]["G_mod_p"] == 0,
    }


def worker(messages):
    try:
        import flint
        from flint import fmpq, nmod_poly
        require(flint.__version__ == "0.9.0", "unfrozen exact runtime")
        exact_maximum = max(
            index // 6
            for p in EXACT_PRIMES
            for index, _, _ in index_contract(p)[3].values()
        )
        exact_x = exact_wp_prefix(exact_maximum, fmpq)
        messages.put({
            "kind": "original_pure_hurwitz_exact_prefix",
            "calibration_primes": list(EXACT_PRIMES),
            "maximum_j": exact_maximum,
            "prefix_sha256": digest([rational_pair(x) for x in exact_x]),
            "source": "independent rational wp''=6wp^2 with x1=-1/7",
        })
        for p in PRIMES:
            record = one_prime(p, exact_x, nmod_poly)
            messages.put(record)
            require(record["all_checks"], f"p={p}: a proved source identity failed")
        messages.put({"kind": "worker_complete"})
    except BaseException as exc:
        messages.put({"kind": "worker_error", "error": str(exc),
                      "traceback": traceback.format_exc()})


def main():
    require(os.environ.get("GITHUB_ACTIONS") == "true",
            "mathematics requires public GitHub Actions")
    require(os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public",
            "wrong public repository")
    parser = argparse.ArgumentParser()
    parser.add_argument("--budget-seconds", type=float, default=MAX_BUDGET_SECONDS)
    args = parser.parse_args()
    require(0 < args.budget_seconds <= MAX_BUDGET_SECONDS, "invalid budget")
    started = time.monotonic()
    context = multiprocessing.get_context("spawn")
    messages = context.Queue()
    process = context.Process(target=worker, args=(messages,))
    process.start()
    rows, prefix, error = [], None, None
    completed = False
    while True:
        remaining = args.budget_seconds - (time.monotonic() - started)
        if remaining <= 0:
            error = "budget_exhausted; no claim about uncompleted primes"
            break
        try:
            record = messages.get(timeout=min(5.0, remaining))
        except queue.Empty:
            if not process.is_alive():
                error = "worker_ended_without_completion"
                break
            continue
        if record["kind"] == "worker_complete":
            completed = True
            break
        if record["kind"] == "worker_error":
            error = record
            print(json.dumps(record, sort_keys=True), flush=True)
            break
        if record["kind"] == "original_pure_hurwitz_prime":
            rows.append(record)
        elif record["kind"] == "original_pure_hurwitz_exact_prefix":
            prefix = record
        print(json.dumps(record, sort_keys=True), flush=True)
    if process.is_alive():
        if not completed:
            process.terminate()
        process.join(timeout=5.0)
    process.join(timeout=5.0)
    finished = [row["p"] for row in rows]
    complete = (completed and finished == list(PRIMES)
                and process.exitcode == 0 and all(row["all_checks"] for row in rows))
    method_file = Path(__file__).resolve().parents[3] / METHOD_PATH
    summary = {
        "kind": "original_pure_hurwitz_summary",
        "complete": complete,
        "requested_primes": list(PRIMES), "completed_primes": finished,
        "uncompleted_primes": [p for p in PRIMES if p not in finished],
        "exact_calibration_primes": list(EXACT_PRIMES),
        "rows_sha256": digest(rows), "prefix_sha256": digest(prefix),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "method_sha256": hashlib.sha256(method_file.read_bytes()).hexdigest(),
        "high_zero_primes": [row["p"] for row in rows if row["high_zero"]],
        "mixed_probe_failures": [row["p"] for row in rows
                                 if row["mixed_probe_all_equal"] is False],
        "error": error,
        "scope": "new pure Hurwitz indices only; no uniform unit or mixed coefficient theorem",
    }
    print(json.dumps(summary, sort_keys=True), flush=True)
    print(json.dumps({"kind": "timing", "elapsed_seconds": time.monotonic() - started},
                     sort_keys=True), flush=True)
    return 0 if complete else 1


if __name__ == "__main__":
    sys.exit(main())
