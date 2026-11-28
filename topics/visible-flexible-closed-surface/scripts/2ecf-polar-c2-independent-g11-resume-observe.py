#!/usr/bin/env python3
"""Fourth full-half observer with shifted 256 angles and Gauss-11 spans.

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


SCHEMA="2ecf-polar-G11-resumed-primitive-audited-observer-v2"

def fresh_source_cache(source, nodes, angles, prefix, args):
    """A new cache consumer with per-row progress, preserving old source/g."""
    refinement_entry = Path(__file__).with_name('2ecf-polar-tight-source-evaluator.py')
    memo_entry = Path(__file__).with_name('2ecf-polar-literal-cache-benchmark.py')
    refinement = load(refinement_entry, 'G10_recovery_refinement')
    memo = load(memo_entry, 'G10_recovery_exact_input_memo')
    cache_stats = memo.install(source.field)
    paths = {key:Path(str(prefix)+suffix) for key,suffix in
        (('jets','-jets.npy'),('radius','-radius.npy'),('report','-cache.json'))}
    journal = Path(str(prefix)+'-completed-rows.jsonl')
    if any(p.exists() for p in list(paths.values())+[journal]):
        raise FileExistsError('Fresh recovery files required')
    jets = np.lib.format.open_memmap(paths['jets'], mode='w+', dtype='<f8', shape=(len(nodes),6,len(angles),3))
    radius = np.lib.format.open_memmap(paths['radius'], mode='w+', dtype='<f8', shape=(len(nodes),3))
    recovery = None; recovered = 0
    if args.failed_prefix is not None:
        oldprefix = args.failed_prefix
        oldlog, oldexit = args.failed_log, args.failed_exit
        exit_record = json.loads(oldexit.read_text())
        if exit_record['returncode'] != 1 or 'Safeguarded literal inverse unresolved' not in oldlog.read_text():
            raise ValueError('The original failed process and its actual exception must be retained')
        completed = []
        for line in oldlog.read_text().splitlines():
            if line.startswith('{'):
                row = json.loads(line)
                if row.get('event') == 'actual_polar_six_jet_cache':
                    if row['radials'] != len(nodes) or row['angles'] != len(angles):
                        raise ValueError('Failed-prefix physical dimensions differ')
                    completed.append(int(row['completed']))
        recovered = max(completed)
        if recovered != 433:
            raise ValueError('This recovery explicitly binds the actual 433-row receipt')
        oldjets_path, oldradius_path = Path(str(oldprefix)+'-new-jets.npy'),Path(str(oldprefix)+'-new-radius.npy')
        oldjets, oldradius = np.load(oldjets_path,mmap_mode='r'),np.load(oldradius_path,mmap_mode='r')
        if oldjets.shape != jets.shape or oldradius.shape != radius.shape:
            raise ValueError('Failed-prefix array layout differs')
        comparisons = []
        for index in (0,recovered//2,recovered-1):
            packet = source.sample([nodes[index]], angles)
            equal = packet['jets'][0].tobytes() == oldjets[index].tobytes() and packet['radius'][0].tobytes() == oldradius[index].tobytes()
            comparisons.append(dict(index=index,s=float(nodes[index]),sameSixJetAndRadiusBytes=equal))
            if not equal: raise ArithmeticError('Failed-prefix source identity check differs')
        jets[:recovered], radius[:recovered] = oldjets[:recovered],oldradius[:recovered]
        jets.flush();radius.flush()
        if jets[:recovered].tobytes() != oldjets[:recovered].tobytes() or radius[:recovered].tobytes() != oldradius[:recovered].tobytes():
            raise ArithmeticError('Recovery altered a completed row')
        recovery = dict(originalExit=exit_record, originalLastFormalCompletedRows=recovered,
            originalNonzeroRowsObservedButNotTrusted=437,
            originalFiles={str(p):sha(p) for p in (oldlog,oldexit,oldjets_path,oldradius_path)},
            literalPrefixBytesUnchanged=True, actualIndependentSourceChecks=comparisons,
            originalProcessClaimedSuccessful=False, unreceiptedRowsRecomputed=True)
        del oldjets,oldradius
    diagnostics = []; fallbacks = []
    with journal.open('x') as progress:
        if recovered:
            progress.write(json.dumps(dict(event='recovered_formally_completed_prefix',completed=recovered,recovery=recovery),separators=(',',':'))+'\n');progress.flush()
        for index in range(recovered,len(nodes)):
            try:
                packet = source.sample([nodes[index]],angles)
            except ArithmeticError as error:
                if 'Safeguarded literal inverse unresolved' not in str(error): raise
                base = sys.modules['nonfold_fixed_weighted_formula'].base
                packet,audit = refinement.audit_row(source,float(nodes[index]),angles,base)
                audit.update(index=index,originalActualFailure=str(error))
                fallbacks.append(audit)
                print(json.dumps(dict(event='actual_nested_inverse_fallback',index=index,s=float(nodes[index]),
                    maximumIndependentPrimitiveResidual=max(r['independentPrimitiveResidual'] for x in audit['strongerPrimitiveChecks'] for r in x['rootChecks']))),flush=True)
            jets[index],radius[index]=packet['jets'][0],packet['radius'][0]
            jets.flush();radius.flush()
            diagnostics.extend(packet['source_point_diagnostics'])
            row=dict(event='actual_recovered_source_row_complete',completed=index+1,s=float(nodes[index]),
                sourceDiagnostics=packet['source_point_diagnostics'])
            progress.write(json.dumps(row,separators=(',',':'))+'\n');progress.flush()
            if index%8 == 0 or index+1 == len(nodes):
                print(json.dumps(dict(event='actual_dense_recovered_cache',completed=index+1,radials=len(nodes),angles=len(angles),seconds=time.monotonic()-source.started)),flush=True)
    del jets,radius
    receipt=dict(schema=SCHEMA+'-actual-resumable-source',source=source.metadata,
        physicalSamples=np.asarray(nodes).tolist(),angles=np.asarray(angles).tolist(),
        actualJetOrder=['X','Xs','Xu','Xss','Xsu','Xuu'],
        rawJetSHA256=sha(paths['jets']),rawRadiusSHA256=sha(paths['radius']),
        recovery=recovery,recoveredFormallyCompletedRows=recovered,newRowsActuallyEvaluated=len(nodes)-recovered,
        originalMathematicalSourceAndMetricUnchanged=True,evaluationConsumerChanged=True,
        refinementEntrySHA256=sha(refinement_entry),memoizationEntrySHA256=sha(memo_entry),
        exactInputMemoStatistics=cache_stats,actualFallbacks=fallbacks,
        fallbackPreservesOuterResidualTolerance=5e-14,
        newSourcePointDiagnostics=diagnostics,originalRecoveredDiagnosticsNotInvented=True,
        allRowsFormallyComplete=True,rowCompletionJournal=str(journal),rowCompletionJournalSHA256=sha(journal),
        intervalSourceCertificate=False)
    write(paths['report'],receipt)
    return dict(files={k:str(v.resolve()) for k,v in paths.items()},receipt=receipt)


def cache(args):
    start = time.monotonic()
    saved, definition, basis, mods = source_and_basis(args)
    meta = saved["sourceMetadata"]
    x, _ = np.polynomial.legendre.leggauss(11)
    a, b = basis.breaks[:-1], basis.breaks[1:]
    span = ((a+b)[:, None]/2 + (b-a)[:, None]*x/2).ravel()
    nodes = np.unique(np.r_[0., basis.c/2, basis.breaks, span,
        np.linspace(meta["S"], meta["cuff"], 18)])
    angles = 2*np.pi*(np.arange(256)+.5)/256
    reuse = json.loads(args.reuse_source.read_text())
    if (reuse["sourceIdentity"] != definition["sourceIdentity"]
            or reuse["sourceDefinitionSHA256"] != meta["sourceDefinitionSHA256"]
            or not np.array_equal(np.asarray(reuse["angles"]), angles)):
        raise ValueError("Reuse requires the same literal background, g and actual shifted angles")
    for key, path in reuse["files"].items():
        if sha(path) != reuse["SHA256"][key]:
            raise ValueError("Existing independent raw cache changed")
    oldnodes = np.asarray(reuse["physicalNodes"])
    shared = np.intersect1d(nodes, oldnodes)
    added = np.setdiff1d(nodes, oldnodes)
    with mods["background"].NonfoldPolarBackground(args.scripts, args.candidate,
            args.target_definition, args.ramp_master, args.coast_master) as source:
        if source.metadata != meta:
            raise ValueError("Observer must consume the same position background and g")
        newraw = fresh_source_cache(source, added, angles, str(args.prefix)+"-new", args)
    child = source.exit_receipt["targetDefinitionOracle"]
    if child.get("actualOSExitCode") != 0 or child.get("naturalExit") is not True:
        raise ArithmeticError("Actual observer target-source exit failed")
    paths = {key: Path(str(args.prefix)+suffix) for key, suffix in
        (("jets", "-jets.npy"), ("radius", "-radius.npy"), ("report", "-cache.json"))}
    if any(path.exists() for path in paths.values()):
        raise FileExistsError("Fresh fourth observer merged arrays required")
    jets = np.lib.format.open_memmap(paths["jets"], mode="w+", dtype="<f8",
        shape=(len(nodes), 6, len(angles), 3))
    radius = np.lib.format.open_memmap(paths["radius"], mode="w+", dtype="<f8",
        shape=(len(nodes), 3))
    oldjets, oldradius = np.load(reuse["files"]["jets"], mmap_mode="r"), np.load(reuse["files"]["radius"], mmap_mode="r")
    newjets, newradius = np.load(newraw["files"]["jets"], mmap_mode="r"), np.load(newraw["files"]["radius"], mmap_mode="r")
    ii, jj, kk = np.searchsorted(nodes, shared), np.searchsorted(oldnodes, shared), np.searchsorted(nodes, added)
    jets[ii], radius[ii] = oldjets[jj], oldradius[jj]
    jets[kk], radius[kk] = newjets, newradius
    jets.flush(); radius.flush()
    if jets[ii].tobytes() != oldjets[jj].tobytes() or radius[ii].tobytes() != oldradius[jj].tobytes():
        raise ArithmeticError("A shared actual observer six-jet changed")
    del jets, radius, oldjets, oldradius, newjets, newradius
    write(paths["report"], dict(schema="2ecf-G11-shifted256-recovered-and-shared-source-cache-v2",
        sameSourceMetadata=meta, reuseSource=str(args.reuse_source), reuseSourceSHA256=sha(args.reuse_source),
        sharedPhysicalRows=len(shared), freshLiteralRows=len(added), sharedRowsBytesUnchanged=True,
        newSourceFiles=newraw["files"], newSourceSHA256={k:sha(v) for k,v in newraw["files"].items()},
        actualNewTargetSourceExit=source.exit_receipt))
    raw = dict(files={k:str(v.resolve()) for k,v in paths.items()})
    report = dict(schema="2ecf-polar-prefix-G11-shifted256-independent-source-v2",
        preparedSHA256=sha(args.prepared), sourceDefinitionSHA256=meta["sourceDefinitionSHA256"],
        sourceIdentity=definition["sourceIdentity"], physicalNodes=nodes.tolist(),
        angles=angles.tolist(), files=raw["files"],
        SHA256={k: sha(v) for k, v in raw["files"].items()},
        allFullPrefixSpansUseElevenGaussPoints=True, basis=basis.definition,
        sharedPreviousObserverRows=len(shared), freshLiteralSourceRows=len(added), angularShiftInMeshSteps=.5,
        exactTrainingGridReused=False, sourceEntrySHA256=sha(__file__),
        refinementEntrySHA256=sha(Path(__file__).with_name("2ecf-polar-tight-source-evaluator.py")),
        memoizationEntrySHA256=sha(Path(__file__).with_name("2ecf-polar-literal-cache-benchmark.py")),
        evaluationConsumerChanged=True, mathematicalSourceAndMetricUnchanged=True,
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
    if (state["preparedSHA256"] != sha(args.prepared)
            or src["sourceIdentity"] != definition["sourceIdentity"]
            or src["sourceDefinitionSHA256"] != saved["sourceMetadata"]["sourceDefinitionSHA256"]
            or src["basis"] != basis.definition):
        raise ValueError("The fourth observer and actual state need this exact g and coefficient space")
    if src["sourceEntrySHA256"] != sha(__file__) or state["modelDefinition"]["basis"] != basis.definition:
        raise ValueError("Actual observer or all Cartesian coefficients changed")
    for k, v in src["files"].items():
        if sha(v) != src["SHA256"][k]:
            raise ValueError("The direct independent source cache changed")
    nodes, angles = np.array(src["physicalNodes"]), np.array(src["angles"])
    jets = np.load(src["files"]["jets"], mmap_mode="r")
    radius = np.load(src["files"]["radius"], mmap_mode="r")
    designed = "logRadiusCoefficients" in state
    if designed:
        if state.get("schema") != "2ecf-polar-full-XYZ-C2-log-radius-new-metric-design-LM-v1-state":
            raise ValueError("An exact explicit metric-design state is required")
        target=state["provisionalMetricDefinition"]
        digest=hashlib.sha256(json.dumps(target,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
        if digest != state["provisionalMetricDefinitionSHA256"]:
            raise ValueError("The provisional designed g changed")
        alpha=np.asarray(state["logRadiusCoefficients"],float)
        if alpha.shape!=(basis.nb,) or not np.all(np.isfinite(alpha)) or target["coefficients"]!=alpha.tolist():
            raise ValueError("All actual designed metric parameters required")
        h,hs,hss=(B@alpha for B in basis.matrices(nodes));a,first,second=radius.T
        ex=np.exp(h);radius=np.column_stack((a*ex,(first+a*hs)*ex,(second+2*first*hs+a*(hss+hs*hs))*ex))
        if not np.all(np.isfinite(radius)) or np.any(radius[:,0]<=0):
            raise ArithmeticError("Actual independent designed radius is not finite positive")
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
    report = dict(schema="2ecf-actual-polar-G11-fourth-shifted-observation-v2",
        preparedSHA256=sha(args.prepared), stateSHA256=sha(args.state),
        sourceObserverSHA256=sha(args.observer), ownExtendedAcceptedSteps=state.get("ownExtendedAcceptedSteps",0),
        ownMetricDesignAcceptedSteps=state.get("ownMetricDesignAcceptedSteps",0),
        explicitDesignedMetricUsed=designed,
        designedMetricDefinitionSHA256=state.get("provisionalMetricDefinitionSHA256"),
        sameMetricConvergenceClaim=False,
        actualRadialCount=len(nodes), actualAngularCount=len(angles),
        angularShiftInMeshSteps=.5, statistics=total,
        producerPreparedSHA256=src["preparedSHA256"],
        actualRadialsNotInCurrentTraining=int(len(np.setdiff1d(nodes, saved["caches"]["training"]["nodes"]))),
        originalProducerPreparedCanDifferOnlyInQuadrature=True,
        minAreaRatio=float(np.sqrt(total["minImmersion"])),
        sameActualFieldDirectVersusProductionFFTSixJetErrors=errors,
        objectiveCostNotClaimed=True, observerUsedInOptimization=False,
        finiteSamplesOnly=True, continuousMetricCertified=False, wholeClosedReachCertified=False,
        seconds=time.monotonic()-start)
    digest = write(args.output, report)
    print(json.dumps(dict(event="actual_independent_observation", SHA256=digest,
        ownAcceptedSteps=state.get("ownExtendedAcceptedSteps",state.get("ownMetricDesignAcceptedSteps",0)), metric=total["maxRelativeMetric"],
        curvature=total["maxCurvature"], sigma=report["minAreaRatio"],
        worstMetric=total["worstMetric"], worstCurvature=total["worstCurvature"],
        seconds=report["seconds"])), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=("cache", "observe"))
    ap.add_argument("--scripts", type=Path, required=True)
    ap.add_argument("--prepare-entry", type=Path,
        default=Path(__file__).with_name("2ecf-polar-c2-g10-resume-prepare.py"))
    ap.add_argument("--prepared", type=Path, required=True)
    for key in ("candidate", "target-definition", "ramp-master", "coast-master", "prefix", "state", "observer", "output", "reuse-source", "failed-prefix", "failed-log", "failed-exit"):
        ap.add_argument("--"+key, type=Path)
    args = ap.parse_args()
    if args.mode == "cache":
        cache(args)
    else:
        observe(args)


if __name__ == "__main__":
    main()
