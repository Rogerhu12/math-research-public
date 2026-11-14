#!/usr/bin/env python3
"""Check storage observations against the original batching/Newton execution.

Synthetic fields only: no physical Flow, BVP, tail worker or geometry is built.
The actual owned Newton source is compiled with its fixed-S and checkpoint
hooks, with and without the new exception observer, then compared literally.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace

HERE=Path(__file__).resolve().parent


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out-prefix',type=Path,required=True)
    args=parser.parse_args();out=args.out_prefix
    if out.with_suffix('.json').exists():
        raise FileExistsError('The verification output already exists')
    sources={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in (
        Path(__file__).name,'strong_domain_rejection_observer.py',
        'strong_fresh_physical_merit_runtime.py','strong_physical_merit_and_affine_resume.py',
        'strong_actual_newton_checkpoints.py','root_domain_newton.py','root_radial_batching.py')}
    import numpy as np
    from scipy.sparse import csc_matrix
    import root_radial_batching as radial
    import strong_actual_newton_checkpoints as checkpoints
    from strong_domain_rejection_observer import DomainObservation
    from strong_fresh_physical_merit_runtime import Runtime
    checks={};diagnostics=[]
    old_value,old_jac=radial.value,radial.state_jacobian
    class SyntheticFlow:
        def __init__(self,fail=False,jac_fail=False):
            self.calls=[];self.fail=fail;self.jac_fail=jac_fail
            self.error=FloatingPointError('synthetic exact radial block')
            self.cfg={'synthetic':True}
        def fun(self,s,y,p):
            self.calls.append(('value',s.tobytes(),y.tobytes(),p.tobytes()))
            if self.fail and s[0]==3.:raise self.error
            return y*2.+s[None,:]+p[0]
        def fun_jac(self,s,y,p):
            self.calls.append(('jacobian',s.tobytes(),y.tobytes(),p.tobytes()))
            if self.jac_fail and s[0]==3.:raise self.error
            return np.repeat((2.*np.eye(y.shape[0]))[:,:,None],len(s),axis=2),None
    s=np.arange(9,dtype=float);y=np.arange(36,dtype=float).reshape(4,9)/17.
    y[0,0]=-0.;p=np.array([-.0,.2,.4])
    direct=SyntheticFlow();a=old_value(direct,s,y,p,3);aj=old_jac(direct,s,y,p,3)
    observer=DomainObservation(out.with_name(out.name+'-radial'),{},sources,
        emit=lambda event,**data:diagnostics.append(dict(event=event,**data)))
    observer.install_radial(radial)
    proxy=SyntheticFlow();b=radial.value(proxy,s,y,p,3);bj=radial.state_jacobian(proxy,s,y,p,3)
    checks['successful_RHS_and_state_Jacobian_literal_bytes']=a.tobytes()==b.tobytes() and aj.tobytes()==bj.tobytes()
    checks['independent_radial_batch_order_and_inputs_unchanged']=direct.calls==proxy.calls
    for method,kind in [('value','radial-value'),('state_jacobian','radial-state-jacobian')]:
        flow=SyntheticFlow(fail=method=='value',jac_fail=method=='state_jacobian')
        same_error=False
        try:getattr(radial,method)(flow,s,y,p,3)
        except FloatingPointError as error:same_error=error is flow.error
        row=observer.failures[-1]
        with np.load(row['path']) as data:
            arrays=(data['s'].tobytes()==s[3:6].tobytes() and
                data['y'].tobytes()==y[:,3:6].tobytes() and data['p'].tobytes()==p.tobytes())
            metadata=json.loads(bytes(data['metadata']).decode())
        checks[method+'_same_exception_object_and_exact_failed_block']=same_error and arrays
        checks[method+'_no_extra_evaluation']=len(flow.calls)==2 and row['kind']==kind
        checks[method+'_unaccepted_observation']=not metadata['solver_success'] and not metadata['physical_surface']
    observer.finish()
    checks['radial_methods_restored']=radial.value is old_value and radial.state_jacobian is old_jac

    # A nonlinear complete residual of the same array layout exercises the
    # unchanged domain rejection and actual checkpoint/merit installation chain.
    M,n,m,k=3,10,3,6
    cfg=dict(modes=M,gauge=.09,fixed_parameter_weights=[1.07,.09,.0081,1.,1.,1.])
    target_y=np.linspace(-.1,.2,n*m).reshape(n,m,order='F')
    target_p=np.array([.5,.4,.3,.2,.1,.25])
    def run(observed):
        label='observed' if observed else 'control'
        path=HERE/'root_domain_newton.py'
        spec=importlib.util.spec_from_file_location('synthetic_owned_Newton_'+label,path)
        loaded=importlib.util.module_from_spec(spec);spec.loader.exec_module(loaded)
        adapter=SimpleNamespace(TRANSFORMS={path.name:dict(original_sha256=sources[path.name],replacements=[])})
        runtime=Runtime(cfg,out.with_name(out.name+'-'+label))
        runtime_events=[];runtime.emit=lambda event,**data:runtime_events.append(dict(event=event,**data))
        runtime.install_newton(loaded,path,adapter)
        obs=None
        if observed:
            obs=DomainObservation(out.with_name(out.name+'-newton'),cfg,sources,
                emit=lambda event,**data:diagnostics.append(dict(event=event,**data)))
            obs.install_newton(loaded,path,adapter)
        records=[]
        class Recorder:
            def save(self,col_fun,Y,P,data,iteration,phase,bvp_tol,bc_tol,stats):
                records.append((Y.tobytes(),P.tobytes(),data[0].tobytes(),int(iteration),phase,dict(stats)))
        checkpoints.install_observer(loaded,path,adapter,Recorder())
        calls={'collocation':0,'boundary':0,'Jacobian':0}
        def col(Y,P):
            calls['collocation']+=1
            if P[0]>.65:raise FloatingPointError('synthetic parameter domain upper bound')
            return Y[:,1:]-target_y[:,1:],.5*(Y[:,:-1]+Y[:,1:]),np.zeros_like(Y),np.zeros((n,m-1))
        def bc(ya,yb,P):
            calls['boundary']+=1
            return np.r_[ya-target_y[:,0],P*P-target_p*target_p]
        def jac(Y,P,ym,ff,fm,br):
            calls['Jacobian']+=1
            cols=np.r_[np.arange(n,n*m),np.arange(n),np.arange(n*m,n*m+k)]
            values=np.r_[np.ones(n*m),2*P]
            return csc_matrix((values,(np.arange(n*m+k),cols)),shape=(n*m+k,n*m+k))
        result=loaded.solve_newton(n,m,np.array([.5,.5]),col,bc,jac,np.zeros((n,m)),
            np.array([.2,.3,.25,.15,.08,.2]),None,1e-9,1e-9)
        if obs:obs.finish()
        runtime.finish()
        return dict(result=result,records=records,calls=calls,stats=loaded.STATS,
            merit_evaluations=runtime.stats['merit_evaluations'],merit_events=runtime_events,
            source_transform=adapter.TRANSFORMS[path.name])
    control,observed=run(False),run(True)
    checks['actual_Newton_final_arrays_and_status_bitwise_equal']=(
        control['result'][0].tobytes()==observed['result'][0].tobytes() and
        control['result'][1].tobytes()==observed['result'][1].tobytes() and
        control['result'][2]==observed['result'][2])
    checks['actual_Newton_all_checkpoint_values_and_order_identical']=control['records']==observed['records']
    checks['actual_Newton_RHS_BC_Jacobian_counts_identical']=control['calls']==observed['calls']
    checks['actual_Newton_domain_merit_factor_decisions_identical']=control['stats']==observed['stats']
    checks['actual_Newton_fixed_merit_evaluations_identical']=control['merit_events']==observed['merit_events']
    checks['nonlinear_trial_really_rejected_then_accepted']=(observed['stats']['rejected_domain_trials']>=1
        and observed['stats']['accepted_steps']>=1 and observed['stats']['minimum_alpha']<1.)
    checks['actual_checkpoint_hook_survives_both_transforms']=len(observed['records'])>=3
    checks['original_final_residual_satisfied']=float(np.max(np.abs(bc_result:=np.r_[
        observed['result'][0].ravel(order='F')-target_y.ravel(order='F'),
        observed['result'][1]**2-target_p**2])))<1e-9
    report=dict(scope=__doc__,passed=all(checks.values()),checks=checks,source_sha256_at_start=sources,
        calls=observed['calls'],Newton_stats=observed['stats'],checkpoints=len(observed['records']),
        actual_physical_Flow_instances=0,physical_RHS_calls=0,tail_workers=0,
        numerical_surface_result=False,domain_observations=diagnostics,
        final_synthetic_residual=float(np.max(np.abs(bc_result))))
    out.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({key:report[key] for key in ('passed','checks','calls','Newton_stats','checkpoints','final_synthetic_residual')}),flush=True)
    if not report['passed']:raise SystemExit(1)


if __name__=='__main__':main()
