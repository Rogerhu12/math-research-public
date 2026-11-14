#!/usr/bin/env python3
"""R719 public Actions driver: exact p137147 orders, independent audit, Arb tail.

This script performs the mathematical run only on the public repository's
GitHub Actions. It retains all exact counts and audit rows, including on a
failed bound. No extrapolation from a previous prime or finite window is used.
"""
import argparse
import csv
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import subprocess
import sys
import time
import traceback

P = 137147
M = (P + 1) // 3
RADIUS_MULTIPLIER = 25
AUDIT_NORM_BOUND = 10000
BAD = (11, 22, 1039, 2078, 11429, 22858)
PHI = (10, 10, 1038, 1038, 10380, 10380)
ALL_DIVISORS = tuple(sorted({2**a * 11**b * 1039**c
                            for a in range(3)
                            for b in range(2) for c in range(2)}))


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def write_json(path, obj):
    p = Path(path)
    tmp = p.with_name(p.name + ".tmp")
    tmp.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n",
                   encoding="utf-8")
    tmp.replace(p)


def deterministic_gzip(src):
    src = Path(src)
    dst = src.with_name(src.name + ".gz")
    with src.open("rb") as a, dst.open("wb") as b:
        with gzip.GzipFile(fileobj=b, mode="wb", filename="", mtime=0) as z:
            for block in iter(lambda: a.read(1 << 20), b""):
                z.write(block)
    return dst


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


def mul(x, y):
    # Independent direct arithmetic in F_p[z]/(z^2+z+1).
    a, b = x
    c, d = y
    return ((a*c-b*d) % P, (a*d+b*c-b*d) % P)


def power(x, e):
    r = (1, 0)
    while e:
        if e & 1:
            r = mul(r, x)
        x = mul(x, x)
        e //= 2
    return r


def independent_small_points(cutoff):
    # Different enumeration: all integer coordinates, then primary filtering.
    box = math.isqrt((4 * cutoff) // 3)
    ans = {}
    for a in range(-box, box + 1):
        for b in range(-box, box + 1):
            n = a*a-a*b+b*b
            if not 0 < n <= cutoff:
                continue
            if a % 3 != 1 or b % 3 != 0:
                continue
            if math.gcd(a, b) != 1 or math.gcd(n, 6*P) != 1:
                continue
            u = power((a % P, b % P), 3*(P-1))
            # Ascending divisors, independently of the C++ prime-factor stripping.
            order = next((d for d in ALL_DIVISORS
                          if power(u, d) == (1, 0)), None)
            if order is None:
                raise AssertionError("independent order does not divide M")
            ans[(a, b)] = (n, u[0], u[1], order)
    return ans


def audit_small(path, meta):
    actual = {}
    with Path(path).open(newline="") as f:
        rd = csv.DictReader(f)
        assert rd.fieldnames == ["a", "b", "n", "u0", "u1", "order"]
        for row in rd:
            a, b, n, u0, u1, order = (int(row[k]) for k in rd.fieldnames)
            assert (a, b) not in actual
            actual[(a, b)] = (n, u0, u1, order)
    expected = independent_small_points(AUDIT_NORM_BOUND)
    assert actual == expected, "all-point small-radius direct audit failed"
    assert len(actual) == meta["small_radius_count"]
    assert len(actual) == meta["direct_power_checks"]
    return {
        "norm_bound": AUDIT_NORM_BOUND,
        "all_small_radius_points_and_orders_equal": True,
        "independent_direct_exponent": 3*(P-1),
        "independent_order_method": "first successful divisor in increasing order",
        "point_count": len(actual),
        "csv_sha256": sha(path),
    }


def histogram_rows(path, meta):
    old = 0
    totals = [0]*6
    count = 0
    with Path(path).open(newline="") as f:
        rd = csv.reader(f)
        assert next(rd) == ["n"] + ["order_" + str(o) for o in BAD]
        for row in rd:
            assert len(row) == 7
            n, *c = map(int, row)
            assert old < n <= RADIUS_MULTIPLIER*P
            assert all(x >= 0 for x in c) and any(c)
            assert math.gcd(n, 6*P) == 1
            old = n
            count += 1
            for j in range(6):
                totals[j] += c[j]
            yield n, c
    assert count == meta["nonzero_norm_rows"]
    assert totals == meta["bad_order_totals"]
    assert sum(meta["all_exact_order_totals"].values()) == meta["admissible_count"]
    assert set(map(int, meta["all_exact_order_totals"])).issubset(ALL_DIVISORS)


def rational_upper(x, arb, den):
    # Only certified Arb comparisons control the integer bisection.
    lo, hi = 0, 1
    while not x < arb(hi)/den:
        hi *= 2
        if hi.bit_length() > 500:
            raise AssertionError("nonfinite or unexpectedly large upper bound")
    while hi-lo > 1:
        mid = (lo+hi)//2
        if x < arb(mid)/den:
            hi = mid
        else:
            lo = mid
    assert x < arb(hi)/den
    return {"numerator": hi, "denominator": den,
            "strict_arb_upper_comparison_verified": True}


def ball_record(x):
    return x.str(80)


def run(args):
    if os.environ.get("GITHUB_ACTIONS") != "true":
        raise RuntimeError("Formal R719 arithmetic is restricted to public GitHub Actions")
    if os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("R719 must use Rogerhu12/math-research-public Actions")
    from flint import arb, ctx
    import flint
    ctx.prec = args.precision
    out = Path(args.output).resolve()
    out.mkdir(parents=True, exist_ok=True)
    cpp = Path(args.cpp_source).resolve()
    repo = Path(args.repo_root).resolve()
    assert is_prime(P) and P % 9 == 5
    assert M == 4*11*1039 and all(is_prime(x) for x in (11, 1039))
    assert args.precision >= 192
    expected_bad = tuple(d for d in ALL_DIVISORS
                         if d > 2 and all(d % (r*r) for r in (2, 11, 1039)))
    assert expected_bad == BAD

    binding_paths = [
        cpp, Path(__file__).resolve(), repo/"README.md",
        repo/"topics/serre-uniformity/README.md",
        repo/"topics/serre-uniformity/results/R714-global-visible-count-and-sublogarithmic-divisor-primitive-region.md",
        repo/"topics/serre-uniformity/results/R616-original-CM-point-difference-and-explicit-height-basis.md",
    ]
    if args.proof_path:
        binding_paths.append(Path(args.proof_path).resolve())
    bindings = {str(p.relative_to(repo)) if p.is_relative_to(repo) else p.name: sha(p)
                for p in binding_paths}
    input_receipt = {
        "schema": "r719.public-input.v1",
        "repository": os.environ["GITHUB_REPOSITORY"],
        "source_commit": os.environ.get("GITHUB_SHA"),
        "run_id": os.environ.get("GITHUB_RUN_ID"),
        "run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"),
        "parameters": {"p": P, "M": M, "radius_multiplier": RADIUS_MULTIPLIER,
                       "norm_cutoff": RADIUS_MULTIPLIER*P,
                       "audit_norm_cutoff": AUDIT_NORM_BOUND,
                       "arb_precision_bits": args.precision,
                       "rational_upper_denominator": args.denominator},
        "source_and_readme_sha256": bindings,
        "python_version": sys.version,
        "python_flint_version": flint.__version__,
        "platform": platform.platform(),
        "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    write_json(out/"public-actions-input.json", input_receipt)

    binary = out/"r719_visible_order_enumerator"
    compile_cmd = ["g++", "-std=c++17", "-O3", "-Wall", "-Wextra",
                   "-pedantic", str(cpp), "-o", str(binary)]
    with (out/"compile.log").open("w") as log:
        cp = subprocess.run(compile_cmd, stdout=log, stderr=subprocess.STDOUT,
                            timeout=600)
    if cp.returncode:
        raise RuntimeError("C++ compile failed; see complete compile.log")
    with (out/"enumeration.log").open("w") as log:
        cp = subprocess.run([str(binary), str(out)], stdout=log,
                            stderr=subprocess.STDOUT, timeout=1800)
    if cp.returncode:
        raise RuntimeError("exact enumeration failed; see complete enumeration.log")
    meta = json.loads((out/"enumeration_metadata.json").read_text())
    assert meta["p"] == P and meta["M"] == M
    assert meta["norm_cutoff"] == RADIUS_MULTIPLIER*P
    assert meta["independent_audit_norm_cutoff"] == AUDIT_NORM_BOUND
    assert meta["bad_orders"] == list(BAD) and meta["bad_order_phi"] == list(PHI)
    assert meta["all_u_orders_divide_M_and_are_exact"]
    assert meta["all_inverse_entries_verified"]
    audit = audit_small(out/"small_radius_points.csv", meta)
    write_json(out/"independent-small-radius-audit.json", audit)

    c = arb.pi()/(3*arb(3).sqrt())
    t = c/P
    S = arb(3)/2*(1+arb(1)/P)
    cutoff = RADIUS_MULTIPLIER*P
    T = arb(cutoff).sqrt()
    xR = t*cutoff
    assert c > arb(3)/5
    assert arb(P).log() > 3
    finite = arb(0)
    finite_by_order = [arb(0) for _ in BAD]
    for n, counts in histogram_rows(out/"norm_order_counts.csv", meta):
        kernel = (-t*n).exp()/arb(n).sqrt()
        for j, amount in enumerate(counts):
            if amount:
                piece = arb(amount)/PHI[j]*kernel
                finite_by_order[j] += piece
                finite += piece

    # Complete primary-lattice tail: spacing 3, weight <= 1/10.
    tail = ((-xR).exp()/10 *
            (1/T + arb(4)/3*(1+1/(2*xR)) +
             arb(4)/9*(T+1/(t*T))))
    B = 2*S*(finite+tail)
    plus_error = (arb(P).log()+2)*B
    full_minus = arb(5393)/6150
    full_plus = arb(9)/5*(arb(P).log()-1)-arb(1)/250
    minus_lower = full_minus-B
    plus_lower = full_plus-plus_error
    target_minus = arb(1159)/3075
    target_plus_formula = arb(13)/10*arb(P).log()-arb(701)/250
    target_plus_absolute = arb(137)/125
    bound = rational_upper(B, arb, args.denominator)
    success = (2*bound["numerator"] < bound["denominator"])
    if success:
        assert B < arb(1)/2
        assert minus_lower > target_minus
        assert plus_lower > target_plus_formula
        assert target_plus_formula > target_plus_absolute

    histogram_gz = deterministic_gzip(out/"norm_order_counts.csv")
    small_gz = deterministic_gzip(out/"small_radius_points.csv")
    result = {
        "schema": "r719.original-R616-primitive-certificate.v1",
        "status": "proved" if success else "bound_not_closed",
        "formal_public_actions_run": True,
        "p": P, "M": M, "M_factorization": meta["M_factorization"],
        "bad_orders": list(BAD), "bad_order_phi": list(PHI),
        "original_cubic_phase_retained": True,
        "original_positive_quotient_and_negative_second_factor_retained": True,
        "visible_primary_definition":
            "a=1 mod3, b=0 mod3, gcd(a,b)=1, gcd(a^2-ab+b^2,6p)=1",
        "actual_order_definition": "ord((a+b*zeta)^(3*(p-1)))",
        "zeta_relation": "zeta^2+zeta+1=0",
        "finite_norm_cutoff": cutoff,
        "all_omitted_histogram_norms_have_zero_six_order_counts": True,
        "finite_sum_ball": ball_record(finite),
        "finite_sum_by_order_balls": [ball_record(x) for x in finite_by_order],
        "tail_ball": ball_record(tail),
        "tail_includes_all_primary_points_above_cutoff": True,
        "tail_packing_count": "(1+2*T/3)^2",
        "tail_max_inverse_phi": "1/10",
        "c_ball": ball_record(c),
        "c_definition": "pi/(3*sqrt(3))",
        "t_ball": ball_record(t),
        "S_ball": ball_record(S),
        "S_definition": "3/2*(1+1/p)",
        "T_ball": ball_record(T),
        "x_R_ball": ball_record(xR),
        "common_exponential_error_B_ball": ball_record(B),
        "common_error_B_strict_rational_upper": bound,
        "B_less_than_one_half": success,
        "plus_error_bound_ball": ball_record(plus_error),
        "primitive_minus_lower_ball": ball_record(minus_lower),
        "primitive_plus_lower_ball": ball_record(plus_lower),
        "minus_lower_target": "1159/3075",
        "plus_lower_target": "(13/10)*log(p)-701/250",
        "plus_lower_absolute_target": "137/125",
        "original_R616_nonvanishing_rank_log_premise_certified": success,
        "not_a_rational_point_or_uniformity_exclusion": True,
        "arb_precision_bits": args.precision,
        "audit": audit,
        "enumeration": meta,
        "input_receipt_sha256": sha(out/"public-actions-input.json"),
        "histogram_csv_sha256": sha(out/"norm_order_counts.csv"),
        "histogram_gzip_sha256": sha(histogram_gz),
        "small_radius_csv_sha256": sha(out/"small_radius_points.csv"),
        "small_radius_gzip_sha256": sha(small_gz),
        "source_and_readme_sha256": bindings,
    }
    write_json(out/"r719_p137147_primitive_certificate.json", result)
    receipt = {
        "schema": "r719.public-receipt.v1",
        "repository": os.environ["GITHUB_REPOSITORY"],
        "source_commit": os.environ.get("GITHUB_SHA"),
        "run_id": os.environ.get("GITHUB_RUN_ID"),
        "run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"),
        "finished_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source_sha256": {"cpp": sha(cpp), "python": sha(__file__)},
        "source_and_readme_sha256": bindings,
        "complete": True,
        "mathematical_bound_closed": success,
        "outputs_sha256": {
            p.name: sha(p) for p in sorted(out.iterdir())
            if p.is_file() and p.name not in {"r719_visible_order_enumerator",
                                             "run-receipt.json", "failure.json"}
        },
    }
    write_json(out/"run-receipt.json", receipt)
    print(json.dumps({"p": P, "status": result["status"],
                      "B_strict_upper": bound,
                      "admissible_points": meta["admissible_count"],
                      "nonzero_norm_rows": meta["nonzero_norm_rows"],
                      "certificate_sha256":
                          sha(out/"r719_p137147_primitive_certificate.json")},
                     sort_keys=True), flush=True)
    return 0 if success else 2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--cpp-source", required=True)
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--proof-path")
    ap.add_argument("--precision", type=int, default=256)
    ap.add_argument("--denominator", type=int, default=10**12)
    args = ap.parse_args()
    out = Path(args.output).resolve()
    out.mkdir(parents=True, exist_ok=True)
    try:
        return run(args)
    except Exception as exc:
        error = {"schema": "r719.failure.v1", "complete": False,
                 "exception_type": type(exc).__name__, "message": str(exc),
                 "traceback": traceback.format_exc(),
                 "run_id": os.environ.get("GITHUB_RUN_ID"),
                 "source_commit": os.environ.get("GITHUB_SHA")}
        write_json(out/"failure.json", error)
        print(error["traceback"], file=sys.stderr, flush=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
