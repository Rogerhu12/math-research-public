#!/usr/bin/env python3
"""Importable directed scalar and finite-speed-mean jets for pulse26e53.

Pass the frozen f512 interval module as I. This helper itself makes no
geometric certificate claim. ScalarEnvelope uses the exact nodal scalar,
not the floating Profile evaluator, and is restricted to s in [0,1].
Vector jets are triples of intervals, each with angular axis last.
"""
import numpy as np


def hermite_bezier(I,left,right,h):
    """Exact nodal (value,first,second) -> degree-five value/first controls."""
    y0,y1=I.exact(left[0]),I.exact(right[0])
    v0,v1=I.mul(h,I.exact(left[1])),I.mul(h,I.exact(right[1]))
    a0,a1=I.mul(I.square(h),I.exact(left[2])),I.mul(I.square(h),I.exact(right[2]))
    b=I.stack([y0,I.add(y0,I.div(v0,I.exact(5))),
        I.add(I.add(y0,I.div(I.scale(v0,2),I.exact(5))),I.div(a0,I.exact(20))),
        I.add(I.sub(y1,I.div(I.scale(v1,2),I.exact(5))),I.div(a1,I.exact(20))),
        I.sub(y1,I.div(v1,I.exact(5))),y1])
    v=I.div(I.scale(I.sub(I.at(b,slice(1,None)),I.at(b,slice(None,-1))),5),h)
    elevated=[I.at(v,0)]
    for j in range(1,5):
        elevated.append(I.div(I.add(I.scale(I.at(v,j-1),j),I.scale(I.at(v,j),5-j)),I.exact(5)))
    return b,I.stack(elevated+[I.at(v,4)])


def hull(controls):
    return controls[0].min(axis=0),controls[1].max(axis=0)


class ScalarEnvelope:
    """at((s_lo,s_hi)) returns directed intervals (a,a_s)."""
    def __init__(self,I,data):
        self.I=I;g=data['fixed_scalar_profile']['geometry'];knots=g['knots']
        self.x=np.array([z['s']for z in knots]);self.j=np.array([[z[k]for k in ('a','ap','app')]for z in knots])
        self.origin=data['analytic_extension_origin'];s=data['inward_scalar_profile'];p=s['compact_curvature_pulse']
        if self.x[0]!=0 or self.x[-1]!=self.origin or not np.isfinite(self.j).all() or np.any(np.diff(self.x)<=0):
            raise ValueError('Ordered finite old scalar required')
        if not np.array_equal(self.j[0],np.array([1.,0.,g['initial_law']['k0']])):
            raise ValueError('First exact initial-law jet mismatch')
        if self.origin!=.99 or s['cut']!=.995 or s['curvature']!=1.5 or s['ramp_in']!=.02 or p['amplitude']!=-5 or p['half_width']!=.005:
            raise ValueError('This envelope is restricted to the fixed pulse design')
        self.K=I.div(I.neg(I.exact(self.j[-1,2])),I.sqrt(I.sub(I.exact(1.),I.square(I.exact(self.j[-1,1])))))
        if not (self.K[0]>1.5 and self.K[1]<3.5):raise ValueError('Absolute curvature bound unavailable')
        self.old=[]
        for i in range(len(self.x)-1):
            h=I.sub(I.exact(self.x[i+1]),I.exact(self.x[i]))
            self.old.append(tuple(hull(z)for z in hermite_bezier(I,self.j[i],self.j[i+1],h)))

    def at(self,interval):
        I=self.I;lo,hi=map(float,interval)
        if not (0<=lo<=hi<=1):raise ValueError('Envelope domain is [0,1]')
        boxes=[]
        if lo<=self.origin:
            for j in range(max(0,int(np.searchsorted(self.x,lo,side='left'))-1),len(self.x)-1):
                if self.x[j]>hi:break
                if self.x[j+1]>=lo:boxes.append(self.old[j])
        if hi>=self.origin:
            delta=(max(0.,float(I.down(lo-self.origin))),max(0.,float(I.up(hi-self.origin))))
            rem=float(I.scale(I.square(delta),1.75)[1]);vp=float(I.scale(delta,3.5)[1])
            aa=I.add(I.add(I.exact(self.j[-1,0]),I.scale(delta,self.j[-1,1])),(-rem,rem))
            av=I.add(I.exact(self.j[-1,1]),(-vp,vp));boxes.append((aa,av))
        return tuple((min(z[k][0]for z in boxes),max(z[k][1]for z in boxes))for k in range(2))


def tree_mean(I,value):
    """Mean over a dyadic last axis, with explicit directed binary additions."""
    n=value[0].shape[-1]
    if n<1 or n&(n-1):raise ValueError('Dyadic angular sample count required')
    while value[0].shape[-1]>1:
        value=I.add(I.at(value,(...,slice(0,None,2))),I.at(value,(...,slice(1,None,2))))
    return I.div(I.at(value,(...,0)),I.exact(n))


def speed_mean_jets(I,d,ds,dss=None):
    """Return (b,b_s[,b_ss]) for b=mean |d| at fixed angular nodes."""
    def add3(values):return I.add(I.add(values[0],values[1]),values[2])
    def dot(v,w):return add3([I.mul(v[j],w[j])for j in range(3)])
    q=I.sqrt(add3([I.square(v)for v in d]))
    if np.any(q[0]<=0):raise ValueError('Speed interval meets zero')
    h=dot(d,ds);qs=I.div(h,q)
    result=(tree_mean(I,q),tree_mean(I,qs))
    if dss is not None:
        numerator=I.add(add3([I.square(v)for v in ds]),dot(d,dss))
        qss=I.sub(I.div(numerator,q),I.div(I.square(h),I.mul(I.square(q),q)))
        result+=(tree_mean(I,qss),)
    return result


def scaling_jets(I,a,ap,b,bp,app=None,bpp=None):
    """Return (lambda,lambda_s[,lambda_ss]) from a=lambda*b exactly."""
    lam=I.div(a,b);lp=I.div(I.sub(I.mul(ap,b),I.mul(a,bp)),I.square(b))
    if (app is None)!=(bpp is None):raise ValueError('Second jets must be supplied together')
    if app is None:return lam,lp
    lpp=I.div(I.sub(I.sub(app,I.mul(lam,bpp)),I.scale(I.mul(lp,bp),2)),b)
    return lam,lp,lpp
