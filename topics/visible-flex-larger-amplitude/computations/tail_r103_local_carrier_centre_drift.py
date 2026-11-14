#!/usr/bin/env python3
"""Consume R103's radial-to-centred gauge drift from complete local primaries.

This is a prepared exact Fraction consumer. It loads no physical engine, Node,
Arb, ODE or source integrator. All binary primaries are read only by this local
filesystem process, never through connector tools. No exact outer solution,
candidate immersion, reach or full eight-part drift is asserted.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
import os
from pathlib import Path
import resource
import time

EXPECTED = {
    "carrier_summary": "0ac4b1e14ec34a86035add63e6250660924537c54acc834e497c6ebdd396ae12",
    "carrier_resource": "dee1cef1a748f4459e00a5428dd4b6b1602c3eb442498091b29bd88e0ea1c865",
    "carrier_primary": "d07456782cfd2cd292cbb77fbbf437617a82ab6039f774fc5637c74a2e486dbe",
    "mean_summary": "a178bc76d676eaa3aa6e0e1f57592dceea27bc996017503097a1fd01f8bde1f2",
    "mean_resource": "263ea6873d694bc3ffaa8540c08bea21bfc6f38defd4a7c52e5dd63a4e0e82ff",
    "mean_primary": "6b6748eab26c02b1960b367acc22f3a80760d6d40c20aa998ddaa3c4193d0e71",
}


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()


def integer(x):
    if isinstance(x, bool) or isinstance(x, float):
        raise TypeError("Only an exact integer encoding is accepted")
    if not isinstance(x, (int, str)):
        raise TypeError("Unknown integer encoding")
    return int(x)


def dyadic(value):
    if isinstance(value, dict):
        n, e = integer(value["mantissa"]), integer(value["binary_exponent"])
    elif isinstance(value, list) and len(value) == 2:
        n, e = map(integer, value)
    else:
        raise TypeError("Unknown frozen dyadic representation")
    return Q(n)*(Q(2)**e)


def interval(value):
    if isinstance(value, dict):
        lo, hi = dyadic(value["lower"]), dyadic(value["upper"])
    elif isinstance(value, list) and len(value) == 2:
        lo, hi = map(dyadic, value)
    else:
        raise TypeError("Unknown frozen interval representation")
    if lo > hi:
        raise ValueError("Reversed interval")
    return lo, hi


def ratio(value):
    if not isinstance(value, dict):
        raise TypeError("Expected original qr record")
    q = Q(integer(value["numerator"]), integer(value["denominator"]))
    return q


def abs_interval(value):
    return max(map(abs, interval(value)))


def positive_upper(value, bits=128):
    """Round nonnegative Q upward at significant binary bits, no exponent cutoff."""
    if value < 0:
        raise ValueError("Negative positive-budget input")
    if value == 0:
        return Q(0)
    n, d = value.numerator, value.denominator
    e = n.bit_length()-d.bit_length()
    below = (n < d*(1 << e)) if e >= 0 else (n*(1 << -e) < d)
    if below:
        e -= 1
    unit = Q(2)**(e-bits+1)
    q = value/unit
    k = (q.numerator+q.denominator-1)//q.denominator
    out = k*unit
    if not (value <= out <= (1+Q(2)**(1-bits))*value):
        raise ArithmeticError("Directed significant rounding invariant")
    return out


def record_upper(value, bits=96):
    q = positive_upper(value, bits)
    if not q:
        return ["0", 0]
    n, d = q.numerator, q.denominator
    if d & (d-1):
        raise ArithmeticError("Directed output is not dyadic")
    e = -(d.bit_length()-1)
    while not n & 1:
        n //= 2
        e += 1
    return [str(n), e]


def record_lower(value, bits=96):
    if value <= 0:
        raise ValueError("Expected positive lower domain margin")
    n = value.numerator*(1 << bits)//value.denominator
    return [str(n), -bits]


def load_json(path):
    with Path(path).open(encoding="utf-8") as stream:
        return json.load(stream)


def assert_gates(value):
    gates = value.get("gates")
    if not gates or not all(x is True for x in gates.values()):
        raise ValueError("A prerequisite complete gate is not true")


def check_formal(value, summary_path):
    if value["exitcode"] != 0 or value["termination_signal"] is not None:
        raise ValueError("A prerequisite formal resource did not succeed")
    command = value["command"]
    original = Path(command[command.index("--out-prefix")+1]+"-summary.json")
    if original.name != Path(summary_path).name:
        raise ValueError("The original formal command identifies another stage")
    return str(original)


def primary_rows(path, kind, header_check):
    header = trailer = False
    count, at = 0, Q(0)
    with gzip.open(path, "rt", encoding="utf-8") as stream:
        for line in stream:
            row = json.loads(line)
            if row["kind"] == "header":
                if header or trailer or count:
                    raise ValueError("Repeated or misplaced primary header")
                header_check(row)
                header = True
                continue
            if row["kind"] == "trailer":
                if not header or trailer or not row["complete"] or row["panels"] != count:
                    raise ValueError("Incomplete original primary trailer")
                if row.get("part", 0) != 0:
                    raise ValueError("Unexpected primary part")
                trailer = True
                continue
            left, right = Q(row["source_left"]), Q(row["source_right"])
            if (not header or trailer or row["kind"] != kind or row["part"] != 0
                    or row["panel"] != count or left != at or not left < right <= Q(1, 8)):
                raise ValueError("The complete common111 partition changed")
            yield row
            at, count = right, count+1
    if not (header and trailer and count == 111 and at == Q(1, 8)):
        raise ValueError("The original111 leaves are not completely covered")


def atomic_json(path, value):
    path = Path(path)
    if path.exists():
        raise FileExistsError("Never replace a prior result")
    tmp = path.with_name(path.name+".tmp-"+str(os.getpid()))
    with tmp.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, separators=(",", ":"), allow_nan=False)
        stream.write("\n")
    if tmp.stat().st_size >= 5_000_000:
        raise ValueError("The complete owned output exceeds the file limit")
    if path.exists():
        raise FileExistsError("A result appeared while writing")
    os.replace(tmp, path)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for key in EXPECTED:
        ap.add_argument("--"+key.replace("_", "-"), type=Path, required=True)
    ap.add_argument("--out-prefix", type=Path, required=True)
    ap.add_argument("--rss-limit-mib", type=int, default=96)
    args = ap.parse_args()
    started = time.monotonic()
    out = Path(str(args.out_prefix)+"-summary.json")
    leaf_out = Path(str(args.out_prefix)+"-leaves.json")
    if out.exists() or leaf_out.exists():
        raise FileExistsError("Use a fresh out-prefix")
    files = {}
    for name, expected in EXPECTED.items():
        path = getattr(args, name)
        actual = digest(path)
        if actual != expected:
            raise ValueError("An original formal input changed: "+name)
        files[name] = dict(path=str(path), sha256=actual, bytes=path.stat().st_size)
    carrier, mean = map(load_json, (args.carrier_summary, args.mean_summary))
    cusage, musage = map(load_json, (args.carrier_resource, args.mean_resource))
    original_cs = check_formal(cusage, args.carrier_summary)
    original_ms = check_formal(musage, args.mean_summary)
    assert_gates(carrier)
    assert_gates(mean)
    if (carrier["mode"] != "carrier" or carrier["panels"] != 111
            or carrier["cell"] != 0 or carrier["segment"] != 7
            or carrier["modes"] != list(range(2, 41, 2))
            or [x["part"] for x in carrier["parts"]] != [0]):
        raise ValueError("The original complete carrier identity changed")
    if (mean["continuous_panels"] != 111 or mean["cell"] != 0 or mean["segment"] != 7
            or mean["modes"] != carrier["modes"] or mean["requested_complete_parts"] != [0]
            or [x["part"] for x in mean["parts"]] != [0]):
        raise ValueError("The original complete mean identity changed")
    for summary, key in ((carrier, "carrier_primary"), (mean, "mean_primary")):
        part = summary["parts"][0]
        if part["panels"] != 111 or part["sha256"] != EXPECTED[key]:
            raise ValueError("A primary is not the one bound to its summary")
    # The two frozen summaries are immutable provenance. Their sources are not
    # re-executed or relabelled; current explicit paths may only relocate bytes.
    relocations = dict(
        carrier_summary=dict(original=original_cs, current=str(args.carrier_summary)),
        mean_summary=dict(original=original_ms, current=str(args.mean_summary)),
        carrier_primary=dict(original=carrier["parts"][0]["path"], current=str(args.carrier_primary)),
        mean_primary=dict(original=mean["parts"][0]["path"], current=str(args.mean_primary)))

    def chead(h):
        if (h["mode"] != "carrier" or h["input_hashes"] != carrier["input_hashes"]
                or h["source_hashes"] != carrier["source_hashes"]
                or h["complete_J_cosine_modes"] != list(range(0, 81, 2))):
            raise ValueError("The complete carrier header changed")

    def mhead(h):
        if h["part"] != 0 or h["metric_and_candidate_origin_hashes"] != mean["input_hashes"]:
            raise ValueError("The full-mean origin header changed")

    cs = primary_rows(args.carrier_primary,
        "complete_new_physical_substage_R64_J_R77_leaf", chead)
    ms = primary_rows(args.mean_primary, "complete_exact_mean_difference_leaf", mhead)
    cumulative = Q(0)
    rows, maximum_increment = [], Q(0)
    minimum_D = Q(1)
    pi2_over_16 = Q(22, 7)**2/16
    while True:
        c, m = next(cs, None), next(ms, None)
        if c is None and m is None:
            break
        if c is None or m is None:
            raise ValueError("A complete primary ended before its counterpart")
        keys = ("part", "panel", "source_left", "source_right")
        if (c["part"] != m["part"] or c["panel"] != m["panel"]
                or any(Q(c[k]) != Q(m[k]) for k in ("source_left", "source_right"))):
            raise ValueError("Different actual leaves cannot be paired")
        if (not c["complete_mean"]
                or not m["actual_physical_mass_from_two_positive_moments"]
                or not m["physical_mass_intersection_only_same_integral"]
                or len(c["full_J_cosine_intervals"]) != 41
                or any(dyadic(x) <= 0 for x in c["gates_lower"].values())):
            raise ValueError("A full-mean, finite-spectrum or real-domain gate is absent")
        rlo, rhi = interval(c["source"]["radius"])
        wlo, whi = interval(c["source"]["w"])
        rxlo, rxhi = interval(c["source"]["radius_x"])
        if not (rlo > Q(1, 20) and rhi < Q(1, 3)
                and 0 < wlo <= whi <= Q(3, 25)
                and rxlo == rxhi == 1):
            raise ValueError("The actual physical-r same-metric carrier changed")
        D = min(Q(1), dyadic(c["gates_lower"]["real_D_lower"]))
        if D <= 0:
            raise ValueError("The true real D denominator is not positive")
        omega_lo, omega = ratio(m["omega_lower"]), ratio(m["omega_upper"])
        if not 0 < omega_lo <= omega:
            raise ValueError("The original true integral w dr has no positive enclosure")
        b = {k:dyadic(x) for k,x in c["bounds_upper"].items()}
        if any(x < 0 for x in b.values()):
            raise ValueError("A complete norm bound became negative")
        J = list(map(abs_interval, c["full_J_cosine_intervals"]))
        Jperp = sum(J[1:], Q(0))
        E = 1+whi**2
        R77 = Q(3, 2)*E**2*b["full_D_nonconstant_W1"]/D**3
        Jmean = min(J[0], R77*Jperp)
        Jfull = min(sum(J, Q(0)), b["complete_J_l1"], Jmean+Jperp)
        increment = pi2_over_16*rhi*whi*Jfull*omega/(rxlo*D**2)
        before = cumulative
        cumulative = positive_upper(cumulative+increment, 128)
        maximum_increment = max(maximum_increment, increment)
        minimum_D = min(minimum_D, D)
        rows.append(dict(
            **{k:c[k] for k in keys},
            complete_J_upper=record_upper(Jfull),
            scalar_J0_upper_after_same_candidate_R77=record_upper(Jmean),
            original_scalar_J0_upper=record_upper(J[0]),
            true_w_dr_lower=record_lower(omega_lo),
            true_w_dr_upper=record_upper(omega),
            real_D_lower=record_lower(D),
            centre_increment_upper=record_upper(increment),
            centre_prefix_before_upper=record_upper(before),
            centre_prefix_through_leaf_upper=record_upper(cumulative)))
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > args.rss_limit_mib*1024:
            raise MemoryError("Owned Fraction consumer exceeded observed RSS")
    if len(rows) != 111:
        raise ValueError("The complete111 cover is missing")
    primary = dict(
        schema="R103-complete-same-carrier-centre-drift-leaves-v1",
        part=0, cell=0, segment=7, continuous_leaves=111,
        input_hashes={k:v["sha256"] for k,v in files.items()},
        initial_centre_difference="0, chosen once",
        derivative_coordinate="physical r",
        rows=rows, all_complete=True)
    atomic_json(leaf_out, primary)
    result = dict(
        schema="R103-complete-same-carrier-centre-drift-v1",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", date_utc="2026-11-13",
        status="Actual candidate radial-reference to centred-reference drift on part0 only",
        files=files, original_paths_and_explicit_byte_preserving_relocations=relocations,
        source_sha256=digest(__file__), cell=0, segment=7, part=0, continuous_leaves=111,
        original_carrier_source_hashes=carrier["source_hashes"],
        original_mean_schema=mean["schema"], full_mean_origin_preserved=True,
        actual_centre_drift_upper=record_upper(cumulative),
        maximum_single_leaf_increment_upper=record_upper(maximum_increment),
        minimum_D_lower=record_lower(minimum_D),
        formula="(pi^2/16) integral r*w^2*|Jx|/(rx*D^(3/2)) dr",
        consumed_same_leaf_bound="(22/7)^2/16*r_hi*w_hi*J_full/(rx_lo*min(1,D_lo)^2)*(I00+I01)",
        complete_J_modes=list(range(0, 81, 2)),
        cumulative_rounding="Upward128 significant binary bits, no exponent cutoff; each rounding factor <=1+2^-127",
        primary=dict(path=str(leaf_out), sha256=digest(leaf_out), bytes=leaf_out.stat().st_size),
        downstream="Carry this centre bound through later parts; no per-part recentering. Other7 drift costs remain separate.",
        conditional_hypotheses=["Exact complete mean root and two common reflection axes, as in R103",
            "Original radial reference uses the same angular frame and one initial-centre gauge"],
        actual_candidate_normal_or_isometric_immersion_claimed=False,
        same_candidate_only=True, true_outer_error_or_reach_claimed=False,
        new_Arb_Node_ODE_source_integrals=0,
        gates=dict(
            six_complete_frozen_input_SHA_checked=True,
            both_original_formal_resources_exit0=True,
            complete111_common_true_partition=True,
            complete_mean_root_retained=True,
            all41_J_modes_and_same_candidate_R77=True,
            true_same_leaf_integral_w_dr=True,
            actual_physical_r_no_missing_rx=True,
            strictly_positive_real_D=True,
            one_initial_centre_no_substage_reset=True,
            all_output_roundings_outward=True),
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    atomic_json(out, result)
    print(json.dumps(dict(event="complete_actual_R103_carrier_centre_drift",
        summary=str(out), leaves=111, centre_drift_upper=result["actual_centre_drift_upper"],
        gates=result["gates"], peak_RSS_KiB=result["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
