#!/usr/bin/env python3
"""Continuous planar geometry bounds for three-lobed radial core curves.

gamma(phi)=(1+a*cos(3phi)+b*cos(6phi))*(cos(phi),sin(phi)).
Decimal trigonometric enclosures and an explicit second-derivative bound
control the entire continuous curve, not just its vertices.  A rotating tip
witness is tested against the filled radial domain.  Normal-chord values are
samples and are never a reach lower certificate.  Parameter scans run only
in this public repository's Actions; local --smoke-only is a tiny check.
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

from folded_reference_geometry import I, PI, UP, DOWN, sincos


def square(x):
    if x.lo <= 0 <= x.hi:
        return I(0, UP.multiply(x.abs_upper(),x.abs_upper()))
    return x*x


def clipped(x, lo=-1, hi=1):
    return I(max(x.lo,D(str(lo))),min(x.hi,D(str(hi))))


def magnitude_lower(x):
    return D(0) if x.lo <= 0 <= x.hi else min(abs(x.lo),abs(x.hi))


def down(x):
    return np.nextafter(x,-np.inf)


def up(x):
    return np.nextafter(x,np.inf)


class F:
    """Binary64 outward intervals; each elementary operation is widened.

    This uses the IEEE-754 correctly rounded elementary +,-,*,/,sqrt model;
    no machine-libm trigonometric assumption enters the continuous bounds.
    """
    def __init__(self,lo,hi=None):
        self.lo=np.asarray(lo,dtype=float)
        self.hi=self.lo if hi is None else np.asarray(hi,dtype=float)
    def __add__(self,other):
        other=other if isinstance(other,F) else F(other)
        return F(down(self.lo+other.lo),up(self.hi+other.hi))
    def __sub__(self,other):
        other=other if isinstance(other,F) else F(other)
        return F(down(self.lo-other.hi),up(self.hi-other.lo))
    def __mul__(self,other):
        other=other if isinstance(other,F) else F(other)
        ends=np.stack([self.lo*other.lo,self.lo*other.hi,
                       self.hi*other.lo,self.hi*other.hi])
        return F(np.min(down(ends),axis=0),np.max(up(ends),axis=0))
    def __truediv__(self,other):
        other=other if isinstance(other,F) else F(other)
        if np.any(other.lo<=0):
            raise ValueError('this quotient requires a positive denominator')
        return self*F(down(1/other.hi),up(1/other.lo))
    def square(self):
        low=np.minimum(self.lo*self.lo,self.hi*self.hi)
        low=np.where((self.lo<=0)&(self.hi>=0),0.,np.maximum(0.,down(low)))
        high=up(np.maximum(self.lo*self.lo,self.hi*self.hi))
        return F(low,high)
    def sqrt(self):
        if np.any(self.lo<0):
            raise ValueError('negative interval square root')
        return F(np.maximum(0.,down(np.sqrt(self.lo))),up(np.sqrt(self.hi)))
    def clamp01(self):
        return F(np.clip(self.lo,0.,1.),np.clip(self.hi,0.,1.))


def dot2(x,y):
    return x[0]*y[0]+x[1]*y[1]


def norm2(x):
    total=x[0].square()+x[1].square()
    return F(np.maximum(total.lo,0.),total.hi).sqrt()


def polygon_distance(point,vertices):
    """Distance interval for exact binary64 point and polygon vertices."""
    nxt=np.roll(vertices,-1,axis=0)
    a=[F(vertices[:,j]) for j in range(2)]
    v=[F(nxt[:,j])-a[j] for j in range(2)]
    w=[F(point[j])-a[j] for j in range(2)]
    vv=dot2(v,v)
    t=(dot2(w,v)/vv).clamp01()
    error=[w[j]-t*v[j] for j in range(2)]
    distance=norm2(error)
    return I(D.from_float(float(np.min(distance.lo))),
             D.from_float(float(np.min(distance.hi))))


def polygon_diameter(vertices,block=128):
    """All pairs, with outward bounds; no unverified farthest-pair shortcut."""
    lower,upper=0.,0.
    for start in range(0,len(vertices),block):
        stop=min(start+block,len(vertices))
        delta=[F(vertices[start:stop,j,None])-F(vertices[None,:,j]) for j in range(2)]
        distance=norm2(delta)
        lower=max(lower,float(np.max(distance.lo)))
        upper=max(upper,float(np.max(distance.hi)))
    return I(D.from_float(lower),D.from_float(upper))


def unit_enclosures(nodes):
    """Exact-parameter vertex and whole-cell sin/cos enclosures, cached once."""
    angles=[2*PI*i/nodes for i in range(nodes+1)]
    vertices=[sincos(angle) for angle in angles[:-1]]
    # Periodicity makes the final exact unit point (0,1).
    endpoints=vertices+[(I(0),I(1))]
    cells=[]
    for i in range(nodes):
        ss=I(min(endpoints[i][0].lo,endpoints[i+1][0].lo),
             max(endpoints[i][0].hi,endpoints[i+1][0].hi))
        cc=I(min(endpoints[i][1].lo,endpoints[i+1][1].lo),
             max(endpoints[i][1].hi,endpoints[i+1][1].hi))
        for k in range(5):
            critical=PI*k/2
            if angles[i].lo<=critical.hi and angles[i+1].hi>=critical.lo:
                if k%4==1: ss.hi=max(ss.hi,D(1))
                if k%4==3: ss.lo=min(ss.lo,D(-1))
                if k%4==0: cc.hi=max(cc.hi,D(1))
                if k%4==2: cc.lo=min(cc.lo,D(-1))
        cells.append((clipped(ss),clipped(cc)))
    return vertices,cells


def radial_range(a,b):
    values=[1+a+b,1-a+b]
    if b.lo!=0 and abs(a.lo)<=4*abs(b.lo):
        values.append(1-b-square(a)/(8*b))
    return I(min(v.lo for v in values),max(v.hi for v in values))


def polar_intervals(s,c,a,b):
    c3=clipped(4*c*c*c-3*c)
    s3=clipped(3*s-4*s*s*s)
    c6=clipped(2*square(c3)-1)
    s6=clipped(2*s3*c3)
    r=1+a*c3+b*c6
    rp=-3*a*s3-6*b*s6
    rpp=-9*a*c3-36*b*c6
    return r,rp,rpp


def midpoint_with_error(x,y):
    fx=float((x.lo+x.hi)/2)
    fy=float((y.lo+y.hi)/2)
    ex=(x-I(D.from_float(fx))).abs_upper()
    ey=(y-I(D.from_float(fy))).abs_upper()
    error=(square(I(ex))+square(I(ey))).sqrt().hi
    return np.array([fx,fy]),error


def curve(phi,a,b):
    co,si=np.cos(phi),np.sin(phi)
    r=1+a*np.cos(3*phi)+b*np.cos(6*phi)
    rp=-3*a*np.sin(3*phi)-6*b*np.sin(6*phi)
    rpp=-9*a*np.cos(3*phi)-36*b*np.cos(6*phi)
    x=np.stack((r*co,r*si),axis=-1)
    xp=np.stack((rp*co-r*si,rp*si+r*co),axis=-1)
    xpp=np.stack(((rpp-r)*co-2*rp*si,(rpp-r)*si+2*rp*co),axis=-1)
    speed=np.sqrt(r*r+rp*rp)
    kappa=(r*r+2*rp*rp-r*rpp)/speed**3
    return x,xp,xpp,kappa


def normal_chord_samples(a,b,n):
    phi=np.arange(n)*2*np.pi/n
    x,xp,_,kappa=curve(phi,a,b)
    normal=np.stack((-xp[:,1],xp[:,0]),axis=-1)/np.linalg.norm(xp,axis=1)[:,None]
    best=np.inf;where=None
    for start in range(0,n,128):
        stop=min(start+128,n)
        delta=x[None,:,:]-x[start:stop,None,:]
        distance2=np.sum(delta*delta,axis=-1)
        denominator=2*np.abs(np.sum(delta*normal[start:stop,None,:],axis=-1))
        valid=(distance2>1e-24)&(denominator>1e-18)
        ratio=np.full_like(distance2,np.inf)
        ratio[valid]=distance2[valid]/denominator[valid]
        index=np.unravel_index(np.argmin(ratio),ratio.shape)
        if ratio[index]<best:
            best=float(ratio[index]);where=(start+index[0],index[1])
    i,j=where
    return {'angles':n,'maximum_absolute_curvature_sample':float(np.max(abs(kappa))),
            'signed_curvature_sample_range':[float(np.min(kappa)),float(np.max(kappa))],
            'minimum_normal_chord_radius_sample':best,
            'normal_chord_pair_indices':[int(i),int(j)],
            'normal_chord_pair_phi':[float(phi[i]),float(phi[j])],
            'pair_cyclic_grid_separation':int(min((i-j)%n,(j-i)%n)),
            'reach_lower_bound':False,
            'normal_chords_only_give_necessary_upper_obstructions':True,
            'continuous_or_roundoff_validated_sample':False}


def analyze(a_text,b_text,nodes,chord_samples,trig):
    a,b=I(a_text),I(b_text)
    if a.lo<=0:
        raise ValueError('the chosen outward rotated-tip witness requires a>0')
    radial=radial_range(a,b)
    if radial.lo<=0:
        raise ValueError('radial curve must remain strictly positive')
    vertex_trig,cell_trig=trig
    points=[];vertex_error=D(0)
    for s,c in vertex_trig:
        r,_,_=polar_intervals(s,c,a,b)
        r=I(max(r.lo,radial.lo),min(r.hi,radial.hi))
        point,error=midpoint_with_error(r*c,r*s)
        points.append(point);vertex_error=max(vertex_error,error)
    points=np.asarray(points)
    radius_tip=1+a+b
    radius_valley=1-a+b
    q,q_error=midpoint_with_error(radius_tip/2,radius_tip*I(3).sqrt()/2)
    abs_a,abs_b=a.abs_upper(),b.abs_upper()
    M2=(square(1+10*I(abs_a)+37*I(abs_b))+
        4*square(3*I(abs_a)+6*I(abs_b))).sqrt()
    step=2*PI/nodes
    chord_error=(M2*square(step)/8).hi
    poly_distance=polygon_distance(q,points)
    distance_error=UP.add(chord_error,UP.add(vertex_error,q_error))
    distance=I(max(D(0),DOWN.subtract(poly_distance.lo,distance_error)),
               UP.add(poly_distance.hi,distance_error))
    pd=polygon_diameter(points)
    diameter=I(max(D(0),DOWN.subtract(pd.lo,UP.multiply(D(2),vertex_error))),
               UP.add(pd.hi,UP.multiply(D(2),UP.add(vertex_error,chord_error))))
    curvature_upper=D(0);perimeter=I(0)
    for s,c in cell_trig:
        r,rp,rpp=polar_intervals(s,c,a,b)
        r=I(max(r.lo,radial.lo),min(r.hi,radial.hi))
        speed2=square(r)+square(rp)
        numerator=square(r)+2*square(rp)-r*rpp
        denominator=speed2*speed2.sqrt()
        upper=UP.divide(numerator.abs_upper(),denominator.lo)
        curvature_upper=max(curvature_upper,upper)
        perimeter+=step*speed2.sqrt()
    ktip=(1+10*a+37*b)/square(radius_tip)
    kvalley=(1-10*a+37*b)/square(radius_valley)
    known_curvature_lower=max(magnitude_lower(ktip),magnitude_lower(kvalley))
    amplitude_ratio=distance/diameter
    diameter_budget=I(distance.lo)/I('.3')
    zbudget2=square(I(diameter_budget.lo))-square(I(diameter.hi))
    zbudget=(I(max(D(0),zbudget2.lo)).sqrt().lo if zbudget2.lo>0 else D(0))
    necessary_reach_ratio_upper=(I(1)/(I(known_curvature_lower)*I(diameter.lo))).hi
    return {
        'a':a_text,'b':b_text,'radial_range':radial.json(),
        'curve_is_simple_regular_radial_graph':True,
        'tip_radius':radius_tip.json(),'valley_radius':radius_valley.json(),
        'rotation_angle':'pi/3','rotated_tip_q_enclosure':{
            'x':(radius_tip/2).json(),'y':(radius_tip*I(3).sqrt()/2).json()},
        'q_outside_filled_domain_proved_by_radial_gap':(2*a).json(),
        'continuous_distance_q_to_filled_star_domain':distance.json(),
        'continuous_full_curve_diameter':diameter.json(),
        'continuous_witness_distance_over_planar_diameter':amplitude_ratio.json(),
        'planar_ratio_lower_at_least_03':amplitude_ratio.lo>=D('.3'),
        'continuous_absolute_curvature_upper':str(curvature_upper),
        'exact_tip_signed_curvature':ktip.json(),'exact_valley_signed_curvature':kvalley.json(),
        'nonconvexity_certified_at_valley':kvalley.hi<0,
        'local_curvature_radius_lower_not_global_reach':str(DOWN.divide(D(1),curvature_upper)),
        'necessary_reach_over_planar_D_upper_for_vertical_cylinder_from_known_curvature':str(necessary_reach_ratio_upper),
        'continuous_perimeter':perimeter.json(),'continuous_mean_radius':(perimeter/(2*PI)).json(),
        'conditional_full_surface_diameter_budget_for_03_witness':diameter_budget.json(),
        'sufficient_total_z_span_budget_if_all_projection_stays_in_domain':str(max(D(0),zbudget)),
        'filled_domain_contains_coaxial_disk_radius':str(radial.lo),
        'subdivision_certificate':{'segments':nodes,'gamma_second_derivative_upper':M2.json(),
            'curve_to_exact_chords_Hausdorff_upper':str(chord_error),
            'vertex_midpoint_radius_error_upper':str(vertex_error),
            'q_midpoint_radius_error_upper':str(q_error),
            'distance_to_binary64_polygon':poly_distance.json(),
            'binary64_polygon_all_pairs_diameter':pd.json()},
        'samples':normal_chord_samples(float(a.lo),float(b.lo),chord_samples),
        'scope':{'continuous_bounds_apply_to':'the stated planar curve and its filled radial domain',
            'transition_projection_containment_proved':False,
            'fixed_metric_connector_obtained':False,'closed_surface_obtained':False,
            'held_amplitude_for_a_closed_surface_certified':False,'reach_lower_certified':False,
            'task_complete':False}}


def derivative_check(a,b):
    phi=np.array([.13,.51,1.17,2.21,4.37])
    x,xp,xpp,k=curve(phi,a,b)
    eps=1e-6
    plus=curve(phi+eps,a,b);minus=curve(phi-eps,a,b)
    first=(plus[0]-minus[0])/(2*eps)
    second=(plus[1]-minus[1])/(2*eps)
    direct=(xp[:,0]*xpp[:,1]-xp[:,1]*xpp[:,0])/np.linalg.norm(xp,axis=-1)**3
    return {'first_derivative_relative_error':float(np.linalg.norm(first-xp)/np.linalg.norm(xp)),
            'second_derivative_relative_error':float(np.linalg.norm(second-xpp)/np.linalg.norm(xpp)),
            'curvature_formula_max_difference':float(np.max(abs(k-direct)))}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--a',default='.6',help='comma-separated exact decimal amplitudes')
    p.add_argument('--b',default='.09',help='comma-separated exact decimal amplitudes')
    p.add_argument('--nodes',type=int,default=4096)
    p.add_argument('--chord-samples',type=int,default=1024)
    p.add_argument('--check-derivatives',action='store_true')
    p.add_argument('--smoke-only',action='store_true')
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    aa=[x.strip() for x in args.a.split(',')];bb=[x.strip() for x in args.b.split(',')]
    if args.nodes<16 or args.chord_samples<16:
        p.error('need at least 16 curve and chord samples')
    if args.smoke_only:
        if len(aa)*len(bb)!=1:
            p.error('local smoke is one parameter pair, not a scan')
        args.nodes=min(args.nodes,32);args.chord_samples=min(args.chord_samples,32)
    elif os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        p.error('geometry scans belong in the public repository Actions; --smoke-only is a tiny local check')
    started=time.monotonic()
    trig=unit_enclosures(args.nodes)
    rows=[]
    for a in aa:
        for b in bb:
            row=analyze(a,b,args.nodes,args.chord_samples,trig)
            if args.check_derivatives:
                row['development_derivative_check']=derivative_check(float(a),float(b))
            rows.append(row)
            print(json.dumps({'a':a,'b':b,'distance':row['continuous_distance_q_to_filled_star_domain'],
                              'D':row['continuous_full_curve_diameter'],
                              'ratio':row['continuous_witness_distance_over_planar_diameter'],
                              'seconds':time.monotonic()-started}),flush=True)
    report={'schema':'star-core-continuous-geometry-v1',
        'status':'development_smoke_only' if args.smoke_only else 'public_actions_geometric_screen',
        'definition':{k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},
        'continuous_bound_arithmetic':'50-digit directed Decimal trigonometry; outward IEEE-754 binary64 elementary vector operations',
        'curve_segment_error_theorem':'sup ||gamma-linear_chord|| <= sup ||gamma_second_derivative|| * parameter_step^2 / 8',
        'normal_chord_samples_are_not_reach_lower_bounds':True,
        'nonconvex_cylindrical_core_cannot_be_assumed_to_enter_positive_K_inward_band':True,
        'candidates':rows,'elapsed_seconds':time.monotonic()-started,
        'source_sha256':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                         for name in ['star_core_geometry.py','folded_reference_geometry.py']},
        'claim':{'closed_embedded_isometric_family':False,'reach_lower_certified':False,'task_complete':False}}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')


if __name__=='__main__':
    main()
