#!/usr/bin/env python3
"""Outward interval geometry audit of the explicit Cartesian tensor prefix.

The input binary64 shared knot jets define exact quintic Hermite functions.
Without --include-center the analytic center lift is explicitly excluded.
With that option its full interval Taylor enclosure is included. Every point
in every radial/angular box is enclosed. No sampled Frenet root or third
derivative is used. Even a successful full-prefix check does not certify a
closing tail or exact isometry.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse,hashlib,json,math,time
from pathlib import Path
import numpy as np
import mpmath as mp

DOWN=-np.inf;UP=np.inf
def dn(x):return np.nextafter(np.asarray(x,dtype=float),DOWN)
def up(x):return np.nextafter(np.asarray(x,dtype=float),UP)
def exact(x):
    x=np.asarray(x,dtype=float);return x,x
def add(a,b):return dn(a[0]+b[0]),up(a[1]+b[1])
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    p=[a[i]*b[j]for i in range(2)for j in range(2)]
    return dn(np.minimum.reduce(p)),up(np.maximum.reduce(p))
def scale(a,b):return mul(a,exact(b))
def div(a,b):
    if np.any(b[0]<=0):raise ValueError('Positive interval denominator required')
    return mul(a,(dn(1/b[1]),up(1/b[0])))
def square(a):
    lo=np.where((a[0]<=0)&(a[1]>=0),0,np.minimum(a[0]*a[0],a[1]*a[1]))
    return np.maximum(0,dn(lo)),up(np.maximum(a[0]*a[0],a[1]*a[1]))
def sqrt(a):
    if np.any(a[0]<0):raise ValueError('Negative square-root interval')
    return np.maximum(0,dn(np.sqrt(a[0]))),up(np.sqrt(a[1]))
def take(a,i):return a[0][i],a[1][i]
def stack(xs,axis=0):return np.stack([x[0]for x in xs],axis),np.stack([x[1]for x in xs],axis)
def ratio(n,d):
    x=float(n)/float(d);return dn(x),up(x)

def hermite_bernstein(knots,jets,derivative):
    h=sub(exact(knots[1:]),exact(knots[:-1]));h=(h[0][None,:],h[1][None,:])
    y,d,q=[exact(jets[j])for j in range(3)]
    left=lambda a:(a[0][:,:-1],a[1][:,:-1])
    right=lambda a:(a[0][:,1:],a[1][:,1:])
    h2=square(h)
    e0=sub(sub(sub(right(y),left(y)),mul(h,left(d))),scale(mul(h2,left(q)),.5))
    e1=sub(sub(right(d),left(d)),mul(h,left(q)))
    e2=sub(right(q),left(q))
    c=[left(y),mul(h,left(d)),scale(mul(h2,left(q)),.5),
       add(sub(scale(e0,10),scale(mul(h,e1),4)),scale(mul(h2,e2),.5)),
       sub(add(scale(e0,-15),scale(mul(h,e1),7)),mul(h2,e2)),
       add(sub(scale(e0,6),scale(mul(h,e1),3)),scale(mul(h2,e2),.5))]
    if derivative:
        c=[scale(c[j],math.factorial(j)//math.factorial(j-derivative))for j in range(derivative,6)]
        denom=h if derivative==1 else h2
        c=[div(z,denom)for z in c]
    n=len(c)-1;bs=[]
    for k in range(n+1):
        v=exact(np.zeros_like(c[0][0]))
        for j in range(k+1):v=add(v,mul(c[j],ratio(math.comb(k,j),math.comb(n,j))))
        bs.append(v)
    return stack(bs)

def split_all(B):
    rows=[take(B,j)for j in range(B[0].shape[0])]
    left=[rows[0]];right=[rows[-1]]
    while len(rows)>1:
        rows=[scale(add(x,y),.5)for x,y in zip(rows[:-1],rows[1:])]
        left.append(rows[0]);right.append(rows[-1])
    l=stack(left);r=stack(right[::-1])
    return np.concatenate((l[0],r[0]),axis=2),np.concatenate((l[1],r[1]),axis=2)

def trig_intervals(freq,N):
    mp.iv.dps=50;co=np.empty((2,len(freq),N));si=np.empty_like(co)
    for j in range(N):
        lo=mp.iv.pi*j/(2*N);hi=mp.iv.pi*(j+1)/(2*N)
        interval=mp.iv.mpf([lo.a,hi.b])
        for i,k in enumerate(freq):
            for target,value in [(co,mp.iv.cos(int(k)*interval)),(si,mp.iv.sin(int(k)*interval))]:
                target[0,i,j]=dn(float(value.a));target[1,i,j]=up(float(value.b))
    return (co[0],co[1]),(si[0],si[1])

def interval_sum_terms(a,axis):
    """Order-independent IEEE binary64 summation enclosure, including padding.

    Every term has already been outward rounded. With n terms, 2*n*u exceeds
    gamma_(n-1). A second such factor covers summation of absolute magnitudes.
    """
    n=a[0].shape[axis];gamma=2*n*2.**-53
    if gamma>=.01:raise ValueError('Unexpectedly large summation')
    magnitude=np.maximum(abs(a[0]),abs(a[1]))
    total=up(np.sum(magnitude,axis=axis)/(1-gamma))
    error=up(gamma*total+n*np.nextafter(0.,1.))
    return dn(np.sum(a[0],axis=axis)-error),up(np.sum(a[1],axis=axis)+error)

def linear_field(coeff,basis):
    # coeff[state, radial], basis[state, angular]
    a=(coeff[0].T[:,:,None],coeff[1].T[:,:,None])
    b=(basis[0][None,:,:],basis[1][None,:,:])
    return interval_sum_terms(mul(a,b),1)

def dot(a,b):
    z=exact(np.zeros(a[0].shape[:-1]))
    for j in range(3):z=add(z,mul((a[0][...,j],a[1][...,j]),(b[0][...,j],b[1][...,j])))
    return z
def norm2(a):
    z=exact(np.zeros(a[0].shape[:-1]))
    for j in range(3):z=add(z,square((a[0][...,j],a[1][...,j])))
    return np.maximum(0,z[0]),z[1]
def cross(a,b):
    out=[]
    for i,j in [(1,2),(2,0),(0,1)]:
        out.append(sub(mul((a[0][...,i],a[1][...,i]),(b[0][...,j],b[1][...,j])),
                       mul((a[0][...,j],a[1][...,j]),(b[0][...,i],b[1][...,i]))))
    return stack(out,-1)

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--data',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--angular-quadrant',type=int,default=512)
    p.add_argument('--radial-bisections',type=int,choices=[0],default=0);p.add_argument('--batch',type=int,default=16)
    p.add_argument('--include-center',action='store_true')
    p.add_argument('--curvature',type=float,default=8);p.add_argument('--support',type=float,default=.3)
    p.add_argument('--diameter',type=float,default=3.031);p.add_argument('--witness',type=float,default=.317)
    a=p.parse_args();beg=time.monotonic();data=np.load(a.data);knots=data['knots'];jets=data['jets']
    odd=data['odd'];even=data['even'];nodd=len(odd);iz=2*nodd;N=a.angular_quadrant
    assert np.all(np.isfinite(knots)) and np.all(np.diff(knots)>0)
    assert np.all(np.isfinite(jets)) and jets.shape==(3,2*nodd+len(even)+1,len(knots))
    assert np.array_equal(odd,np.arange(1,2*nodd,2))
    assert np.array_equal(even,2*np.arange(1,len(even)+1))
    assert np.array_equal(data['core_frequencies'],even)
    assert N>0 and a.batch>0
    coeff=[hermite_bernstein(knots,jets,j)for j in range(3)]
    low=knots[:-1].copy();high=knots[1:].copy()
    for level in range(a.radial_bisections):
        coeff=[split_all(x)for x in coeff];mid=(low+high)/2
        low,high=np.r_[low,mid],np.r_[mid,high]
    assert np.any(knots==float(data['lift_width']))
    keep=np.ones(len(low),dtype=bool)if a.include_center else low>=float(data['lift_width'])
    low=low[keep];high=high[keep]
    coeff=[(x[0][:,:,keep].min(axis=0),x[1][:,:,keep].max(axis=0))for x in coeff]
    center_delta=None;center_diagnostics=None
    if a.include_center:
        from tensor_interval_center import CoreLiftIntervals,add_center_correction
        center_delta,center_diagnostics=CoreLiftIntervals(data,N).all_boxes()
    cs,ss=trig_intervals(odd,N);ce,se=trig_intervals(even,N)
    bases=[]
    for j in range(3):
        if j==0:bx,by,bz=cs,ss,ce
        elif j==1:bx,by,bz=neg(ss),cs,neg(se)
        else:bx,by,bz=neg(cs),neg(ss),neg(ce)
        bx=scale(bx,odd[:,None]**j);by=scale(by,odd[:,None]**j);bz=scale(bz,even[:,None]**j)
        const=exact(np.ones((1,N))if j==0 else np.zeros((1,N)))
        bz=(np.concatenate((const[0],bz[0])),np.concatenate((const[1],bz[1])))
        bases.append([bx,by,bz])
    cuts=[slice(0,nodd),slice(nodd,iz),slice(iz,None)]
    p0=exact(1.)
    for value in data['core_coefficients']:p0=add(p0,exact(value))
    assert np.all(np.isfinite(data['core_coefficients'])) and p0[0]>0
    summary={'support_lower':np.inf,'radius_upper':0.,'witness_lower':np.inf,
             'area_lower':np.inf,'curvature_psd_diagonal_lower':np.inf,'curvature_psd_det_lower':np.inf}
    summary.update(planar_radial_projection_lower=np.inf,azimuth_numerator_lower=np.inf)
    failed=[];total_failed=0;checked=0
    for start in range(0,len(low),a.batch):
        sl=slice(start,start+a.batch);fields=[]
        for radial,angular in [(0,0),(1,0),(2,0),(0,1),(0,2),(1,1)]:
            cr=(coeff[radial][0][:,sl],coeff[radial][1][:,sl]);parts=[]
            for cut,B in zip(cuts,bases[angular]):parts.append(linear_field((cr[0][cut],cr[1][cut]),B))
            fields.append(stack(parts,-1))
        if a.include_center:
            fields=add_center_correction(fields,low[sl],high[sl],float(data['lift_width']),center_delta)
        X,Xs,Xss,Xp,Xpp,Xsp=fields;normal=cross(Xp,Xs);area=sqrt(norm2(normal))
        assert all(np.all(np.isfinite(endpoint))for field in fields for endpoint in field)
        if np.any(area[0]<=0):raise ValueError('Area enclosure includes zero; refine boxes')
        support=div(dot(X,normal),area)
        x=(X[0][...,0],X[1][...,0]);y=(X[0][...,1],X[1][...,1])
        xp=(Xp[0][...,0],Xp[1][...,0]);yp=(Xp[0][...,1],Xp[1][...,1])
        azimuth=sub(mul(x,yp),mul(y,xp))
        radial_projection=add(mul(x,(cs[0][0][None,:],cs[1][0][None,:])),
                              mul(y,(ss[0][0][None,:],ss[1][0][None,:])))
        E=norm2(Xs);F=dot(Xs,Xp);G=norm2(Xp)
        L=div(dot(Xss,normal),area);M=div(dot(Xsp,normal),area);NN=div(dot(Xpp,normal),area)
        diag=np.full(area[0].shape,np.inf);det=np.full_like(diag,np.inf)
        for sign in [-1,1]:
            A=add(scale(E,a.curvature),scale(L,sign));B=add(scale(F,a.curvature),scale(M,sign));C=add(scale(G,a.curvature),scale(NN,sign))
            diagonal=np.minimum(A[0],C[0]);determinant=sub(mul(A,C),square(B))[0]
            diag=np.minimum(diag,diagonal);det=np.minimum(det,determinant)
        radius=sqrt(norm2(X))
        y=(X[0][...,1],X[1][...,1]);ay=(np.maximum(0,np.where(y[0]>0,y[0],np.where(y[1]<0,-y[1],0))),np.maximum(abs(y[0]),abs(y[1])))
        distance=square(sub(ay,p0));distance=add(distance,square((X[0][...,0],X[1][...,0])));distance=add(distance,square((X[0][...,2],X[1][...,2])));distance=sqrt((np.maximum(0,distance[0]),distance[1]))
        values={'support_lower':float(support[0].min()),'radius_upper':float(radius[1].max()),
            'witness_lower':float(distance[0].min()),'area_lower':float(area[0].min()),
            'curvature_psd_diagonal_lower':float(diag.min()),'curvature_psd_det_lower':float(det.min()),
            'planar_radial_projection_lower':float(radial_projection[0].min()),
            'azimuth_numerator_lower':float(azimuth[0].min())}
        for key,value in values.items():summary[key]=(max if key=='radius_upper'else min)(summary[key],value)
        bad=(support[0]<a.support)|(radius[1]>a.diameter/2)|(distance[0]<a.witness)|(diag<=0)|(det<=0)|(radial_projection[0]<=0)|(azimuth[0]<=0)
        count=int(bad.sum());total_failed+=count;checked+=bad.size
        for i,j in np.argwhere(bad)[:max(0,30-len(failed))]:
            failed.append(dict(s=[float(low[start+i]),float(high[start+i])],angle_index=int(j),
                support=float(support[0][i,j]),radius=float(radius[1][i,j]),witness=float(distance[0][i,j]),
                psd_diag=float(diag[i,j]),psd_det=float(det[i,j])))
        if start%128==0:print(json.dumps(dict(event='interval_batch',radial_done=start+len(bad),radial_total=len(low),boxes=checked,failed_boxes=total_failed,seconds=time.monotonic()-beg)),flush=True)
    out=dict(scope=__doc__,success=(total_failed==0),covered_radial_min=float(low.min()),covered_radial_max=float(high.max()),
        excluded_center_width=0. if a.include_center else float(data['lift_width']),
        center_diagnostics=center_diagnostics,radial_boxes=len(low),angular_quadrant_boxes=N,
        exact_symmetry='x even, y odd, z even in psi; half-turn XY plus reflected quadrant images.',
        boxes=checked,failed_boxes=total_failed,first_failures=failed,bounds=summary,
        thresholds={'curvature':a.curvature,'support':a.support,'diameter':a.diameter,'witness':a.witness},
        arithmetic='Binary64 nextafter outward interval operations; gamma_n-enclosed finite sums; 50-digit mpmath interval trigonometry. Stored binary64 jets are exact defining constants.',
        data_sha256=hashlib.sha256(a.data.read_bytes()).hexdigest(),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        center_source_sha256=hashlib.sha256(Path(__file__).with_name('tensor_interval_center.py').read_bytes()).hexdigest()if a.include_center else None,
        numpy=np.__version__,mpmath=mp.__version__,seconds=time.monotonic()-beg)
    a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='first_failures'}),flush=True)

if __name__=='__main__':main()
