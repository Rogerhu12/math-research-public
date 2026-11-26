#!/usr/bin/env python3
"""Finite identity and normal-report check; no actual polar value or LM is run."""
from __future__ import annotations
import argparse,copy,hashlib,importlib.util,json,sys,time
from pathlib import Path
from types import SimpleNamespace
import numpy as np

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):
    spec=importlib.util.spec_from_file_location('actual_polar_entry_guard_fixture',p)
    m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m);return m

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--entry',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();start=time.monotonic();entry=load(args.entry)
    if args.output.exists():raise FileExistsError('Fresh fixture output required')
    basis=SimpleNamespace(nb=2,na=3,dimension=6,definition={'syntheticIdentityFixture':True,'shape':[2,3]})
    definition=dict(pointConfig={'fixture':True},sourceIdentity={'fixture':'new-polar'},correctionSupport=[.2,1.])
    model=dict(syntheticIdentityFixture=True,operatorSourceEpoch='a'*40,definition=definition)
    model_sha=entry.canonical(model);prepared_sha='b'*64;entry_sha=sha(args.entry)
    def call(state):
        return entry.starting_state(state,model,model_sha,basis,definition,prepared_sha,entry_sha)
    zero,own,attempts=call(None)
    if zero.shape!=(2,3) or np.any(zero) or (own,attempts)!=(0,0):raise AssertionError('New source zero initialization changed')
    state=dict(schema=entry.SCHEMA+'-checkpoint',preparedSHA256=prepared_sha,
        targetMetricFrozen=True,basis=basis.definition,pointConfig=definition['pointConfig'],
        sourceIdentity=definition['sourceIdentity'],correctionSupport=definition['correctionSupport'],
        newIndependentPolarSource=True,modelDefinitionSHA256=model_sha,modelDefinition=model,
        entrySHA256=entry_sha,polarFullBandAcceptedSteps=2,polarFullBandAttemptCount=3,
        actualTotalCartesianAcceptedSteps=2,borrowedOldSourceAcceptedSteps=0,
        z=[.001,-.002,.003,-.004,.005,-.006])
    got,own,attempts=call(state)
    if not np.array_equal(got.ravel(),np.asarray(state['z'])) or (own,attempts)!=(2,3):
        raise AssertionError('Nonzero own continuation lost bytes or counters')
    got[0,0]=42
    if state['z'][0]!=.001:raise AssertionError('Continuation aliases input state')
    mutations=[('old-model-schema','schema','6a65-gap105-complete14-q2-full-physical-normal-fixed-g-Cartesian-v1-checkpoint'),
        ('wrong-prepared','preparedSHA256','0'*64),('unfrozen-g','targetMetricFrozen',False),
        ('wrong-basis','basis',{'fixture':'changed'}),('wrong-point-config','pointConfig',{'fixture':False}),
        ('wrong-source','sourceIdentity',{'fixture':'old-gap'}),('wrong-support','correctionSupport',[.1,1.]),
        ('old-position-identity','newIndependentPolarSource',False),('changed-model-hash','modelDefinitionSHA256','0'*64),
        ('changed-model-bytes','modelDefinition',dict(model,operatorSourceEpoch='c'*40)),
        ('changed-entry','entrySHA256','d'*64),('wrong-own-count','polarFullBandAcceptedSteps',4),
        ('boolean-own-count','polarFullBandAcceptedSteps',True),('negative-attempts','polarFullBandAttemptCount',-1),
        ('wrong-total-count','actualTotalCartesianAcceptedSteps',3),('boolean-total-count','actualTotalCartesianAcceptedSteps',True),
        ('borrowed-old-acceptance','borrowedOldSourceAcceptedSteps',1),('boolean-borrowed-count','borrowedOldSourceAcceptedSteps',False),
        ('missing-column','z',state['z'][:-1]),('extra-column','z',state['z']+[0.]),
        ('nonfinite-column','z',[float('nan')]+state['z'][1:])]
    rejected=[]
    for label,key,value in mutations:
        q=copy.deepcopy(state);q[key]=value
        try:call(q)
        except (ValueError,TypeError,KeyError):rejected.append(label)
        else:raise AssertionError('Mutated independent-source guard accepted: '+label)
    entry.check_run_binding({'runIdentity':{'actualRunId':None}},None)
    entry.check_run_binding({'runIdentity':{'actualRunId':123}},'123')
    rejected_runs=[]
    for label,claimed,current in [('missing-live-run',123,None),('different-live-run',123,'124'),
            ('invalid-live-run',0,'0'),('string-run-id','123','123')]:
        try:entry.check_run_binding({'runIdentity':{'actualRunId':claimed}},current)
        except ValueError:rejected_runs.append(label)
        else:raise AssertionError('Changed actual run accepted: '+label)
    small=entry.physical_normal_statistics(np.asarray([6e-11,8e-11]),np.asarray([3e-9,4e-9]))
    if not np.isclose(small['originalPhysicalNormalAbsoluteResidual'],1e-10,rtol=1e-15,atol=0):raise AssertionError('Absolute residual changed')
    if not np.isclose(small['originalPhysicalInitialGradientNorm'],5e-9,rtol=1e-15,atol=0):raise AssertionError('Initial gradient changed')
    if not np.isclose(small['originalPhysicalNormalRelativeResidual'],.02,rtol=1e-15,atol=0):raise AssertionError('True relative denominator changed')
    if not np.isclose(small['originalPhysicalNormalMaxOneScaledResidual'],1e-10,rtol=1e-15,atol=0):raise AssertionError('Max-one statistic changed')
    zeros=entry.physical_normal_statistics(np.zeros(2),np.zeros(2))
    if zeros['originalPhysicalNormalRelativeResidual']!=0:raise AssertionError('Zero/zero diagnostic changed')
    try:entry.physical_normal_statistics(np.asarray([np.nan]),np.asarray([1.]))
    except ArithmeticError:pass
    else:raise AssertionError('Nonfinite physical normal accepted')
    report=dict(schema='6a65-independent-polar-q2-entry-identity-fixture-v1',
        entrySHA256=entry_sha,fixtureSHA256=sha(__file__),syntheticIdentityFixtureOnly=True,
        actualPolarBackgroundEvaluated=False,actual5292SolveComputed=False,actualNonlinearAcceptedSteps=0,
        zeroInitializationPassed=True,nonzeroOwnContinuationPreserved=True,
        rejectedStateCases=rejected,rejectedActualRunCases=rejected_runs,
        smallGradientPhysicalDiagnostics=small,zeroNormalCase=zeros,
        seconds=time.monotonic()-start,OSExitCode=None,externalExitRequired=True)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(args.output),SHA256=sha(args.output),stateGuards=len(rejected),
        runGuards=len(rejected_runs),seconds=report['seconds'],actualNonlinearAcceptedSteps=0)))

if __name__=='__main__':main()
