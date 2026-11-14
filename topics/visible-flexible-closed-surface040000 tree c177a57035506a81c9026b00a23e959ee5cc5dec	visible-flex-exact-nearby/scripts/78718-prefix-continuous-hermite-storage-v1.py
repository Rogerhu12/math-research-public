#!/usr/bin/env python3
# New 78718 explicit storage adaptation; original mathematical source is retained below.
"""Outward-rounded continuous geometry bounds for an exact shared-jet map.

No source BVP evaluator is imported. Saved binary64 nodal jets and mean
increments define an exact piecewise quintic, finite-Fourier map. Bernstein
hulls enclose each radial span; rational Taylor enclosures cover angular
arcs. This certifies only the finite represented map, not a closed surface,
an infinite tail, an exact metric, or a prefix-cylinder interface.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
from fractions import Fraction as Q
from functools import lru_cache
import gzip
import hashlib
import io
import json
import math
from pathlib import Path
import time
import numpy as np
import importlib.util

HERE = Path(__file__).resolve().parent

_storage_spec = importlib.util.spec_from_file_location(
    'prefix_78718_explicit_storage', HERE/'78718-prefix-storage-v1.py')
storage = importlib.util.module_from_spec(_storage_spec)
_storage_spec.loader.exec_module(storage)


def down(x):
    return np.nextafter(x, -np.inf)


def up(x):
    return np.nextafter(x, np.inf)


class I:
    """Closed binary64 intervals; every arithmetic operation rounds out."""
    def __init__(self, lo, hi=None):
        self.lo = np.asarray(lo, dtype=np.float64)
        self.hi = self.lo if hi is None else np.asarray(hi, dtype=np.float64)

    @staticmethod
    def get(x):
        return x if isinstance(x, I) else I(x)

    def __getitem__(self, key):
        return I(self.lo[key], self.hi[key])

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __add__(self, x):
        x = I.get(x)
        return I(down(self.lo+x.lo), up(self.hi+x.hi))

    __radd__ = __add__

    def __sub__(self, x):
        return self + (-I.get(x))

    def __rsub__(self, x):
        return I.get(x) + (-self)

    def __mul__(self, x):
        x = I.get(x)
        a, b = self.lo*x.lo, self.lo*x.hi
        c, d = self.hi*x.lo, self.hi*x.hi
        return I(down(np.minimum(np.minimum(a,b),np.minimum(c,d))),
                 up(np.maximum(np.maximum(a,b),np.maximum(c,d))))

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = I.get(x)
        if np.any((x.lo <= 0) & (x.hi >= 0)):
            raise ArithmeticError('Division interval contains zero')
        return self * I(down(1/x.hi), up(1/x.lo))

    def square(self):
        lower = np.minimum(self.lo*self.lo, self.hi*self.hi)
        lower = np.where((self.lo <= 0) & (self.hi >= 0), 0, down(lower))
        return I(np.maximum(lower,0), up(np.maximum(self.lo*self.lo,self.hi*self.hi)))

    def sqrt(self):
        if np.any(self.lo < 0):
            raise ArithmeticError('Square-root interval has negative input')
        return I(np.maximum(0,down(np.sqrt(self.lo))), up(np.sqrt(self.hi)))

    def abs(self):
        low = np.where((self.lo <= 0)&(self.hi >= 0), 0,
                       np.minimum(abs(self.lo),abs(self.hi)))
        return I(low, np.maximum(abs(self.lo),abs(self.hi)))


def qbounds(q):
    f = float(q)
    fq = Q.from_float(f)
    return I(math.nextafter(f,-math.inf) if fq > q else f,
             math.nextafter(f,math.inf) if fq < q else f)


def stack(items, axis):
    return I(np.stack([x.lo for x in items],axis=axis),
             np.stack([x.hi for x in items],axis=axis))


def dot(a,b):
    ans = I(np.zeros(np.broadcast_shapes(a.lo.shape[:-1],b.lo.shape[:-1])))
    for j in range(3):
        ans = ans+a[...,j]*b[...,j]
    return ans


def norm(a):
    ans = a[...,0].square()+a[...,1].square()+a[...,2].square()
    return ans.sqrt()


def cross(a,b):
    return stack([a[...,1]*b[...,2]-a[...,2]*b[...,1],
                  a[...,2]*b[...,0]-a[...,0]*b[...,2],
                  a[...,0]*b[...,1]-a[...,1]*b[...,0]],-1)


@lru_cache(None)
def pi_bounds():
    # Machin identity, with alternating-series errors in each arctangent.
    def atan(q):
        n=42
        s=sum(((-1)**k*q**(2*k+1)/Q(2*k+1) for k in range(n)),Q(0))
        e=q**(2*n+1)/Q(2*n+1)
        return s-e,s+e
    a,b=atan(Q(1,5));c,d=atan(Q(1,239))
    lo,hi=16*a-4*d,16*b-4*c
    scale=10**50
    return Q((lo*scale).numerator//(lo*scale).denominator,scale), Q(-((-hi*scale).numerator//(-hi*scale).denominator),scale)


@lru_cache(None)
def trig_point(q, cosine):
    q = (q+1) % 2 - 1
    lo,hi=pi_bounds()
    x=q*(lo+hi)/2
    if cosine:
        p=sum(((-1)**k*x**(2*k)/math.factorial(2*k) for k in range(25)),Q(0))
        err=abs(x)**49/math.factorial(49)
    else:
        p=sum(((-1)**k*x**(2*k+1)/math.factorial(2*k+1) for k in range(25)),Q(0))
        err=abs(x)**50/math.factorial(50)
    err += abs(q)*(hi-lo)/2
    return float(qbounds(p-err).lo),float(qbounds(p+err).hi)


def floor(q):
    return q.numerator//q.denominator


def ceil(q):
    return -floor(-q)


def trig_range(a,b,cosine):
    ea,eb=trig_point(a,cosine),trig_point(b,cosine)
    lo,hi=min(ea[0],eb[0]),max(ea[1],eb[1])
    max_at,min_at=(Q(0),Q(1)) if cosine else (Q(1,2),Q(3,2))
    if ceil((a-max_at)/2)<=floor((b-max_at)/2):hi=1.
    if ceil((a-min_at)/2)<=floor((b-min_at)/2):lo=-1.
    return lo,hi


def trigonometry(modes, angular):
    a=np.empty((modes,angular,2));b=a.copy()
    for j in range(1,modes+1):
        for k in range(angular):
            left,right=Q(2*j*k,angular),Q(2*j*(k+1),angular)
            a[j-1,k]=trig_range(left,right,True)
            b[j-1,k]=trig_range(left,right,False)
    return I(a[...,0],a[...,1]),I(b[...,0],b[...,1])


def witness_trigonometry(angular):
    out=[]
    for sector in range(3):
        a=np.empty((angular,2));b=a.copy()
        for k in range(angular):
            lo=Q(1,3)-Q(2*(k+1),3*angular)-Q(2*sector,3)
            hi=Q(1,3)-Q(2*k,3*angular)-Q(2*sector,3)
            a[k]=trig_range(lo,hi,True);b[k]=trig_range(lo,hi,False)
        out.append((I(a[:,0],a[:,1]),I(b[:,0],b[:,1])))
    return out


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class ExactHermite:
    def __init__(self,path):
        self.path=Path(path)
        self.meta=json.loads(self.path.read_text())
        stored_meta,payload,self.storage_bindings=storage.read_payload(self.path,verify_arrays=True)
        if stored_meta!=self.meta:raise ValueError('Geometry metadata changed during storage read')
        raw=np.load(io.BytesIO(gzip.decompress(payload)),allow_pickle=False)
        self.x=raw['mesh'];self.M=self.meta['modes']
        nodal=raw['jets']
        self.inlet_radius_exact=sum((Q.from_float(float(v)) for v in nodal[0,0,:self.M+1]),Q(0))
        r=sum((Q.from_float(float(v))*(-1)**j for j,v in enumerate(nodal[0,0,:self.M+1])),Q(0))
        tangent0=self.inlet_radius_exact+sum((3*j*Q.from_float(float(nodal[0,0,self.M+j])) for j in range(1,self.M+1)),Q(0))
        tangent_half=r+sum((3*j*(-1)**j*Q.from_float(float(nodal[0,0,self.M+j])) for j in range(1,self.M+1)),Q(0))
        dz0=sum((Q.from_float(float(v)) for v in nodal[1,0,2*self.M+1:]),Q(0))
        dzhalf=Q.from_float(float(nodal[1,0,-1]))+sum(((-1)**j*Q.from_float(float(nodal[1,0,2*self.M+j])) for j in range(1,self.M+1)),Q(0))
        self.inlet_exact=dict(planar_z_values_zero=bool(np.all(nodal[0,0,2*self.M+1:]==0)),
            horizontal_first_jet_zero=bool(np.all(nodal[1,0,:2*self.M+1]==0)),
            vertical_second_jet_zero=bool(np.all(nodal[2,0,2*self.M+1:]==0)),
            vertical_second_jet_abs_max=float(np.max(abs(nodal[2,0,2*self.M+1:]))),
            radius_at_zero=str(self.inlet_radius_exact),radius_at_pi_over_three=str(r),
            radial_gap_exact=str(self.inlet_radius_exact-r),radial_gap_lower=float(qbounds(self.inlet_radius_exact-r).lo),
            tangent_at_zero=str(tangent0),tangent_at_pi_over_three=str(tangent_half),
            tangent_signs_positive=bool(tangent0>0 and tangent_half>0),
            vertical_first_at_zero=str(dz0),vertical_first_at_pi_over_three=str(dzhalf),
            vertical_first_signs_positive=bool(dz0>0 and dzhalf>0))
        if not (np.isfinite(nodal).all() and np.isfinite(self.x).all() and np.isfinite(raw['mean_increments']).all()):
            raise ValueError('Nonfinite input')
        if nodal.shape!=(3,len(self.x),3*self.M+2):raise ValueError('Unexpected data shape')
        if not np.all(np.diff(self.x)>0):raise ValueError('Non-increasing mesh')
        Y=I(nodal[0].copy(),nodal[0].copy());D=I(nodal[1]);Q2=I(nodal[2])
        qsum=Q(0)
        for k in range(len(self.x)):
            y=qbounds(qsum);Y.lo[k,-1]=y.lo;Y.hi[k,-1]=y.hi
            if k<len(self.x)-1:qsum+=Q.from_float(float(raw['mean_increments'][k]))
        self.h=I(self.x[1:])-I(self.x[:-1])
        h=self.h[:,None]
        delta=Y[1:]-Y[:-1]
        delta.lo[:,-1]=raw['mean_increments'];delta.hi[:,-1]=raw['mean_increments']
        c0,c1,c2=Y[:-1],h*D[:-1],h*h*Q2[:-1]/2
        e0=delta-c1-c2
        e1=h*(D[1:]-D[:-1])-h*h*Q2[:-1]
        e2=h*h*(Q2[1:]-Q2[:-1])
        self.power=stack([c0,c1,c2,10*e0-4*e1+e2/2,
                          -15*e0+7*e1-e2,6*e0-3*e1+e2/2],1)

    def ranges(self,derivative,a=Q(0),b=Q(1)):
        d=5-derivative
        source=[self.power[:,k+derivative,:]*
                (math.factorial(k+derivative)//math.factorial(k)) for k in range(d+1)]
        # Translation and rescaling from tau in [a,b] to u in [0,1].
        p=[]
        for k in range(d+1):
            v=I(np.zeros_like(source[0].lo))
            for j in range(k,d+1):
                if j==k or a:
                    v=v+source[j]*qbounds(math.comb(j,k)*a**(j-k)*(b-a)**k)
            p.append(v)
        bern=[]
        for k in range(d+1):
            v=I(np.zeros_like(p[0].lo))
            for j in range(k+1):v=v+p[j]*qbounds(Q(math.comb(k,j),math.comb(d,j)))
            bern.append(v)
        hull=I(np.minimum.reduce([x.lo for x in bern]),np.maximum.reduce([x.hi for x in bern]))
        for _ in range(derivative):hull=hull/self.h[:,None]
        return hull


def cylindrical(c,cos,sin,M):
    n=c.lo.shape[0];N=cos.lo.shape[1]
    zero=lambda:I(np.zeros((n,N)))
    R=zero()+c[:,0,None];T=zero();Z=zero()+c[:,-1,None]
    Rp,Tp,Zp=zero(),zero(),zero()
    Rpp,Tpp,Zpp=zero(),zero(),zero()
    for j in range(1,M+1):
        m=3*j;co=cos[j-1][None,:];si=sin[j-1][None,:]
        r,t,z=c[:,j,None],c[:,M+j,None],c[:,2*M+j,None]
        R=R+r*co;T=T+t*si;Z=Z+z*co
        Rp=Rp-m*r*si;Tp=Tp+m*t*co;Zp=Zp-m*z*si
        Rpp=Rpp-m*m*r*co;Tpp=Tpp-m*m*t*si;Zpp=Zpp-m*m*z*co
    return (stack([R,T,Z],-1),stack([Rp-T,R+Tp,Zp],-1),
            stack([Rpp-2*Tp-R,2*Rp+Tpp-T,Zpp],-1))


def certify(args):
    begin=time.monotonic()
    geom=ExactHermite(args.geometry)
    cos,sin=trigonometry(geom.M,args.angular)
    witness=witness_trigonometry(args.angular) if args.witness else None
    witness_radius=qbounds(geom.inlet_radius_exact)
    ell=geom.meta['ell'] if args.ell is None else args.ell
    stop=len(geom.x)-1 if args.stop is None else min(args.stop,len(geom.x)-1)
    out=dict(scope=__doc__,geometry=str(args.geometry),geometry_sha256=sha(args.geometry),
             data_sha256=geom.meta['data_sha256'],script_sha256=sha(__file__),
             storage_bindings=geom.storage_bindings,
             angular_intervals_per_threefold_period=args.angular,radial_subdivisions=args.radial,
             first_span=args.start,last_span_exclusive=stop,total_spans=len(geom.x)-1,
             backend='IEEE754 binary64 arithmetic, nextafter outward on every operation; '
                     'Machin arctangent rational enclosure of pi; rational Taylor enclosures of trig; '
                     'Bernstein radial convex-hull bounds. No source evaluator imported.',
             support_lower=float('inf'),principal_curvature_upper=0.,norm_upper=0.,
             area_element_lower=float('inf'),complete_closed_surface=False,
             cylinder_interface_certified=False,metric_certified=False)
    out['ell_as_binary64']=ell
    out['inlet_exact']=geom.inlet_exact
    out['mirror_interface_certified']=(ell==0 and geom.inlet_exact['planar_z_values_zero']
                                      and geom.inlet_exact['horizontal_first_jet_zero']
                                      and geom.inlet_exact['vertical_second_jet_zero'])
    if witness is not None:
        out.update(witness_distance_lower=float('inf'),
                   witness_radius_exact=str(geom.inlet_radius_exact),
                   witness_angle='pi/3',witness_height=0.,
                   witness_scope='Distance only to represented upper prefix, all three angular sectors. '
                                 'Reflection in z=0 preserves this distance. Other blocks require separate checks; '
                                 'the witness must occur on the actual rotating core.')
    for sub in range(args.radial):
        bounds=[geom.ranges(d,Q(sub,args.radial),Q(sub+1,args.radial)) for d in range(3)]
        for first in range(args.start,stop,args.batch):
            end=min(first+args.batch,stop)
            X,Xp,Xpp=cylindrical(bounds[0][first:end],cos,sin,geom.M)
            Xs,Xsp,_=cylindrical(bounds[1][first:end],cos,sin,geom.M)
            Xss,_,_=cylindrical(bounds[2][first:end],cos,sin,geom.M)
            X.lo[...,2]=down(X.lo[...,2]+ell)
            X.hi[...,2]=up(X.hi[...,2]+ell)
            if witness is not None:
                for co,si in witness:
                    v=stack([X[...,0]-witness_radius*co[None,:],
                             X[...,1]-witness_radius*si[None,:],X[...,2]],-1)
                    out['witness_distance_lower']=min(out['witness_distance_lower'],float(norm(v).lo.min()))
            area=cross(Xp,Xs);length=norm(area)
            if float(length.lo.min())<=0:
                raise ArithmeticError(f'Unresolved immersion, spans {first}:{end}')
            normal=area/length[...,None]
            support=dot(X,normal)
            E,F,G=dot(Xs,Xs),dot(Xs,Xp),dot(Xp,Xp)
            L,M,N=dot(Xss,normal),dot(Xsp,normal),dot(Xpp,normal)
            det=length.square()
            tr=(L*G-2*M*F+N*E)/det
            gauss=(L*N-M.square())/det
            discr=tr.square()-4*gauss
            discr=I(np.maximum(0,discr.lo),np.maximum(0,discr.hi))
            curv=(tr.abs()+discr.sqrt())/2
            out['support_lower']=min(out['support_lower'],float(support.lo.min()))
            out['principal_curvature_upper']=max(out['principal_curvature_upper'],float(curv.hi.max()))
            out['norm_upper']=max(out['norm_upper'],float(norm(X).hi.max()))
            out['area_element_lower']=min(out['area_element_lower'],float(length.lo.min()))
    out['two_ball_diameter_upper']=float(up(2*out['norm_upper']))
    out['entire_finite_prefix_covered']=args.start==0 and stop==len(geom.x)-1
    out['continuous_bounds_certified']=out['entire_finite_prefix_covered']
    out['time_seconds']=time.monotonic()-begin
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('scope','backend')},indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--geometry',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--angular',type=int,default=256)
    p.add_argument('--radial',type=int,default=1)
    p.add_argument('--start',type=int,default=0)
    p.add_argument('--stop',type=int)
    p.add_argument('--batch',type=int,default=16)
    p.add_argument('--ell',type=float,help='Exact binary64 vertical shift overriding metadata; recorded explicitly')
    p.add_argument('--witness',action='store_true',help='Bound distance of half-period core witness to all angular sectors')
    certify(p.parse_args())
