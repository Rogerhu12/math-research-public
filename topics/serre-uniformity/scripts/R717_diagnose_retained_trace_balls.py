#!/usr/bin/env python3
"""Diagnose retained R717 balls and chirps; never enumerate lattice terms or run a DFT."""
from __future__ import annotations

import argparse
import ast
from functools import cmp_to_key
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import time
import traceback

import flint
from flint import acb, arb, ctx

from p41_public_actions_recovery import REPO, TOPIC, publish

REQUEST = TOPIC / "notes/R717-trace-diagnostic-request.json"
SCRIPT = TOPIC / "scripts/R717_diagnose_retained_trace_balls.py"
WORKFLOW = REPO / ".github/workflows/serre-R717-trace-diagnostics.yml"
SESSION = Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "R717-trace-diagnostic-session.json"


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def write_json(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".next")
    tmp.write_text(json.dumps(obj, indent=2) + "\n")
    tmp.replace(path)


def archive_bytes(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as raw:
        with gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0) as stream:
            stream.write(data)


def read_gzip(path):
    with gzip.open(path, "rt") as stream:
        return json.load(stream)


def load_arb(v):
    assert len(v) == 4
    return arb((int(v[0]), int(v[1])), (int(v[2]), int(v[3])))


def serial_arb(x):
    m, e = x.mid().man_exp()
    r, f = x.rad().man_exp()
    return [str(m), int(e), str(r), int(f)]


def serial_acb(x):
    return [serial_arb(x.real), serial_arb(x.imag)]


def dyadic(value):
    m, e = int(value[0]), int(value[1])
    if m == 0:
        return (0, 0)
    shift = (abs(m) & -abs(m)).bit_length() - 1
    return (m >> shift, e + shift)


def dy_compare(a, b):
    """Exact comparison of nonnegative dyadics, without huge exponent shifts."""
    a, b = dyadic(a), dyadic(b)
    am, ae = a
    bm, be = b
    assert am >= 0 and bm >= 0
    if am == 0 or bm == 0:
        return (am > bm) - (am < bm)
    at = am.bit_length() + ae
    bt = bm.bit_length() + be
    if at != bt:
        return (at > bt) - (at < bt)
    common = min(ae, be)
    aa, bb = am << (ae-common), bm << (be-common)
    return (aa > bb) - (aa < bb)


def dy_record(a):
    m, e = dyadic(a)
    return {"mantissa": str(m), "exponent": e,
            "approx_log2_abs": math.log2(abs(m))+e if m else None}


def stats(values):
    values = [dyadic(v) for v in values]
    assert all(v[0] >= 0 for v in values)
    if not values:
        return {"count": 0}
    values.sort(key=cmp_to_key(dy_compare))
    n = len(values)
    return {"count": n, "zeros": sum(m == 0 for m, _ in values),
            "minimum": dy_record(values[0]), "maximum": dy_record(values[-1]),
            "median_lower": dy_record(values[(n-1)//2]),
            "median_upper": dy_record(values[n//2])}


def radius(v):
    return dyadic((int(v[2]), int(v[3])))


def abs_mid(v):
    return dyadic((abs(int(v[0])), int(v[1])))


def midpoint_distance(v):
    """Exact distance from the dyadic midpoint to the nearest integer."""
    m, e = int(v[0]), int(v[1])
    if m == 0 or e >= 0:
        return (0, 0)
    m = abs(m)
    shift = -e
    if shift > m.bit_length():
        return dyadic((m, e))
    modulus = 1 << shift
    rem = m % modulus
    return dyadic((min(rem, modulus-rem), e))


def real_ball_stats(values):
    result = {"radius": stats(radius(v) for v in values),
              "absolute_midpoint": stats(abs_mid(v) for v in values),
              "midpoint_distance_to_nearest_integer":
                  stats(midpoint_distance(v) for v in values)}
    result["contains_zero_count_exact_dyadic"] = sum(
        dy_compare(abs_mid(v), radius(v)) <= 0 for v in values)
    return result


def checked_cfg(cfg, request, expected=None):
    c = dict(cfg)
    parameter = c.pop("parameter_sha256")
    assert hashlib.sha256(canonical(c)).hexdigest() == parameter
    assert cfg["prime"] == request["prime"] == 137147
    assert cfg["n"] == 137148 and cfg["prec_bits"] == 384
    assert cfg["tail_bits"] == 256 and cfg["cutoff_multiple"] == 360
    assert cfg["shard_count"] == 4 and cfg["a_max"] == 8113
    assert cfg["source_sha256"] == request["original_core_sha256"]
    if expected is not None:
        assert cfg == expected
    return cfg


def diagnose_traces(record, request):
    cfg = checked_cfg(record["configuration"], request)
    ctx.prec = cfg["prec_bits"]
    balls = record["all_trace_balls"]
    assert len(balls) == cfg["n"]
    counts = {"complex_unique_integer_missing": 0,
              "real_unique_integer_missing": 0,
              "imaginary_interval_excludes_zero": 0,
              "real_radius_not_strictly_below_quarter": 0,
              "real_interval_excludes_nearest_midpoint_integer": 0,
              "imaginary_midpoint_nonzero": 0,
              "any_original_gate_failed": 0}
    recomputed = []
    samples = []
    real_radii, imag_radii, distances, imag_centers = [], [], [], []
    for j, item in enumerate(balls):
        rv, iv = item
        rb, ib = load_arb(rv), load_arb(iv)
        z = acb(rb, ib)
        integer = z.unique_fmpz()
        real_integer = rb.unique_fmpz()
        imaginary_ok = bool(ib.contains(0))
        radius_ok = dy_compare(radius(rv), (1, -2)) < 0
        distance = midpoint_distance(rv)
        nearest_inside = dy_compare(distance, radius(rv)) <= 0
        failed = integer is None or not imaginary_ok or not radius_ok
        counts["complex_unique_integer_missing"] += integer is None
        counts["real_unique_integer_missing"] += real_integer is None
        counts["imaginary_interval_excludes_zero"] += not imaginary_ok
        counts["real_radius_not_strictly_below_quarter"] += not radius_ok
        counts["real_interval_excludes_nearest_midpoint_integer"] += not nearest_inside
        counts["imaginary_midpoint_nonzero"] += int(iv[0]) != 0
        counts["any_original_gate_failed"] += failed
        if failed:
            recomputed.append(j)
        real_radii.append(radius(rv))
        imag_radii.append(radius(iv))
        distances.append(distance)
        imag_centers.append(abs_mid(iv))
        if len(samples) < 10 and failed:
            samples.append({"index": j, "real": rv, "imaginary": iv,
                            "complex_unique_integer": None if integer is None else str(integer),
                            "real_unique_integer": None if real_integer is None else str(real_integer),
                            "imaginary_contains_zero": imaginary_ok,
                            "real_radius_below_quarter": radius_ok,
                            "nearest_midpoint_integer_in_real_interval": nearest_inside,
                            "midpoint_distance_to_nearest_integer": dy_record(distance)})
        if j and j % 25000 == 0:
            print(json.dumps({"diagnostic": "trace", "completed": j}), flush=True)
    original = record["failed_indices"]
    result = {"configuration": cfg, "count": len(balls), "failure_counts": counts,
              "original_failed_count": len(original),
              "recomputed_failed_indices_equal_original": recomputed == original,
              "first_recomputed_failed_indices": recomputed[:10],
              "real_radii": stats(real_radii), "imaginary_radii": stats(imag_radii),
              "midpoint_distance_to_nearest_integer": stats(distances),
              "absolute_imaginary_midpoints": stats(imag_centers),
              "stored_max_real_radius": record["max_real_radius"],
              "first_ten_failed_samples": samples}
    return cfg, result


def diagnose_embeddings(record, request, cfg):
    checked_cfg(record["configuration"], request, cfg)
    rows = record["original_primitive_character_embeddings"]
    return {"embedding_pairs": len(rows),
            "L5": real_ball_stats([r["L5"] for r in rows]),
            "L7": real_ball_stats([r["L7"] for r in rows]),
            "P": real_ball_stats([r["P"] for r in rows]),
            "Omega": record["Omega"], "A": record["A"],
            "period_factor": record["complete_period_factor"],
            "tail_bounds": record["tail_bounds"],
            "tail_bounds_below_target": record["tail_bounds_below_target"]}


def diagnose_bin(record, request, cfg, index):
    checked_cfg(record["configuration"], request, cfg)
    assert record["shard_index"] == index and record["complete"]
    rows = len(range(index+1, cfg["a_max"]+1, cfg["shard_count"]))
    assert record["row_count"] == rows
    assert record["completed_through_a"] == index+1+(rows-1)*cfg["shard_count"]
    assert len(record["bins"]) == 4
    components = []
    for label, values in zip(record["bin_basis"], record["bins"]):
        assert len(values) == cfg["n"]
        components.append({"basis": label, **real_ball_stats(values)})
    return {"shard_index": index, "complete": True, "row_count": rows,
            "term_count": record["term_count"], "components": components}


def diagnose_chirps(core_source, cfg):
    """Execute only the retained original chirps function, never core.main or a DFT."""
    tree = ast.parse(core_source)
    functions = [node for node in tree.body
                 if isinstance(node, ast.FunctionDef) and node.name == "chirps"]
    assert len(functions) == 1
    function_source = ast.get_source_segment(core_source, functions[0])
    namespace = {"acb": acb}
    exec(compile(function_source, "<retained-original-chirps-only>", "exec"), namespace)
    n = cfg["n"]
    ctx.prec = cfg["prec_bits"]
    started = time.monotonic()
    old = namespace["chirps"](n)
    selected = sorted(set([0, 1, 2, 10, 41, 42, 100, 1000, 10000,
                           n//4, n//2, 3*n//4, n-1]))
    thresholds = [-128, -64, -2, 0, 64, 1024]
    first_crossings = {str(e): None for e in thresholds}
    old_radii = []
    comparisons = []
    for j, value in enumerate(old):
        serial = serial_acb(value)
        r = max([radius(serial[0]), radius(serial[1])], key=cmp_to_key(dy_compare))
        old_radii.append(r)
        for exponent in thresholds:
            if first_crossings[str(exponent)] is None and dy_compare(r, (1, exponent)) >= 0:
                first_crossings[str(exponent)] = j
        if j in selected:
            residue = j*j % (2*n)
            direct = (acb(residue)/n).exp_pi_i()
            difference = value-direct
            comparisons.append({"index": j, "phase_numerator_mod_2n": residue,
                                "phase_denominator": n,
                                "original_recurrence": serial,
                                "direct_independent_phase": serial_acb(direct),
                                "difference_real_contains_zero": bool(difference.real.contains(0)),
                                "difference_imaginary_contains_zero": bool(difference.imag.contains(0))})
    return {"n": n, "precision": ctx.prec,
            "retained_function_sha256": hashlib.sha256(function_source.encode()).hexdigest(),
            "retained_function": function_source,
            "direct_formula": "acb((j*j) % (2*n)) / n, then exp_pi_i",
            "old_max_component_radii": stats(old_radii),
            "first_index_radius_at_least_power_of_two": first_crossings,
            "representative_comparisons": comparisons,
            "elapsed_seconds": time.monotonic()-started,
            "lattice_enumerations": 0, "DFTs": 0}


def run():
    request = json.loads(REQUEST.read_text())
    assert sha(SCRIPT) == request["diagnostic_source_sha256"]
    assert flint.__version__ == request["python_flint_version"] == "0.9.0"
    run_id = os.environ["GITHUB_RUN_ID"]
    attempt = os.environ.get("GITHUB_RUN_ATTEMPT", "1")
    out = Path(os.environ["RUNNER_TEMP"]) / "R717-trace-diagnostic-output"
    out.mkdir(parents=True, exist_ok=True)
    write_json(SESSION, {"out": str(out), "result": request["result"],
                         "request_sha256": sha(REQUEST)})
    completed = out / "R717-diagnostic-summary.json"
    if completed.exists():
        prior = json.loads(completed.read_text())
        if prior.get("complete") and prior["request_sha256"] == sha(REQUEST):
            assert prior["diagnostic_source_sha256"] == sha(SCRIPT)
            print("REUSED_COMPLETE_DIAGNOSTIC", flush=True)
            return
        raise RuntimeError("Existing diagnostic is incomplete or incompatible")
    sources = []
    for path in [SCRIPT, REQUEST, WORKFLOW,
                 TOPIC/"scripts/p41_public_actions_recovery.py",
                 REPO/"README.md", TOPIC/"README.md"]:
        rel = path.relative_to(REPO)
        archive = out/"sources"/(str(rel)+".gz")
        archive_bytes(archive, path.read_bytes())
        sources.append({"path": str(rel), "sha256": sha(path),
                        "archive": str(archive.relative_to(out)), "archive_sha256": sha(archive)})
    write_json(out/"public-actions-input.json",
               {"result": request["result"], "source_commit": os.environ["GITHUB_SHA"],
                "request": request, "sources": sources,
                "source_repository": "Rogerhu12/math-research-public",
                "execution_environment": "public-repository-github-actions",
                "mathematical_completion_claimed": False})
    write_json(out/"run-receipt.json", {"complete": False, "kind": "retained-ball-diagnostic"})
    try:
        dest = Path(os.environ["RUNNER_TEMP"])/"R717-trace-diagnostic-input"
        dest.mkdir(parents=True, exist_ok=True)
        subprocess.run(["gh", "run", "download", str(request["source_run_id"]),
                        "--repo", "Rogerhu12/math-research-public",
                        "--name", request["source_artifact_name"], "--dir", str(dest)],
                       check=True, timeout=900)
        paths = {}
        manifest = []
        for name, expected in request["input_files_sha256"].items():
            matches = list(dest.rglob(name))
            assert len(matches) == 1, (name, len(matches))
            path = matches[0]
            actual = sha(path)
            assert actual == expected, (name, actual, expected)
            paths[name] = path
            manifest.append({"file": name, "bytes": path.stat().st_size,
                             "sha256": actual, "retained_source_artifact": request["source_artifact_name"]})
        write_json(out/"verified-retained-inputs.json", {"files": manifest})
        cfg, trace_report = diagnose_traces(
            read_gzip(paths["R717-integral-trace-balls.json.gz"]), request)
        write_json(out/"R717-trace-diagnostic.json", trace_report)
        print(json.dumps({"diagnostic": "trace", "failure_counts": trace_report["failure_counts"]}), flush=True)
        embeddings_report = diagnose_embeddings(
            read_gzip(paths["R717-complex-embeddings.json.gz"]), request, cfg)
        write_json(out/"R717-embedding-diagnostic.json", embeddings_report)
        bin_reports = []
        for i in range(4):
            report = diagnose_bin(read_gzip(paths[f"R717-bins-{i}.json.gz"]), request, cfg, i)
            bin_reports.append(report)
            write_json(out/f"R717-bin-{i}-diagnostic.json", report)
            print(json.dumps({"diagnostic": "bin", "shard": i, "complete": True}), flush=True)
        core_archive = paths["R717_certified_original_CM_norm.py.gz"]
        with gzip.open(core_archive, "rb") as stream:
            core_bytes = stream.read()
        assert hashlib.sha256(core_bytes).hexdigest() == request["original_core_sha256"]
        chirp_report = diagnose_chirps(core_bytes.decode(), cfg)
        write_json(out/"R717-chirp-diagnostic.json", chirp_report)
        output_records = [{"file": p.name, "sha256": sha(p), "bytes": p.stat().st_size}
                          for p in sorted(out.glob("R717-*-diagnostic.json"))]
        summary = {"complete": True, "kind": "retained-ball-diagnostic",
                   "diagnostic_source_sha256": sha(SCRIPT), "request_sha256": sha(REQUEST),
                   "configuration": cfg, "verified_inputs": manifest,
                   "trace_failure_counts": trace_report["failure_counts"],
                   "trace_real_radii": trace_report["real_radii"],
                   "trace_imaginary_radii": trace_report["imaginary_radii"],
                   "embedding_P_radii": embeddings_report["P"]["radius"],
                   "bin_max_radii": [[x["radius"]["maximum"] for x in r["components"]]
                                     for r in bin_reports],
                   "chirp_first_radius_crossings":
                       chirp_report["first_index_radius_at_least_power_of_two"],
                   "diagnostic_outputs": output_records,
                   "lattice_enumerations": 0, "DFTs": 0,
                   "new_integer_trace_certificate": False,
                   "actual_M2_value_computed": False}
        write_json(completed, summary)
        write_json(out/"run-receipt.json", {"complete": True,
                   "kind": "retained-ball-diagnostic", "summary_sha256": sha(completed)})
        print(json.dumps({"status": "DIAGNOSTIC_COMPLETE", "summary": str(completed),
                          "summary_sha256": sha(completed)}), flush=True)
    except BaseException:
        (out/"R717-diagnostic-failure.txt").write_text(traceback.format_exc())
        raise


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("phase", choices=["run", "publish", "verify"])
    args = ap.parse_args()
    if args.phase == "run":
        run()
        return
    session = json.loads(SESSION.read_text())
    out = Path(session["out"])
    if args.phase == "publish":
        raise SystemExit(publish({"result": session["result"]}, out, "serre-cartier"))
    else:
        summary = json.loads((out/"R717-diagnostic-summary.json").read_text())
        assert summary["complete"] and summary["lattice_enumerations"] == summary["DFTs"] == 0
        for item in summary["diagnostic_outputs"]:
            assert sha(out/item["file"]) == item["sha256"]
        print("RETAINED_DIAGNOSTIC_VERIFIED")


if __name__ == "__main__":
    main()
