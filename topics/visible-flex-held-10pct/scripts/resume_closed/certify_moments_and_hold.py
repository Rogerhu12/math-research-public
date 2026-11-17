#!/usr/bin/env python3
"""Interval volume-moment and horizontal-support bounds for the finite m3 map.

Uses the already reviewed outward Hermite/Bernstein/IEEE-sum kernel. The m3
analytic center is enclosed by independently validated arclength inverse
brackets and second-order interval Taylor remainders. The complete common-cut
lift is added using full-angle coefficient bounds. No symmetry reduction,
sampled endpoint argument or isometry certificate is used.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"finite_closure/m3_m8_closed_map"))
import argparse,gzip,hashlib,json,time
import numpy as np
import mpmath as mp
from scipy.interpolate import CubicSpline
from interval_geometry_kernel import *
from m3_interval_center import CoreLiftIntervals,add_center_correction,lift_weights

p=argparse.ArgumentParser(description=__doc__)
for k in ['data','checkpoint','prefix-audit','cut-bounds','tail-certificate','background-certificate','out']:p.add_argument('--'+k,type=Path,required=True)
p.add_argument('--angular',type=int,default=512);p.add_argument('--batch',type=int,default=12)
p.add_argument('--curvature',type=float,default=10);p.add_argument('--support',type=float,default=.7)
p.add_argument('--radius',type=float,default=1.17)
a=p.parse_args();started=time.monotonic()
raw=np.load(a.data);report=json.loads(a.prefix_audit.read_text());bounds=json.loads(a.cut_bounds.read_text())
cp=json.load(gzip.open(a.checkpoint,'rt'));pm=raw['planar_modes'];hm=raw['height_modes'];P=len(pm)
odd=np.sort(abs(pm));assert len(np.unique(odd))==len(odd)and odd[0]==1
index={int(k):j for j,k in enumerate(odd)};J=np.zeros((3,2*len(odd)+len(hm),len(raw['knots'])))
for j,k in enumerate(pm):
    i=index[abs(int(k))];J[:,i]=raw['jets'][:,j];J[:,len(odd)+i]=(1 if k>0 else-1)*raw['jets'][:,j]
J[:,2*len(odd):]=raw['jets'][:,P:]
end=float(cp['meridian_length']);f=CubicSpline(cp['chart']['knots'],cp['chart']['values'],bc_type=((1,0.),(1,cp['chart']['final_derivative'])))
warp=8*cp['warp_reference_q']
data=dict(knots=raw['knots'],jets=J,odd=odd,even=hm[1:],core_coefficients=raw['core_coefficients'],
    core_frequencies=raw['core_frequencies'],chart_E0=warp*float(f(0.)),chart_Epp=warp*float(f(0.,2))/end**2,
    lift_width=report['center_width'])
assert np.all(np.isfinite(J))and np.all(np.diff(data['knots'])>0)
assert np.any(data['knots']==data['lift_width'])and data['knots'][-1]==end
N=a.angular;mp.iv.dps=50
def trig_full(freq):
    co=np.empty((2,len(freq),N));si=np.empty_like(co)
    for j in range(N):
        lo=2*mp.iv.pi*j/N;hi=2*mp.iv.pi*(j+1)/N
        arg=mp.iv.mpf([lo.a,hi.b])
        for i,k in enumerate(freq):
            for z,v in [(co,mp.iv.cos(int(k)*arg)),(si,mp.iv.sin(int(k)*arg))]:
                z[0,i,j]=dn(float(v.a));z[1,i,j]=up(float(v.b))
    return (co[0],co[1]),(si[0],si[1])
center,center_record=CoreLiftIntervals(data,N).all_boxes()
cs,ss=trig_full(odd);ce,se=trig_full(hm[1:]);bases=[]
for j in range(3):
    if j==0:bx,by,bz=cs,ss,ce
    elif j==1:bx,by,bz=neg(ss),cs,neg(se)
    else:bx,by,bz=neg(cs),neg(ss),neg(ce)
    bx=scale(bx,odd[:,None]**j);by=scale(by,odd[:,None]**j);bz=scale(bz,hm[1:,None]**j)
    const=exact(np.ones((1,N))if j==0 else np.zeros((1,N)))
    bz=(np.concatenate([const[0],bz[0]]),np.concatenate([const[1],bz[1]]));bases.append([bx,by,bz])
coeff=[]
for j in range(3):
    z=hermite_bernstein(data['knots'],J,j);coeff.append((z[0].min(axis=0),z[1].max(axis=0)))
low,high=data['knots'][:-1],data['knots'][1:]
cuts=[slice(0,len(odd)),slice(len(odd),2*len(odd)),slice(2*len(odd),None)]
db=np.asarray(bounds['all_angle_delta_bounds_angular_then_radial_jet'])

from fractions import Fraction as Q

def iq(x):
    v=float(x);lo,hi=float(dn(v)),float(up(v))
    assert Q.from_float(lo)<=x<=Q.from_float(hi)
    return lo,hi

def rq(x):return Q(int(x['numerator']),int(x['denominator']))

def display(x):return dict(numerator=str(x.numerator),denominator=str(x.denominator),display_only=float(x))

bg=json.loads(a.background_certificate.read_text());tail=json.loads(a.tail_certificate.read_text())
zmax=Q.from_float(report['zcut_mean'])+rq(tail['finite_mean_at_cut_interval'][1])+Q(bg['exact_background_height']['upper_exact'])+Q.from_float(tail['complete_coefficient_bounds']['V'])
rxy=Q.from_float(.3)+Q.from_float(tail['complete_coefficient_bounds']['V'])
assert zmax<Q(102,125) and rxy<Q(301,1000)
mp.iv.dps=70
pi=(float(dn(float(mp.iv.pi.a))),float(up(float(mp.iv.pi.b))))
angle_width=div(scale(pi,2),exact(N))
rt3=sqrt(exact(3));directions=[(exact(1),exact(0)),(exact(.5),scale(rt3,-.5)),(scale(rt3,.5),exact(-.5))]
support_lo=np.full(3,-np.inf);support_hi=np.full(3,-np.inf)
whole=(0.,0.);volume=(0.,0.);boxes=0
for start in range(0,len(low),a.batch):
    sl=slice(start,start+a.batch);fields=[]
    for radial,angular in [(0,0),(1,0),(2,0),(0,1),(0,2),(1,1)]:
        c=(coeff[radial][0][:,sl],coeff[radial][1][:,sl])
        fields.append(stack([linear_field((c[0][k],c[1][k]),b)for k,b in zip(cuts,bases[angular])],-1))
    fields=add_center_correction(fields,low[sl],high[sl],data['lift_width'],center)
    elow=dn(end-high[sl]);ehigh=up(end-low[sl]);weights=[lift_weights(elow,ehigh,report['cut_width'],j)for j in range(3)]
    for n,(radial,angular)in enumerate([(0,0),(1,0),(2,0),(0,1),(0,2),(1,1)]):
        correction=exact(np.zeros_like(fields[n][0]))
        for j in range(3):
            z=(-db[angular,j],db[angular,j]);w=(weights[radial][0][:,j,None,None],weights[radial][1][:,j,None,None])
            correction=add(correction,mul(scale(w,(-1)**(j+radial)),z))
        fields[n]=add(fields[n],correction)
    X,Xs,_,Xp,_,_=fields
    axis=lambda field,j:(field[0][...,j],field[1][...,j])
    xx,yy,zz=[axis(X,j)for j in range(3)]
    nz=sub(mul(axis(Xp,0),axis(Xs,1)),mul(axis(Xp,1),axis(Xs,0)))
    density=scale(mul(sub(mul(zz,square(xx)),div(mul(zz,square(zz)),exact(3))),nz),2)
    vden=scale(mul(zz,nz),2)
    width=sub(exact(high[sl]),exact(low[sl]));weight=mul((width[0][:,None],width[1][:,None]),angle_width)
    integral=mul(density,weight);vint=mul(vden,weight)
    whole=add(whole,interval_sum_terms((integral[0].ravel(),integral[1].ravel()),0))
    volume=add(volume,interval_sum_terms((vint[0].ravel(),vint[1].ravel()),0))
    for j,(dx,dy)in enumerate(directions):
        v=add(mul(xx,dx),mul(yy,dy));support_lo[j]=max(support_lo[j],float(v[0].max()));support_hi[j]=max(support_hi[j],float(v[1].max()))
    boxes+=density[0].size
    if start%120==0:print(json.dumps({'event':'moment_interval_batch','radial_done':start+len(low[sl]),'radial_total':len(low),'boxes':boxes,'prefix_moment_interval':[float(whole[0]),float(whole[1])]}),flush=True)
# Tail/collar/disk is an upward graph over a planar domain inside r_xy<.301.
# Its volume-moment integrand is 2*z*x^2-(2/3)*z^3, and dA_xy is positive.
# The following lower bound discards the nonnegative first term.
pi_hi=Q.from_float(float(pi[1]));cap_moment_abs=(Q(2,3)*zmax**3*pi_hi*rxy**2)
base_gap=Q.from_float(float(whole[0]))-cap_moment_abs
# Fixed twofold markers with epsilon=eta=1/2 and r_c=a_cuff<=.05.
ac=Q.from_float(float(.3-.25));eps=Q(1,2);eta=Q(1,2)
fmax=Q(27,256)*eps*(1+eta)*ac**2
marker_zz=2*pi_hi*ac**2*fmax*(zmax+fmax)**2
marked_gap=base_gap-marker_zz
qxy=Q.from_float(float(pi[0]))*eps*eta*ac**6/60
assert all(x>rxy for x in map(Q.from_float,support_lo))
held=[max(0.,float(dn(support_lo[0]-support_hi[j])),float(dn(support_lo[j]-support_hi[0])))for j in [1,2]]
out=dict(scope=__doc__,success=base_gap>0 and marked_gap>0,
    inputs={str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest()for p in [a.data,a.checkpoint,a.prefix_audit,a.cut_bounds,a.tail_certificate,a.background_certificate]},
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),boxes=boxes,
    prefix_volume_flux_interval=[float(volume[0]),float(volume[1])],
    prefix_axial_second_moment_difference_interval=[float(whole[0]),float(whole[1])],
    tail_collar_disk_moment_lower=display(-cap_moment_abs),
    baseline_Qxx_minus_Qzz_lower=display(base_gap),
    marker_parameters=dict(epsilon=.5,eta=.5,radius=float(ac)),
    marker_added_Qzz_upper=display(marker_zz),marked_Qyy_minus_Qzz_lower=display(marked_gap),
    marked_Qxx_minus_Qyy_lower=display(qxy),
    horizontal_support_directions=['angle 0','angle -pi/3','angle -pi/6'],
    horizontal_support_intervals=list(map(list,zip(support_lo.tolist(),support_hi.tolist()))),
    held_support_difference_lower_pi3_pi6=held,
    scope_limits=['C2 embedding/graph/height premises are the separate full geometry certificate.',
        'No lower bound for optimized rigid-motion Hausdorff distance is computed here.',
        'Strict noncongruence follows from the moment eigenspaces and the analytic core, as proved separately.'],
    seconds=time.monotonic()-started)
a.out.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k]for k in ['success','prefix_axial_second_moment_difference_interval','baseline_Qxx_minus_Qzz_lower','marked_Qyy_minus_Qzz_lower','horizontal_support_intervals','held_support_difference_lower_pi3_pi6','seconds']}),flush=True)
