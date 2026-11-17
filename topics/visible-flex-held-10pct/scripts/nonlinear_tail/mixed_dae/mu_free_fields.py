"""Full finite momentum equations in physical (v,t,L), without a Gram inverse.

The discrete angular quadrature, complete mean and nonlinear products are
retained. Pointwise D/S remain strict domain conditions. This is an explicitly
separate mixed formulation, not an accepted positive-A tail computation.
"""
import numpy as np


class MuFreeFields:
    def __init__(self,modes=8,spacing=2,angular=256,full=True,floor=.01):
        self.modes=int(modes);self.spacing=int(spacing);self.angular=int(angular)
        self.full=bool(full);self.floor=float(floor)
        if self.angular<=4*self.modes*self.spacing:raise ValueError('Angular grid does not meet the original resolved-grid condition')
        u=2*np.pi*np.arange(self.angular)/self.angular
        f=self.spacing*np.arange(1,self.modes+1)
        co=np.sqrt(2)*np.cos(f[:,None]*u);si=np.sqrt(2)*np.sin(f[:,None]*u)
        if full:
            self.freq=np.r_[f,f];self.phi=np.r_[co,si]
            self.dphi=np.r_[-f[:,None]*si,f[:,None]*co]
        else:self.freq=f;self.phi=co;self.dphi=-f[:,None]*si
        self.d=len(self.freq);self.J=self.d+1;self.width=3*self.d+1
        self.ddphi=-self.freq[:,None]**2*self.phi
        self.Phi=np.vstack([np.ones(self.angular),self.phi])
        self.dPhi=np.vstack([np.zeros(self.angular),self.dphi])

    def evaluate(self,Y,r,w,rx,ell,jacobian=False):
        """Y has node rows [v,t,L]; ell=(log w)_x, rx=r_x."""
        Y=np.atleast_2d(np.asarray(Y,dtype=float));n=len(Y);d=self.d
        r,w,rx,ell=[np.broadcast_to(np.asarray(a,float),(n,))for a in (r,w,rx,ell)]
        if Y.shape[1]!=self.width or np.any(r<=0)or np.any(w<=0):raise ValueError('Mixed state or physical profile is invalid')
        v=Y[:,:d];t=Y[:,d:2*d];L=Y[:,2*d:]
        ww=w[:,None]**2;E=1+ww;s=rx/r
        P=v@self.dphi;Pt=v@self.ddphi;Lv=L@self.Phi
        K=Lv-Pt;U=(L[:,1:]+(self.freq**2-1)*v)@self.dphi
        T=2*K+K*K+E*P*P;q=ww*T;D=1-q;S=1-ww*P*P;A=1+Lv+ww*Pt
        if np.min(D)<=self.floor or np.min(S)<=self.floor or not np.all(np.isfinite(D+S)):
            raise FloatingPointError('Mixed finite chart D/S domain failure')
        sd=np.sqrt(D)
        fc=q*(2+sd)/(2*sd*(1+sd)**2)
        gc=ww*(P*P+S*T/(1+sd))/(S*sd)
        quad=.5*(K*K+E*P*P)+K*Pt+T*fc+(1+K)*Pt*gc
        moments=L+quad@self.Phi.T/self.angular
        algebraic=moments-np.c_[np.zeros(n),t]
        flux=(1+K)*U/(S*sd)
        fv=((self.freq**2-1)*s[:,None]-ell[:,None])*v+s[:,None]*L[:,1:]
        ft=-2*ell[:,None]*t-s[:,None]*(flux@self.dphi.T)/self.angular
        flow=np.c_[fv,ft]
        scales=np.maximum(np.max(abs(quad),axis=1),np.max(abs(t),axis=1))
        relative=np.max(abs(algebraic),axis=1)/np.maximum(scales,1e-300)
        out=dict(flow=flow,algebraic=algebraic,moments=moments,root_relative=relative,
                 minD=float(D.min()),minS=float(S.min()),minA=float(A.min()),
                 maxA=float(A.max()),max_quad=float(abs(quad).max()))
        if not jacobian:return out
        # These derivatives are the literal complete-momentum derivatives of
        # the original engine, now evaluated without solving any Gram system.
        am=Lv+ww*Pt;bm=am+(1+am)*np.expm1(-1.5*np.log1p(-q))
        G=np.eye(self.J)[None]+np.einsum('nq,iq,jq->nij',bm,self.Phi,self.Phi)/self.angular
        omega=1+ww*(Lv+quad)
        FP=E*P*omega/D+2*ww*(1+K)*Pt*P/(S*S*sd)
        FT=-(E*Pt+ww*(1+K)*(ww*P*P+2*K+K*K)/S)/(D*sd)
        C=np.einsum('nq,iq,jq->nij',FP,self.Phi,self.dphi)/self.angular
        C+=np.einsum('nq,iq,jq->nij',FT,self.Phi,self.ddphi)/self.angular
        aj=np.zeros((n,self.J,self.width));aj[:,:,:d]=C
        aj[:,1:,d:2*d]=-np.eye(d)[None];aj[:,:,2*d:]=G
        fj=np.zeros((n,2*d,self.width));j=np.arange(d)
        fj[:,j,j]=(self.freq**2-1)*s[:,None]-ell[:,None]
        fj[:,j,2*d+1+j]=s[:,None];fj[:,d+j,d+j]=-2*ell[:,None]
        def flux_derivative(K1,P1,U1):
            return ((K1[None]*U[:,:,None]+(1+K)[:,:,None]*U1[None])/(S*sd)[:,:,None]
                +flux[:,:,None]*(2*ww[:,:,None]*P[:,:,None]*P1[None]/S[:,:,None]
                  +ww[:,:,None]*((1+K)[:,:,None]*K1[None]+E[:,:,None]*P[:,:,None]*P1[None])/D[:,:,None]))
        dvflux=flux_derivative(-self.ddphi.T,self.dphi.T,((self.freq**2-1)[:,None]*self.dphi).T)
        dlflux=flux_derivative(self.Phi.T,np.zeros((self.angular,self.J)),self.dPhi.T)
        fj[:,d:,:d]=-s[:,None,None]*np.einsum('nqj,iq->nij',dvflux,self.dphi)/self.angular
        fj[:,d:,2*d:]=-s[:,None,None]*np.einsum('nqj,iq->nij',dlflux,self.dphi)/self.angular
        out.update(flow_jacobian=fj,algebraic_jacobian=aj,gram=G)
        return out
