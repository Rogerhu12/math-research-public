"""Invariant reference and finite orbit integration on the full double shoulder."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
from bent_disk_killing_fields import DT,scalar,row,radial_nodes,PAIRS,positive_field

class Target:
    """One cached numerical representation of the Haar integral of the source field.
    The continuum definition is R741 (12)-(13) with the recorded source coefficients.
    """
    def __init__(self,b,cf,cx,parts,half_steps,rtol,margin):
        self.b=b
        self.r=radial_nodes(b.edges,parts)
        self.half_steps=half_steps
        self.cx,self.scale,self.lower=positive_field(b,cx,margin)
        rr=self.r; n=len(rr); m=half_steps
        alpha=np.arange(m+1)*np.pi/m
        def ode(th,y):
            s,J,t,tr=y.reshape(4,n)
            u,w,us,ws=b.vect_at(self.cx,np.clip(s,0.,b.edges[-1]),th)
            if np.any(w<=0.):
                raise ValueError("nonpositive certified angular clock within orbit integration")
            return np.stack((u/w,(us/w-u*ws/w**2)*J,1./w,-ws*J/w**2)).ravel()
        y=np.stack([rr,np.ones(n),np.zeros(n),np.zeros(n)])
        res=solve_ivp(ode,(0.,np.pi),y.ravel(),t_eval=alpha,method="DOP853",
                      rtol=rtol,atol=rtol*.01,max_step=np.pi/min(m,64))
        if not res.success or res.y.shape[1]!=m+1:
            raise ValueError("full orbit integration failed: "+res.message)
        sigma,J,t,tr=res.y.reshape(4,n,m+1)
        if np.min(np.diff(sigma,axis=0))<=0. or np.min(J)<=0.:
            raise ValueError("nonordered numerical orbit chart")
        self.period=2*t[:,-1]
        per=t[:,-1,None];per_r=tr[:,-1,None]
        h=[];ar=[];D=[];er=[];pp=[]
        for k,th in enumerate(alpha):
            so=np.clip(sigma[:,k],0.,b.edges[-1])
            u,w,_,_=b.vect_at(self.cx,so,th)
            d=u/w
            ht=np.pi/(w*per[:,0])
            hr=np.pi*(tr[:,k]-t[:,k]*per_r[:,0]/per[:,0])/per[:,0]
            fj=b.field_at(cf,so,th)
            fs,fa=fj[...,1,:],fj[...,2,:]
            tangent=fa+row(d)*fs
            mer=row(J[:,k])*fs-row(hr/ht)*tangent
            cir=tangent/row(ht)
            h.append(ht);ar.append(hr);D.append(d)
            er.append(scalar(mer,mer)*ht);pp.append(scalar(cir,cir)*ht)
        A=np.trapezoid(np.stack(er,axis=1),x=alpha,axis=1)/np.pi
        P2=np.trapezoid(np.stack(pp,axis=1),x=alpha,axis=1)/np.pi
        if A.min()<=0. or P2.min()<=0.:
            raise ValueError("nonpositive Haar radial profiles")
        self.A,self.P2=A,P2
        components=[]
        for k in range(m+1):
            bs=1./J[:,k];bt=-D[k]*bs
            ps=ar[k]*bs;pt=h[k]+ar[k]*bt
            E=A*bs**2+P2*ps**2
            F=A*bs*bt+P2*ps*pt
            G=A*bt**2+P2*pt**2
            spatial=np.clip(sigma[:,k],0.,b.edges[-1])
            vals=np.stack([np.log(np.maximum(E-F*F/G,1e-20)),F/G,np.log(G)],axis=1)
            components.append(CubicSpline(spatial,vals,axis=0)(rr))
        half=np.stack(components,axis=1)
        half[:,[0,-1],1]=0.
        other=half[:,-2:0:-1].copy();other[...,1]*=-1
        self.table=np.concatenate([half,other],axis=1)
        self.coeff=CubicSpline(rr,np.fft.rfft(self.table,axis=1)/self.table.shape[1],axis=0)
        self.report={"ode_calls":int(res.nfev),"samples":[n,2*m],"period_range":[float(self.period.min()),float(self.period.max())],
                     "min_variational_derivative":float(J.min()),"min_label_spacing":float(np.diff(sigma,axis=0).min()),
                     "positive_clock_scale":float(self.scale),"positive_clock_control_lower":float(self.lower),
                     "radial_E_interval":[float(A.min()),float(A.max())],"radial_P2_interval":[float(P2.min()),float(P2.max())]}
    def values(self,s,a):
        f=self.coeff(s);n=self.table.shape[1]
        e=np.exp(1j*np.arange(f.shape[1])[:,None]*np.asarray(a)[None,:])
        e[1:-1]*=2.
        v=np.einsum("rkc,ka->rac",f,e,optimize=True).real
        a1,q,g=np.exp(v[...,0]),v[...,1],np.exp(v[...,2])
        return a1+q*q*g,q*g,g
