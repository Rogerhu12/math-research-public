#!/usr/bin/env python3
"""Consume R248 in the actual polar source, preserving all old sampled jets.

The fixed target metric and physical parameters do not change.  The old
5292-dimensional correction space is included exactly in a 12789-dimensional
C2 space.  The new left knots coincide with the actual prefix source knots.
Two interior Gauss points per every physical spline span are added to the old
97-node grids; only genuinely new source rows are recomputed.
"""
from __future__ import annotations
import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np

SCHEMA = "2ecf-polar-C2-full-prefix-direct-205-node-v1"
PARENT_SHA = "4e6aaee2178c621e1207f6d5b06d58d075aea1c0566f84c8b506cfd588db0ddd"
EXTENSION_SHA = "a418343e1a7229ff6f5ca8508952808c2e1d7c01ef7ba9a64cf3e802ed47151c"
BACKGROUND_SHA = "58e7080d51c0c0a7d584e688c9ec1b995fdffb72c0c0a21eec9a8f23f178c3fd"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
        allow_nan=False).encode()).hexdigest()


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def write(path, value):
    path = Path(path)
    if path.exists():
        raise FileExistsError("Fresh actual output required: " + str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, separators=(",", ":"), allow_nan=False) + "\n")
    return sha(path)


def emit(event, **value):
    print(json.dumps(dict(event=event, **value), allow_nan=False), flush=True)


def modules(scripts):
    names = dict(parent="6a65-geometry-nonfold-cartesian-prepare-v2.py",
        extension="6a65-cartesian-c2-support-extension.py",
        background="6a65-geometry-nonfold-polar-background-v2.py",
        stream="6a65-cartesian-complete-stream.py",
        generic="6a65-geometry-gap-window-cartesian.py")
    for key, expected in (("parent", PARENT_SHA), ("extension", EXTENSION_SHA),
                          ("background", BACKGROUND_SHA)):
        if sha(scripts / names[key]) != expected:
            raise ValueError("Published production dependency changed: " + key)
    return {key: module(scripts / name, "polar_extended_" + key)
            for key, name in names.items()}


def load_parent(args, mods):
    parent_args = argparse.Namespace(scripts=args.scripts,
        background=args.scripts / "6a65-geometry-nonfold-polar-background-v2.py",
        prepared=args.parent_prepared)
    return mods["parent"].validate_prepared(parent_args, mods["stream"], mods["background"])


def extended_basis(args, old, meta, extension):
    # The 16 internal new knots are the actual source's internal/terminal
    # ramp nodes; the last interval is the existing coast.
    with np.load(args.ramp_master) as ramp:
        c = float(ramp["centralLength"])
        left = np.r_[c + ramp["sx"], meta["b"]]
    if c != meta["c"] or len(left) != 18 or not np.all(np.diff(left) > 0):
        raise ValueError("The actual 16-cell ramp and coast source are required")
    basis, _ = extension.extend_left_c2(old, left,
        np.full(len(left) - 2, 3, dtype=int))
    if basis.dimension != 12789 or basis.nb != 87 or basis.na != 147:
        raise ArithmeticError("The full inherited-plus-prefix space changed")
    return basis


def extended_grid(old_nodes, basis):
    lo, hi = basis.breaks[:-1], basis.breaks[1:]
    mid, half = (lo + hi) / 2, (hi - lo) / 2
    gauss = np.sort(np.r_[mid - half / np.sqrt(3.), mid + half / np.sqrt(3.)])
    nodes = np.unique(np.r_[old_nodes, gauss])
    added = np.setdiff1d(nodes, old_nodes)
    if len(gauss) != 108 or len(added) != 108 or len(nodes) != 205:
        raise ValueError("The explicit full-span quadrature changed")
    counts = [int(np.count_nonzero((nodes > a) & (nodes < b))) for a, b in zip(lo, hi)]
    if min(counts) < 2:
        raise ArithmeticError("Every nonempty quintic span needs two interior positive weights")
    ds = np.empty(len(nodes))
    ds[0], ds[-1] = (nodes[1] - nodes[0]) / 2, (nodes[-1] - nodes[-2]) / 2
    ds[1:-1] = (nodes[2:] - nodes[:-2]) / 2
    return nodes, added, ds / basis.end, counts


def cache(args):
    start = time.monotonic()
    mods = modules(args.scripts)
    parent, olddef, oldbasis, oldcaches = load_parent(args, mods)
    meta = parent["sourceMetadata"]
    basis = extended_basis(args, oldbasis, meta, mods["extension"])
    old = oldcaches[args.group]
    nodes, added, trap, counts = extended_grid(old.nodes, basis)
    prefix = Path(str(args.prefix) + "-" + args.group)
    with mods["background"].NonfoldPolarBackground(args.scripts, args.candidate,
            args.target_definition, args.ramp_master, args.coast_master) as source:
        if source.metadata != meta:
            raise ValueError("Expanded support must retain exactly the original source and g")
        packet = source.cache(added, old.u, str(prefix) + "-new", batch_size=1)
    natural = source.exit_receipt["targetDefinitionOracle"]
    if natural.get("actualOSExitCode") != 0 or natural.get("naturalExit") is not True:
        raise ArithmeticError("The true target metric source did not naturally exit zero")
    newjets = np.load(packet["files"]["jets"], mmap_mode="r")
    newradius = np.load(packet["files"]["radius"], mmap_mode="r")
    paths = {key: Path(str(prefix) + suffix) for key, suffix in
        (("jets", "-jets.npy"), ("radius", "-radius.npy"), ("report", "-cache.json"))}
    if any(p.exists() for p in paths.values()):
        raise FileExistsError("Fresh full merged cache required")
    jets = np.lib.format.open_memmap(paths["jets"], mode="w+", dtype="<f8",
        shape=(len(nodes), 6, len(old.u), 3))
    radius = np.lib.format.open_memmap(paths["radius"], mode="w+", dtype="<f8",
        shape=(len(nodes), 3))
    oldrows, newrows = np.searchsorted(nodes, old.nodes), np.searchsorted(nodes, added)
    jets[oldrows], radius[oldrows] = old.jets, old.radius
    jets[newrows], radius[newrows] = newjets, newradius
    jets.flush(); radius.flush()
    if jets[oldrows].tobytes() != old.jets.tobytes() or radius[oldrows].tobytes() != old.radius.tobytes():
        raise ArithmeticError("An actual inherited source row changed")
    del jets, radius, newjets, newradius
    zero = json.loads(args.target_definition.read_text())
    weights = dict(metric=trap, curvature=float(zero["curvatureOptions"]["weight"]) * trap,
        geometry=float(zero["geometryOptions"]["weight"]) * trap)
    receipt = dict(schema=SCHEMA + "-merged-cache", source=meta,
        parentPreparedSHA256=sha(args.parent_prepared), parentRecord=parent["caches"][args.group],
        newSourceCache=packet["files"], newSourceCacheSHA256={k: sha(v) for k, v in packet["files"].items()},
        targetSourceExit=source.exit_receipt, inheritedRows=int(len(old.nodes)),
        inheritedSixJetAndRadiusBytesUnchanged=True, newDirectRows=len(added),
        actualAllRadialRows=len(nodes), actualAngles=len(old.u),
        actualInteriorPointCountsBySplineSpan=counts, allSpanWeightsStrictlyPositive=True,
        sourceDefinitionSHA256=meta["sourceDefinitionSHA256"], sourceChanged=False,
        targetMetricChanged=False, seconds=time.monotonic() - start)
    write(paths["report"], receipt)
    record = dict(nodes=nodes.tolist(), angles=old.u.tolist(),
        weights={k: v.tolist() for k, v in weights.items()},
        files={k: str(v.resolve()) for k, v in paths.items()},
        SHA256={k: sha(v) for k, v in paths.items()},
        sourceDefinitionSHA256=meta["sourceDefinitionSHA256"])
    report = dict(schema=SCHEMA + "-group", group=args.group,
        parentPrepared=str(args.parent_prepared.resolve()), parentPreparedSHA256=sha(args.parent_prepared),
        basis=basis.definition, record=record, sourceMetadata=meta,
        preparationEntrySHA256=sha(__file__), extensionHelperSHA256=EXTENSION_SHA,
        rampMaster=str(args.ramp_master.resolve()), rampMasterSHA256=sha(args.ramp_master),
        exactSourceIdentity=olddef["sourceIdentity"], ownAcceptedSteps=0,
        inheritedRowsCopiedExactly=True, newDirectRows=len(added),
        actualSourceExit=source.exit_receipt, seconds=time.monotonic() - start)
    digest = write(str(prefix) + "-group.json", report)
    emit("extended_polar_group_complete", group=args.group, SHA256=digest,
        columns=basis.dimension, inheritedRows=len(old.nodes), newDirectRows=len(added),
        fullRows=len(nodes), angles=len(old.u), seconds=report["seconds"])


def assemble(args):
    mods = modules(args.scripts)
    parent, olddef, oldbasis, oldcaches = load_parent(args, mods)
    meta = parent["sourceMetadata"]
    basis = extended_basis(args, oldbasis, meta, mods["extension"])
    groups, records = {}, {}
    for key in ("training", "observer"):
        path = Path(str(args.prefix) + "-" + key + "-group.json")
        item = json.loads(path.read_text())
        if (item["schema"] != SCHEMA + "-group" or item["group"] != key
                or item["parentPreparedSHA256"] != sha(args.parent_prepared)
                or item["sourceMetadata"] != meta or item["basis"] != basis.definition
                or item["preparationEntrySHA256"] != sha(__file__)):
            raise ValueError("Complete groups must bind the same source, g and exact new basis")
        cached = mods["generic"].Cached(item["record"])
        expected, _, _, _ = extended_grid(oldcaches[key].nodes, basis)
        if not np.array_equal(cached.nodes, expected):
            raise ValueError("Full old-plus-new grid changed")
        groups[key] = dict(path=str(path.resolve()), SHA256=sha(path))
        records[key] = item["record"]
    recipe = copy.deepcopy(olddef["recipe"])
    recipe["basis"].update(radialBasisCount=basis.nb, support="central_end_to_developed_cut",
        prefixCorrectionReleased=True, physicalKnotsAuthoritative=True)
    recipe["quadrature"].update(kind="old 97 nodes plus two Gauss nodes per every new spline span; trapezoid weights",
        radialCount=205, oldSourceRowsKeptExactly=True, inheritedColumns=5292, addedColumns=7497)
    definition = dict(sourceIdentity=olddef["sourceIdentity"], basis=basis.definition,
        recipe=recipe, pointConfig=olddef["pointConfig"],
        completePhysicalCuts=np.unique(np.r_[olddef["completePhysicalCuts"], basis.breaks]).tolist(),
        correctionSupport=[basis.c, basis.end], fixedPrefixSupport=[0, basis.c],
        completeHalfDomain=olddef["completeHalfDomain"], operatorSources=olddef["operatorSources"],
        newPreparationEntrySHA256=sha(__file__), extensionHelperSHA256=EXTENSION_SHA,
        parentPreparedSHA256=sha(args.parent_prepared), targetMetricChanged=False,
        sourcePositionChanged=False, oldFieldExactlyContained=True,
        runIdentity=olddef["runIdentity"], groupReceipts=groups,
        rampMasterSHA256=sha(args.ramp_master))
    report = dict(schema=SCHEMA + "-prepared", definition=definition,
        definitionSHA256=canonical(definition), sourceMetadata=meta, caches=records,
        parentPrepared=str(args.parent_prepared.resolve()), parentPreparedSHA256=sha(args.parent_prepared),
        rampMaster=str(args.ramp_master.resolve()), groupReceipts=groups,
        sourceBindingComplete=True, ownExtendedAcceptedSteps=0,
        fullContinuousMetricCertificate=False, wholeClosedReachCertified=False)
    path = Path(str(args.prefix) + "-prepared.json")
    digest = write(path, report)
    emit("extended_polar_prepared", path=str(path), SHA256=digest,
        columns=basis.dimension, points=205 * 320, rows=205 * 320 * 14,
        newAcceptedSteps=0, parentAcceptedStepsBorrowed=False)


def validate_prepared(args):
    saved = json.loads(args.prepared.read_text())
    if saved.get("schema") != SCHEMA + "-prepared":
        raise ValueError("Actual complete-prefix prepared required")
    definition = saved["definition"]
    if canonical(definition) != saved["definitionSHA256"] or definition["newPreparationEntrySHA256"] != sha(__file__):
        raise ValueError("Prepared definition or production preparation source changed")
    args.parent_prepared, args.ramp_master = Path(saved["parentPrepared"]), Path(saved["rampMaster"])
    if sha(args.parent_prepared) != saved["parentPreparedSHA256"] or sha(args.ramp_master) != definition["rampMasterSHA256"]:
        raise ValueError("Actual parent prepared or source master changed")
    mods = modules(args.scripts)
    parent, olddef, oldbasis, oldcaches = load_parent(args, mods)
    basis = extended_basis(args, oldbasis, saved["sourceMetadata"], mods["extension"])
    if basis.definition != definition["basis"] or olddef["sourceIdentity"] != definition["sourceIdentity"]:
        raise ValueError("All new Cartesian directions and the original g must be preserved")
    caches = {}
    for key, record in saved["caches"].items():
        receipt = saved["groupReceipts"][key]
        if sha(receipt["path"]) != receipt["SHA256"]:
            raise ValueError("Direct cache receipt changed")
        group = json.loads(Path(receipt["path"]).read_text())
        if group["record"] != record:
            raise ValueError("Actual cache record changed")
        caches[key] = mods["generic"].Cached(record)
    if set(caches) != {"training", "observer"}:
        raise ValueError("Both complete 14-row groups are required")
    return saved, definition, basis, caches, mods, parent, olddef, oldbasis


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=("cache", "assemble", "check"))
    ap.add_argument("--scripts", type=Path, required=True)
    for key in ("parent-prepared", "candidate", "target-definition", "ramp-master", "coast-master", "prepared"):
        ap.add_argument("--" + key, type=Path)
    ap.add_argument("--prefix", type=Path, required=True)
    ap.add_argument("--group", choices=("training", "observer"))
    args = ap.parse_args()
    if args.scripts.parents[2] in args.prefix.resolve().parents:
        raise ValueError("Reproducible arrays remain outside Git")
    if args.mode == "cache":
        cache(args)
    elif args.mode == "assemble":
        assemble(args)
    else:
        saved, definition, basis, caches, *_ = validate_prepared(args)
        emit("extended_polar_checked", columns=basis.dimension,
            shapes={k: [len(v.nodes), len(v.u)] for k, v in caches.items()})


if __name__ == "__main__":
    main()
