#!/usr/bin/env python3
"""Independent full-half observer with shifted 256 angles and Gauss-3 spans.

Its samples do not enter the production 128/192-angle LM objective.  The
correction jets are evaluated by direct trigonometric sums at the actual
shifted angles, rather than by relabelling an unshifted FFT grid.
"""
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


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, value):
    if Path(path).exists():
        raise FileExistsError("Fresh independent output required")
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(value, separators=(",", ":"), allow_nan=False)+"\n")
    return sha(path)


def source_and_basis(args):
    prepare = load(args.prepare_entry, "polar_independent_prepare")
    saved, definition, basis, caches, mods, *_ = prepare.validate_prepared(args)
    return saved, definition, basis, mods


def cache(args):
    start = time.monotonic()
    saved, definition, basis, mods = source_and_basis(args)
    meta = saved["sourceMetadata"]
    x, _ = np.polynomial.legendre.leggauss(3)
    a, b = basis.breaks[:-1], basis.breaks[1:]
    span = ((a+b)[:, None]/2 + (b-a)[:, None]*x/2).ravel()
    nodes = np.unique(np.r_[0., basis.c/2, basis.breaks, span,
        np.linspace(meta["S"], meta["cuff"], 18)])
    angles = 2*np.pi*(np.arange(256)+.5)/256
    with mods["background"].NonfoldPolarBackground(args.scripts, args.candidate,
            args.target_definition, args.ramp_master, args.coast_master) as source:
        if source.metadata != meta:
            raise ValueError("Observer must consume the same position background and g")
        raw = source.cache(nodes, angles, args.prefix, batch_size=1)
    child = source.exit_receipt["targetDefinitionOracle"]
    if child.get("actualOSExitCode") != 0 or child.get("naturalExit") is not True:
        raise ArithmeticError("Actual observer target-source exit failed")
    report = dict(schema="2ecf-polar-prefix-G3-shifted256-independent-source-v1",
        preparedSHA256=sha(args.prepared), sourceDefinitionSHA256=meta["sourceDefinitionSHA256"],
        sourceIdentity=definition["sourceIdentity"], physicalNodes=nodes.tolist(),
        angles=angles.tolist(), files=raw["files"],
        SHA256={k: sha(v) for k, v in raw["files"].items()},
        allFullPrefixSpansUseThreeGaussPoints=True, angularShiftInMeshSteps=.5,
        exactTrainingGridReused=False, sourceEntrySHA256=sha(__file__),
        actualTargetSourceExit=source.exit_receipt, seconds=time.monotonic()-start)
    digest = write(str(args.prefix)+"-independent.json", report)
    print(json.dumps(dict(event="independent_cache_complete", SHA256=digest,
        radials=len(nodes), angles=len(angles), points=len(nodes)*len(angles),
        seconds=report["seconds"])), flush=True)


def direct_packet(basis, nodes, z, angles):
    matrices = basis.matrices(nodes)
    amplitudes = [m @ z for m in matrices]
    harmonics = np.zeros((3, basis.na, len(angles), 3))
    for j, (component, k, kind) in enumerate(basis.channels):
        phase = k*angles
        if kind == "cos":
            f, df, ddf = np.cos(phase), -k*np.sin(phase), -k*k*np.cos(phase)
        elif kind == "sin":
            f, df, ddf = np.sin(phase), k*np.cos(phase), -k*k*np.sin(phase)
        else:
            raise ValueError("Actual real angular channels required")
        harmonics[0, j, :, component] = f
        harmonics[1, j, :, component] = df
        harmonics[2, j, :, component] = ddf
    angular = lambda ri, ui: np.einsum("sc,cuk->suk", amplitudes[ri], harmonics[ui], optimize=True)
    return np.stack((angular(0, 0), angular(1, 0), angular(0, 1),
        angular(2, 0), angular(1, 1), angular(0, 2)), axis=1)


def observe(args):
    start = time.monotonic()
    saved, definition, basis, mods = source_and_basis(args)
    src = json.loads(args.observer.read_text())
    state = json.loads(args.state.read_text())
    if src["preparedSHA256"] != sha(args.prepared) or state["preparedSHA256"] != sha(args.prepared):
        raise ValueError("The independent observer and actual state need this exact g and space")
    if src["sourceEntrySHA256"] != sha(__file__) or state["modelDefinition"]["basis"] != basis.definition:
        raise ValueError("Actual observer or all Cartesian coefficients changed")
    for k, v in src["files"].items():
        if sha(v) != src["SHA256"][k]:
            raise ValueError("The direct independent source cache changed")
    nodes, angles = np.array(src["physicalNodes"]), np.array(src["angles"])
    jets = np.load(src["files"]["jets"], mmap_mode="r")
    radius = np.load(src["files"]["radius"], mmap_mode="r")
    z = np.asarray(state["z"], float).reshape(basis.nb, basis.na)
    stream = mods["stream"]
    config = stream.point.PointConfig(**definition["pointConfig"])
    total = None
    for lo in range(0, len(nodes), 12):
        ns = nodes[lo:lo+12]
        packet = jets[lo:lo+12]+direct_packet(basis, ns, z, angles)
        values = stream.point.PointLinearized(packet.swapaxes(1, 2),
            np.broadcast_to(radius[lo:lo+12, 0, None], (len(ns), len(angles))),
            config, {k: np.ones((len(ns), 1))/len(angles) for k in ("metric", "curvature", "geometry")})
        part = stream._block_statistics(values, ns, len(angles))
        # The statistics helper's labels assume an unshifted grid.  The
        # actual packet above was evaluated at the shifted physical angle.
        part["worstMetric"]["u"] += float(angles[0])
        part["worstCurvature"]["u"] += float(angles[0])
        total = stream._merge_statistics(total, part)
    # A concrete check of the direct Fourier consumer on the same actual
    # nonzero field, at unshifted points supported by the production FFT.
    checknodes = np.linspace(basis.c, basis.end, 9)
    u = 2*np.pi*np.arange(128)/128
    direct = direct_packet(basis, checknodes, z, u)
    fft = basis.packet(basis.matrices(checknodes), z, 128)
    errors = np.max(np.abs(direct-fft), axis=(0, 2, 3)).tolist()
    total.pop("squaredNorm", None)
    total.pop("groupSquaredNorm", None)
    report = dict(schema="2ecf-actual-polar-independent-shifted-observation-v1",
        preparedSHA256=sha(args.prepared), stateSHA256=sha(args.state),
        sourceObserverSHA256=sha(args.observer), ownExtendedAcceptedSteps=state["ownExtendedAcceptedSteps"],
        actualRadialCount=len(nodes), actualAngularCount=len(angles),
        angularShiftInMeshSteps=.5, statistics=total,
        minAreaRatio=float(np.sqrt(total["minImmersion"])),
        sameActualFieldDirectVersusProductionFFTSixJetErrors=errors,
        objectiveCostNotClaimed=True, observerUsedInOptimization=False,
        finiteSamplesOnly=True, continuousMetricCertified=False, wholeClosedReachCertified=False,
        seconds=time.monotonic()-start)
    digest = write(args.output, report)
    print(json.dumps(dict(event="actual_independent_observation", SHA256=digest,
        ownAcceptedSteps=state["ownExtendedAcceptedSteps"], metric=total["maxRelativeMetric"],
        curvature=total["maxCurvature"], sigma=report["minAreaRatio"],
        worstMetric=total["worstMetric"], worstCurvature=total["worstCurvature"],
        seconds=report["seconds"])), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=("cache", "observe"))
    ap.add_argument("--scripts", type=Path, required=True)
    ap.add_argument("--prepare-entry", type=Path,
        default=Path(__file__).with_name("2ecf-polar-c2-prefix-prepare.py"))
    ap.add_argument("--prepared", type=Path, required=True)
    for key in ("candidate", "target-definition", "ramp-master", "coast-master", "prefix", "state", "observer", "output"):
        ap.add_argument("--"+key, type=Path)
    args = ap.parse_args()
    if args.mode == "cache":
        cache(args)
    else:
        observe(args)


if __name__ == "__main__":
    main()
