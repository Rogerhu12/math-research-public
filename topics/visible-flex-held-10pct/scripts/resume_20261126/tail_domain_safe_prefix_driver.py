#!/usr/bin/env python3
"""Keep the original delta centered-difference queries inside their domain.

Only the delta finite-difference column in analytic_adaptive_core_jac.install
is adapted. Its original step is halved until both original RHS calls pass
their original guards. The base point must first pass the original RHS.
No geometry value is clipped, and no residual, Newton, or acceptance gate is
changed. The existing streamed/released prefix entry still executes the BVP.
The finite difference is a numerical Jacobian, not a derivative certificate.
"""
import argparse
import hashlib
import importlib.util
import inspect
import json
import os
from pathlib import Path
import sys

for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import numpy as np


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def domain_safe_delta_column(obj,t,y,p,max_halvings,emit):
    """Use the same centered quotient, with domain-valid perturbations only."""
    base_delta=float(obj.cfg['delta']+p[0])
    initial_step=2e-6*max(.1,base_delta)
    info=dict(nodes=len(t),base_parameter=float(p[0]),base_delta=base_delta,
              original_step=initial_step)
    try:
        try:
            base=obj.fun(t,y,p)
        except Exception as exc:
            emit('base_rejected',**info,error=repr(exc))
            raise
        if not np.all(np.isfinite(base)):
            raise FloatingPointError('Original base RHS is nonfinite')
        emit('base_passed',**info)
        for halvings in range(max_halvings+1):
            step=initial_step*2.**(-halvings)
            plus=p.copy();minus=p.copy()
            plus[0]+=step;minus[0]-=step
            delta_plus=float(obj.cfg['delta']+plus[0])
            delta_minus=float(obj.cfg['delta']+minus[0])
            trial=dict(**info,halvings=halvings,step=step,
                       plus_parameter=float(plus[0]),minus_parameter=float(minus[0]),
                       delta_plus=delta_plus,delta_minus=delta_minus)
            if not (delta_minus<base_delta<delta_plus and minus[0]<p[0]<plus[0]):
                emit('perturbations_indistinguishable',**trial)
                raise FloatingPointError('No distinguishable two-sided delta perturbation remains')
            values={}
            errors={}
            for side,parameter in (('plus',plus),('minus',minus)):
                try:
                    value=obj.fun(t,y,parameter)
                    if not np.all(np.isfinite(value)):
                        raise FloatingPointError('Perturbed original RHS is nonfinite')
                    values[side]=value
                except FloatingPointError as exc:
                    if not str(exc).startswith('Adaptive Frenet domain failure:'):
                        emit('non_domain_failure',**trial,side=side,error=repr(exc))
                        raise
                    errors[side]=repr(exc)
            if errors:
                emit('perturbation_domain_rejection',**trial,errors=errors)
                continue
            column=(values['plus']-values['minus'])/(2*step)
            if not np.all(np.isfinite(column)):
                emit('nonfinite_quotient',**trial)
                raise FloatingPointError('Original centered delta quotient is nonfinite')
            emit('centered_difference_return',**trial,
                 column_max=float(np.max(np.abs(column))))
            return column
        emit('halving_budget_exhausted',**info,max_halvings=max_halvings)
        raise FloatingPointError('Two-sided original delta domain was not reached within halving budget')
    finally:
        obj.initial(p)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--delta-max-halvings',type=int,default=40)
    options,original_arguments=parser.parse_known_args()
    if not 0<=options.delta_max_halvings<=60:
        raise ValueError('Use a finite halving budget between 0 and 60')
    if original_arguments.count('--outdir')!=1:
        raise ValueError('Expected the original single --outdir argument')
    out=Path(original_arguments[original_arguments.index('--outdir')+1]).resolve()
    records=out.with_name(out.name+'-delta-differencing')
    records.mkdir(parents=True,exist_ok=False)
    own=Path(__file__).resolve()
    current=own.parent
    library=current.parent/'resume_m3/round_raw_lib'
    original_module=library/'analytic_adaptive_core_jac.py'
    streamed=current/'streamed_release_prefix_driver.py'
    sys.path.insert(0,str(library))
    spec=importlib.util.spec_from_file_location('analytic_adaptive_core_jac',original_module)
    analytic=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=analytic
    spec.loader.exec_module(analytic)
    before=inspect.getsource(analytic.install)
    marker="   step=2e-6*max(.1,self.cfg['delta']+p[0]);plus=p.copy();minus=p.copy();plus[0]+=step;minus[0]-=step;PJ[:,0,:]=(self.fun(t,y,plus)-self.fun(t,y,minus))/(2*step);self.initial(p)"
    if before.count(marker)!=1:
        raise ValueError('Original delta centered-difference source anchor differs')
    after=before.replace(marker,'   PJ[:,0,:]=_held10_domain_safe_delta(self,t,y,p)')
    state=dict(scope=__doc__,status='prepared',progress=dict(
        calls=0,returned=0,rejected_perturbations=0,maximum_halvings=0),
        source_hashes={str(p):digest(p) for p in (own,original_module,streamed)},
        original_install_sha256=hashlib.sha256(before.encode()).hexdigest(),
        executed_install_sha256=hashlib.sha256(after.encode()).hexdigest(),
        only_replaced_original_delta_difference=True,complete_surface=False,
        max_halvings=options.delta_max_halvings)

    def save():
        temporary=records/'summary.json.tmp'
        temporary.write_text(json.dumps(state,indent=2,allow_nan=False)+'\n')
        temporary.replace(records/'summary.json')

    def emit(kind,**fields):
        row=dict(kind=kind,**fields)
        with (records/'events.jsonl').open('a') as stream:
            stream.write(json.dumps(row,allow_nan=False)+'\n')
        progress=state['progress']
        if kind in ('base_passed','base_rejected'):
            progress['calls']+=1
        if kind=='centered_difference_return':
            progress['returned']+=1
        if kind=='perturbation_domain_rejection':
            progress['rejected_perturbations']+=len(fields['errors'])
        progress['maximum_halvings']=max(progress['maximum_halvings'],fields.get('halvings',0))
        progress['last_actual_difference_event']=row
        save()

    analytic._held10_domain_safe_delta=lambda obj,t,y,p: domain_safe_delta_column(
        obj,t,y,p,options.delta_max_halvings,emit)
    exec(compile(after,str(own)+'::domain_valid_delta_install','exec'),analytic.__dict__)
    save()
    spec=importlib.util.spec_from_file_location('held10_domain_safe_streamed',streamed)
    driver=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(driver)
    sys.argv=[str(streamed),*original_arguments]
    state['status']='original_bvp_running'
    save()
    try:
        driver.main()
        state['status']='original_driver_returned'
    except Exception as exc:
        state.update(status='original_driver_exception',error=repr(exc))
        raise
    finally:
        save()


if __name__=='__main__':
    main()
