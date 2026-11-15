#!/usr/bin/env python3
"""Smooth spectral proposal rows; unchanged actual two-grid physical gates.

This module changes only the soft metric proposal values and their analytic
parameter derivatives. It reuses the frozen short-step/SOC controller, true
Schur/eta/curvature decisions, physical family, quadrature and source inputs.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import time
import numpy as np

from frame_collar_residual_audit import digest
from frame_metric_epigraph import metric_rows
from frame_curvature_epigraph_exchange import GROUPS, POSITION_JETS
from frame_metric_budget_recovery import (MetricRecoveryObjective, run_recovery,
    implementation_hashes as previous_hashes)
import frame_metric_budget_recovery as previous
import frame_metric_budget_restoration_rows as rows_api

POLICY='fixed-curvature-two-grid-spectral-metric-recovery-v1'
EPSILON_EXACT='1/100000000'
PROPOSAL_BRANCHES=[
    {'group_index':0,'legacy_slot_label':'metric_minus','spectral_sign':1,
     'new_proposal_row':'b-(e+sqrt(e^2+4*f^2+epsilon^2))/2'},
    {'group_index':1,'legacy_slot_label':'metric_plus','spectral_sign':-1,
     'new_proposal_row':'b-(-e+sqrt(e^2+4*f^2+epsilon^2))/2'}]


def implementation_hashes():
    result=previous_hashes();p=Path(__file__)
    result[p.name]=hashlib.sha256(p.read_bytes()).hexdigest();return result


def configuration(base):
    """Keep both actual budgets/cap; change only proposal semantics."""
    cfg=copy.deepcopy(base)
    if (Q(cfg['fixed_metric_budget_exact'])<=0 or Q(cfg['previous_qualified_metric_budget_exact'])
            <=Q(cfg['fixed_metric_budget_exact']) or Q(cfg['fixed_hard_curvature_cap_exact'])<=0):
        raise ValueError('positive new target below prior qualified budget and positive hard curvature cap required')
    cfg.update(metric_proposal_policy=POLICY,metric_proposal_epsilon_exact=EPSILON_EXACT,
        metric_proposal_branch_mapping=copy.deepcopy(PROPOSAL_BRANCHES),
        optimizer_objective='smooth true spectral metric excess then small normalized step; curvature is hard',
        metric_proposal_regularization_changes_no_physical_field_or_actual_gate=True,
        metric_proposal_upper_bias_bound_exact=str(Q(EPSILON_EXACT)/2),
        old_Schur_soft_objective_replaced_not_relabelled=True,
        raw_row_IDs_and_legacy_slot_names_retained_with_explicit_new_semantics=True,
        frozen_short_step_controller_reused=True)
    return cfg


def spectral_proposal_rows(e,f,budget,epsilon):
    e,f=np.broadcast_arrays(np.asarray(e,float),np.asarray(f,float))
    b,eps=float(budget),float(epsilon)
    if not(b>0 and eps>0 and np.isfinite(b) and np.isfinite(eps)
            and np.all(np.isfinite(e)) and np.all(np.isfinite(f))):
        raise ValueError('finite e/f, positive fixed proposal target and epsilon required')
    root=np.hypot(np.hypot(e,2*f),eps)
    return np.stack([b-(e+root)/2,b-(-e+root)/2])


def spectral_parameter_rows(e,f,de,df,groups,epsilon):
    """One new metric row per selected point, with stable derivative at zero."""
    e,f,de,df=np.asarray(e,float),np.asarray(f,float),np.asarray(de,float),np.asarray(df,float)
    g=np.asarray(groups)
    if (e.ndim!=1 or f.shape!=e.shape or g.shape!=e.shape or g.dtype.kind not in 'iu'
            or np.any((g<0)|(g>1)) or de.ndim!=2 or de.shape[0]!=len(e) or df.shape!=de.shape
            or not all(np.all(np.isfinite(v)) for v in (e,f,de,df)) or float(epsilon)<=0):
        raise ValueError('selected finite e/f and their common-layout parameter Jacobians required')
    root=np.hypot(np.hypot(e,2*f),float(epsilon))
    sign=np.where(g==0,1.,-1.)
    return -.5*(sign[:,None]*de+(e[:,None]*de+4*f[:,None]*df)/root[:,None])


def selected_spectral_parameter_jacobian(data,a,groups,side,cfg):
    # Retain every established physical/curvature row and its consistency guard.
    result=rows_api.selected_parameter_jacobian(data,a,groups,side,cfg)
    g=np.asarray(groups);mask=g<2
    if np.any(mask):
        U,T=np.asarray(data['Xs'])[mask],np.asarray(data['T'])[mask]
        JU,JT=np.asarray(data['jac_Xs'])[mask],np.asarray(data['jac_T'])[mask]
        e=np.sum(U*U,axis=1)-1;f=np.sum(U*T,axis=1)
        de=2*np.einsum('ic,icn->in',U,JU)
        df=np.einsum('ic,icn->in',T,JU)+np.einsum('ic,icn->in',U,JT)
        result[mask]=spectral_parameter_rows(e,f,de,df,g[mask],float(Q(cfg['metric_proposal_epsilon_exact'])))
    if not np.all(np.isfinite(result)):raise FloatingPointError('nonfinite spectral selected Jacobian')
    return result


class SpectralMetricRecoveryObjective(MetricRecoveryObjective):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        if self.cfg.get('metric_proposal_policy')!=POLICY or self.cfg.get('metric_proposal_epsilon_exact')!=EPSILON_EXACT:
            raise ValueError('explicit frozen spectral proposal configuration required')
        for name,old in list(self.constraint_definitions.items()):
            definition=copy.deepcopy(old);oldhash=definition.pop('definition_sha256')
            definition.update(schema=POLICY+'-constraint-definition',
                inherited_geometry_and_gate_definition_sha256=oldhash,
                proposal_metric_branch_mapping=copy.deepcopy(PROPOSAL_BRANCHES),
                proposal_epsilon_exact=EPSILON_EXACT,
                true_eta_Schur_old_budget_and_all_hard_gate_formulas_unchanged=True,
                integer_row_ids_preserved_but_metric_proposal_values_and_derivatives_changed=True,
                source_files_sha256=implementation_hashes())
            definition['definition_sha256']=digest(definition);self.constraint_definitions[name]=definition
        self.evaluation_definition.update(schema=POLICY+'-evaluation',
            metric_proposal_policy=POLICY,metric_proposal_branch_mapping=copy.deepcopy(PROPOSAL_BRANCHES),
            metric_proposal_epsilon_exact=EPSILON_EXACT,
            actual_gate_definition_not_the_smooth_proposal=True,
            constraint_definition_sha256={k:v['definition_sha256'] for k,v in self.constraint_definitions.items()},
            implementation_source_sha256=implementation_hashes())
        self.evaluation_sha256=digest(self.evaluation_definition)

    def rows_from_geometry(self,data,zeta):
        result=super().rows_from_geometry(data,zeta)
        result[:2]=spectral_proposal_rows(data['e'],data['f'],
            float(Q(self.cfg['fixed_metric_budget_exact'])),float(Q(EPSILON_EXACT)))
        return result

    def proposal_diagnostic(self,rows,data):
        b=float(Q(self.cfg['fixed_metric_budget_exact']));eps=float(Q(EPSILON_EXACT))
        sm,sp=metric_rows(data['e'],data['f'],b)
        eta=np.asarray(data['eta']);maximum=float(np.max(eta))
        spectral_max=b-float(np.min(rows[:2]))
        return {'proposal_policy':POLICY,'epsilon_exact':EPSILON_EXACT,
            'actual_full_spectral_proposal_slack':max(0.,spectral_max-b),
            'actual_full_old_Schur_slack':max(0.,-float(min(np.min(sm),np.min(sp)))),
            'actual_true_eta_excess':max(0.,maximum-b),
            'actual_spectral_maximum':spectral_max,'actual_true_eta_maximum':maximum,
            'maximum_spectral_bias_evaluated':spectral_max-maximum,
            'analytic_upper_bias_bound':eps/2,'floating_evaluations_not_continuous_bounds':True}

    def evaluate(self,vector):
        result=super().evaluate(vector)
        detail=self.proposal_diagnostic(self.epigraph_cache['rows'],self.geometry_cache)
        result['metric_proposal_diagnostic']=detail
        number=result['physical_geometry_evaluation']
        if number in self.saved_coarse_trials:
            self.saved_coarse_trials[number]['metric_proposal_diagnostic']=copy.deepcopy(detail)
        return result

    def fine_decision(self,state):
        before=self.fine_evaluations;result=super().fine_decision(state)
        if self.fine_evaluations>before:
            self.saved_fine_trials[-1]['metric_proposal_diagnostic']=self.proposal_diagnostic(
                self.fine_cache['rows'],self.fine_cache['data'])
        return result

    def constraint_jac(self,vector):
        result=super().constraint_jac(vector)
        d=self.derivative_cache;data=self.geometry_cache;count=data['e'].size
        groups=self.pool//count;mask=groups<2;points=(self.pool%count)[mask];pp=d['pool_points'][mask]
        result[mask,:self.n]=spectral_parameter_rows(data['e'].ravel()[points],data['f'].ravel()[points],
            d['de_metric'][pp],d['df_metric'][pp],groups[mask],float(Q(EPSILON_EXACT)))
        return result

    def set_pool(self,indices,reason):
        record=super().set_pool(indices,reason)
        record['proposal_metric_branch_mapping']=copy.deepcopy(PROPOSAL_BRANCHES)
        record['proposal_metric_semantics_sha256']=digest(PROPOSAL_BRANCHES)
        return record

    def set_fine_pool(self,indices,reason):
        record=super().set_fine_pool(indices,reason)
        record['proposal_metric_branch_mapping']=copy.deepcopy(PROPOSAL_BRANCHES)
        record['proposal_metric_semantics_sha256']=digest(PROPOSAL_BRANCHES)
        return record

    # The complete fine two-jet batching body below is copied from the frozen
    # previous module. Only the selected row-derivative helper is substituted.
    def fine_derivatives(self,state):
        self.fine_decision(state)
        if not len(self.fine_pool):raise ValueError('initialize full fine pool before derivatives')
        d=self.fine_derivative_cache
        if d is not None and d['pool_version']==self.fine_pool_version and np.array_equal(state,d['state']):
            return d['J']
        before=time.monotonic(); Nr,Nt=len(self.radial),len(self.fine_theta)
        groups=self.fine_pool//(Nr*Nt); points=self.fine_pool%(Nr*Nt)
        radial_ids=np.unique(points//Nt); J=np.empty((len(points),self.n)); covered=np.zeros(len(points),bool)
        width=int(self.cfg['fine_Jacobian_owned_radial_rows']); self.fine_Jacobian_refreshes+=1
        for start in range(0,len(radial_ids),width):
            self._wall(); owned=radial_ids[start:start+width]
            selected=np.flatnonzero(np.isin(points//Nt,owned)); query=np.unique(np.r_[0,owned,Nr-1])
            second=bool(np.any(groups[selected]>=7))
            data=self.problem.geometry(state,self.radial[query],self.fine_theta,self.order,
                jacobian=True,full_two_jet_jacobian=second)
            self.fine_Jacobian_batches+=1
            self.fine_Jacobian_maximum_query_radial_rows=max(self.fine_Jacobian_maximum_query_radial_rows,len(query))
            maximum=0.; scale=1.
            for key in POSITION_JETS+('center',):
                current=np.asarray(data[key]); target=np.asarray(self.fine_cache['data'][key])[query]
                if current.shape!=target.shape or not np.all(np.isfinite(current)):
                    raise FloatingPointError('fine batch ordinary replay: '+key)
                error=float(np.max(abs(current-target))); maximum=max(maximum,error)
                scale=max(scale,float(np.max(abs(target))))
                self.fine_batch_replay_maxima[key]=max(self.fine_batch_replay_maxima[key],error)
            for group in ['metric','height']:
                for key,target0 in self.fine_cache['data'].get(group,{}).items():
                    current=np.asarray(data[group][key]); target=np.asarray(target0)[query]
                    if current.shape!=target.shape or not np.all(np.isfinite(current)):
                        raise FloatingPointError('fine batch common primitive replay: '+group+'/'+key)
                    error=float(np.max(abs(current-target))); maximum=max(maximum,error)
                    scale=max(scale,float(np.max(abs(target))))
                    self.fine_batch_replay_maxima[group]=max(self.fine_batch_replay_maxima[group],error)
            if maximum>self.cfg['value_Jacobian_replay_relative_tolerance']*scale:
                raise ArithmeticError('batch changed same-state full ordinary two jets beyond floating replay tolerance')
            requested=POSITION_JETS if second else ('X','Xs','Xt','T')
            total=0
            for key in requested:
                jac=np.asarray(data['jac_'+key])
                if jac.shape!=(len(query),Nt,3,self.n) or not np.all(np.isfinite(jac)):
                    raise FloatingPointError('required complete fine parameter jet missing: '+key)
                total+=jac.nbytes
            self.fine_Jacobian_maximum_returned_bytes=max(self.fine_Jacobian_maximum_returned_bytes,total)
            ri=np.searchsorted(query,points[selected]//Nt); ti=points[selected]%Nt
            small={k:np.asarray(data[k])[ri,ti] for k in POSITION_JETS}
            small.update({'jac_'+k:np.asarray(data['jac_'+k])[ri,ti] for k in requested})
            J[selected]=selected_spectral_parameter_jacobian(small,np.asarray(data['metric']['a'])[ri],
                groups[selected],self.gate.side,self.cfg)
            covered[selected]=True
            del data,small,jac
        if not np.all(covered) or not np.all(np.isfinite(J)):raise ArithmeticError('fine eleven-group Jacobian incomplete')
        J.setflags(write=False)
        self.fine_derivative_cache={'state':np.asarray(state).copy(),'pool_version':self.fine_pool_version,'J':J}
        self.fine_Jacobian_maximum_retained_bytes=max(self.fine_Jacobian_maximum_retained_bytes,J.nbytes)
        self.fine_Jacobian_seconds+=time.monotonic()-before; self._wall(); return J

    def snapshot(self):
        result=super().snapshot()
        result.update(schema=POLICY+'-checkpoint',metric_proposal_policy=POLICY,
            inherited_metric_short_step_controller=previous.POLICY,
            proposal_metric_branch_mapping=copy.deepcopy(PROPOSAL_BRANCHES),
            proposal_epsilon_exact=EPSILON_EXACT,
            proposal_only_upper_bias_bound_exact=str(Q(EPSILON_EXACT)/2),
            true_eta_Schur_and_all_physical_acceptance_gates_unchanged=True)
        return result


def run_spectral_recovery(objective,initial,*,known_metric_locations=(),artificial_inputs_only=False,evaluate_only=False):
    if not isinstance(objective,SpectralMetricRecoveryObjective):
        raise ValueError('the explicit spectral-proposal objective is required')
    result=run_recovery(objective,initial,known_metric_locations=known_metric_locations,
        artificial_inputs_only=artificial_inputs_only,evaluate_only=evaluate_only)
    result['solver']['inherited_controller_method']=result['solver']['method']
    result['solver']['method']=POLICY
    result['proposal_metric_branch_mapping']=copy.deepcopy(PROPOSAL_BRANCHES)
    result['proposal_epsilon_exact']=EPSILON_EXACT
    result['old_actual_metric_gates_not_replaced_by_smoothed_values']=True
    return result


def developer_check():
    """Only new spectral rows, mixed selected derivatives and a tiny array family."""
    from frame_curvature_epigraph_exchange import _CurvatureArrayProblem
    from frame_height_affine_gate import HeightAffineGate
    from frame_curvature_soc_steps import configuration as original_configuration
    eps=float(Q(EPSILON_EXACT));b=.26
    e0=np.array([0.,.2672]);f0=np.array([.2672,0.])
    e1=np.array([0.,.27]);f1=np.array([.265,0.])
    sm0=np.stack(metric_rows(e0,f0,b));sm1=np.stack(metric_rows(e1,f1,b))
    old0,old1=max(0.,-float(sm0.min())),max(0.,-float(sm1.min()))
    new0=max(0.,-float(spectral_proposal_rows(e0,f0,b,eps).min()))
    new1=max(0.,-float(spectral_proposal_rows(e1,f1,b,eps).min()))
    mismatch=bool(old1<old0 and new1>new0)
    e=np.array([0.,.2,-.3,1e-12,-2e-10]);f=np.array([0.,-.15,.07,2e-12,1e-10])
    rows=spectral_proposal_rows(e,f,b,eps)
    eta=(abs(e)+np.hypot(e,2*f))/2;bias=b-rows.min(axis=0)-eta
    bounded=bool(np.min(bias)>=-16*np.finfo(float).eps and np.max(bias)<=eps/2+16*np.finfo(float).eps)
    de=np.array([[1.,-.2],[.3,.1],[-.1,.4],[.2,-.3],[.1,.2]])
    df=de[:,::-1]*.3;groups=np.array([0,1,0,1,0]);j=spectral_parameter_rows(e,f,de,df,groups,eps)
    zero=spectral_parameter_rows(np.array([0.,0.]),np.array([0.,0.]),
        np.array([[1.,2.],[1.,2.]]),np.ones((2,2)),np.array([0,1]),eps)
    zero_ok=np.array_equal(zero,np.array([[-.5,-1.],[.5,1.]])) and np.all(np.isfinite(j))
    p=_CurvatureArrayProblem();initial=np.array([.3,.6,.6])
    radial=np.array([0.,.2,.4,.7,1.]);theta=np.arange(12)*2*np.pi/12
    lower=np.array([-.8,-1.,-1.]);upper=np.array([2.,1.,1.])
    oldcfg=previous.configuration(original_configuration(),target='1/100',curvature_cap='3')
    cfg=configuration(oldcfg);cfg.update(radial_Jacobian_batch_owned_rows=2,fine_Jacobian_owned_radial_rows=2,
        max_linear_models=2,max_seconds=20.)
    config_roundtrip=json.loads(json.dumps(cfg))==cfg
    gate=HeightAffineGate.from_artificial_array_problem(p)
    obj=SpectralMetricRecoveryObjective(p,gate,radial,theta,3,lower,upper,cfg=cfg)
    vector=obj.vector(initial);c=obj.evaluate(vector);f=obj.fine_decision(initial)
    identity=p.identity(initial)
    obj.initialize_pool(vector);obj.initialize_fine_pool(initial)
    base,J,groups,tol=obj.linear_rows(vector);direction=np.array([.2,-.3,.4]);step=1e-6
    def values(x):
        return np.r_[obj.constraint_fun(obj.vector(x)),obj.fine_rows(x).reshape(-1)[obj.fine_pool]]
    fd=(values(initial+step*direction)-values(initial-step*direction))/(2*step)
    jacerror=float(np.max(abs(fd-J@direction)))
    old=MetricRecoveryObjective(p,gate,radial,theta,3,lower,upper,cfg=oldcfg)
    samegate=(old.evaluate(old.vector(initial))['decision']==c['decision']
        and old.fine_decision(initial)==f and p.identity(initial)==identity)
    olddata=old.geometry_cache;newdata=obj.geometry_cache
    # Compare formulas at the identical initial state, not the most recent FD query.
    obj.evaluate(vector);obj.fine_decision(initial)
    newdata=obj.geometry_cache
    allold=old.rows_from_geometry(olddata,old.fixed_zeta);allnew=obj.rows_from_geometry(newdata,obj.fixed_zeta)
    hard_same=bool(np.array_equal(allold[2:],allnew[2:]))
    index_semantics=bool(obj.pool_history[-1]['proposal_metric_branch_mapping']==list(PROPOSAL_BRANCHES)
        or obj.pool_history[-1]['proposal_metric_branch_mapping']==PROPOSAL_BRANCHES)
    before_count=obj.geometry_evaluations
    obj.linear_rows(vector);obj.linear_rows(vector)
    cache_same=obj.geometry_evaluations==before_count
    # Use a fresh small array model for the unchanged bounded controller.
    runobj=SpectralMetricRecoveryObjective(p,gate,radial,theta,3,lower,upper,cfg=cfg)
    result=run_spectral_recovery(runobj,initial,artificial_inputs_only=True)
    accepted=result['checkpoint'].get('accepted_iterates',[])
    values_eta=[v['maximum_eta_on_both_grids'] for v in accepted]
    accepted_ok=len(values_eta)>=2 and all(b<a for a,b in zip(values_eta,values_eta[1:]))
    accepted_hard=all(v['coarse']['single_grid_hard_gate_pass'] and v['fine']['single_grid_hard_gate_pass']
        and v['coarse']['previous_metric_budget_pass'] and v['fine']['previous_metric_budget_pass'] for v in accepted)
    passed=bool(mismatch and bounded and zero_ok and config_roundtrip and jacerror<1e-7 and samegate and hard_same
        and index_semantics and cache_same and accepted_ok and accepted_hard)
    return {'schema':POLICY+'-artificial-check','artificial_inputs_only':True,
        'configuration_JSON_roundtrip_preserves_strict_comparison':config_roundtrip,
        'research_candidate_geometry_evaluated_or_optimized':False,
        'Schur_slack_counterexample':{'before':old0,'after':old1,'spectral_before':new0,'spectral_after':new1,
            'new_objective_rejects_the_wrong_direction':mismatch},
        'upper_bias_maximum':float(np.max(bias)),'upper_bias_bound_exact':str(Q(EPSILON_EXACT)/2),
        'upper_bias_bound_check_pass':bounded,'finite_exact_zero_anisotropy_derivative':bool(zero_ok),
        'complete_coarse_fine_selected_Jacobian_maximum_error':jacerror,
        'same_physical_identity_and_original_actual_gate_decisions':samegate,
        'all_hard_row_values_bitwise_same':hard_same,'explicit_old_ID_new_branch_mapping':index_semantics,
        'same_state_cache_does_not_recompute_geometry':cache_same,
        'tiny_nonlinear_controller_status':result['status'],'tiny_nonlinear_controller_error':result.get('error'),
        'tiny_accepted_eta':values_eta,'tiny_accepted_true_eta_strictly_decreases':accepted_ok,
        'tiny_accepted_points_pass_both_true_hard_and_old_metric_gates':accepted_hard,
        'actual_controller_LP_count':result['solver']['linear_program_invocation_count'],'passed':passed}
