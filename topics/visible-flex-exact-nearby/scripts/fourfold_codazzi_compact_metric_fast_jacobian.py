#!/usr/bin/env python3
"""Exact discrete Fourier identities for the floating Codazzi Jacobian.

AB=2 alpha B/C is odd and Ac=-(ell Cr^2+alpha^2 B^2)/C^2 is even.
Their multiplication matrices are Toeplitz-plus-Hankel Fourier tables.
The entire sampled rational functions are transformed, without truncating
their Fourier coefficients.  This computes the same finite trapezoidal
Jacobian as the original three-index angular contractions, up to floating
roundoff.  It does not certify the continuous nonlinear PDE.
"""
from __future__ import annotations
import numpy as np
from fourfold_codazzi_compact_metric_branch_probe import CompactNormalized


class FastCompactNormalized(CompactNormalized):
    def base(self,r):
        r=np.atleast_1d(np.asarray(r,dtype=float));key=r.tobytes()
        if not hasattr(self,'all_base_cache'):self.all_base_cache={}
        if key not in self.all_base_cache:self.all_base_cache[key]=super().base(r)
        return self.all_base_cache[key]

    def jacobian(self,r,y,p):
        t,B,c,C,A=self.data(r,y,p);a,g,b,K,ell,Cr,dg,dl,dCr=t
        m=self.modes;n=2*m+1;N=self.angular_grid
        AB=2*self.alpha*B/C
        Ac=-(ell*Cr*Cr+self.alpha*self.alpha*B*B)/(C*C)
        fb=np.fft.fft(AB,axis=0).imag/N
        fc=np.fft.fft(Ac,axis=0).real/N
        rows=np.arange(m+1)[:,None]
        kb=np.arange(1,m+1)[None,:];kc=np.arange(m+1)[None,:]
        scale=np.ones((m+1,1,1));scale[0]=.5
        da_b=scale*(fb[(rows-kb)%N]-fb[(rows+kb)%N])
        da_c=scale*(fc[(rows-kc)%N]+fc[(rows+kc)%N])
        da=np.concatenate([da_b,da_c],axis=1);out=np.empty((n,n,len(r)))
        out[:m]=-g*self.frequency[:,None,None]*da[1:]
        out[m:]=b*da
        for j in range(m):
            out[j,j]-=2*b;out[m+1+j,j]+=g*self.frequency[j]
        for j in range(m+1):out[m+j,m+j]-=b
        dA=-dl*c+self.alpha*dl*c*c/C-self.alpha*(B*B+ell*c*c)*dCr/(C*C)
        ap=self.proj@dA;ac=self.proj@A;dp=np.empty((n,1,len(r)))
        dp[:m,0]=-self.frequency[:,None]*(dg*ac[1:]+g*ap[1:])
        dp[m:,0]=b*ap;dp[m+1:,0]+=dg*self.frequency[:,None]*y[:m]
        self.jac_calls+=1
        return out,dp
