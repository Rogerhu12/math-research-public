"""Relative rotations on the complete R732 disk, including the true negative collar frames."""
import numpy as np
from numpy.polynomial.chebyshev import chebvander,chebder,chebval
from r732_compensated_pulses import H,B0,gate
from r732_closed_ring import angles,line_k
from r732_physical_disk import A,L,W,R0,col,dot,vec,physical_psi,native_w,time_from_x


def apply(M,v):return np.einsum('...ij,...j->...i',M,v)
def trans(a):return np.swapaxes(a,-1,-2)


def rotation(a,axis):
    c=np.cos(a);s=np.sin(a)
    V=np.zeros(a.shape+(3,3),dtype=a.dtype);D=np.zeros_like(V)
    i=(axis+1)%3;j=(axis+2)%3
    V[...,axis,axis]=1.;V[...,i,i]=V[...,j,j]=c;V[...,j,i]=s;V[...,i,j]=-s
    D[...,i,i]=D[...,j,j]=-s;D[...,j,i]=c;D[...,i,j]=-c
    return V,D


def unit(a,d):
    norm=np.linalg.norm(a,axis=-1)
    if np.any(norm<=1.e-15):raise ArithmeticError('degenerate true collar tangent')
    u=a/col(norm)
    return u,(d-col(dot(d,u))*u)/col(norm)


def frames(j):
    _,a,b,aa,ab,bb=j
    n=np.cross(a,b);ds=[]
    for da,db in ((aa,ab),(ab,bb)):
        e,de=unit(a,da);N,dN=unit(n,np.cross(da,b)+np.cross(a,db))
        T=np.cross(N,e)
        ds.append(np.stack((de,np.cross(dN,e)+np.cross(N,de),dN),axis=-1))
    return np.stack((e,T,N),axis=-1),*ds


def product(a,b):
    X,Xx,Xs,Xxx,Xxs,Xss=b
    w,wx,ws,wxx,wxs,wss=map(col,a)
    return (w*X,wx*X+w*Xx,ws*X+w*Xs,
            wxx*X+2*wx*Xx+w*Xxx,wxs*X+wx*Xs+ws*Xx+w*Xxs,
            wss*X+2*ws*Xs+w*Xss)


def collar_jets(build,phase,d,s,actual):
    """Physical (x,sigma) jets in the original ring labels, before any order-one subtraction."""
    ring=build.target(phase);gamma,T,N,k,ks=ring.jets(s)
    _,kind,v=ring.label(s)
    orient=np.where(kind==0,1.,np.where(kind==2,-1.,0.))
    w,wp,wpp=native_w(v)
    w*=abs(orient);wp*=orient;wpp*=abs(orient)
    ks0=np.where(abs(v)<.6,1.,-1.)*np.sign(v)*orient/B0
    p,px,pxx=physical_psi(d,build.order)
    b=w*ks0*p;bx=w*ks0*px;bs=wp*ks0*p;bxx=w*ks0*pxx;bxs=wp*ks0*px;bss=wpp*ks0*p
    speed=1+k*b
    z=np.zeros_like(d)
    out=[vec(W+d,gamma-col(b)*N),vec(np.ones_like(d),-col(bx)*N),vec(z,col(speed)*T-col(bs)*N),
         vec(z,-col(bxx)*N),vec(z,col(k*bx)*T-col(bxs)*N),
         vec(z,col(ks*b+2*k*bs)*T+col(k*speed-bss)*N)]
    if not actual or phase==0:return tuple(out)
    t,gap,td,tdd=time_from_x(d)
    f=1-gate(d/H-1);fx=-gate(d/H-1,1)/H;fxx=-gate(d/H-1,2)/H**2
    pulses=build.pulses(phase)
    for pulse in pulses:
        use=(abs(v)>pulse.lo)&(abs(v)<pulse.hi)&(orient!=0)&(w!=0)
        if not np.any(use):continue
        y=v[use];sg=np.sign(y);dy=sg*orient[use]
        T0,N0=T[use],N[use]
        signs=vec(np.ones_like(sg),np.column_stack((sg,sg)))
        raw=[pulse.raw_delta(t[use],abs(y),i,j)*signs for i,j in ((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))]
        V,Vt,Vy,Vtt,Vty,Vyy=raw
        h=td[use];hh=tdd[use]
        sec=[V,col(h)*Vt,col(dy)*Vy,col(h*h)*Vtt+col(hh)*Vt,col(h*dy)*Vty,Vyy]
        xx=d[use];tt=t[use];sp=np.sqrt(1-16*tt**6/B0**2)
        # Remove the rigidly carried source normal offset from the actual h^4Q.
        # In this expression k and N are those of the new target, the reciprocal k* belongs to the source.
        iw=ks0[use];kt=k[use];kts=ks[use];pd=p[use];pxd=px[use];pxxd=pxx[use]
        base=[vec(gap[use],col(iw*pd)*N0),vec(16*tt**6/(B0**2*sp*(1+sp)),col(iw*pxd)*N0),
              vec(np.zeros_like(xx),-col(iw*pd*kt)*T0),vec(hh,col(iw*pxxd)*N0),
              vec(np.zeros_like(xx),-col(iw*pxd*kt)*T0),
              vec(np.zeros_like(xx),-col(iw*pd*kts)*T0-col(iw*pd*kt**2)*N0)]
        weights=(f[use]*w[use],fx[use]*w[use],f[use]*wp[use],fxx[use]*w[use],fx[use]*wp[use],f[use]*wpp[use])
        corr=product(weights,[a+b for a,b in zip(sec,base)])
        for dst,inc in zip(out,corr):dst[use]+=inc
    return tuple(out)


class Frame:
    def __init__(self,build,phase,r,s,degree):
        r,s=np.broadcast_arrays(np.asarray(r,float),np.asarray(s,float))
        if np.any(r<=0) or np.any(r>1):raise ValueError('use 0<r<=1 for physical Cartesian curl rows')
        self.shape=r.shape;self.r=r.ravel();self.s=s.ravel();self.degree=degree
        r=self.r;s=self.s
        self.j0,angle=build.geometry(r,s)
        phi,phip,_=angle;self.phip=phip;self.phi=phi
        cp=np.cos(phi);sp=np.sin(phi)
        cartx=r*cp;carty=r*sp
        x,u,xr,ur,xrr,urr,ell=build.profile.read(r)
        delta,ds=build.target(phase).angular_data(s)
        # Fade the zero-control angular seed only along the physical final fillet.
        # Every core rotation coefficient remains free, including all three at the disk centre.
        turn=(ell-build.identity.get('fillet_start_ell',A))/L
        rf=np.where(r<=R0,0.,1-gate(turn))
        drf=np.where(r<=R0,0.,gate(turn,1)*np.hypot(xr,ur)/L)
        self.base,V=rotation(rf*delta,0)
        self.br=(drf*delta)[:,None,None]*V
        self.bs=(rf*ds)[:,None,None]*V
        use=(ell<2*H)&(phase!=0)
        if np.any(use):
            j=collar_jets(build,phase,ell[use],s[use],True)
            j0=collar_jets(build,0.,ell[use],s[use],False)
            m,md,ms=frames(j);n,nd,ns=frames(j0)
            self.base[use]=m@trans(n)
            self.br[use]=xr[use,None,None]*(md@trans(n)+m@trans(nd))
            self.bs[use]=build.ring.length*(ms@trans(n)+m@trans(ns))
        envelope=gate(.002+(ell-H)/.025)
        ep=gate(.002+(ell-H)/.025,1)*xr/.025
        # In the only nonconstant envelope zone the profile is the straight collar and x_r=ell_r.
        Bx=chebvander(cartx,degree);By=chebvander(carty,degree)
        Dx=np.column_stack([chebval(cartx,chebder(b)) for b in np.eye(degree+1)])
        Dy=np.column_stack([chebval(carty,chebder(b)) for b in np.eye(degree+1)])
        B=[];Br=[];Bs=[]
        for i in range(degree+1):
            for j in range(degree+1-i):
                v=Bx[:,i]*By[:,j];dx=Dx[:,i]*By[:,j];dy=Bx[:,i]*Dy[:,j]
                B.append(envelope*v);Br.append(ep*v+envelope*(dx*cp+dy*sp))
                Bs.append(envelope*r*phip*(-dx*sp+dy*cp))
        self.B,self.Br,self.Bs=[np.column_stack(g) for g in (B,Br,Bs)]
        self.ncols=3*self.B.shape[1];self.q0=np.zeros(self.ncols)
        self.det=r*phip
        _,ar,as_,*_=self.j0
        dx=col(cp)*ar-col(sp/self.det)*as_;dy=col(sp)*ar+col(cp/self.det)*as_
        self.source_min=float(np.min(np.linalg.svd(np.stack((dx,dy),axis=-1),compute_uv=False)[:,-1]))

    def read(self,q,output=False):
        coef=np.asarray(q).reshape(-1,3)
        ang=self.B@coef;dr=self.Br@coef;ds=self.Bs@coef
        M=self.base;R=self.br;S=self.bs
        for a in range(3):
            V,Vp=rotation(ang[:,a],a);D=M@Vp
            R=R@V+dr[:,a,None,None]*D;S=S@V+ds[:,a,None,None]*D;M=M@V
        _,xr,xs,xrr,xrs,xss=self.j0
        kr=apply(R,xs)-apply(S,xr)
        if not output:return (kr/col(self.det)).reshape(self.shape+(3,))
        data=(kr,apply(M,xr),apply(M,xs),apply(S,xr)+apply(M,xrs),
              apply(R,xr)+apply(M,xrr),apply(S,xs)+apply(M,xss))
        return tuple(v.reshape(self.shape+(3,)) for v in data)

    def curl(self,q):return self.read(q)

    def jac(self,q):
        x=np.asarray(q,dtype=complex);J=np.empty((self.r.size*3,len(x)))
        for i in range(len(x)):
            x[i]+=1.e-24j;J[:,i]=self.curl(x).imag.ravel()/1.e-24;x[i]-=1.e-24j
        return J

