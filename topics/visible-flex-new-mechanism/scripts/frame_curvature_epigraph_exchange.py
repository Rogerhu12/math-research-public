#!/usr/bin/env python3
"""Actual-metric curvature epigraph with full-grid gates and exchanged rows.

The physical coefficients do not include the auxiliary zeta=lambda/100.
The direct-metric budget is fixed. Complete position two-jet derivatives are
queried in small radial batches with the same periodic primitive and common
height reference. Every trial is screened on the full value grid; the SLSQP
pool only selects rows whose Jacobian is retained.
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
from scipy.optimize import Bounds, minimize

from frame_collar_bvp import atomic_save
from frame_collar_residual_audit import digest
from frame_height_affine_gate import (HeightAffineGate, EvaluationBudgetReached,
    require_public_research_environment, _ArrayProblem)
from frame_metric_epigraph import MetricEpigraphObjective, geometry_values, metric_rows
from frame_metric_epigraph_dense import mirror_values
from frame_metric_epigraph_exchange import (configuration as previous_configuration,
    candidate_decision as previous_decision, PoolExchangeRequested,
    implementation_hashes as previous_hashes)
from frame_curvature_psd import curvature_values, independent_principal_curvatures

GROUPS = ('metric_minus', 'metric_plus', 'signed_z', 'ball', 'strip_plus',
    'strip_minus', 'mirror_pair', 'curvature_plus_trace',
    'curvature_plus_determinant', 'curvature_minus_trace', 'curvature_minus_determinant')
POSITION_JETS = ('X', 'Xs', 'Xt', 'Xss', 'Xst', 'Xtt', 'T')


def implementation_hashes():
    result = previous_hashes()
    for name in ['frame_curvature_psd.py', Path(__file__).name]:
        path = Path(__file__).with_name(name)
        result[name] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def configuration():
    cfg = previous_configuration()
    cfg.update(fixed_metric_budget_exact='167/625', curvature_scale_exact='100',
        curvature_lambda_min_exact='1/100000000', curvature_initial_margin_exact='1/1000000',
        curvature_target_radius_exact='61/1000', curvature_row_tolerance=1e-9,
        direct_curvature_tolerance=1e-8, radial_Jacobian_batch_owned_rows=16,
        max_exchange_rounds=20, initial_per_radial_group=[2,2,1,1,1,1,1,1,1,1,1],
        optimizer_objective='min zeta=lambda/100; fixed metric budget, no soft objective',
        final_selection='best actual maximum curvature passing all full-grid fixed-metric and physical gates',
        no_curvature_or_all_pairs_constraint_added=False,
        curvature_gates_use_actual_metric_and_complete_position_two_jets=True,
        curvature_and_mirror_gates_are_not_a_whole_surface_reach_certificate=True)
    return cfg


def curvature_forms(data, cfg):
    """Complete actual forms, independent principal curvatures, no regularization."""
    a = np.asarray(data['metric']['a'], float)
    if a.shape != (len(data['radial']),):
        raise ValueError('one fixed positive material radius per radial row required')
    values = curvature_values(data, a[:, None], 1/float(Q(cfg['curvature_scale_exact'])),
        area_floor=cfg['normal_area_numerical_floor'])
    principal = independent_principal_curvatures(values)
    if not np.all(np.isfinite(principal)):
        raise FloatingPointError('nonfinite independent actual-metric principal curvature')
    values['principal'] = principal
    values['maximum_absolute_by_point'] = np.max(abs(principal), axis=-1)
    return values


def curvature_rows(values, zeta, scale):
    zeta, scale = float(zeta), float(scale)
    if not np.isfinite(zeta) or zeta <= 0 or not np.isfinite(scale) or scale <= 0:
        raise ValueError('finite strictly positive curvature auxiliary and fixed scale required')
    q = values['q']
    h11 = np.stack([zeta*q*values['E'] + values['e']/scale,
                    zeta*q*values['E'] - values['e']/scale], axis=-1)
    h12 = np.stack([zeta*q*values['F'] + values['f']/scale,
                    zeta*q*values['F'] - values['f']/scale], axis=-1)
    h22 = np.stack([zeta*q*values['G'] + values['k']/scale,
                    zeta*q*values['G'] - values['k']/scale], axis=-1)
    traces = h11+h22
    determinants = h11*h22-h12*h12
    rows = np.stack([traces[...,0], determinants[...,0], traces[...,1], determinants[...,1]], axis=-1)
    if not np.all(np.isfinite(rows)):
        raise FloatingPointError('nonfinite scaled actual-metric curvature rows')
    return rows, (h11,h12,h22)


def candidate_decision(problem, gate, state, zeta, data, lower, upper, cfg, *, forms=None):
    bar = float(Q(cfg['fixed_metric_budget_exact']))
    result = previous_decision(problem, gate, state, bar, data, lower, upper, cfg)
    base_physical = result['eligible_under_physical_gates_including_mirror']
    metric_pass = result['divided_metric_row_pass'] and result['independent_direct_eta_pass']
    for name in ['auxiliary_delta','delta_min_exact','delta_bound_pass','direct_eta_minus_delta',
                 'auxiliary_delta_is_not_a_physical_parameter',
                 'auxiliary_delta_failure_does_not_erase_a_physically_eligible_trial',
                 'eligible_under_physical_gates_including_mirror']:
        result.pop(name, None)
    values = curvature_forms(data, cfg) if forms is None else forms
    scale = float(Q(cfg['curvature_scale_exact']))
    lam = scale*float(zeta)
    rows, unused = curvature_rows(values, zeta, scale)
    maximum_field = values['maximum_absolute_by_point']
    maximum = float(np.max(maximum_field))
    index = np.unravel_index(np.argmax(maximum_field), maximum_field.shape)
    row_pass = bool(np.min(rows) >= -cfg['curvature_row_tolerance'])
    direct_pass = bool(maximum <= lam+cfg['direct_curvature_tolerance'])
    lambda_pass = bool(lam >= float(Q(cfg['curvature_lambda_min_exact'])))
    physical = bool(base_physical and metric_pass)
    target = 1/float(Q(cfg['curvature_target_radius_exact']))
    result.update(fixed_metric_budget_exact=cfg['fixed_metric_budget_exact'],
        fixed_metric_budget_evaluated=bar, fixed_metric_budget_pass=bool(metric_pass),
        direct_eta_minus_fixed_budget=result['direct_max_eta']-bar,
        physical_gate_pass_excluding_fixed_metric=bool(base_physical),
        eligible_under_fixed_metric_and_physical_gates=physical,
        eligible_under_all_declared_sampled_constraints=bool(physical and row_pass and direct_pass and lambda_pass),
        curvature_auxiliary_zeta=float(zeta), curvature_auxiliary_lambda=lam,
        curvature_scale_exact=cfg['curvature_scale_exact'], curvature_lambda_bound_pass=lambda_pass,
        curvature_scaled_row_minima={name:float(np.min(rows[...,j])) for j,name in enumerate(GROUPS[7:])},
        curvature_scaled_PSD_row_pass=row_pass, curvature_row_tolerance=cfg['curvature_row_tolerance'],
        direct_maximum_absolute_principal_curvature=maximum,
        direct_max_curvature_location={'t':float(data['radial'][index[0]]),
            'theta':float(data['theta'][index[1]]), 'principal_curvatures':values['principal'][index].tolist()},
        independent_direct_curvature_pass=direct_pass, direct_curvature_minus_lambda=maximum-lam,
        direct_curvature_tolerance=cfg['direct_curvature_tolerance'],
        curvature_target_radius_exact=cfg['curvature_target_radius_exact'],
        target_local_curvature_upper_evaluated=target,
        target_local_curvature_pass=bool(maximum <= target+cfg['direct_curvature_tolerance']),
        target_curvature_and_existing_sampled_gates_pass=bool(physical and maximum <= target+cfg['direct_curvature_tolerance']),
        old_metric_auxiliary_is_not_reused_as_curvature_auxiliary=True,
        no_continuous_curvature_embedding_or_whole_reach_certificate=True)
    return result


def curvature_differentials(data, a, values):
    """Seven primitive derivatives on selected points only; a is fixed."""
    scale = np.asarray(a, float)
    dA = data['jac_Xs']; dT = data['jac_Xt']/scale[...,None,None]
    dU = data['jac_Xss']; dV = data['jac_Xst']/scale[...,None,None]
    dZ = data['jac_Xtt']/scale[...,None,None]**2
    dw = np.moveaxis(np.cross(np.moveaxis(dA,-1,-2),values['T'][...,None,:])
        + np.cross(values['A'][...,None,:],np.moveaxis(dT,-1,-2)), -2,-1)
    dotj = lambda x,j: np.einsum('...c,...cn->...n',x,j)
    return dict(dq=dotj(values['w'],dw)/values['q'][...,None],
        dE=2*dotj(values['A'],dA),
        dF=dotj(values['T'],dA)+dotj(values['A'],dT),
        dG=2*dotj(values['T'],dT),
        dIIe=dotj(values['U'],dw)+dotj(values['w'],dU),
        dIIf=dotj(values['V'],dw)+dotj(values['w'],dV),
        dIIk=dotj(values['W'],dw)+dotj(values['w'],dZ))


class CurvatureExchangeObjective(MetricEpigraphObjective):
    """Shared ordinary geometry; small-batch complete two-jet Jacobians."""
    def __init__(self,*args,**kwargs):
        if kwargs.get('cfg') is None: kwargs['cfg']=configuration()
        super().__init__(*args,**kwargs)
        for key in ['fixed_metric_budget_exact','curvature_scale_exact','curvature_lambda_min_exact',
                    'curvature_initial_margin_exact','curvature_target_radius_exact']:
            if Q(self.cfg[key])<=0: raise ValueError('positive exact curvature configuration required: '+key)
        if not 0<Q(self.cfg['hard_strip_half_width_exact'])<Q(self.cfg['outer_strip_half_width_exact']):
            raise ValueError('strict positive inner/outer strip sizes required')
        if Q(self.cfg['outer_strip_half_width_exact'])-Q(self.cfg['hard_strip_half_width_exact'])!=Q(self.cfg['strip_inner_margin_exact']):
            raise ValueError('exact strip margin identity failed')
        if (len(self.cfg['initial_per_radial_group'])!=len(GROUPS)
                or min(self.cfg['initial_per_radial_group'])<1
                or self.cfg['radial_Jacobian_batch_owned_rows']<1
                or self.cfg['max_pool_rows']<len(GROUPS) or self.cfg['max_exchange_rounds']<1):
            raise ValueError('finite positive eleven-group pool and radial-batch configuration required')
        for key in ['curvature_row_tolerance','direct_curvature_tolerance']:
            if self.cfg[key]<0 or not np.isfinite(self.cfg[key]): raise ValueError('finite nonnegative curvature tolerance required')
        self.total_started=self.started; self.optimization_started=None
        self.pool=np.empty(0,dtype=np.int64); self.pool_version=0; self.pool_history=[]
        self.derivative_cache=None; self.jacobian_geometry_batches=0; self.jacobian_refreshes=0
        self.value_geometry_seconds=0.; self.jacobian_geometry_seconds=0.; self.pool_jacobian_seconds=0.
        self.maximum_retained_derivative_bytes=0; self.maximum_batch_returned_Jacobian_bytes=0
        self.maximum_value_Jacobian_replay_difference=0.; self.maximum_batch_query_rows=0
        self.batch_replay_maxima={name:0. for name in POSITION_JETS+('center','metric')}
        self.best_physical=None; self.best_auxiliary=None; self.best_auxiliary_curvature=None; self.lowest_lambda_trial=None
        self.batch_definitions=self._batch_definitions()
        self.evaluation_definition={
            'schema':'actual-curvature-fixed-metric-budget-exchanged-row-evaluation-v1',
            'configuration':copy.deepcopy(self.cfg), 'physical_height_gate_sha256':self.gate.physical_sha256,
            'frozen_height_numerical_gate_sha256':self.gate.numerical_sha256,
            'fixed_physical_tangent_family':self.space,'physical_parameter_count':self.n,
            'solver_parameter_count':self.n+1,'auxiliary_curvature_zeta_index':self.n,
            'auxiliary_curvature_not_in_physical_state_identity':True,
            'old_metric_delta_not_a_solver_variable':True,
            'objective':'zeta=lambda/curvature_scale, with zero physical gradient and final derivative one',
            'constraint_row_order':list(GROUPS), 'actual_curvature_forms':'Hhat+-=zeta*q*I+-K/curvature_scale',
            'radial_nodes_exact_binary64':[str(Q.from_float(float(x))) for x in self.radial],
            'theta_nodes_exact_binary64':[str(Q.from_float(float(x))) for x in self.theta],
            'geometry_quadrature_order':self.order,'problem_evaluation':copy.deepcopy(self.problem.evaluation_definition()),
            'complete_value_grid_is_fixed_during_all_rounds':True,
            'full_value_gates_checked_at_every_trial':True,'row_pool_not_physical_state':True,
            'radial_Jacobian_query_batches':copy.deepcopy(self.batch_definitions),
            'same_full_angular_grid_and_same_query_independent_primitive_in_every_batch':True,
            'source_files_sha256':implementation_hashes()}
        self.evaluation_sha256=digest(self.evaluation_definition)

    def _batch_definitions(self):
        n=len(self.radial); width=int(self.cfg['radial_Jacobian_batch_owned_rows']); result=[]
        for start in range(0,n,width):
            owned=np.arange(start,min(n,start+width),dtype=int)
            query=np.unique(np.r_[0,owned,n-1])
            result.append({'owned_full_radial_indices':owned.tolist(),'query_full_radial_indices':query.tolist(),
                'query_radial_exact_binary64':[str(Q.from_float(float(self.radial[i]))) for i in query]})
        if sorted(i for b in result for i in b['owned_full_radial_indices'])!=list(range(n)):
            raise ArithmeticError('radial batch ownership is not a partition')
        return result

    def _wall(self):
        if self.optimization_started is not None and time.monotonic()-self.optimization_started>=self.cfg['max_seconds']:
            raise EvaluationBudgetReached('shared curvature-exchange optimization wall budget reached; full-grid best preserved')

    def begin_optimization(self):
        if self.optimization_started is not None: raise ValueError('the shared optimization clock cannot be restarted')
        self.optimization_started=time.monotonic(); self.last_checkpoint=self.optimization_started

    def physical_geometry(self,state):
        state=np.asarray(state,float)
        if state.shape!=(self.n,) or not np.all(np.isfinite(state)): raise ValueError('finite full physical coefficient vector required')
        self.assert_context(state); self._wall()
        if self.geometry_cache is not None and np.array_equal(state,self.geometry_cache['state']): return self.geometry_cache
        if self.geometry_evaluations>=self.cfg['max_physical_evaluations']:
            raise EvaluationBudgetReached('shared full-grid physical-state evaluation budget reached')
        before=time.monotonic(); data=self.problem.geometry(state,self.radial,self.theta,self.order,jacobian=False)
        expected=(len(self.radial),len(self.theta),3)
        for key in POSITION_JETS:
            if np.asarray(data[key]).shape!=expected or not np.all(np.isfinite(data[key])):
                raise FloatingPointError('finite complete whole-grid position jets required: '+key)
        values=geometry_values(data); mirror=mirror_values(data,float(Q(self.cfg['mirror_target_exact'])))
        forms=curvature_forms(data,self.cfg)
        cache={key:np.asarray(data[key]).copy() for key in POSITION_JETS+('center',)}
        for key in ['Ts','Tss','Ttheta','primitive']:
            if key in data: cache[key]=np.asarray(data[key]).copy()
        for key in ['metric','height']:
            if key in data: cache[key]={name:np.asarray(v).copy() for name,v in data[key].items()}
        cache.update(state=state.copy(),radial=self.radial,theta=self.theta,e=values['e'],f=values['f'],eta=values['eta'],
            mirror_polynomial=mirror['polynomial'],curvature=forms)
        self.geometry_evaluations+=1; cache['geometry_evaluation']=self.geometry_evaluations
        for value in cache.values():
            if isinstance(value,np.ndarray): value.setflags(write=False)
            elif isinstance(value,dict):
                for item in value.values():
                    if isinstance(item,np.ndarray): item.setflags(write=False)
        self.value_geometry_seconds+=time.monotonic()-before
        self.geometry_cache=cache; self.derivative_cache=None
        size=sum(v.nbytes if isinstance(v,np.ndarray) else sum(x.nbytes for x in v.values() if isinstance(x,np.ndarray))
            if isinstance(v,dict) else 0 for v in cache.values())
        self.maximum_geometry_cache_array_bytes=max(self.maximum_geometry_cache_array_bytes,size)
        return cache

    def initial_vector(self,state,lambda_initial=None):
        data=self.physical_geometry(state); maximum=float(np.max(data['curvature']['maximum_absolute_by_point']))
        minimum=float(Q(self.cfg['curvature_lambda_min_exact'])); scale=float(Q(self.cfg['curvature_scale_exact']))
        lam=(max(2*minimum,maximum+(1+maximum)*float(Q(self.cfg['curvature_initial_margin_exact'])))
            if lambda_initial is None else float(lambda_initial))
        if not np.isfinite(lam) or lam<minimum: raise ValueError('valid explicit initial curvature lambda required')
        return np.r_[np.asarray(state,float),lam/scale]

    def rows_from_geometry(self,data,zeta):
        cm,cp=metric_rows(data['e'],data['f'],float(Q(self.cfg['fixed_metric_budget_exact'])))
        X=data['X']; p=float(Q(self.cfg['hard_strip_half_width_exact'])); R=float(Q(self.cfg['hard_ball_radius_exact']))
        cr,_=curvature_rows(data['curvature'],zeta,float(Q(self.cfg['curvature_scale_exact'])))
        return np.concatenate([np.stack([cm,cp,self.gate.side*X[...,2]-float(Q(self.cfg['minimum_signed_height_exact'])),
            1-np.sum(X*X,axis=-1)/R**2,1-X[...,1]/p,1+X[...,1]/p,data['mirror_polynomial']]),
            np.moveaxis(cr,-1,0)],axis=0)

    def row_tolerances(self):
        c=self.cfg
        return np.asarray([c['metric_row_tolerance']]*2+[c['signed_height_tolerance']]
            +[c['shape_constraint_tolerance']]*3+[c['mirror_polynomial_tolerance']]+[c['curvature_row_tolerance']]*4)

    def evaluate(self,vector):
        vector=np.asarray(vector,float)
        if vector.shape!=(self.n+1,) or not np.all(np.isfinite(vector)) or vector[-1]<=0:
            raise ValueError('physical vector plus finite positive auxiliary curvature zeta required')
        self.assert_context(vector[:-1]); self._wall()
        if (self.epigraph_cache is not None and np.array_equal(vector,self.epigraph_cache['vector'])
                and self.geometry_cache is not None and np.array_equal(vector[:-1],self.geometry_cache['state'])):
            return self.epigraph_cache['record']
        data=self.physical_geometry(vector[:-1])
        decision=candidate_decision(self.problem,self.gate,vector[:-1],vector[-1],data,self.lower,self.upper,self.cfg,forms=data['curvature'])
        rows=self.rows_from_geometry(data,vector[-1]); violating=rows < -self.row_tolerances()[:,None,None]
        omitted=violating.copy(); omitted.reshape(-1)[self.pool]=False
        separation={'all_full_grid_violating_rows':int(np.count_nonzero(violating)),
            'omitted_violating_rows':int(np.count_nonzero(omitted)),
            'group_counts':{name:{'whole_grid':int(np.count_nonzero(violating[g])),
                'omitted':int(np.count_nonzero(omitted[g]))} for g,name in enumerate(GROUPS)}}
        now=time.monotonic(); self.epigraph_evaluations+=1
        record={'epigraph_evaluation':self.epigraph_evaluations,'physical_geometry_evaluation':data['geometry_evaluation'],
            'elapsed_seconds':now-self.total_started,
            'optimization_elapsed_seconds':None if self.optimization_started is None else now-self.optimization_started,
            'phase':'initialization' if self.optimization_started is None else 'optimization',
            'pool_version':self.pool_version,'pool_rows':len(self.pool),
            'whole_grid_and_pool_separation_at_this_same_trial':separation,'decision':decision}
        point={'vector':vector.copy(),'record':copy.deepcopy(record)}
        if self.lowest_lambda_trial is None or vector[-1]<self.lowest_lambda_trial['vector'][-1]: self.lowest_lambda_trial=point
        def better(old):
            key=lambda p:(p['record']['decision']['direct_maximum_absolute_principal_curvature'],
                p['record']['decision']['direct_max_eta'],p['vector'][-1])
            return old is None or key(point)<key(old)
        if decision['eligible_under_fixed_metric_and_physical_gates'] and better(self.best_physical): self.best_physical=point
        if decision['eligible_under_all_declared_sampled_constraints']:
            if self.best_auxiliary is None or vector[-1]<self.best_auxiliary['vector'][-1]: self.best_auxiliary=point
            if better(self.best_auxiliary_curvature): self.best_auxiliary_curvature=point
        rows.setflags(write=False); self.history.append(record)
        self.epigraph_cache={'vector':vector.copy(),'record':copy.deepcopy(record),'rows':rows}
        if self.checkpoint is not None and (self.geometry_evaluations-self.last_checkpoint_geometry>=self.cfg['checkpoint_physical_evaluations']
                or now-self.last_checkpoint>=self.cfg['checkpoint_seconds']):
            self.checkpoint(self.snapshot()); self.last_checkpoint=now; self.last_checkpoint_geometry=self.geometry_evaluations
        self._wall(); return record

    def all_rows(self,vector):
        self.evaluate(vector); return self.epigraph_cache['rows']

    def missing_rows(self,vector,*,callback_trigger=False):
        rows=self.all_rows(vector); limits=self.row_tolerances().copy()
        if callback_trigger: limits[:2]=np.maximum(limits[:2],float(Q(self.cfg['callback_metric_exchange_trigger_exact'])))
        missing=rows < -limits[:,None,None]; missing.reshape(-1)[self.pool]=False
        return rows,missing,{'callback_trigger_not_an_eligibility_tolerance':bool(callback_trigger),
            'omitted_violating_count':int(np.count_nonzero(missing)),
            'groups':{name:{'omitted_violating_count':int(np.count_nonzero(missing[g])),
                'whole_grid_minimum_row':float(np.min(rows[g])),'trigger_tolerance':float(limits[g]),
                'actual_eligibility_tolerance':float(self.row_tolerances()[g])} for g,name in enumerate(GROUPS)}}

    def set_pool(self,indices,reason):
        total=len(GROUPS)*len(self.radial)*len(self.theta)
        indices=np.asarray(sorted(set(int(x) for x in indices)),dtype=np.int64)
        if not len(indices) or np.any(indices<0) or np.any(indices>=total): raise ValueError('valid nonempty eleven-group row pool required')
        if len(indices)>self.cfg['max_pool_rows']: raise ValueError('declared row-pool capacity exceeded')
        if len(self.pool) and not set(self.pool)<=set(indices): raise ValueError('previous enforced rows cannot be removed')
        old=set(self.pool); self.pool=indices; self.pool.setflags(write=False); self.pool_version+=1
        self.derivative_cache=None; self.epigraph_cache=None
        record={'version':self.pool_version,'row_count':len(indices),'total_full_grid_rows':total,
            'group_order':list(GROUPS),'flat_index_rule':'group*(Nr*Ntheta)+radial_index*Ntheta+theta_index',
            'row_indices':indices.tolist(),'row_indices_sha256':digest(indices.tolist()),
            'added_row_indices':[int(i) for i in indices if int(i) not in old],'reason':copy.deepcopy(reason)}
        self.pool_history.append(record); return record

    def initialize_pool(self,vector):
        rows=self.all_rows(vector); Nr,Nt=rows.shape[1:]; chosen=[]
        for group in range(len(GROUPS)):
            take=min(Nt,int(self.cfg['initial_per_radial_group'][group]))
            order=np.argsort(rows[group],axis=1,kind='stable')[:,:take]
            chosen.extend((group*Nr*Nt+np.arange(Nr)[:,None]*Nt+order).ravel().tolist())
        return self.set_pool(chosen,{'kind':'initial-worst-angular-rows-in-every-radial-slice-and-all-eleven-groups',
            'per_radial_group':list(self.cfg['initial_per_radial_group'])})

    def expand_pool(self,vector,reason):
        rows,missing,detail=self.missing_rows(vector); Nr,Nt=rows.shape[1:]; chosen=set(int(x) for x in self.pool)
        for group in range(len(GROUPS)):
            for ir in range(Nr):
                ids=np.flatnonzero(missing[group,ir])
                if len(ids):
                    ids=ids[np.argsort(rows[group,ir,ids],kind='stable')[:self.cfg['exchange_per_radial_group']]]
                    chosen.update(int(group*Nr*Nt+ir*Nt+j) for j in ids)
            ids=np.flatnonzero(missing[group].ravel())
            if len(ids):
                ids=ids[np.argsort(rows[group].ravel()[ids],kind='stable')[:self.cfg['exchange_global_per_group']]]
                chosen.update(int(group*Nr*Nt+j) for j in ids)
        if len(chosen)==len(self.pool): return None,detail
        if len(chosen)>self.cfg['max_pool_rows']:
            detail.update(pool_capacity_would_be_exceeded=True,proposed_pool_rows=len(chosen)); return None,detail
        record=self.set_pool(chosen,{'kind':reason,'full_grid_violation_summary':detail,
            'all_groups_screened_only_declared_worst_omitted_rows_added':True})
        after=missing.reshape(-1).copy(); after[self.pool]=False
        record['omitted_violations_after_this_addition']=int(np.count_nonzero(after))
        return record,detail

    def active_derivatives(self,vector):
        self.evaluate(vector)
        if not len(self.pool): raise ValueError('initialize the row pool before requesting its Jacobian')
        if (self.derivative_cache is not None and self.derivative_cache['pool_version']==self.pool_version
                and np.array_equal(vector[:-1],self.derivative_cache['state'])): return self.derivative_cache
        self._wall(); Nr,Nt=len(self.radial),len(self.theta); count=Nr*Nt; points=np.unique(self.pool%count)
        keys=['de_metric','df_metric','mirror_jac','dq','dE','dF','dG','dIIe','dIIf','dIIk']
        cache={name:np.empty((len(points),self.n)) for name in keys}
        cache['jac_X']=np.empty((len(points),3,self.n)); covered=np.zeros(len(points),bool)
        cache.update(state=np.asarray(vector[:-1]).copy(),pool_version=self.pool_version,points=points,
            pool_points=np.searchsorted(points,self.pool%count))
        self.jacobian_refreshes+=1
        for definition in self.batch_definitions:
            owned=np.asarray(definition['owned_full_radial_indices'],int)
            selected=np.flatnonzero((points//Nt>=owned[0]) & (points//Nt<=owned[-1]))
            if not len(selected): continue
            self._wall(); query=np.asarray(definition['query_full_radial_indices'],int)
            before=time.monotonic()
            data=self.problem.geometry(vector[:-1],self.radial[query],self.theta,self.order,
                jacobian=True,full_two_jet_jacobian=True)
            self.jacobian_geometry_seconds+=time.monotonic()-before; self.jacobian_geometry_batches+=1
            self.maximum_batch_query_rows=max(self.maximum_batch_query_rows,len(query))
            maximum=0.; scale=1.
            for key in POSITION_JETS+('center',):
                current=np.asarray(data[key]); target=np.asarray(self.geometry_cache[key])[query]
                if current.shape!=target.shape or not np.all(np.isfinite(current)): raise FloatingPointError('bad batch ordinary jet: '+key)
                difference=float(np.max(abs(current-target))); maximum=max(maximum,difference)
                scale=max(scale,float(np.max(abs(target)))); self.batch_replay_maxima[key]=max(self.batch_replay_maxima[key],difference)
            for key,target0 in self.geometry_cache['metric'].items():
                target=np.asarray(target0)[query]; current=np.asarray(data['metric'][key])
                if current.shape!=target.shape or not np.all(np.isfinite(current)): raise FloatingPointError('bad batch fixed metric: '+key)
                difference=float(np.max(abs(current-target))); maximum=max(maximum,difference)
                scale=max(scale,float(np.max(abs(target)))); self.batch_replay_maxima['metric']=max(self.batch_replay_maxima['metric'],difference)
            self.maximum_value_Jacobian_replay_difference=max(self.maximum_value_Jacobian_replay_difference,maximum)
            if maximum>self.cfg['value_Jacobian_replay_relative_tolerance']*scale:
                raise ArithmeticError('same-state batch ordinary jets differ beyond declared floating replay tolerance')
            expected=(len(query),Nt,3,self.n); totalbytes=0
            for key in POSITION_JETS:
                jac=np.asarray(data['jac_'+key])
                if jac.shape!=expected or not np.all(np.isfinite(jac)): raise FloatingPointError('complete finite batch position two-jet Jacobian required: '+key)
                totalbytes+=jac.nbytes
            self.maximum_batch_returned_Jacobian_bytes=max(self.maximum_batch_returned_Jacobian_bytes,totalbytes)
            gpoints=points[selected]; ri=np.searchsorted(query,gpoints//Nt); ti=gpoints%Nt
            small={key:np.asarray(data[key])[ri,ti] for key in POSITION_JETS}
            for key in POSITION_JETS: small['jac_'+key]=np.asarray(data['jac_'+key])[ri,ti]
            a=np.asarray(data['metric']['a'])[ri]
            values=curvature_values(small,a,1/float(Q(self.cfg['curvature_scale_exact'])),area_floor=self.cfg['normal_area_numerical_floor'])
            differential=curvature_differentials(small,a,values)
            for key,value in differential.items(): cache[key][selected]=value
            X,U,T=(small[key] for key in ['X','Xs','T']); JX,JU,JT=(small['jac_'+key] for key in ['X','Xs','T'])
            cache['jac_X'][selected]=JX
            cache['de_metric'][selected]=2*np.einsum('ic,icn->in',U,JU)
            cache['df_metric'][selected]=np.einsum('ic,icn->in',T,JU)+np.einsum('ic,icn->in',U,JT)
            W=np.cross(U,T); z=X[:,2]; D=z[:,None]**2*W
            D[:,2]-=float(Q(self.cfg['mirror_target_exact']))**2*W[:,2]
            cache['mirror_jac'][selected]=(2*z*np.sum(W*W,axis=1))[:,None]*JX[:,2,:]
            cache['mirror_jac'][selected]+=2*np.einsum('ic,icn->in',np.cross(T,D),JU)+2*np.einsum('ic,icn->in',np.cross(D,U),JT)
            covered[selected]=True
            del data,small,differential,values,JX,JU,JT,jac
        if not np.all(covered): raise ArithmeticError('selected Jacobian point ownership incomplete')
        if any(not np.all(np.isfinite(v)) for v in cache.values() if isinstance(v,np.ndarray)):
            raise FloatingPointError('nonfinite selected curvature derivative')
        for value in cache.values():
            if isinstance(value,np.ndarray): value.setflags(write=False)
        self.derivative_cache=cache
        self.maximum_retained_derivative_bytes=max(self.maximum_retained_derivative_bytes,
            sum(x.nbytes for x in cache.values() if isinstance(x,np.ndarray)))
        self._wall(); return cache

    def constraint_fun(self,vector): return self.all_rows(vector).reshape(-1)[self.pool]

    def constraint_jac(self,vector):
        before=time.monotonic(); d=self.active_derivatives(vector); data=self.geometry_cache
        count=data['e'].size; groups=self.pool//count; pp=d['pool_points']; points=self.pool%count
        J=np.zeros((len(self.pool),self.n+1)); bar=float(Q(self.cfg['fixed_metric_budget_exact']))
        radius=float(Q(self.cfg['hard_ball_radius_exact'])); strip=float(Q(self.cfg['hard_strip_half_width_exact']))
        f=data['f'].ravel()[points]; zeta=float(vector[-1]); scale=float(Q(self.cfg['curvature_scale_exact']))
        forms=data['curvature']; flat={k:forms[k].ravel() for k in ['q','E','F','G','e','f','k']}
        for group in range(len(GROUPS)):
            mask=groups==group; i=pp[mask]; p=points[mask]
            if group<2:
                J[mask,:self.n]=(-1 if group==0 else 1)*d['de_metric'][i]-(2*f[mask]/bar)[:,None]*d['df_metric'][i]
            elif group==2: J[mask,:self.n]=self.gate.side*d['jac_X'][i,2,:]
            elif group==3: J[mask,:self.n]=-2*np.einsum('ic,icn->in',data['X'].reshape(count,3)[p],d['jac_X'][i])/radius**2
            elif group==4: J[mask,:self.n]=-d['jac_X'][i,1,:]/strip
            elif group==5: J[mask,:self.n]=d['jac_X'][i,1,:]/strip
            elif group==6: J[mask,:self.n]=d['mirror_jac'][i]
            else:
                sign=1 if group<9 else -1; q=flat['q'][p]
                h=[]; dh=[]
                for metric,second,dmetric,dsecond in [('E','e','dE','dIIe'),('F','f','dF','dIIf'),('G','k','dG','dIIk')]:
                    h.append(zeta*q*flat[metric][p]+sign*flat[second][p]/scale)
                    dh.append(zeta*(d['dq'][i]*flat[metric][p,None]+q[:,None]*d[dmetric][i])+sign*d[dsecond][i]/scale)
                if group in [7,9]:
                    J[mask,:self.n]=dh[0]+dh[2]; J[mask,-1]=q*(flat['E'][p]+flat['G'][p])
                else:
                    J[mask,:self.n]=h[2][:,None]*dh[0]+h[0][:,None]*dh[2]-2*h[1][:,None]*dh[1]
                    J[mask,-1]=q*(flat['G'][p]*h[0]+flat['E'][p]*h[2]-2*flat['F'][p]*h[1])
        if not np.all(np.isfinite(J)): raise FloatingPointError('nonfinite selected actual-curvature Jacobian')
        self.maximum_constraint_Jacobian_bytes=max(self.maximum_constraint_Jacobian_bytes,J.nbytes)
        self.pool_jacobian_seconds+=time.monotonic()-before; return J

    def snapshot(self):
        scale=float(Q(self.cfg['curvature_scale_exact'])); now=time.monotonic()
        def point(item):
            if item is None:return None
            state=item['vector'][:-1]; zeta=float(item['vector'][-1]); lam=scale*zeta
            return {'physical_parameter_coefficients_binary64':state.tolist(),
                'exact_binary64_physical_coefficients':[str(Q.from_float(float(x))) for x in state],
                'physical_state_sha256':digest(self.problem.identity(state)),
                'auxiliary_zeta_evaluated':zeta,'auxiliary_zeta_exact_binary64':str(Q.from_float(zeta)),
                'auxiliary_lambda_evaluated':lam,'auxiliary_lambda_exact_binary64':str(Q.from_float(lam)),
                'record':copy.deepcopy(item['record'])}
        return {'schema':'actual-curvature-eleven-group-exchange-checkpoint-v1','configuration':copy.deepcopy(self.cfg),
            'height_gate':self.gate.record(),'objective_evaluation_definition':self.evaluation_definition,
            'objective_evaluation_sha256':self.evaluation_sha256,
            'physical_geometry_evaluations':self.geometry_evaluations,'epigraph_vector_evaluations':self.epigraph_evaluations,
            'auxiliary_only_changes_do_not_count_as_new_physical_geometry':True,
            'jacobian_geometry_batches':self.jacobian_geometry_batches,'jacobian_refreshes':self.jacobian_refreshes,
            'best_physical_curvature_point':point(self.best_physical),
            'best_auxiliary_feasible_lambda_point':point(self.best_auxiliary),
            'best_auxiliary_feasible_curvature_point':point(self.best_auxiliary_curvature),
            'lowest_lambda_trial_may_be_ineligible':point(self.lowest_lambda_trial),
            'history':copy.deepcopy(self.history),'physical_box_lower':self.lower.tolist(),'physical_box_upper':self.upper.tolist(),
            'total_elapsed_seconds':now-self.total_started,
            'initialization_elapsed_seconds':now-self.total_started if self.optimization_started is None else self.optimization_started-self.total_started,
            'optimization_elapsed_seconds':None if self.optimization_started is None else now-self.optimization_started,
            'value_geometry_seconds':self.value_geometry_seconds,'jacobian_geometry_seconds':self.jacobian_geometry_seconds,
            'pool_Jacobian_including_refresh_seconds':self.pool_jacobian_seconds,
            'maximum_geometry_cache_array_bytes':self.maximum_geometry_cache_array_bytes,
            'maximum_retained_selected_derivative_bytes':self.maximum_retained_derivative_bytes,
            'maximum_returned_batch_Jacobian_bytes':self.maximum_batch_returned_Jacobian_bytes,
            'maximum_single_constraint_Jacobian_bytes':self.maximum_constraint_Jacobian_bytes,
            'maximum_batch_query_radial_rows':self.maximum_batch_query_rows,
            'maximum_same_state_batch_ordinary_jet_difference':self.maximum_value_Jacobian_replay_difference,
            'same_state_batch_ordinary_jet_differences_by_field':dict(self.batch_replay_maxima),
            'active_row_pool_history':copy.deepcopy(self.pool_history),
            'no_full_grid_constraint_Jacobian_formed':True,
            'full_grid_two_jet_Jacobian_was_requested':bool(self.maximum_batch_query_rows==len(self.radial)),
            'all_selected_points_screened_on_whole_value_grid':True,
            'regularity_not_replaced_by_sqrt_q2_plus_epsilon':True,
            'no_whole_surface_reach_certificate':True}


def run_exchange(objective,initial,*,lambda_initial=None,artificial_inputs_only=False,evaluate_only=False):
    if not artificial_inputs_only: require_public_research_environment()
    elif objective.gate.kind!='artificial-array' and not evaluate_only:
        raise ValueError('artificial solver calls require the explicit array family')
    metadata={'method':'SLSQP with eleven-group explicit row exchanges','minimize_invocation_count':0,
        'total_major_iterations':0,'shared_maxiter':objective.cfg['maxiter'],
        'shared_max_physical_evaluations':objective.cfg['max_physical_evaluations'],
        'shared_optimization_seconds':objective.cfg['max_seconds'],'max_exchange_rounds':objective.cfg['max_exchange_rounds'],
        'rounds':[],'artificial_inputs_only':bool(artificial_inputs_only),'evaluate_only':bool(evaluate_only),
        'numpy_version':np.__version__,'scipy_version':scipy.__version__,
        'keep_feasible_not_passed_or_claimed':True,'all_eligibility_tests_are_whole_grid':True}
    def finish(status,error=None,budget=None):
        snap=objective.snapshot()
        if objective.checkpoint: objective.checkpoint(snap)
        return {'status':status,'error':error,'budget_message':budget,'solver':metadata,'checkpoint':snap,
            'selected_point':'best actual maximum curvature satisfying full fixed-metric and physical gates',
            'no_metric_parameter_or_height_reference_change':True}
    try:
        vector=objective.initial_vector(initial,lambda_initial); preflight=objective.evaluate(vector)
        if not preflight['decision']['eligible_under_all_declared_sampled_constraints']:
            return finish('initial-full-grid-fixed-metric-physical-or-curvature-bound-gate-failed')
        if not len(objective.pool): objective.initialize_pool(vector)
        objective.evaluate(vector); objective.active_derivatives(vector)
        metadata['new_initial_auxiliary_zeta']=float(vector[-1])
        metadata['new_initial_auxiliary_lambda']=float(Q(objective.cfg['curvature_scale_exact']))*float(vector[-1])
        if evaluate_only: return finish('evaluation-only-full-grid-batched-two-jets-and-pooled-Jacobian-no-solver')
        objective.begin_optimization()
        for round_index in range(int(objective.cfg['max_exchange_rounds'])):
            objective._wall(); remaining=int(objective.cfg['maxiter'])-metadata['total_major_iterations']
            if remaining<=0: return finish('shared-major-iteration-budget-exit')
            rd={'round':round_index+1,'pool_version':objective.pool_version,'pool_rows':len(objective.pool),
                'initial_vector_exact':[str(Q.from_float(float(x))) for x in vector],
                'major_iterations':0,'exit_reason':None}
            metadata['rounds'].append(rd)
            def callback(x):
                rd['major_iterations']+=1; metadata['total_major_iterations']+=1; objective.evaluate(x)
                _,_,detail=objective.missing_rows(x,callback_trigger=True)
                if rd['major_iterations']>=objective.cfg['minimum_major_iterations_before_exchange'] and detail['omitted_violating_count']:
                    raise PoolExchangeRequested(x,detail)
            try:
                metadata['minimize_invocation_count']+=1
                lower_zeta=float(Q(objective.cfg['curvature_lambda_min_exact']))/float(Q(objective.cfg['curvature_scale_exact']))
                result=minimize(objective.fun,vector,jac=objective.jac,method='SLSQP',
                    bounds=Bounds(np.r_[objective.lower,lower_zeta],np.r_[objective.upper,np.inf]),
                    constraints=[objective.cap_constraint(),objective.nonlinear_constraint()],callback=callback,
                    options={'maxiter':remaining,'ftol':objective.cfg['ftol'],'disp':False})
                vector=np.asarray(result.x,float).copy(); objective.evaluate(vector)
                rd['library_result']={k:(bool(getattr(result,k)) if k=='success' else int(getattr(result,k)) if k in ['status','nit','nfev','njev']
                    else float(getattr(result,k)) if k=='fun' else str(getattr(result,k)))
                    for k in ['success','status','message','nit','nfev','njev','fun'] if hasattr(result,k)}
                rd['exit_reason']='library-return'; _,_,detail=objective.missing_rows(vector)
                if not detail['omitted_violating_count']:
                    rd['full_grid_separation']=detail
                    return finish('curvature-exchange-library-returned-no-omitted-violating-rows')
                exchange=PoolExchangeRequested(vector,detail)
            except PoolExchangeRequested as error:
                exchange=error; vector=error.vector; rd['exit_reason']='whole-grid-omitted-rows-exchange-request'
            rd['full_grid_separation']=exchange.reason
            if round_index+1>=objective.cfg['max_exchange_rounds']:
                return finish('exchange-round-limit-with-missing-eleven-group-rows-recorded')
            added,detail=objective.expand_pool(vector,'callback-or-library-return-missing-eleven-group-rows')
            rd['pool_addition']=added; rd['exact_tolerance_missing_summary']=detail
            if added is None: return finish('row-pool-capacity-or-no-new-row-stop')
            scale=float(Q(objective.cfg['curvature_scale_exact'])); raw_lambda=float(vector[-1])*scale
            data=objective.physical_geometry(vector[:-1]); maximum=float(np.max(data['curvature']['maximum_absolute_by_point']))
            next_lambda=max(raw_lambda,maximum+(1+maximum)*float(Q(objective.cfg['curvature_initial_margin_exact'])),
                2*float(Q(objective.cfg['curvature_lambda_min_exact'])))
            rd['next_auxiliary_initialization']={'old_raw_lambda':raw_lambda,'new_lambda':next_lambda,
                'physical_coefficients_unchanged':True,'old_decision_and_failure_retained':True,
                'rule':'max(old_lambda, whole-grid max_abs_curvature+(1+maximum)/1000000, 2*lambda_min)'}
            vector=vector.copy(); vector[-1]=next_lambda/scale
            if objective.checkpoint: objective.checkpoint(objective.snapshot())
        return finish('curvature-exchange-round-budget-exit')
    except EvaluationBudgetReached as error: return finish('shared-curvature-exchange-budget-exit',budget=str(error))
    except Exception as error: return finish('curvature-objective-or-solver-error',error={'type':type(error).__name__,'message':str(error)})


class _CurvatureArrayProblem(_ArrayProblem):
    """Smooth explicit local jets; no assertion that all arrays integrate to a surface."""
    def objective_family_definition(self):
        return {'schema':'artificial-complete-curvature-jet-family-v1','token':self.objective_token,
            'curvature_amplitude':'1+p0','all_jets_and_Jacobians_explicit':True,
            'not_a_research_surface':True}
    def identity(self,state):
        return {'family':self.objective_family_definition(),'height_family':self.height_gate_family_definition(),
            'coefficients':[str(Q.from_float(float(x))) for x in state]}
    def geometry(self,state,radial,theta,order,jacobian=False,full_two_jet_jacobian=False):
        self.calls+=1
        if self.fail_after_calls is not None and self.calls>self.fail_after_calls:
            raise FloatingPointError('injected artificial batch failure')
        p=np.asarray(state,float); r=np.asarray(radial,float); th=np.asarray(theta,float)
        shape=(len(r),len(th),3); fields={k:np.zeros(shape) for k in POSITION_JETS}
        jac={k:np.zeros(shape+(3,)) for k in POSITION_JETS}
        h=.5*p[1]+.25*p[2]; ang=th+.03*p[0]
        T=fields['T']; T[...,0]=np.cos(ang); T[...,1]=np.sin(ang)
        jac['T'][...,0,0]=-.03*np.sin(ang); jac['T'][...,1,0]=.03*np.cos(ang)
        fields['Xt']=T.copy(); jac['Xt']=jac['T'].copy()
        U=fields['Xs']; U[...,2]=1+.02*p[1]
        jac['Xs'][...,2,1]=.02
        fields['X'][...,0]=.2*np.cos(th)+.01*p[0]
        fields['X'][...,1]=.1*np.sin(th); fields['X'][...,2]=.05+r[:,None]*h
        jac['X'][...,0,0]=.01; jac['X'][...,2,1]=r[:,None]/2; jac['X'][...,2,2]=r[:,None]/4
        normal=np.stack([-np.sin(ang),np.cos(ang),np.zeros_like(ang)],axis=-1)
        normal0=np.stack([-np.cos(ang),-np.sin(ang),np.zeros_like(ang)],axis=-1)*.03
        for name,factor in [('Xss',1.),('Xst',.1),('Xtt',-.3)]:
            amplitude=factor*(1+p[0])*(1+.1*np.cos(2*th))
            fields[name][:]=amplitude[None,:,None]*normal[None,:,:]
            jac[name][...,0]=factor*(1+.1*np.cos(2*th))[None,:,None]*normal[None,:,:]+amplitude[None,:,None]*normal0[None,:,:]
        result=dict(fields,center=r*h,radial=r,theta=th,
            metric={'a':np.ones(len(r)),'ap':np.zeros(len(r)),'app':np.zeros(len(r))})
        if jacobian: result.update({'jac_'+key:value for key,value in jac.items()})
        return result


def developer_check():
    initial=np.array([.3,.6,.6]); radial=np.array([0.,.2,.4,.7,1.]); theta=np.arange(12)*np.pi/6
    lower=np.array([-.8,-1.,-1.]); upper=np.array([2.,1.,1.])
    def make(changes=None,problem=None):
        p=_CurvatureArrayProblem() if problem is None else problem; cfg=configuration()
        cfg.update(fixed_metric_budget_exact='1/5',curvature_scale_exact='3',mirror_target_exact='1/1000',
            radial_Jacobian_batch_owned_rows=2,maxiter=8,max_physical_evaluations=45,max_seconds=30.,max_exchange_rounds=4,
            max_pool_rows=1000,minimum_major_iterations_before_exchange=1)
        if changes:cfg.update(changes)
        return CurvatureExchangeObjective(p,HeightAffineGate.from_artificial_array_problem(p),radial,theta,3,lower,upper,cfg=cfg)
    obj=make(); v=obj.initial_vector(initial); obj.initialize_pool(v); obj.evaluate(v)
    calls=obj.problem.calls; obj.fun(v); obj.jac(v); obj.constraint_fun(v)
    value_reuse=obj.problem.calls==calls; J=obj.constraint_jac(v)
    calls=obj.problem.calls; obj.constraint_jac(v); reuse=obj.problem.calls==calls
    auxiliary=v.copy(); auxiliary[-1]+=.1; obj.constraint_jac(auxiliary); auxiliary_reuse=obj.problem.calls==calls
    d=np.array([.2,-.3,.4,.25]); step=1e-6
    fd=(obj.constraint_fun(v+step*d)-obj.constraint_fun(v-step*d))/(2*step)
    error=float(np.max(abs(fd-J@d)))
    obj.evaluate(v); obj.constraint_jac(v)
    batch_error=obj.maximum_value_Jacobian_replay_difference
    allbatch=make({'radial_Jacobian_batch_owned_rows':len(radial)}); allbatch.set_pool(obj.pool,{'kind':'artificial-identical-pool'})
    other=allbatch.constraint_jac(v); full_error=float(np.max(abs(J-other)))
    identities_same=obj.problem.identity(initial)==allbatch.problem.identity(initial)
    split=make(); split.evaluate(split.initial_vector(initial)); improved=initial.copy(); improved[0]=.1
    data=split.physical_geometry(improved); mx=float(np.max(data['curvature']['maximum_absolute_by_point']))
    small=np.r_[improved,mx/(2*float(Q(split.cfg['curvature_scale_exact'])))]; dec=split.evaluate(small)['decision']
    separation=bool(dec['eligible_under_fixed_metric_and_physical_gates'] and not dec['independent_direct_curvature_pass']
        and np.array_equal(split.best_physical['vector'][:-1],improved)
        and not np.array_equal(split.best_auxiliary['vector'][:-1],improved))
    sparse=make(); w=sparse.initial_vector(initial); sparse.set_pool([2*len(radial)*len(theta)],{'kind':'artificial-omitted-curvature-rows'})
    w[-1]*=.5; sparse.evaluate(w); unused,missing,before=sparse.missing_rows(w)
    additions,detail=sparse.expand_pool(w,'artificial-eleven-group-completeness')
    unused,missing,after=sparse.missing_rows(w)
    coverage=bool(additions and before['omitted_violating_count']>after['omitted_violating_count'])
    zero=run_exchange(make(),initial,artificial_inputs_only=True,evaluate_only=True)
    failed_problem=_CurvatureArrayProblem(); failed=make(problem=failed_problem)
    fv=failed.initial_vector(initial); failed.initialize_pool(fv); failed.evaluate(fv)
    failed_problem.fail_after_calls=failed_problem.calls
    failure=run_exchange(failed,initial,artificial_inputs_only=True)
    preserved=failure['status']=='curvature-objective-or-solver-error' and failure['checkpoint']['best_physical_curvature_point'] is not None
    solve=make(); solve.set_pool([2*len(radial)*len(theta)],{'kind':'artificial-callback-exchange'})
    solved=run_exchange(solve,initial,artificial_inputs_only=True)
    callback=any(r.get('exit_reason')=='whole-grid-omitted-rows-exchange-request' for r in solved['solver']['rounds'])
    bad=make(); gd=bad.problem.geometry(initial,radial,theta,3); gd['Xt']=gd['Xs'].copy()
    try: curvature_forms(gd,bad.cfg); regular_reject=False
    except ValueError: regular_reject=True
    return {'schema':'actual-curvature-row-exchange-artificial-development-v1','artificial_inputs_only':True,
        'research_geometry_evaluated_or_optimized':False,'complete_selected_directional_Jacobian_error':error,
        'ordinary_same_state_batch_replay_error':batch_error,'selected_batch_vs_single_batch_Jacobian_error':full_error,
        'batching_changes_no_physical_identity':identities_same,'value_callbacks_share_one_state':value_reuse,
        'repeat_selected_Jacobian_reuses_cache':reuse,'auxiliary_only_change_reuses_all_geometry_and_derivatives':auxiliary_reuse,
        'physical_best_and_auxiliary_coverage_recorded_separately':separation,
        'omitted_curvature_rows_recorded_and_added':coverage,'degenerate_jets_rejected_without_regularization':regular_reject,
        'injected_batch_failure_preserves_eligible_best':preserved,'evaluation_only_status':zero['status'],
        'array_SLSQP_status':solved['status'],'array_SLSQP_error':solved.get('error'),
        'actual_array_callback_exchange_exercised':callback,
        'shared_budget_not_restarted':solved['solver']['minimize_invocation_count']<=4 and solve.geometry_evaluations<=45,
        'passed':bool(error<3e-7 and batch_error<1e-13 and full_error<1e-12 and identities_same and value_reuse
            and reuse and auxiliary_reuse and separation and coverage and regular_reject and preserved and callback
            and zero['solver']['minimize_invocation_count']==0 and solved.get('error') is None)}


def main():
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path,required=True); args=parser.parse_args()
    try: result=developer_check()
    except Exception as error:
        atomic_save(args.out,{'passed':False,'artificial_inputs_only':True,'source_files_sha256':implementation_hashes(),
            'error':{'type':type(error).__name__,'message':str(error)}}); raise
    result['source_files_sha256']=implementation_hashes(); atomic_save(args.out,result)
    print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
    if not result['passed']: raise SystemExit(1)


if __name__=='__main__': main()
