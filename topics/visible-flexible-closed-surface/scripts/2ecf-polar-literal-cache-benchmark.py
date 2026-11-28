#!/usr/bin/env python3
"""Audit exact-input memoization of the unchanged polar source arithmetic.

The source files remain untouched. Cache hits return copies of previously
computed binary64 arrays; misses retain the original operation ordering.
This is a separate evaluator audit and is not installed into live sources.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
import argparse
from collections import OrderedDict
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import types
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def install(source):
    curve = source.master.curve.raw
    original_theta = curve.theta
    phases, thetas = OrderedDict(), OrderedDict()
    coefficient = curve.coeff.copy()
    modes = curve.modes.copy()
    stats = dict(phaseHits=0, phaseMisses=0, thetaHits=0, thetaMisses=0,
        peakPhaseCacheBytes=0, phaseCacheLimitBytes=48*1024*1024)
    memory = [0]

    def derivative(instance, theta, order=0):
        theta = np.asarray(theta).reshape(-1)
        key = (theta.dtype.str, theta.shape, theta.tobytes())
        if key in phases:
            phase = phases.pop(key)
            phases[key] = phase
            stats["phaseHits"] += 1
        else:
            phase = np.exp(1j*theta[:, None]*modes)
            stats["phaseMisses"] += 1
            if phase.nbytes <= stats["phaseCacheLimitBytes"]:
                while phases and memory[0]+phase.nbytes > stats["phaseCacheLimitBytes"]:
                    _, removed = phases.popitem(last=False)
                    memory[0] -= removed.nbytes
                phases[key] = phase
                memory[0] += phase.nbytes
                stats["peakPhaseCacheBytes"] = max(stats["peakPhaseCacheBytes"], memory[0])
        # Exactly the same coefficient powers, multiplication, matrix product
        # and real selection as the published literal derivative.
        return (phase @ (coefficient*(1j*modes[:, None])**order)).real

    def theta(instance, u):
        u = np.asarray(u).reshape(-1)
        key = (u.dtype.str, u.shape, u.tobytes())
        if key in thetas:
            value = thetas.pop(key)
            thetas[key] = value
            stats["thetaHits"] += 1
            return value.copy()
        stats["thetaMisses"] += 1
        value = original_theta(u)
        thetas[key] = value.copy()
        if len(thetas) > 64:
            thetas.popitem(last=False)
        return value

    curve.derivative = types.MethodType(derivative, curve)
    curve.theta = types.MethodType(theta, curve)
    return stats


def main():
    ap = argparse.ArgumentParser()
    for key in ("scripts", "ramp-master", "coast-master", "output"):
        ap.add_argument("--"+key, type=Path, required=True)
    args = ap.parse_args()
    path = args.scripts/"6a65-geometry-nonfold-polar-compatible-inverse.py"
    original_module = load(path, "literal_benchmark_original")
    original = original_module.NonfoldPolarConnector(args.scripts, args.ramp_master, args.coast_master)
    cases, saved = [], []
    for N in (128, 192, 256):
        angles = 2*np.pi*(np.arange(N)+(0.5 if N == 256 else 0.))/N
        for fraction in (.17, .413, .79):
            s = original.b+fraction*original.L
            start = time.monotonic()
            packet = original.jet(s, angles)
            elapsed = time.monotonic()-start
            saved.append(packet)
            row = dict(angles=N, angularOffsetInSteps=(.5 if N==256 else 0.), s=s,
                literalSeconds=elapsed)
            cases.append((row, angles))
            print(json.dumps(dict(event="literal_baseline", **row)), flush=True)
    fast_module = load(path, "literal_benchmark_cached")
    fast = fast_module.NonfoldPolarConnector(args.scripts, args.ramp_master, args.coast_master)
    stats = install(fast)
    rows = []
    for (row, angles), baseline in zip(cases, saved):
        start = time.monotonic()
        packet = fast.jet(row["s"], angles)
        elapsed = time.monotonic()-start
        differences = {key:float(np.max(abs(packet[key]-baseline[key])))
            for key in ("X", "Xs", "Xu", "Xss", "Xsu", "Xuu")}
        identical = all(packet[key].tobytes() == baseline[key].tobytes() for key in differences)
        row.update(cachedSeconds=elapsed, sixJetMaxDifferences=differences,
            allActualSixJetBytesIdentical=identical,
            originalMaximumInverseResidual=baseline["maximumInverseResidual"],
            cachedMaximumInverseResidual=packet["maximumInverseResidual"])
        rows.append(row)
        print(json.dumps(dict(event="literal_cache_comparison", **row)), flush=True)
        if not identical:
            raise ArithmeticError("The evaluator optimization changed actual source bytes")
    out = dict(schema="2ecf-literal-polar-exact-input-arithmetic-cache-benchmark-v1",
        sourceEntrySHA256=sha(path), evaluatorEntrySHA256=sha(__file__),
        rampMasterSHA256=sha(args.ramp_master), coastMasterSHA256=sha(args.coast_master),
        actualComparisons=rows, cacheStatistics=stats,
        originalInverseReceipts=original.inverse_receipts, cachedInverseReceipts=fast.inverse_receipts,
        allInverseReceiptsUnchanged=original.inverse_receipts == fast.inverse_receipts,
        allSourceFilesUnchanged=True, installedIntoLiveProduction=False,
        sourceTargetMetricNotEvaluatedHere=True, finiteComparisonsOnly=True,
        literalTotalSeconds=sum(row["literalSeconds"] for row in rows),
        cachedTotalSeconds=sum(row["cachedSeconds"] for row in rows))
    if args.output.exists():
        raise FileExistsError("Fresh evaluator audit output required")
    args.output.write_text(json.dumps(out, separators=(",", ":"), allow_nan=False)+"\n")
    print(json.dumps(dict(event="literal_cache_audit_finished", SHA256=sha(args.output),
        literalSeconds=out["literalTotalSeconds"], cachedSeconds=out["cachedTotalSeconds"],
        stats=stats)), flush=True)


if __name__ == "__main__":
    main()
