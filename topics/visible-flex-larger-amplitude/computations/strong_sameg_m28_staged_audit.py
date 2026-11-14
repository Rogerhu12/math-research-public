#!/usr/bin/env python3
"""Complete the original M28 tail audit after a saved successful prefix solve.

The accepted raw result and its earlier affine-inner checkpoint must have
bitwise identical x/y/p/cubic/RMS. The original complete M28 tail response is
only a warm state; this run repeats the original full Jacobian and audit at
the exact new H. No prefix Newton solve, field, physical datum or MJS changes.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
for key in tuple(os.environ):
    if key in ('GH_TOKEN','GITHUB_TOKEN','GITHUB_PAT') or key.startswith('GIT_CONFIG_'):
        os.environ.pop(key,None)
import argparse
import gc
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time
import numpy as np
import root_actual_staged_tail as stage
import strong_sameg_spectral_refinement as spectral

HERE=Path(__file__).resolve().parent
SELF_SHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument('--accepted-raw',type=Path,required=True)
    parser.add_argument('--original-spectral-plan',type=Path,required=True)
    parser.add_argument('--node-young-space',type=int,choices=(1,2,4,8),default=4)
    own,remaining=parser.parse_known_args()
    def arg(name):
        if remaining.count(name)!=1:raise ValueError('Exactly one '+name+' is required')
        return Path(remaining[remaining.index(name)+1])
    pending_file=arg('--raw');cfg_file=arg('--config');warm_file=arg('--warm')
    out=arg('--out-prefix');source_topic=arg('--source-topic')
    if str(arg('--storage'))!='frozen':
        raise ValueError('Original frozen binary geometry storage is required')
    old_heap=int(str(arg('--node-heap')))
    if old_heap not in (96,128):
        raise ValueError('Explicit reviewed Node heap 96 or 128 MiB required')
    original_plan=stage.read_json(own.original_spectral_plan)
    for name,expected in original_plan['source_sha256'].items():
        path=HERE/name
        if not path.is_file() or stage.sha(path)!=expected:
            raise ValueError('Original spectral source differs: '+name)
    current_mjs={p.name:stage.sha(p) for p in sorted(HERE.glob('*.mjs'))}
    if current_mjs!=original_plan['MJS_source_sha256']:
        raise ValueError('Frozen MJS source tree differs from original spectral run')
    accepted,A=stage.raw_arrays(own.accepted_raw)
    pending,B=stage.raw_arrays(pending_file)
    identity=accepted['identity']
    if (not accepted['solver_success'] or accepted['status']!=0 or
            accepted['physical_surface'] is not False or
            identity['modes']!=28 or identity['angular']!=1024 or
            identity['tol']!=1e-7 or not identity['fixed']):
        raise ValueError('Accepted same-g M28/N1024/tol7 raw identity required')
    if (pending['solver_success'] or pending['status']!=0 or
            not pending['provenance'].get('affine_inner_success') or
            not pending['provenance'].get('actual_nonlinear_coupling_pending')):
        raise ValueError('Original successful pending affine-inner raw required')
    if spectral.canonical(identity)!=spectral.canonical(pending['identity']):
        raise ValueError('Pending and accepted complete physical/chart identities differ')
    for name in ('x','y','p','cubic','rms'):
        if A[name].shape!=B[name].shape or A[name].tobytes()!=B[name].tobytes():
            raise ValueError('Pending/accepted raw changed an array: '+name)
    if np.max(A['rms'])>identity['tol']:
        raise ValueError('Original saved RMS exceeds its unchanged tolerance')
    original=stage.read_json(cfg_file)
    if stage.sha(cfg_file)!=identity['coupling_context']['tail_config_sha256']:
        raise ValueError('Original configuration bytes changed')
    warm=stage.read_json(warm_file);response=warm['response'];request=warm['request']
    M=identity['modes'];height=-float(identity['gauge'])*A['y'][2*M+1:,-1]
    J=np.asarray(response.get('heightJetJacobian'),dtype=float)
    if (stage.equation_config(warm['config'])!=stage.equation_config(original) or
            not request.get('jacobian') or not response.get('converged') or
            response.get('failed') or float(response['residual'])>float(original['solveTolerance']) or
            not np.isfinite(J).all() or J.size!=(3*M+2)*M or
            np.asarray(request['height'],dtype=float).tobytes()!=height.tobytes() or
            np.asarray(response['checkpoint']['cutHeight'],dtype=float).tobytes()!=height.tobytes()):
        raise ValueError('Original complete M28 true-H response/Jacobian does not match accepted raw')
    for name,expected in warm['source_sha256'].items():
        local=HERE/name
        source=local if local.is_file() else source_topic/'scripts'/name
        if not source.is_file() or stage.sha(source)!=expected:
            raise ValueError('Original warm tail mathematical source differs: '+name)
    out.parent.mkdir(parents=True,exist_ok=True)
    record=dict(scope=__doc__,source_sha256=SELF_SHA,
        stage_source_sha256=stage.sha(Path(stage.__file__)),
        resource_wrapper_source_sha256=stage.sha(Path(spectral.__file__)),
        accepted_raw=dict(file=str(own.accepted_raw),sha256=stage.sha(own.accepted_raw)),
        pending_raw=dict(file=str(pending_file),sha256=stage.sha(pending_file)),
        original_spectral_plan=dict(file=str(own.original_spectral_plan),sha256=stage.sha(own.original_spectral_plan)),
        original_tail_response=dict(file=str(warm_file),sha256=stage.sha(warm_file),audit_was_requested=request.get('audit')),
        original_config_sha256=stage.sha(cfg_file),all_five_raw_arrays_bitwise_equal=True,
        original_RMS_max=float(np.max(A['rms'])),nodes=len(A['x']),modes=M,angular=identity['angular'],
        raw_solver_success=True,physical_surface_complete=False,
        complete_28_H_bitwise_equal=True,physical_height=height.tolist(),
        new_full_Jacobian_and_audit_required=True,prefix_Newton_calls=0,
        source_MJS_unchanged=True,node_old_heap_MiB=old_heap,
        node_young_semi_space_MiB=own.node_young_space,
        command_arguments=[v for v in remaining if v!='--prepare-only'],no_credentials_recorded=True)
    spectral.atomic_new_or_same(out.with_name(out.name+'-recovery-guards.json'),record)
    del A,B,accepted,pending,warm,response,J,height
    gc.collect()
    print(json.dumps(dict(event='same_g_M28_staged_audit_guards_passed',
        nodes=record['nodes'],all_five_raw_arrays_bitwise_equal=True,
        complete_28_H_bitwise_equal=True,prefix_Newton_calls=0)),flush=True)
    os.environ['VISIBLE_FLEX_SOURCE_TOPIC']=str(source_topic.resolve())
    import tail_frozen_client
    old=tail_frozen_client.WeightedTailPort
    tail_frozen_client.WeightedTailPort=spectral.resource_class(old,old_heap,own.node_young_space)
    oldargv=sys.argv
    started=time.monotonic()
    try:
        sys.argv=[oldargv[0],*remaining]
        stage.main()
    finally:
        tail_frozen_client.WeightedTailPort=old;sys.argv=oldargv
        terminal=dict(source_sha256=SELF_SHA,seconds=time.monotonic()-started,
            prepare_only='--prepare-only' in remaining,
            original_stage_summary=str(out.with_name(out.name+'-summary.json')),
            result_not_inferred_from_process_liveness=True)
        suffix='-recovery-prepare-terminal.json' if '--prepare-only' in remaining else '-recovery-terminal.json'
        spectral.atomic_new_or_same(out.with_name(out.name+suffix),terminal)

if __name__=='__main__':main()
