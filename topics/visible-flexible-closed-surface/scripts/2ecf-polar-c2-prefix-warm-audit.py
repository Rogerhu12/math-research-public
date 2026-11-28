#!/usr/bin/env python3
"""Compare actual inherited warm jets on every old and new production point."""
import os
for k in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[k] = "1"
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scripts", type=Path, required=True)
    ap.add_argument("--prepare-entry", type=Path, required=True)
    ap.add_argument("--prepared", type=Path, required=True)
    ap.add_argument("--warm-state", type=Path, required=True)
    ap.add_argument("--new-initial", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.output.exists():
        raise FileExistsError("Fresh actual report required")
    start = time.monotonic()
    prepare = load(args.prepare_entry, "expanded_polar_warm_prepare")
    saved, definition, basis, caches, mods, parent, olddef, oldbasis = prepare.validate_prepared(args)
    old = json.loads(args.warm_state.read_text())
    new = json.loads(args.new_initial.read_text())
    oldz = np.asarray(old["z"], dtype=np.float64).reshape(oldbasis.nb, oldbasis.na)
    newz = np.asarray(new["z"], dtype=np.float64).reshape(basis.nb, basis.na)
    exact, transfer = mods["extension"].prolongate_exact(oldbasis, basis, oldz)
    if exact.tobytes() != newz.tobytes():
        raise ArithmeticError("Actual warm saved coefficients differ from exact copying")
    results = {}
    for key, cache in caches.items():
        oldcache = mods["generic"].Cached(parent["caches"][key])
        mask = np.isin(cache.nodes, oldcache.nodes)
        rows = np.searchsorted(cache.nodes, oldcache.nodes)
        copied = (cache.jets[rows].tobytes() == oldcache.jets.tobytes()
            and cache.radius[rows].tobytes() == oldcache.radius.tobytes())
        errors = {name: np.zeros(6) for name in ("old", "new", "all")}
        for lo in range(0, len(cache.nodes), 12):
            nodes = cache.nodes[lo:lo+12]
            a = oldbasis.packet(oldbasis.matrices(nodes), oldz, len(cache.u))
            b = basis.packet(basis.matrices(nodes), newz, len(cache.u))
            error = np.max(np.abs(a-b), axis=(2, 3))
            for name, selection in (("old", mask[lo:lo+12]), ("new", ~mask[lo:lo+12]),
                    ("all", np.ones(len(nodes), dtype=bool))):
                if np.any(selection):
                    errors[name] = np.maximum(errors[name], np.max(error[selection], axis=0))
        results[key] = dict(angles=len(cache.u), oldRadials=int(mask.sum()),
            newRadials=int((~mask).sum()), inheritedBackgroundAndRadiusBytesExact=copied,
            maximumAbsoluteSixJetDifferences={k: v.tolist() for k, v in errors.items()})
    report = dict(schema="2ecf-actual-polar-warm-all-production-points-audit-v1",
        warmStateSHA256=sha(args.warm_state), newInitialSHA256=sha(args.new_initial),
        preparedSHA256=sha(args.prepared), transfer=transfer, groups=results,
        mathematicalWholeFieldEqualitySource="R248 local seven-knot equality and literal zero-pad coefficient injection",
        finiteFloatingEvaluationComparisonsOnly=True, newGlobalRoundoffBoundClaimed=False,
        originalBackgroundRoundoffNotRemoved=True, seconds=time.monotonic()-start)
    args.output.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps(dict(SHA256=sha(args.output), **report), allow_nan=False))


if __name__ == "__main__":
    main()
