#!/usr/bin/env python3
"""Warm projected endpoint design, normalized feasibility, then epigraph polish.

This is a new geometry design, not refinement of the warm input. Only its
H1,H4,... values seed the already defined exact tip/valley q_ell=0 subspace.
A fixed curvature target is used in the first bounded least-squares stage:
lambda0/K + w*abs(q_ell) <= 1. Every physical constraint is dimensionless and
has a chained analytic Jacobian. SLSQP is attempted only from a sufficiently
feasible point. One case is run, and research solves require public Actions.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as R
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np
from scipy.optimize import least_squares,minimize

from folded_reference_geometry import I
from star_core_geometry import square
from space_star_lift_design import load_planar,rational_interval
from space_star_cosine_design import CosineLiftProblem,rational_json
from space_star_cosine_endpoint_design import EndpointElimination,EndpointProblem,tip_limit
from cosine_rectifying_core import canonical_identity,exact_rational,identity_hash


def positive_part(value,smoothing):
    """Stable C-infinity approximation to max(value,0), with its derivative."""
    value=np.asarray(value,float)
    radius=np.hypot(value,smoothing)
    result=np.empty_like(value)
    positive=value>=0
    result[positive]=.5*(value[positive]+radius[positive])
    result[~positive]=.5*smoothing*smoothing/(radius[~positive]-value[~positive])
    derivative=.5*(1+value/radius)
    return result,derivative


class NormalizedEndpoint:
    def __init__(self,problem,target_curvature,smoothing=1e-6):
        self.problem=problem
        self.target=float(target_curvature);self.smoothing=float(smoothing)
        if self.target<=0 or self.smoothing<=0:
            raise ValueError('positive curvature target and positive hinge smoothing required')
        base=problem.base;n=len(base.phi);m=problem.modes
        if base.kappa_floor<=0 or base.height_budget<=0 or problem.tip_z2_limit<=0:
            raise ValueError('all physical normalization scales must be positive')
        self.scales=np.r_[np.full(n,self.target),np.ones(n),np.full(n,base.kappa_floor),
                          np.full(2*n,base.height_budget),problem.height_bounds,
                          problem.height_bounds,np.full(2,problem.tip_z2_limit)]
        # Each of the five full-angle blocks and the coefficient/tip blocks has
        # order-one aggregate weight. Feasibility is still selected by MAX
        # unweighted dimensionless violation, never by RMS alone.
        self.weights=np.r_[np.full(5*n,1/np.sqrt(n)),
                           np.full(2*m,1/np.sqrt(2*m)),np.full(2,1/np.sqrt(2))]
        self.nangles=n

    def constraints(self,state):
        return self.problem.constraints(state)/self.scales

    def jacobian(self,state):
        return self.problem.constraint_jacobian(state)/self.scales[:,None]

    def feasibility_residual(self,free):
        violation=-self.constraints(np.r_[free,self.target])
        residual,_=positive_part(violation,self.smoothing)
        return self.weights*residual

    def feasibility_jacobian(self,free):
        state=np.r_[free,self.target]
        violation=-self.constraints(state)
        _,derivative=positive_part(violation,self.smoothing)
        return -(self.weights*derivative)[:,None]*self.jacobian(state)[:,:-1]

    def violations(self,state):
        constraints=self.constraints(state)
        values=np.maximum(-constraints,0)
        return {'maximum':float(np.max(values)),
                'weighted_rms':float(np.linalg.norm(self.weights*values)),
                'minimum_normalized_constraint':float(np.min(constraints)),
                'per_block_maximum':{
                    'curvature_budget':float(np.max(values[:self.nangles])),
                    'J_floor':float(np.max(values[self.nangles:2*self.nangles])),
                    'kappa_floor':float(np.max(values[2*self.nangles:3*self.nangles])),
                    'height':float(np.max(values[3*self.nangles:5*self.nangles])),
                    'physical_coefficient_bounds':float(np.max(values[5*self.nangles:-2])),
                    'tip_turn_budget':float(np.max(values[-2:]))}}


def project_warm_identity(identity,elimination,width,fixed_offset=None):
    canonical=canonical_identity(identity)
    if (R(canonical['a'])!=elimination.a or R(canonical['b'])!=elimination.b or
        R(canonical['half_width'])!=R(width) or len(canonical['height_coefficients'])!=elimination.modes):
        raise ValueError('warm identity must have the same a,b,width and number of cosine modes')
    original=[exact_rational(x) for x in canonical['height_coefficients']]
    free=[float(original[j]) for j in elimination.free_indices]
    if fixed_offset is None:free.append(float(exact_rational(canonical['height_offset'])))
    return np.array(free),canonical


def read_warm(path,elimination,width,fixed_offset=None):
    raw=path.read_bytes();report=json.loads(raw)
    identity=report['frozen_physical_identity']
    digest=identity_hash(identity)
    if report.get('frozen_physical_identity_sha256')!=digest:
        raise ValueError('warm report physical identity hash mismatch')
    free,canonical=project_warm_identity(identity,elimination,width,fixed_offset)
    return free,{'path':str(path),'sha256':hashlib.sha256(raw).hexdigest(),
        'physical_identity_sha256':digest,'original_frozen_physical_identity':canonical,
        'preserved_height_harmonics':[j+1 for j in elimination.free_indices],
        'recomputed_height_harmonics':[2,3],
        'original_certificate_is_not_inherited':True,
        'projection_is_new_geometry_design_not_fixed_parameter_refinement':True}


def developer_check():
    elimination=EndpointElimination('.07','.005',6)
    checks=[]
    for fixed in [None,.013]:
        problem=EndpointProblem(elimination,np.arange(32)*2*np.pi/32,.02,.4,1.2,.1,.03,fixed)
        normalized=NormalizedEndpoint(problem,.7,1e-5)
        free=np.array([.04,.00008,-.00001,.000001]+([] if fixed is not None else [.013]))
        direction=np.random.default_rng(7713).normal(size=len(free));direction/=np.linalg.norm(direction)
        epsilon=1e-7
        fd=(normalized.feasibility_residual(free+epsilon*direction)-
            normalized.feasibility_residual(free-epsilon*direction))/(2*epsilon)
        analytic=normalized.feasibility_jacobian(free)@direction
        relative=float(np.linalg.norm(fd-analytic)/max(1e-30,np.linalg.norm(fd)))
        state=np.r_[free,1.3]
        direction2=np.random.default_rng(7714).normal(size=len(state));direction2/=np.linalg.norm(direction2)
        fd2=(normalized.constraints(state+epsilon*direction2)-
             normalized.constraints(state-epsilon*direction2))/(2*epsilon)
        analytic2=normalized.jacobian(state)@direction2
        relative2=float(np.linalg.norm(fd2-analytic2)/max(1e-30,np.linalg.norm(fd2)))
        data=problem.base.evaluate(problem.physical(free))
        budget=1-data['lambda0'].v/normalized.target-problem.base.width*abs(data['qell'].v)
        equivalence=float(np.max(abs(budget-normalized.constraints(np.r_[free,normalized.target])[:32])))
        identity,_,_,_=problem.freeze(free,'.02')
        projected,canonical=project_warm_identity(identity,elimination,'.02',fixed)
        wrong=dict(canonical);wrong['half_width']='1/100'
        mismatch=False
        try:project_warm_identity(wrong,elimination,'.02',fixed)
        except ValueError:mismatch=True
        checks.append({'fixed_offset':fixed,'feasibility_jacobian_relative_error':relative,
            'normalized_epigraph_jacobian_relative_error':relative2,
            'fixed_budget_algebra_numeric_difference':equivalence,
            'warm_free_values_preserved_exactly':bool(np.array_equal(projected,free)),
            'wrong_warm_width_rejected':mismatch})
    values=np.array([-1e4,-1.,0.,1.,1e4]);smoothed,derivative=positive_part(values,1e-6)
    passed=all(c['feasibility_jacobian_relative_error']<3e-5 and
               c['normalized_epigraph_jacobian_relative_error']<3e-5 and
               c['fixed_budget_algebra_numeric_difference']<1e-12 and
               c['warm_free_values_preserved_exactly'] and c['wrong_warm_width_rejected'] for c in checks)
    passed=passed and bool(np.all(np.isfinite(smoothed)) and np.all(smoothed>0) and
                            np.all((derivative>=0)&(derivative<=1)))
    return {'schema':'cosine-endpoint-feasibility-development-v1','development_check_only':True,
        'research_geometry_evaluated':False,'optimization_performed':False,'checks':checks,
        'stable_positive_part_values':smoothed.tolist(),'passed':bool(passed)}


def save(path,result):
    path.parent.mkdir(parents=True,exist_ok=True);temporary=path.with_suffix('.tmp')
    temporary.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');temporary.replace(path)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--a',default='.65');p.add_argument('--b',default='.12')
    p.add_argument('--height-modes',type=int,default=6);p.add_argument('--half-width',default='.02')
    p.add_argument('--warm-input',type=Path);p.add_argument('--offset-policy',choices=['auto','source'],default='auto')
    p.add_argument('--fixed-offset',type=float)
    p.add_argument('--angles',type=int,default=768);p.add_argument('--dense-angles',type=int,default=6144)
    p.add_argument('--target-curvature',default='planned')
    p.add_argument('--feasibility-max-nfev',type=int,default=500)
    p.add_argument('--feasibility-smoothing',type=float,default=1e-6)
    p.add_argument('--epigraph-start-max-violation',type=float,default=1e-4)
    p.add_argument('--epigraph-max-iterations',type=int,default=300)
    p.add_argument('--first-coefficient-bound',type=float,default=.6)
    p.add_argument('--higher-coefficient-bound',type=float,default=.12)
    p.add_argument('--derived-coefficient-bound',type=float,default=.5)
    p.add_argument('--j-floor',type=float,default=.3);p.add_argument('--kappa-floor',type=float,default=.1)
    p.add_argument('--height-reserve',default='.02')
    p.add_argument('--tip-budget',choices=['planned','necessary'],default='planned')
    p.add_argument('--checkpoint-every',type=int,default=10);p.add_argument('--checkpoint-seconds',type=float,default=60.)
    p.add_argument('--planar-report',type=Path);p.add_argument('--check-only',action='store_true')
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();started=time.monotonic()
    names=['space_star_cosine_endpoint_feasible.py','space_star_cosine_endpoint_design.py',
           'space_star_cosine_design.py','space_star_lift_design.py','cosine_rectifying_core.py',
           'space_star_flat_core.py','star_core_geometry.py','folded_reference_geometry.py']
    hashes={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in names}
    if args.check_only:
        result=developer_check();result['source_files_sha256']=hashes
        save(args.out,result);print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
        if not result['passed']:raise SystemExit(1)
        return
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        p.error('actual warm projection and optimization run only in this public repository Actions')
    if args.planar_report is None or args.warm_input is None or args.height_modes<3 or args.angles<24*args.height_modes:
        p.error('need public planar and warm reports, three or more modes, and sufficient angular nodes')
    if (R(args.half_width)<=0 or R(args.height_reserve)<0 or not 0<args.j_floor<1 or
        args.kappa_floor<=0 or args.checkpoint_every<1 or args.feasibility_smoothing<=0 or
        min(args.first_coefficient_bound,args.higher_coefficient_bound,args.derived_coefficient_bound)<=0 or
        args.dense_angles<args.angles or args.epigraph_start_max_violation<0 or
        args.feasibility_max_nfev<1 or args.epigraph_max_iterations<1):
        p.error('invalid positive geometric or solver configuration')
    repo=Path(__file__).resolve().parents[3];allowed=[repo/'topics'/'visible-flex-new-mechanism'/'notes']
    if os.environ.get('RUNNER_TEMP'):allowed.append(Path(os.environ['RUNNER_TEMP']))
    if not any(args.warm_input.resolve().is_relative_to(root.resolve()) for root in allowed):
        p.error('warm input must be a public topic note or current Actions temporary output')
    planar=load_planar(args.planar_report,args.a,args.b)
    width=I(args.half_width);distance=I(planar['continuous_distance_q_to_filled_star_domain']['lower'])
    dxy=I(planar['continuous_full_curve_diameter']['upper']);dxy_lower=I(planar['continuous_full_curve_diameter']['lower'])
    diameter_budget=(distance-width)/I('.3')
    available=square(I(diameter_budget.lo))-square(dxy+2*width)
    if available.lo<=0:p.error('planar padding exhausts the displacement budget')
    unreserved=(I(available.lo).sqrt()/2-width).lo
    height_budget=(I(unreserved)-I(args.height_reserve)).lo
    if height_budget<=0:p.error('height reserve exceeds available height')
    elimination=EndpointElimination(args.a,args.b,args.height_modes)
    radial=rational_interval(-1-10*elimination.a-37*elimination.b)
    tau_necessary=I('.03')*dxy_lower;tau_planned=I('.03')*I(diameter_budget.hi)
    necessary=tip_limit(radial,width,tau_necessary);planned=tip_limit(radial,width,tau_planned)
    tip_bound=planned if args.tip_budget=='planned' else necessary
    tip_design=float(np.nextafter(float(tip_bound.lo),-np.inf))
    target_enclosure=I(1)/tau_planned if args.target_curvature=='planned' else I(args.target_curvature)
    target=float(np.nextafter(float(target_enclosure.lo),-np.inf))
    if target<=0:p.error('positive curvature target required')
    problem=EndpointProblem(elimination,np.arange(args.angles)*2*np.pi/args.angles,float(width.hi),float(height_budget),
        tip_design,args.j_floor,args.kappa_floor,args.fixed_offset,args.first_coefficient_bound,
        args.higher_coefficient_bound,args.derived_coefficient_bound)
    normalized=NormalizedEndpoint(problem,target,args.feasibility_smoothing)
    dense=CosineLiftProblem(float(elimination.a),float(elimination.b),elimination.modes,
        np.arange(args.dense_angles)*2*np.pi/args.dense_angles,float(width.hi),float(height_budget),
        args.j_floor,args.kappa_floor,args.fixed_offset)
    free,warm_source=read_warm(args.warm_input,elimination,args.half_width,args.fixed_offset)
    warm_preserved=free.copy()
    if args.fixed_offset is None and args.offset_policy=='auto':
        free[-1]=0
        height=problem.base.evaluate(problem.physical(free))['height'].v
        free[-1]=-(float(np.min(height))+float(np.max(height)))/2
    nheight=problem.nheight
    bounds=[(-args.first_coefficient_bound,args.first_coefficient_bound)]+[
        (-args.higher_coefficient_bound,args.higher_coefficient_bound)]*(nheight-1)
    if args.fixed_offset is None:bounds.append((-float(height_budget),float(height_budget)))
    lower=np.array([x[0] for x in bounds]);upper=np.array([x[1] for x in bounds])
    unclipped=free.copy();free=np.maximum(np.nextafter(lower,np.inf),np.minimum(np.nextafter(upper,-np.inf),free))
    warm_source.update(projected_free_before_offset_policy=warm_preserved.tolist(),
                       offset_policy=args.offset_policy,projected_free_before_box_clipping=unclipped.tolist(),
                       actual_initial_free=free.tolist(),maximum_box_clipping=float(np.max(abs(free-unclipped))))
    initial=problem.summary(free)
    initial_identity,_,_,_=problem.freeze(free,args.half_width)
    definition={key:str(value) if isinstance(value,Path) else value for key,value in vars(args).items()}
    checkpoint=args.out.with_name(args.out.stem+'-checkpoint.json')
    evaluation=[0];iteration=[0];last_saved=[0.];history=[];best={};stage=['feasibility']
    feasibility_result={};epigraph_result={'attempted':False}

    def payload(state,status,final=False):
        frozen,exact_free,physical,map_delta=problem.freeze(state[:-1],args.half_width)
        heights=[exact_rational(x) for x in frozen['height_coefficients']]
        tipz=-9*sum(R(j*j)*h for j,h in enumerate(heights,1))
        out={'schema':'space-star-cosine-design-v1','design_branch':'exact_endpoint_warm_normalized_feasibility',
            'status':status,'definition':definition,'height_basis':'cosine',
            'frozen_physical_identity':frozen,'frozen_physical_identity_sha256':identity_hash(frozen),
            'coefficient_freezing':'actual binary64 free parameters to exact Fractions, then exact rational endpoint map',
            'warm_source':warm_source,'initial_projected_frozen_physical_identity':initial_identity,
            'free_height_harmonics':[j+1 for j in elimination.free_indices],
            'free_height_coefficients_exact_rational':[rational_json(x) for x in exact_free],
            'elimination_matrix_exact_rational':[[rational_json(x) for x in row] for row in elimination.exact],
            'derived_height_harmonics':[2,3],'derived_physical_coefficient_bound':args.derived_coefficient_bound,
            'exact_tip_q_ell_numerator_zero':sum(x*y for x,y in zip(elimination.tip,heights))==0,
            'exact_valley_q_ell_numerator_zero':sum(x*y for x,y in zip(elimination.valley,heights))==0,
            'frozen_exact_map_vs_float_evaluation_max_difference':map_delta,
            'fixed_curvature_target':target,'fixed_curvature_target_enclosure':target_enclosure.json(),
            'epigraph_curvature':float(state[-1]),'normalized_constraint_audit':normalized.violations(state),
            'collocation_audit':problem.base.summary(physical),
            'tip_turn_budget':{'constraint_kind':args.tip_budget,'padding':args.half_width,
                'necessary_tau_lower':str(tau_necessary.lo),'planned_tau':str(tau_planned.hi),
                'necessary_tip_z2_limit_enclosure':necessary.json(),'planned_tip_z2_limit_enclosure':planned.json(),
                'design_limit_binary64':tip_design,'tip_z2_exact_rational':rational_json(tipz),
                'exact_frozen_point_passes_necessary_tip_gate':rational_interval(abs(tipz)).hi<=necessary.lo,
                'necessary_gate_strictly_violated':rational_interval(abs(tipz)).lo>necessary.hi,
                'planned_constraint_failure_is_not_a_general_exclusion':True},
            'unreserved_center_height_budget':str(unreserved),'reserved_center_height_budget':str(height_budget),
            'diameter_budget_for_conditional_03_witness':diameter_budget.json(),
            'planar_certificate_source':{'path':str(args.planar_report),'sha256':hashlib.sha256(args.planar_report.read_bytes()).hexdigest()},
            'source_files_sha256':hashes,'github_repository':os.environ.get('GITHUB_REPOSITORY'),
            'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
            'evaluations_seen':evaluation[0],'iterations_seen':iteration[0],'history':history,
            'initial_collocation_audit':initial,'feasibility_solver':feasibility_result,
            'epigraph_solver':epigraph_result,'elapsed_seconds':time.monotonic()-started,
            'selection_rule':'least maximum normalized violation; feasible candidates then minimize epigraph',
            'a0_changes_during_design_not_fixed_metric_refinement':True,
            'continuous_verification_performed':False,'embedding_proved':False,
            'surface_reach_lower_proved':False,'closed_surface_constructed':False,'task_complete':False}
        if final:
            out['dense_frozen_audit']=dense.summary(physical)
            out['tip_valley_frozen_audit']=problem.base.symmetry_audit(physical)
        return out

    def consider(state,force=False):
        evaluation[0]+=1;audit=normalized.violations(state)
        if audit['maximum']<=1e-8:score=(0,float(state[-1]),audit['weighted_rms'])
        else:score=(1,audit['maximum'],audit['weighted_rms'],float(state[-1]))
        if not best or score<best['score']:best.update(score=score,state=np.array(state,copy=True))
        now=time.monotonic()
        if force or evaluation[0]==1 or evaluation[0]%args.checkpoint_every==0 or now-last_saved[0]>=args.checkpoint_seconds:
            selected=best['state'];geometry=problem.summary(selected[:-1]);violation=normalized.violations(selected)
            row={'stage':stage[0],'evaluation':evaluation[0],'iteration':iteration[0],
                'maximum_normalized_violation':violation['maximum'],'per_block_violation':violation['per_block_maximum'],
                'selected_epigraph':float(selected[-1]),'J_min_sample':geometry['J_min_sample'],
                'curvature_min_sample':geometry['curvature_min_sample'],
                'whole_width_curvature_sample':geometry['whole_width_principal_curvature_max_sample'],
                'seconds':now-started}
            history.append(row);save(checkpoint,payload(selected,'checkpoint_normalized_feasibility_candidate'))
            print(json.dumps(row),flush=True);last_saved[0]=now

    def feasibility_fun(value):
        consider(np.r_[value,target]);return normalized.feasibility_residual(value)

    first=least_squares(feasibility_fun,free,jac=normalized.feasibility_jacobian,
        bounds=(lower,upper),x_scale=(upper-lower)/2,max_nfev=args.feasibility_max_nfev,
        ftol=1e-11,xtol=1e-11,gtol=1e-11,method='trf')
    consider(np.r_[first.x,target],True)
    feasibility_result.update(success=bool(first.success),message=str(first.message),status=int(first.status),
        nfev=int(first.nfev),njev=int(first.njev) if first.njev is not None else None,
        cost=float(first.cost),optimality=float(first.optimality),
        raw_final_normalized_constraints=normalized.violations(np.r_[first.x,target]),
        raw_final_free=first.x.tolist(),
        termination_flag_is_not_feasibility_certificate=True,
        raw_final_is_sampled_feasible=bool(normalized.violations(np.r_[first.x,target])['maximum']<=1e-8))
    starting=best['state'].copy();starting_audit=normalized.violations(starting)
    if starting_audit['maximum']<=args.epigraph_start_max_violation:
        stage[0]='epigraph';epigraph_result['attempted']=True
        def constraint_fun(value):consider(value);return normalized.constraints(value)
        def callback(value):iteration[0]+=1
        second=minimize(lambda value:float(value[-1])/target,starting,
            jac=lambda value:np.r_[np.zeros(len(value)-1),1/target],method='SLSQP',
            bounds=[*bounds,(.001,target)],
            constraints=[{'type':'ineq','fun':constraint_fun,'jac':normalized.jacobian}],
            callback=callback,options={'maxiter':args.epigraph_max_iterations,'ftol':1e-11,'disp':False})
        consider(second.x,True)
        epigraph_result.update(success=bool(second.success),message=str(second.message),status=int(second.status),
            iterations=int(second.nit),nfev=int(second.nfev),raw_final_epigraph=float(second.x[-1]),
            raw_final_normalized_constraints=normalized.violations(second.x),raw_final_free=second.x[:-1].tolist())
    else:
        epigraph_result.update(reason='fixed-target feasibility was not close enough; avoid epigraph iteration from a bad immersion',
            selected_maximum_normalized_violation=starting_audit['maximum'],
            permitted_start_maximum=args.epigraph_start_max_violation)
    chosen=best['state'];report=payload(chosen,'geometry_design_frozen_cosine_warm_feasibility_candidate',True)
    save(args.out,report);save(checkpoint,report)
    print(json.dumps({'out':str(args.out),'normalized':report['normalized_constraint_audit'],
                      'selected_dense':report['dense_frozen_audit'],'task_complete':False}),flush=True)


if __name__=='__main__':main()
