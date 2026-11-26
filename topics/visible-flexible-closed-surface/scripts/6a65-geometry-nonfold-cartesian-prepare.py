#!/usr/bin/env python3
"""Direct two-grid preparation for a new polar background and all 5292 columns.

Each cache phase is a separate, naturally exited child. Assembly only seals
their complete direct arrays and independent target identity. No old gap or
Cauchy state/acceptance is synthesized. Both angular grids are training.
"""
from __future__ import annotations
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[key]="1"
import argparse,hashlib,importlib.util,json,subprocess,sys,time,uuid
from dataclasses import asdict
from pathlib import Path
import numpy as np

SCHEMA="6a65-own-polar-complete5292-direct-two-grid-fixed-independent-g-v1"
BASE_SHA="ca22b417066c3e7f46470b876eabb57ed4d1673858000d31d4c99d8acc3f2f86"
REFINED_SHA="1596f0f40bbc19aabd4ea28a51a516d1bbfb86cca35f8ff03ae6d34f7349acb1"

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def canonical(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec);sys.modules[name]=out
    spec.loader.exec_module(out);return out
def emit(event,**x):print(json.dumps(dict(event=event,**x),allow_nan=False),flush=True)
def write(path,x):
    path=Path(path)
    if path.exists():raise FileExistsError("Fresh actual output required: "+str(path))
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(x,separators=(",",":"),allow_nan=False)+"\n");return sha(path)

def components(scripts):
    basepath=Path(scripts)/"6a65-geometry-gap-window-cartesian.py"
    refinedpath=Path(scripts)/"6a65-geometry-gap-window-refined-cartesian.py"
    if sha(basepath)!=BASE_SHA or sha(refinedpath)!=REFINED_SHA:
        raise ValueError("Unchanged complete basis/cache implementation required")
    return module(basepath,"polar_prepare_generic_basis"),module(refinedpath,"polar_prepare_exact_basis_knots")

def basis5292(scripts,stream,b,S):
    base,refined=components(scripts)
    old=base.periodic_basis(stream,b,S,32,12)
    basis,_=refined.refined_basis(base,stream,old)
    if basis.dimension!=5292:raise ValueError("Every full Cartesian column required")
    return basis

def default_recipe(source_kind):
    return dict(schema=SCHEMA,sourceKind=source_kind,
        basis=dict(radialBasisCount=36,maxAngularFrequency=24,
            support="coast_end_to_developed_cut",allRealPeriodicChannels=True,
            physicalKnotsAuthoritative=True,localKnotRefinement=True),
        angles=128,observerAngles=192,normalizationQuadrature=1024,
        quadrature=dict(kind="same 97 physical nonuniform trapezoid nodes; separate full 128 and 192 angle rules",
            connectorRadials=65,allPhysicalEndpointsIncluded=True,
            groupScales=dict(training=.5,observer=.5),bothGroupsAreTraining=True,
            sameAsOld514And343Grids=False,continuousQuadratureAccuracyClaimed=False),
        radialBlock=12,sourceBatchSize=1,cachePointBlocks=True,
        preconditioner=dict(kind="banded_sobolev_h2",beta0=.01,beta1=1.,beta2=.001),
        lm=dict(damping=1e-4,maxDampingAttempts=3,alphas=[1.,.5,.25,.125],armijo=1e-4),
        lsmr=dict(maxIterations=160,atol=1e-6,btol=1e-6,conditionLimit=1e10))

def physical_grid(field):
    t=np.sin(.5*np.pi*np.linspace(0,1,65))**2
    nodes=np.unique(np.r_[np.linspace(0,field.master.c,5),field.master.c+field.master.sx,
        np.linspace(field.master.ramp_end,field.b,5),field.b+field.L*t,
        field.S+np.asarray([0,.03,.06,.1,.2,.3,.4,.46,.48])])
    if len(nodes)!=97 or nodes[0]!=0 or nodes[-1]!=field.cuff:
        raise ValueError("Explicit new complete 97-node grid changed")
    ds=np.empty(len(nodes));ds[0]=(nodes[1]-nodes[0])/2;ds[-1]=(nodes[-1]-nodes[-2])/2
    ds[1:-1]=(nodes[2:]-nodes[:-2])/2
    return nodes,ds/field.S

def sources(args):
    return dict(stream=sha(args.scripts/"6a65-cartesian-complete-stream.py"),
        point=sha(args.scripts/"6a65-cartesian-complete-point-operator.py"),
        background=sha(args.background),entry=sha(__file__),
        genericBasisAndCache=BASE_SHA,completeRefinedBasis=REFINED_SHA)

def cache_worker(args,stream,background):
    started=time.monotonic()
    for name in ("candidate","target_definition","ramp_master","coast_master"):
        if getattr(args,name) is None:raise ValueError("Actual new source input missing: "+name)
    if args.group not in ("training","observer"):raise ValueError("Explicit complete group required")
    out=Path(str(args.prefix)+"-"+args.group+"-worker.json")
    if out.exists():raise FileExistsError("Actual cache phase already exists")
    saved=json.loads(args.target_definition.read_text())
    cv,gv=saved["curvatureOptions"],saved["geometryOptions"]
    with background.NonfoldPolarBackground(args.scripts,args.candidate,args.target_definition,
            args.ramp_master,args.coast_master) as source:
        identity=background.bind_new_source_metadata(source.metadata,source.expected_hashes)
        recipe=default_recipe(background.SOURCE_KIND)
        basis=basis5292(args.scripts,stream,source.b,source.S)
        nodes,trap=physical_grid(source.field)
        N=recipe["angles" if args.group=="training" else "observerAngles"]
        weights=dict(metric=trap,curvature=float(cv["weight"])*trap,geometry=float(gv["weight"])*trap)
        conf=stream.point.PointConfig(metric_tau=float(saved["metricTau"]),
            curvature_tau=float(saved["curvatureTau"]),curvature_guide=float(cv["guide"]),
            true_cuff_height=source.metadata["Z"],central_a=source.metadata["centralA"])
        emit("new_polar_actual_cache_start",group=args.group,nodes=len(nodes),angles=N,
            columns=basis.dimension,allOriginalThirteenRows=len(nodes)*N*13)
        cache=source.cache(nodes,2*np.pi*np.arange(N)/N,str(args.prefix)+"-"+args.group,
            batch_size=recipe["sourceBatchSize"])
        record=dict(nodes=nodes.tolist(),angles=cache["u"].tolist(),
            weights={k:v.tolist() for k,v in weights.items()},files=cache["files"],
            SHA256={k:sha(v) for k,v in cache["files"].items()},
            sourceDefinitionSHA256=source.metadata["sourceDefinitionSHA256"])
        metadata=source.metadata
        cuts=np.unique(np.r_[source.integration_cuts,basis.breaks]).tolist()
    child=source.exit_receipt["targetDefinitionOracle"]
    if child.get("actualOSExitCode")!=0 or child.get("naturalExit")is not True:
        raise ArithmeticError("Independent target oracle did not naturally exit zero")
    report=dict(schema=SCHEMA+"-cache-worker",group=args.group,sourceIdentity=identity,
        sourceMetadata=metadata,record=record,basis=basis.definition,recipe=recipe,
        pointConfig=asdict(conf),completePhysicalCuts=cuts,operatorSources=sources(args),
        actualNaturalChildExit=source.exit_receipt,ownPolarAcceptedSteps=0,
        actualRunId=args.run_id,seconds=time.monotonic()-started)
    digest=write(out,report)
    emit("new_polar_actual_cache_child_complete",group=args.group,path=str(out),SHA256=digest)

def cache_phase(args):
    out=Path(str(args.prefix)+"-"+args.group+"-group.json")
    if out.exists():raise FileExistsError("A sealed actual cache phase already exists")
    command=[sys.executable,str(Path(__file__).resolve()),"_cache",*sys.argv[2:]]
    started=time.monotonic()
    process=subprocess.run(command,check=False)
    if process.returncode!=0:raise RuntimeError("Actual direct cache child exit "+str(process.returncode))
    worker=Path(str(args.prefix)+"-"+args.group+"-worker.json")
    report=json.loads(worker.read_text())
    if report["operatorSources"]["entry"]!=sha(__file__):raise ValueError("Worker entry changed")
    receipt=dict(schema=SCHEMA+"-cache-group",worker=report,workerFile=str(worker.resolve()),
        workerSHA256=sha(worker),actualCacheChildOSExitCode=process.returncode,
        actualCacheChildNaturalExit=True,seconds=time.monotonic()-started)
    digest=write(out,receipt)
    emit("new_polar_actual_group_sealed",group=args.group,path=str(out),SHA256=digest,
        actualChildOSExitCode=process.returncode,seconds=receipt["seconds"])

def sealed_group(path,label,args,background):
    saved=json.loads(Path(path).read_text())
    if (saved.get("schema")!=SCHEMA+"-cache-group" or saved.get("actualCacheChildOSExitCode")!=0
        or saved.get("actualCacheChildNaturalExit")is not True):
        raise ValueError("Actually naturally exited complete cache group required")
    if sha(saved["workerFile"])!=saved["workerSHA256"]:
        raise ValueError("Actual cache worker receipt changed")
    worker=json.loads(Path(saved["workerFile"]).read_text())
    if worker!=saved["worker"] or worker.get("group")!=label:
        raise ValueError("Saved complete group changed")
    if worker["operatorSources"]!=sources(args):raise ValueError("Actual source/operator bytes changed")
    natural=worker["actualNaturalChildExit"]["targetDefinitionOracle"]
    if natural.get("actualOSExitCode")!=0 or natural.get("naturalExit")is not True:
        raise ValueError("Target definition oracle exit was not paid")
    meta=worker["sourceMetadata"]
    if background.bind_new_source_metadata(meta,meta["sourceDefinition"]["sourceHashes"])!=worker["sourceIdentity"]:
        raise ValueError("Independent actual source identity changed")
    base,_=components(args.scripts)
    cache=base.Cached(worker["record"])
    record=worker["record"]
    if sha(record["files"]["report"])!=record["SHA256"]["report"]:raise ValueError("Cache receipt changed")
    rawreceipt=json.loads(Path(record["files"]["report"]).read_text())
    if rawreceipt["source"]!=meta or rawreceipt["rawJetSHA256"]!=record["SHA256"]["jets"]:
        raise ValueError("Cache was not sampled from this exact new source")
    return saved,worker,cache

def assemble(args,stream,background):
    if args.training_group is None or args.observer_group is None:raise ValueError("Two real cache receipts required")
    seals={};workers={};caches={}
    for key in ("training","observer"):
        seals[key],workers[key],caches[key]=sealed_group(getattr(args,key+"_group"),key,args,background)
    a,b=workers["training"],workers["observer"]
    common=("sourceIdentity","sourceMetadata","basis","recipe","pointConfig","completePhysicalCuts","operatorSources","actualRunId")
    if any(a[k]!=b[k] for k in common):raise ValueError("Separate phases did not consume exactly the same full source and g")
    if (not np.array_equal(caches["training"].nodes,caches["observer"].nodes)
        or not np.array_equal(caches["training"].radius,caches["observer"].radius)):
        raise ValueError("Independent target radius changed between angular groups")
    meta=a["sourceMetadata"];basis=basis5292(args.scripts,stream,meta["b"],meta["S"])
    if basis.definition!=a["basis"]:raise ValueError("Complete 5292 basis changed")
    records={k:v["record"] for k,v in workers.items()}
    run_identity=dict(scope="local-actual-new-polar-source" if a["actualRunId"] is None else "actual-same-job-new-polar-source",
        actualRunId=a["actualRunId"],executionUUID=str(uuid.uuid4()))
    definition=dict(sourceIdentity=a["sourceIdentity"],basis=basis.definition,recipe=a["recipe"],
        pointConfig=a["pointConfig"],completePhysicalCuts=a["completePhysicalCuts"],
        correctionSupport=[meta["b"],meta["S"]],fixedPrefixSupport=[0,meta["b"]],
        completeHalfDomain=[0,meta["cuff"]],runIdentity=run_identity,
        cacheIdentity={key:{k:record[k] for k in ("SHA256","nodes","angles","weights","sourceDefinitionSHA256")}
            for key,record in records.items()},operatorSources=a["operatorSources"])
    report=dict(schema=SCHEMA+"-prepared",definition=definition,definitionSHA256=canonical(definition),
        sourceMetadata=meta,caches=records,
        groupReceipts={k:dict(path=str(getattr(args,k+"_group").resolve()),SHA256=sha(getattr(args,k+"_group")))
            for k in ("training","observer")},
        actualNaturalChildExits={k:v["actualNaturalChildExit"] for k,v in workers.items()},
        sourceBindingComplete=True,rawArraysPublished=False,ownPolarAcceptedSteps=0,
        oldCauchyAcceptedStepsBorrowed=0,oldGapAcceptedStepsBorrowed=0,
        wholeFieldMetricToleranceCertified=False,wholeClosedReachCertified=False)
    out=Path(str(args.prefix)+"-prepared.json")
    digest=write(out,report)
    emit("new_polar_prepared",path=str(out),SHA256=digest,columns=basis.dimension,
        points=sum(len(v.nodes)*len(v.u) for v in caches.values()),allOriginalThirteenRows=True,
        ownAcceptedSteps=0,actualValueBaselineComputed=False)
    return report

def validate_prepared(args,stream,background):
    saved=json.loads(args.prepared.read_text())
    if saved.get("schema")!=SCHEMA+"-prepared" or saved.get("sourceBindingComplete")is not True:
        raise ValueError("Own actually assembled polar source required")
    definition=saved["definition"]
    if canonical(definition)!=saved["definitionSHA256"] or definition["operatorSources"]!=sources(args):
        raise ValueError("Independent prepared source/operator identity changed")
    meta=saved["sourceMetadata"]
    if background.bind_new_source_metadata(meta,meta["sourceDefinition"]["sourceHashes"])!=definition["sourceIdentity"]:
        raise ValueError("New position/target source identity changed")
    if definition["correctionSupport"]!=[meta["b"],meta["S"]] or definition["fixedPrefixSupport"]!=[0,meta["b"]]:
        raise ValueError("Entire prefix or true tail two-jets changed")
    if definition["recipe"]!=default_recipe(background.SOURCE_KIND):raise ValueError("Complete new quadrature or solver recipe changed")
    basis=basis5292(args.scripts,stream,meta["b"],meta["S"])
    if basis.definition!=definition["basis"]:raise ValueError("All 5292 directions required")
    caches={}
    for key,record in saved["caches"].items():
        receipt=saved["groupReceipts"][key]
        if sha(receipt["path"])!=receipt["SHA256"]:raise ValueError("Natural actual phase receipt changed")
        seal,worker,cache=sealed_group(receipt["path"],key,args,background)
        if worker["record"]!=record or worker["sourceMetadata"]!=meta:
            raise ValueError("Actual complete cache does not match assembled metadata")
        expected={k:record[k] for k in ("SHA256","nodes","angles","weights","sourceDefinitionSHA256")}
        if definition["cacheIdentity"][key]!=expected:raise ValueError("Actual grid or quadrature weights changed")
        caches[key]=cache
    if set(caches)!={"training","observer"}:raise ValueError("Both complete groups required")
    return saved,definition,basis,caches

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("mode",choices=("cache","_cache","assemble","check"))
    ap.add_argument("--scripts",type=Path,required=True)
    ap.add_argument("--background",type=Path,required=True)
    for name in ("candidate","target-definition","ramp-master","coast-master","prepared","training-group","observer-group"):
        ap.add_argument("--"+name,type=Path)
    ap.add_argument("--prefix",type=Path,required=True)
    ap.add_argument("--group",choices=("training","observer"))
    ap.add_argument("--run-id",type=int)
    args=ap.parse_args()
    if args.run_id is not None and args.run_id<=0:raise ValueError("A real positive Actions run ID is required if supplied")
    if args.mode=="cache":cache_phase(args);return
    stream=module(args.scripts/"6a65-cartesian-complete-stream.py","polar_prepare_complete_stream")
    background=module(args.background,"polar_prepare_explicit_source")
    if args.mode=="_cache":cache_worker(args,stream,background)
    elif args.mode=="assemble":assemble(args,stream,background)
    else:
        saved,definition,basis,caches=validate_prepared(args,stream,background)
        emit("new_polar_prepared_validated",columns=basis.dimension,
            sourceIdentity=definition["sourceIdentity"]["identitySHA256"],
            definitionSHA256=saved["definitionSHA256"],
            gridShapes={k:[len(v.nodes),len(v.u)] for k,v in caches.items()},
            ownAcceptedSteps=0,actualSolveComputed=False)

if __name__=="__main__":main()
