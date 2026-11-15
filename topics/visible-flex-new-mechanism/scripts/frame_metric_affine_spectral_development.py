#!/usr/bin/env python3
"""New artificial development for affine-e/f spectral proposals only.

No old development suite is invoked. The tiny original-family fixture is a
new de/df and cache-interface check, not a scientific surface or accepted
candidate. All execution is reserved for public repository Actions.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import resource
import time
from types import SimpleNamespace
from unittest.mock import patch

import numpy as np

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import ArrayLP
from frame_metric_affine_spectral_model import (
    N, EPSILON_EXACT, AffineSpectralModel, phi, phi_gradient,
    solve_affine_primary, error_decomposition, partial_row_error,
    norm_curvature_diagnostic)
from frame_selected_row_metric_observables import SelectedMetricObservables
from frame_metric_height159_affine_spectral import (
    AffineSpectralHeight159Objective, configuration)
from frame_selected_row_radial_jacobian_development import _setup
from frame_height_affine_gate import HeightAffineGate
from frame_height_null_gate import FiveNullHeightGate
from frame_entry_single_q import SingleQGrid
from frame_metric_height159_soc_hold import require_public_research_environment

SCHEMA='affine-ef-spectral-new-artificial-development-v1'


def implementation_hashes():
    from frame_metric_height159_affine_spectral import implementation_hashes as inherited
    result=inherited()
    # A frozen fixture builder, not the old developer entry point.
    import frame_selected_row_radial_jacobian_development as fixtures
    result[Path(fixtures.__file__).name]=hashlib.sha256(Path(fixtures.__file__).read_bytes()).hexdigest()
    p=Path(__file__);result[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
    return result


def _relative(a,b):
    a,b=np.asarray(a,float),np.asarray(b,float)
    if a.shape!=b.shape:return float('inf')
    return float(np.max(abs(a-b),initial=0.))/max(1.,float(np.max(abs(b),initial=0.)))


def _reject(callback):
    try:callback()
    except (ValueError,ArithmeticError,KeyError,TypeError):return True
    return False


def _array_model():
    """Only labelled arrays: two nonlinear soft branches and one fixed hard row."""
    cfg={'fixed_metric_budget_exact':'13/50','metric_proposal_epsilon_exact':EPSILON_EXACT,
        'value_Jacobian_replay_relative_tolerance':5e-12,
        'metric_row_tolerance':1e-9,'linear_model_residual_limit':1e-7,
        'linear_model_improvement_floor':1e-10,
        'linear_program_seconds':10.,'max_linear_models':12,'max_seconds':120.,
        'new_affine_array_fixture_only':True}
    e=np.array([.4,.4]);f=np.array([.1,.1]);groups=np.array([0,1],np.int64)
    de=np.zeros((2,N));df=de.copy();de[:,0]=-1.;df[:,1]=1.
    pe,pf=phi_gradient(e,f,groups,float(Q(EPSILON_EXACT)))
    gradient=pe[:,None]*de+pf[:,None]*df
    values=np.r_[.26-phi(e,f,groups,float(Q(EPSILON_EXACT))),1.]
    J=np.vstack([-gradient,np.zeros(N)])
    all_groups=np.array([0,1,2],np.int64)
    A=np.zeros((3+2*N,N+2));b=np.r_[values,np.zeros(2*N)]
    A[:3,:N]=-J;A[:2,N]=-1.
    A[3:3+N,:N]=np.eye(N);A[3+N:,:N]=-np.eye(N)
    A[3:,-1]=-1.
    c=np.r_[np.zeros(N),1.,.001]
    lo=np.r_[-np.ones(N),0.,0.];hi=np.r_[np.ones(N),np.inf,1.]
    tags=[{'grid':'labelled-array','flat_row_id':i,'group':int(all_groups[i])} for i in range(3)]
    primary=ArrayLP(A,b,c,lo,hi,information={
        'rho_out':0.,'initial_selected_and_constant_metric_slack':max(0.,float(np.max(-values[:2]))),
        'active_original_rows':tags,'radius_independent_model_sha256':digest({'new_array_only':True})})
    primary.active_values=values;primary.active_J=J;primary.active_groups=all_groups
    primary.step_scale=np.ones(N);primary.state=np.zeros(N)
    model=AffineSpectralModel(primary,e,f,de,df,tags[:2],cfg,
        observable_binding={'explicit_new_artificial_arrays':True})
    return primary,model,cfg


def _stub_solver(point,*,extra_rho=0.,raise_at=None):
    calls=[]
    def solver(lp,cfg):
        calls.append({'matrix_rows':len(lp.b),'time_limit':cfg['linear_program_seconds']})
        if raise_at is not None and len(calls)==raise_at:raise RuntimeError('new-stub-LP-error')
        p=np.asarray(point,float).copy()
        h=float(np.max(abs(p)))
        v=np.r_[p,0.,h]
        rows=lp.A[:,N]<0
        rho=max(0.,float(np.max((lp.A[rows]@v-lp.b[rows])/(-lp.A[rows,N]),initial=-np.inf)))+extra_rho
        v[N]=rho
        residual=lp.residual(v)
        return p,{'LP_invoked':True,'status':0,'success':True,'normalized_step_norm':h,
            'predicted_metric_slack':rho,'method':'new-labelled-LP-stub-not-HiGHS',
            'maximum_linear_row_violation':residual['maximum_original_linear_row_violation'],
            'maximum_linear_bound_violation':residual['maximum_original_linear_bound_violation'],
            'primary_step_cost_diagnostic':{
                'actual_trust_normalized_step_norm':h,
                'returned_weighted_objective':float(lp.c@v),
                'returned_predicted_metric_slack':rho},
            'projection':{'original163_geometry_J_still_computed_then159_independent_columns_returned':True}}
    return solver,calls


def array_checks():
    primary,model,cfg=_array_model()
    p=np.zeros(N);p[:2]=[.1,.1]
    evaluated=model.evaluated(p)
    A,b,record=model.cuts(p,np.array([0,1]))
    q=np.zeros(N);q[:2]=[-.05,.08]
    eq=model.evaluated(q);pq=np.r_[q,0.,float(np.max(abs(q)))]
    contact=np.r_[p,evaluated['slack'],float(np.max(abs(p)))]
    grad0=phi_gradient(np.zeros(2),np.zeros(2),np.array([0,1]),float(Q(EPSILON_EXACT)))
    v=np.stack([evaluated['e'],2*evaluated['f'],np.full(2,float(Q(EPSILON_EXACT)))],axis=1)
    sign=np.array([1.,-1.])
    epigraph_rhs=2*(model.target+evaluated['slack'])-sign*evaluated['e']
    ledger={'linear_program_invocation_count':0,'primary_LP_invocation_count':0}
    progress={};solver,calls=_stub_solver(p)
    got,report=solve_affine_primary(primary,model,cfg,ledger,progress=progress,
        wall=lambda:None,remaining_seconds=lambda:120.,solve_one=solver)
    p2,m2,c2=_array_model();l2={'linear_program_invocation_count':11,'primary_LP_invocation_count':0}
    r2={};s2,calls2=_stub_solver(p)
    got2,r2=solve_affine_primary(p2,m2,c2,l2,progress=r2,wall=lambda:None,
        remaining_seconds=lambda:120.,solve_one=s2)
    p3,m3,c3=_array_model();l3={'linear_program_invocation_count':0,'primary_LP_invocation_count':0}
    r3={};s3,calls3=_stub_solver(p,raise_at=1)
    raised=False
    try:solve_affine_primary(p3,m3,c3,l3,progress=r3,wall=lambda:None,
        remaining_seconds=lambda:120.,solve_one=s3)
    except RuntimeError:raised=True
    p4,m4,c4=_array_model();l4={'linear_program_invocation_count':12,'primary_LP_invocation_count':0}
    r4={};s4,calls4=_stub_solver(p)
    got4,r4=solve_affine_primary(p4,m4,c4,l4,progress=r4,wall=lambda:None,
        remaining_seconds=lambda:120.,solve_one=s4)
    p5,m5,c5=_array_model();l5={'linear_program_invocation_count':0,'primary_LP_invocation_count':0}
    r5={};s5,calls5=_stub_solver(p,extra_rho=.1)
    got5,r5=solve_affine_primary(p5,m5,c5,l5,progress=r5,wall=lambda:None,
        remaining_seconds=lambda:120.,solve_one=s5)
    actual_e=evaluated['e']-.01;actual_f=evaluated['f'].copy()
    actual_phi=phi(actual_e,actual_f,model.groups,model.epsilon)
    true=np.maximum(.5*(np.abs(actual_e)+np.hypot(actual_e,2*actual_f))-.26,0.)
    error=error_decomposition(model,p,actual_e,actual_f,
        complete_smooth_slack=max(0.,float(np.max(actual_phi-.26))),
        complete_true_slack=float(np.max(true)),complete_two_grid_available=True,
        observed_grid_labels=['labelled-array'])
    partial=partial_row_error(model,p,np.array([0]),actual_e[:1],actual_f[:1],'coarse')
    stable=error['norm_curvature_direct_and_stable_diagnostic']
    rounded_cancellation=norm_curvature_diagnostic(
        np.array([1.]),np.array([0.]),np.array([-2.]),np.array([0.]),float(Q(EPSILON_EXACT)))
    checks={
        'same_two_branch_norm_epigraph':bool(np.all(np.linalg.norm(v,axis=1)<=epigraph_rhs+1e-14)),
        'supporting_cuts_are_tangent_and_global_underestimators':bool(
            record['contact_max_absolute_residual']<1e-14
            and np.max(A@pq-b-(eq['phi']-.26))<=1e-14),
        'original_scalar_tangent_has_strict_spectral_curvature_gap':bool(
            np.min(evaluated['phi']-evaluated['scalar_linear_phi'])>1e-3),
        'zero_e_f_gradient_is_finite_without_dividing_by_f':bool(
            np.array_equal(grad0[0],np.array([.5,-.5])) and np.array_equal(grad0[1],np.zeros(2))),
        'inner_LPs_are_charged_and_contact_cut_ends_new_fixture':bool(
            len(calls)==2 and ledger['linear_program_invocation_count']==2
            and ledger['primary_LP_invocation_count']==2
            and report['status']=='evaluated-affine-epigraph-gap-met'
            and np.array_equal(got,p)),
        'last_shared_LP_returns_honest_inexact_repaired_prediction':bool(
            len(calls2)==1 and l2['linear_program_invocation_count']==12
            and r2['returned_inexact_cut_model']
            and abs(r2['predicted_metric_slack']-m2.slack(got2))<1e-14),
        'solver_exception_keeps_started_call_and_original_error':bool(
            raised and len(calls3)==1 and l3['linear_program_invocation_count']==1
            and r3['inner_LPs'][0]['status']=='LP-call-raised'
            and r3['inner_LPs'][0]['error']['message']=='new-stub-LP-error'),
        'exhausted_shared_budget_never_calls_stub':bool(got4 is None and not calls4 and l4['linear_program_invocation_count']==12),
        'LP_auxiliary_above_norm_is_not_confused_with_prediction':bool(
            r5['repaired_rho_auxiliary']>=r5['predicted_metric_slack']
            and r5['inner_LPs'][0]['raw_epigraph_gap']<0
            and abs(r5['predicted_metric_slack']-m5.slack(got5))<1e-14),
        'row_two_piece_and_maximum_four_piece_identities':bool(
            error['row_identity_max_absolute_error']<1e-14
            and error['global_identity_absolute_error']<1e-14
            and error['row_actual_ef_nonlinearity']['minimum']['value']<0
            and error['row_actual_ef_nonlinearity']['maximum']['value']>0
            and stable['stable_identity_applicable_rows']==2
            and stable['direct_stable_max_absolute_difference_where_both_available']<1e-14
            and rounded_cancellation['stable_identity_applicable_rows']==0
            and rounded_cancellation['direct_remainder_range']['minimum']==1.),
        'missing_fine_produces_only_observed_row_identity':bool(
            not partial['complete_two_grid_available']
            and not partial['global_maximum_decomposition_available']
            and _reject(lambda:error_decomposition(model,p,actual_e,actual_f,
                complete_smooth_slack=0.,complete_true_slack=0.,
                complete_two_grid_available=False,observed_grid_labels=['coarse']))),
        'any_later_supporting_cut_keeps_full_norm_repaired_candidate':bool(
            np.max(A@contact-b)<=1e-14 and primary.residual(contact)['maximum_original_linear_row_violation']<=1e-14)}
    return {'checks':{k:bool(v) for k,v in checks.items()},'all_passed':bool(all(checks.values())),
        'actual_HiGHS_LP_calls':0,'new_stub_LP_calls':sum(map(len,[calls,calls2,calls3,calls4,calls5])),
        'new_model_error_example':error,'new_inner_report':report,
        'no_old_developer_entry_or_scientific_inputs':True}


def observable_and_cache_checks():
    old,reference,field,state,base,oldcfg,nodes,radial=_setup(1)
    cfg=configuration(oldcfg);theta=np.arange(8)*2*np.pi/8
    evaluator=SelectedMetricObservables(field,cfg)
    ordinary=field.geometry(state,radial,theta,2)
    nr,nt=len(radial),len(theta);count=nr*nt
    raw=[g*count+ir*nt+((g+2*ir+1)%nt) for g in (0,1) for ir in range(nr)]
    ids=np.array(raw[::-1]+[raw[3],raw[3]],np.int64)
    bound=evaluator.bind_ordinary(state,radial,theta,ordinary,owner='new-artificial-current-cache')
    with patch.object(field,'geometry',side_effect=AssertionError('no geometry inside new derivative pass')), \
         patch.object(old,'geometry',side_effect=AssertionError('no old full J')), \
         patch.object(SingleQGrid,'basis_jacobian',side_effect=AssertionError('no full parameter basis')):
        J,diag,obs=evaluator.evaluate(state,radial,theta,ids,bound,side=1,owned_width=3)
    directions=[]
    u=np.sin(np.arange(159)+.7);u/=np.linalg.norm(u);directions.append(u)
    h=np.zeros(159);h[154:]=[1.,-.5,.25,.3,-.2];h/=np.linalg.norm(h);directions.append(h)
    fd=[]
    for direction in directions:
        delta=2e-7
        plus=field.geometry(state+delta*direction,radial,theta,2)
        minus=field.geometry(state-delta*direction,radial,theta,2)
        point=obs['row_ids']%count
        def ef(data):
            U=np.asarray(data['Xs']).reshape(-1,3)[point]
            T=np.asarray(data['T']).reshape(-1,3)[point]
            return np.sum(U*U,axis=1)-1,np.sum(U*T,axis=1)
        ep,fp=ef(plus);em,fm=ef(minus)
        fd.append({'de_relative_error':_relative(obs['de']@direction,(ep-em)/(2*delta)),
                   'df_relative_error':_relative(obs['df']@direction,(fp-fm)/(2*delta))})
    pe,pf=phi_gradient(obs['e'],obs['f'],obs['groups'],float(Q(EPSILON_EXACT)))
    chain=-pe[:,None]*obs['de']-pf[:,None]*obs['df']
    reference_data=old.geometry(reference,radial,theta,2)
    original_gate=HeightAffineGate.from_frozen_problem(old,reference,reference_data)
    lower=np.r_[np.full(154,-8.),np.full(9,-1.)];upper=-lower
    gate=FiveNullHeightGate.from_original(original_gate,field,lower,upper)
    objective=AffineSpectralHeight159Objective(field,gate,radial,theta,2,
        gate.coordinate_lower,gate.coordinate_upper,cfg=cfg,radial_nodes_exact=[str(x) for x in nodes])
    def soft_ids(nt0):
        ct=len(radial)*nt0
        return np.array(sorted({g*ct+ir*nt0+((g+ir+1)%nt0)
            for g in (0,1) for ir in (0,len(radial)//2,len(radial)-1)}),np.int64)
    objective.set_pool(soft_ids(8),{'kind':'new-observable-cache-fixture'})
    objective.set_fine_pool(soft_ids(16),{'kind':'new-observable-cache-fixture'})
    objective.linear_rows(objective.vector(state))
    coarse=objective.derivative_cache;fine=objective.fine_derivative_cache
    before=(objective.geometry_evaluations,objective.fine_evaluations,
        objective.factorized_statistics['coarse']['refreshes'],objective.factorized_statistics['fine']['refreshes'])
    objective.linear_rows(objective.vector(state))
    after=(objective.geometry_evaluations,objective.fine_evaluations,
        objective.factorized_statistics['coarse']['refreshes'],objective.factorized_statistics['fine']['refreshes'])
    objective.accepted_cache={'state':state.copy(),'coarse':objective.geometry_cache,'fine':objective.fine_cache,
        'coarse_derivatives':coarse,'fine_derivatives':fine}
    trial=state.copy();trial[3]+=1e-8
    objective.evaluate(objective.vector(trial));objective.fine_decision(trial)
    value_count=(objective.geometry_evaluations,objective.fine_evaluations)
    objective.linear_rows(objective.vector(state))
    rollback=(value_count==(objective.geometry_evaluations,objective.fine_evaluations)
        and objective.derivative_cache is coarse and objective.fine_derivative_cache is fine)
    coarse_obs=coarse['metric_observables'];fine_obs=fine['metric_observables']
    old_refresh=objective.factorized_statistics['coarse']['refreshes']
    old_ids=set(int(x) for x in objective.pool)
    extra=next(i for i in range(2*len(radial)*8) if i not in old_ids)
    objective.set_pool(list(old_ids)+[extra],{'kind':'new-observable-cache-growth'})
    objective.linear_rows(objective.vector(state))
    checks={
        'direct_metric_de_df_match_new_two_direction_finite_differences':all(
            v[k]<1e-6 for v in fd for k in ('de_relative_error','df_relative_error')),
        'new_observables_reproduce_existing_scalar_J_chain':_relative(chain,J)<5e-12,
        'original_order_and_exact_repeated_IDs_retained':np.array_equal(obs['row_ids'],ids),
        'both_real_null_height_and_tangent_columns_exercised':bool(
            np.max(abs(obs['de'][:,154:]))>0 and np.max(abs(obs['df'][:,:154]))>0),
        'no_full_parameter_geometry_tensor_or_extra_field_call':bool(
            diag['full_angle_163_or159_parameter_tensors_formed']==0
            and diag['extra_field_J_or_ordinary_value_calls']==0),
        'same_state_cache_reuses_observable_arrays':before==after,
        'actual_parent_rollback_retains_same_de_df_object':rollback,
        'coarse_and_fine_are_separately_bound':bool(
            coarse_obs['binding_sha256']!=fine_obs['binding_sha256']
            and coarse_obs['full_theta_sha256']!=fine_obs['full_theta_sha256']),
        'only_changed_pool_refreshes_its_observables':bool(
            objective.factorized_statistics['coarse']['refreshes']==old_refresh+1
            and objective.fine_derivative_cache is fine),
        'new_fixture_has_no_accepted_surface_or_optimizer':not objective.accepted_iterates}
    return {'checks':{k:bool(v) for k,v in checks.items()},'all_passed':bool(all(checks.values())),
        'de_df_directional_finite_differences':fd,'scalar_chain_relative_error':_relative(chain,J),
        'new_observable_statistics':diag,
        'old_developer_suites_not_called':True,'actual_LP_calls':0,
        'new_artificial_ordinary_values_are_not_scientific_geometry':True}


def developer_check():
    require_public_research_environment()
    started=time.monotonic()
    first=array_checks()
    print('DEVELOPMENT_PART AFFINE_ARRAYS '+json.dumps(first,sort_keys=True,allow_nan=False),flush=True)
    second=observable_and_cache_checks()
    print('DEVELOPMENT_PART AFFINE_OBSERVABLES '+json.dumps(second,sort_keys=True,allow_nan=False),flush=True)
    return {'schema':SCHEMA,'artificial_inputs_only':True,
        'parts':{'arrays':first,'observables':second},
        'all_passed':bool(first['all_passed'] and second['all_passed']),
        'elapsed_seconds':time.monotonic()-started,
        'peak_rss_kib_linux':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'source_files_sha256':implementation_hashes(),
        'old_research_or_old_developer_suites_invoked':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    result=developer_check()
    text=json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2,allow_nan=False)+'\n'
    if args.out is not None:
        args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(text,encoding='utf-8')
    print('DEVELOPMENT_COMPLETE '+text,flush=True)
    if not result['all_passed']:raise SystemExit(1)


if __name__=='__main__':main()

