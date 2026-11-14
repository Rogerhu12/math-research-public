#!/usr/bin/env python3
"""Lifted star curves and their exact rectifying flat annuli.

Theory: theta=u+s*q(u)/a0, X=gamma(u)+s*(B+q*T), q=tau/kappa.
For J=1+s*dq/dell>0, X_s=B and X_theta=a0*T exactly.  All actual
lift/width scans run in this public repository's Actions.  Local smoke is
one small implementation check, never an optimization or final certificate.
Full proof: results/R9-rectifying-flat-core.md.
"""
from __future__ import annotations

import argparse
from decimal import Decimal as D
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np

from folded_reference_geometry import I, PI, UP, DOWN
from star_core_geometry import analyze as planar_analyze
from star_core_geometry import clipped, square, unit_enclosures


def dot(v,w):
    return sum((a*b for a,b in zip(v,w)),I(0))


def cross(v,w):
    return [v[1]*w[2]-v[2]*w[1],v[2]*w[0]-v[0]*w[2],v[0]*w[1]-v[1]*w[0]]


def norm(v):
    value=sum((square(a) for a in v),I(0)).sqrt()
    return I(max(D(0),value.lo),value.hi)


def resolve_mix(a_text,b_text,spec):
    a,b=I(a_text),I(b_text)
    if spec=='valley-zero':
        r=1-a+b;third=28*a-109*b-1
        return (9*r+third)/(72*r+2*third)
    if spec=='tip-zero':
        r=1+a+b;third=-1-28*a-109*b
        return -(9*r+third)/(72*r+2*third)
    return I(spec)


def absolute_interval(x):
    return I(0 if x.lo<=0<=x.hi else min(abs(x.lo),abs(x.hi)),x.abs_upper())


def lift_height_bound(h,mix):
    """Exact critical equation for |h(sin t+mix*sin 2t)|."""
    if mix.lo==mix.hi==0:
        return h
    root=(1+32*square(mix)).sqrt()
    candidates=[(-1+root)/(8*mix),(-1-root)/(8*mix)]
    lower,upper=D(0),D(0)
    for c in candidates:
        if c.hi<-1 or c.lo>1:
            continue
        c=clipped(c)
        sine2=1-square(c)
        sine=I(max(D(0),sine2.lo),max(D(0),sine2.hi)).sqrt()
        value=absolute_interval(h*sine*(1+2*mix*c))
        lower=max(lower,value.lo);upper=max(upper,value.hi)
    return I(lower,upper)


def interval_curve_jets(s,c,a,b,h,mix):
    c3=clipped(4*c*c*c-3*c);s3=clipped(3*s-4*s*s*s)
    c6=clipped(2*square(c3)-1);s6=clipped(2*s3*c3)
    r=[1+a*c3+b*c6,-3*a*s3-6*b*s6,-9*a*c3-36*b*c6,
       27*a*s3+216*b*s6,81*a*c3+1296*b*c6]
    z=[h*(s3+mix*s6),h*(3*c3+6*mix*c6),h*(-9*s3-36*mix*s6),
       h*(-27*c3-216*mix*c6),h*(81*s3+1296*mix*s6)]
    radial=[r[0],r[1],r[2]-r[0],r[3]-3*r[1],r[4]-6*r[2]+r[0]]
    angular=[I(0),r[0],2*r[1],3*r[2]-r[0],4*r[3]-4*r[1]]
    return [[radial[k]*c-angular[k]*s,radial[k]*s+angular[k]*c,z[k]] for k in range(5)]


def continuous_frame_bounds(a_text,b_text,h_text,mix,cells):
    a,b,h=map(I,[a_text,b_text,h_text])
    kmin=None;kmax=D(0);taumax=D(0);qmax=D(0);qlmax=D(0)
    lambda0_upper=D(0);lambda0_max_lower=D(0);perimeter=I(0);unresolved=0
    step=2*PI/len(cells)
    for s,c in cells:
        _,v1,v2,v3,v4=interval_curve_jets(s,c,a,b,h,mix)
        v=norm(v1);C=cross(v1,v2);W=norm(C)
        perimeter+=step*v
        if v.lo<=0 or W.lo<=0:
            unresolved+=1
            continue
        Cp=cross(v1,v3)
        determinant=dot(C,v3)
        determinant_p=dot(v1,cross(v2,v4))
        vp=dot(v1,v2)/v;Wp=dot(C,Cp)/W
        kappa=W/(v**3);tau=determinant/square(W);q=tau/kappa
        qphi=(determinant_p*(v**3)/(W**3)+3*determinant*square(v)*vp/(W**3)
              -3*determinant*(v**3)*Wp/(W**4))
        qell=qphi/v
        lambda0=kappa+square(tau)/kappa
        kmin=kappa.lo if kmin is None else min(kmin,kappa.lo)
        kmax=max(kmax,kappa.hi);taumax=max(taumax,tau.abs_upper())
        qmax=max(qmax,q.abs_upper());qlmax=max(qlmax,qell.abs_upper())
        lambda0_upper=max(lambda0_upper,lambda0.hi)
        lambda0_max_lower=max(lambda0_max_lower,lambda0.lo)
    return {'curvature_nonzero_certified':unresolved==0,'unresolved_cells':unresolved,
            'curvature_positive_lower':None if kmin is None else str(kmin),
            'curvature_upper':str(kmax),'torsion_absolute_upper':str(taumax),
            'q_absolute_upper':str(qmax),'q_arclength_derivative_absolute_upper':str(qlmax),
            'central_principal_curvature_upper':str(lambda0_upper),
            'central_max_principal_curvature_lower':str(lambda0_max_lower),
            'perimeter':perimeter.json(),'bounds_cover_whole_curve':unresolved==0,
            'frame_numeric_bounds_are_only_for_resolved_cells_when_unresolved_cells_positive':True}


def space_curve_jets(phi,a,b,h,mix=0.):
    phi=np.asarray(phi,float)
    s,c=np.sin(phi),np.cos(phi)
    r=[(1. if k==0 else 0.)+a*3**k*np.cos(3*phi+k*np.pi/2)
       +b*6**k*np.cos(6*phi+k*np.pi/2) for k in range(5)]
    z=[h*(3**k*np.sin(3*phi+k*np.pi/2)+mix*6**k*np.sin(6*phi+k*np.pi/2)) for k in range(5)]
    radial=[r[0],r[1],r[2]-r[0],r[3]-3*r[1],r[4]-6*r[2]+r[0]]
    angular=[np.zeros_like(phi),r[0],2*r[1],3*r[2]-r[0],4*r[3]-4*r[1]]
    return [np.stack((radial[k]*c-angular[k]*s,radial[k]*s+angular[k]*c,z[k]),axis=-1)
            for k in range(5)]


def frame(phi,a,b,h,mix=0.):
    x,v1,v2,v3,v4=space_curve_jets(phi,a,b,h,mix)
    speed=np.linalg.norm(v1,axis=-1)
    C=np.cross(v1,v2);W=np.linalg.norm(C,axis=-1)
    if np.any(speed<=0) or np.any(W<=1e-13):
        raise ValueError('Frenet frame is singular on the requested points')
    T=v1/speed[...,None];B=C/W[...,None];N=np.cross(B,T)
    determinant=np.sum(C*v3,axis=-1)
    determinant_p=np.sum(v1*np.cross(v2,v4),axis=-1)
    vp=np.sum(v1*v2,axis=-1)/speed
    Wp=np.sum(C*np.cross(v1,v3),axis=-1)/W
    kappa=W/speed**3;tau=determinant/W**2;q=tau/kappa
    qphi=(determinant_p*speed**3/W**3+3*determinant*speed**2*vp/W**3
          -3*determinant*speed**3*Wp/W**4)
    return {'x':x,'speed':speed,'T':T,'N':N,'B':B,'kappa':kappa,'tau':tau,
            'q':q,'q_phi':qphi,'q_ell':qphi/speed,
            'lambda0':kappa+tau*tau/kappa}


def speed_only(phi,a,b,h,mix=0.):
    r=1+a*np.cos(3*phi)+b*np.cos(6*phi)
    rp=-3*a*np.sin(3*phi)-6*b*np.sin(6*phi)
    zp=h*(3*np.cos(3*phi)+6*mix*np.cos(6*phi))
    return np.sqrt(r*r+rp*rp+zp*zp)


class SpaceStarFlatCore:
    """Numerical evaluator of the exact arclength-defined formula.

    evaluate(s,theta) broadcasts its arguments and returns the full position
    two-jet in (s,theta).  Numerical quadrature is reported as such; the exact
    metric identity refers to exact arclength in the mathematical definition.
    """
    def __init__(self,a=.6,b=.09,lift=.2,mix=0.,arc_cells=192,quadrature=12):
        self.a,self.b,self.lift=float(a),float(b),float(lift)
        self.mix=float(mix)
        self.arc_cells=int(arc_cells);self.quadrature=int(quadrature)
        self.gl,self.gw=np.polynomial.legendre.leggauss(quadrature)
        self.step=2*np.pi/arc_cells
        left=np.arange(arc_cells)*self.step
        points=left[:,None]+self.step*(self.gl[None,:]+1)/2
        speeds=speed_only(points,self.a,self.b,self.lift,self.mix)
        increments=self.step*(speeds@self.gw)/2
        self.arc_prefix=np.r_[0.,np.cumsum(increments)]
        self.perimeter=float(self.arc_prefix[-1]);self.a0=self.perimeter/(2*np.pi)
        self.q0=float(frame(np.array([0.]),self.a,self.b,self.lift,self.mix)['q'][0])

    def arclength(self,phi):
        phi=np.asarray(phi,float)
        turns=np.floor(phi/(2*np.pi))
        rem=phi-turns*2*np.pi
        index=np.minimum(np.floor(rem/self.step).astype(int),self.arc_cells-1)
        left=index*self.step;length=rem-left
        points=left[...,None]+length[...,None]*(self.gl+1)/2
        speed=speed_only(points,self.a,self.b,self.lift,self.mix)
        return turns*self.perimeter+self.arc_prefix[index]+length*(speed@self.gw)/2

    def internal_phi(self,s,theta):
        s,theta=np.broadcast_arrays(np.asarray(s,float),np.asarray(theta,float))
        target=s*self.q0+np.mod(self.a0*theta-s*self.q0,self.perimeter)
        lo=np.zeros_like(target);hi=np.full_like(target,2*np.pi)
        phi=2*np.pi*(target-s*self.q0)/self.perimeter
        for _ in range(50):
            f=frame(phi,self.a,self.b,self.lift,self.mix)
            residual=self.arclength(phi)+s*f['q']-target
            if np.max(abs(residual))<3e-15*max(1.,self.perimeter):
                break
            derivative=f['speed']+s*f['q_phi']
            if np.any(derivative<=0):
                raise ValueError('angular material map loses monotonicity')
            lo=np.where(residual<0,phi,lo);hi=np.where(residual>=0,phi,hi)
            proposed=phi-residual/derivative
            phi=np.where((proposed>lo)&(proposed<hi),proposed,(lo+hi)/2)
        final=frame(phi,self.a,self.b,self.lift,self.mix)
        error=np.max(abs(self.arclength(phi)+s*final['q']-target))
        if error>2e-11*max(1.,self.perimeter):
            raise RuntimeError('implicit arclength map did not converge')
        return phi,float(error)

    def evaluate(self,s,theta):
        s,theta=np.broadcast_arrays(np.asarray(s,float),np.asarray(theta,float))
        phi,error=self.internal_phi(s,theta)
        f=frame(phi,self.a,self.b,self.lift,self.mix)
        J=1+s*f['q_ell']
        if np.min(J)<=0:
            raise ValueError('J must be positive')
        N,T,B=f['N'],f['T'],f['B'];k,tau=f['kappa'],f['tau']
        X=f['x']+s[...,None]*(B+f['q'][...,None]*T)
        return {'x':X,'xs':B,'xu':self.a0*T,
                'xss':(tau*tau/(k*J))[...,None]*N,
                'xsu':(-self.a0*tau/J)[...,None]*N,
                'xuu':(self.a0*self.a0*k/J)[...,None]*N,
                'normal':N,'phi':phi,'J':J,'principal_curvature':f['lambda0']/J,
                'implicit_map_residual':error}


def sample_frame_summary(a,b,h,mix,n):
    phi=np.arange(n)*2*np.pi/n
    f=frame(phi,a,b,h,mix)
    peak=int(np.argmax(f['lambda0']))
    return {'points':n,'curvature_range':[float(np.min(f['kappa'])),float(np.max(f['kappa']))],
            'torsion_range':[float(np.min(f['tau'])),float(np.max(f['tau']))],
            'q_absolute_max':float(np.max(abs(f['q']))),
            'q_arclength_derivative_absolute_max':float(np.max(abs(f['q_ell']))),
            'central_principal_curvature_max':float(np.max(f['lambda0'])),
            'central_curvature_peak_phi':float(phi[peak]),'continuous_certificate':False}


def exact_extremum_curvature(a_text,b_text,h_text,mix,spec,valley=True):
    """Central principal curvature at a valley/tip, using rational data."""
    a,b,h=map(I,[a_text,b_text,h_text])
    if valley:
        r=1-a+b;c=10*a-37*b-1;third=28*a-109*b-1
        z1=h*(-3+6*mix);z3=h*(27-216*mix)
    else:
        r=1+a+b;c=-1-10*a-37*b;third=-1-28*a-109*b
        z1=h*(3+6*mix);z3=h*(-27-216*mix)
    if c.lo<=0<=c.hi:
        return None
    C=I(min(abs(c.lo),abs(c.hi)),c.abs_upper())
    determinant_factor=r*z3-third*z1
    exact_zero=(valley and spec=='valley-zero') or (not valley and spec=='tip-zero')
    if exact_zero:
        determinant_factor=I(0)
    denominator=square(r)+square(z1)
    kappa=C/denominator
    principal=(C+square(determinant_factor)/(C**3))/denominator
    return {'spatial_curvature':kappa.json(),'rectifying_principal_curvature':principal.json(),
            'formula':'lambda0=(abs(c)+(r*z3-third*z1)^2/abs(c)^3)/(r^2+z1^2)',
            'torsion_exactly_zero_by_parameter_formula':exact_zero,
            'exact_parameter_angle':'pi/3' if valley else '0'}


def numerical_jet_check(core,ql_sample):
    ds=min(1e-6,1e-3/(1+ql_sample));du=1e-6
    s=np.array([0.,ds*7,-ds*5,.0,.0])
    theta=np.array([.17,.51,1.27,2.31,5.09])
    z=core.evaluate(s,theta)
    ps=core.evaluate(s+ds,theta);ms=core.evaluate(s-ds,theta)
    pu=core.evaluate(s,theta+du);mu=core.evaluate(s,theta-du)
    checks={}
    for key,numeric in [('xs',(ps['x']-ms['x'])/(2*ds)),
                        ('xu',(pu['x']-mu['x'])/(2*du)),
                        ('xss',(ps['xs']-ms['xs'])/(2*ds)),
                        ('xsu',(pu['xs']-mu['xs'])/(2*du)),
                        ('xuu',(pu['xu']-mu['xu'])/(2*du))]:
        checks[key]=float(np.linalg.norm(numeric-z[key])/max(np.linalg.norm(z[key]),1e-30))
    reverse=core.evaluate(-s,-theta);A=np.array([1.,-1.,-1.])
    symmetry={k:float(np.max(abs(reverse[k]-sign*z[k]*A))) for k,sign in
              [('x',1),('xs',-1),('xu',-1),('xss',1),('xsu',1),('xuu',1)]}
    E=np.sum(z['xs']**2,axis=-1);F=np.sum(z['xs']*z['xu'],axis=-1)
    G=np.sum(z['xu']**2,axis=-1)/core.a0**2
    return {'position_and_jet_FD_relative_errors':checks,'halfturn_two_jet_errors':symmetry,
            'algebraic_EFG_error_max':float(max(np.max(abs(E-1)),np.max(abs(F)),np.max(abs(G-1)))),
            'implicit_map_residual_max':max(v['implicit_map_residual'] for v in [z,ps,ms,pu,mu,reverse]),
            'a0_from_numerical_arclength':core.a0,'numerical_arclength_certified':False}


def core_normal_chord_sample(core,w,angles=96):
    theta=np.arange(angles)*2*np.pi/angles
    z=core.evaluate(np.array([-w,0.,w])[:,None],theta[None,:])
    x=z['x'].reshape(-1,3);normal=z['normal'].reshape(-1,3)
    delta=x[None,:,:]-x[:,None,:]
    distance2=np.sum(delta*delta,axis=-1)
    denominator=2*np.abs(np.sum(delta*normal[:,None,:],axis=-1))
    valid=(distance2>1e-22)&(denominator>1e-18)
    ratios=np.full_like(distance2,np.inf);ratios[valid]=distance2[valid]/denominator[valid]
    pair=np.unravel_index(np.argmin(ratios),ratios.shape)
    return {'radial_values':[-w,0.,w],'angles':angles,
            'minimum_normal_chord_radius_sample':float(ratios[pair]),
            'sample_pair_indices':[int(x) for x in pair],
            'principal_curvature_max_sample':float(np.max(z['principal_curvature'])),
            'J_min_sample':float(np.min(z['J'])),
            'reach_lower_certificate':False,'embedding_certificate':False}


def analyze_lift(a,b,h_text,mix_spec,widths,cells,planar,samples):
    h=I(h_text)
    mix=resolve_mix(a,b,mix_spec)
    mix_numeric=float((mix.lo+mix.hi)/2)
    height=lift_height_bound(h,mix)
    bounds=continuous_frame_bounds(a,b,h_text,mix,cells)
    sample=sample_frame_summary(float(a),float(b),float(h.lo),mix_numeric,samples)
    core=SpaceStarFlatCore(float(a),float(b),float(h.lo),mix_numeric)
    d=I(planar['continuous_distance_q_to_filled_star_domain']['lower'])
    Dxy=I(planar['continuous_full_curve_diameter']['upper'])
    Dlower=I(planar['continuous_full_curve_diameter']['lower'])
    Q=I(bounds['q_arclength_derivative_absolute_upper'])
    L0=I(bounds['central_principal_curvature_upper'])
    lower=I(bounds['central_max_principal_curvature_lower'])
    rows=[]
    for w_text in widths:
        w=I(w_text);J=1-w*Q
        regular=bounds['curvature_nonzero_certified'] and J.lo>0
        Dcore=(square(Dxy+2*w)+square(2*(I(height.hi)+w))).sqrt()
        witness=I(max(D(0),(d-w).lo))
        row={'half_width':w_text,
             'continuous_material_map_J_lower':str(J.lo) if bounds['bounds_cover_whole_curve'] else None,
             'whole_core_immersion_and_angular_closure_certified':regular,
             'projection_padding_upper':w_text,'total_z_span_upper':(2*(I(height.hi)+w)).json(),
             'core_diameter_upper':str(Dcore.hi),
             'conditional_witness_distance_lower':str(witness.lo),
             'conditional_witness_over_D_core_lower':str((witness/I(Dcore.hi)).lo),
             'requires_same_projection_and_height_budget_for_all_future_caps':True,
             'embedding_proved':False,'reach_lower_proved':False}
        if regular:
            curvature=(L0/J).hi
            row['continuous_principal_curvature_upper']=str(curvature)
            row['local_curvature_radius_lower_not_reach']=str(DOWN.divide(D(1),curvature))
            row['curvature_ceiling_sufficient_for_003_Dcore_budget']=bool(
                (I(curvature)*I('.03')*I(Dcore.hi)).hi<=1)
            row['core_samples']=core_normal_chord_sample(core,float(w.lo))
        rows.append(row)
    necessary=None
    if bounds['curvature_nonzero_certified'] and lower.lo>0:
        necessary=str((I(1)/(lower*Dlower)).hi)
    valley=exact_extremum_curvature(a,b,h_text,mix,mix_spec,True)
    tip=exact_extremum_curvature(a,b,h_text,mix,mix_spec,False)
    valley_reach=None
    if valley is not None:
        valley_lower=I(valley['rectifying_principal_curvature']['lower'])
        valley_reach=(I(1)/(valley_lower*Dlower)).hi
    extrema=[v for v in [valley,tip] if v is not None]
    extremum_reach=None
    if extrema:
        known=max(D(v['rectifying_principal_curvature']['lower']) for v in extrema)
        extremum_reach=(I(1)/(I(known)*Dlower)).hi
    return {'lift':h_text,'lift_mix_spec':mix_spec,'lift_mix_enclosure':mix.json(),
            'actual_lift_absolute_height':height.json(),
            'continuous_frame_bounds':bounds,'frame_samples':sample,
            'exact_valley_geometry':valley,
            'exact_tip_geometry':tip,
            'necessary_reach_over_planar_D_upper_from_exact_valley':None if valley_reach is None else str(valley_reach),
            'ruled_out_for_reach_003_by_exact_valley_curvature':valley_reach is not None and valley_reach<D('.03'),
            'necessary_reach_over_planar_D_upper_from_exact_extrema':None if extremum_reach is None else str(extremum_reach),
            'ruled_out_for_reach_003_by_exact_extrema':extremum_reach is not None and extremum_reach<D('.03'),
            'necessary_reach_over_planar_D_upper_from_continuous_core_curvature_lower':necessary,
            'numeric_position_and_two_jet_check':numerical_jet_check(core,sample['q_arclength_derivative_absolute_max']),
            'width_candidates':rows,'formula_exact_with_exact_arclength':True,
            'numeric_quadrature_is_not_an_exact_arclength_certificate':True,
            'central_mixed_second_fundamental_coefficient':'W=-a0*tau, generally nonzero',
            'closed_surface_constructed':False,'task_complete':False}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--a',default='.6');p.add_argument('--b',default='.09')
    p.add_argument('--lifts',default='.04,.06,.08,.10,.12,.16,.20,.30')
    p.add_argument('--lift-mixes',default='0',help='decimals, valley-zero, tip-zero; comma-separated')
    p.add_argument('--widths',default='.01,.02,.04')
    p.add_argument('--nodes',type=int,default=2048)
    p.add_argument('--samples',type=int,default=1024)
    p.add_argument('--planar-report',type=Path,help='published star-core geometry JSON; reuse its matching continuous certificate')
    p.add_argument('--smoke-only',action='store_true')
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    lifts=[x.strip() for x in args.lifts.split(',')]
    mixes=[x.strip() for x in args.lift_mixes.split(',')]
    widths=[x.strip() for x in args.widths.split(',')]
    if any(D(h)<=0 for h in lifts) or any(D(w)<=0 for w in widths):
        p.error('lifts and widths must be positive')
    if args.smoke_only:
        if len(lifts)!=1 or len(widths)!=1 or len(mixes)!=1:
            p.error('local smoke is one lift, one mix and one width')
        args.nodes=min(args.nodes,32);args.samples=min(args.samples,64)
    elif os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        p.error('lift scans belong in the public repository Actions; use --smoke-only locally')
    if args.nodes<16 or args.samples<16:
        p.error('need at least 16 nodes and samples')
    started=time.monotonic();trig=unit_enclosures(args.nodes)
    planar_source=None
    if args.planar_report:
        published=json.loads(args.planar_report.read_text())
        if published.get('schema')!='star-core-continuous-geometry-v1' or published.get('status')!='public_actions_geometric_screen':
            raise ValueError('planar-report must be a published Actions geometry screen')
        found=[r for r in published['candidates'] if D(r['a'])==D(args.a) and D(r['b'])==D(args.b)]
        if len(found)!=1:
            raise ValueError('planar-report has no unique matching a,b candidate')
        planar=found[0]
        planar_source={'path':str(args.planar_report),
            'sha256':hashlib.sha256(args.planar_report.read_bytes()).hexdigest(),
            'nodes':published['definition']['nodes']}
    else:
        planar=planar_analyze(args.a,args.b,args.nodes,args.samples,trig)
    rows=[]
    for h in lifts:
        for mix in mixes:
            try:
                row=analyze_lift(args.a,args.b,h,mix,widths,trig[1],planar,args.samples)
            except (ValueError,ZeroDivisionError,RuntimeError,FloatingPointError) as exc:
                row={'lift':h,'lift_mix_spec':mix,'status':'geometric_evaluation_failed',
                     'reason':str(exc),'candidate_certified':False,'task_complete':False}
            rows.append(row)
            if 'frame_samples' in row:
                update={'lift':h,'mix':mix,'continuous_kappa_positive':row['continuous_frame_bounds']['curvature_nonzero_certified'],
                    'lambda0_sample':row['frame_samples']['central_principal_curvature_max'],
                    'q_ell_sample':row['frame_samples']['q_arclength_derivative_absolute_max']}
            else:
                update=row
            print(json.dumps({**update,'seconds':time.monotonic()-started}),flush=True)
    report={'schema':'space-star-rectifying-flat-core-v1',
        'status':'development_smoke_only' if args.smoke_only else 'public_actions_geometric_screen',
        'definition':{k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},
        'planar_star_certificate':planar,'planar_certificate_source':planar_source,
        'lifts':rows,'elapsed_seconds':time.monotonic()-started,
        'source_sha256':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in ['space_star_flat_core.py','star_core_geometry.py','folded_reference_geometry.py']},
        'claim':{'exact_local_formula_proved':True,'closed_embedded_surface':False,
                  'fixed_hold_amplitude_for_closed_surface_certified':False,
                  'reach_lower_certified':False,'task_complete':False}}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')


if __name__=='__main__':
    main()
