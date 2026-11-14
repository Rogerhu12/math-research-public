#!/usr/bin/env python3
"""Continue a curvature pool until its enforced rows recover feasibility.

The geometry, actual-curvature PSD rows, all full-grid gates, tolerances and
batched two-jet Jacobians are inherited unchanged. Only exchange scheduling
and the provenance of a previously learned row pool are new.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import time
from types import SimpleNamespace

import numpy as np
import scipy
from scipy.optimize import Bounds, LinearConstraint, NonlinearConstraint, minimize

from frame_collar_bvp import atomic_save
from frame_collar_residual_audit import digest
from frame_height_affine_gate import EvaluationBudgetReached, require_public_research_environment
from frame_metric_epigraph_exchange import PoolExchangeRequested
from frame_curvature_epigraph_exchange import (
    CurvatureExchangeObjective as PreviousObjective, GROUPS,
    configuration as previous_configuration, implementation_hashes as previous_hashes)

POLICY = 'exchange-only-after-current-pool-and-cap-box-regularity-restored-v1'


def implementation_hashes():
    result=previous_hashes()
    result[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


def upgrade_configuration(old=None):
    cfg=copy.deepcopy(previous_configuration() if old is None else old)
    legacy=cfg.pop('callback_metric_exchange_trigger_exact',None)
    cfg.update(exchange_callback_policy=POLICY,
        historical_unused_wide_metric_callback_trigger_exact=legacy,
        every_exchange_uses_actual_group_eligibility_tolerances=True,
        library_return_with_infeasible_pool_stops_without_claiming_full_feasibility=True,
        no_budget_or_geometric_gate_relaxation=True)
    return cfg


def configuration():
    return upgrade_configuration()


def pooled_feasibility(rows,pool,tolerances,decision):
    """Same-state enforced-row check; no tolerance enlargement or new geometry."""
    rows=np.asarray(rows,float); pool=np.asarray(pool,dtype=np.int64)
    tolerances=np.asarray(tolerances,float)
    if (rows.ndim!=3 or rows.shape[0]!=len(GROUPS) or tolerances.shape!=(len(GROUPS),)
            or not np.all(np.isfinite(rows)) or not np.all(np.isfinite(tolerances))
            or np.any(tolerances<0) or pool.ndim!=1 or not len(pool)
            or np.any(pool<0) or np.any(pool>=rows.size) or len(np.unique(pool))!=len(pool)):
        raise ValueError('finite eleven-group values, valid unique pool and original tolerances required')
    count=rows.shape[1]*rows.shape[2]
    group=pool//count; values=rows.reshape(-1)[pool]
    bad=values < -tolerances[group]
    groups={}
    for k,name in enumerate(GROUPS):
        present=group==k; selected=values[present]
        groups[name]={'enforced_count':int(np.count_nonzero(present)),
            'violating_count':int(np.count_nonzero(bad[present])),
            'minimum_row':None if not len(selected) else float(np.min(selected)),
            'actual_tolerance':float(tolerances[k])}
    cap=bool(decision['cap_and_box']['eligible_under_declared_numerical_gate_tolerances'])
    regular=bool(decision['regularity_screen_pass'])
    return {'schema':'same-state-enforced-curvature-pool-feasibility-v1',
        'pool_rows':int(len(pool)),'enforced_violating_rows':int(np.count_nonzero(bad)),
        'cap_and_box_pass':cap,'independent_regularity_pass':regular,
        'ready_for_exchange':bool(not np.any(bad) and cap and regular),
        'groups':groups,'uses_original_actual_tolerances':True,
        'not_a_whole_grid_feasibility_claim':True}


class FeasibleCurvatureExchangeObjective(PreviousObjective):
    def __init__(self,*args,**kwargs):
        if kwargs.get('cfg') is None: kwargs['cfg']=configuration()
        super().__init__(*args,**kwargs)
        if self.cfg.get('exchange_callback_policy')!=POLICY:
            raise ValueError('explicit pool-feasibility scheduling policy required')
        self.deferred_exchange_callbacks=0
        self.pooled_feasible_exchange_callbacks=0
        self.evaluation_definition.update(
            schema='pooled-feasibility-curvature-exchange-evaluation-v1',
            scheduling_policy=POLICY,
            source_files_sha256=implementation_hashes())
        self.evaluation_sha256=digest(self.evaluation_definition)
    def snapshot(self):
        result=super().snapshot()
        result.update(exchange_callback_policy=POLICY,
            deferred_exchange_callbacks=self.deferred_exchange_callbacks,
            pooled_feasible_exchange_callbacks=self.pooled_feasible_exchange_callbacks,
            callback_and_library_return_use_actual_group_tolerances=True)
        return result


def current_pool_status(objective,vector):
    record=objective.evaluate(vector)
    rows=objective.all_rows(vector)
    return pooled_feasibility(rows,objective.pool,objective.row_tolerances(),record['decision'])


def run_exchange(objective,initial,*,lambda_initial=None,artificial_inputs_only=False,evaluate_only=False):
    if not artificial_inputs_only:
        require_public_research_environment()
    elif objective.gate.kind!='artificial-array' and not evaluate_only:
        raise ValueError('artificial solver calls require the explicit array family')
    metadata={'method':'SLSQP with feasibility-controlled eleven-group row exchanges',
        'exchange_callback_policy':POLICY,
        'minimize_invocation_count':0,'total_major_iterations':0,
        'shared_maxiter':objective.cfg['maxiter'],
        'shared_max_physical_evaluations':objective.cfg['max_physical_evaluations'],
        'shared_optimization_seconds':objective.cfg['max_seconds'],
        'max_exchange_rounds':objective.cfg['max_exchange_rounds'],'rounds':[],
        'artificial_inputs_only':bool(artificial_inputs_only),'evaluate_only':bool(evaluate_only),
        'numpy_version':np.__version__,'scipy_version':scipy.__version__,
        'keep_feasible_not_passed_or_claimed':True,
        'all_eligibility_tests_are_whole_grid':True,
        'callback_and_library_return_use_original_actual_group_tolerances':True}
    def finish(status,error=None,budget=None):
        snap=objective.snapshot()
        if objective.checkpoint: objective.checkpoint(snap)
        return {'status':status,'error':error,'budget_message':budget,'solver':metadata,'checkpoint':snap,
            'selected_point':'best actual maximum curvature satisfying full fixed-metric and physical gates',
            'no_metric_parameter_or_height_reference_change':True}
    try:
        vector=objective.initial_vector(initial,lambda_initial)
        preflight=objective.evaluate(vector)
        if not preflight['decision']['eligible_under_all_declared_sampled_constraints']:
            return finish('initial-full-grid-fixed-metric-physical-or-curvature-bound-gate-failed')
        if not len(objective.pool): objective.initialize_pool(vector)
        metadata['initial_pool_rows']=len(objective.pool)
        objective.evaluate(vector); objective.active_derivatives(vector)
        metadata['new_initial_auxiliary_zeta']=float(vector[-1])
        metadata['new_initial_auxiliary_lambda']=float(Q(objective.cfg['curvature_scale_exact']))*float(vector[-1])
        if evaluate_only:
            return finish('evaluation-only-full-grid-batched-two-jets-and-learned-pool-no-solver')
        objective.begin_optimization()
        for round_index in range(int(objective.cfg['max_exchange_rounds'])):
            objective._wall()
            remaining=int(objective.cfg['maxiter'])-metadata['total_major_iterations']
            if remaining<=0: return finish('shared-major-iteration-budget-exit')
            rd={'round':round_index+1,'pool_version':objective.pool_version,'pool_rows':len(objective.pool),
                'initial_vector_exact':[str(Q.from_float(float(x))) for x in vector],
                'major_iterations':0,'exit_reason':None,'callback_observations':[]}
            metadata['rounds'].append(rd)
            def callback(x):
                rd['major_iterations']+=1; metadata['total_major_iterations']+=1
                objective.evaluate(x)
                _,_,detail=objective.missing_rows(x,callback_trigger=False)
                pooled=current_pool_status(objective,x)
                enough=rd['major_iterations']>=objective.cfg['minimum_major_iterations_before_exchange']
                exchange=bool(enough and detail['omitted_violating_count'] and pooled['ready_for_exchange'])
                defer=bool(enough and detail['omitted_violating_count'] and not pooled['ready_for_exchange'])
                if defer: objective.deferred_exchange_callbacks+=1
                if exchange: objective.pooled_feasible_exchange_callbacks+=1
                rd['callback_observations'].append({
                    'major_in_round':rd['major_iterations'],
                    'epigraph_evaluation':objective.evaluate(x)['epigraph_evaluation'],
                    'enforced_pool':pooled,'omitted_violating_count':detail['omitted_violating_count'],
                    'exchange_requested':exchange,'same_SLSQP_continues_to_restore_pool':defer})
                if exchange:
                    detail=dict(detail,pooled_feasibility_at_exchange=pooled)
                    raise PoolExchangeRequested(x,detail)
            try:
                metadata['minimize_invocation_count']+=1
                lower_zeta=float(Q(objective.cfg['curvature_lambda_min_exact']))/float(Q(objective.cfg['curvature_scale_exact']))
                result=minimize(objective.fun,vector,jac=objective.jac,method='SLSQP',
                    bounds=Bounds(np.r_[objective.lower,lower_zeta],np.r_[objective.upper,np.inf]),
                    constraints=[objective.cap_constraint(),objective.nonlinear_constraint()],
                    callback=callback,options={'maxiter':remaining,'ftol':objective.cfg['ftol'],'disp':False})
                vector=np.asarray(result.x,float).copy(); objective.evaluate(vector)
                rd['library_result']={k:(bool(getattr(result,k)) if k=='success' else int(getattr(result,k))
                    if k in ['status','nit','nfev','njev'] else float(getattr(result,k)) if k=='fun'
                    else str(getattr(result,k))) for k in ['success','status','message','nit','nfev','njev','fun'] if hasattr(result,k)}
                rd['exit_reason']='library-return'
                pooled=current_pool_status(objective,vector)
                _,_,detail=objective.missing_rows(vector,callback_trigger=False)
                rd['pooled_feasibility_at_library_return']=pooled
                rd['full_grid_separation']=detail
                if not pooled['ready_for_exchange']:
                    return finish('library-return-before-enforced-pool-feasibility-restored')
                if not detail['omitted_violating_count']:
                    return finish('pooled-feasibility-exchange-library-returned-no-omitted-violating-rows')
                exchange=PoolExchangeRequested(vector,dict(detail,pooled_feasibility_at_exchange=pooled))
            except PoolExchangeRequested as error:
                exchange=error; vector=error.vector
                rd['exit_reason']='pooled-feasible-whole-grid-omitted-rows-exchange-request'
            rd['full_grid_separation']=exchange.reason
            if round_index+1>=objective.cfg['max_exchange_rounds']:
                return finish('exchange-round-limit-with-missing-eleven-group-rows-recorded')
            added,detail=objective.expand_pool(vector,'pooled-feasible-exact-tolerance-omitted-rows')
            rd['pool_addition']=added; rd['exact_tolerance_missing_summary']=detail
            if added is None: return finish('row-pool-capacity-or-no-new-row-stop')
            scale=float(Q(objective.cfg['curvature_scale_exact']))
            raw_lambda=float(vector[-1])*scale
            data=objective.physical_geometry(vector[:-1])
            maximum=float(np.max(data['curvature']['maximum_absolute_by_point']))
            next_lambda=max(raw_lambda,maximum+(1+maximum)*float(Q(objective.cfg['curvature_initial_margin_exact'])),
                2*float(Q(objective.cfg['curvature_lambda_min_exact'])))
            rd['next_auxiliary_initialization']={'old_raw_lambda':raw_lambda,'new_lambda':next_lambda,
                'physical_coefficients_unchanged':True,'old_decision_and_failure_retained':True,
                'rule':'unchanged explicit max(old raw lambda, sampled curvature plus declared margin, 2*lambda_min)'}
            vector=vector.copy(); vector[-1]=next_lambda/scale
            if objective.checkpoint: objective.checkpoint(objective.snapshot())
        return finish('exchange-round-budget-exit')
    except EvaluationBudgetReached as error:
        return finish('shared-curvature-exchange-budget-exit',budget=str(error))
    except Exception as error:
        return finish('curvature-objective-or-solver-error',error={'type':type(error).__name__,'message':str(error)})


class _SchedulingToy:
    """Two scalars only: min lambda, 1-x^2>=0, .8-x>=0, lambda+x-2>=0."""
    def __init__(self):
        self.n=1; self.lower=np.array([-2.]); self.upper=np.array([2.])
        self.cfg=configuration(); self.cfg.update(curvature_scale_exact='1',maxiter=30,
            max_physical_evaluations=100,max_seconds=10.,max_exchange_rounds=5)
        self.gate=SimpleNamespace(kind='artificial-array'); self.checkpoint=None
        self.pool=np.array([0,16],dtype=np.int64); self.pool_version=1
        self.started=time.monotonic(); self.optimization_started=None
        self.epigraph_evaluations=0; self.physical_evaluations=0
        self.last_vector=None; self.last_x=None; self.record=None; self.best=None
        self.deferred_exchange_callbacks=0; self.pooled_feasible_exchange_callbacks=0
    def _wall(self):
        if time.monotonic()-self.started>10: raise EvaluationBudgetReached('artificial scheduling clock')
    def initial_vector(self,initial,lambda_initial=None):
        return np.r_[initial,1.6 if lambda_initial is None else lambda_initial]
    def row_tolerances(self):
        return np.full(len(GROUPS),1e-9)
    def rows(self,vector):
        x,lam=vector; a=np.ones((11,1,2)); a.flat[0]=1-x*x; a.flat[2]=.8-x; a.flat[16]=lam+x-2
        return a
    def evaluate(self,vector):
        v=np.asarray(vector,float)
        if self.last_vector is not None and np.array_equal(v,self.last_vector): return self.record
        self._wall(); self.epigraph_evaluations+=1
        if self.last_x is None or float(v[0])!=self.last_x:
            self.physical_evaluations+=1; self.last_x=float(v[0])
        rows=self.rows(v); physical=bool(rows.flat[0]>=-1e-9 and rows.flat[2]>=-1e-9)
        decision={'eligible_under_all_declared_sampled_constraints':bool(np.all(rows>=-1e-9)),
            'eligible_under_fixed_metric_and_physical_gates':physical,
            'cap_and_box':{'eligible_under_declared_numerical_gate_tolerances':bool(-2<=v[0]<=2)},
            'regularity_screen_pass':True,'direct_maximum_absolute_principal_curvature':2-float(v[0])}
        self.record={'epigraph_evaluation':self.epigraph_evaluations,'decision':decision}
        if physical and (self.best is None or 2-v[0]<self.best['curvature']):
            self.best={'x':float(v[0]),'curvature':2-float(v[0])}
        self.last_vector=v.copy(); return self.record
    def all_rows(self,vector):
        self.evaluate(vector); return self.rows(vector)
    def active_derivatives(self,vector):
        return self.constraint_jac(vector)
    def begin_optimization(self):
        self.optimization_started=time.monotonic()
    def fun(self,vector):
        self.evaluate(vector); return float(vector[-1])
    def jac(self,vector):
        self.evaluate(vector); return np.array([0.,1.])
    def cap_constraint(self):
        return LinearConstraint(np.zeros((1,2)),[-1.],[np.inf])
    def constraint_fun(self,vector):
        return self.all_rows(vector).reshape(-1)[self.pool]
    def constraint_jac(self,vector):
        self.evaluate(vector); j=np.zeros((22,2))
        j[0]=[-2*vector[0],0]; j[2]=[-1,0]; j[16]=[1,1]
        return j[self.pool]
    def nonlinear_constraint(self):
        return NonlinearConstraint(self.constraint_fun,0,np.inf,jac=self.constraint_jac)
    def missing_rows(self,vector,callback_trigger=False):
        if callback_trigger: raise AssertionError('wide callback trigger must never be requested')
        rows=self.all_rows(vector); missing=rows < -self.row_tolerances()[:,None,None]
        missing.reshape(-1)[self.pool]=False
        return rows,missing,{'omitted_violating_count':int(np.count_nonzero(missing)),
            'callback_trigger_not_an_eligibility_tolerance':False}
    def expand_pool(self,vector,reason):
        rows,missing,detail=self.missing_rows(vector)
        new=np.flatnonzero(missing.reshape(-1))
        if not len(new): return None,detail
        self.pool=np.unique(np.r_[self.pool,new]); self.pool_version+=1
        return {'row_count':len(self.pool),'reason':reason,'added_row_indices':new.tolist()},detail
    def physical_geometry(self,state):
        return {'curvature':{'maximum_absolute_by_point':np.array([2-float(state[0])])}}
    def snapshot(self):
        return {'best_physical_curvature_point':copy.deepcopy(self.best),
            'epigraph_vector_evaluations':self.epigraph_evaluations,
            'physical_geometry_evaluations':self.physical_evaluations,
            'deferred_exchange_callbacks':self.deferred_exchange_callbacks,
            'pooled_feasible_exchange_callbacks':self.pooled_feasible_exchange_callbacks}


def developer_check():
    rows=np.ones((11,2,4)); tolerances=np.full(11,1e-9)
    pool=np.array([0,8,16,24,32,40,48,56,64,72,80])
    decision={'cap_and_box':{'eligible_under_declared_numerical_gate_tolerances':True},
        'regularity_screen_pass':True}
    rows.flat[0]=-2e-8; rows.flat[1]=-5e-9
    bad=pooled_feasibility(rows,pool,tolerances,decision)
    rows.flat[0]=0.
    good=pooled_feasibility(rows,pool,tolerances,decision)
    strict_omitted=bool(rows.flat[1]<-tolerances[0] and abs(rows.flat[1])<1e-5)
    capbad=copy.deepcopy(decision); capbad['cap_and_box']['eligible_under_declared_numerical_gate_tolerances']=False
    blocked=pooled_feasibility(rows,pool,tolerances,capbad)
    toy=_SchedulingToy()
    result=run_exchange(toy,np.array([.5]),lambda_initial=1.6,artificial_inputs_only=True)
    rounds=result['solver']['rounds']
    deferred=any(o['same_SLSQP_continues_to_restore_pool'] for r in rounds for o in r['callback_observations'])
    valid_exchanges=all(o['enforced_pool']['ready_for_exchange'] for r in rounds for o in r['callback_observations'] if o['exchange_requested'])
    best=toy.best
    passed=bool(not bad['ready_for_exchange'] and good['ready_for_exchange'] and strict_omitted
        and not blocked['ready_for_exchange'] and deferred and valid_exchanges and result['error'] is None
        and best is not None and abs(best['x']-.8)<2e-7
        and result['solver']['minimize_invocation_count']>=2)
    return {'schema':'curvature-pooled-feasibility-scheduling-development-v1',
        'artificial_inputs_only':True,'research_geometry_evaluated_or_optimized':False,
        'infeasible_enforced_pool_not_ready':not bad['ready_for_exchange'],
        'actual_tolerance_detects_omitted_rows_between_1e_minus9_and_1e_minus5':strict_omitted,
        'cap_box_failure_blocks_exchange':not blocked['ready_for_exchange'],
        'same_SLSQP_continues_during_enforced_pool_violation':deferred,
        'every_callback_exchange_had_feasible_enforced_pool':valid_exchanges,
        'two_scalar_scheduling_result':result,'two_scalar_best':best,'passed':passed}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check-only',action='store_true',required=True)
    p.add_argument('--out',type=Path,required=True); a=p.parse_args()
    result=developer_check(); result['source_files_sha256']=implementation_hashes()
    atomic_save(a.out,result)
    print(json.dumps({'out':str(a.out),'passed':result['passed']}),flush=True)
    if not result['passed']: raise SystemExit(1)


if __name__=='__main__':
    main()
