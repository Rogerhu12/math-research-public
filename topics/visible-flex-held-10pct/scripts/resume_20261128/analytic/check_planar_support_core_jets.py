#!/usr/bin/env python3
"""Resolve the remaining large-jet and small-RHS signals on one real snapshot.

Read the completed support-column diagnostic; do not rebuild a Jacobian.
Compare all original core coefficient three-jets at the actual angular grid,
then only the first two nearly cancelling RHS columns at larger physical
coefficient steps. No live solver, original source or numerical gate changes.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import json
from pathlib import Path
import resource
import sys
import time
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import check_unaccepted_design_delta_nodes_v2 as original
import check_planar_support_parameter_columns as prior
import planar_support_exact_parameter_jets as jets


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--support-comparison',type=Path,required=True)
    parser.add_argument('--outdir',type=Path,required=True)
    args=parser.parse_args()
    support=json.loads(args.support_comparison.read_text())
    if (support['status']!='actual_original_planar_support_column_comparison_returned'
            or support['source_is_accepted'] is not False
            or support['evaluated_nodes']!=7):
        raise ValueError('Use the genuine completed same-snapshot support diagnostic')
    for key in ('original_model_builder','analytic_parameter_jets_source','production_core_source'):
        prior.checked(support[key])
    delta=json.loads(prior.checked(support['parent_delta_comparison']).read_text())
    record=json.loads(prior.checked(delta['source_run_snapshot']).read_text())
    with np.load(prior.checked(support['checkpoint']),allow_pickle=False) as data:
        x,y,p,pscale=(data[k].copy() for k in ('x','y','p','pscale'))
    with np.load(prior.checked(support['complete_columns']),allow_pickle=False) as data:
        indices,t,analytic_dp=(data[k].copy() for k in ('indices','t','analytic_dp'))
    if not np.array_equal(x[indices],t):
        raise ValueError('The actual node coordinates changed')
    out=args.outdir.resolve()
    repo=original.SCRIPTS.parents[2]
    if out==repo or repo in out.parents:
        raise ValueError('Use an independent outside-repository diagnostic output')
    out.mkdir(parents=True,exist_ok=False)
    start=time.monotonic()
    obj,_,branch=original.build_original_model(record,repo)
    if branch['live_V5_delta_install_called']:
        raise ValueError('Require the real lambda-zero core and fallback')
    obj.initial(p)
    core=obj._core
    theta=obj.flow(p[0]).angular(obj.nt)[1]
    exact=jets.parameter_jets(core,theta)
    saved=core.evaluate(theta)
    coefficients=core.coefficients.copy()
    core_rows=[]
    for j in range(len(coefficients)):
        for step in (1e-6,3e-7,1e-7):
            plus,minus=coefficients.copy(),coefficients.copy()
            plus[j]+=step
            minus[j]-=step
            def make(c):
                return type(core)(float(c[0]),c[1:],base_mode=core.base_mode,arc_nodes=core.arc_nodes)
            P,Q=make(plus).evaluate(theta),make(minus).evaluate(theta)
            for order,name in enumerate(('F','Ft','Ftt')):
                fd=(P[name]-Q[name])/(2*step)
                core_rows.append(dict(coefficient_index=j,frequency=int(core.frequencies[j]),
                    physical_step=step,derivative_order=order,
                    analytic_l2=float(np.linalg.norm(exact[order][j])),
                    **original.difference(exact[order][j],fd)))
    restored=core.evaluate(theta)
    core_restored=all(np.array_equal(saved[key],restored[key]) for key in ('F','Ft','Ftt','phi'))
    yy=y[:,indices]
    base=obj.fun(t,yy,p)
    low=[]
    for j in (1,2):
        for physical_step in (1e-4,3e-5,1e-5):
            step=physical_step/pscale[j-1]
            plus,minus=p.copy(),p.copy()
            plus[j]+=step
            minus[j]-=step
            fd=(obj.fun(t,yy,plus)-obj.fun(t,yy,minus))/(2*step)
            low.append(dict(parameter_index=j,frequency=3*(j+1),physical_step=physical_step,
                parameter_step=float(step),analytic_l2=float(np.linalg.norm(analytic_dp[:,j,:])),
                **original.difference(analytic_dp[:,j,:],fd)))
    rhs_restored=np.array_equal(base,obj.fun(t,yy,p))
    if not core_restored or not rhs_restored:
        raise ArithmeticError('An original core/RHS base failed to restore exactly')
    result=dict(status='actual_planar_core_three_jets_and_low_RHS_columns_returned',
        source=original.ref(__file__),parent_support_comparison=original.ref(args.support_comparison),
        checkpoint=support['checkpoint'],checkpoint_ordinal=support['checkpoint_ordinal'],
        analytic_parameter_jets_source=original.ref(Path(jets.__file__)),
        original_core_source=support['production_core_source'],actual_angular_nodes=len(theta),
        all_coefficient_three_jet_comparisons=core_rows,low_RHS_comparisons=low,
        core_base_restored_bitwise=core_restored,whole_RHS_restored_bitwise=bool(rhs_restored),
        large_signal_core_jets_not_confused_with_cancelling_RHS=True,
        Jacobian_assembled=False,live_solver_changed=False,BVP_or_native_solve_invoked=False,
        derivative_interval_certificate=False,nonlinear_convergence_proved=False,
        elapsed_seconds=time.monotonic()-start,maximum_rss_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    (out/'comparison.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    summary=[]
    for h in (1e-6,3e-7,1e-7):
        rows=[r for r in core_rows if r['physical_step']==h]
        summary.append(dict(physical_step=h,maximum_relative_l2=max(r['relative_l2'] for r in rows),
            maximum_absolute=max(r['maximum_absolute'] for r in rows)))
    print(json.dumps(dict(status=result['status'],report=original.ref(out/'comparison.json'),
        core_three_jet_summary=summary,low_RHS_comparisons=low,
        elapsed_seconds=result['elapsed_seconds'],maximum_rss_KiB=result['maximum_rss_KiB'])),flush=True)


if __name__=='__main__':
    main()
