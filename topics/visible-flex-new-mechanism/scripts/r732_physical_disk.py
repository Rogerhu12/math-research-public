"""Actual R732 right source disk, with a regular Cartesian disk centre and true cap jets."""
import numpy as np
from r688_actual_r664_window_collars import quadrature, mollifier_cdf, require_public
from r688_true_caps_and_reference_sections import sym_step
from r732_compensated_pulses import B0,H,Pulse,gate
from r732_closed_ring import Ring,angles


W,A,L,R0,EPS,DU=.27,.52,.174,.35,.004,.0005
ANGULAR_KNOTS=(0.,.0005,.0015,.9985,.9995,1.)


def col(a):return np.asarray(a)[...,None]


def dot(a,b):return np.sum(a*b,axis=-1)


def vec(x,q):return np.concatenate((col(x),q),axis=-1)


def native_w(v):
    """Cutoff w and two derivatives in v on both basal constant-curvature pulses."""
    v=np.asarray(v);shape=v.shape;v,inv=np.unique(v.ravel(),return_inverse=True)
    r=abs(v);out=[np.zeros_like(r) for i in range(3)]
    for c in (.206,.847):
        a=(r-(c-.0005))/.0002; b=((c+.1005)-r)/.0002
        out[0]+=gate(a)*gate(b)
        out[1]+=(gate(a,1)*gate(b)-gate(a)*gate(b,1))/.0002
        out[2]+=(gate(a,2)*gate(b)-2*gate(a,1)*gate(b,1)+gate(a)*gate(b,2))/.0002**2
    out[1]*=np.sign(v)
    return tuple(x[inv].reshape(shape) for x in out)


def time_from_x(d):
    """The true source ray; t-x is evaluated before rounding when used as a correction."""
    d=np.asarray(d)
    q,w=quadrature(12)
    t=d.copy()
    c=16/B0**2
    for i in range(2):
        z=(q+1)*t[...,None]/2
        gap=(t/2)*((c*z**6/(1+np.sqrt(1-c*z**6)))@w)
        t=d+gap
    speed=np.sqrt(1-c*t**6)
    return t,gap,1/speed,3*c*t**5/speed**4


def physical_psi(d,order):
    d=np.asarray(d);shape=d.shape;d,inv=np.unique(d.ravel(),return_inverse=True)
    dsmall=np.clip(d,0.,3*H)
    t,_,td,tdd=time_from_x(dsmall)
    p=t**4;dp=4*t**3*td;dd=12*t**2*td**2+4*t**3*tdd
    mask=d>3*H
    if np.any(mask):
        x=d[mask];b=np.minimum(x,4*H);z=(b-3*H)/2
        q,w=quadrature(order)
        a=3*H+z[:,None]*(1+q)
        t,_,td,tdd=time_from_x(a)
        G=gate((a-3*H)/H)
        acc=(1-G)*(12*t*t*td*td+4*t**3*tdd)+G*H**3
        v0=dp[mask]
        p[mask]+=v0*(x-3*H)+z*((acc*(x[:,None]-a))@w)+.5*H**3*(x-b)**2
        dp[mask]+=z*(acc@w)+H**3*(x-b)
        t,_,td,tdd=time_from_x(b)
        G=gate((b-3*H)/H)
        dd[mask]=(1-G)*(12*t*t*td*td+4*t**3*tdd)+G*H**3
    mask=d<0
    for a in (p,dp,dd):a[mask]=0.
    g=1-gate((d-A)/.01);gp=-gate((d-A)/.01,1)/.01;gpp=-gate((d-A)/.01,2)/.01**2
    return tuple(x[inv].reshape(shape) for x in (p*g,dp*g+p*gp,dd*g+2*dp*gp+p*gpp))


class Profile:
    def __init__(self,order):
        self.order=order
        self.nodes=L*np.array(ANGULAR_KNOTS)
        inc=[self.inc(a,b) for a,b in zip(self.nodes,self.nodes[1:])]
        self.prefix=np.r_[np.zeros((1,2)),np.cumsum(inc,axis=0)]
        self.ub=self.prefix[-1,1];self.endx=W+A+self.prefix[-1,0]

    def inc(self,a,b):
        z=(np.atleast_1d(b)-a)/2
        q,w=quadrature(self.order)
        th=(np.pi/2)*sym_step((a+z[:,None]*(1+q))/L)
        P=z[:,None]*np.column_stack((np.cos(th)@w,np.sin(th)@w))
        return P[0] if np.ndim(b)==0 else P

    def read(self,r):
        r=np.asarray(r);shape=r.shape;r,inv=np.unique(r.ravel(),return_inverse=True)
        t=np.clip((r-R0)/(1-R0),0.,1.)
        c=DU*(1-R0)/R0; h=A+L-c
        # Signed material distance from the true ring, stable at r=1.
        ell=(1-t)*(c+h*(1+t+t*t))
        de=-(c+3*h*t*t)/(1-R0); dde=-6*h*t/(1-R0)**2
        u=np.zeros_like(r);x=W+ell;th=np.zeros_like(r);k=np.zeros_like(r)
        curve=ell>A
        if np.any(curve):
            z=np.clip(ell[curve]-A,0,L)
            nodes,ix=np.unique(z,return_inverse=True); ids=np.minimum(np.searchsorted(self.nodes,nodes,side='right')-1,4)
            P=np.empty((len(nodes),2))
            for i in np.unique(ids):
                use=ids==i;P[use]=self.prefix[i]+self.inc(self.nodes[i],nodes[use])
            x[curve]=W+A+P[ix,0];u[curve]=P[ix,1]
            y=z/L
            th[curve]=(np.pi/2)*sym_step(y)
            k[curve]=(np.pi/2)*(mollifier_cdf((y-.001)/.0005)-mollifier_cdf((y-.999)/.0005))/(.998*L)
        xr=np.cos(th)*de;ur=np.sin(th)*de
        xrr=np.cos(th)*dde-np.sin(th)*k*de**2
        urr=np.sin(th)*dde+np.cos(th)*k*de**2
        return tuple(z[inv].reshape(shape) for z in (x,u,xr,ur,xrr,urr,ell))


class Build:
    def __init__(self,baseline=.100,modes=8192,steps=12,order=40):
        require_public()
        if baseline!=.100 or modes<128 or steps<6 or order<12:raise ValueError('fixed R732 physical input')
        self.baseline=baseline;self.modes=modes;self.steps=steps;self.order=order
        self.rings={0.:Ring(0.,order)};self.pulse_cache={};self.profile=Profile(order)
        self.ring=self.rings[0.]
        self.identity=dict(baseline=baseline,modes=modes,steps=steps,order=order,
                           W=W,a=A,round_length=L,core_R=R0,core_rad=EPS,core_collar=DU,
                           pulse_h=H,section_length=self.ring.length)

    def target(self,phase):
        key=float(phase)
        if key not in self.rings:self.rings[key]=Ring(key,self.order)
        return self.rings[key]

    def pulses(self,phase):
        key=float(phase)
        if key not in self.pulse_cache:
            self.pulse_cache[key]=[Pulse(key,c,sgn,angles,self.modes,self.steps) for c,sgn in ((.206,1.),(.847,-1.))]
        return self.pulse_cache[key]

    def geometry(self,r,s):
        """P,P_r,P_s,P_rr,P_rs,P_ss; s is normalized arclength of the given ring."""
        r,s=np.broadcast_arrays(r,s);shape=r.shape;r=r.ravel();s=s.ravel()
        gamma,T,N,k,ks=self.ring.jets(s)
        perimeter=self.ring.length;origin=self.ring.origin
        x,u,xr,ur,xrr,urr,ell=self.profile.read(r)
        d,kind,v=self.ring.label(s)
        w,wp,wpp=native_w(v)
        orientation=np.where(kind==0,1.,np.where(kind==2,-1.,0.))
        w*=abs(orientation);wp*=orientation;wpp*=abs(orientation)
        sign=np.where(abs(v)<.6,1.,-1.)*np.sign(v)*orientation
        inv=sign/B0
        # For the straight collar use ell, not (W+ell)-W, even for original source jets.
        phys=np.where(ell<=A,ell,x-W)
        psi,px,pxx=physical_psi(phys,self.order)
        b=w*inv*psi; br=w*inv*px*xr;bs=wp*inv*psi
        brr=w*inv*(pxx*xr*xr+px*xrr);brs=wp*inv*px*xr;bss=wpp*inv*psi
        U=u+b;Ur=ur+br;Urr=urr+brr;speed=1+k*U
        P=vec(x,gamma-col(U)*N)
        Pr=vec(xr,-col(Ur)*N)
        Ps=vec(np.zeros_like(r),col(speed)*T-col(bs)*N)
        Prr=vec(xrr,-col(Urr)*N)
        Prs=vec(np.zeros_like(r),col(k*Ur)*T-col(brs)*N)
        Pss=vec(np.zeros_like(r),col(ks*U+2*k*bs)*T+col(k*speed-bss)*N)
        # The upper side advances in Y and the far U turns downward: this material circle is clockwise.
        B=gamma-col(np.full_like(r,self.profile.ub))*N-origin
        Bp=col(1+k*self.profile.ub)*T
        Bpp=col(ks*self.profile.ub)*T+col(k*(1+k*self.profile.ub))*N
        rad=np.linalg.norm(B,axis=-1);e=B/col(rad);et=np.column_stack((-e[:,1],e[:,0]))
        phi=np.arctan2(e[:,1],e[:,0]);phip=dot(Bp,et)/rad
        phipp=(dot(Bpp,et)-2*dot(Bp,e)*phip)/rad
        if np.max(phip)>=0:raise ArithmeticError('source cap clockwise polar label lost support')
        mask=r<R0
        if np.any(mask):
            y=r[mask]/R0
            f=gate((y-.25)/.50);fr=gate((y-.25)/.50,1)/(.50*R0);frr=gate((y-.25)/.50,2)/(.50*R0)**2
            uu=self.profile.ub+DU*(1-y)
            outer=gamma[mask]-col(uu)*N[mask]-origin
            os=col(1+k[mask]*uu)*T[mask]
            oss=col(ks[mask]*uu)*T[mask]+col(k[mask]*(1+k[mask]*uu))*N[mask]
            orr=DU/R0*N[mask];ors=-DU/R0*col(k[mask])*T[mask]
            low=col(EPS*y)*e[mask];lr=EPS/R0*e[mask]
            es=col(phip[mask])*et[mask]
            ess=col(phipp[mask])*et[mask]-col(phip[mask]**2)*e[mask]
            ls=col(EPS*y)*es;lrs=EPS/R0*es;lss=col(EPS*y)*ess
            gap=outer-low
            P[mask]=vec(np.full_like(y,self.profile.endx),origin+low+col(f)*gap)
            Pr[mask]=vec(np.zeros_like(y),lr+col(fr)*gap+col(f)*(orr-lr))
            Ps[mask]=vec(np.zeros_like(y),ls+col(f)*(os-ls))
            Prr[mask]=vec(np.zeros_like(y),col(frr)*gap+2*col(fr)*(orr-lr))
            Prs[mask]=vec(np.zeros_like(y),lrs+col(fr)*(os-ls)+col(f)*(ors-lrs))
            Pss[mask]=vec(np.zeros_like(y),lss+col(f)*(oss-lss))
        jets=P,Pr,perimeter*Ps,Prr,perimeter*Prs,perimeter**2*Pss
        return tuple(a.reshape(shape+(3,)) for a in jets),(phi.reshape(shape),(perimeter*phip).reshape(shape),(perimeter**2*phipp).reshape(shape))

    def boundary_jets(self,phase,s):
        P,T,N,k,_=self.target(phase).jets(s);per=self.ring.length
        z=np.zeros_like(k)
        return vec(np.full_like(k,W),P),vec(z,per*T),vec(z,per**2*col(k)*N)

    def radius_at(self,ell):
        ell=np.asarray(ell);lo=np.zeros_like(ell,dtype=float);hi=np.ones_like(lo)
        c=DU*(1-R0)/R0; h=A+L-c
        for unused in range(54):
            mid=(lo+hi)/2;gap=(1-mid)*(c+h*(1+mid+mid*mid))
            lo=np.where(gap>ell,mid,lo);hi=np.where(gap>ell,hi,mid)
        return R0+(1-R0)*(lo+hi)/2

    def nodes(self,level,purpose):
        """Finite training, independent validation, or physical qualification selections."""
        if purpose not in ('train','validation','qualification'):raise ValueError('R732 node purpose')
        n=max(1,int(level)); shift={'train':.5,'validation':.319,'qualification':.173}[purpose]
        radial=list((np.arange(5+3*n)+shift)/(5+3*n))
        radial.extend([R0*.09,R0*.25,R0*.50,R0*.75,R0,1.])
        radial.extend(self.radius_at(np.r_[H*np.array([.27,.73,1.,1.45,2.,3.7]),.018,.30,A,
                                              A+L*np.array([.0008,.0012,.25,.50,.75,.9988,.9992])]))
        length=self.ring.length; lu=self.ring.LU
        signed=list((np.arange(10+3*n)+shift)/(10+3*n))
        for c,w in ((.205,.102),(.206,.100),(.846,.102),(.847,.100)):
            # All four true pulse start/end ramps in each primary, with independent interior offsets.
            q=.0005+shift*.001
            points=c+w*np.array([q,.5,1-q])
            if purpose!='train':points=np.r_[points,c-.0004,c+.0001,c+.1004]
            signed.extend(points)
        v=np.unique(np.r_[-np.asarray(signed),0.,signed])
        s=[(v+1)/length,(3+lu-v)/length]
        upts=np.r_[0.,.0005+.001*shift,(np.arange(4+n)+shift)/(4+n),.9995-.001*shift]
        s.extend([(2+upts*lu)/length,(4+lu+upts*lu)/length])
        return np.unique(np.clip(radial,1.e-10,1.)),np.unique(np.r_[0.,np.mod(np.concatenate(s),1.)])

    @property
    def seed_identity(self):
        import hashlib
        import json
        from pathlib import Path
        here=Path(__file__).resolve().parent
        files=['r732_physical_disk.py','r732_closed_ring.py','r732_compensated_pulses.py','r732_disk_fields.py',
               'r688_actual_r664_window_collars.py','r688_true_caps_and_reference_sections.py']
        return {**self.identity,'physics_sha256':{p:hashlib.sha256((here/p).read_bytes()).hexdigest() for p in files}}


