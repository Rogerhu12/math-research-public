#!/usr/bin/env python3
"""Read-only decomposition of uncontrollable complete rows on frozen caches."""
from __future__ import annotations
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scripts", type=Path, required=True)
    ap.add_argument("--prepared", type=Path, required=True)
    ap.add_argument("--state", type=Path, required=True)
    ap.add_argument("--base-entry", type=Path, default=Path(__file__).with_name("6a65-geometry-gap-window-cartesian.py"))
    ap.add_argument("--background", type=Path, default=Path(__file__).with_name("6a65-geometry-gap-window-background.py"))
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError("Fresh actual fixed-cost receipt required")
    started = time.monotonic()
    if sha(args.base_entry) != "ca22b417066c3e7f46470b876eabb57ed4d1673858000d31d4c99d8acc3f2f86":
        raise ValueError("Frozen actual prepared loader changed")
    base = module(args.base_entry, "gap_fixed_cost_base")
    stream = module(args.scripts/"6a65-cartesian-complete-stream.py", "gap_fixed_cost_stream")
    background = module(args.background, "gap_fixed_cost_background")
    prepared, definition, basis, caches = base.validate_prepared(args, stream, background)
    state = json.loads(args.state.read_text())
    if state.get("preparedSHA256") != sha(args.prepared) or state.get("basis") != basis.definition:
        raise ValueError("Actual complete state changed frozen source/basis")
    z = np.asarray(state["z"], float).reshape(basis.nb, basis.na)
    config = stream.point.PointConfig(**definition["pointConfig"])
    lo, hi = definition["correctionSupport"]
    groups = {}
    for name, cache in caches.items():
        groups[name] = {}
        allweights = {key: .5*np.asarray(value, float)
            for key, value in prepared["caches"][name]["weights"].items()}
        for region, mask in (("fixed_prefix", cache.nodes <= lo),
                             ("fixed_tail", cache.nodes >= hi),
                             ("all_fixed", (cache.nodes <= lo)|(cache.nodes >= hi))):
            nodes = cache.nodes[mask]
            matrices = basis.matrices(nodes)
            delta = basis.packet(matrices, z, len(cache.u))
            if np.any(delta != 0):
                raise ArithmeticError("Claimed fixed region has a nonzero correction jet")
            value = stream.observe(basis, nodes, {key: value[mask] for key, value in allweights.items()},
                                   cache, z, len(cache.u), config, 12)
            value["allSixCorrectionJetsExactlyZero"] = True
            value["physicalNodeMinimum"] = float(nodes[0])
            value["physicalNodeMaximum"] = float(nodes[-1])
            groups[name][region] = value
    combined = {}
    import copy
    for region in ("fixed_prefix", "fixed_tail", "all_fixed"):
        total = None
        for name in groups:
            part = copy.deepcopy(groups[name][region])
            for key in ("worstMetric", "worstCurvature"):
                part[key]["grid"] = name
            total = stream._merge_statistics(total, part)
        combined[region] = total
    result = dict(schema="6a65-gap105-frozen-region-complete-cost-v1",
        preparedSHA256=sha(args.prepared), actualStateSHA256=sha(args.state),
        sourceDefinitionSHA256=prepared["sourceMetadata"]["sourceDefinitionSHA256"],
        entrySHA256=sha(__file__), sourceUnchanged=True, correctionSupport=[lo,hi],
        complete13RowsIncluded=True, weights={"training":.5,"observer":.5},
        groups=groups,combined=combined, acceptedStepsAdded=0,
        noCostSubtractedFromActualSolve=True, noSourceReevaluation=True,
        continuousCertificate=False, seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(result,separators=(",",":"),allow_nan=False)+"\n")
    print(json.dumps(dict(actualReportSHA256=sha(args.out),combined=combined,
                         seconds=result["seconds"]),allow_nan=False),flush=True)


if __name__ == "__main__":
    main()
