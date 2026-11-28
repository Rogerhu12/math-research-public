#!/usr/bin/env python3
"""Compare saved full fields on one frozen independent finite G3 grid.

This newly declared positive trapezoid objective is only a warm-start
selection aid. It is neither a production cost history nor a certificate.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    out = importlib.util.module_from_spec(spec)
    sys.modules[name] = out
    spec.loader.exec_module(out)
    return out


def main():
    ap = argparse.ArgumentParser()
    for key in ("scripts", "prepared", "observer", "target-definition", "output"):
        ap.add_argument("--"+key, type=Path, required=True)
    ap.add_argument("--states", type=Path, nargs="+", required=True)
    args = ap.parse_args()
    started = time.monotonic()
    prep = module(Path(__file__).with_name("2ecf-polar-c2-prefix-prepare.py"), "candidate_comparison_prepare")
    consumer = module(Path(__file__).with_name("2ecf-polar-c2-prefix-observe.py"), "candidate_comparison_consumer")
    area = module(args.scripts/"6a65-geometry-area-ratio-power-two.py", "candidate_comparison_area")
    saved, definition, basis, caches, mods, *_ = prep.validate_prepared(args)
    src = json.loads(args.observer.read_text())
    if src["preparedSHA256"] != prep.sha(args.prepared):
        raise ValueError("The actual comparison grid must bind the same prepared source")
    for key, path in src["files"].items():
        if prep.sha(path) != src["SHA256"][key]:
            raise ValueError("Actual observer cache changed")
    target = json.loads(args.target_definition.read_text())
    if prep.sha(args.target_definition) != saved["sourceMetadata"]["sourceDefinition"]["sourceHashes"]["targetDefinition"]:
        raise ValueError("Comparison weights must come from the same source target definition")
    nodes, angles = np.asarray(src["physicalNodes"]), np.asarray(src["angles"])
    ds = np.empty(len(nodes))
    ds[0], ds[-1] = (nodes[1]-nodes[0])/2, (nodes[-1]-nodes[-2])/2
    ds[1:-1] = (nodes[2:]-nodes[:-2])/2
    radial = ds/basis.end
    factors = dict(metric=1., curvature=float(target["curvatureOptions"]["weight"]),
        geometry=float(target["geometryOptions"]["weight"]))
    jets = np.load(src["files"]["jets"], mmap_mode="r")
    radius = np.load(src["files"]["radius"], mmap_mode="r")
    point = mods["stream"].point
    config = point.PointConfig(**definition["pointConfig"])
    reports = []
    for path in args.states:
        state = json.loads(path.read_text())
        if state["preparedSHA256"] != prep.sha(args.prepared) or state["modelDefinition"]["basis"] != basis.definition:
            raise ValueError("Only complete saved fields of this same target are comparable")
        z = np.asarray(state["z"], float).reshape(basis.nb, basis.na)
        total = 0.
        parts = dict(metric=0., curvature=0., geometry=0., area=0.)
        for lo in range(0, len(nodes), 12):
            ns = nodes[lo:lo+12]
            packet = jets[lo:lo+12]+consumer.direct_packet(basis, ns, z, angles)
            r = np.broadcast_to(radius[lo:lo+12, 0, None], (len(ns), len(angles)))
            w = radial[lo:lo+12, None]/len(angles)
            values = point.PointLinearized(packet.swapaxes(1, 2), r, config,
                {key:factor*w for key,factor in factors.items()})
            stat = mods["stream"]._block_statistics(values, ns, len(angles))
            for key, value in stat["groupSquaredNorm"].items():
                parts[key] += value
            parts["area"] += area.AreaPacket(packet, r, w, .5).stats["squaredNorm"]
        row = dict(path=str(path), stateSHA256=prep.sha(path), ownAcceptedSteps=state["ownExtendedAcceptedSteps"],
            actualSelectionCostSquared=float(sum(parts.values())), componentCostSquared=parts)
        reports.append(row)
        print(json.dumps(row), flush=True)
    reports.sort(key=lambda row:row["actualSelectionCostSquared"])
    out = dict(schema="2ecf-actual-finite-G3-positive-trapezoid-candidate-comparison-v1",
        preparedSHA256=prep.sha(args.prepared), observerSHA256=prep.sha(args.observer),
        entrySHA256=prep.sha(__file__), weights="one grid: trapezoid ds/S times 1/N; same original curvature/geometry weights; q2 strength 1",
        actualRadialCount=len(nodes), actualAngularCount=len(angles), candidates=reports,
        neitherOldTrainingCostNorDenseG10Baseline=True, acceptsNotPerformed=True,
        finiteSamplesOnly=True, continuousCertificate=False, seconds=time.monotonic()-started)
    print(json.dumps(dict(outputSHA256=prep.write(args.output, out), best=reports[0], seconds=out["seconds"])), flush=True)


if __name__ == "__main__":
    main()
