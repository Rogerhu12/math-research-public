#!/usr/bin/env python3
"""Use a complete same-discretization tail packet only as a startup guess.

The accepted prefix/reference remains A. The seed may have another complete H;
the unchanged original predictor transfers it to the first live request. The
original raw-state validation, snapshot identity comparison, nonlinear solve,
full Jacobian, positivity and every final acceptance gate remain in force.
This does not mark the seed's prefix, its H, or any unaudited tail as accepted.
"""
from __future__ import annotations
import argparse
import ast
import gzip
import hashlib
import json
from pathlib import Path
import sys
import strong_full_tangent_actual_bvp_v2 as storage
import strong_20261114_loop_actual_bvp as entry

HERE=Path(__file__).resolve().parent
IO={'traceFile','iterationCheckpointFile','trialDiagnosticFile','initialCheckpoint'}

def read(p):
    p=Path(p); b=p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)

def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument('--startup-tail-seed',type=Path,required=True)
    own,remaining=parser.parse_known_args()
    if any(x in remaining for x in ('--tail-warm-checkpoint','--initial-audited-tail-packet','--initial-audited-tail-ready','--initial-full-tangent-manifest')):
        raise ValueError('Startup seed is a guess; exact-old-H or alternate manifest shortcuts must be absent')
    seed=own.startup_tail_seed.resolve(); packet=read(seed)
    reference=Path(remaining[remaining.index('--actual-reference-tail')+1])
    baseline=read(reference)
    old=baseline['response']['checkpoint']; new=packet['response']['checkpoint']
    if not packet['response'].get('converged') or not packet['response'].get('fullFlowTangentSnapshot'):
        raise ValueError('The startup packet needs its original converged complete flow tangent')
    if {k:v for k,v in old['parameters'].items() if k not in IO}!={k:v for k,v in new['parameters'].items() if k not in IO}:
        raise ValueError('Startup seed changed the physical or numerical tail problem')
    if old['rawNode']!=new['rawNode'] or len(old['states'])!=len(new['states']):
        raise ValueError('Startup seed is not on the identical complete shooting grid')
    # The unmodified exact-raw worker checks all raw copies and float values;
    # the unmodified full-flow loader binds all bytes and complete identities.
    seed_record=dict(file=str(seed),sha256=hashlib.sha256(seed.read_bytes()).hexdigest(),
        request_height=packet['request']['height'],seed_residual=packet['response']['residual'],
        seed_audit_present=packet['response'].get('audit') is not None,
        accepted_prefix_reference_unchanged=True,warm_only=True,
        original_snapshot_identity_and_full_new_H_solve_unchanged=True)
    prior=storage.resource_outer
    def outer(original):
        retained=prior(original)
        def installed(original_build,old_heap,semi_space):
            retained_build=retained(original_build,old_heap,semi_space)
            def build(merit,disk):
                source,record=retained_build(merit,disk)
                before='initialCheckpoint=str((options.tail_warm_checkpoint or options.actual_reference_tail).resolve()))'
                after='initialCheckpoint='+repr(str(seed))+')'
                if source.count(before)!=1:
                    raise ValueError('Original startup checkpoint assignment is not unique')
                changed=source.replace(before,after,1); ast.parse(changed)
                if changed.replace(after,before,1)!=source:
                    raise ValueError('Startup seed changed unrelated code')
                result=dict(record)
                result['source_sha256']={**record['source_sha256'],str(Path(__file__).resolve()):hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),str(seed):seed_record['sha256']}
                result['prior_transformed_source_sha256']=record['transformed_source_sha256']
                result['transformed_source_sha256']=hashlib.sha256(changed.encode()).hexdigest()
                result['replacements']=list(record['replacements'])+[dict(before=before,after=after,count=1)]
                result['complete_startup_tail_seed']=dict(scope=__doc__,**seed_record)
                return changed,result
            return build
        return installed
    storage.resource_outer=outer;old_argv=sys.argv;sys.argv=[old_argv[0],*remaining]
    try:entry.main()
    finally:storage.resource_outer=prior;sys.argv=old_argv

if __name__=='__main__':main()
