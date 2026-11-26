#!/usr/bin/env python3
"""Actual small checks of v3's identity gate and nonzero own-state handoff.

The identity documents here are explicitly synthetic fixtures. No live
Cauchy oracle, mathematical state, optimization acceptance, or certificate
is claimed. Production run() separately binds the actual oracle and bytes.
"""
import argparse
import copy
from dataclasses import asdict
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("cartesian_resume_v3_fixture_entry",HERE/"6a65-cartesian-independent-experiment-v3.py")
entry=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=entry
spec.loader.exec_module(entry)
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():raise FileExistsError("Fresh fixture receipt required")
    started=time.monotonic()
    basis=entry.stream.HalfTurnBasis(.1,1.1,4,4)
    values=(np.arange(basis.dimension,dtype=float)+1)*1e-5
    identity={"schema":"explicit-synthetic-interface-fixture-not-actual-source","payload":"not a production oracle"}
    cfg=asdict(entry.stream.point.PointConfig(.05,1e6,9.5,.51,1.436024268143396))
    operators={name:sha(HERE/file) for name,file in [
        ("streamSHA256","6a65-cartesian-complete-stream.py"),
        ("pointOperatorSHA256","6a65-cartesian-complete-point-operator.py"),
        ("oracleAdapterSHA256","6a65-cartesian-oracle-background.py")]}
    expected=dict(sourceStateSHA256="1"*64,candidateSHA256="2"*64,originalObserverSHA256="3"*64,
        sourceEpoch="4"*40,runId=123,sourceIdentity=identity,originalCauchyAcceptedSteps=7,
        gridSHA256="5"*64,pointConfig=cfg,recipeSHA256="6"*64,operatorSources=operators,
        allowedParentEntrySHA256=[sha(HERE/"6a65-cartesian-independent-experiment-v3.py"),
                                 sha(HERE/"6a65-cartesian-independent-experiment-v2.py")])
    state=dict(schema="6a65-complete-Cartesian-fixed-g-checkpoint-v1",
        cartesianAcceptedSteps=2,completeAttemptCount=3,
        source=dict(inputSHA256=expected["sourceStateSHA256"],candidateSHA256=expected["candidateSHA256"],
            observerSHA256=expected["originalObserverSHA256"],sourceEpoch=expected["sourceEpoch"],
            runId=123,sourceIdentity=identity),
        originalCauchyAcceptedSteps=7,basis=basis.definition,dimension=basis.dimension,
        gridSHA256=expected["gridSHA256"],pointConfig=cfg,recipeSHA256=expected["recipeSHA256"],
        targetMetricFrozen=True,allSixEndpointJetsFixed=True,allThirteenPointRowsRetained=True,
        model="complete-proper-half-turn-Cartesian-fixed-g",entrySHA256=expected["allowedParentEntrySHA256"][0],
        cartesianOperatorSources=operators,z=values.tolist())
    state_hash="7"*64
    observed=dict(schema="6a65-complete-Cartesian-fixed-g-same-field-observer-v1",
        inputs=dict(cartesianStateSHA256=state_hash,candidateSHA256=expected["candidateSHA256"],
            originalCauchyStateSHA256=expected["sourceStateSHA256"],originalObserverSHA256=expected["originalObserverSHA256"]),
        fixedSourceIdentity=identity,fieldCoefficientsUnchanged=True,physicalMetricUnchanged=True,
        sourceAngularPrimitiveUnchanged=True)
    coeff,count,attempts=entry.prepare_cartesian_resume(state,observed,state_hash,expected,basis)
    preserved=np.array_equal(coeff.ravel(),values) and count==2 and attempts==3 and np.all(coeff!=0)
    mutations=[
        ("original_state_bytes",("source","inputSHA256"),"0"*64),
        ("actual_run",("source","runId"),124),
        ("source_epoch",("source","sourceEpoch"),"0"*40),
        ("fixed_g_identity",("source","sourceIdentity"),{"wrong":True}),
        ("quadrature",("gridSHA256",),"0"*64),
        ("recipe",("recipeSHA256",),"0"*64),
        ("full_dimension",("dimension",),basis.dimension-1),
        ("original_count",("originalCauchyAcceptedSteps",),8),
        ("twojet_receipt",("allSixEndpointJetsFixed",),False),
        ("complete_rows",("allThirteenPointRowsRetained",),False),
        ("operator_sources",("cartesianOperatorSources","streamSHA256"),"0"*64),
        ("accepted_attempt_counts",("completeAttemptCount",),1),
        ("truncated_vector",("z",),values[:-1].tolist()),
        ("nonfinite_vector",("z",),[float("nan")]+values[1:].tolist())]
    rejected=[]
    for label,keys,value in mutations:
        bad=copy.deepcopy(state);target=bad
        for k in keys[:-1]:target=target[k]
        target[keys[-1]]=value
        try:entry.prepare_cartesian_resume(bad,observed,state_hash,expected,basis)
        except ValueError:rejected.append(label)
        else:raise AssertionError("Identity mismatch accepted: "+label)
    for label,change in [
        ("observer_state_bytes",lambda x:x["inputs"].update(cartesianStateSHA256="0"*64)),
        ("observer_original_bytes",lambda x:x["inputs"].update(originalCauchyStateSHA256="0"*64)),
        ("observer_primitive_receipt",lambda x:x.update(sourceAngularPrimitiveUnchanged=False))]:
        bad=copy.deepcopy(observed);change(bad)
        try:entry.prepare_cartesian_resume(state,bad,state_hash,expected,basis)
        except ValueError:rejected.append(label)
        else:raise AssertionError("Observer mismatch accepted: "+label)
    legacy=copy.deepcopy(state)
    legacy["entrySHA256"]=expected["allowedParentEntrySHA256"][1]
    del legacy["cartesianOperatorSources"]
    legacy_coeff,legacy_count,legacy_attempts=entry.prepare_cartesian_resume(legacy,observed,state_hash,expected,basis)
    legacy_preserved=np.array_equal(legacy_coeff,coeff) and (legacy_count,legacy_attempts)==(2,3)
    report=dict(schema="6a65-v3-Cartesian-resume-identity-finite-fixture-v1",
        fixtureSHA256=sha(__file__),entrySHA256=sha(HERE/"6a65-cartesian-independent-experiment-v3.py"),
        columns=basis.dimension,completeNonzeroVectorPreserved=bool(preserved),
        inheritedOwnAcceptedSteps=count,inheritedOwnAttemptCount=attempts,
        frozenV2ParentCompatibilityPreserved=bool(legacy_preserved),
        exactIdentityRejections=rejected,rejectionCount=len(rejected),
        actualCauchySourceConsumed=False,completeLMAcceptances=0,syntheticIdentityFixtureOnly=True,
        productionLiveOracleBindingStillRequired=True,continuousCertificate=False,
        verified=bool(preserved and legacy_preserved and len(rejected)==17),seconds=time.monotonic()-started)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    print(json.dumps(report,allow_nan=False),flush=True)
    if not report["verified"]:raise AssertionError("Actual finite resume check failed")

if __name__=="__main__":main()
