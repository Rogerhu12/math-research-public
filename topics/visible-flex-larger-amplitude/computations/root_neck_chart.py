"""C2 positive numerical coordinate fixing every finite-neck physical knot.

On each t interval, the derivative is a quartic Bernstein polynomial with
controls [v0,v0,5*r-2*v0-2*v1,v1,v1], where r is the physical secant.
Positive harmonic-mean nodal slopes are multiplied by a smooth common
factor guaranteeing 2*(v0+v1)/(5*r)<.95 in every interval. All controls
are positive; the integral is the prescribed physical interval length.
Equal endpoint derivatives and zero endpoint second derivatives give a
global C2 increasing map. This changes only the numerical coordinate,
never the physical meridian metric. Nearly uniform secants give a nearly
affine map, avoiding artificial high radial derivatives in a warm solve.
"""
import numpy as np


class NeckChart:
    def __init__(self,t,s):
        self.t=np.asarray(t,float);self.s=np.asarray(s,float)
        if self.t.shape!=self.s.shape or len(self.t)<2:
            raise ValueError('Physical neck knot topology changed')
        h=np.diff(self.t);r=np.diff(self.s)/h
        if np.min(h)<=0 or np.min(r)<=0:raise FloatingPointError('Nonpositive neck chart interval')
        self.h=h;self.r=r
        v=np.empty(len(r)+1);v[0]=r[0];v[-1]=r[-1]
        v[1:-1]=2/(1/r[:-1]+1/r[1:])
        ratios=2*(v[:-1]+v[1:])/(5*r)
        # This is smooth in all positive physical interval lengths. Since
        # scale <= .95/ratios[j], every middle control is >= .25*r[j].
        scale=(1+float(np.sum((ratios/.95)**64)))**(-1/64)
        v*=scale;self.slope_scale=scale
        self.v=v
        self.bernstein_min=float(np.min(np.r_[v,5*r-2*v[:-1]-2*v[1:]]))
        if self.bernstein_min<=0:raise FloatingPointError('Nonpositive Bernstein derivative control')

    def evaluate(self,t):
        t=np.asarray(t,float)
        j=np.clip(np.searchsorted(self.t,t,side='right')-1,0,len(self.h)-1)
        u=(t-self.t[j])/self.h[j];r=self.r[j];v=self.v[j];w=self.v[j+1]
        c3=10*r-6*v-4*w;c4=-15*r+8*v+7*w;c5=6*r-3*v-3*w
        value=self.s[j]+self.h[j]*(v*u+c3*u**3+c4*u**4+c5*u**5)
        first=v+3*c3*u*u+4*c4*u**3+5*c5*u**4
        return value,first

    def inverse(self,s):
        s=np.asarray(s,float)
        j=np.clip(np.searchsorted(self.s,s,side='right')-1,0,len(self.h)-1)
        lo=self.t[j].copy();hi=self.t[j+1].copy()
        t=lo+(hi-lo)*(s-self.s[j])/(self.s[j+1]-self.s[j])
        for _ in range(50):
            value,first=self.evaluate(t);res=value-s
            done=abs(res)<=3e-14*np.maximum(1.,abs(s))
            if np.all(done):return t
            lo=np.where((res<0)&~done,t,lo);hi=np.where((res>0)&~done,t,hi)
            new=t-res/first;bad=(new<=lo)|(new>=hi)|~np.isfinite(new)
            t=np.where(done,t,np.where(bad,(lo+hi)/2,new))
        raise FloatingPointError('Neck chart inversion failed')
