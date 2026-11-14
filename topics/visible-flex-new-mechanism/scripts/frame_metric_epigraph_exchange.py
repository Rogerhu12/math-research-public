#!/usr/bin/env python3
"""Full-grid minimax gates with a finite exchanged SLSQP row pool.

The physical field, fixed metric, and height reference are unchanged. Every
trial is judged on the whole declared grid. Only the nonlinear Jacobian sent
to SLSQP is reduced. Missing violated rows cause an explicit pool exchange;
they never turn a failed whole-grid decision into an eligible state.
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
import scipy
from scipy.optimize import Bounds,minimize

from frame_collar_bvp import atomic_save
from frame_collar_residual_audit import digest
from frame_height_affine_gate import HeightAffineGate,EvaluationBudgetReached,require_public_research_environment
from frame_metric_epigraph import metric_rows,geometry_values,_EpigraphArrayProblem
from frame_metric_epigraph_dense import (DenseMirrorEpigraphObjective,configuration as dense_configuration,
    candidate_decision as dense_decision,mirror_values,implementation_hashes as dense_hashes)

GROUPS=('metric_minus','metric_plus','signed_z','ball','strip_plus','strip_minus','mirror_pair')


def implementation_hashes():
    out=dense_hashes();out[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();return out


def configuration():
    out=dense_configuration()
    out.update(hard_strip_half_width_exact='38999/100000',outer_strip_half_width_exact='39/100',
        strip_inner_margin_exact='1/100000',max_exchange_rounds=6,max_pool_rows=12000,
        initial_per_radial_group=[2,2,1,1,1,1,1],exchange_per_radial_group=2,
        exchange_global_per_group=32,minimum_major_iterations_before_exchange=2,
        callback_metric_exchange_trigger_exact='1/100000',
        value_Jacobian_replay_relative_tolerance=5e-12,
        optimization_seconds_exclude_declared_initialization=True,
        full_grid_values_checked_at_every_trial=True,
        final_selection='best physical true eta satisfying all full-grid inner-strip and mirror gates',
        missing_row_violations_never_accepted_as_auxiliary_feasibility=True,
        nonlinear_pool_size_constant_inside_each_SLSQP_invocation=True)
    return out


def candidate_decision(problem,gate,state,delta,data,lower,upper,cfg):
    out=dense_decision(problem,gate,state,delta,data,lower,upper,cfg)
    outer=float(Q(cfg['outer_strip_half_width_exact']))
    out.update(outer_strip_half_width_exact=cfg['outer_strip_half_width_exact'],
        outer_strip_pass=bool(1-out['maximum_absolute_y']/outer>=-cfg['shape_constraint_tolerance']),
        outer_strip_absolute_margin=outer-out['maximum_absolute_y'],
        inner_strip_absolute_margin=float(Q(cfg['hard_strip_half_width_exact']))-out['maximum_absolute_y'],
        strip_inner_margin_exact=cfg['strip_inner_margin_exact'],
        physical_selection_uses_the_inner_not_only_outer_strip=True,
        decision_uses_every_declared_radial_angular_point_not_only_the_QP_pool=True)
    return out


class PoolExchangeRequested(RuntimeError):
    def __init__(self,vector,reason):
        super().__init__('omitted full-grid constraint rows require an explicit pool exchange')
        self.vector=np.asarray(vector,float).copy();self.reason=copy.deepcopy(reason)


class ExchangeEpigraphObjective(DenseMirrorEpigraphObjective):
    def __init__(self,*args,**kwargs):
        if kwargs.get('cfg') is None:kwargs['cfg']=configuration()
        super().__init__(*args,**kwargs)
        self.total_started=self.started;self.optimization_started=None
        self.pool=np.empty(0,dtype=np.int64);self.pool_version=0;self.pool_history=[]
        self.derivative_cache=None;self.jacobian_geometry_evaluations=0
        self.value_geometry_seconds=0.;self.jacobian_geometry_seconds=0.;self.pool_jacobian_seconds=0.
        self.maximum_retained_derivative_bytes=0;self.maximum_value_Jacobian_replay_difference=0.
        self.geometry_cache=None
        if not 0<Q(self.cfg['hard_strip_half_width_exact'])<Q(self.cfg['outer_strip_half_width_exact']):
            raise ValueError('the new inner strip must be positive and strictly inside the old outer strip')
        if Q(self.cfg['outer_strip_half_width_exact'])-Q(self.cfg['hard_strip_half_width_exact'])!=Q(self.cfg['strip_inner_margin_exact']):
            raise ValueError('exact strip-margin identity failed')
        if (len(self.cfg['initial_per_radial_group'])!=7 or min(self.cfg['initial_per_radial_group'])<1
                or self.cfg['max_pool_rows']<7 or self.cfg['max_exchange_rounds']<1):
            raise ValueError('finite positive row-pool configuration required')
        self.evaluation_definition.update(schema='full-grid-values-exchanged-QP-rows-v1',
            source_files_sha256=implementation_hashes(),
            complete_value_grid_is_fixed_during_all_rounds=True,
            row_pool_is_solver_bookkeeping_not_physical_state=True,
            only_selected_point_Jacobians_are_retained=True,
            full_geometry_Jacobian_is_transient_not_a_full_constraint_Jacobian=True,
            value_and_Jacobian_geometry_calls_have_separate_actual_counters=True,
            initialization_and_optimization_wall_times_are_reported_separately=True)
        self.evaluation_sha256=digest(self.evaluation_definition)

    def _wall(self):
        if self.optimization_started is not None and time.monotonic()-self.optimization_started>=self.cfg['max_seconds']:
            raise EvaluationBudgetReached('shared exchange optimization wall budget reached; whole-grid best retained')

    def begin_optimization(self):
        if self.optimization_started is not None:raise ValueError('the shared optimization clock cannot be restarted')
        self.optimization_started=time.monotonic();self.last_checkpoint=self.optimization_started

    def physical_geometry(self,state):
        state=np.asarray(state,float)
        if state.shape!=(self.n,) or not np.all(np.isfinite(state)):raise ValueError('finite complete physical state required')
        self.assert_context(state);self._wall()
        if self.geometry_cache is not None and np.array_equal(state,self.geometry_cache['state']):return self.geometry_cache
        if self.geometry_evaluations>=self.cfg['max_physical_evaluations']:
            raise EvaluationBudgetReached('shared full-grid physical-state evaluation budget reached')
        before=time.monotonic();data=self.problem.geometry(state,self.radial,self.theta,self.order,jacobian=False)
        self.value_geometry_seconds+=time.monotonic()-before
        expected=(len(self.radial),len(self.theta),3)
        for key in ['X','Xs','T']:
            if np.asarray(data[key]).shape!=expected or not np.all(np.isfinite(data[key])):
                raise FloatingPointError('finite complete whole-grid geometry required: '+key)
        values=geometry_values(data);mirror=mirror_values(data,float(Q(self.cfg['mirror_target_exact'])))
        cache={key:np.asarray(data[key]).copy() for key in ['X','Xs','T','center']}
        for key in ['Xt','Xss','Xst','Xtt','Ts','Tss','Ttheta','primitive']:
            if key in data:cache[key]=np.asarray(data[key]).copy()
        for key in ['metric','height']:
            if key in data:cache[key]={name:np.asarray(value).copy() for name,value in data[key].items()}
        cache.update(state=state.copy(),radial=self.radial,theta=self.theta,e=values['e'],f=values['f'],eta=values['eta'],
            mirror_polynomial=mirror['polynomial'])
        self.geometry_evaluations+=1;cache['geometry_evaluation']=self.geometry_evaluations
        for value in cache.values():
            if isinstance(value,np.ndarray):value.setflags(write=False)
            elif isinstance(value,dict):
                for item in value.values():
                    if isinstance(item,np.ndarray):item.setflags(write=False)
        self.geometry_cache=cache;self.derivative_cache=None
        self.maximum_geometry_cache_array_bytes=max(self.maximum_geometry_cache_array_bytes,
            sum(v.nbytes if isinstance(v,np.ndarray) else
                sum(x.nbytes for x in v.values() if isinstance(x,np.ndarray)) if isinstance(v,dict) else 0
                for v in cache.values()))
        return cache

    def evaluate(self,vector):
        vector=np.asarray(vector,float)
        if vector.shape!=(self.n+1,) or not np.all(np.isfinite(vector)):raise ValueError('physical vector and finite auxiliary delta required')
        metric_rows(np.array([0.]),np.array([0.]),vector[-1]);self.assert_context(vector[:-1]);self._wall()
        if (self.epigraph_cache is not None and np.array_equal(vector,self.epigraph_cache['vector'])
                and self.geometry_cache is not None and np.array_equal(vector[:-1],self.geometry_cache['state'])):
            return self.epigraph_cache['record']
        data=self.physical_geometry(vector[:-1]);decision=candidate_decision(self.problem,self.gate,vector[:-1],
            vector[-1],data,self.lower,self.upper,self.cfg)
        rows=self.rows_from_geometry(data,vector[-1]);violating=rows < -self.row_tolerances()[:,None,None]
        omitted=violating.copy();omitted.reshape(-1)[self.pool]=False
        separation={'all_full_grid_violating_rows':int(np.count_nonzero(violating)),
            'omitted_violating_rows':int(np.count_nonzero(omitted)),
            'group_counts':{name:{'whole_grid':int(np.count_nonzero(violating[g])),
                'omitted':int(np.count_nonzero(omitted[g]))} for g,name in enumerate(GROUPS)}}
        now=time.monotonic();self.epigraph_evaluations+=1
        record={'epigraph_evaluation':self.epigraph_evaluations,'physical_geometry_evaluation':data['geometry_evaluation'],
            'elapsed_seconds':now-self.total_started,'optimization_elapsed_seconds':None if self.optimization_started is None else now-self.optimization_started,
            'phase':'initialization' if self.optimization_started is None else 'optimization',
            'pool_version':self.pool_version,'pool_rows':len(self.pool),
            'whole_grid_and_pool_separation_at_this_same_trial':separation,'decision':decision}
        point={'vector':vector.copy(),'record':copy.deepcopy(record)}
        if self.best_trial is None or vector[-1]<self.best_trial['vector'][-1]:self.best_trial=point
        def smaller(old):
            return old is None or decision['direct_max_eta']<old['record']['decision']['direct_max_eta'] or (
                decision['direct_max_eta']==old['record']['decision']['direct_max_eta'] and vector[-1]<old['vector'][-1])
        if decision['eligible_under_physical_gates_including_mirror'] and smaller(self.best_physical):self.best_physical=point
        if decision['eligible_under_all_declared_sampled_constraints']:
            if self.best_delta is None or vector[-1]<self.best_delta['vector'][-1]:self.best_delta=point
            if smaller(self.best_eta):self.best_eta=point
        rows.setflags(write=False)
        self.history.append(record);self.epigraph_cache={'vector':vector.copy(),'record':copy.deepcopy(record),'rows':rows}
        due=(self.geometry_evaluations-self.last_checkpoint_geometry>=self.cfg['checkpoint_physical_evaluations']
            or now-self.last_checkpoint>=self.cfg['checkpoint_seconds'])
        if self.checkpoint is not None and due:
            self.checkpoint(self.snapshot());self.last_checkpoint=now;self.last_checkpoint_geometry=self.geometry_evaluations
        self._wall();return record

    def rows_from_geometry(self,data,delta):
        cm,cp=metric_rows(data['e'],data['f'],delta);X=data['X']
        p=float(Q(self.cfg['hard_strip_half_width_exact']));R=float(Q(self.cfg['hard_ball_radius_exact']))
        return np.stack([cm,cp,self.gate.side*X[...,2]-float(Q(self.cfg['minimum_signed_height_exact'])),
            1-np.sum(X*X,axis=-1)/R**2,1-X[...,1]/p,1+X[...,1]/p,data['mirror_polynomial']])

    def all_rows(self,vector):
        self.evaluate(vector);return self.epigraph_cache['rows']

    def row_tolerances(self):
        c=self.cfg
        return np.asarray([c['metric_row_tolerance']]*2+[c['signed_height_tolerance']]+[c['shape_constraint_tolerance']]*3+[c['mirror_polynomial_tolerance']])

    def missing_rows(self,vector,*,callback_trigger=False):
        rows=self.all_rows(vector);limits=self.row_tolerances().copy()
        if callback_trigger:limits[:2]=np.maximum(limits[:2],float(Q(self.cfg['callback_metric_exchange_trigger_exact'])))
        missing=rows < -limits[:,None,None]
        missing.reshape(-1)[self.pool]=False
        return rows,missing,{'callback_trigger_not_an_eligibility_tolerance':bool(callback_trigger),
            'omitted_violating_count':int(np.count_nonzero(missing)),
            'groups':{name:{'omitted_violating_count':int(np.count_nonzero(missing[g])),
                'whole_grid_minimum_row':float(np.min(rows[g])),
                'trigger_tolerance':float(limits[g]),'actual_eligibility_tolerance':float(self.row_tolerances()[g])}
                for g,name in enumerate(GROUPS)}}

    def set_pool(self,indices,reason):
        total=7*len(self.radial)*len(self.theta);indices=np.asarray(sorted(set(int(x) for x in indices)),dtype=np.int64)
        if len(indices)==0 or np.any(indices<0) or np.any(indices>=total):raise ValueError('valid nonempty finite row pool required')
        if len(indices)>self.cfg['max_pool_rows']:raise ValueError('declared row-pool capacity exceeded')
        if len(self.pool) and not set(self.pool)<=set(indices):raise ValueError('previous enforced rows cannot be silently removed')
        old=set(self.pool);self.pool=indices;self.pool.setflags(write=False);self.pool_version+=1
        self.derivative_cache=None;self.epigraph_cache=None
        rec={'version':self.pool_version,'row_count':len(indices),'total_full_grid_rows':total,
            'group_order':list(GROUPS),'flat_index_rule':'group*(Nr*Ntheta)+radial_index*Ntheta+theta_index',
            'row_indices':[int(x) for x in indices],'row_indices_sha256':digest([int(x) for x in indices]),
            'added_row_indices':[int(x) for x in indices if int(x) not in old],'reason':copy.deepcopy(reason)}
        self.pool_history.append(rec);return rec

    def initialize_pool(self,vector):
        rows=self.all_rows(vector);Nr,Nt=rows.shape[1:];chosen=[]
        for group in range(7):
            take=min(Nt,int(self.cfg['initial_per_radial_group'][group]))
            order=np.argsort(rows[group],axis=1,kind='stable')[:,:take]
            chosen.extend((group*Nr*Nt+np.arange(Nr)[:,None]*Nt+order).ravel().tolist())
        return self.set_pool(chosen,{'kind':'initial-most-restrictive-angular-rows-in-every-radial-slice',
            'per_radial_group':list(self.cfg['initial_per_radial_group'])})

    def expand_pool(self,vector,reason):
        rows,missing,detail=self.missing_rows(vector);Nr,Nt=rows.shape[1:];chosen=set(int(x) for x in self.pool)
        for group in range(7):
            for ir in range(Nr):
                ids=np.flatnonzero(missing[group,ir])
                if len(ids):
                    ids=ids[np.argsort(rows[group,ir,ids],kind='stable')[:self.cfg['exchange_per_radial_group']]]
                    chosen.update(int(group*Nr*Nt+ir*Nt+j) for j in ids)
            ids=np.flatnonzero(missing[group].ravel())
            if len(ids):
                ids=ids[np.argsort(rows[group].ravel()[ids],kind='stable')[:self.cfg['exchange_global_per_group']]]
                chosen.update(int(group*Nr*Nt+j) for j in ids)
        if len(chosen)==len(self.pool):return None,detail
        if len(chosen)>self.cfg['max_pool_rows']:
            detail['pool_capacity_would_be_exceeded']=True;detail['proposed_pool_rows']=len(chosen);return None,detail
        record=self.set_pool(chosen,{'kind':reason,'full_grid_violation_summary':detail,
            'all_violations_recorded_but_only_declared_worst_rows_per_slice_added':True})
        after=missing.reshape(-1).copy();after[self.pool]=False
        record['omitted_violations_after_this_addition']=int(np.count_nonzero(after))
        return record,detail

    def active_derivatives(self,vector):
        self.evaluate(vector)
        if len(self.pool)==0:raise ValueError('initialize the fixed row pool before requesting its Jacobian')
        if self.derivative_cache is not None and self.derivative_cache['pool_version']==self.pool_version and np.array_equal(vector[:-1],self.derivative_cache['state']):
            return self.derivative_cache
        self._wall();before=time.monotonic()
        data=self.problem.geometry(vector[:-1],self.radial,self.theta,self.order,jacobian=True)
        self.jacobian_geometry_seconds+=time.monotonic()-before;self.jacobian_geometry_evaluations+=1
        count=len(self.radial)*len(self.theta);expected=(len(self.radial),len(self.theta),3,self.n)
        maximum=0.;scale=1.
        for key in ['X','Xs','T','center']:
            maximum=max(maximum,float(np.max(abs(np.asarray(data[key])-self.geometry_cache[key]))))
            scale=max(scale,float(np.max(abs(self.geometry_cache[key]))))
        self.maximum_value_Jacobian_replay_difference=max(self.maximum_value_Jacobian_replay_difference,maximum)
        if maximum>self.cfg['value_Jacobian_replay_relative_tolerance']*scale:
            raise ArithmeticError('same-state value and analytic-Jacobian geometry replay differs beyond declared floating comparison')
        for key in ['jac_X','jac_Xs','jac_T']:
            if np.asarray(data[key]).shape!=expected or not np.all(np.isfinite(data[key])):
                raise FloatingPointError('finite complete analytic geometry Jacobian required')
        points=np.unique(self.pool%count)
        X,U,T=(np.asarray(data[k]).reshape(count,3)[points] for k in ['X','Xs','T'])
        JX,JU,JT=(np.asarray(data[k]).reshape(count,3,self.n)[points] for k in ['jac_X','jac_Xs','jac_T'])
        de=2*np.einsum('ic,icn->in',U,JU)
        df=np.einsum('ic,icn->in',T,JU)+np.einsum('ic,icn->in',U,JT)
        W=np.cross(U,T);z=X[:,2];area2=np.sum(W*W,axis=1);D=z[:,None]**2*W
        D[:,2]-=float(Q(self.cfg['mirror_target_exact']))**2*W[:,2]
        dm=2*z[:,None]*area2[:,None]*JX[:,2,:]
        dm+=2*np.einsum('ic,icn->in',np.cross(T,D),JU)+2*np.einsum('ic,icn->in',np.cross(D,U),JT)
        cache={'state':np.asarray(vector[:-1]).copy(),'pool_version':self.pool_version,'points':points,
            'pool_points':np.searchsorted(points,self.pool%count),'de':de,'df':df,'jac_X':JX,'mirror_jac':dm}
        del data,JU,JT
        if any(not np.all(np.isfinite(x)) for x in cache.values() if isinstance(x,np.ndarray)):
            raise FloatingPointError('nonfinite selected-row derivative')
        for x in cache.values():
            if isinstance(x,np.ndarray):x.setflags(write=False)
        self.derivative_cache=cache
        self.maximum_retained_derivative_bytes=max(self.maximum_retained_derivative_bytes,
            sum(x.nbytes for x in cache.values() if isinstance(x,np.ndarray)))
        self._wall();return cache

    def constraint_fun(self,vector):return self.all_rows(vector).reshape(-1)[self.pool]

    def constraint_jac(self,vector):
        before=time.monotonic();d=self.active_derivatives(vector);data=self.geometry_cache
        count=data['e'].size;groups=self.pool//count;pp=d['pool_points'];points=self.pool%count
        f=data['f'].ravel()[points];delta=float(vector[-1]);J=np.zeros((len(self.pool),self.n+1))
        p=float(Q(self.cfg['hard_strip_half_width_exact']));R=float(Q(self.cfg['hard_ball_radius_exact']))
        for group in range(7):
            mask=groups==group;i=pp[mask]
            if group<2:
                J[mask,:self.n]=((-1 if group==0 else 1)*d['de'][i]-(2*f[mask]/delta)[:,None]*d['df'][i])
                J[mask,-1]=1+(f[mask]/delta)**2
            elif group==2:J[mask,:self.n]=self.gate.side*d['jac_X'][i,2,:]
            elif group==3:
                X=data['X'].reshape(count,3)[points[mask]]
                J[mask,:self.n]=-2*np.einsum('ic,icn->in',X,d['jac_X'][i])/R**2
            elif group==4:J[mask,:self.n]=-d['jac_X'][i,1,:]/p
            elif group==5:J[mask,:self.n]=d['jac_X'][i,1,:]/p
            else:J[mask,:self.n]=d['mirror_jac'][i]
        if not np.all(np.isfinite(J)):raise FloatingPointError('nonfinite exchanged constraint Jacobian')
        self.maximum_constraint_Jacobian_bytes=max(self.maximum_constraint_Jacobian_bytes,J.nbytes)
        self.pool_jacobian_seconds+=time.monotonic()-before;return J

    def snapshot(self):
        out=super().snapshot();now=time.monotonic()
        out.update(schema='whole-grid-physical-best-with-exchanged-row-pool-v1',
            total_elapsed_seconds=now-self.total_started,
            initialization_elapsed_seconds=(now-self.total_started if self.optimization_started is None else self.optimization_started-self.total_started),
            optimization_elapsed_seconds=None if self.optimization_started is None else now-self.optimization_started,
            jacobian_geometry_evaluations=self.jacobian_geometry_evaluations,
            value_geometry_seconds=self.value_geometry_seconds,jacobian_geometry_seconds=self.jacobian_geometry_seconds,
            pool_Jacobian_including_refresh_seconds=self.pool_jacobian_seconds,
            maximum_retained_selected_derivative_bytes=self.maximum_retained_derivative_bytes,
            maximum_value_Jacobian_replay_difference=self.maximum_value_Jacobian_replay_difference,
            active_row_pool_history=copy.deepcopy(self.pool_history),
            no_full_grid_constraint_Jacobian_was_formed=True,
            full_geometry_Jacobian_transient_peak_not_claimed_small=True,
            all_selected_physical_best_decisions_use_the_complete_grid=True)
        return out


def run_exchange(objective,initial,*,artificial_inputs_only=False,evaluate_only=False):
    if not artificial_inputs_only:require_public_research_environment()
    elif objective.gate.kind!='artificial-array' and not evaluate_only:
        raise ValueError('artificial solver calls are restricted to explicit array problems')
    metadata={'method':'SLSQP with explicit finite-row exchanges','minimize_invocation_count':0,
        'total_major_iterations':0,'shared_maxiter':objective.cfg['maxiter'],
        'shared_max_physical_evaluations':objective.cfg['max_physical_evaluations'],
        'shared_optimization_seconds':objective.cfg['max_seconds'],'max_exchange_rounds':objective.cfg['max_exchange_rounds'],
        'rounds':[],'artificial_inputs_only':bool(artificial_inputs_only),'evaluate_only':bool(evaluate_only),
        'numpy_version':np.__version__,'scipy_version':scipy.__version__,
        'keep_feasible_not_passed_or_claimed':True,'all_eligibility_tests_are_whole_grid':True}
    def finish(status,error=None,budget=None):
        snap=objective.snapshot()
        if objective.checkpoint:objective.checkpoint(snap)
        return {'status':status,'error':error,'budget_message':budget,'solver':metadata,'checkpoint':snap,
            'selected_point':'best full-grid inner-strip/physical/mirror actual eta',
            'no_metric_parameter_or_height_reference_change':True}
    try:
        vector=objective.initial_vector(initial);objective.evaluate(vector)
        if not len(objective.pool):objective.initialize_pool(vector)
        objective.evaluate(vector);objective.active_derivatives(vector)
        metadata['new_initial_auxiliary_delta']=float(vector[-1])
        metadata['initial_all_physical_gates_pass']=objective.evaluate(vector)['decision']['eligible_under_physical_gates_including_mirror']
        metadata['infeasible_inner_strip_start_is_not_labeled_eligible']=True
        if evaluate_only:return finish('evaluation-only-full-grid-and-pooled-Jacobian-no-solver')
        objective.begin_optimization()
        for round_index in range(int(objective.cfg['max_exchange_rounds'])):
            objective._wall();remaining=int(objective.cfg['maxiter'])-metadata['total_major_iterations']
            if remaining<=0:return finish('shared-major-iteration-budget-exit')
            rd={'round':round_index+1,'pool_version':objective.pool_version,'pool_rows':len(objective.pool),
                'initial_vector_exact':[str(Q.from_float(float(x))) for x in vector],
                'major_iterations':0,'exit_reason':None}
            metadata['rounds'].append(rd);exchange=None;result=None
            def callback(x):
                rd['major_iterations']+=1;metadata['total_major_iterations']+=1
                objective.evaluate(x)
                _,_,missing=objective.missing_rows(x,callback_trigger=True)
                if (rd['major_iterations']>=objective.cfg['minimum_major_iterations_before_exchange']
                        and missing['omitted_violating_count']):
                    raise PoolExchangeRequested(x,missing)
            try:
                metadata['minimize_invocation_count']+=1
                result=minimize(objective.fun,vector,jac=objective.jac,method='SLSQP',
                    bounds=Bounds(np.r_[objective.lower,float(Q(objective.cfg['delta_min_exact']))],np.r_[objective.upper,np.inf]),
                    constraints=[objective.cap_constraint(),objective.nonlinear_constraint()],callback=callback,
                    options={'maxiter':remaining,'ftol':objective.cfg['ftol'],'disp':False})
                vector=np.asarray(result.x,float).copy();objective.evaluate(vector)
                rd['library_result']={k:(bool(getattr(result,k)) if k=='success' else int(getattr(result,k)) if k in ['status','nit','nfev','njev']
                    else float(getattr(result,k)) if k=='fun' else str(getattr(result,k)))
                    for k in ['success','status','message','nit','nfev','njev','fun'] if hasattr(result,k)}
                rd['exit_reason']='library-return';_,_,missing=objective.missing_rows(vector)
                if not missing['omitted_violating_count']:
                    rd['full_grid_separation']=missing
                    return finish('exchange-library-returned-no-omitted-violating-rows')
                exchange=PoolExchangeRequested(vector,missing)
            except PoolExchangeRequested as error:
                exchange=error;vector=error.vector;rd['exit_reason']='whole-grid-omitted-rows-exchange-request'
            rd['full_grid_separation']=exchange.reason
            if round_index+1>=objective.cfg['max_exchange_rounds']:
                return finish('exchange-round-limit-with-missing-rows-recorded')
            added,detail=objective.expand_pool(vector,'callback-or-library-return-missing-whole-grid-rows')
            rd['pool_addition']=added;rd['exact_tolerance_missing_summary']=detail
            if added is None:return finish('row-pool-capacity-or-no-new-row-stop')
            raw_delta=float(vector[-1]);data=objective.physical_geometry(vector[:-1]);eta=float(np.max(data['eta']))
            next_delta=max(raw_delta,eta+float(Q(objective.cfg['initial_delta_margin_exact']))*(1+eta),2*float(Q(objective.cfg['delta_min_exact'])))
            rd['next_auxiliary_initialization']={'old_raw_delta':raw_delta,'new_delta':next_delta,
                'physical_coefficients_unchanged':True,'old_decision_and_failure_retained':True,
                'rule':'max(old_raw_delta, full_grid_eta+(1+eta)/1000000, 2*delta_min)'}
            vector=vector.copy();vector[-1]=next_delta
            if objective.checkpoint:objective.checkpoint(objective.snapshot())
        return finish('exchange-round-budget-exit')
    except EvaluationBudgetReached as error:return finish('shared-exchange-budget-exit',budget=str(error))
    except Exception as error:return finish('exchange-objective-or-solver-error',error={'type':type(error).__name__,'message':str(error)})


def developer_check():
    initial=np.array([0.,.6,.6]);radial=np.array([0.,.3,1.]);theta=np.arange(16)*np.pi/8
    lower=np.array([-2.,-1.,-1.]);upper=np.array([2.,1.,1.])
    def make(problem=None,changes=None):
        p=_EpigraphArrayProblem() if problem is None else problem;c=configuration()
        c.update(mirror_target_exact='1/1000',maxiter=8,max_physical_evaluations=45,max_seconds=30.,
            max_exchange_rounds=3,max_pool_rows=336)
        if changes:c.update(changes)
        return ExchangeEpigraphObjective(p,HeightAffineGate.from_artificial_array_problem(p),radial,theta,3,lower,upper,cfg=c)
    obj=make();v=obj.initial_vector(initial);obj.initialize_pool(v);obj.evaluate(v)
    calls=obj.problem.calls;obj.fun(v);obj.jac(v);obj.constraint_fun(v);value_reuse=obj.problem.calls==calls
    J=obj.constraint_jac(v);jac_calls=obj.problem.calls;obj.constraint_jac(v);jac_reuse=obj.problem.calls==jac_calls
    d=np.array([.2,-.3,.4,.5]);h=1e-6
    numerical=(obj.constraint_fun(v+h*d)-obj.constraint_fun(v-h*d))/(2*h)
    error=float(np.max(abs(numerical-J@d)))
    obj.evaluate(v);J=obj.constraint_jac(v);calls=obj.problem.calls
    vdelta=v.copy();vdelta[-1]+=.1;obj.constraint_jac(vdelta);delta_reuse=obj.problem.calls==calls
    # Selecting only an uninformative row cannot hide all omitted violations.
    sparse=make();w=sparse.initial_vector(initial);sparse.set_pool([2*len(radial)*len(theta)],{'kind':'artificial-deliberately-incomplete'})
    w[-1]=.05;record=sparse.evaluate(w)['decision'];before_rows,before_missing,before=sparse.missing_rows(w)
    additions,detail=sparse.expand_pool(w,'artificial-specific-missed-row-coverage')
    after_rows,after_missing,after=sparse.missing_rows(w)
    coverage=bool(before['omitted_violating_count']>0 and additions and
        after['omitted_violating_count']<before['omitted_violating_count'] and not record['independent_direct_eta_pass'])
    before_identity=sparse.problem.identity(w[:-1]);old_pool=sparse.pool.copy();sparse.constraint_jac(w)
    identity_unchanged=before_identity==sparse.problem.identity(w[:-1]) and set(old_pool)<=set(sparse.pool)
    zero=make();zero_run=run_exchange(zero,initial,artificial_inputs_only=True,evaluate_only=True)
    bad_problem=_EpigraphArrayProblem();bad=make(bad_problem);bv=bad.initial_vector(initial);bad.initialize_pool(bv);bad.evaluate(bv)
    bad_problem.fail_after_calls=bad_problem.calls
    failed=run_exchange(bad,initial,artificial_inputs_only=True)
    retained=failed['status']=='exchange-objective-or-solver-error' and failed['checkpoint']['best_physical_max_eta_point'] is not None
    solver=make(changes={'minimum_major_iterations_before_exchange':1})
    solver.set_pool([2*len(radial)*len(theta)],{'kind':'artificial-force-a-real-callback-exchange'})
    solved=run_exchange(solver,initial,artificial_inputs_only=True)
    invocations=solved['solver']['minimize_invocation_count']
    callback_exchange=any(rd.get('exit_reason')=='whole-grid-omitted-rows-exchange-request' for rd in solved['solver']['rounds'])
    return {'schema':'full-grid-row-exchange-artificial-development-v1','artificial_inputs_only':True,
        'research_geometry_evaluated':False,'selected_row_directional_Jacobian_absolute_error':error,
        'four_value_callbacks_share_one_whole_grid_state':value_reuse,'repeat_Jacobian_reuses_selected_derivatives':jac_reuse,
        'delta_only_change_reuses_geometry_and_derivatives':delta_reuse,'omitted_violations_recorded_and_pool_expanded':coverage,
        'row_pool_change_preserves_physical_identity':identity_unchanged,
        'zero_solver_path_status':zero_run['status'],'injected_Jacobian_failure_preserves_eligible_best':retained,
        'small_array_solver_status':solved['status'],'small_array_solver_error':solved.get('error'),
        'small_array_solver_invocations':invocations,'shared_budget_never_restarted':bool(invocations<=3 and solver.geometry_evaluations<=45),
        'real_array_SLSQP_callback_pool_exchange_exercised':callback_exchange,
        'no_full_constraint_Jacobian_formed':solved['checkpoint']['no_full_grid_constraint_Jacobian_was_formed'],
        'passed':bool(error<3e-7 and value_reuse and jac_reuse and delta_reuse and coverage and identity_unchanged
            and retained and callback_exchange and zero_run['solver']['minimize_invocation_count']==0 and invocations<=3
            and solved.get('error') is None and solver.geometry_evaluations<=45)}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    try:result=developer_check()
    except Exception as error:
        atomic_save(args.out,{'passed':False,'artificial_inputs_only':True,'source_files_sha256':implementation_hashes(),
            'error':{'type':type(error).__name__,'message':str(error)}});raise
    result['source_files_sha256']=implementation_hashes();atomic_save(args.out,result)
    print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
    if not result['passed']:raise SystemExit(1)


if __name__=='__main__':main()
