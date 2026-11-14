#!/usr/bin/env python3
"""R158 exact same-function angular injection and small local evaluation.

No BVP, Jacobian assembly, body integration, field fitting or tail degree
elevation is performed.  The complete old and new functions are evaluated
at one explicitly common angular grid and a few physical radial points.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import copy
import json
from pathlib import Path
import resource
import time
import traceback
import numpy as np
from fd2d_gc_archive_arrays import identity, load_npz, save_npz
from fd2d_gc_raw_bump_positive_trace import PositiveTraceRawBumpDAE
from fd2d_gc_nested_angular_positive_trace import FixedTailDegreePositiveTraceDAE, checkpoint_arrays
from fd2d_gc_positive_gauss_l import positive_gauss_l_delta
from fd2d_gc_positive_trace_branch import positive_trace_delta


def local_complete_fields(problem, vector, points, angles):
    view=copy.copy(problem)
    view.x=np.asarray(points,float);view.N=len(view.x);view.h=np.diff(view.x)
    view.size=view.N*view.q+view.parameter_count
    view.work=len(angles)
    freq=2*np.arange(view.K+1)
    view.E=np.cos(angles[:,None]*freq)
    view.O=np.sin(angles[:,None]*freq[1:])
    view.Ex=-np.sin(angles[:,None]*freq)*freq
    view.Ox=np.cos(angles[:,None]*freq[1:])*freq[1:]
    view.PE=2*view.E.T/view.work;view.PE[0]*=.5
    view.PO=2*view.O.T/view.work
    view.coords={k:np.asarray(v,float) for k,v in view.chart.coordinates(view.x,coordinate=angles).items()}
    view._operator_cache={}
    # Re-evaluate the same exact central seed on this explicitly common
    # grid; the frozen field functions are not resampled into coefficients.
    rho=np.asarray(view.geometry.radius(angles),float)
    rhop=np.asarray(view.geometry.radius_derivative(angles),float)
    if view.base_kind=='balanced_seed':
        view.seed=1/rho;view.seed_xi=-rhop/(rho*rho)
    else:
        view.seed=np.full_like(rho,1/float(view.geometry.a0));view.seed_xi=np.zeros_like(rho)
    original,p=problem.unpack(vector)
    y=np.column_stack([np.interp(view.x,problem.x,original[:,j]) for j in range(problem.q)])
    ops=view.operators(p[view.profile_parameter_slice])
    lift=view.lifting(p[view.profile_parameter_slice],p[view.tail_parameter_slice])
    raw=np.stack((view.E@y[:,:view.e].T,view.O@y[:,view.e:view.d].T,view.E@y[:,view.d:].T),axis=-1)+lift['values']
    angular=np.stack((view.Ex@y[:,:view.e].T,view.Ox@y[:,view.e:view.d].T,view.Ex@y[:,view.d:].T),axis=-1)+lift['xi']
    K=ops['jet']['K'][None,:]
    coast=positive_gauss_l_delta(raw,angular,K,view.window()[None,:],minimum_active_n=view.minimum_active_n)
    bg=raw.copy();bg[:,:,2]=coast['actual_l']
    bx=angular.copy();bx[:,:,2]=coast['actual_l_xi']
    terminal=positive_trace_delta(bg,bx,K,view.trace_window()[None,:],exact_tail_mask=view.trace_mask()[None,:])
    return dict(raw=raw,raw_angular=angular,lifting=lift['values'],lifting_angular=lift['xi'],
        actual=terminal['actual'],actual_angular=terminal['actual_angular'],
        a=ops['jet']['a'],a_s=ops['jet']['a_s'],K=ops['jet']['K'],
        U=view.coords['u'],U_s=view.coords['u_s'],U_xi=view.coords['u_xi'],
        tail_parameter_count=lift['tail'].parameter_count)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('candidate','input','radius-packet','reference-inlet','reference-cache','out-prefix'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--modes',type=int,default=31)
    args=ap.parse_args();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a new complete output stem')
    started=time.monotonic()
    here=Path(__file__).resolve().parent
    report=dict(schema='fd2d-exact-independent-tail-angular-injection-check-v1',
        source=identity(__file__),input=identity(args.input),candidate=identity(args.candidate),
        nested_provider=identity(here/'fd2d_gc_nested_angular_positive_trace.py'),
        inherited_provider=identity(here/'fd2d_gc_raw_bump_positive_trace.py'),
        completed=False,nonlinear_BVP_performed=False,Jacobian_assembled=False,
        continuous_certificate=False,exception=None)
    def save():
        report.update(seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        stem.with_name(stem.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    save()
    try:
        old=load_npz(args.input);k=int(old['modes'])
        nt=int(old['tail_parameter_count']) if 'tail_parameter_count' in old else k+1
        proof=json.loads(args.radius_packet.read_text())
        if not proof['passed'] or proof['candidate_sha256']!=report['candidate']['sha256']:
            raise ValueError('Wrong actual physical-radius packet')
        witness=dict(**identity(args.radius_packet),candidate_sha256=proof['candidate_sha256'])
        common=dict(max_step=.04,gap=.9,reference_inlet=args.reference_inlet,reference_cache=args.reference_cache,
            base_lower_bound='4/5',base_lower_provenance=witness,radius_floor=.1,minimum_active_n=.05)
        low=PositiveTraceRawBumpDAE(args.candidate,modes=k,**common)
        high=FixedTailDegreePositiveTraceDAE(args.candidate,modes=args.modes,tail_parameter_count=nt,**common)
        vector,embedding=high.inject_saved_field(old)
        if not np.array_equal(old['mesh'],low.x):
            raise ValueError('Old physical mesh differs from the bound original provider')
        old_vector=np.r_[old['corrections'].ravel(),old['parameters']]
        embedding['input']=report['input']
        report['embedding']=embedding
        report['new_field']=save_npz(stem.with_name(stem.name+'-field.npz'),
            **checkpoint_arrays(high,vector,report['candidate']['sha256'],embedding_definition=embedding))
        report['layout']=high.parameter_layout()
        # The common function check includes arbitrary points inside the
        # coast and terminal windows, plus the accurate cut.  These are not
        # new unknowns, and no field coefficients are fitted on this grid.
        ref=low.coast_reference
        points=np.unique(np.r_[0.,.1,.4,.57,
            ref.entry_s+.2*ref.length,ref.entry_s+.63*ref.length,
            ref.exit_s+.01,1.1,low.trace_start+.003,
            low.trace_ramp_stop+.003,low.trace_cut])
        angles=2*np.pi*np.arange(128)/128
        lo=local_complete_fields(low,old_vector,points,angles)
        hi=local_complete_fields(high,vector,points,angles)
        errors={name:float(np.max(np.abs(lo[name]-hi[name]),initial=0.))
            for name in ('raw','raw_angular','lifting','lifting_angular','actual','actual_angular','a','a_s','K','U','U_s','U_xi')}
        central_lo=low.core(old['parameters'][:k])[0].curvature(angles)
        yp,pp=high.unpack(vector)
        central_hi=high.core(pp[:high.K])[0].curvature(angles)
        errors['central_n']=float(np.max(np.abs(central_lo['n']-central_hi['n'])))
        errors['central_n_phi']=float(np.max(np.abs(central_lo['n_phi']-central_hi['n_phi'])))
        report['local_same_function_evaluation']=dict(points=points.tolist(),angle_count=len(angles),
            angle_definition='2*pi*j/128, common to both complete function readers',
            maximum_errors=errors,old_tail_count=lo['tail_parameter_count'],new_tail_count=hi['tail_parameter_count'],
            old_default_angular_work=low.work,new_default_angular_work=high.work,
            explicit_comparison_grid_is_not_a_new_solver_projection=True,
            symbolic_field_identity_proved_in_R158=True)
        report['input_unchanged']=identity(args.input)['sha256']==report['input']['sha256']
        report['completed']=report['input_unchanged'] and lo['tail_parameter_count']==hi['tail_parameter_count']==nt and max(errors.values())<2e-9
        save()
        print(json.dumps(dict(completed=report['completed'],field=report['new_field'],errors=errors,
            old_modes=k,new_modes=high.K,tail_parameter_count=nt,parameter_count=high.parameter_count,
            old_size=low.size,new_size=high.size,old_equations=low.residual_size,new_equations=high.residual_size,
            seconds=report['seconds'],peak_rss_kib=report['peak_rss_kib'])),flush=True)
        if not report['completed']:
            raise SystemExit(1)
    except Exception as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
        save();raise


if __name__=='__main__':
    main()
