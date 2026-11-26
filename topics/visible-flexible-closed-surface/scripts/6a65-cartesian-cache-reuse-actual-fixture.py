#!/usr/bin/env python3
"""Actual local source-cache creation/reuse and strict boundary fixture.

The source is a separately computed true Cauchy INITIAL, not an Actions raw
state and not an interface probe. Only 4x4 and 3x8 samples are requested.
This fixture does not evaluate a complete value, normal, trial or acceptance.
"""
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import time
import numpy as np

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module);return module
def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources",type=Path,required=True)
    parser.add_argument("--scripts",type=Path,required=True)
    parser.add_argument("--candidate",type=Path,required=True)
    parser.add_argument("--source",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args();start=time.monotonic()
    out=args.output.resolve()
    if out.exists():raise FileExistsError("A new actual fixture directory is required")
    out.mkdir(parents=True)
    oracle=load("actual_cache_fixture_oracle",args.sources/"6a65-cartesian-oracle-background.py")
    reuse=load("actual_cache_fixture_reuse",args.sources/"6a65-cartesian-fixed-source-cache-reuse.py")
    source_hash=sha(args.source);candidate_hash=sha(args.candidate)
    keyword=dict(wrapper=args.scripts/"6a65-geometry-cauchy-source-radial-cuts.cjs",heap_mb=128)
    pool_path=out/"shared-source-cache"
    numerical=dict(schema="6a65-local-small-grid-cache-fixture-only-v1",
        purpose="actual original source samples; no full Cartesian experiment",
        sourceFieldProjection=False)
    with oracle.OracleBackground(args.scripts,args.candidate,args.source,**keyword) as first:
        if first.metadata["interfaceProbeOnly"] is not False:raise ValueError("An actual nonprobe source is required")
        identity=dict(schema="6a65-explicit-local-cache-interface-identity-v1",
            sourceStateSHA256=source_hash,candidateSHA256=candidate_hash,
            parameterVectorSHA256=first.expected_hashes["parameterVectorSHA256"],
            localFixtureName="actual-local-Cauchy-fixed-cache",
            sourceEpochKind="explicit local source; not a GitHub run",
            physicalMetricDefinition=first.metadata["radialMetricDefinition"])
        train_s=np.array([0.,first.c,(first.c+first.S)/2,first.cuff])
        train_u=2*np.pi*np.arange(4)/4
        observe_s=np.array([first.c,first.S,first.cuff])
        observe_u=2*np.pi*np.arange(8)/8
        pool1=reuse.FixedSourceCachePool(pool_path,first,identity,allowed_directory=out,
            numerical_identity=numerical,local_interface_fixture=True)
        training=pool1.cache("training",train_s,train_u,batch_size=2)
        observing=pool1.cache("observing",observe_s,observe_u,batch_size=2)
        first_training=np.array(training["jets"]);first_observing=np.array(observing["jets"])
        first_radius=np.array(training["radius"])
        first_training_binding=training["receipt"]["jetsSHA256"]
        readonly_rejected=False
        try:training["jets"][0,0,0,0]=0
        except ValueError:readonly_rejected=True
        if not readonly_rejected:raise AssertionError("Read-only cache write was not rejected")
    first_receipt=pool1.seal_after_natural_exit(first.exit_receipt)
    rejected=[]
    def must_reject(label,fn):
        try:fn()
        except (ValueError,ArithmeticError,FileNotFoundError):rejected.append(label);return
        raise AssertionError("Required rejection did not occur: "+label)
    with oracle.OracleBackground(args.scripts,args.candidate,args.source,**keyword) as second:
        def no_new_sample(*a,**kw):
            raise AssertionError("Second process attempted to resample an immutable source")
        second.cache=no_new_sample
        pool2=reuse.FixedSourceCachePool(pool_path,second,identity,allowed_directory=out,
            numerical_identity=numerical,local_interface_fixture=True)
        t2=pool2.cache("training",train_s,train_u,batch_size=2)
        o2=pool2.cache("observing",observe_s,observe_u,batch_size=2)
        if not (np.array_equal(first_training,t2["jets"]) and
                np.array_equal(first_observing,o2["jets"]) and
                np.array_equal(first_radius,t2["radius"])):
            raise AssertionError("Reused actual source arrays changed")
        def constructor(path=pool_path,ident=identity,numeric=numerical,local=True):
            return reuse.FixedSourceCachePool(path,second,ident,allowed_directory=out,
                numerical_identity=numeric,local_interface_fixture=local)
        must_reject("local fixture cannot claim production identity",lambda:constructor(local=False))
        for key,value in (("runId","different-local-session"),("sourceEpoch","different-explicit-source-epoch"),
                          ("physicalMetricDefinition",{"changed":True})):
            changed=copy.deepcopy(identity);changed[key]=value
            must_reject("changed "+key,lambda changed=changed:constructor(ident=changed))
        changed_numerical=copy.deepcopy(numerical);changed_numerical["changedRecipe"]=True
        must_reject("changed complete numerical identity",lambda:constructor(numeric=changed_numerical))
        changed_s=train_s.copy();changed_s[1]+=.00001
        must_reject("changed physical sample grid",lambda:pool2.cache("training",changed_s,train_u))
        changed_u=train_u.copy();changed_u[1]+=.00001
        must_reject("changed material sample grid",lambda:pool2.cache("training",train_s,changed_u))
        for label,filename in (("changed source array bytes","training-jets.npy"),
                               ("changed original cache receipt bytes","training-cache.json"),
                               ("missing natural-exit seal","sealed-original-oracle-exit.json")):
            copied=out/("negative-"+str(len(rejected)));shutil.copytree(pool_path,copied)
            target=copied/filename
            if label=="missing natural-exit seal":target.unlink()
            elif target.suffix==".json":target.write_bytes(target.read_bytes()+b" ")
            else:
                with target.open("r+b") as f:
                    f.seek(-1,2);old=f.read(1);f.seek(-1,2);f.write(bytes([old[0]^1]))
            must_reject(label,lambda copied=copied:constructor(copied).cache("training",train_s,train_u))
        seal=pool_path/"sealed-original-oracle-exit.json";oldseal=seal.read_bytes()
        seal.write_bytes(oldseal+b" ")
        must_reject("changed producer seal bytes",pool2.verify_unchanged)
        seal.write_bytes(oldseal)
        invalid=out/"wrong-shape";invalid.mkdir()
        np.save(invalid/"jets.npy",np.zeros((4,6,5,3),dtype="<f8"))
        np.save(invalid/"radius.npy",np.ones((4,3),dtype="<f8"))
        must_reject("changed actual array shape",lambda:reuse.FixedSourceCachePool._arrays(
            dict(jets=invalid/"jets.npy",radius=invalid/"radius.npy"),train_s,train_u))
        np.save(invalid/"jets.npy",np.zeros((4,6,4,3),dtype="<f4"))
        must_reject("changed actual array dtype",lambda:reuse.FixedSourceCachePool._arrays(
            dict(jets=invalid/"jets.npy",radius=invalid/"radius.npy"),train_s,train_u))
    second_receipt=pool2.seal_after_natural_exit(second.exit_receipt)
    if first.exit_receipt["actualOSExitCode"]!=0 or second.exit_receipt["actualOSExitCode"]!=0:
        raise AssertionError("Actual original child must exit naturally with zero")
    if second.exit_receipt["requests"]!=1:raise AssertionError("Reuse must request only live source metadata")
    if sha(args.source)!=source_hash or sha(args.candidate)!=candidate_hash:raise AssertionError("Fixture changed its inputs")
    report=dict(schema="6a65-actual-local-fixed-source-cache-reuse-fixture-v1",
        fixtureSHA256=sha(__file__),reuseImplementationSHA256=sha(args.sources/"6a65-cartesian-fixed-source-cache-reuse.py"),
        originalAdapterSHA256=sha(args.sources/"6a65-cartesian-oracle-background.py"),
        actualSourceSHA256=source_hash,candidateSHA256=candidate_hash,
        sourceIdentityKind="separately evaluated actual local Cauchy INITIAL; not Actions and not probe",
        trainingShape=list(first_training.shape),observationShape=list(first_observing.shape),
        firstTrainingSHA256=first_training_binding,reusedArraysExactlyEqual=True,
        arraysReadOnlyAndWriteRejected=readonly_rejected,actualRejectedCases=rejected,
        firstActualOriginalChildExit=first.exit_receipt,secondActualOriginalChildExit=second.exit_receipt,
        firstCacheReceipt=first_receipt,secondCacheReceipt=second_receipt,
        secondChildOnlyMetadataRequested=True,fullCartesianValueOrAcceptanceComputed=False,
        actualCartesianAcceptedSteps=0,rawPublished=False,continuousCertificate=False,
        seconds=time.monotonic()-start)
    target=out/"report.json";target.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    print(json.dumps({"report":str(target),"reportSHA256":sha(target),"seconds":report["seconds"],
        "rejectionCount":len(rejected),"firstChildExit":first.exit_receipt["actualOSExitCode"],
        "secondChildExit":second.exit_receipt["actualOSExitCode"]}),flush=True)
if __name__=="__main__":main()

