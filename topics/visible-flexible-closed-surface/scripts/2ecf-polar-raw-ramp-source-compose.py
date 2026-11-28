#!/usr/bin/env python3
"""Compose corrected 33/65 raw Cauchy-Hermite ramps with the actual original complete suffix."""
import argparse
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

for name in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[name]="1"
import numpy as np


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod


def sha(path):
    digest=hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda:f.read(1<<20),b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical(item):
    return hashlib.sha256(json.dumps(item,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()


def write(path,item):
    with Path(path).open("x") as f:
        json.dump(item,f,separators=(",",":"),allow_nan=False)
        f.write("\n")


def compose(args):
    start=time.monotonic()
    here=Path(__file__).resolve().parent
    parent_entry=here/"2ecf-polar-c2-g10-split-prepare.py"
    parent=load(parent_entry,"validated_legacy_complete")
    saved,definition,basis,_,mods,*_=parent.validate_prepared(argparse.Namespace(prepared=args.parent_prepared,scripts=args.scripts))
    independent=json.loads(args.parent_observer.read_text())
    if independent["sourceIdentity"]!=definition["sourceIdentity"] or independent["basis"]!=basis.definition:
        raise ValueError("G10/G11 original source mismatch")
    warm_path=args.scripts/"6a65-geometry-cauchy-unit-t-warm.py"
    sys.path.insert(0,str(args.scripts.resolve()))
    warm=load(warm_path,"ramp_substitution_warm")
    if sha(args.coast)!="f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d":
        raise ValueError("Original coast required")
    masters={33:"4fcc0542ddf34674672556a85608ac0ab56c8b34f3bd81451f6c7b75e99f0544",
             65:"479dab51bd77a211f64a256bbb16d67b4382e150af0deee7fa6baf84d8e5464a"}
    model=warm.WarmMaster(args.ramp,args.coast,coast_length=.02)
    count=len(model.sx)
    if sha(args.ramp)!=masters.get(count):
        raise ValueError("Actual parent-preserving physical h-master required")
    extractor=load(here/"2ecf-polar-source-prefix-spans.py","signed_prefix_statistics")
    keys=("X","Xs","Xu","Xss","Xsu","Xuu")
    ident=dict(schema="actual-physical-h-raw-ramp-with-existing-complete-suffix-v1",
        oldSource=definition["sourceIdentity"],centralAndCoastAndWholeRightSourceUnchanged=True,
        rampMasterSHA256=sha(args.ramp),coastMasterSHA256=sha(args.coast),nodes=count,
        mathematicalRamp="full native Hermite of retained physical IVP nodes in original ellipse material angle; same accurate Gamma95 terminal P,V,A",
        numericalRamp="WarmMaster.jet evaluated on original material angles in strict ramp interior",
        numericalEvaluatorSHA256=sha(warm_path),physicalTargetUnchanged=True,
        completeEndpointJetsCharged=True)
    identity=canonical(ident)
    allout={}
    config=copy.deepcopy(definition)
    config["sourceIdentity"]=dict(schema=ident["schema"],identitySHA256=identity,sourceDefinition=ident)
    records={}
    for key in ("training","observer","independent"):
        rec=copy.deepcopy(independent if key=="independent" else saved["caches"][key])
        nodes=np.asarray(rec["physicalNodes" if key=="independent" else "nodes"])
        u=np.asarray(rec["angles"])
        for k in ("jets","radius","report"):
            if sha(rec["files"][k])!=rec["SHA256"][k]:
                raise ValueError("Original complete source cache changed")
        old=np.load(rec["files"]["jets"],mmap_mode="r")
        radius=np.load(rec["files"]["radius"],mmap_mode="r")
        out=Path(str(args.prefix)+"-"+key+"-jets.npy").resolve()
        if out.exists(): raise FileExistsError(out)
        target=np.lib.format.open_memmap(out,mode="w+",dtype=old.dtype,shape=old.shape)
        target[:]=old
        active=np.flatnonzero((nodes>model.c)&(nodes<model.ramp_end))
        for i in active:
            value=model.jet(float(nodes[i]),u)
            target[i]=np.stack([value[k] for k in keys])
        complement=np.setdiff1d(np.arange(len(nodes)),active)
        if not np.array_equal(target[complement],old[complement]):
            raise ArithmeticError("Source outside new ramp changed")
        endpoint={}
        for s in (model.c,model.ramp_end):
            matches=np.where(nodes==s)[0]
            if len(matches):
                value=model.jet(float(s),u)
                endpoint[str(s)]=np.max(np.abs(old[matches[0]]-np.stack([value[k] for k in keys])),axis=(1,2)).tolist()
        im=np.flatnonzero((nodes>=model.c)&(nodes<=model.ramp_end))
        metrics={}
        for label,packet in (("old",old),("new",target)):
            met,kap=extractor.extrema(packet[im],radius[im,0,None])
            x,y=np.unravel_index(np.argmax(met),met.shape)
            metrics[label]=dict(metric=float(met[x,y]),curvature=float(kap.max()),s=float(nodes[im[x]]),u=float(u[y]))
        target.flush()
        del target
        original_record=rec["SHA256"].copy()
        rec["sourceDefinitionSHA256"]=identity
        rec["files"]["jets"]=str(out)
        rec["SHA256"]["jets"]=sha(out)
        report=Path(str(args.prefix)+"-"+key+"-source.json").resolve()
        result=dict(schema=ident["schema"],sourceIdentitySHA256=identity,oldHashes=original_record,
            composedJetsSHA256=rec["SHA256"]["jets"],unchangedTargetRadiusSHA256=rec["SHA256"]["radius"],
            replacedRadials=len(active),retainedRadials=len(complement),angles=len(u),endpointSixJetDiscrepancy=endpoint,
            originalAndNewActualRampExtrema=metrics,allUnchangedRowsByteEqual=True,
            everySourceAngleAndAllSixJetsPresent=True,finiteOnly=True)
        write(report,result)
        rec["files"]["report"]=str(report)
        rec["SHA256"]["report"]=sha(report)
        if key=="independent":
            rec={k:rec[k] for k in ("physicalNodes","angles","files","SHA256","basis")}
            rec.update(schema=ident["schema"]+"-independent",sourceIdentity=config["sourceIdentity"],sourceEntrySHA256=sha(__file__),
                originalIndependentSHA256=sha(args.parent_observer),observerUsedInTraining=False)
            write(str(args.prefix)+"-independent.json",rec)
        else:
            records[key]=rec
        allout[key]=result
        print(key, json.dumps(result["originalAndNewActualRampExtrema"]),flush=True)
    merged=dict(schema=ident["schema"]+"-prepared",definition=config,definitionSHA256=canonical(config),
        parentPrepared=str(args.parent_prepared.resolve()),parentPreparedSHA256=sha(args.parent_prepared),
        parentPrepareEntrySHA256=sha(parent_entry),prepareEntrySHA256=sha(__file__),
        caches=records,sourceMetadata=ident,groups=allout,seconds=time.monotonic()-start)
    write(str(args.prefix)+"-prepared.json",merged)


def validate_prepared(args):
    saved=json.loads(args.prepared.read_text())
    if saved["prepareEntrySHA256"]!=sha(__file__) or saved["definitionSHA256"]!=canonical(saved["definition"]):
        raise ValueError("Actual composed prepared input required")
    parent_path=Path(saved["parentPrepared"])
    parent_entry=Path(__file__).with_name("2ecf-polar-c2-g10-split-prepare.py")
    if sha(parent_path)!=saved["parentPreparedSHA256"] or sha(parent_entry)!=saved["parentPrepareEntrySHA256"]:
        raise ValueError("Original complete source changed")
    parent,original,basis,_,mods,*_=load(parent_entry,"actual_prior_strong_source").validate_prepared(
        argparse.Namespace(prepared=parent_path,scripts=args.scripts))
    caches={}
    for key,rec in saved["caches"].items():
        prior=parent["caches"][key]
        if any(rec[k]!=prior[k] for k in ("nodes","angles","weights")) or rec["SHA256"]["radius"]!=prior["SHA256"]["radius"]:
            raise ValueError("All original weights and the fixed target are required")
        if sha(rec["files"]["report"])!=rec["SHA256"]["report"]:raise ValueError("Source composition receipt changed")
        caches[key]=mods["generic"].Cached(rec)
    return saved,saved["definition"],basis,caches,mods,parent,original,basis


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    for name in ("scripts","ramp","coast","parent-prepared","parent-observer","prefix"):
        parser.add_argument("--"+name,required=True,type=Path)
    compose(parser.parse_args())
