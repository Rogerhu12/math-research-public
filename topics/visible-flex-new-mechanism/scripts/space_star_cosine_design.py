#!/usr/bin/env python3
"""Design a zero-framing cosine-lift rectifying core, one case per run.

All six cosine heights are free; the former sine tip/valley elimination is
absent. The optional vertical offset changes position only and is frozen with
the actual binary64 height coefficients as exact rational data. Minimizing the
sampled whole-width curvature does not certify embedding or reach. A separate
continuous verifier consumes frozen_physical_identity without reselecting it.
Research optimization runs only in this public repository's GitHub Actions.
"""
from __future__ import annotations

import argparse
from decimal import Decimal as D
from fractions import Fraction as R
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np
from scipy.optimize import minimize

from folded_reference_geometry import I
from star_core_geometry import square
from space_star_lift_design import AD,adot,across,load_planar,normal_chord_sample


def rational_json(x):
    return {'numerator':str(x.numerator),'denominator':str(x.denominator)}


class CosineLiftProblem:
    def __init__(self,a,b,modes,phi,width,height_budget,j_floor=.3,kappa_floor=.1,fixed_offset=None):
        self.a,self.b=float(a),float(b)
        self.modes=int(modes);self.phi=np.asarray(phi,float)
        self.width,self.height_budget=float(width),float(height_budget)
        self.j_floor,self.kappa_floor=float(j_floor),float(kappa_floor)
        self.fixed_offset=None if fixed_offset is None else float(fixed_offset)
        self.nfree=self.modes+(fixed_offset is None)
        r=[(1. if k==0 else 0.)+self.a*3**k*np.cos(3*self.phi+k*np.pi/2)
           +self.b*6**k*np.cos(6*self.phi+k*np.pi/2) for k in range(5)]
        radial=[r[0],r[1],r[2]-r[0],r[3]-3*r[1],r[4]-6*r[2]+r[0]]
        angular=[np.zeros_like(self.phi),r[0],2*r[1],3*r[2]-r[0],4*r[3]-4*r[1]]
        co,si=np.cos(self.phi),np.sin(self.phi)
        self.xy=[np.stack((radial[k]*co-angular[k]*si,radial[k]*si+angular[k]*co),axis=-1)
                 for k in range(5)]
        freq=3*np.arange(1,self.modes+1)
        self.height_matrices=[np.cos(self.phi[:,None]*freq+k*np.pi/2)*freq**k for k in range(5)]
        self.height_gradients=[np.column_stack((mat,np.ones(len(phi)) if k==0 else np.zeros(len(phi))))
                               if fixed_offset is None else mat
                               for k,mat in enumerate(self.height_matrices)]
        self.height_error_weights=freq**2*(2*np.pi/len(phi))**2/8
        self._cache=None

    def unpack(self,free):
        return free[:self.modes],float(free[-1] if self.fixed_offset is None else self.fixed_offset)

    def evaluate(self,free):
        free=np.asarray(free,float)
        if self._cache is not None and np.array_equal(self._cache[0],free):
            return self._cache[1]
        heights,offset=self.unpack(free)
        z=[AD(mat@heights+(offset if k==0 else 0.),grad)
           for k,(mat,grad) in enumerate(zip(self.height_matrices,self.height_gradients))]
        zero=np.zeros((len(self.phi),self.nfree))
        vec=[[AD(xy[:,0],zero),AD(xy[:,1],zero),zz] for xy,zz in zip(self.xy,z)]
        v1,v2,v3,v4=vec[1:]
        speed=adot(v1,v1)**.5
        C=across(v1,v2);raw_W2=adot(C,C)
        W=raw_W2.floor(1e-24)**.5
        Cp=across(v1,v3)
        determinant=adot(C,v3);determinant_p=adot(v1,across(v2,v4))
        vp=adot(v1,v2)/speed;Wp=adot(C,Cp)/W
        kappa=W/speed**3;tau=determinant/W**2
        qphi=determinant_p*speed**3/W**3+3*determinant*speed**2*vp/W**3-3*determinant*speed**3*Wp/W**4
        qell=qphi/speed;lambda0=kappa+tau**2/kappa
        J=1-self.width*qell.absolute()
        error=float(self.height_error_weights@abs(heights))
        error_gradient=np.zeros(self.nfree)
        error_gradient[:self.modes]=self.height_error_weights*np.sign(heights)
        data={'height':z[0],'height_error':error,'height_error_gradient':error_gradient,
              'kappa':kappa,'tau':tau,'qell':qell,'lambda0':lambda0,'J':J,
              'heights':heights,'height_offset':offset,'speed':speed,
              'regularization_used':bool(np.min(raw_W2.v)<=1e-24),
              'x':np.column_stack((self.xy[0],z[0].v)),
              'v1':np.stack([v.v for v in v1],axis=-1),
              'cross':np.stack([v.v for v in C],axis=-1)}
        self._cache=(np.array(free,copy=True),data)
        return data

    def constraints(self,state):
        data=self.evaluate(state[:-1]);cap=state[-1]
        margin=self.height_budget-data['height_error']
        return np.concatenate([cap*data['J'].v-data['lambda0'].v,
            data['J'].v-self.j_floor,data['kappa'].v-self.kappa_floor,
            margin-data['height'].v,margin+data['height'].v])

    def constraint_jacobian(self,state):
        data=self.evaluate(state[:-1]);cap=state[-1];zero=np.zeros((len(self.phi),1))
        return np.vstack([
            np.column_stack((cap*data['J'].g-data['lambda0'].g,data['J'].v)),
            np.column_stack((data['J'].g,zero)),
            np.column_stack((data['kappa'].g,zero)),
            np.column_stack((-data['height'].g-data['height_error_gradient'],zero)),
            np.column_stack((data['height'].g-data['height_error_gradient'],zero))])

    def summary(self,free):
        data=self.evaluate(free)
        positive=np.min(data['J'].v)>0 and not data['regularization_used']
        maximum=float(np.max(data['lambda0'].v/data['J'].v)) if positive else None
        return {'angles':len(self.phi),'J_min_sample':float(np.min(data['J'].v)),
            'curvature_min_sample':float(np.min(data['kappa'].v)),
            'curvature_max_sample':float(np.max(data['kappa'].v)),
            'torsion_absolute_max_sample':float(np.max(abs(data['tau'].v))),
            'q_ell_absolute_max_sample':float(np.max(abs(data['qell'].v))),
            'lambda0_max_sample':float(np.max(data['lambda0'].v)),
            'whole_width_principal_curvature_max_sample':maximum,
            'height_sample_min':float(np.min(data['height'].v)),
            'height_sample_max':float(np.max(data['height'].v)),
            'height_absolute_sample_max':float(np.max(abs(data['height'].v))),
            'height_interpolation_remainder_upper_formula':data['height_error'],
            'height_absolute_bound_before_roundoff_validation':float(np.max(abs(data['height'].v))+data['height_error']),
            'design_height_budget':self.height_budget,
            'height_budget_margin_before_roundoff_validation':self.height_budget-float(np.max(abs(data['height'].v)))-data['height_error'],
            'regularization_used':data['regularization_used'],
            'continuous_curvature_certificate':False,'embedding_proved':False,'reach_lower_proved':False}

    def symmetry_audit(self,free):
        points=CosineLiftProblem(self.a,self.b,self.modes,np.array([0.,np.pi/3]),self.width,
                                self.height_budget,self.j_floor,self.kappa_floor,self.fixed_offset)
        data=points.evaluate(free);heights,offset=self.unpack(free)
        formula=[]
        for index,sign in enumerate([1.,-1.]):
            r=1+self.a*sign+self.b
            r2=-9*self.a*sign-36*self.b;r4=81*self.a*sign+1296*self.b
            radial=r2-r;fourth=r4-6*r2+r
            parity=np.array([sign**j for j in range(1,self.modes+1)])
            freq=3*np.arange(1,self.modes+1)
            z2=float(np.sum(-freq**2*heights*parity));z4=float(np.sum(freq**4*heights*parity))
            denominator=radial*radial+z2*z2
            kappa=np.sqrt(denominator)/(r*r)
            qell=(z2*fourth-radial*z4)/denominator**1.5
            J=1-self.width*abs(qell)
            formula.append({'location':'tip' if index==0 else 'valley',
                'torsion_exactly_zero_by_even_reflection':True,
                'torsion_numeric_residual':float(abs(data['tau'].v[index])),
                'kappa_from_symmetry_formula':float(kappa),'q_ell_from_symmetry_formula':float(qell),
                'q_ell_formula_numeric_discrepancy':float(abs(qell-data['qell'].v[index])),
                'whole_width_J_at_point':float(J),
                'whole_width_principal_curvature_at_point':float(kappa/J) if J>0 else None,
                'automatic_torsion_zero_does_not_force_q_ell_zero':True})
        return formula


def identity(a,b,width,problem,free):
    heights,offset=problem.unpack(np.asarray(free,float))
    out={'height_basis':'cosine','a':str(R(a)),'b':str(R(b)),'half_width':str(R(width)),
         'height_coefficients':[rational_json(R.from_float(float(x))) for x in heights],
         'height_offset':rational_json(R.from_float(offset))}
    encoded=json.dumps(out,sort_keys=True,separators=(',',':'))
    return out,hashlib.sha256(encoded.encode()).hexdigest()


def developer_check():
    a,b='.07','.005';modes=6;phi=np.arange(32)*2*np.pi/32
    checks=[];symmetry=[]
    for fixed in [None,.013]:
        problem=CosineLiftProblem(a,b,modes,phi,.02,.4,.1,.03,fixed)
        free=np.array([.04,.003,-.0005,.00008,-.00001,.000001]+([] if fixed is not None else [.013]))
        state=np.r_[free,50.]
        direction=np.random.default_rng(99127).normal(size=len(state));direction/=np.linalg.norm(direction)
        eps=2e-7
        fd=(problem.constraints(state+eps*direction)-problem.constraints(state-eps*direction))/(2*eps)
        exact=problem.constraint_jacobian(state)@direction
        rel=float(np.linalg.norm(fd-exact)/max(np.linalg.norm(fd),1e-30))
        reverse=CosineLiftProblem(a,b,modes,-phi,.02,.4,.1,.03,fixed)
        p,q=problem.evaluate(free),reverse.evaluate(free)
        parity={'height_even':float(np.max(abs(p['height'].v-q['height'].v))),
                'kappa_even':float(np.max(abs(p['kappa'].v-q['kappa'].v))),
                'torsion_odd':float(np.max(abs(p['tau'].v+q['tau'].v))),
                'q_ell_even':float(np.max(abs(p['qell'].v-q['qell'].v)))}
        ident,_=identity(a,b,'.02',problem,free)
        reconstructed=[float(R(int(v['numerator']),int(v['denominator']))) for v in ident['height_coefficients']]
        off=ident['height_offset'];offset=float(R(int(off['numerator']),int(off['denominator'])))
        exact_roundtrip=np.array_equal(np.asarray(reconstructed),free[:modes]) and offset==problem.unpack(free)[1]
        checks.append({'fixed_offset':fixed,'jacobian_directional_relative_error':rel,
                       'symmetry_errors':parity,'binary64_rational_identity_roundtrip_exact':bool(exact_roundtrip)})
        symmetry.extend(problem.symmetry_audit(free))
    passed=all(v['jacobian_directional_relative_error']<2e-5 and
               max(v['symmetry_errors'].values())<1e-8 and v['binary64_rational_identity_roundtrip_exact'] for v in checks)
    passed=passed and all(v['torsion_numeric_residual']<1e-10 and
                          v['q_ell_formula_numeric_discrepancy']<1e-8 for v in symmetry)
    return {'schema':'space-star-cosine-design-development-v1','development_check_only':True,
            'research_geometry_evaluated':False,'optimization_performed':False,
            'checks':checks,'tip_valley_checks':symmetry,'passed':bool(passed)}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--a',default='.65');p.add_argument('--b',default='.12')
    p.add_argument('--height-modes',type=int,default=6);p.add_argument('--half-width',default='.02')
    p.add_argument('--angles',type=int,default=768);p.add_argument('--dense-angles',type=int,default=6144)
    p.add_argument('--initial-lift',type=float,default=.15)
    p.add_argument('--initial-coefficients',default='');p.add_argument('--initial-offset',type=float,default=0.)
    p.add_argument('--fixed-offset',type=float)
    p.add_argument('--first-coefficient-bound',type=float,default=.6)
    p.add_argument('--higher-coefficient-bound',type=float,default=.12)
    p.add_argument('--j-floor',type=float,default=.3);p.add_argument('--kappa-floor',type=float,default=.1)
    p.add_argument('--height-reserve',default='.02')
    p.add_argument('--max-iterations',type=int,default=400)
    p.add_argument('--checkpoint-every',type=int,default=10);p.add_argument('--checkpoint-seconds',type=float,default=60.)
    p.add_argument('--planar-report',type=Path);p.add_argument('--check-only',action='store_true')
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    source_files=['space_star_cosine_design.py','space_star_lift_design.py','space_star_flat_core.py',
                  'star_core_geometry.py','folded_reference_geometry.py']
    hashes={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in source_files}
    if args.check_only:
        report=developer_check();report['source_files_sha256']=hashes
        args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
        print(json.dumps({'passed':report['passed'],'checks':report['checks']}),flush=True)
        if not report['passed']:raise SystemExit(1)
        return
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        p.error('cosine geometry design runs only in this public repository Actions')
    if args.planar_report is None or args.height_modes<1 or args.angles<24*args.height_modes:
        p.error('need published planar report, positive mode count and adequate angular grid')
    if R(args.half_width)<=0 or R(args.height_reserve)<0 or not 0<args.j_floor<1 or args.checkpoint_every<1:
        p.error('positive width, 0<j-floor<1 and positive checkpoint interval required')
    planar=load_planar(args.planar_report,args.a,args.b)
    width=I(args.half_width)
    distance=I(planar['continuous_distance_q_to_filled_star_domain']['lower'])
    dxy=I(planar['continuous_full_curve_diameter']['upper'])
    diameter_budget=(distance-width)/I('.3')
    budget2=square(I(diameter_budget.lo))-square(dxy+2*width)
    if budget2.lo<=0:p.error('planar padding exhausts the amplitude budget')
    full_height_budget=(I(budget2.lo).sqrt()/2-width).lo
    height_budget=(I(full_height_budget)-I(args.height_reserve)).lo
    if height_budget<=0:p.error('height reserve exhausts the available central height')
    problem=CosineLiftProblem(args.a,args.b,args.height_modes,np.arange(args.angles)*2*np.pi/args.angles,
                             float(width.hi),float(height_budget),args.j_floor,args.kappa_floor,args.fixed_offset)
    dense=CosineLiftProblem(args.a,args.b,args.height_modes,np.arange(args.dense_angles)*2*np.pi/args.dense_angles,
                           float(width.hi),float(height_budget),args.j_floor,args.kappa_floor,args.fixed_offset)
    heights=np.zeros(args.height_modes)
    if args.initial_coefficients:
        parsed=[float(v) for v in args.initial_coefficients.split(',')]
        if len(parsed)!=args.height_modes:p.error('initial-coefficients must specify every mode')
        heights[:]=parsed
    else:heights[0]=args.initial_lift
    free=np.r_[heights,args.initial_offset] if args.fixed_offset is None else heights
    bounds=[(-args.first_coefficient_bound,args.first_coefficient_bound)]+[(-args.higher_coefficient_bound,args.higher_coefficient_bound)]*(args.height_modes-1)
    if args.fixed_offset is None:bounds.append((-float(height_budget),float(height_budget)))
    bounds.append((.001,10000.))
    free=np.array([np.clip(v,*bound) for v,bound in zip(free,bounds[:-1])])
    first=problem.summary(free);cap=first['whole_width_principal_curvature_max_sample']
    state=np.r_[free,100. if cap is None else min(9999.,max(.01,1.05*cap))]
    started=time.monotonic();last_save=[0.];evaluations=[0];iterations=[0];best={};history=[]
    checkpoint=args.out.with_name(args.out.stem+'-checkpoint.json')
    definition={key:str(value) if isinstance(value,Path) else value for key,value in vars(args).items()}
    def payload(value,status,final=False):
        frozen,identity_hash=identity(args.a,args.b,args.half_width,problem,value[:-1])
        result={'schema':'space-star-cosine-design-v1','status':status,'definition':definition,
            'height_basis':'cosine','frozen_physical_identity':frozen,'frozen_physical_identity_sha256':identity_hash,
            'coefficient_freezing':'Fraction.from_float of the selected actual binary64 coefficient and offset',
            'exact_tip_and_valley_torsion_zero_by_even_reflection':True,
            'old_sine_tip_valley_elimination_used':False,
            'zero_framing_theorem_requires_nonzero_curvature_and_regular_Jordan_planar_projection':True,
            'a0_changes_during_design_not_fixed_metric_refinement':True,
            'epigraph_curvature':float(value[-1]),
            'minimum_collocation_constraint':float(np.min(problem.constraints(value))),
            'collocation_audit':problem.summary(value[:-1]),
            'unreserved_center_height_budget':str(full_height_budget),'reserved_center_height_budget':str(height_budget),
            'diameter_budget_for_conditional_03_witness':diameter_budget.json(),
            'planar_certificate_source':{'path':str(args.planar_report),
                'sha256':hashlib.sha256(args.planar_report.read_bytes()).hexdigest()},
            'source_files_sha256':hashes,'github_repository':os.environ.get('GITHUB_REPOSITORY'),
            'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
            'evaluations_seen':evaluations[0],'iterations_seen':iterations[0],'history':history,
            'elapsed_seconds':time.monotonic()-started,'continuous_verification_performed':False,
            'embedding_proved':False,'surface_reach_lower_proved':False,'closed_surface_constructed':False,'task_complete':False}
        if final:
            result['dense_frozen_audit']=dense.summary(value[:-1])
            result['tip_valley_frozen_audit']=problem.symmetry_audit(value[:-1])
            if result['dense_frozen_audit']['J_min_sample']>0 and not result['dense_frozen_audit']['regularization_used']:
                result['normal_chord_samples']=normal_chord_sample(dense,value[:-1],float(width.hi),192)
        return result
    def save(path,result):
        path.parent.mkdir(parents=True,exist_ok=True);tmp=path.with_suffix('.tmp')
        tmp.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');tmp.replace(path)
    def consider(value,force=False):
        constraints=problem.constraints(value);evaluations[0]+=1
        violation=max(0.,float(-np.min(constraints)))
        score=(0,float(value[-1])) if violation<=1e-8 else (1,violation,float(value[-1]))
        if not best or score<best['score']:best.update(score=score,state=np.array(value,copy=True))
        now=time.monotonic()
        if force or evaluations[0]==1 or evaluations[0]%args.checkpoint_every==0 or now-last_save[0]>=args.checkpoint_seconds:
            chosen=best['state'];audit=problem.summary(chosen[:-1])
            entry={'evaluation':evaluations[0],'iteration':iterations[0],
                   'selected_epigraph':float(chosen[-1]),'selected_min_constraint':float(np.min(problem.constraints(chosen))),
                   'J_min_sample':audit['J_min_sample'],'curvature_min_sample':audit['curvature_min_sample'],
                   'whole_width_curvature_sample':audit['whole_width_principal_curvature_max_sample'],
                   'height_absolute_bound':audit['height_absolute_bound_before_roundoff_validation'],
                   'seconds':now-started}
            history.append(entry);save(checkpoint,payload(chosen,'checkpoint_selected_sampled_candidate'))
            print(json.dumps(entry),flush=True);last_save[0]=now
        return constraints
    def callback(value):iterations[0]+=1
    result=minimize(lambda value:float(value[-1]),state,jac=lambda value:np.r_[np.zeros(len(value)-1),1.],
                    method='SLSQP',bounds=bounds,
                    constraints=[{'type':'ineq','fun':consider,'jac':problem.constraint_jacobian}],
                    callback=callback,options={'maxiter':args.max_iterations,'ftol':1e-10,'disp':False})
    consider(result.x,True);chosen=best['state']
    report=payload(chosen,'geometry_design_frozen_cosine_candidate',True)
    report['initial_collocation_audit']=first
    report['solver']={'success':bool(result.success),'message':str(result.message),'status':int(result.status),
        'iterations':int(result.nit),'nfev':int(result.nfev),'final_epigraph':float(result.x[-1]),
        'final_minimum_collocation_constraint':float(np.min(problem.constraints(result.x))),
        'selection_rule':'best sampled feasible epigraph if available; otherwise least sampled violation; no continuous feasibility assumed'}
    report['raw_final_frozen_physical_identity']=identity(args.a,args.b,args.half_width,problem,result.x[:-1])[0]
    report['raw_final_dense_audit']=dense.summary(result.x[:-1])
    save(args.out,report);save(checkpoint,report)
    print(json.dumps({'out':str(args.out),'selected_dense':report['dense_frozen_audit'],'task_complete':False}),flush=True)


if __name__=='__main__':
    main()
