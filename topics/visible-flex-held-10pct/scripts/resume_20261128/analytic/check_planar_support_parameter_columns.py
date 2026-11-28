#!/usr/bin/env python3
"""Diagnose real lambda-zero support-column cancellation on seven saved nodes.

Use the complete original nodal source and stored original seven-node Jacobian
from the preceding actual delta diagnostic.  No full matrix, BVP or native
solve is repeated.  New exact support jets are compared to complete original
RHS differences at several explicitly recorded physical coefficient steps.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import gc
import hashlib
import json
from pathlib import Path
import resource
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import check_unaccepted_design_delta_nodes_v2 as original
import planar_support_exact_parameter_jets as jets


def checked(reference):
    path = Path(reference['path']).resolve()
    if original.sha(path) != reference['sha256']:
        raise ValueError('Changed real seven-node diagnostic source: '+str(path))
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--delta-comparison',type=Path,required=True)
    parser.add_argument('--outdir',type=Path,required=True)
    parser.add_argument('--physical-steps',type=float,nargs='+',default=[1e-7,3e-8,1e-8])
    args = parser.parse_args()
    if any(not np.isfinite(v) or v <= 0 for v in args.physical_steps):
        raise ValueError('Use positive finite physical support-coefficient steps')
    parent=json.loads(args.delta_comparison.read_text())
    if (parent.get('status') != 'real_unaccepted_complete_node_delta_comparison_returned'
            or parent.get('source_is_accepted_original') is not False
            or parent['original_parameter_J_branch']['live_V5_delta_install_called'] is not False
            or parent['evaluated_nodes'] != 7):
        raise ValueError('Require the real seven-node lambda-zero fallback diagnostic')
    for path,expected in parent['source_hashes'].items():
        if original.sha(path) != expected:
            raise ValueError('The completed original comparison source changed: '+path)
    record=json.loads(checked(parent['source_run_snapshot']).read_text())
    for group in (record['source_hashes'],record['inputs']):
        for path,expected in group.items():
            if original.sha(path) != expected:
                raise ValueError('An original model dependency changed: '+path)
    if record['core_settings']['homotopy'] != 0:
        raise ValueError('This diagnostic concerns the actual lambda-zero fallback only')
    with np.load(checked(parent['checkpoint']),allow_pickle=False) as raw:
        x,y,p,pscale=(raw[key].copy() for key in ('x','y','p','pscale'))
    with np.load(checked(parent['complete_selected_columns']),allow_pickle=False) as raw:
        indices,t,old_dy,old_dp=(raw[key].copy() for key in
                                 ('source_indices','t','original_dy','original_dp'))
    if not np.array_equal(t,x[indices]):
        raise ValueError('The selected material/computational nodes changed')
    yy=y[:,indices]
    out=args.outdir.resolve()
    repo=original.SCRIPTS.parents[2]
    if out == repo or repo in out.parents:
        raise ValueError('Keep scientific arrays outside the source tree')
    out.mkdir(parents=True,exist_ok=False)
    begin=time.monotonic()
    obj,table_stats,branch=original.build_original_model(record,repo)
    if branch['live_V5_delta_install_called'] or not np.array_equal(obj.pscale,pscale):
        raise ValueError('The true lambda-zero model/parameter coordinates changed')
    obj.initial(p)
    base=obj.fun(t,yy,p)
    import analytic_adaptive_core_jac as analytic
    installation=jets.install(type(obj),analytic)
    new_dy,new_dp=obj.fun_jac(t,yy,p)
    unchanged=dict(all_state_columns_bitwise=bool(np.array_equal(old_dy,new_dy)),
                   original_delta_column_bitwise=bool(np.array_equal(old_dp[:,0,:],new_dp[:,0,:])))
    if not all(unchanged.values()):
        raise ArithmeticError('A declared unchanged production Jacobian component differs: '+str(unchanged))
    rows,columns=[],[]
    for j in range(1,obj.M):
        column=new_dp[:,j,:]
        current=original.difference(column,old_dp[:,j,:])
        base_step=2e-5*max(1.,abs(p[j]))
        row=dict(parameter_index=j,support_frequency=3*(j+1),
            parameter_scale=float(pscale[j-1]),original_parameter_step=float(base_step),
            original_physical_coefficient_step=float(base_step*pscale[j-1]),
            analytic_l2=float(np.linalg.norm(column)),original_FD_vs_analytic=current,
            physical_step_comparisons=[])
        parameter_columns=[]
        for physical_step in args.physical_steps:
            step=physical_step/pscale[j-1]
            plus,minus=p.copy(),p.copy()
            plus[j]+=step
            minus[j]-=step
            fd=(obj.fun(t,yy,plus)-obj.fun(t,yy,minus))/(2*step)
            comparison=dict(requested_physical_step=physical_step,parameter_step=float(step),
                actual_plus_parameter_step=float(plus[j]-p[j]),
                actual_minus_parameter_step=float(p[j]-minus[j]),**original.difference(column,fd))
            row['physical_step_comparisons'].append(comparison)
            parameter_columns.append(fd)
            gc.collect()
        rows.append(row)
        columns.append(parameter_columns)
        print(json.dumps(dict(event='real_full_support_column',**row)),flush=True)
    restored=obj.fun(t,yy,p)
    unchanged['base_RHS_after_full_parameter_differences_bitwise']=bool(np.array_equal(base,restored))
    if not all(unchanged.values()):
        raise ArithmeticError('The complete original base RHS failed to restore')
    np.savez_compressed(out/'complete-selected-support-columns.npz',indices=indices,t=t,
        analytic_dy=new_dy,analytic_dp=new_dp,original_dy=old_dy,original_dp=old_dp,
        physical_steps=np.asarray(args.physical_steps),full_RHS_differences=np.asarray(columns))
    result=dict(status='actual_original_planar_support_column_comparison_returned',
        scope=__doc__,source=original.ref(__file__),parent_delta_comparison=original.ref(args.delta_comparison),
        checkpoint=parent['checkpoint'],checkpoint_ordinal=parent['checkpoint_ordinal'],
        original_source_run=parent['source_run_observed'],source_is_accepted=False,
        actual_nodes=len(x),evaluated_nodes=len(t),state_components=obj.n,modes=obj.M,
        complete_original_parameter_columns_checked=list(range(1,obj.M)),
        original_branch=branch,independent_installation=installation,comparisons=rows,
        unchanged_component_checks=unchanged,complete_columns=original.ref(out/'complete-selected-support-columns.npz'),
        original_model_builder=original.ref(Path(original.__file__)),analytic_parameter_jets_source=original.ref(Path(jets.__file__)),
        production_core_source=original.ref(Path(sys.modules['fixed_metric_mode3_core'].__file__)),
        full_chart_lift_projection_convection_retained=True,
        actual_live_solver_modified=False,large_collocation_J_assembled=False,
        BVP_or_native_solve_invoked=False,interval_derivative_certificate=False,
        numerical_solver_convergence_proved=False,
        elapsed_seconds=time.monotonic()-begin,maximum_rss_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    (out/'comparison.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(status=result['status'],report=original.ref(out/'comparison.json'),
        elapsed_seconds=result['elapsed_seconds'],maximum_rss_KiB=result['maximum_rss_KiB'],
        unchanged_component_checks=unchanged)),flush=True)


if __name__=='__main__':
    main()
