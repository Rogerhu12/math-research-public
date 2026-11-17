#!/usr/bin/env python3
"""Full-circle continuous geometry of the repaired finite m3 prefix.

Uses the already reviewed outward Hermite/Bernstein/IEEE-sum kernel. The m3
analytic center is enclosed by independently validated arclength inverse
brackets and second-order interval Taylor remainders. The complete common-cut
lift is added using full-angle coefficient bounds. No symmetry reduction,
sampled endpoint argument or isometry certificate is used.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
import argparse,gzip,hashlib,json,time
import numpy as np
import mpmath as mp
from scipy.interpolate import CubicSpline
from interval_geometry_kernel import *
from m3_interval_center import CoreLiftIntervals,add_center_correction,lift_weights

p=argparse.ArgumentParser(description=__doc__)
for k in ['data','checkpoint','prefix-audit','cut-bounds','out']:p.add_argument('--'+k,type=Path,required=True)
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
summary=dict(support_lower=np.inf,radius_upper=0.,area_lower=np.inf,curvature_psd_diag_lower=np.inf,
             curvature_psd_det_lower=np.inf,planar_radial_projection_lower=np.inf,azimuth_numerator_lower=np.inf)
failed=[];nfailed=0;count=0
for start in range(0,len(low),a.batch):
    sl=slice(start,start+a.batch);fields=[]
    for radial,angular in [(0,0),(1,0),(2,0),(0,1),(0,2),(1,1)]:
        c=(coeff[radial][0][:,sl],coeff[radial][1][:,sl])
        fields.append(stack([linear_field((c[0][k],c[1][k]),b)for k,b in zip(cuts,bases[angular])],-1))
    fields=add_center_correction(fields,low[sl],high[sl],data['lift_width'],center)
    # Full right-end correction. Reverse the radial variable, retaining the
    # (-1)^(endpoint-jet+radial-derivative) chain factors.
    elow=dn(end-high[sl]);ehigh=up(end-low[sl])
    weights=[lift_weights(elow,ehigh,report['cut_width'],j)for j in range(3)]
    for n,(radial,angular)in enumerate([(0,0),(1,0),(2,0),(0,1),(0,2),(1,1)]):
        correction=exact(np.zeros_like(fields[n][0]))
        for j in range(3):
            z=(-db[angular,j],db[angular,j]);w=(weights[radial][0][:,j,None,None],weights[radial][1][:,j,None,None])
            correction=add(correction,mul(scale(w,(-1)**(j+radial)),z))
        fields[n]=add(fields[n],correction)
    X,Xs,Xss,Xp,Xpp,Xsp=fields;normal=cross(Xp,Xs);area=sqrt(norm2(normal))
    assert all(np.all(np.isfinite(v))for field in fields for v in field)
    if np.any(area[0]<=0):raise ValueError('Area enclosure includes zero')
    support=div(dot(X,normal),area);radius=sqrt(norm2(X))
    xx=(X[0][...,0],X[1][...,0]);yy=(X[0][...,1],X[1][...,1])
    xp=(Xp[0][...,0],Xp[1][...,0]);yp=(Xp[0][...,1],Xp[1][...,1])
    azimuth=sub(mul(xx,yp),mul(yy,xp))
    projection=add(mul(xx,(cs[0][0][None,:],cs[1][0][None,:])),mul(yy,(ss[0][0][None,:],ss[1][0][None,:])))
    E,F,G=norm2(Xs),dot(Xs,Xp),norm2(Xp)
    L,M,NN=[div(dot(Z,normal),area)for Z in [Xss,Xsp,Xpp]]
    diag=np.full(area[0].shape,np.inf);det=np.full_like(diag,np.inf)
    for sign in [-1,1]:
        aa=add(scale(E,a.curvature),scale(L,sign));bb=add(scale(F,a.curvature),scale(M,sign));cc=add(scale(G,a.curvature),scale(NN,sign))
        diag=np.minimum(diag,np.minimum(aa[0],cc[0]));det=np.minimum(det,sub(mul(aa,cc),square(bb))[0])
    vals=dict(support_lower=float(support[0].min()),radius_upper=float(radius[1].max()),area_lower=float(area[0].min()),
        curvature_psd_diag_lower=float(diag.min()),curvature_psd_det_lower=float(det.min()),
        planar_radial_projection_lower=float(projection[0].min()),azimuth_numerator_lower=float(azimuth[0].min()))
    for k,v in vals.items():summary[k]=(max if k=='radius_upper'else min)(summary[k],v)
    bad=(support[0]<a.support)|(radius[1]>a.radius)|(diag<=0)|(det<=0)|(projection[0]<=0)|(azimuth[0]<=0)
    nfailed+=int(bad.sum());count+=bad.size
    for i,j in np.argwhere(bad)[:max(0,24-len(failed))]:
        failed.append(dict(s=[float(low[start+i]),float(high[start+i])],angle=int(j),support=float(support[0][i,j]),
            radius=float(radius[1][i,j]),diag=float(diag[i,j]),det=float(det[i,j])))
    if start%120==0:print(json.dumps({'event':'prefix_interval_batch','radial_done':start+len(bad),'radial_total':len(low),'boxes':count,'failed':nfailed}),flush=True)
out=dict(scope=__doc__,success=nfailed==0,inputs={str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest()for p in [a.data,a.checkpoint,a.prefix_audit,a.cut_bounds]},
    source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in [Path(__file__),Path(__file__).with_name('interval_geometry_kernel.py'),Path(__file__).with_name('m3_interval_center.py')]},
    full_angular_range='[0,2*pi]',symmetry_reduction_used=False,angular_boxes=N,radial_boxes=len(low),covered_radial=[float(low[0]),float(high[-1])],
    boxes=count,failed_boxes=nfailed,first_failures=failed,bounds=summary,center=center_record,
    thresholds=dict(curvature=a.curvature,support=a.support,radius=a.radius),isometry_certified=False,
    seconds=time.monotonic()-started)
a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ['inputs','source_sha256','first_failures']}),flush=True)
