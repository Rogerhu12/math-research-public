#!/usr/bin/env python3
"""Optimize whole-angle rectifying curvature with exact tip/valley constraints.

Height = sum H_j sin(3*j*phi). H_2,H_3 are eliminated by exact rational
linear algebra. SLSQP minimizes the true sampled worst curvature on |s|<=w,
with a positive material-map margin, nonzero curvature, and a continuous
height interpolation bound. Final decimal free parameters are frozen as
exact rationals, then independently resampled and enclosed continuously.
Geometry design changes a0; it is not fixed-metric refinement across trials.
Actual optimization/certification runs only in the public repository Actions.
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

from folded_reference_geometry import I, PI, DOWN, UP
from star_core_geometry import clipped, square, unit_enclosures
from space_star_flat_core import dot, cross, norm, absolute_interval


class HeightElimination:
    def __init__(self,a,b,modes):
        if modes<4:
            raise ValueError('use at least four height harmonics')
        self.a,self.b,self.modes=R(a),R(b),int(modes)
        rv,rt=1-self.a+self.b,1+self.a+self.b
        tv,tt=28*self.a-109*self.b-1,-1-28*self.a-109*self.b
        self.tip=[j*(9*j*j*rt+tt) for j in range(1,modes+1)]
        self.valley=[(-1)**j*j*(9*j*j*rv+tv) for j in range(1,modes+1)]
        self.free_indices=[0,*range(3,modes)]
        T2,T3=self.tip[1:3];V2,V3=self.valley[1:3]
        determinant=T2*V3-T3*V2
        if determinant==0:
            raise ValueError('tip/valley elimination is singular for this radial curve')
        self.exact=[[R(0) for _ in self.free_indices] for _ in range(modes)]
        for column,j in enumerate(self.free_indices):
            self.exact[j][column]=R(1)
            t,v=self.tip[j],self.valley[j]
            self.exact[1][column]=(-t*V3+T3*v)/determinant
            self.exact[2][column]=(-T2*v+t*V2)/determinant
        for column in range(len(self.free_indices)):
            for row in [self.tip,self.valley]:
                if sum(row[j]*self.exact[j][column] for j in range(modes))!=0:
                    raise AssertionError('rational elimination failed')
        self.matrix=np.array([[float(x) for x in row] for row in self.exact])

    def freeze(self,free):
        strings=[format(float(x),'.17g') for x in free]
        rational=[R(x) for x in strings]
        heights=[sum(c*x for c,x in zip(row,rational)) for row in self.exact]
        assert sum(c*x for c,x in zip(self.tip,heights))==0
        assert sum(c*x for c,x in zip(self.valley,heights))==0
        return strings,heights


class AD:
    """First-order forward differentiation of scalar fields vs free heights."""
    def __init__(self,value,gradient):
        self.v=np.asarray(value,float);self.g=np.asarray(gradient,float)
    def other(self,x):
        return x if isinstance(x,AD) else AD(np.broadcast_to(x,self.v.shape),np.zeros_like(self.g))
    def __add__(self,x):
        x=self.other(x);return AD(self.v+x.v,self.g+x.g)
    __radd__=__add__
    def __neg__(self):
        return AD(-self.v,-self.g)
    def __sub__(self,x):
        return self+-self.other(x)
    def __rsub__(self,x):
        return self.other(x)+-self
    def __mul__(self,x):
        x=self.other(x)
        return AD(self.v*x.v,self.g*x.v[:,None]+x.g*self.v[:,None])
    __rmul__=__mul__
    def __pow__(self,power):
        return AD(self.v**power,power*self.v[:,None]**(power-1)*self.g)
    def __truediv__(self,x):
        return self*self.other(x)**-1
    def absolute(self):
        return AD(abs(self.v),np.sign(self.v)[:,None]*self.g)
    def floor(self,value):
        return AD(np.maximum(self.v,value),self.g*(self.v>value)[:,None])


def adot(v,w):
    return sum((x*y for x,y in zip(v,w)),0)


def across(v,w):
    return [v[1]*w[2]-v[2]*w[1],v[2]*w[0]-v[0]*w[2],v[0]*w[1]-v[1]*w[0]]


class LiftProblem:
    def __init__(self,elimination,phi,width,height_budget,j_floor,kappa_floor):
        self.elim=elimination;self.phi=np.asarray(phi,float)
        self.width,self.height_budget=width,height_budget
        self.j_floor,self.kappa_floor=j_floor,kappa_floor
        self.nfree=elimination.matrix.shape[1]
        a,b=float(elimination.a),float(elimination.b)
        r=[(1. if k==0 else 0.)+a*3**k*np.cos(3*self.phi+k*np.pi/2)
           +b*6**k*np.cos(6*self.phi+k*np.pi/2) for k in range(5)]
        radial=[r[0],r[1],r[2]-r[0],r[3]-3*r[1],r[4]-6*r[2]+r[0]]
        angular=[np.zeros_like(self.phi),r[0],2*r[1],3*r[2]-r[0],4*r[3]-4*r[1]]
        co,si=np.cos(self.phi),np.sin(self.phi)
        self.xy=[np.stack((radial[k]*co-angular[k]*si,radial[k]*si+angular[k]*co),axis=-1)
                 for k in range(5)]
        freq=3*np.arange(1,elimination.modes+1)
        self.height_matrices=[np.sin(self.phi[:,None]*freq+k*np.pi/2)*freq**k for k in range(5)]
        self.height_gradients=[mat@elimination.matrix for mat in self.height_matrices]
        self.height_error_weights=freq**2*(2*np.pi/len(phi))**2/8
        self._cache=None

    def evaluate(self,free):
        free=np.asarray(free)
        if self._cache is not None and np.array_equal(self._cache[0],free):
            return self._cache[1]
        heights=self.elim.matrix@free
        z=[AD(mat@heights,grad) for mat,grad in zip(self.height_matrices,self.height_gradients)]
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
        error_grad=(self.height_error_weights*np.sign(heights))@self.elim.matrix
        data={'height':z[0],'height_error':error,'height_error_gradient':error_grad,
              'kappa':kappa,'tau':tau,'qell':qell,'lambda0':lambda0,'J':J,
              'heights':heights,'speed':speed,
              'regularization_used':bool(np.min(raw_W2.v)<=1e-24),
              'x':np.column_stack((self.xy[0],z[0].v)),
              'v1':np.stack([v.v for v in v1],axis=-1),
              'cross':np.stack([v.v for v in C],axis=-1)}
        self._cache=(np.array(free,copy=True),data)
        return data

    def constraints(self,state):
        d=self.evaluate(state[:-1]);cap=state[-1]
        height_margin=self.height_budget-d['height_error']
        values=[cap*d['J'].v-d['lambda0'].v,d['J'].v-self.j_floor,
                d['kappa'].v-self.kappa_floor,
                height_margin-d['height'].v,height_margin+d['height'].v]
        return np.concatenate(values)

    def constraint_jacobian(self,state):
        d=self.evaluate(state[:-1]);cap=state[-1]
        n=len(self.phi);zeros=np.zeros((n,1))
        gradients=[np.column_stack((cap*d['J'].g-d['lambda0'].g,d['J'].v)),
                   np.column_stack((d['J'].g,zeros)),
                   np.column_stack((d['kappa'].g,zeros)),
                   np.column_stack((-d['height'].g-d['height_error_gradient'],zeros)),
                   np.column_stack((d['height'].g-d['height_error_gradient'],zeros))]
        return np.vstack(gradients)

    def summary(self,free):
        d=self.evaluate(free)
        positive=np.min(d['J'].v)>0 and not d['regularization_used']
        value=float(np.max(d['lambda0'].v/d['J'].v)) if positive else None
        return {'angles':len(self.phi),'J_min_sample':float(np.min(d['J'].v)),
                'curvature_min_sample':float(np.min(d['kappa'].v)),
                'lambda0_max_sample':float(np.max(d['lambda0'].v)),
                'whole_width_principal_curvature_max_sample':value,
                'height_sample_max':float(np.max(abs(d['height'].v))),
                'height_interpolation_remainder_upper_formula':d['height_error'],
                'height_continuous_bound_before_roundoff_validation':float(np.max(abs(d['height'].v))+d['height_error']),
                'regularization_used':d['regularization_used'],'continuous_curvature_certificate':False}


def rational_interval(x):
    return I(str(x.numerator))/I(str(x.denominator))


def generic_interval_jets(s,c,a,b,heights):
    c3=clipped(4*c*c*c-3*c);s3=clipped(3*s-4*s*s*s)
    trig=[];cj,sj=I(1),I(0)
    for _ in heights:
        cj,sj=clipped(cj*c3-sj*s3),clipped(sj*c3+cj*s3)
        trig.append((sj,cj))
    c6=clipped(2*square(c3)-1);s6=clipped(2*s3*c3)
    r=[1+a*c3+b*c6,-3*a*s3-6*b*s6,-9*a*c3-36*b*c6,
       27*a*s3+216*b*s6,81*a*c3+1296*b*c6]
    z=[]
    for order in range(5):
        total=I(0)
        for j,(height,(ss,cc)) in enumerate(zip(heights,trig),1):
            angular=[ss,cc,-ss,-cc][order%4]
            total+=height*(3*j)**order*angular
        z.append(total)
    radial=[r[0],r[1],r[2]-r[0],r[3]-3*r[1],r[4]-6*r[2]+r[0]]
    angular=[I(0),r[0],2*r[1],3*r[2]-r[0],4*r[3]-4*r[1]]
    return [[radial[k]*c-angular[k]*s,radial[k]*s+angular[k]*c,z[k]] for k in range(5)]


def continuous_certificate(elim,heights,width,planar,nodes):
    _,cells=unit_enclosures(nodes)
    a,b=rational_interval(elim.a),rational_interval(elim.b)
    hh=[rational_interval(x) for x in heights];w=I(str(width))
    d=I(planar['continuous_distance_q_to_filled_star_domain']['lower'])
    Dxy=I(planar['continuous_full_curve_diameter']['upper'])
    Dlower=I(planar['continuous_full_curve_diameter']['lower'])
    unresolved=0;Jlower=D(1);height_upper=D(0);lambda_upper=D(0);lambda_lower=D(0)
    kappa_lower=None;perimeter=I(0);step=2*PI/nodes
    for s,c in cells:
        x,v1,v2,v3,v4=generic_interval_jets(s,c,a,b,hh)
        height_upper=max(height_upper,x[2].abs_upper())
        v=norm(v1);C=cross(v1,v2);W=norm(C);perimeter+=step*v
        if v.lo<=0 or W.lo<=0:
            unresolved+=1
            continue
        determinant=dot(C,v3);determinant_p=dot(v1,cross(v2,v4))
        vp=dot(v1,v2)/v;Wp=dot(C,cross(v1,v3))/W
        kappa=W/(v**3);tau=determinant/square(W)
        qphi=determinant_p*(v**3)/(W**3)+3*determinant*square(v)*vp/(W**3)-3*determinant*(v**3)*Wp/(W**4)
        qell=qphi/v;qa=absolute_interval(qell);localJ=1-w*I(qa.hi)
        Jlower=min(Jlower,localJ.lo)
        kappa_lower=kappa.lo if kappa_lower is None else min(kappa_lower,kappa.lo)
        lambda0=kappa+square(tau)/kappa
        lambda_lower=max(lambda_lower,lambda0.lo)
        if localJ.lo>0:
            lambda_upper=max(lambda_upper,(lambda0/localJ).hi)
            lower_den=1-w*I(qa.lo)
            lambda_lower=max(lambda_lower,(I(lambda0.lo)/lower_den).lo)
    regular=unresolved==0 and Jlower>0
    Dcore=(square(Dxy+2*w)+square(2*(I(height_upper)+w))).sqrt()
    witness=I(max(D(0),(d-w).lo))
    ratio=witness/I(Dcore.hi)
    curvature_ratio=None
    if lambda_lower>0:
        curvature_ratio=(I(1)/(I(lambda_lower)*Dlower)).hi
    return {'nodes':nodes,'unresolved_frame_cells':unresolved,
            'exact_height_coefficients_used':True,
            'whole_core_immersion_and_angular_closure_certified':regular,
            'J_lower':str(Jlower) if unresolved==0 else None,
            'kappa_positive_lower':str(kappa_lower) if unresolved==0 else None,
            'central_height_absolute_upper':str(height_upper),
            'perimeter':perimeter.json(),'a0_exact_enclosure':(perimeter/(2*PI)).json(),
            'whole_width_principal_curvature_upper':str(lambda_upper) if regular else None,
            'principal_curvature_max_lower_from_resolved_cells':str(lambda_lower),
            'necessary_reach_over_D_upper_from_curvature_lower':None if curvature_ratio is None else str(curvature_ratio),
            'projection_padding_upper':str(w.hi),'core_diameter_upper':str(Dcore.hi),
            'conditional_witness_distance_lower':str(witness.lo),
            'conditional_witness_over_core_D_lower':str(ratio.lo),
            'conditional_witness_ratio_at_least_03':ratio.lo>=D('.3'),
            'local_curvature_ceiling_sufficient_for_003_Dcore_budget':regular and
                (I(lambda_upper)*I('.03')*I(Dcore.hi)).hi<=1,
            'full_transition_and_caps_share_projection_height_budget_proved':False,
            'embedding_proved':False,'reach_lower_proved':False,'task_complete':False}


def normal_chord_sample(problem,free,width,angles=192):
    d=problem.evaluate(free)
    v=d['v1'];speed=np.linalg.norm(v,axis=-1);T=v/speed[:,None]
    C=d['cross'];B=C/np.linalg.norm(C,axis=-1)[:,None];N=np.cross(B,T)
    q=d['tau'].v/d['kappa'].v
    # All points of each exact section are covered by internal phi; uniform
    # material theta is unnecessary for a point-pair obstruction sample.
    indices=np.arange(0,len(problem.phi),max(1,len(problem.phi)//angles))
    xyz=np.concatenate([d['x'][indices]+s*(B[indices]+q[indices,None]*T[indices])
                        for s in [-width,0.,width]])
    normals=np.tile(N[indices],(3,1))
    best=np.inf
    for start in range(0,len(xyz),128):
        delta=xyz[None,:,:]-xyz[start:start+128,None,:]
        distance2=np.sum(delta*delta,axis=-1)
        denom=2*np.abs(np.sum(delta*normals[start:start+128,None,:],axis=-1))
        valid=(distance2>1e-22)&(denom>1e-18)
        ratios=np.full_like(distance2,np.inf);ratios[valid]=distance2[valid]/denom[valid]
        best=min(best,float(np.min(ratios)))
    return {'points':len(xyz),'minimum_normal_chord_radius_sample':best,
            'reach_lower_bound':False,'continuous_or_roundoff_certified':False}


def load_planar(path,a,b):
    data=json.loads(path.read_text())
    if data.get('schema')!='star-core-continuous-geometry-v1' or data.get('status')!='public_actions_geometric_screen':
        raise ValueError('use a published planar Actions certificate')
    match=[x for x in data['candidates'] if R(x['a'])==R(a) and R(x['b'])==R(b)]
    if len(match)!=1:
        raise ValueError('no unique matching planar parameter pair')
    return match[0]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--a',default='.60');p.add_argument('--b',default='.09')
    p.add_argument('--height-modes',type=int,default=4)
    p.add_argument('--half-width',type=float,default=.02)
    p.add_argument('--angles',type=int,default=384)
    p.add_argument('--dense-angles',type=int,default=3072)
    p.add_argument('--initial-lifts',default='.10,.20,.30')
    p.add_argument('--higher-coefficient-bound',type=float,default=.08)
    p.add_argument('--j-floor',type=float,default=.15)
    p.add_argument('--kappa-floor',type=float,default=.04)
    p.add_argument('--max-iterations',type=int,default=200)
    p.add_argument('--certificate-nodes',type=int,default=4096)
    p.add_argument('--planar-report',type=Path,required=True)
    p.add_argument('--check-only',action='store_true')
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    if not args.check_only and (os.environ.get('GITHUB_ACTIONS')!='true' or
            os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        p.error('optimization and certificates run only in this public repository Actions')
    if args.height_modes<4 or not 0<args.half_width or not 0<args.j_floor<1:
        p.error('need >=4 height modes, positive width, and 0<j-floor<1')
    planar=load_planar(args.planar_report,args.a,args.b)
    w=I(str(args.half_width));d=I(planar['continuous_distance_q_to_filled_star_domain']['lower'])
    Dxy=I(planar['continuous_full_curve_diameter']['upper'])
    maximum_diameter=(d-w)/I('.3')
    square_budget=square(I(maximum_diameter.lo))-square(Dxy+2*w)
    if square_budget.lo<=0:
        p.error('padding alone exhausts the planar amplitude budget')
    height_budget=(I(square_budget.lo).sqrt()/2-w).lo
    if height_budget<=D('.02'):
        p.error('height budget does not accommodate the stated positive first-mode lower bound')
    elim=HeightElimination(args.a,args.b,args.height_modes)
    n=32 if args.check_only else args.angles
    problem=LiftProblem(elim,np.arange(n)*2*np.pi/n,args.half_width,float(height_budget),args.j_floor,args.kappa_floor)
    started=time.monotonic();records=[]
    if args.check_only:
        free=np.zeros(elim.matrix.shape[1]);free[0]=.2
        if len(free)>1:free[1]=.001
        state=np.r_[free,50.]
        direction=np.random.default_rng(20261114).normal(size=len(state));direction/=np.linalg.norm(direction)
        eps=2e-7
        numeric=(problem.constraints(state+eps*direction)-problem.constraints(state-eps*direction))/(2*eps)
        analytic=problem.constraint_jacobian(state)@direction
        _,heights=elim.freeze(free)
        report={'schema':'space-star-lift-design-check-v1','status':'development_derivative_and_exact_elimination_check_only',
            'height_modes':args.height_modes,'no_optimization_performed':True,
            'tip_exact_constraint_zero':sum(a*b for a,b in zip(elim.tip,heights))==0,
            'valley_exact_constraint_zero':sum(a*b for a,b in zip(elim.valley,heights))==0,
            'constraint_jacobian_directional_relative_error':float(np.linalg.norm(numeric-analytic)/max(np.linalg.norm(numeric),1e-30)),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    else:
        dense=LiftProblem(elim,np.arange(args.dense_angles)*2*np.pi/args.dense_angles,args.half_width,
                          float(height_budget),args.j_floor,args.kappa_floor)
        bounds=[(.02,min(.75,float(height_budget)))]+[(-args.higher_coefficient_bound,args.higher_coefficient_bound)]*(elim.matrix.shape[1]-1)+[(.01,10000.)]
        for initial in args.initial_lifts.split(','):
            free=np.zeros(elim.matrix.shape[1]);free[0]=np.clip(float(initial),*bounds[0])
            summary=problem.summary(free)
            cap=summary['whole_width_principal_curvature_max_sample']
            state=np.r_[free,100. if cap is None else min(9999.,1.05*cap)]
            iterations=[0]
            def callback(x):
                iterations[0]+=1
                if iterations[0]%10==1:
                    print(json.dumps({'initial_lift':initial,'iteration':iterations[0],
                        'epigraph_curvature':float(x[-1]),'minimum_constraint':float(np.min(problem.constraints(x))),
                        'seconds':time.monotonic()-started}),flush=True)
            result=minimize(lambda x:float(x[-1]),state,jac=lambda x:np.r_[np.zeros(len(x)-1),1.],
                method='SLSQP',bounds=bounds,constraints=[{'type':'ineq','fun':problem.constraints,'jac':problem.constraint_jacobian}],
                callback=callback,options={'maxiter':args.max_iterations,'ftol':1e-10,'disp':False})
            strings,heights=elim.freeze(result.x[:-1])
            frozen=np.array([float(R(x)) for x in strings])
            audit=dense.summary(frozen)
            records.append({'initial_lift':initial,'solver_success':bool(result.success),'message':str(result.message),
                'iterations':int(result.nit),'epigraph_curvature':float(result.x[-1]),
                'minimum_collocation_constraint':float(np.min(problem.constraints(np.r_[frozen,result.x[-1]]))),
                'free_coefficients_exact_decimal':strings,
                'height_coefficients_exact_rational':[{'numerator':str(x.numerator),'denominator':str(x.denominator)} for x in heights],
                'dense_frozen_audit':audit})
        def rank(row):
            a=row['dense_frozen_audit'];value=a['whole_width_principal_curvature_max_sample']
            valid=value is not None and a['height_continuous_bound_before_roundoff_validation']<=float(height_budget)+1e-10 and a['curvature_min_sample']>0
            return (not valid,np.inf if value is None else value)
        best=min(records,key=rank)
        frozen=np.array([float(R(x)) for x in best['free_coefficients_exact_decimal']])
        heights=[R(x['numerator'])/R(x['denominator']) for x in best['height_coefficients_exact_rational']]
        print(json.dumps({'stage':'certifying_frozen_coefficients','nodes':args.certificate_nodes}),flush=True)
        cert=continuous_certificate(elim,heights,args.half_width,planar,args.certificate_nodes)
        chords=None
        if cert['whole_core_immersion_and_angular_closure_certified']:
            chords=normal_chord_sample(dense,frozen,args.half_width)
        report={'schema':'space-star-lift-design-v1','status':'geometry_design_then_frozen_certificate_attempt',
            'definition':{k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},
            'planar_certificate_source':{'path':str(args.planar_report),'sha256':hashlib.sha256(args.planar_report.read_bytes()).hexdigest()},
            'height_budget_from_true_planar_bounds':str(height_budget),
            'diameter_budget_for_conditional_03_witness':maximum_diameter.json(),
            'a0_changes_during_design_not_fixed_metric_refinement':True,
            'free_height_coefficient_harmonics':[j+1 for j in elim.free_indices],
            'optimization_objective':'min t subject to t*(1-w*abs(q_ell))-lambda0 >=0 at all collocation angles',
            'exact_tip_and_valley_torsion_constraints_eliminated':True,
            'optimization_trials':records,'selected_frozen_candidate':best,
            'continuous_certificate':cert,'normal_chord_samples':chords,
            'elapsed_seconds':time.monotonic()-started,
            'source_sha256':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                for name in ['space_star_lift_design.py','space_star_flat_core.py','star_core_geometry.py','folded_reference_geometry.py']},
            'claim':{'exact_local_formula':True,'global_closure_obtained':False,
                      'closed_surface_reach_certified':False,'task_complete':False}}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'out':str(args.out),'status':report['status']}),flush=True)


if __name__=='__main__':
    main()
