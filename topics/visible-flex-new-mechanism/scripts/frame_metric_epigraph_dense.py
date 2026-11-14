#!/usr/bin/env python3
"""Dense-radial minimax continuation with physical/auxiliary selection split.

The published epigraph module stays unchanged. This independent subclass adds
the exact sampled mirror-pair polynomial and retains the best physical eta even
when a solver trial's auxiliary delta underestimates that eta. The CLI evaluates
only artificial arrays; research geometry belongs to the public Actions driver.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import time

import numpy as np

from frame_collar_bvp import atomic_save
from frame_collar_residual_audit import digest
from frame_height_affine_gate import HeightAffineGate,EvaluationBudgetReached
from frame_metric_epigraph import (MetricEpigraphObjective,configuration as old_configuration,
    metric_rows,geometry_values,candidate_decision as old_candidate_decision,
    run_epigraph_slsqp,_EpigraphArrayProblem,implementation_hashes as old_hashes)


def implementation_hashes():
    result=old_hashes()
    result[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


def configuration():
    result=old_configuration()
    result.update(mirror_target_exact='61/1000',mirror_polynomial_tolerance=1e-12,
        mirror_radius_tolerance=1e-9,normal_area_numerical_floor=1e-10,
        final_selection='best_physical_max_eta_point',
        physical_selection_ignores_only_the_auxiliary_delta_coverage=True,
        mirror_constraint='z^2*|Xs cross T|^2-tau^2*(Xs cross T)_z^2 >= 0',
        mirror_constraint_is_necessary_for_these_sampled_pairs_only=True,
        no_curvature_or_all_pairs_constraint_added=True)
    return result


def mirror_values(data,tau):
    tau=float(tau)
    if not np.isfinite(tau) or tau<=0:raise ValueError('finite positive mirror target required')
    X,U,T=(np.asarray(data[key],float) for key in ['X','Xs','T'])
    with np.errstate(over='raise',invalid='raise'):
        W=np.cross(U,T);area2=np.sum(W*W,axis=-1);z=X[...,2]
        polynomial=z*z*area2-tau*tau*W[...,2]**2
    if not np.all(np.isfinite(polynomial)) or not np.all(np.isfinite(area2)):
        raise FloatingPointError('nonfinite mirror polynomial or normal area')
    denominator=abs(W[...,2]);radius=np.full(area2.shape,np.inf)
    nonzero=denominator>0
    with np.errstate(over='ignore',divide='ignore',invalid='raise'):
        radius[nonzero]=abs(z[nonzero])*np.sqrt(area2[nonzero])/denominator[nonzero]
    return {'W':W,'area_squared':area2,'polynomial':polynomial,'radius':radius,
        'nonzero_normal_z':nonzero}


def mirror_parameter_jacobian(data,tau,values=None):
    """Exact polynomial derivative; no division by W_z and no unit-T shortcut."""
    values=mirror_values(data,tau) if values is None else values
    X,U,T=(np.asarray(data[key],float) for key in ['X','Xs','T'])
    W=values['W'];z=X[...,2];D=z[...,None]**2*W
    D[...,2]-=float(tau)**2*W[...,2]
    result=(2*z*values['area_squared'])[...,None]*data['jac_X'][:,:,2,:]
    result+=2*np.einsum('rtc,rtcn->rtn',np.cross(T,D),data['jac_Xs'])
    result+=2*np.einsum('rtc,rtcn->rtn',np.cross(D,U),data['jac_T'])
    if not np.all(np.isfinite(result)):raise FloatingPointError('nonfinite mirror parameter Jacobian')
    return result


def candidate_decision(problem,gate,state,delta,data,lower,upper,cfg):
    result=old_candidate_decision(problem,gate,state,delta,data,lower,upper,cfg)
    values=mirror_values(data,float(Q(cfg['mirror_target_exact'])))
    area=np.sqrt(values['area_squared']);radius=values['radius'];finite=np.isfinite(radius)
    nonregular=int(np.count_nonzero(area<=cfg['normal_area_numerical_floor']))
    row_min=float(np.min(values['polynomial']))
    finite_min=float(np.min(radius[finite])) if np.any(finite) else None
    direct_pass=bool(finite_min is None or finite_min>=float(Q(cfg['mirror_target_exact']))-cfg['mirror_radius_tolerance'])
    row_pass=bool(row_min>=-cfg['mirror_polynomial_tolerance'])
    regular=nonregular==0
    existing_physical=bool(result['cap_and_box']['eligible_under_declared_numerical_gate_tolerances']
        and result['signed_height_pass'] and result['hard_ball_pass'] and result['hard_strip_pass'])
    physical=bool(existing_physical and row_pass and direct_pass and regular)
    prior_auxiliary=bool(result['eligible_under_all_declared_sampled_constraints'])
    result.update(eligible_under_original_physical_gate_groups=existing_physical,
        eligible_under_physical_gates_including_mirror=physical,
        eligible_under_all_declared_sampled_constraints=bool(prior_auxiliary and physical),
        mirror_target_exact=cfg['mirror_target_exact'],mirror_polynomial_min=row_min,
        mirror_polynomial_tolerance=cfg['mirror_polynomial_tolerance'],mirror_polynomial_pass=row_pass,
        direct_mirror_radius_min_finite=finite_min,mirror_radius_tolerance=cfg['mirror_radius_tolerance'],
        independent_direct_mirror_radius_pass=direct_pass,
        zero_normal_z_pairs_without_finite_upper_bound_count=int(np.count_nonzero(~values['nonzero_normal_z'])),
        regular_normal_area_floor=cfg['normal_area_numerical_floor'],
        nonregular_sample_count=nonregular,regularity_screen_pass=regular,
        auxiliary_delta_failure_does_not_erase_a_physically_eligible_trial=True,
        mirror_pair_screen_does_not_certify_whole_surface_reach=True)
    return result


class DenseMirrorEpigraphObjective(MetricEpigraphObjective):
    def __init__(self,*args,**kwargs):
        if kwargs.get('cfg') is None:kwargs['cfg']=configuration()
        super().__init__(*args,**kwargs)
        if Q(self.cfg['mirror_target_exact'])<=0:raise ValueError('positive exact mirror target required')
        for name in ['mirror_polynomial_tolerance','mirror_radius_tolerance','normal_area_numerical_floor']:
            if not np.isfinite(self.cfg[name]) or self.cfg[name]<0:raise ValueError('finite nonnegative mirror screening numbers required')
        self.best_physical=None
        self.evaluation_definition.update(schema='dense-radial-mirror-max-metric-objective-evaluation-v1',
            source_files_sha256=implementation_hashes(),
            separate_physical_and_auxiliary_best_points=True,
            curvature_remains_an_independent_final_diagnostic=True)
        self.evaluation_definition['constraint_row_order'].append('z^2*|Xs cross T|^2-tau^2*(Xs cross T)_z^2')
        self.evaluation_sha256=digest(self.evaluation_definition)

    def physical_geometry(self,state):
        """One geometry call; retain a mirror Jacobian, not two extra 3-vector Jacobians."""
        state=np.asarray(state,float)
        if state.shape!=(self.n,) or not np.all(np.isfinite(state)):raise ValueError('finite complete physical state required')
        self.assert_context(state);self._wall()
        if self.geometry_cache is not None and np.array_equal(state,self.geometry_cache['state']):return self.geometry_cache
        if self.geometry_evaluations>=self.cfg['max_physical_evaluations']:
            raise EvaluationBudgetReached('distinct physical geometry budget reached; physical and auxiliary best points retained')
        data=self.problem.geometry(state,self.radial,self.theta,self.order,jacobian=True)
        expected=(len(self.radial),len(self.theta),3)
        for name in ['X','Xs','T']:
            if np.asarray(data[name]).shape!=expected or np.asarray(data['jac_'+name]).shape!=expected+(self.n,):
                raise ValueError('complete current geometry and analytic physical Jacobians required')
            if not np.all(np.isfinite(data[name])) or not np.all(np.isfinite(data['jac_'+name])):
                raise FloatingPointError('nonfinite geometry or analytic physical Jacobian')
        values=geometry_values(data)
        de=2*np.einsum('rtc,rtcn->rtn',data['Xs'],data['jac_Xs'])
        df=(np.einsum('rtc,rtcn->rtn',data['T'],data['jac_Xs'])
            +np.einsum('rtc,rtcn->rtn',data['Xs'],data['jac_T']))
        mirror=mirror_values(data,float(Q(self.cfg['mirror_target_exact'])))
        mirror_jac=mirror_parameter_jacobian(data,float(Q(self.cfg['mirror_target_exact'])),mirror)
        if not np.all(np.isfinite(de)) or not np.all(np.isfinite(df)):
            raise FloatingPointError('nonfinite direct metric derivatives')
        cache={key:np.asarray(data[key]).copy() for key in ['X','Xs','T','center']}
        for key in ['Xt','Xss','Xst','Xtt','Ts','Tss','Ttheta','primitive']:
            if key in data:cache[key]=np.asarray(data[key]).copy()
        for key in ['metric','height']:
            if key in data:cache[key]={name:np.asarray(value).copy() for name,value in data[key].items()}
        cache.update(state=state.copy(),radial=self.radial,theta=self.theta,
            e=values['e'],f=values['f'],eta=values['eta'],de=de,df=df,
            jac_X=np.asarray(data['jac_X']).copy(),mirror_polynomial=mirror['polynomial'],mirror_jacobian=mirror_jac)
        for value in cache.values():
            if isinstance(value,np.ndarray):value.setflags(write=False)
            elif isinstance(value,dict):
                for item in value.values():
                    if isinstance(item,np.ndarray):item.setflags(write=False)
        self.geometry_evaluations+=1;cache['geometry_evaluation']=self.geometry_evaluations
        self.geometry_cache=cache
        self.maximum_geometry_cache_array_bytes=max(self.maximum_geometry_cache_array_bytes,
            sum(value.nbytes if isinstance(value,np.ndarray) else
                sum(item.nbytes for item in value.values() if isinstance(item,np.ndarray))
                if isinstance(value,dict) else 0 for value in cache.values()))
        return cache

    def evaluate(self,vector):
        vector=np.asarray(vector,float)
        if vector.shape!=(self.n+1,) or not np.all(np.isfinite(vector)):raise ValueError('physical vector plus finite auxiliary delta required')
        delta=float(vector[-1]);metric_rows(np.array([0.]),np.array([0.]),delta)
        self.assert_context(vector[:-1]);self._wall()
        if (self.epigraph_cache is not None and np.array_equal(vector,self.epigraph_cache['vector'])
                and self.geometry_cache is not None and np.array_equal(vector[:-1],self.geometry_cache['state'])):
            return self.epigraph_cache['record']
        data=self.physical_geometry(vector[:-1])
        decision=candidate_decision(self.problem,self.gate,vector[:-1],delta,data,self.lower,self.upper,self.cfg)
        self.epigraph_evaluations+=1
        record={'epigraph_evaluation':self.epigraph_evaluations,'physical_geometry_evaluation':data['geometry_evaluation'],
            'elapsed_seconds':time.monotonic()-self.started,'decision':decision}
        point={'vector':vector.copy(),'record':copy.deepcopy(record)}
        if self.best_trial is None or delta<self.best_trial['vector'][-1]:self.best_trial=point
        def smaller_eta(old):
            return (old is None or decision['direct_max_eta']<old['record']['decision']['direct_max_eta']
                or (decision['direct_max_eta']==old['record']['decision']['direct_max_eta'] and delta<old['vector'][-1]))
        if decision['eligible_under_physical_gates_including_mirror'] and smaller_eta(self.best_physical):self.best_physical=point
        if decision['eligible_under_all_declared_sampled_constraints']:
            if self.best_delta is None or delta<self.best_delta['vector'][-1]:self.best_delta=point
            if smaller_eta(self.best_eta):self.best_eta=point
        self.history.append(record);self.epigraph_cache={'vector':vector.copy(),'record':copy.deepcopy(record)}
        now=time.monotonic()
        due=(self.geometry_evaluations-self.last_checkpoint_geometry>=self.cfg['checkpoint_physical_evaluations']
            or now-self.last_checkpoint>=self.cfg['checkpoint_seconds'])
        if self.checkpoint is not None and due:
            self.checkpoint(self.snapshot());self.last_checkpoint=now;self.last_checkpoint_geometry=self.geometry_evaluations
        if now-self.started>=self.cfg['max_seconds']:
            raise EvaluationBudgetReached('wall budget after preserving both completed physical/auxiliary decisions')
        return record

    def constraint_fun(self,vector):
        previous=super().constraint_fun(vector)
        return np.r_[previous,self.geometry_cache['mirror_polynomial'].ravel()]

    def constraint_jac(self,vector):
        previous=super().constraint_jac(vector);count=self.geometry_cache['e'].size
        result=np.zeros((7*count,self.n+1));result[:6*count]=previous
        result[6*count:,:self.n]=self.geometry_cache['mirror_jacobian'].reshape(count,self.n)
        self.maximum_constraint_Jacobian_bytes=max(self.maximum_constraint_Jacobian_bytes,result.nbytes)
        return result

    def snapshot(self):
        result=super().snapshot();point=self.best_physical
        if point is None:encoded=None
        else:
            state=point['vector'][:-1];delta=float(point['vector'][-1])
            encoded={'physical_parameter_coefficients_binary64':state.tolist(),
                'exact_binary64_physical_coefficients':[str(Q.from_float(float(x))) for x in state],
                'physical_state_sha256':digest(self.problem.identity(state)),
                'auxiliary_delta_evaluated':delta,'auxiliary_delta_exact_binary64':str(Q.from_float(delta)),
                'record':copy.deepcopy(point['record'])}
        result.update(schema='dense-mirror-epigraph-two-selection-checkpoint-v1',
            best_physical_max_eta_point=encoded,final_selection='best_physical_max_eta_point',
            best_eligible_points_still_require_current_auxiliary_delta_coverage=True,
            physical_best_may_fail_its_saved_auxiliary_delta_without_changing_that_delta=True)
        return result


def run_dense_epigraph(objective,initial,*,artificial_inputs_only=False,evaluate_only=False):
    result=run_epigraph_slsqp(objective,initial,artificial_inputs_only=artificial_inputs_only,evaluate_only=evaluate_only)
    result['solver']['hard_constraint_groups'].append('current mirror-pair polynomial; independent direct-radius and regularity selection')
    result['selected_point']='best_physical_max_eta_point; saved auxiliary failure remains separately visible'
    result['separate_physical_and_auxiliary_selection']=True
    return result


def developer_check():
    initial=np.array([0.,.6,.6]);theta=np.arange(8)*np.pi/4;t=np.array([0.,.3,1.])
    lower=np.array([-2.,-1.,-1.]);upper=np.array([2.,1.,1.])
    def make(problem=None,changes=None):
        p=_EpigraphArrayProblem() if problem is None else problem;cfg=configuration()
        cfg.update(mirror_target_exact='1/1000',maxiter=6,max_physical_evaluations=25,max_seconds=30.)
        if changes:cfg.update(changes)
        return DenseMirrorEpigraphObjective(p,HeightAffineGate.from_artificial_array_problem(p),t,theta,3,lower,upper,cfg=cfg)
    objective=make();vector=objective.initial_vector(initial);objective.evaluate(vector)
    calls=objective.problem.calls
    objective.fun(vector);objective.jac(vector);objective.constraint_fun(vector);J=objective.constraint_jac(vector)
    shared=objective.problem.calls==calls
    delta_only=vector.copy();delta_only[-1]+=.1;objective.constraint_jac(delta_only)
    delta_reuse=objective.problem.calls==calls
    direction=np.array([.2,-.3,.4,.5]);h=1e-6
    numerical=(objective.constraint_fun(vector+h*direction)-objective.constraint_fun(vector-h*direction))/(2*h)
    error=float(np.max(abs(numerical-J@direction)))
    # Same real toy family, lower direct eta, deliberately under-bounded delta.
    separated=make();separated.evaluate(separated.initial_vector(initial))
    better=np.array([0.,.2,.6]);data=separated.physical_geometry(better);maximum=float(np.max(data['eta']))
    under=np.r_[better,maximum/2];record=separated.evaluate(under)['decision'];snap=separated.snapshot()
    split=(record['eligible_under_physical_gates_including_mirror'] and not record['independent_direct_eta_pass']
        and snap['best_physical_max_eta_point']['exact_binary64_physical_coefficients']==[str(Q.from_float(float(x))) for x in better]
        and snap['best_eligible_direct_max_eta_point']['physical_state_sha256']!=snap['best_physical_max_eta_point']['physical_state_sha256'])
    bad=make(changes={'mirror_target_exact':'10'});bad_record=bad.evaluate(bad.initial_vector(initial))['decision']
    mirror_rejection=bad_record['eligible_under_original_physical_gate_groups'] and not bad_record['eligible_under_physical_gates_including_mirror']
    degeneracy=make();data=degeneracy.problem.geometry(initial,t,theta,3,True);data['Xs']=data['T'].copy()
    deg=candidate_decision(degeneracy.problem,degeneracy.gate,initial,3.,data,lower,upper,degeneracy.cfg)
    degenerate_rejection=deg['mirror_polynomial_pass'] and not deg['regularity_screen_pass'] and not deg['eligible_under_physical_gates_including_mirror']
    failure_problem=_EpigraphArrayProblem();failure_problem.fail_after_calls=1
    failure=run_dense_epigraph(make(failure_problem),initial,artificial_inputs_only=True)
    retained=((failure.get('error') or {}).get('type')=='FloatingPointError'
        and failure['checkpoint']['best_physical_max_eta_point'] is not None)
    only=run_dense_epigraph(make(),initial,artificial_inputs_only=True,evaluate_only=True)
    passed=bool(shared and delta_reuse and error<3e-8 and split and mirror_rejection and degenerate_rejection
        and retained and only['solver']['minimize_invocation_count']==0)
    return {'schema':'dense-mirror-epigraph-targeted-array-development-v1','artificial_inputs_only':True,
        'research_geometry_evaluated_or_optimized':False,'shared_four_callbacks_one_geometry':shared,
        'delta_only_change_reuses_geometry':delta_reuse,'seven_group_directional_Jacobian_error':error,
        'physically_better_underbounded_trial_retained_separately':bool(split),
        'mirror_failure_rejects_cap_box_z_ball_strip_feasible_point':bool(mirror_rejection),
        'squared_row_zero_does_not_accept_degenerate_normal':bool(degenerate_rejection),
        'injected_error_preserves_physical_best':bool(retained),'evaluation_only_calls_no_optimizer':
            only['solver']['minimize_invocation_count']==0,'passed':passed}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    try:result=developer_check()
    except Exception as error:
        atomic_save(args.out,{'schema':'dense-mirror-epigraph-development-error-v1','passed':False,
            'source_files_sha256':implementation_hashes(),'error':{'type':type(error).__name__,'message':str(error)}})
        raise
    result['source_files_sha256']=implementation_hashes();atomic_save(args.out,result)
    print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
    if not result['passed']:raise SystemExit(1)


if __name__=='__main__':main()
