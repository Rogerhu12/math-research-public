#!/usr/bin/env python3
"""Compare V5's complete delta column at a real, unaccepted nodal checkpoint.

This is explicitly a diagnostic of a saved current equation state. It does
not pass accepted_original, alter a run label, invoke a BVP/native solve or
assemble a complete collocation matrix. Every state/support column at the
selected actual nodes is retained in the original-vs-V5 comparison.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
import gc
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
sys.path[:0] = [str(HERE),str(SCRIPTS/'resume_20261126')]
from material_lambda_tangent_predictor import build_model
from material_delta_column import OriginalDeltaColumn


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path),sha256=sha(path))


def module(name,path):
    spec = importlib.util.spec_from_file_location(name,path)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[name] = obj
    spec.loader.exec_module(obj)
    return obj


def difference(first,second):
    delta = np.abs(first-second)
    location = np.unravel_index(np.argmax(delta),delta.shape)
    return dict(maximum_absolute=float(np.max(delta)),
        relative_l2=float(np.linalg.norm(first-second)/max(np.linalg.norm(second),np.finfo(float).tiny)),
        maximum_location=list(map(int,location)),second_l2=float(np.linalg.norm(second)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('source-run','checkpoint-metadata','outdir'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--node-count',type=int,default=7)
    parser.add_argument('--steps',type=float,nargs='+',default=[1e-6,2e-7,5e-8])
    args = parser.parse_args()
    if not 1 <= args.node_count <= 9 or any(not np.isfinite(h) or h <= 0 for h in args.steps):
        raise ValueError('Use one to nine actual nodes and positive finite difference steps')
    out = args.outdir.resolve()
    repo = SCRIPTS.parents[2]
    if out == repo or repo in out.parents:
        raise ValueError('Keep scientific diagnostic arrays outside the source tree')
    run_bytes = args.source_run.read_bytes()
    meta_bytes = args.checkpoint_metadata.read_bytes()
    record,metadata = json.loads(run_bytes),json.loads(meta_bytes)
    checkpoint = (args.checkpoint_metadata.parent/metadata['file']).resolve()
    if (metadata.get('kind') != 'unaccepted_complete_nodal_restart'
            or metadata.get('accepted_bvp') is not False
            or metadata.get('before_full_J_assembly') is not True
            or sha(checkpoint) != metadata['sha256']):
        raise ValueError('Require a genuine complete unaccepted nodal checkpoint with matching SHA')
    for group in (record['source_hashes'],record['inputs'],metadata['original_source_hashes']):
        for path,expected in group.items():
            if sha(path) != expected:
                raise ValueError('A real checkpoint source/input changed: '+path)
    with np.load(checkpoint,allow_pickle=False) as saved:
        x,y,p,pscale = (saved[key].copy() for key in ('x','y','p','pscale'))
    M = record['modes']
    if (x.shape != (metadata['nodes'],) or y.shape != (3*M+1,len(x))
            or p.shape != (M,) or pscale.shape != (M-1,)
            or not all(np.all(np.isfinite(a)) for a in (x,y,p,pscale))
            or not np.all(np.diff(x)>0) or x[0] != 0 or x[-1] != 1
            or not np.array_equal(pscale,np.asarray(record['parameter_scales']))):
        raise ValueError('The complete original mesh/state/parameter coordinates differ')
    out.mkdir(parents=True,exist_ok=False)
    (out/'source-run-snapshot.json').write_bytes(run_bytes)
    (out/'checkpoint-metadata-snapshot.json').write_bytes(meta_bytes)
    started = time.monotonic()
    obj,_,table_stats = build_model(record,repo)
    if not np.array_equal(obj.pscale,pscale):
        raise ValueError('The fresh original model changed the checkpoint parameter scales')
    indices = np.unique(np.rint(np.linspace(0,len(x)-1,args.node_count)).astype(int))
    t,yy = x[indices],y[:,indices]
    obj.initial(p)
    memo_path = HERE.parent/'design/material_core_evaluate_cache.py'
    memo = module('_unaccepted_delta_core_memo',memo_path)
    memo_stats = memo.install(type(obj._core),max_entries=4)
    base = obj.fun(t,yy,p)
    original_dy,original_dp = obj.fun_jac(t,yy,p)
    analytical = OriginalDeltaColumn(obj,p).rhs(t,yy)
    adapter_path = HERE.parent/'design/analytic_delta_jac_adapter.py'
    adapter = module('_unaccepted_delta_actual_v5_adapter',adapter_path)
    adapter_stats = adapter.install(type(obj))
    new_dy,new_dp = obj.fun_jac(t,yy,p)
    v5_RHS = obj.fun(t,yy,p)
    comparisons,columns = [],[]
    for step in args.steps:
        plus,minus = p.copy(),p.copy()
        plus[0] += step
        minus[0] -= step
        fd = (obj.fun(t,yy,plus)-obj.fun(t,yy,minus))/(2*step)
        row = dict(step=step,**difference(analytical,fd))
        row['source_node_at_maximum'] = int(indices[row['maximum_location'][1]])
        comparisons.append(row)
        columns.append(fd)
        print(json.dumps(dict(event='real_unaccepted_delta_FD',**row)),flush=True)
        gc.collect()
    restored = obj.fun(t,yy,p)
    invariants = dict(original_state_columns_bitwise_equal=bool(np.array_equal(original_dy,new_dy)),
        original_all_support_columns_bitwise_equal=bool(np.array_equal(original_dp[:,1:,:],new_dp[:,1:,:])),
        V5_delta_column_equals_declared_analytic_bitwise=bool(np.array_equal(new_dp[:,0,:],analytical)),
        original_RHS_after_V5_install_bitwise_equal=bool(np.array_equal(base,v5_RHS)),
        original_base_RHS_restored_bitwise=bool(np.array_equal(base,restored)))
    if not all(invariants.values()):
        raise ArithmeticError('A declared unchanged full-node RHS/Jacobian component changed: '+str(invariants))
    np.savez_compressed(out/'selected-complete-columns.npz',source_indices=indices,t=t,
        analytic=analytical,finite_differences=np.asarray(columns),steps=np.asarray(args.steps),
        original_dy=original_dy,original_dp=original_dp,V5_dy=new_dy,V5_dp=new_dp)
    report = dict(status='real_unaccepted_complete_node_delta_comparison_returned',
        scope=__doc__,source=ref(__file__),source_run_observed=dict(path=str(args.source_run.resolve()),
            sha256=hashlib.sha256(run_bytes).hexdigest()),
        source_run_snapshot=ref(out/'source-run-snapshot.json'),
        checkpoint_metadata_observed=dict(path=str(args.checkpoint_metadata.resolve()),
            sha256=hashlib.sha256(meta_bytes).hexdigest()),
        checkpoint_metadata_snapshot=ref(out/'checkpoint-metadata-snapshot.json'),
        checkpoint=ref(checkpoint),checkpoint_ordinal=metadata['checkpoint_ordinal'],
        source_role='genuine_unaccepted_before-full-J_complete_nodal_snapshot',
        source_is_accepted_original=False,nodes=len(x),evaluated_nodes=len(t),
        selected_actual_node_indices=indices.tolist(),state_components=obj.n,modes=M,angular=obj.nt,
        original_core_settings=record['core_settings'],original_profile=record['physical_profile'],
        original_gauge_q=record['gauge_q'],original_warp_reference=record['warp_reference'],
        original_gates=record['gates'],physical_delta=float(obj.cfg['delta']+p[0]),
        original_centered_delta_vs_analytic=difference(analytical,original_dp[:,0,:]),
        finite_differences=comparisons,unchanged_component_checks=invariants,
        complete_selected_columns=ref(out/'selected-complete-columns.npz'),
        fourier_assembly_cache=table_stats,core_evaluate_memo=memo_stats,V5_adapter=adapter_stats,
        source_hashes={str(path.resolve()):sha(path) for path in
            (Path(__file__),HERE/'material_delta_column.py',HERE/'material_lambda_tangent_predictor.py',
             memo_path,adapter_path)},
        elapsed_seconds=time.monotonic()-started,
        maximum_rss_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        current_live_source_or_equations_changed=False,large_collocation_J_assembled=False,
        BVP_or_native_solve_invoked=False,interval_derivative_certificate=False,
        nonlinear_convergence_proved=False)
    (out/'comparison.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(status=report['status'],report=ref(out/'comparison.json'),
        elapsed_seconds=report['elapsed_seconds'],maximum_rss_KiB=report['maximum_rss_KiB'],
        unchanged_component_checks=invariants)),flush=True)


if __name__ == '__main__':
    main()
