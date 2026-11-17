"""Exactly equivalent continuous finite system in physical height/momentum.

h = r*w*v, p = w**2*t, each divided by one fixed nonzero constant scale.
Only the radial collocation coordinates change. The full original moment
equations, angular quadrature, mean, and D/S conditions are unchanged.
"""
import numpy as np


class PhysicalMixedFields:
    def __init__(self, base, height_scale, momentum_scale):
        self.base=base
        self.height_scale=float(height_scale)
        self.momentum_scale=float(momentum_scale)
        if self.height_scale<=0 or self.momentum_scale<=0:
            raise ValueError('Positive fixed coordinate scales are required')

    def __getattr__(self,name):
        return getattr(self.base,name)

    def to_base(self,Y,r,w):
        Y=np.atleast_2d(np.asarray(Y,float)).copy()
        r,w=[np.broadcast_to(np.asarray(q,float),(len(Y),))for q in (r,w)]
        Y[:,:self.d]*=(self.height_scale/(r*w))[:,None]
        Y[:,self.d:2*self.d]*=(self.momentum_scale/w**2)[:,None]
        return Y

    def from_base(self,Y,r,w):
        Y=np.atleast_2d(np.asarray(Y,float)).copy()
        r,w=[np.broadcast_to(np.asarray(q,float),(len(Y),))for q in (r,w)]
        Y[:,:self.d]*=((r*w)/self.height_scale)[:,None]
        Y[:,self.d:2*self.d]*=(w**2/self.momentum_scale)[:,None]
        return Y

    def evaluate(self,Y,r,w,rx,ell,jacobian=False):
        Y=np.atleast_2d(np.asarray(Y,float));n=len(Y);d=self.d
        r,w,rx,ell=[np.broadcast_to(np.asarray(q,float),(n,))for q in (r,w,rx,ell)]
        Z=self.to_base(Y,r,w)
        e=self.base.evaluate(Z,r,w,rx,ell,jacobian)
        v=Z[:,:d];L=Z[:,2*d:]
        P=v@self.dphi;Pt=v@self.ddphi;Lv=L@self.Phi
        K=Lv-Pt;U=(L[:,1:]+(self.freq**2-1)*v)@self.dphi
        ww=w[:,None]**2;E=1+ww;D=1-ww*(2*K+K*K+E*P*P);S=1-ww*P*P
        flux=(1+K)*U/(S*np.sqrt(D))
        hs,ps=self.height_scale,self.momentum_scale
        fh=(rx*w/hs)[:,None]*(self.freq**2*v+L[:,1:])
        fp=-(rx/r*w*w/ps)[:,None]*(flux@self.dphi.T)/self.angular
        e['flow']=np.c_[fh,fp]
        if jacobian:
            vs=hs/(r*w);ts=ps/w**2
            aj=e['algebraic_jacobian'].copy()
            aj[:,:,:d]*=vs[:,None,None]
            aj[:,:,d:2*d]*=ts[:,None,None]
            old=e['flow_jacobian'];fj=np.zeros_like(old);j=np.arange(d)
            fj[:,j,j]=(rx/r)[:,None]*self.freq**2
            fj[:,j,2*d+1+j]=(rx*w/hs)[:,None]
            fj[:,d:,:d]=(w*w/ps*vs)[:,None,None]*old[:,d:,:d]
            fj[:,d:,2*d:]=(w*w/ps)[:,None,None]*old[:,d:,2*d:]
            e['flow_jacobian']=fj;e['algebraic_jacobian']=aj
        return e
