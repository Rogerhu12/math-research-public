#!/usr/bin/env python3
"""Reconstruct one saved failed endpoint state and inspect its original trials.

This evaluates one original Newton direction and the original halving sequence
without updating the saved state or solving a new BVP.  It distinguishes a
core-domain failure from a subsequent collocation/Frenet failure.  It does not
claim to recover the unsaved historical iteration sequence.  The original
core, full Jacobian, affine DN, residual, merit and domain checks are used.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
from datetime import datetime, timezone
import gzip
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy.integrate import _bvp
from scipy.interpolate import PPoly
from scipy.sparse.linalg import splu
from m3_raw_diagnostic_model import RawDiagnosticEnvironment, sha


def event(name, **kwargs):
    print(json.dumps(dict(event=name,utc=datetime.now(timezone.utc).isoformat(),**kwargs)),flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--short-bridge',type=Path,
        help='Optional byte-identical current-session path replacing the recorded input path')
    args=parser.parse_args()
    started=time.monotonic();run=args.run.resolve()
    command=json.loads((run/'continuation-command.json').read_text())['command']
    def argument(name):return command[command.index('--'+name)+1]
    cp=run/'seed.json.gz';record=json.loads(gzip.decompress(cp.read_bytes()))
    if record['solver_success'] or record['config']['fixed_metric']:
        raise ValueError('Expected the saved failed nonfixed endpoint state')
    settings=record['core_round_settings']
    if settings['homotopy']!=1.:
        raise ValueError('This diagnostic is for the exact circle endpoint')
    source=Path(argument('source-topic'))
    old_bridge=Path(argument('short-bridge'))
    bridge=args.short_bridge.resolve() if args.short_bridge else old_bridge
    expected_bridge=record['core_round_sources'][str(old_bridge)]
    if sha(bridge)!=expected_bridge:
        raise ValueError('The bridge override is not byte-identical')
    profile=json.loads(Path(argument('profile')).read_text())
    chart=json.loads(Path(argument('chart')).read_text())
    port_path=Path(argument('linear-port'))
    port=json.loads(port_path.read_text());port['_sha256']=sha(port_path)
    if chart!=record['chart'] or port['_sha256']!=record['physical_port_sha256']:
        raise ValueError('The original finite problem inputs differ')
    env=RawDiagnosticEnvironment(source,bridge,chart,settings)
    M,N=record['config']['modes'],record['config']['angular']
    obj=env.make(settings,profile,port,record['gauge_amplitude'],M,N,
                 False,record['warp_reference_q'])
    obj.pscale=np.asarray(record['central_correction_scales'])
    obj.bcweights=np.full(M,record['config']['physical_bc_tol']/record['config']['bc_tol'])
    p=np.asarray(record['parameters']);obj.initial(p)
    if {**profile,'delta':profile['delta']+p[0]}!=record['frozen_profile']:
        raise ValueError('The physical profile was not reconstructed')
    from curve_stable_prefix_bvp import load_checkpoint
    decoded=load_checkpoint(cp);physical=np.asarray(decoded['mesh'])
    pp=PPoly.construct_fast(np.asarray(decoded['pp_coefficients']),physical,
                             extrapolate=False,axis=1)
    x=obj.inverse_chart(physical,p[0]);y=pp(physical);h=np.diff(x)
    tail_file=run/'seed_tail_0002.json.gz'
    tail=json.loads(gzip.decompress(tail_file.read_bytes()))
    if not tail['response']['converged'] or not tail['response']['residual']<tail['config']['solveTolerance']:
        raise ValueError('The original affine anchor did not pass its original gate')
    obj.tail=env.coupler.AffineTailForInnerBVP(tail['request']['height'],tail['response'],M)
    n,m,k=obj.n,len(x),len(p)
    col_fun,jac=_bvp.prepare_sys(n,m,k,obj.fun,obj.bc,obj.fun_jac,obj.bc_jac,x,h)
    col,ym,ff,fm=col_fun(y,p);br=obj.bc(y[:,0],y[:,-1],p)
    residual=np.r_[col.ravel(order='F'),br]
    spline=_bvp.create_spline(y,ff,x,h)
    rms=_bvp.estimate_rms_residuals(obj.fun,spline,x,h,p,1.5*col/h,fm)
    replay=dict(recorded_rms=record['max_rms_collocation_residual'],
        reconstructed_rms=float(rms.max()),difference=float(rms.max()-record['max_rms_collocation_residual']),
        physical_chart_error=float(abs(obj.chart(x,p[0])[0]-physical).max()),
        original_bc_max=float(abs(br).max()),original_residual_max=float(abs(residual).max()),
        provenance='The saved physical quintic node values and original inverse chart '
            'reconstruct a finite state. The final quintic endpoint need not be bitwise '
            'the lost raw solve_bvp cubic. This is a new one-state diagnostic, not a replay '
            'of all historical rejected iterations.')
    event('matrix_start',nodes=m,**replay)
    J=jac(y,p,ym,ff,fm,br);LU=splu(J);step=LU.solve(residual)
    field_step=step[:n*m].reshape((n,m),order='F');parameter_step=step[n*m:]
    cost=float(step@step)
    event('original_direction',linear_residual=float(abs(J@step-residual).max()),
          field_step_max=float(abs(field_step).max()),parameter_step=parameter_step.tolist())
    rows=[]
    for back in range(21):
        alpha=2.**(-back);trial_p=p-alpha*parameter_step
        trial_y=y-alpha*field_step
        row=dict(backtracking_index=back,alpha=alpha,
            trial_delta=float(profile['delta']+trial_p[0]),
            physical_control_max=float(abs(trial_p[1:]*obj.pscale).max()))
        try:
            obj.initial(trial_p)
            core=obj._core
            row.update(core_domain_passed=True,
                core_rho_lower=core.rho_lower,core_rho_sample_min=core.rho_min_sample,
                core_positivity_grid=core.positivity_grid_per_sector)
        except FloatingPointError as error:
            row.update(core_domain_passed=False,rejected_stage='original_core_or_profile',error=str(error))
            rows.append(row);event('trial',**row);continue
        try:
            cr,tm,tf,tmm=col_fun(trial_y,trial_p)
            bc=obj.bc(trial_y[:,0],trial_y[:,-1],trial_p)
            trial_res=np.r_[cr.ravel(order='F'),bc]
            newstep=LU.solve(trial_res);newcost=float(newstep@newstep)
            merit=np.isfinite(newcost) and newcost<(1-.4*alpha)*cost
            row.update(collocation_domain_passed=True,
                original_residual_max=float(abs(trial_res).max()),
                original_bc_max=float(abs(bc).max()),
                original_merit_ratio=newcost/cost,original_merit_threshold=1-.4*alpha,
                would_pass_original_one_step_merit=bool(merit))
            if not merit:row['rejected_stage']='original_merit'
        except FloatingPointError as error:
            row.update(collocation_domain_passed=False,
                rejected_stage='original_collocation_or_boundary',error=str(error))
        rows.append(row);event('trial',**row)
        if row.get('would_pass_original_one_step_merit'):
            break
    obj.initial(p)
    counts={name:sum(row.get('rejected_stage')==name for row in rows) for name in
            ('original_core_or_profile','original_collocation_or_boundary','original_merit')}
    result=dict(scope=__doc__,command=sys.argv,run=str(run),input=dict(path=str(cp),sha256=sha(cp)),
        input_chunks=[dict(path=str(z),sha256=sha(z)) for z in sorted(run.glob('seed_coeff_*.npy.gz'))],
        affine_anchor=dict(path=str(tail_file),sha256=sha(tail_file)),
        bridge_storage=dict(recorded_path=str(old_bridge),verified_path=str(bridge),sha256=sha(bridge)),
        source_sha256={**env.sources,str(Path(__file__).resolve()):sha(__file__),
            str(source/'repro/source-root/topics/large-amplitude-twist-flex/scripts/f6curve_domain_newton.py'):
                sha(source/'repro/source-root/topics/large-amplitude-twist-flex/scripts/f6curve_domain_newton.py')},
        settings=settings,parameters=p.tolist(),parameter_step=parameter_step.tolist(),
        physical_control_step=(parameter_step[1:]*obj.pscale).tolist(),
        original_control_scales=obj.pscale.tolist(),q_gauge=obj.q,
        replay=replay,matrix_shape=list(J.shape),matrix_nnz=J.nnz,
        original_linear_residual_max=float(abs(J@step-residual).max()),
        original_field_step_max=float(abs(field_step).max()),
        original_merit_cost=cost,trials=rows,rejection_counts=counts,
        one_step_candidate_found=any(row.get('would_pass_original_one_step_merit',False) for row in rows),
        seconds=time.monotonic()-started,
        interpretation='No state is advanced or accepted. Original core/profile and then '
            'full collocation/BC checks are evaluated on the original halving sequence. '
            'This isolates a concrete rejection source at one reconstructed state; it '
            'does not assign all historical domain rejections to that source or change '
            'any physical equation, original positivity floor, grid ceiling or tolerance.')
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    event('finished',output=str(args.out),counts=counts,seconds=result['seconds'])


if __name__=='__main__':
    main()
