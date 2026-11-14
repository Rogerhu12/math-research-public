#!/usr/bin/env python3
"""One bounded direct-metric solve with independent radial center speed.

Research execution is restricted to this public repository's Actions. The
developer mode runs the same initial/gate/solve/freeze/final-audit orchestration
on a small artificial problem, including its report writer and distribution.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import resource
import tempfile
import time

import numpy as np
from scipy.optimize import least_squares

from frame_collar_bvp import (FrameCollarProblem,EllipticCylinderPort,NegativeKRadialSeed,
    atomic_save,smooth_positive)
from frame_collar_bent_tail import artificial_enriched_report,load_enriched_report
from frame_collar_enriched import make_enriched
from frame_collar_natural_body_audit import NaturalBodyProblem,implementation_hashes as natural_hashes
from frame_collar_residual_audit import digest
from frame_independent_height import IndependentHeightProblem


def implementation_hashes():
    hashes=natural_hashes()
    for name in ['frame_independent_height.py',Path(__file__).name]:
        hashes[name]=hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
    return hashes


def point_values(problem,data):
    X,U,Xt,T=(data[key] for key in ['X','Xs','Xt','T'])
    e=np.sum(U*U,axis=-1)-1;q=np.sum(U*T,axis=-1)
    E=e+1;F=np.sum(U*Xt,axis=-1);G=np.sum(Xt*Xt,axis=-1)
    normal=np.cross(U,Xt);area=np.linalg.norm(normal,axis=-1)
    unit=np.divide(normal,area[...,None],out=np.full_like(normal,np.nan),where=area[...,None]>0)
    second=[np.sum(unit*data[key],axis=-1) for key in ['Xss','Xst','Xtt']]
    with np.errstate(divide='ignore',invalid='ignore',over='ignore'):
        H=(G*second[0]-2*F*second[1]+E*second[2])/(2*area*area)
        K=(second[0]*second[2]-second[1]**2)/(area*area)
        discriminant=H*H-K
        curvature=np.maximum(abs(H+np.sqrt(np.maximum(discriminant,0))),abs(H-np.sqrt(np.maximum(discriminant,0))))
    return {'E_minus_one':e,'F_over_a':q,
        'metric_operator_error':.5*(abs(e)+np.sqrt(e*e+4*q*q)),
        'area':area,'principal_curvature_absolute':curvature,
        'curvature_discriminant':discriminant,
        'ball_radius_squared_normalized':np.sum(X*X,axis=-1)/problem.ball_radius**2,
        'strip_abs_normalized':abs(X[...,1])/problem.strip_half_width,
        'signed_side_height_minus_core_width':problem.port.side*X[...,2]-problem.port.width,
        'G_over_a_squared_minus_one':G/data['metric']['a'][:,None]**2-1}


def extremum(values,radial,theta,kind='max'):
    values=np.asarray(values,float);finite=np.isfinite(values)
    if not np.any(finite):return {'value':None,'finite_count':0,'nonfinite_count':int(values.size)}
    adjusted=abs(values) if kind=='abs' else values
    valid=np.where(finite,adjusted,np.inf if kind=='min' else -np.inf)
    index=np.unravel_index(np.argmin(valid) if kind=='min' else np.argmax(valid),valid.shape)
    return {'value':float(values[index]),'magnitude':float(adjusted[index]),
        't':float(radial[index[0]]),'theta':float(theta[index[1]]),
        'finite_count':int(finite.sum()),'nonfinite_count':int(values.size-finite.sum())}


def objective_cost(problem,data):
    values=point_values(problem,data);count=values['E_minus_one'].size
    metric=float(np.sum(values['E_minus_one']**2+2*values['F_over_a']**2)/(2*count))
    X=data['X'];shape=0.
    if problem.shape_weight>0:
        for constraint in [np.sum(X*X,axis=-1)/problem.ball_radius**2-1,
                           X[...,1]/problem.strip_half_width-1,-X[...,1]/problem.strip_half_width-1]:
            positive=smooth_positive(constraint)[0]
            shape+=float(problem.shape_weight**2*np.sum(positive**2)/(2*count))
    return {'metric_only':metric,'ball_strip_only':shape,'total':metric+shape}


def endpoint_comparison(problem,data):
    t,theta=data['radial'],data['theta'];mapping={'X':'X','Xs':'Xs','Xt':'Xtheta','Xss':'Xss','Xst':'Xst','Xtt':'Xtt'}
    core=problem.port.position_jets(t[0],theta)
    core_error={key:float(np.max(np.linalg.norm(data[key][0]-core[target],axis=-1))) for key,target in mapping.items()}
    after=t>=problem.source.active_end
    if not np.any(after):raise ValueError('a complete audit must include the physical open tail')
    if t[-1]!=problem.seed.length:raise ValueError('one cap height must be anchored at the actual inner tail endpoint')
    height=problem.port.side*float(data['center'][-1])
    radius=problem.seed.cut_radius+problem.seed.length-t[after]
    target=problem.tail.position_jets(radius[:,None],theta[None,:],height,48)
    tail_error={key:float(np.max(np.linalg.norm(data[key][after]-target[name],axis=-1))) for key,name in mapping.items()}
    held_radius=problem.seed.cut_radius
    return {'core_position_two_jet_errors':core_error,
        'open_tail_position_two_jet_errors_from_one_exact_cap':tail_error,
        'single_cap_height':height,'held_disk_radius':held_radius,
        'height_not_refitted_by_radial_row':True,
        'exact_cap_geometric_budget':problem.tail.analytic_budget(),
        'global_reference_center_quadrature_error_not_bounded_by_this_comparison':True,
        'finite_Pi_and_quadrature_differences_are_not_continuous_bounds':True}


def sampled_audit(problem,state,data):
    values=point_values(problem,data);t,theta=data['radial'],data['theta'];X=data['X']
    maxima={key:extremum(value,t,theta,'min' if key in ['area','signed_side_height_minus_core_width','curvature_discriminant']
                         else 'abs' if key in ['E_minus_one','F_over_a','G_over_a_squared_minus_one'] else 'max')
            for key,value in values.items()}
    return {'schema':'independent-height-actual-position-audit-v1','radial_nodes':len(t),'angular_nodes':len(theta),
        'extrema':maxima,'objective_cost':objective_cost(problem,data),
        'coordinate_min_sample':X.min(axis=(0,1)).tolist(),'coordinate_max_sample':X.max(axis=(0,1)).tolist(),
        'center_height_first_last':[float(data['center'][0]),float(data['center'][-1])],
        'center_speed_min_max_sample':[float(np.min(data['height']['b'])),float(np.max(data['height']['b']))],
        'target_K_min_max_sample':[float(np.min(data['metric']['K'])),float(np.max(data['metric']['K']))],
        'radius_min_max_sample':[float(np.min(data['metric']['a'])),float(np.max(data['metric']['a']))],
        'position_ports':endpoint_comparison(problem,data),
        'metric_identity_sha256':problem.metric_model(state)['mathematical_definition_sha256'],
        'auxiliary_R_not_evaluated_or_used_as_a_goal':True,'sampled_only':True,
        'embedding_proved':False,'whole_surface_reach_proved':False,'task_complete':False}


def radial_distribution(problem,data):
    """Own explicit data API; do not reuse the old R-distribution signature."""
    values=point_values(problem,data);t,theta=data['radial'],data['theta'];rows=[]
    for i,time_value in enumerate(t):
        row={'t':float(time_value)}
        for key in ['E_minus_one','F_over_a','metric_operator_error','principal_curvature_absolute','area']:
            kind='min' if key=='area' else 'abs' if key in ['E_minus_one','F_over_a'] else 'max'
            row[key]=extremum(values[key][i:i+1],t[i:i+1],theta,kind)
        row['angular_means']={key:float(np.mean(values[key][i])) for key in ['E_minus_one','F_over_a']}
        rows.append(row)
    return {'radial_rows':rows,'radial_nodes':len(t),'angular_nodes':len(theta),
        'all_values_sampled_only':True,'no_auxiliary_R_fields':True}


def compare_evaluation(problem,state,variant,radial,theta,order=4,variant_order=None):
    if problem.identity(state)!=variant.identity(state):raise ArithmeticError('refinement changes physical identity')
    other_order=order if variant_order is None else variant_order
    d0=problem.geometry(state,radial,theta,order);d1=variant.geometry(state,radial,theta,other_order)
    p0,p1=point_values(problem,d0),point_values(variant,d1)
    positions={key:float(np.max(np.linalg.norm(d0[key]-d1[key],axis=-1))) for key in ['X','Xs','Xt','Xss','Xst','Xtt']}
    metric={'E_minus_one':float(np.max(abs(p0['E_minus_one']-p1['E_minus_one']))),
        'sqrt2_F_over_a':float(np.sqrt(2)*np.max(abs(p0['F_over_a']-p1['F_over_a']))),
        'operator_error':float(np.max(abs(p0['metric_operator_error']-p1['metric_operator_error'])))}
    first=max(positions[key] for key in ['X','Xs','Xt'])
    first=max(first,metric['E_minus_one'],metric['sqrt2_F_over_a'])
    return {'same_canonical_identity_and_coefficients':True,'physical_identity_sha256':digest(problem.identity(state)),
        'evaluation_before':problem.evaluation_definition(),'evaluation_after':variant.evaluation_definition(),
        'radial_quadrature_orders':[int(order),int(other_order)],'radial_nodes':len(radial),'angular_nodes':len(theta),
        'position_jet_differences':positions,'direct_metric_differences':metric,
        'first_position_and_direct_metric_gate_max':first,
        'center_speed_differences':{key:float(np.max(abs(d0['height'][key]-d1['height'][key]))) for key in ['b','b_s','b_ss']},
        'fixed_state_objective_costs':[objective_cost(problem,d0),objective_cost(variant,d1)],
        'no_reoptimization_or_step_applied':True,'differences_not_continuous_error_bounds':True}


def state_record(problem,state):
    physical=problem.identity(state)
    return {'canonical_physical_state':physical,'canonical_physical_state_sha256':digest(physical),
        'exact_parameter_coefficients':{name:[str(Q.from_float(float(x))) for x in state[problem.slices[name]]]
                                        for name in ['u','v','height','metric']},
        'parameter_coefficients_binary64':np.asarray(state,float).tolist(),
        'parameter_slices':{name:[value.start,value.stop] for name,value in problem.slices.items()},
        'metric_model':problem.metric_model(state),'evaluation_definition':problem.evaluation_definition()}


class WallBudgetReached(RuntimeError):
    pass


class Evaluator:
    def __init__(self,problem,radial,theta,order,initial,initial_cost,max_seconds,checkpoint,
                 every=10,seconds=60):
        self.problem=problem;self.radial=radial;self.theta=theta;self.order=order
        self.best_state=initial.copy();self.best_cost=float(initial_cost)
        self.max_seconds=float(max_seconds);self.checkpoint=checkpoint
        self.every=int(every);self.seconds=float(seconds);self.started=time.monotonic();self.last_write=self.started
        self.cache=None;self.evaluations=0;self.history=[]

    def evaluate(self,state):
        if self.cache is not None and np.array_equal(state,self.cache[0]):return self.cache[1:]
        if time.monotonic()-self.started>=self.max_seconds:raise WallBudgetReached('declared solve wall budget reached')
        residual,J,data=self.problem.direct_residual_and_jacobian(state,self.radial,self.theta,self.order)
        self.evaluations+=1;cost=float(residual@residual/2)
        if np.isfinite(cost) and cost<self.best_cost:self.best_cost=cost;self.best_state=np.asarray(state).copy()
        self.cache=(np.asarray(state).copy(),residual,J,data)
        now=time.monotonic()
        if self.evaluations%self.every==0 or now-self.last_write>=self.seconds:
            self.history.append({'evaluation':self.evaluations,'trial_cost':cost,'best_cost':self.best_cost,
                'elapsed_solve_seconds':now-self.started})
            self.checkpoint(self.best_state,'bounded-solve-checkpoint',self);self.last_write=now
        if now-self.started>=self.max_seconds:raise WallBudgetReached('declared solve wall budget reached after evaluation')
        return residual,J,data

    def residual(self,state):return self.evaluate(state)[0]
    def jacobian(self,state):return self.evaluate(state)[1]


def run_problem(problem,initial,configuration,out,*,source_record,artificial=False):
    """The single common orchestration path for Actions and artificial checks."""
    started=time.monotonic();initial=np.asarray(initial,float);cfg=configuration
    radial=problem.source.radial;theta=problem.source.theta;order=int(cfg['quadrature_order'])
    bounds=np.empty(problem.nunknown)
    for name,value in [('u',cfg['uv_bound']),('v',cfg['uv_bound']),('height',cfg['height_bound']),('metric',cfg['body_bound'])]:
        bounds[problem.slices[name]]=float(value)
    if not np.all(np.isfinite(initial)) or np.any(abs(initial)>=bounds):
        raise ValueError('the exact initial coefficients must lie strictly inside all declared bounds; no clipping')
    report={'schema':'independent-height-bounded-direct-metric-solve-v1',
        'configuration':cfg,'source_record':source_record,'source_files_sha256':implementation_hashes(),
        'initial_uv_from_original_c0':True,'initial_height_and_body_controls_zero':bool(np.all(initial[problem.slices['height']]==0) and np.all(initial[problem.slices['metric']]==0)),
        'initial_exact_state':state_record(problem,initial),'active_shape_budget':{
            'ball_radius':str(problem.source.ball_exact),'strip_half_width':str(problem.source.strip_exact),
            'shape_weight':problem.shape_weight,'no_signed_height_penalty_added':True},
        'bounds_by_block':{name:float(bounds[value.start]) for name,value in problem.slices.items() if value.stop>value.start},
        'sampling_definition':problem.source.sampling_definition,'artificial_developer_path':bool(artificial),
        'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'github_repository':os.environ.get('GITHUB_REPOSITORY'),
        'only_one_bounded_nonlinear_solve_is_permitted':True,'closed_surface_constructed':False,
        'embedding_proved':False,'whole_surface_reach_proved':False,'task_complete':False}
    def save(state,status,evaluator=None):
        report['status']=status;report['selected_state']=state_record(problem,state)
        report['selected_bound_usage']={name:{'maximum_absolute_coefficient':float(np.max(abs(state[block]))),
            'minimum_distance_to_bound':float(np.min(bounds[block]-abs(state[block]))),
            'coefficients_within_1e_minus5_of_bound':int(np.count_nonzero(bounds[block]-abs(state[block])<=1e-5))}
            for name,block in problem.slices.items() if block.stop>block.start}
        if evaluator is not None:
            report['history']=evaluator.history;report['unique_evaluations_seen']=evaluator.evaluations
            report['selected_collocation_cost']=evaluator.best_cost
        report['elapsed_seconds']=time.monotonic()-started
        report['peak_rss_kib_linux']=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        atomic_save(out,report)
    initial_data=problem.geometry(initial,radial,theta,order)
    report['initial_audit']=sampled_audit(problem,initial,initial_data)
    report['initial_cost']=objective_cost(problem,initial_data)['total']
    save(initial,'initial-state-saved')
    gh_variant=problem.evaluation_variant(initial,heat_order=2*problem.source.heat_order)
    nb_variant=problem.evaluation_variant(initial,height_angular_nodes=2*problem.height_angular_nodes)
    report['initial_GH_comparison']=compare_evaluation(problem,initial,gh_variant,radial,theta,order)
    save(initial,'initial-GH-comparison-saved')
    report['initial_height_mean_comparison']=compare_evaluation(problem,initial,nb_variant,radial,theta,order)
    tolerance=float(cfg['evaluation_tolerance'])
    gates={'tolerance':tolerance,'definition':'max of X/Xs/Xtheta and (E-1,sqrt2 F/a) differences; no second-jet certification',
        'GH_passed':bool(report['initial_GH_comparison']['first_position_and_direct_metric_gate_max']<=tolerance),
        'height_mean_passed':bool(report['initial_height_mean_comparison']['first_position_and_direct_metric_gate_max']<=tolerance),
        'initial_cost_limit':float(cfg['initial_cost_max']),
        'initial_cost_passed':bool(np.isfinite(report['initial_cost']) and report['initial_cost']<=cfg['initial_cost_max']),
        'engineering_gates_not_mathematical_feasibility_certificates':True}
    report['initial_engineering_gates']=gates;save(initial,'initial-engineering-gates-saved')
    selected=initial.copy();solver=None
    if gates['GH_passed'] and gates['height_mean_passed'] and gates['initial_cost_passed']:
        evaluator=Evaluator(problem,radial,theta,order,initial,report['initial_cost'],cfg['max_seconds'],save,
                            cfg['checkpoint_every'],cfg['checkpoint_seconds'])
        solver={'attempted':True,'method':'bounded scipy least_squares TRF with analytic Jacobian',
                'max_nfev':int(cfg['max_nfev']),'wall_budget_seconds':float(cfg['max_seconds']),
                'no_unconstrained_linear_prediction_step_used':True}
        try:
            result=least_squares(evaluator.residual,initial,jac=evaluator.jacobian,
                bounds=(-bounds,bounds),method='trf',max_nfev=int(cfg['max_nfev']),
                ftol=1e-10,xtol=1e-10,gtol=1e-8)
            solver.update(success=bool(result.success),status=int(result.status),message=str(result.message),
                nfev=int(result.nfev),optimality=float(result.optimality),wall_budget_reached=False)
        except WallBudgetReached as error:
            solver.update(success=False,status='wall-budget',message=str(error),wall_budget_reached=True)
        selected=evaluator.best_state.copy();report['solver']=solver
        report['solve_elapsed_seconds']=time.monotonic()-evaluator.started
        save(selected,'bounded-solve-finished',evaluator)
        evaluator.cache=None
    else:
        solver={'attempted':False,'reason':'initial engineering gate failed; diagnostics only'}
        report['solver']=solver;save(selected,'initial-gate-failed-no-solve')
    # Freeze the actual selected g without interpreting its coefficients in a
    # new basis. All remaining work is fixed-state evaluation, never another solve.
    frozen,fc=problem.frozen_metric_copy(selected)
    if problem.identity(selected)!=frozen.identity(fc):raise ArithmeticError('freezing g changed full physical identity')
    before=problem.geometry(selected,radial,theta,order);after=frozen.geometry(fc,radial,theta,order)
    report['final_metric_freeze']={'same_complete_physical_identity':True,
        'metric_model':frozen.metric_model(fc),
        'same_grid_position_two_jet_replay_errors':{key:float(np.max(abs(before[key]-after[key]))) for key in ['X','Xs','Xt','Xss','Xst','Xtt']},
        'all_later_evaluations_hold_this_metric_and_all_other_coefficients_fixed':True}
    report['final_collocation_audit']=sampled_audit(frozen,fc,after)
    save(selected,'metric-frozen-and-replayed')
    fine_radial=np.linspace(0,problem.seed.length,int(cfg['audit_radial_nodes']))
    fine_theta=np.arange(int(cfg['audit_angular_nodes']))*2*np.pi/int(cfg['audit_angular_nodes'])
    fine_order=int(cfg['audit_quadrature_order'])
    fine=frozen.geometry(fc,fine_radial,fine_theta,fine_order)
    report['fixed_state_fine_audit']=sampled_audit(frozen,fc,fine)
    report['fixed_state_radial_distribution']=radial_distribution(frozen,fine)
    save(selected,'fine-audit-and-distribution-saved')
    twice=frozen.geometry(fc,fine_radial,np.arange(2*len(fine_theta))*np.pi/len(fine_theta),fine_order)
    report['fixed_state_double_angle_audit']=sampled_audit(frozen,fc,twice)
    report['Pi_same_point_refinement']={'only_query_angle_count_changed':True,
        'height_mean_rule_fixed':True,'GH_rule_fixed':True,
        'position_jet_differences':{key:float(np.max(np.linalg.norm(fine[key]-twice[key][:,::2],axis=-1)))
                                    for key in ['X','Xs','Xt','Xss','Xst','Xtt']},
        'not_a_continuous_error_bound':True}
    # Include both exact interface radii in a separate globally anchored chart.
    ports=np.array([0.,problem.source.active_start,problem.source.active_end,problem.seed.length])
    port_data=frozen.geometry(fc,ports,np.arange(2*len(fine_theta))*np.pi/len(fine_theta),fine_order)
    report['exact_interface_grid_audit']=sampled_audit(frozen,fc,port_data)
    save(selected,'angle-and-interface-audits-saved')
    final_gh,gh_state=gh_variant.frozen_metric_copy(selected)
    if not np.array_equal(gh_state,fc):raise ArithmeticError('GH frozen replay changed coefficients')
    report['fixed_state_GH_comparison']=compare_evaluation(frozen,fc,final_gh,fine_radial,fine_theta,fine_order)
    save(selected,'final-GH-comparison-saved')
    final_nb,nb_state=nb_variant.frozen_metric_copy(selected)
    if not np.array_equal(nb_state,fc):raise ArithmeticError('height-mean frozen replay changed coefficients')
    report['fixed_state_height_mean_comparison']=compare_evaluation(frozen,fc,final_nb,fine_radial,fine_theta,fine_order)
    report['fixed_state_radial_quadrature_comparison']=compare_evaluation(frozen,fc,frozen,fine_radial,fine_theta,fine_order,
                                                                         int(cfg['refined_quadrature_order']))
    report['no_final_refinement_reoptimized_any_parameter']=True
    report['nonlinear_solve_count']=1 if solver['attempted'] else 0
    save(selected,'complete-fixed-state-audit')
    return report


def default_configuration():
    return {'uv_bound':8.,'height_bound':1.,'body_bound':.5,'max_nfev':250,'max_seconds':600.,
        'checkpoint_every':10,'checkpoint_seconds':60.,'evaluation_tolerance':1e-4,'initial_cost_max':1.,
        'quadrature_order':4,'audit_quadrature_order':8,'refined_quadrature_order':12,
        'audit_radial_nodes':121,'audit_angular_nodes':384}


def artificial_problem():
    port=EllipticCylinderPort('9/10','18/25','1/50',1)
    seed=NegativeKRadialSeed.from_core(port,'11/10','11/50')
    baseline=FrameCollarProblem(port,seed,radial_free=2,angular_modes=2,
        ellipse_envelope=(port.major,port.minor),height_limit=.1,radial_nodes=9,angular_nodes=24,radial_quadrature_order=3)
    old=make_enriched(baseline,2,1,9,24,3,strip_half_width='2/5');c0=.009*np.sin(np.arange(old.nunknown)+.2)
    carrier=artificial_enriched_report(old,c0,baseline,.006*np.cos(np.arange(baseline.nunknown)))
    old,c0,replay=load_enriched_report(carrier)
    source=NaturalBodyProblem(old,c0,metric_free=3,ball_radius='91/100',strip_half_width='1/3',
        amplitudes=['1/7','1/9','1/9','1/7','1/9','1/9'],radial_nodes=9,angular_nodes=24,quadrature_order=3,heat_order=8)
    return IndependentHeightProblem(source,3,height_angular_nodes=24),replay


def developer_check():
    problem,replay=artificial_problem();cfg=default_configuration()
    cfg.update(max_nfev=2,max_seconds=90.,checkpoint_every=1,checkpoint_seconds=60.,
        evaluation_tolerance=1e6,initial_cost_max=1e6,quadrature_order=3,
        audit_quadrature_order=4,refined_quadrature_order=6,audit_radial_nodes=11,audit_angular_nodes=24)
    with tempfile.TemporaryDirectory(prefix='independent-height-artificial-') as folder:
        path=Path(folder)/'complete.json'
        report=run_problem(problem,problem.initial_state(),cfg,path,source_record={'artificial':True,'replay':replay},artificial=True)
        roundtrip=json.loads(path.read_text())
        zero_gate=dict(cfg,evaluation_tolerance=0.,initial_cost_max=-1.)
        rejected=run_problem(problem,problem.initial_state(),zero_gate,Path(folder)/'rejected.json',
                             source_record={'artificial':True},artificial=True)
        expired=run_problem(problem,problem.initial_state(),dict(cfg,max_seconds=0.),Path(folder)/'budget.json',
                            source_record={'artificial':True},artificial=True)
    fields=['initial_audit','initial_GH_comparison','initial_height_mean_comparison','final_metric_freeze',
        'fixed_state_fine_audit','fixed_state_radial_distribution','fixed_state_double_angle_audit',
        'Pi_same_point_refinement','exact_interface_grid_audit','fixed_state_GH_comparison',
        'fixed_state_height_mean_comparison','fixed_state_radial_quadrature_comparison']
    freeze=report['final_metric_freeze'];errors=freeze['same_grid_position_two_jet_replay_errors']
    hashes=report['selected_state'];canonical_ok=digest(hashes['canonical_physical_state'])==hashes['canonical_physical_state_sha256']
    passed=(report['status']=='complete-fixed-state-audit' and all(key in report for key in fields)
        and report['nonlinear_solve_count']==1 and report['solver']['attempted']
        and rejected['nonlinear_solve_count']==0 and not rejected['solver']['attempted']
        and expired['solver']['wall_budget_reached'] and expired['unique_evaluations_seen']==0
        and expired['status']=='complete-fixed-state-audit'
        and freeze['same_complete_physical_identity'] and max(errors.values())==0.
        and canonical_ok and roundtrip==report
        and len(report['fixed_state_radial_distribution']['radial_rows'])==cfg['audit_radial_nodes'])
    return {'schema':'independent-height-full-driver-development-v1','passed':bool(passed),
        'artificial_inputs_only':True,'research_geometry_evaluated':False,
        'artificial_small_bounded_solve_max_nfev':2,
        'artificial_engineering_thresholds_relaxed_only_to_exercise_the_solve_branch':True,
        'both_passed_gate_and_rejected_gate_paths_exercised':True,
        'wall_budget_exception_preserves_state_and_completes_audits':expired['solver']['wall_budget_reached'],
        'same_run_problem_function_as_actual_main':True,'complete_reports_JSON_roundtrip':roundtrip==report,
        'full_final_distribution_and_all_refinement_call_signatures_exercised':all(key in report for key in fields),
        'canonical_selected_state_hash_checked':canonical_ok,'same_g_freeze_replay_errors':errors,
        'artificial_solver':report['solver'],'rejected_gate_solver':rejected['solver'],
        'separate_GH_Nb_radial_comparisons_not_continuous_bounds':True,
        'passed_does_not_mean_research_initial_gates_or_feasibility_pass':True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only',action='store_true');parser.add_argument('--input',type=Path)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--height-free',type=int,default=9);parser.add_argument('--metric-free',type=int,default=5)
    parser.add_argument('--heat-order',type=int,default=64);parser.add_argument('--height-angular-nodes',type=int,default=384)
    parser.add_argument('--radial-nodes',type=int,default=61);parser.add_argument('--angular-nodes',type=int,default=192)
    for key,value in default_configuration().items():
        parser.add_argument('--'+key.replace('_','-'),type=int if isinstance(value,int) else float,default=value)
    args=parser.parse_args()
    if args.check_only:
        report=developer_check();report['source_files_sha256']=implementation_hashes();atomic_save(args.out,report)
        print(json.dumps({'out':str(args.out),'passed':report['passed']}),flush=True)
        if not report['passed']:raise SystemExit(1)
        return
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        parser.error('research evaluation and this single bounded solve require the public repository Actions')
    if not args.input:parser.error('--input must be the original enriched c0 report')
    notes=Path(__file__).resolve().parents[1]/'notes'
    if not args.input.resolve().is_relative_to(notes.resolve()):parser.error('only public topic notes may supply the input')
    if (args.radial_nodes<3 or args.angular_nodes<4 or args.angular_nodes%4 or args.audit_angular_nodes<4
        or args.audit_angular_nodes%4 or args.height_free<1 or args.metric_free<1
        or args.heat_order<4 or args.heat_order>128 or args.height_angular_nodes<4 or args.height_angular_nodes%4
        or args.audit_radial_nodes<args.radial_nodes or args.audit_angular_nodes<args.angular_nodes):
        parser.error('invalid positive basis/evaluation dimensions')
    configuration={key:getattr(args,key) for key in default_configuration()}
    if min(configuration.values())<=0:parser.error('all solve, checkpoint, gate and quadrature budgets must be positive')
    raw=args.input.read_bytes();old,c0,replay=load_enriched_report(json.loads(raw))
    source=NaturalBodyProblem(old,c0,metric_free=args.metric_free,support_width='1/10',plateau_fraction='1/3',tau0='1/128',
        heat_order=args.heat_order,radial_nodes=args.radial_nodes,angular_nodes=args.angular_nodes,
        quadrature_order=args.quadrature_order)
    problem=IndependentHeightProblem(source,args.height_free,height_angular_nodes=args.height_angular_nodes)
    source_record={'path':str(args.input),'sha256':hashlib.sha256(raw).hexdigest(),'identity':replay,
        'exact_original_c0':[str(Q.from_float(float(x))) for x in c0],
        'original_input_only_not_saturated_c1':True}
    configuration.update(height_free=args.height_free,metric_free=args.metric_free,heat_order=args.heat_order,
        height_angular_nodes=args.height_angular_nodes,radial_nodes=args.radial_nodes,angular_nodes=args.angular_nodes)
    report=run_problem(problem,problem.initial_state(),configuration,args.out,source_record=source_record)
    print(json.dumps({'out':str(args.out),'status':report['status'],'nonlinear_solve_count':report['nonlinear_solve_count'],
        'final_cost':report['final_collocation_audit']['objective_cost']['total'],'task_complete':False}),flush=True)


if __name__=='__main__':main()
