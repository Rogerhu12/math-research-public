#!/usr/bin/env python3
"""Dense same-g quadrature after actual independent prefix peak detection.

All old 205 nodes and all 236 third-observer radial nodes are retained. Ten
Gauss nodes are added in every nonempty quintic span. Only missing literal
background rows are regenerated at the unchanged 128/192 physical angles.
The complete 12789 coefficient space and source position/target g stay fixed.
"""
from __future__ import annotations
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np

SCHEMA = "2ecf-polar-C2-full-prefix-G10-plus-all-old-observer-nodes-v1"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
        allow_nan=False).encode()).hexdigest()


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    out = importlib.util.module_from_spec(spec)
    sys.modules[name] = out
    spec.loader.exec_module(out)
    return out


def write(path, value):
    path = Path(path)
    if path.exists():
        raise FileExistsError("Fresh dense source output required: " + str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, separators=(",", ":"), allow_nan=False)+"\n")
    return sha(path)


def load_parent(args):
    entry = Path(args.parent_entry)
    parent = module(entry, "polar_G10_parent_prepare")
    probe = argparse.Namespace(scripts=args.scripts, prepared=args.parent_prepared)
    saved, definition, basis, caches, mods, *_ = parent.validate_prepared(probe)
    observer = json.loads(args.third_observer.read_text())
    if (observer["preparedSHA256"] != sha(args.parent_prepared)
            or observer["sourceIdentity"] != definition["sourceIdentity"]
            or observer["sourceDefinitionSHA256"] != saved["sourceMetadata"]["sourceDefinitionSHA256"]
            or observer["angularShiftInMeshSteps"] != .5):
        raise ValueError("The actual independent observation must bind this original source")
    if basis.dimension != 12789 or (basis.nb, basis.na) != (87, 147):
        raise ValueError("No Cartesian directions may be removed or added here")
    return saved, definition, basis, caches, mods, observer


def dense_grid(old_nodes, basis, observer):
    roots, _ = np.polynomial.legendre.leggauss(10)
    lo, hi = basis.breaks[:-1], basis.breaks[1:]
    gauss = (((lo+hi)[:, None]+(hi-lo)[:, None]*roots)/2).ravel()
    nodes = np.unique(np.r_[old_nodes, observer["physicalNodes"], basis.breaks, gauss])
    added = np.setdiff1d(nodes, old_nodes)
    counts = [int(np.count_nonzero((nodes > a) & (nodes < b))) for a, b in zip(lo, hi)]
    if len(gauss) != 540 or min(counts) < 10:
        raise ArithmeticError("Every physical quintic span requires all ten interior Gauss nodes")
    weight = np.empty(len(nodes))
    weight[0], weight[-1] = (nodes[1]-nodes[0])/2, (nodes[-1]-nodes[-2])/2
    weight[1:-1] = (nodes[2:]-nodes[:-2])/2
    if np.any(weight <= 0):
        raise ArithmeticError("Every retained finite point must receive positive weight")
    return nodes, added, weight/basis.end, counts


def cache(args):
    started = time.monotonic()
    parent, olddef, basis, oldcaches, mods, observer = load_parent(args)
    old = oldcaches[args.group]
    nodes, added, trap, counts = dense_grid(old.nodes, basis, observer)
    prefix = Path(str(args.prefix)+"-"+args.group)
    with mods["background"].NonfoldPolarBackground(args.scripts, args.candidate,
            args.target_definition, args.ramp_master, args.coast_master) as source:
        if source.metadata != parent["sourceMetadata"]:
            raise ValueError("Dense quadrature must retain the identical source position and g")
        raw = source.cache(added, old.u, str(prefix)+"-new", batch_size=1)
    child = source.exit_receipt["targetDefinitionOracle"]
    if child.get("actualOSExitCode") != 0 or child.get("naturalExit") is not True:
        raise ArithmeticError("Actual target oracle must naturally exit zero")
    newjets = np.load(raw["files"]["jets"], mmap_mode="r")
    newradius = np.load(raw["files"]["radius"], mmap_mode="r")
    paths = {key: Path(str(prefix)+suffix) for key, suffix in
        (("jets", "-jets.npy"), ("radius", "-radius.npy"), ("report", "-cache.json"))}
    if any(path.exists() for path in paths.values()):
        raise FileExistsError("Fresh dense full cache required")
    jets = np.lib.format.open_memmap(paths["jets"], mode="w+", dtype="<f8",
        shape=(len(nodes), 6, len(old.u), 3))
    radius = np.lib.format.open_memmap(paths["radius"], mode="w+", dtype="<f8",
        shape=(len(nodes), 3))
    ii, jj = np.searchsorted(nodes, old.nodes), np.searchsorted(nodes, added)
    jets[ii], radius[ii] = old.jets, old.radius
    jets[jj], radius[jj] = newjets, newradius
    jets.flush(); radius.flush()
    if jets[ii].tobytes() != old.jets.tobytes() or radius[ii].tobytes() != old.radius.tobytes():
        raise ArithmeticError("An inherited source row changed")
    del jets, radius, newjets, newradius
    target = json.loads(args.target_definition.read_text())
    weights = dict(metric=trap, curvature=float(target["curvatureOptions"]["weight"])*trap,
        geometry=float(target["geometryOptions"]["weight"])*trap)
    receipt = dict(schema=SCHEMA+"-merged-cache", source=source.metadata,
        parentPreparedSHA256=sha(args.parent_prepared), parentRecord=parent["caches"][args.group],
        newSourceCache=raw["files"], newSourceCacheSHA256={k:sha(v) for k,v in raw["files"].items()},
        targetSourceExit=source.exit_receipt, inheritedRows=len(old.nodes),
        inheritedSixJetAndRadiusBytesUnchanged=True, newDirectRows=len(added),
        actualAllRadialRows=len(nodes), actualAngles=len(old.u),
        actualInteriorPointCountsBySplineSpan=counts, allSpanWeightsStrictlyPositive=True,
        independentObserverRadialNodesNowIncludedInTraining=True,
        independentObserverShiftedAnglesNotIncluded=True,
        sourceDefinitionSHA256=source.metadata["sourceDefinitionSHA256"],
        sourceChanged=False, targetMetricChanged=False, coefficientSpaceChanged=False,
        seconds=time.monotonic()-started)
    write(paths["report"], receipt)
    record = dict(nodes=nodes.tolist(), angles=old.u.tolist(),
        weights={k:v.tolist() for k,v in weights.items()}, files={k:str(v.resolve()) for k,v in paths.items()},
        SHA256={k:sha(v) for k,v in paths.items()},
        sourceDefinitionSHA256=source.metadata["sourceDefinitionSHA256"])
    out = dict(schema=SCHEMA+"-group", group=args.group,
        parentPrepared=str(args.parent_prepared.resolve()), parentPreparedSHA256=sha(args.parent_prepared),
        parentEntry=str(args.parent_entry.resolve()), parentEntrySHA256=sha(args.parent_entry),
        thirdObserver=str(args.third_observer.resolve()), thirdObserverSHA256=sha(args.third_observer),
        basis=basis.definition, sourceMetadata=source.metadata, record=record,
        preparationEntrySHA256=sha(__file__), ownAcceptedSteps=0,
        inheritedRowsCopiedExactly=True, newDirectRows=len(added),
        actualSourceExit=source.exit_receipt, seconds=time.monotonic()-started)
    digest = write(str(prefix)+"-group.json", out)
    print(json.dumps(dict(event="dense_same_g_group_complete", group=args.group, SHA256=digest,
        inheritedRows=len(old.nodes), newDirectRows=len(added), fullRows=len(nodes),
        angles=len(old.u), seconds=out["seconds"])), flush=True)


def assemble(args):
    parent, olddef, basis, oldcaches, mods, observer = load_parent(args)
    records, receipts = {}, {}
    for key in ("training", "observer"):
        path = Path(str(args.prefix)+"-"+key+"-group.json")
        group = json.loads(path.read_text())
        if (group["schema"] != SCHEMA+"-group" or group["group"] != key
                or group["parentPreparedSHA256"] != sha(args.parent_prepared)
                or group["parentEntrySHA256"] != sha(args.parent_entry)
                or group["thirdObserverSHA256"] != sha(args.third_observer)
                or group["preparationEntrySHA256"] != sha(__file__)
                or group["basis"] != basis.definition or group["sourceMetadata"] != parent["sourceMetadata"]):
            raise ValueError("Both actual dense source groups must share the exact definition")
        cached = mods["generic"].Cached(group["record"])
        nodes, _, _, counts = dense_grid(oldcaches[key].nodes, basis, observer)
        if not np.array_equal(cached.nodes, nodes):
            raise ValueError("Dense same-g radial nodes changed")
        records[key] = group["record"]
        receipts[key] = dict(path=str(path.resolve()), SHA256=sha(path))
    recipe = copy.deepcopy(olddef["recipe"])
    recipe["quadrature"].update(kind="old 205 plus actual G3 observer radials plus G10 per quintic span; positive trapezoid",
        radialCount=len(nodes), oldSourceRowsKeptExactly=True, gaussNodesPerSpan=10,
        thirdObserverRadialSamplesNowTraining=True)
    definition = copy.deepcopy(olddef)
    definition.update(recipe=recipe, newPreparationEntrySHA256=sha(__file__),
        parentPreparedSHA256=sha(args.parent_prepared), parentPreparationEntrySHA256=sha(args.parent_entry),
        thirdObserverSHA256=sha(args.third_observer), groupReceipts=receipts,
        targetMetricChanged=False, sourcePositionChanged=False, coefficientSpaceChanged=False,
        oldFieldExactlyContained=True, finiteQuadratureChanged=True,
        actualMinimumInteriorPointsPerSpan=min(counts))
    out = dict(schema=SCHEMA+"-prepared", definition=definition,
        definitionSHA256=canonical(definition), sourceMetadata=parent["sourceMetadata"], caches=records,
        parentPrepared=str(args.parent_prepared.resolve()), parentPreparedSHA256=sha(args.parent_prepared),
        parentEntry=str(args.parent_entry.resolve()), parentEntrySHA256=sha(args.parent_entry),
        thirdObserver=str(args.third_observer.resolve()), thirdObserverSHA256=sha(args.third_observer),
        groupReceipts=receipts, sourceBindingComplete=True, ownExtendedAcceptedSteps=0,
        fullContinuousMetricCertificate=False, wholeClosedReachCertified=False)
    digest = write(str(args.prefix)+"-prepared.json", out)
    print(json.dumps(dict(event="dense_same_g_prepared", SHA256=digest, columns=basis.dimension,
        radials=len(nodes), points=len(nodes)*320, rows=len(nodes)*320*14)), flush=True)


def validate_prepared(args):
    saved = json.loads(args.prepared.read_text())
    definition = saved["definition"]
    if (saved["schema"] != SCHEMA+"-prepared" or canonical(definition) != saved["definitionSHA256"]
            or definition["newPreparationEntrySHA256"] != sha(__file__)):
        raise ValueError("Exact dense same-g prepared required")
    probe = argparse.Namespace(scripts=args.scripts, parent_prepared=Path(saved["parentPrepared"]),
        parent_entry=Path(saved["parentEntry"]), third_observer=Path(saved["thirdObserver"]))
    for key in ("parentPrepared", "parentEntry", "thirdObserver"):
        if sha(saved[key]) != saved[key+"SHA256"]:
            raise ValueError("Dense source parent binding changed: "+key)
    parent, olddef, basis, oldcaches, mods, observer = load_parent(probe)
    if basis.definition != definition["basis"] or olddef["sourceIdentity"] != definition["sourceIdentity"]:
        raise ValueError("Actual unchanged correction space and target required")
    caches = {}
    for key, record in saved["caches"].items():
        receipt = saved["groupReceipts"][key]
        if sha(receipt["path"]) != receipt["SHA256"]:
            raise ValueError("Dense group receipt changed")
        group = json.loads(Path(receipt["path"]).read_text())
        if group["record"] != record:
            raise ValueError("Dense literal cache changed")
        caches[key] = mods["generic"].Cached(record)
        expected, _, _, _ = dense_grid(oldcaches[key].nodes, basis, observer)
        if not np.array_equal(caches[key].nodes, expected):
            raise ValueError("Dense same-g nodes changed")
    if set(caches) != {"training", "observer"}:
        raise ValueError("Both actual full groups required")
    return saved, definition, basis, caches, mods, parent, olddef, basis


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=("cache", "assemble", "check"))
    ap.add_argument("--scripts", type=Path, required=True)
    ap.add_argument("--parent-entry", type=Path, default=Path(__file__).with_name("2ecf-polar-c2-prefix-prepare.py"))
    for key in ("parent-prepared", "third-observer", "candidate", "target-definition", "ramp-master", "coast-master", "prepared", "prefix"):
        ap.add_argument("--"+key, type=Path)
    ap.add_argument("--group", choices=("training", "observer"))
    args = ap.parse_args()
    if args.mode == "cache":
        cache(args)
    elif args.mode == "assemble":
        assemble(args)
    else:
        saved, definition, basis, caches, *_ = validate_prepared(args)
        print(json.dumps(dict(validated=True, columns=basis.dimension,
            radialCounts={k:len(v.nodes) for k,v in caches.items()})), flush=True)


if __name__ == "__main__":
    main()
