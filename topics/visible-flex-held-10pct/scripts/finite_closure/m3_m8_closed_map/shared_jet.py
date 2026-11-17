"""Shared C2 Hermite evaluator and mean constructor, unchanged formulas.
Extracted from smallcut_c2_representative.py SHA256 8b2a452ff74bb685bf0b264bce1f40d598e47d36f26a3bdc269ecac2b50aac5e.
"""
import math
import numpy as np

class SharedJetQuintic:
    """Exact model: common endpoint jets and the normalized Hermite basis.

    Jets have shape (3, nstate, nknots). Treat their finite float entries as
    exact real constants when defining the map. The evaluator is approximate.
    """
    def __init__(self, x, jets):
        self.x=np.asarray(x,dtype=float)
        self.jets=np.asarray(jets,dtype=float)
        if self.jets.ndim!=3 or self.jets.shape[0]!=3 or self.jets.shape[2]!=len(self.x):
            raise ValueError('Expected shared jets[3, state, knot].')
        if not np.all(np.diff(self.x)>0):
            raise ValueError('Strictly increasing knots required.')
        j=np.asarray(self.jets,dtype=np.longdouble);h=np.diff(self.x).astype(np.longdouble)[None,:]
        y,d,q=j
        e0=y[:,1:]-y[:,:-1]-h*d[:,:-1]-h*h*q[:,:-1]/2
        e1=d[:,1:]-d[:,:-1]-h*q[:,:-1]
        e2=q[:,1:]-q[:,:-1]
        self._normalized=np.stack((y[:,:-1],h*d[:,:-1],h*h*q[:,:-1]/2,
             10*e0-4*h*e1+h*h*e2/2,
             -15*e0+7*h*e1-h*h*e2,
             6*e0-3*h*e1+h*h*e2/2))
    @classmethod
    def from_ppoly(cls, pp):
        return cls(pp.x,np.stack([pp(pp.x,k) for k in range(3)]))
    def __call__(self, x, nu=0):
        if not 0<=nu<=5:raise ValueError('Only derivatives 0 through 5 are implemented.')
        inp=np.asarray(x,dtype=float);flat=inp.reshape(-1)
        if np.any(flat<self.x[0]) or np.any(flat>self.x[-1]):
            raise ValueError('No extrapolation is part of the representative.')
        i=np.clip(np.searchsorted(self.x,flat,side='right')-1,0,len(self.x)-2)
        h=(self.x[i+1]-self.x[i]).astype(np.longdouble)
        t=(flat.astype(np.longdouble)-self.x[i].astype(np.longdouble))/h
        c=self._normalized[:,:,i]
        v=np.zeros(c.shape[1:],dtype=np.longdouble)
        for degree in range(5,nu-1,-1):
            factor=math.factorial(degree)//math.factorial(degree-nu)
            v=v*t[None,:]+factor*c[degree]
        v/=h[None,:]**nu
        out=np.asarray(v,dtype=float)
        # The endpoint value of each of the first three jets is its one shared
        # datum. This is also exactly the endpoint identity of the Hermite basis.
        if nu<=2:
            k=np.searchsorted(self.x,flat,side='left')
            exact=(k<len(self.x)) & (self.x[np.minimum(k,len(self.x)-1)]==flat)
            out[:,exact]=self.jets[nu,:,k[exact]].T
        return out.reshape((out.shape[0],)+inp.shape)

def build_mean(flow,sol,angular=1536,order=8):
    """Define a finite C2 mean coordinate from one shared two-jet per knot."""
    s=sol.x
    height=flow.height_integral(sol,s,angular,order)
    mu=np.empty(len(s));mup=np.empty(len(s));_,B1,B2=flow.basis(angular)
    for first in range(0,len(s),32):
        sl=slice(first,first+32);t=s[sl]
        fr,_,dW=flow.velocity_s(t,sol.sol(t),sol.sol(t,1),B1,B2)
        mu[sl]=np.mean(fr['V'][:,:,2],axis=1)
        mup[sl]=np.mean(dW[:,:,2],axis=1)
    return SharedJetQuintic(s,np.stack((height,mu,mup))[:,None,:])
