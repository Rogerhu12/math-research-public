"""R701's actual material circle, signed mass, full physical two-jets, and scalar merit."""
from __future__ import annotations
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import BSpline
from r703_transported_lattice_anchor import wave


class Rad:
    """Value and first two (unnormalized) true radial derivatives at fixed auxiliary angle."""
    def __init__(self,x,d=0,dd=0):self.x,self.d,self.dd=x,d,dd
    @staticmethod
    def cast(x):return x if isinstance(x,Rad) else Rad(x)
    def __add__(self,y):
        y=self.cast(y);return Rad(self.x+y.x,self.d+y.d,self.dd+y.dd)
    __radd__=__add__
    def __neg__(self):return Rad(-self.x,-self.d,-self.dd)
    def __sub__(self,y):return self+-self.cast(y)
    def __rsub__(self,y):return -self+y
    def __mul__(self,y):
        y=self.cast(y);return Rad(self.x*y.x,self.d*y.x+self.x*y.d,self.dd*y.x+2*self.d*y.d+self.x*y.dd)
    __rmul__=__mul__
    def apply(self,f,fp,fpp):
        return Rad(f(self.x),fp(self.x)*self.d,fp(self.x)*self.dd+fpp(self.x)*self.d*self.d)
    def power(self,p):return self.apply(lambda x:x**p,lambda x:p*x**(p-1),lambda x:p*(p-1)*x**(p-2))
    def __truediv__(self,y):return self*self.cast(y).power(-1)
    def __rtruediv__(self,y):return self.power(-1)*y
    def sin(self):return self.apply(np.sin,np.cos,lambda a:-np.sin(a))
    def cos(self):return self.apply(np.cos,lambda a:-np.sin(a),lambda a:-np.cos(a))
    def transform(self,f):return Rad(*(f(np.asarray(a)) if np.ndim(a)>0 else a for a in (self.x,self.d,self.dd)))
    def col(self):return self.transform(lambda x:x[...,None])
    def avg(self):return self.transform(lambda x:x.mean(axis=1,keepdims=True))


def dot(a,b):return np.sum(a*b,axis=-1)
def rdot(a,b):return (a*b).transform(lambda v:np.sum(v,axis=-1))
def rcross(a,b):
    return Rad(np.cross(a.x,b.x),np.cross(a.d,b.x)+np.cross(a.x,b.d),
               np.cross(a.dd,b.x)+2*np.cross(a.d,b.d)+np.cross(a.x,b.dd))


def spectral(v,derivative=False):
    def realop(x):
        M=x.shape[1];k=np.arange(M//2+1);z=np.fft.rfft(x,axis=1)
        op=1j*k if derivative else 1/(1j*np.where(k,k,1));op[0]=0
        return np.fft.irfft(z*op.reshape((1,-1)+(1,)*(x.ndim-2)),n=M,axis=1)
    return realop(v.real)+1j*realop(v.imag) if np.iscomplexobj(v) else realop(v)


def weighted_I(f,J):
    w=J if f.ndim==2 else J[...,None]
    mean=(f*w).mean(axis=1,keepdims=True)
    p=spectral((f-mean)*w)
    return p-(p*w).mean(axis=1,keepdims=True),mean


def take_rad(table,j):return Rad(*(table[i,j] for i in range(3)))


class Space:
    def __init__(self,spans,modes):
        self.spans,self.K=spans,modes;self.edges=np.linspace(.075,.22,spans+1)
        self.knots=np.r_[[.075]*5,self.edges,[.22]*5];self.nb=len(self.knots)-6
        self.spl=BSpline(self.knots,np.eye(self.nb),5);self.na=self.nb-6
        self.size=modes*self.na+(modes+1)*self.nb
    def split(self,x):return x[:self.K*self.na].reshape(self.K,self.na),x[self.K*self.na:].reshape(self.K+1,self.nb)
    def frozen_columns(self):
        mask=np.ones(self.size,bool);mask[self.K*self.na:self.K*self.na+self.nb]=False
        return np.flatnonzero(mask)
    def prolong(self,old,x):
        o1,o2=old.split(x);out=np.zeros(self.size);n1,n2=self.split(out)
        if self.spans%old.spans or self.K<old.K:raise ValueError('Nested material coordinates required.')
        for a,b,pad in ((o1,n1,3),(o2,n2,0)):
            for j,row in enumerate(a):
                curve=BSpline(old.knots,np.pad(row,pad),5)
                for i,pos in enumerate(self.edges[1:-1],1):
                    if i%(self.spans//old.spans):curve=curve.insert_knot(pos)
                b[j]=curve.c[pad:-pad] if pad else curve.c
        return out
    def grid(self,g):
        mats=[self.spl(g.r,i) for i in range(3)]
        def bank(odd):
            ids=range(int(odd),self.K+1)
            return [np.array([wave(g.phi,m,odd,j) for m in ids]) for j in range(3)]
        return mats,bank(True),bank(False)


class Field:
    def __init__(self,space,g):
        self.sp,self.g=space,g;self.mats,self.ws,self.wc=space.grid(g)
        if 'reflection' in g.anchor:
            ref=SimpleNamespace(r=g.r,phi=np.array([np.pi]),anchor=g.anchor['reflection'])
            self.pi=Field(space,ref)
    def jets(self,x,old_slope=False):
        cf,cb=self.sp.split(x);g=self.g;anc=g.anchor
        def make(co,odd,j):
            return Rad(*[((m[:,3:-3] if odd else m)@co.T)@(self.ws if odd else self.wc)[j] for m in self.mats])
        f,fp,fpp=[make(cf,True,j) for j in range(3)]
        co,si=f.cos(),f.sin();T0,U0=take_rad(anc['T'],0),take_rad(anc['B'],0)
        T1,U1=take_rad(anc['T'],1),take_rad(anc['B'],1)
        T2,U2=anc['T'][0,2],anc['B'][0,2]
        T=co.col()*T0+si.col()*U0;V=(-si).col()*T0+co.col()*U0
        Tp=fp.col()*V+co.col()*T1+si.col()*U1
        Tpp=(fpp.x[...,None]*V.x-fp.x[...,None]**2*T.x
             +2*fp.x[...,None]*(-si.x[...,None]*T1.x+co.x[...,None]*U1.x)+co.x[...,None]*T2+si.x[...,None]*U2)
        v=rdot(Tp,Tp).power(.5)
        if not np.all(np.isfinite(v.x)) or np.min(v.x.real)<=.08:raise FloatingPointError('Nonregular actual tangent indicatrix.')
        U=Tp/v.col();B=rcross(T,U)
        vp=dot(U.x,Tpp);Up=(Tpp-vp[...,None]*U.x)/v.x[...,None];Bp=np.cross(T.x,Up)
        beta=Rad(*(w[:,None] for w in anc['beta']))
        base=anc['old_b'] if old_slope else anc['b']
        delta=make(cb,False,0);dp=make(cb,False,1)
        b=take_rad(base,0)+beta*delta
        bp=base[0,1]+beta.x*dp.x
        # The true b/beta limit on both rims is evaluated from the transported source, with the full free even row.
        mask=beta.x[:,0]==0
        safe_beta=beta.transform(lambda z:z.copy())
        safe_beta.x[mask]=1.;safe_beta.d[mask]=0.;safe_beta.dd[mask]=0.
        normalized=b/safe_beta
        normalized.x[mask]=anc['M']*(1.01+np.cos(g.phi))+delta.x[mask]
        normalized.d[mask]=0.;normalized.dd[mask]=0.
        return dict(T=T,Tp=Tp,Tpp=Tpp,U=U,B=B,v=v,vp=vp,Up=Up,Bp=Bp,b=b,bp=bp,beta=beta,s=normalized,mask=mask)

    def length_excess(self,j):
        # Evaluate the same finite integration-by-parts surrogate and all its radial jets.
        g=self.g;c=np.cos(g.phi)[None,:];s=np.sin(g.phi)[None,:]
        q=Rad(*(t[:,None] for t in g.anchor['q_jets']));ca=q.cos();sa=q.sin()
        T=j['T'];Tp=j['Tp'];v=j['v'];safe=j['beta'].transform(lambda z:z.copy())
        for t,fill in ((safe.x,1.),(safe.d,0.),(safe.dd,0.)):t[j['mask']]=fill
        # Work componentwise so constant y-components have exact zero radial derivatives.
        td=[T.transform(lambda z,k=k:z[...,k])-y for k,y in enumerate((ca*(-s),c,sa*s))]
        pd=[Tp.transform(lambda z,k=k:z[...,k])-y for k,y in enumerate((ca*(-c),-s,sa*c))]
        mag=sum(w*w for w in pd)
        vminus=(2*sum(a*u for a,u in zip(pd,(ca*(-c),-s,sa*c)))+mag)/(v+1)
        val=.5*(sum((a/safe)*(a/safe)-(b/safe)*(b/safe) for a,b in zip(pd,td))-(vminus/safe)*(vminus/safe)).avg()
        for t in (val.x,val.d,val.dd):t[j['mask']]=0.
        return val

    def mass(self,j,reference,zbase):
        beta,s,v=j['beta'],j['s'],j['v'];B=beta.x;S=s.x;V=v.x;mask=j['mask']
        target_jet=reference['scaled_gap']+self.length_excess(j);target=target_jet.x
        if np.min(target.real)<=0:raise FloatingPointError('Frozen positive fourth-order mass gap lost.')
        def val(z):
            sq=np.sqrt(1+z*B**2*S**2)
            return z*np.mean(V*S*S/(sq*(1+sq)),axis=1,keepdims=True)
        if zbase is None:
            lo=np.zeros_like(target.real);hi=np.ones_like(lo)
            for _ in range(42):
                need=val(hi).real<target.real
                if not np.any(need):break
                hi=np.where(need,hi*2,hi)
            if np.any(val(hi).real<target.real):raise FloatingPointError('No finite positive mass bracket.')
            for _ in range(57):
                mid=(lo+hi)/2;ll=val(mid).real<target.real;lo=np.where(ll,mid,lo);hi=np.where(ll,hi,mid)
            root=(lo+hi)/2
        else:root=zbase
        z=root.astype(np.result_type(target,V),copy=True)
        for _ in range(2):
            dz=.5*np.mean(V*S*S/(1+z*B**2*S**2)**1.5,axis=1,keepdims=True);z=z-(val(z)-target)/dz
        # Value, two radial derivatives and parameter columns solve this very same discrete equation.
        # On the rims only z itself enters either physical jet, since b=b_r=0.
        zr=Rad(z,np.zeros_like(z),np.zeros_like(z))
        for _ in range(2):
            sq=(1+zr*beta*beta*s*s).power(.5)
            f=zr*(v*s*s/(sq*(1+sq))).avg()-target_jet
            deriv=.5*(v*s*s/(sq*sq*sq)).avg()
            f.x=np.zeros_like(z);f.d[mask]=0.;f.dd[mask]=0.
            zr=zr-f/deriv
        if np.min(dz.real)<=0 or not np.all(np.isfinite(zr.dd)):raise FloatingPointError('Frozen mass derivative lost.')
        return zr.power(.5),root,float(np.min(dz.real)),float(np.max(abs(val(z)-target)))

    def state(self,x,level,reference=None,zbase=None,old_slope=False):
        g=self.g;j=self.jets(x,old_slope);r=g.r[:,None];T,Tp,Tpp=j['T'],j['Tp'],j['Tpp'];v,U,B=j['v'],j['U'],j['B']
        b,bp=j['b'],j['bp'];root=None;mass_margin=None;mass_error=None
        if reference is not None:
            if level!=1:raise ValueError('A frozen physical target requires the radial stage.')
            scale,root,mass_margin,mass_error=self.mass(j,reference,zbase);b=b*scale;bp=bp*scale.x
        W=v/(1+b*b).power(.5);wp=j['vp']/np.sqrt(1+b.x*b.x)-W.x*b.x*bp/(1+b.x*b.x)
        m=1/W.avg()
        target_m=m if reference is None else 1/reference['meanW']
        raw_errors=[0.,0.,0.]
        if reference is not None:
            raw=W.avg()-reference['meanW'];span=g.b-g.a
            raw_errors=[float(np.max(abs(t))*span**k) for k,t in enumerate((raw.x,raw.d,raw.dd))]
            if any(e>tol for e,tol in zip(raw_errors,(5.e-11,5.e-10,5.e-8))):
                raise FloatingPointError(f'Frozen raw mean value or scaled radial jets exceed tolerance: {raw_errors}')
        if level<1:
            jp=self.pi.jets(x,old_slope);Wpi=jp['v'].x/np.sqrt(1+jp['b'].x**2)
            e_meridians=(1-level)/np.column_stack((W.x[:,0],Wpi[:,0]))+level*m.x
        else:
            e_meridians=np.repeat(target_m.x,2,axis=1)
        J=1-level+level*W*m
        if np.min(J.x.real)<.05:raise FloatingPointError('Actual material angle Jacobian lost.')
        Jp=level*m.x*wp;e=J/W;ell=J/v
        D=ell.col()*((-U)+b.col()*B)
        Dp=(((Jp-ell.x*j['vp'])/v.x)[...,None]*(-U.x+b.x[...,None]*B.x)
            +ell.x[...,None]*(-j['Up']+bp[...,None]*B.x+b.x[...,None]*j['Bp']))
        def from_zero(y):
            p=spectral(y);return p-p[:,0:1]
        angle=g.phi[None,:]+from_zero(J.x-1);pr=from_zero(J.d);prr=from_zero(J.dd)
        gam=pr/J.x;gp=(J.d-gam*Jp)/J.x;gr=(prr-gam*J.d)/J.x
        Tr=T.d-gam[...,None]*Tp.x
        Trr=T.dd-2*gam[...,None]*Tp.d+gam[...,None]**2*Tpp+(gam*gp-gr)[...,None]*Tp.x
        G=Dp/J.x[...,None]-T.x-r[...,None]*Tr
        C0=(D.x*J.x[...,None]).mean(axis=1);C1=(D.d*J.x[...,None]+D.x*J.d[...,None]).mean(axis=1)
        C=g.integral@C0
        A,meanT=weighted_I(T.x,J.x);Ar,meanTr=weighted_I(Tr,J.x);Arr,_=weighted_I(Trr,J.x)
        H=T.x-meanT;dr=C0[:,None,:]+A+r[...,None]*Ar
        sh=[C[:,None,:]+r[...,None]*A,dr,H,C1[:,None,:]+2*Ar+r[...,None]*Arr,
            (H+r[...,None]*(Tr-meanTr))/r[...,None],Tp.x/(r*J.x)[...,None]]
        # The native finite angular interpolant has its own two-jet at fixed material angle.
        mean_r=(T*J.col()).avg()
        prim=((T-mean_r)*J.col()).transform(spectral)
        ai=prim-(prim*J.col()).avg()
        ap=spectral(ai.x,True);app=spectral(ap,True);arp=spectral(ai.d,True)
        ajp=spectral(J.x,True);gpi=(J.d-gam*ajp)/J.x
        ar=ai.d-gam[...,None]*ap
        arr=ai.dd-2*gam[...,None]*arp+gam[...,None]**2*app+(gam*gpi-gr)[...,None]*ap
        C0i=g.c_value@C0;C1i=g.c_derivative@C0
        shi=[sh[0],C0i[:,None,:]+ai.x+r[...,None]*ar,ap/J.x[...,None],
             C1i[:,None,:]+2*ar+r[...,None]*arr,
             (ap+r[...,None]*(arp-gpi[...,None]*ap-gam[...,None]*app))/(r*J.x)[...,None],
             (app-ap*(ajp/J.x)[...,None])/(r*J.x**2)[...,None]]
        # At shared radial knots the actual finite center anti-derivative is only piecewise polynomial.
        # Keep the other one-sided slope and acceleration for its independent two-jet hard gate.
        ei=g.edge_ids;left=[v[ei].copy() for v in shi]
        left[1]+=(g.left_value@C0-C0i[ei])[:,None,:]
        left[3]+=(g.left_derivative@C0-C1i[ei])[:,None,:]
        return dict(j=j,G=G,Ur=U.x,Br=B.x,e=e.x,e0=target_m.x[:,0],meridian_e=e_meridians,sampled_raw_mass_errors=raw_errors,J=J.x,angle=angle,F=sh,Fi=shi,Fi_left=left,C=C,C0=C0,C1=C1,
                    virtual=D.x,root=root,closure=meanT[:,0,:],material_change=angle-g.phi[None,:],
                    mass_margin=mass_margin,mass_error=mass_error,Tp=Tp.x,source_b=b.x)


def frozen_for(reference_field,reference_x):
    j=reference_field.jets(reference_x);b,s,v=j['b'],j['s'],j['v'];cc=(1+b*b).power(.5)
    W=v/cc;K=(v*s*s/(cc*(1+cc))).avg()
    return dict(meanW=W.avg(),scaled_gap=K-reference_field.length_excess(j),slope_mean=s.x.mean(axis=1))
