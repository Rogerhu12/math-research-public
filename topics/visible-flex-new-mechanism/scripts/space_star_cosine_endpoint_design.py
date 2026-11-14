#!/usr/bin/env python3
"""Cosine-core design with exact tip/valley q_ell=0 and a tip-turn budget.

This is a new geometry-design subspace, not refinement of the rejected cosine
point. H2,H3 are derived from two exact rational linear equations for q_ell;
all remaining heights and the optional vertical offset remain free. Selected
binary64 free coefficients are frozen as exact rationals and then passed
through the exact defining linear map. A separate verifier sees only the
resulting full physical cosine identity.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as R
from decimal import Decimal as D
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np
from scipy.optimize import minimize

from folded_reference_geometry import I
from star_core_geometry import square
from space_star_lift_design import load_planar,rational_interval
from space_star_flat_core import absolute_interval
from space_star_cosine_design import CosineLiftProblem,rational_json
from cosine_rectifying_core import identity_hash


class EndpointElimination:
    def __init__(self,a,b,modes=6):
        self.a,self.b=R(a),R(b);self.modes=int(modes)
        if self.modes<3:raise ValueError('at least three cosine harmonics required')
        self.rows=[]
        for sign in [1,-1]:
            radial=-1-10*sign*self.a-37*self.b
            fourth=1+136*sign*self.a+1513*self.b
            self.rows.append([R(sign**j*j*j)*(fourth+9*j*j*radial) for j in range(1,self.modes+1)])
        self.tip,self.valley=self.rows
        self.free_indices=[0,*range(3,self.modes)]
        self.exact=[[R(0) for _ in self.free_indices] for _ in range(self.modes)]
        t2,t3=self.tip[1:3];v2,v3=self.valley[1:3]
        determinant=t2*v3-t3*v2
        if determinant==0:raise ValueError('H2/H3 q_ell elimination matrix is singular')
        for column,j in enumerate(self.free_indices):
            t,v=self.tip[j],self.valley[j]
            self.exact[j][column]=R(1)
            self.exact[1][column]=(-t*v3+t3*v)/determinant
            self.exact[2][column]=(-t2*v+t*v2)/determinant
        for row in self.rows:
            for column in range(len(self.free_indices)):
                if sum(row[j]*self.exact[j][column] for j in range(self.modes))!=0:
                    raise AssertionError('exact endpoint elimination failed')
        self.matrix=np.array([[float(x) for x in row] for row in self.exact])
        self.tip_z2=np.array([-9*j*j for j in range(1,self.modes+1)],float)

    def freeze(self,free_heights):
        exact_free=[R.from_float(float(x)) for x in free_heights]
        heights=[sum(c*x for c,x in zip(row,exact_free)) for row in self.exact]
        if any(sum(c*x for c,x in zip(row,heights))!=0 for row in self.rows):
            raise AssertionError('frozen model does not satisfy its defining endpoint equations')
        return exact_free,heights


class EndpointProblem:
    def __init__(self,elimination,phi,width,height_budget,tip_z2_limit,j_floor=.3,
                 kappa_floor=.1,fixed_offset=None,first_bound=.6,higher_bound=.12,derived_bound=.5):
        self.elimination=elimination;self.modes=elimination.modes
        self.nheight=len(elimination.free_indices)
        self.base=CosineLiftProblem(float(elimination.a),float(elimination.b),self.modes,phi,width,
                                   height_budget,j_floor,kappa_floor,fixed_offset)
        self.nfree=self.nheight+(fixed_offset is None)
        self.transform=np.zeros((self.base.nfree,self.nfree))
        self.transform[:self.modes,:self.nheight]=elimination.matrix
        if fixed_offset is None:self.transform[-1,-1]=1
        self.tip_z2_limit=float(tip_z2_limit)
        self.height_bounds=np.full(self.modes,higher_bound)
        self.height_bounds[0]=first_bound;self.height_bounds[1:3]=derived_bound

    def physical(self,free):
        return self.transform@np.asarray(free,float)

    def constraints(self,state):
        full=self.physical(state[:-1]);H=full[:self.modes]
        z2=float(self.elimination.tip_z2@H)
        return np.r_[self.base.constraints(np.r_[full,state[-1]]),
                     self.height_bounds-H,self.height_bounds+H,
                     self.tip_z2_limit-z2,self.tip_z2_limit+z2]

    def constraint_jacobian(self,state):
        full=self.physical(state[:-1])
        chain=np.zeros((self.base.nfree+1,self.nfree+1))
        chain[:-1,:-1]=self.transform;chain[-1,-1]=1
        main=self.base.constraint_jacobian(np.r_[full,state[-1]])@chain
        heights=np.column_stack((self.transform[:self.modes],np.zeros(self.modes)))
        tip=np.r_[self.elimination.tip_z2@self.transform[:self.modes],0.]
        return np.vstack((main,-heights,heights,-tip,tip))

    def summary(self,free):
        full=self.physical(free);out=self.base.summary(full)
        z2=float(self.elimination.tip_z2@full[:self.modes])
        radial=float(-1-10*self.elimination.a-37*self.elimination.b)
        out.update(tip_z2=z2,tip_z2_design_limit=self.tip_z2_limit,
                   tip_outward_unit_radial_component=abs(z2)/np.sqrt(radial*radial+z2*z2),
                   physical_height_coefficients=full[:self.modes].tolist())
        return out

    def freeze(self,free,width):
        exact_free,H=self.elimination.freeze(np.asarray(free)[:self.nheight])
        full=self.physical(free)
        offset=R.from_float(self.base.unpack(full)[1])
        ident={'height_basis':'cosine','a':str(self.elimination.a),'b':str(self.elimination.b),
               'half_width':str(R(width)),'height_coefficients':[rational_json(x) for x in H],
               'height_offset':rational_json(offset)}
        frozen_full=np.array([float(x) for x in H]+([] if self.base.fixed_offset is not None else [float(offset)]))
        return ident,exact_free,frozen_full,float(np.max(abs(frozen_full-full)))


def tip_limit(radial,width,tau):
    e=width/tau
    s=1+(2*e).sqrt()
    return absolute_interval(radial)*(s-1/s)/2


def developer_check():
    elim=EndpointElimination('.07','.005',6)
    rows=[]
    for fixed in [None,.013]:
        problem=EndpointProblem(elim,np.arange(32)*2*np.pi/32,.02,.4,1.2,.1,.03,fixed)
        free=np.array([.04,.00008,-.00001,.000001]+([] if fixed is not None else [.013]))
        state=np.r_[free,50.]
        direction=np.random.default_rng(611107).normal(size=len(state));direction/=np.linalg.norm(direction)
        eps=2e-7
        fd=(problem.constraints(state+eps*direction)-problem.constraints(state-eps*direction))/(2*eps)
        exact=problem.constraint_jacobian(state)@direction
        error=float(np.linalg.norm(fd-exact)/max(np.linalg.norm(fd),1e-30))
        ident,ef,physical,delta=problem.freeze(free,'.02')
        heights=[R(int(x['numerator']),int(x['denominator'])) for x in ident['height_coefficients']]
        endpoints=problem.base.symmetry_audit(physical)
        rows.append({'fixed_offset':fixed,'directional_jacobian_relative_error':error,
            'exact_tip_q_ell_numerator_zero':sum(x*y for x,y in zip(elim.tip,heights))==0,
            'exact_valley_q_ell_numerator_zero':sum(x*y for x,y in zip(elim.valley,heights))==0,
            'frozen_identity_hash':identity_hash(ident),'floating_exact_map_difference':delta,
            'endpoint_numeric_audits':endpoints})
    passed=all(row['directional_jacobian_relative_error']<3e-5 and
               row['exact_tip_q_ell_numerator_zero'] and row['exact_valley_q_ell_numerator_zero'] and
               max(abs(x['q_ell_from_symmetry_formula']) for x in row['endpoint_numeric_audits'])<1e-8
               for row in rows)
    return {'schema':'cosine-endpoint-design-development-v1','development_check_only':True,
            'research_geometry_evaluated':False,'optimization_performed':False,'checks':rows,'passed':bool(passed)}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--a',default='.65');p.add_argument('--b',default='.12')
    p.add_argument('--height-modes',type=int,default=6);p.add_argument('--half-width',default='.02')
    p.add_argument('--angles',type=int,default=768);p.add_argument('--dense-angles',type=int,default=6144)
    p.add_argument('--initial-lift',type=float,default=.15);p.add_argument('--initial-free-coefficients',default='')
    p.add_argument('--initial-offset',default='auto');p.add_argument('--fixed-offset',type=float)
    p.add_argument('--first-coefficient-bound',type=float,default=.6)
    p.add_argument('--higher-coefficient-bound',type=float,default=.12)
    p.add_argument('--derived-coefficient-bound',type=float,default=.5)
    p.add_argument('--j-floor',type=float,default=.3);p.add_argument('--kappa-floor',type=float,default=.1)
    p.add_argument('--height-reserve',default='.02')
    p.add_argument('--tip-budget',choices=['planned','necessary'],default='planned')
    p.add_argument('--max-iterations',type=int,default=400)
    p.add_argument('--checkpoint-every',type=int,default=10);p.add_argument('--checkpoint-seconds',type=float,default=60.)
    p.add_argument('--planar-report',type=Path);p.add_argument('--check-only',action='store_true')
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    names=['space_star_cosine_endpoint_design.py','space_star_cosine_design.py','space_star_lift_design.py',
           'cosine_rectifying_core.py','space_star_flat_core.py','star_core_geometry.py','folded_reference_geometry.py']
    hashes={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in names}
    if args.check_only:
        report=developer_check();report['source_files_sha256']=hashes
        args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
        print(json.dumps({'passed':report['passed'],'checks':report['checks']}),flush=True)
        if not report['passed']:raise SystemExit(1)
        return
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        p.error('endpoint-constrained cosine research design runs only in this public repository Actions')
    if args.planar_report is None or args.height_modes<3 or args.angles<24*args.height_modes:
        p.error('need public planar report, at least three modes, and sufficient angular nodes')
    if R(args.half_width)<=0 or R(args.height_reserve)<0 or not 0<args.j_floor<1 or args.checkpoint_every<1:
        p.error('invalid width, height reserve, J floor, or checkpoint period')
    planar=load_planar(args.planar_report,args.a,args.b)
    w=I(args.half_width);distance=I(planar['continuous_distance_q_to_filled_star_domain']['lower'])
    dxy=I(planar['continuous_full_curve_diameter']['upper'])
    dxy_lower=I(planar['continuous_full_curve_diameter']['lower'])
    diameter_budget=(distance-w)/I('.3')
    available=square(I(diameter_budget.lo))-square(dxy+2*w)
    if available.lo<=0:p.error('planar padding exhausts the displacement budget')
    unreserved=(I(available.lo).sqrt()/2-w).lo
    height_budget=(I(unreserved)-I(args.height_reserve)).lo
    if height_budget<=0:p.error('height reserve exceeds available height')
    elim=EndpointElimination(args.a,args.b,args.height_modes)
    Rt=rational_interval(-1-10*elim.a-37*elim.b)
    tau_necessary=I('.03')*dxy_lower
    tau_planned=I('.03')*I(diameter_budget.hi)
    necessary=tip_limit(Rt,w,tau_necessary);planned=tip_limit(Rt,w,tau_planned)
    chosen_bound=planned if args.tip_budget=='planned' else necessary
    limit=float(np.nextafter(float(chosen_bound.lo),-np.inf))
    problem=EndpointProblem(elim,np.arange(args.angles)*2*np.pi/args.angles,float(w.hi),float(height_budget),
        limit,args.j_floor,args.kappa_floor,args.fixed_offset,args.first_coefficient_bound,
        args.higher_coefficient_bound,args.derived_coefficient_bound)
    dense=CosineLiftProblem(float(elim.a),float(elim.b),elim.modes,np.arange(args.dense_angles)*2*np.pi/args.dense_angles,
        float(w.hi),float(height_budget),args.j_floor,args.kappa_floor,args.fixed_offset)
    nheight=len(elim.free_indices)
    free=np.zeros(problem.nfree)
    if args.initial_free_coefficients:
        parsed=[float(x) for x in args.initial_free_coefficients.split(',')]
        if len(parsed)!=nheight:p.error('initial-free-coefficients must specify H1,H4,... in that order')
        free[:nheight]=parsed
    else:free[0]=args.initial_lift
    bounds=[(-args.first_coefficient_bound,args.first_coefficient_bound)]+[
        (-args.higher_coefficient_bound,args.higher_coefficient_bound)]*(nheight-1)
    if args.fixed_offset is None:
        if args.initial_offset=='auto':
            zero=problem.base.evaluate(problem.physical(free))['height'].v
            free[-1]=-(float(np.min(zero))+float(np.max(zero)))/2
        else:free[-1]=float(args.initial_offset)
        bounds.append((-float(height_budget),float(height_budget)))
    bounds.append((.001,10000.))
    free=np.array([np.clip(x,*bb) for x,bb in zip(free,bounds[:-1])])
    initial=problem.summary(free);cap=initial['whole_width_principal_curvature_max_sample']
    state=np.r_[free,100. if cap is None else min(9999.,max(.01,1.05*cap))]
    definition={k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()}
    checkpoint=args.out.with_name(args.out.stem+'-checkpoint.json')
    started=time.monotonic();last_saved=[0.];evaluations=[0];iterations=[0];best={};history=[]
    def payload(value,status,final=False):
        frozen,exact_free,physical,map_delta=problem.freeze(value[:-1],args.half_width)
        heights=[R(int(x['numerator']),int(x['denominator'])) for x in frozen['height_coefficients']]
        tipz=-9*sum(R(j*j)*h for j,h in enumerate(heights,1))
        output={'schema':'space-star-cosine-design-v1','design_branch':'exact_tip_valley_q_ell_zero',
            'status':status,'definition':definition,'height_basis':'cosine',
            'frozen_physical_identity':frozen,'frozen_physical_identity_sha256':identity_hash(frozen),
            'coefficient_freezing':'actual binary64 free parameters as exact Fractions; derived heights by the exact defining rational map',
            'free_height_harmonics':[j+1 for j in elim.free_indices],
            'free_height_coefficients_exact_rational':[rational_json(x) for x in exact_free],
            'elimination_matrix_exact_rational':[[rational_json(x) for x in row] for row in elim.exact],
            'derived_height_harmonics':[2,3],'derived_physical_coefficient_bound':args.derived_coefficient_bound,
            'exact_tip_q_ell_numerator_zero':sum(x*y for x,y in zip(elim.tip,heights))==0,
            'exact_valley_q_ell_numerator_zero':sum(x*y for x,y in zip(elim.valley,heights))==0,
            'old_sine_tip_valley_torsion_elimination_used':False,
            'frozen_exact_map_vs_float_evaluation_max_difference':map_delta,
            'tip_z2_exact_rational':rational_json(tipz),
            'tip_turn_budget':{'constraint_kind':args.tip_budget,'padding':args.half_width,
                'necessary_tau_lower':str(tau_necessary.lo),'planned_tau':str(tau_planned.hi),
                'necessary_tip_z2_limit_enclosure':necessary.json(),'planned_tip_z2_limit_enclosure':planned.json(),
                'design_limit_binary64':limit,
                'exact_frozen_point_passes_necessary_tip_gate':rational_interval(abs(tipz)).hi<=necessary.lo,
                'necessary_gate_strictly_violated':rational_interval(abs(tipz)).lo>necessary.hi,
                'planned_constraint_failure_is_not_a_general_exclusion':True},
            'epigraph_curvature':float(value[-1]),'minimum_design_collocation_constraint':float(np.min(problem.constraints(value))),
            'collocation_audit':problem.base.summary(physical),
            'unreserved_center_height_budget':str(unreserved),'reserved_center_height_budget':str(height_budget),
            'diameter_budget_for_conditional_03_witness':diameter_budget.json(),
            'planar_certificate_source':{'path':str(args.planar_report),'sha256':hashlib.sha256(args.planar_report.read_bytes()).hexdigest()},
            'source_files_sha256':hashes,'github_repository':os.environ.get('GITHUB_REPOSITORY'),
            'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
            'evaluations_seen':evaluations[0],'iterations_seen':iterations[0],'history':history,
            'a0_changes_during_design_not_fixed_metric_refinement':True,
            'continuous_verification_performed':False,'embedding_proved':False,
            'surface_reach_lower_proved':False,'closed_surface_constructed':False,'task_complete':False,
            'elapsed_seconds':time.monotonic()-started}
        if final:
            output['dense_frozen_audit']=dense.summary(physical)
            output['tip_valley_frozen_audit']=problem.base.symmetry_audit(physical)
        return output
    def save(path,result):
        path.parent.mkdir(parents=True,exist_ok=True);tmp=path.with_suffix('.tmp')
        tmp.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');tmp.replace(path)
    def consider(value,force=False):
        rr=problem.constraints(value);evaluations[0]+=1
        violation=max(0.,float(-np.min(rr)))
        score=(0,float(value[-1])) if violation<=1e-8 else (1,violation,float(value[-1]))
        if not best or score<best['score']:best.update(score=score,state=np.array(value,copy=True))
        now=time.monotonic()
        if force or evaluations[0]==1 or evaluations[0]%args.checkpoint_every==0 or now-last_saved[0]>=args.checkpoint_seconds:
            chosen=best['state'];audit=problem.summary(chosen[:-1])
            entry={'evaluation':evaluations[0],'iteration':iterations[0],'selected_epigraph':float(chosen[-1]),
                'selected_minimum_constraint':float(np.min(problem.constraints(chosen))),
                'J_min_sample':audit['J_min_sample'],'curvature_min_sample':audit['curvature_min_sample'],
                'whole_width_curvature_sample':audit['whole_width_principal_curvature_max_sample'],
                'tip_z2':audit['tip_z2'],'seconds':now-started}
            history.append(entry);save(checkpoint,payload(chosen,'checkpoint_endpoint_constrained_candidate'))
            print(json.dumps(entry),flush=True);last_saved[0]=now
        return rr
    def callback(value):iterations[0]+=1
    result=minimize(lambda value:float(value[-1]),state,jac=lambda value:np.r_[np.zeros(len(value)-1),1.],
        method='SLSQP',bounds=bounds,constraints=[{'type':'ineq','fun':consider,'jac':problem.constraint_jacobian}],
        callback=callback,options={'maxiter':args.max_iterations,'ftol':1e-10,'disp':False})
    consider(result.x,True);chosen=best['state']
    report=payload(chosen,'geometry_design_frozen_cosine_endpoint_candidate',True)
    report['initial_collocation_audit']=initial
    report['solver']={'success':bool(result.success),'message':str(result.message),'status':int(result.status),
        'iterations':int(result.nit),'nfev':int(result.nfev),'final_epigraph':float(result.x[-1]),
        'final_minimum_design_constraint':float(np.min(problem.constraints(result.x))),
        'selection_rule':'best sampled feasible epigraph if available; otherwise least sampled violation'}
    raw_identity,_,raw_physical,_=problem.freeze(result.x[:-1],args.half_width)
    report['raw_final_frozen_physical_identity']=raw_identity
    report['raw_final_dense_audit']=dense.summary(raw_physical)
    save(args.out,report);save(checkpoint,report)
    print(json.dumps({'out':str(args.out),'selected_dense':report['dense_frozen_audit'],'task_complete':False}),flush=True)


if __name__=='__main__':main()

