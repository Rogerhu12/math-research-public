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

SCHEMA = "2ecf-polar-C2-full-prefix-G10-consistent-arc-split-source-v3"


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


def fresh_source_cache(source, nodes, angles, prefix, args):
    """A new cache consumer with per-row progress, preserving old source/g."""
    refinement_entry = Path(__file__).with_name('2ecf-polar-refined-arc-source-evaluator.py')
    memo_entry = Path(__file__).with_name('2ecf-polar-literal-cache-benchmark.py')
    refinement = module(refinement_entry, 'G10_recovery_refinement')
    memo = module(memo_entry, 'G10_recovery_exact_input_memo')
    cache_stats = memo.install(source.field)
    paths = {key:Path(str(prefix)+suffix) for key,suffix in
        (('jets','-jets.npy'),('radius','-radius.npy'),('report','-cache.json'))}
    journal = Path(str(prefix)+'-completed-rows.jsonl')
    if any(p.exists() for p in list(paths.values())+[journal]):
        raise FileExistsError('Fresh recovery files required')
    jets = np.lib.format.open_memmap(paths['jets'], mode='w+', dtype='<f8', shape=(len(nodes),6,len(angles),3))
    radius = np.lib.format.open_memmap(paths['radius'], mode='w+', dtype='<f8', shape=(len(nodes),3))
    recovery = None; recovered = 0
    if args.group == 'training' and args.failed_prefix is not None:
        oldprefix = Path(str(args.failed_prefix)+'-training')
        oldlog, oldexit = Path(str(oldprefix)+'-source.log'), Path(str(oldprefix)+'-source-exit.json')
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
        if recovered != 665:
            raise ValueError('This recovery explicitly binds the actual 665-row receipt')
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
            originalNonzeroRowsObservedButNotTrusted=667,
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
    started=time.monotonic()
    parent,olddef,basis,oldcaches,mods,observer=load_parent(args)
    old=oldcaches['observer'];nodes,added,trap,counts=dense_grid(old.nodes,basis,observer)
    if (args.first,args.stop) not in ((502,610),(610,753)):
        raise ValueError('Explicit disjoint continuation chunks [502,610), [610,753) required')
    if args.group!='observer' or args.failed_prefix is not None:
        raise ValueError('The chunk producer only generates its actual new observer rows')
    with mods['background'].NonfoldPolarBackground(args.scripts,args.candidate,args.target_definition,
            args.ramp_master,args.coast_master) as source:
        if source.metadata!=parent['sourceMetadata']:raise ValueError('Original mathematical source/g changed')
        raw=fresh_source_cache(source,added[args.first:args.stop],old.u,str(args.prefix)+'-new',args)
    child=source.exit_receipt['targetDefinitionOracle']
    if child.get('actualOSExitCode')!=0 or child.get('naturalExit')is not True:
        raise ArithmeticError('Actual chunk target oracle did not naturally exit zero')
    out=dict(schema=SCHEMA+'-actual-chunk',first=args.first,stop=args.stop,
        fullAddedRowCount=len(added),physicalNodes=added[args.first:args.stop].tolist(),angles=old.u.tolist(),
        parentPreparedSHA256=sha(args.parent_prepared),sourceMetadata=source.metadata,basis=basis.definition,
        files=raw['files'],SHA256={k:sha(v) for k,v in raw['files'].items()},
        preparationEntrySHA256=sha(__file__),
        refinementEntrySHA256=sha(Path(__file__).with_name('2ecf-polar-refined-arc-source-evaluator.py')),
        actualTargetExit=source.exit_receipt,actualRows=args.stop-args.first,ownAcceptedSteps=0,
        completeFullSourceGroupClaimed=False,seconds=time.monotonic()-started)
    digest=write(str(args.prefix)+'-chunk.json',out)
    print(json.dumps(dict(event='actual_dense_source_chunk_complete',first=args.first,stop=args.stop,
        SHA256=digest,seconds=out['seconds'])),flush=True)


def make_group(args,key,record,basis,meta,receipt):
    out=dict(schema=SCHEMA+'-group',group=key,parentPrepared=str(args.parent_prepared.resolve()),
        parentPreparedSHA256=sha(args.parent_prepared),parentEntry=str(args.parent_entry.resolve()),
        parentEntrySHA256=sha(args.parent_entry),thirdObserver=str(args.third_observer.resolve()),
        thirdObserverSHA256=sha(args.third_observer),basis=basis.definition,sourceMetadata=meta,
        record=record,preparationEntrySHA256=sha(__file__),ownExtendedAcceptedSteps=0,
        sourceProvenance=receipt,mathematicalSourceAndMetricUnchanged=True,
        fullGroupPointCompletenessActuallyChecked=True)
    write(str(args.prefix)+'-'+key+'-group.json',out)


def assemble(args):
    start=time.monotonic()
    parent,olddef,basis,oldcaches,mods,observer=load_parent(args)
    oldtraining=Path(str(args.completed_training_prefix)+'-group.json')
    trainexit=Path(str(args.completed_training_prefix)+'-source-exit.json')
    old=json.loads(oldtraining.read_text());oe=json.loads(trainexit.read_text())
    if (oe['returncode']!=0 or old['sourceMetadata']!=parent['sourceMetadata'] or old['basis']!=basis.definition
            or old['parentPreparedSHA256']!=sha(args.parent_prepared)
            or old['preparationEntrySHA256']!=sha(Path(__file__).with_name('2ecf-polar-c2-g10-resume-prepare.py'))):
        raise ValueError('The completed original training group must actually match')
    training=mods['generic'].Cached(old['record'])
    expected,_,_,_=dense_grid(oldcaches['training'].nodes,basis,observer)
    if not np.array_equal(training.nodes,expected):raise ValueError('Adopted full training nodes differ')
    make_group(args,'training',old['record'],basis,parent['sourceMetadata'],
        dict(kind='adopt complete actual successful G10r training group without recomputation',
            groupPath=str(oldtraining),groupSHA256=sha(oldtraining),actualOSExit=oe,exitSHA256=sha(trainexit),
            allSourceFilesRetainedWithoutModification=True))
    oldobs=oldcaches['observer'];nodes,added,trap,counts=dense_grid(oldobs.nodes,basis,observer)
    failed=args.failed_observer_prefix
    journal=Path(str(failed)+'-new-completed-rows.jsonl');failure=Path(str(failed)+'-source-exit.json')
    failedlog=Path(str(failed)+'-source.log')
    records=[json.loads(line) for line in journal.read_text().splitlines()]
    if (json.loads(failure.read_text())['returncode']!=1 or
            [r['completed'] for r in records] != list(range(1,503)) or
            not np.array_equal(np.array([r['s'] for r in records]),added[:502])):
        raise ValueError('Only the actual formally completed 502 observer rows may be restored')
    partial_jets_path=Path(str(failed)+'-new-jets.npy');partial_radius_path=Path(str(failed)+'-new-radius.npy')
    partial_jets=np.load(partial_jets_path,mmap_mode='r');partial_radius=np.load(partial_radius_path,mmap_mode='r')
    checks=[]
    with mods['background'].NonfoldPolarBackground(args.scripts,args.candidate,args.target_definition,
            args.ramp_master,args.coast_master) as source:
        if source.metadata!=parent['sourceMetadata']:raise ValueError('Recovered prefix source identity changed')
        for index in (0,251,501):
            packet=source.sample([added[index]],oldobs.u)
            ok=packet['jets'][0].tobytes()==partial_jets[index].tobytes() and packet['radius'][0].tobytes()==partial_radius[index].tobytes()
            checks.append(dict(index=index,s=float(added[index]),actualSixJetAndRadiusBytesIdentical=ok))
            if not ok:raise ArithmeticError('Actual restored observer prefix source check differs')
    chunks=[]
    for prefix in args.chunk_prefixes:
        path=Path(str(prefix)+'-chunk.json');exitpath=Path(str(prefix)+'-source-exit.json')
        chunk=json.loads(path.read_text());exitrow=json.loads(exitpath.read_text())
        if (exitrow['returncode']!=0 or chunk['preparationEntrySHA256']!=sha(__file__)
                or chunk['sourceMetadata']!=parent['sourceMetadata'] or chunk['basis']!=basis.definition
                or chunk['parentPreparedSHA256']!=sha(args.parent_prepared)
                or chunk['refinementEntrySHA256']!=sha(Path(__file__).with_name('2ecf-polar-refined-arc-source-evaluator.py'))
                or not np.array_equal(np.array(chunk['physicalNodes']),added[chunk['first']:chunk['stop']])
                or not np.array_equal(np.array(chunk['angles']),oldobs.u)):
            raise ValueError('Actual complete disjoint source chunk binding failed')
        for key,path0 in chunk['files'].items():
            if sha(path0)!=chunk['SHA256'][key]:raise ValueError('Completed chunk bytes changed')
        chunks.append((chunk,dict(path=str(path),SHA256=sha(path),actualOSExit=exitrow,exitSHA256=sha(exitpath))))
    chunks.sort(key=lambda x:x[0]['first'])
    if [(x['first'],x['stop']) for x,r in chunks]!=[(502,610),(610,753)]:
        raise ValueError('Every unresolved physical source row is required exactly once')
    prefix=Path(str(args.prefix)+'-observer')
    paths={key:Path(str(prefix)+suffix) for key,suffix in (('jets','-jets.npy'),('radius','-radius.npy'),('report','-cache.json'))}
    if any(p.exists() for p in paths.values()):raise FileExistsError('Fresh full merged observer arrays required')
    jets=np.lib.format.open_memmap(paths['jets'],mode='w+',dtype='<f8',shape=(len(nodes),6,len(oldobs.u),3))
    radius=np.lib.format.open_memmap(paths['radius'],mode='w+',dtype='<f8',shape=(len(nodes),3))
    ii,jj=np.searchsorted(nodes,oldobs.nodes),np.searchsorted(nodes,added)
    jets[ii],radius[ii]=oldobs.jets,oldobs.radius
    jets[jj[:502]],radius[jj[:502]]=partial_jets[:502],partial_radius[:502]
    for chunk,receipt in chunks:
        selected=jj[chunk['first']:chunk['stop']]
        jets[selected]=np.load(chunk['files']['jets'],mmap_mode='r')
        radius[selected]=np.load(chunk['files']['radius'],mmap_mode='r')
    jets.flush();radius.flush()
    if (jets[ii].tobytes()!=oldobs.jets.tobytes() or radius[ii].tobytes()!=oldobs.radius.tobytes()
            or jets[jj[:502]].tobytes()!=partial_jets[:502].tobytes()
            or radius[jj[:502]].tobytes()!=partial_radius[:502].tobytes()
            or not np.all(np.isfinite(jets)) or not np.all(np.isfinite(radius)) or np.any(radius[:,0]<=0)):
        raise ArithmeticError('Full merged physical source data completeness failed')
    del jets,radius,partial_jets,partial_radius
    receipt=dict(schema=SCHEMA+'-full-observer-merge',parentSourceRowsKeptByteExactly=205,
        formallyRecoveredSourceRows=502,newActualDirectSourceRows=251,actualFullRadialRows=958,
        actualAngles=192,fullSixJetAndMetricDataPresent=True,sourceMetadata=parent['sourceMetadata'],
        failedPrefixFiles={str(p):sha(p) for p in (journal,failure,failedlog,partial_jets_path,partial_radius_path)},
        originalFailureRetained=True,actualRecoveredPrefixChecks=checks,prefixCheckSourceExit=source.exit_receipt,
        chunks=[r for c,r in chunks],newEvaluationConsumerSHA256=sha(__file__),
        originalMathematicalSourceAndIndependentTargetMetricUnchanged=True,
        numericalErrorNotPromotedToContinuousCertificate=True)
    write(paths['report'],receipt)
    target=json.loads(args.target_definition.read_text())
    weights=dict(metric=trap,curvature=float(target['curvatureOptions']['weight'])*trap,
        geometry=float(target['geometryOptions']['weight'])*trap)
    record=dict(nodes=nodes.tolist(),angles=oldobs.u.tolist(),weights={k:v.tolist() for k,v in weights.items()},
        files={k:str(v.resolve()) for k,v in paths.items()},SHA256={k:sha(v) for k,v in paths.items()},
        sourceDefinitionSHA256=parent['sourceMetadata']['sourceDefinitionSHA256'])
    make_group(args,'observer',record,basis,parent['sourceMetadata'],receipt)
    assemble_complete_groups(args)
    print(json.dumps(dict(event='actual_split_full_prepared_complete',seconds=time.monotonic()-start)),flush=True)


def assemble_complete_groups(args):
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
        sourceEvaluationConsumerChanged=True,
        refinementEntrySHA256=sha(Path(__file__).with_name("2ecf-polar-refined-arc-source-evaluator.py")),
        memoizationEntrySHA256=sha(Path(__file__).with_name("2ecf-polar-literal-cache-benchmark.py")),
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
    if (definition["refinementEntrySHA256"] != sha(Path(__file__).with_name("2ecf-polar-refined-arc-source-evaluator.py"))
            or definition["memoizationEntrySHA256"] != sha(Path(__file__).with_name("2ecf-polar-literal-cache-benchmark.py"))):
        raise ValueError("Actual source-evaluation consumer changed")
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
    ap.add_argument("--failed-prefix", type=Path)
    ap.add_argument("--first",type=int)
    ap.add_argument("--stop",type=int)
    ap.add_argument("--completed-training-prefix",type=Path)
    ap.add_argument("--failed-observer-prefix",type=Path)
    ap.add_argument("--chunk-prefixes",type=Path,nargs='+')
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
