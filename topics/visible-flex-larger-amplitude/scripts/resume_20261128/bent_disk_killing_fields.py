#!/usr/bin/env python3
"""Physical two-jet fields and a boundary-clamped material Killing solve."""
import numpy as np
from scipy.interpolate import BSpline
from scipy.sparse.linalg import LinearOperator, lsmr

PAIRS=((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))
DT=2*np.pi

def scalar(x,y):
    return np.einsum("...i,...i->...",x,y)

def row(coeff):
    return coeff[...,None]

def s7(v):
    t=np.clip(v,0.,1.)
    return t**4*(35+t*(-84+t*(70-20*t)))

def span_edges(d,base,extra):
    return np.array([0.,base.A_LENGTH,base.A_LENGTH+d.join+extra,d.length+extra])

def radial_nodes(edges,parts):
    return np.concatenate([edges[k]+.5*(1-np.cos(np.pi*np.arange(n)/(n-1)))*(edges[k+1]-edges[k])
                    if k==0 else edges[k]+.5*(1-np.cos(np.pi*np.arange(1,n)/(n-1)))*(edges[k+1]-edges[k])
                    for k,n in enumerate(parts)])

def original(jet,d,extra,s,theta):
    # S(a)=a+extra*S7((a-A)/join), a genuine common material change.
    # Its positive derivative is one and its second derivative zero on both seams.
    abase=jet.base.A_LENGTH
    s,theta=np.broadcast_arrays(s,theta)
    q=(s-abase)/(d.join+extra)
    lo=np.zeros_like(s);hi=np.ones_like(s)
    for _ in range(49):
        v=(lo+hi)/2
        less=d.join*v+extra*s7(v)<s-abase
        lo=np.where(less,v,lo);hi=np.where(less,hi,v)
    t=np.where(q<=0.,0.,np.where(q>=1.,1.,(lo+hi)/2))
    a=np.where(q<=0.,s,np.where(q>=1.,s-extra,abase+d.join*t))
    a=np.clip(a,0.,d.length)
    g=t*(1-t)
    v=1.+extra*140*g**3/d.join
    acc=extra*420*g*g*(1-2*t)/d.join**2
    z=jet.shoulder_jet(a,theta,design=d,normalized=False)
    z[...,3,:]=z[...,3,:]/row(v*v)-z[...,1,:]*row(acc/v**3)
    z[...,1,:]/=row(v);z[...,4,:]/=row(v)
    return z

def transform(n,kind):
    # Nonnegative open quintic controls. Each constrained row is exactly
    # zero or a copied free row, except the odd-reflection acceleration row.
    full=np.eye(n)
    if kind=="z":
        return full[:,3:-3]
    if kind in ("x","y","W"):
        t=full[:,3:-1].copy()
        t[-1]=t[-2]
        return t
    # U=0,U_ss=0 at the equator. For last knot widths h1,h2,
    # spline endpoint second derivative is proportional to
    # (c_n-c_{n-1})/h1 - (c_{n-1}-c_{n-2})/(h1+h2).
    raise ValueError(kind)

class Space:
    def __init__(self,edges,parts,mode,kind):
        cuts=np.concatenate([np.linspace(edges[k],edges[k+1],n+1) if k==0 else
                             np.linspace(edges[k],edges[k+1],n+1)[1:] for k,n in enumerate(parts)])
        knots=np.r_[np.repeat(cuts[0],5),cuts,np.repeat(cuts[-1],5)]
        n=len(knots)-6
        if kind=="U":
            # c_last=0 and c_{last-2}=(2+hprev/hlast)c_{last-1}.
            t=np.eye(n)[:,3:-2].copy()
            h,prev=cuts[-1]-cuts[-2],cuts[-2]-cuts[-3]
            t[-2]=t[-3]/(2.+prev/h)
        else:
            t=transform(n,kind)
        self.spl=BSpline(knots,t,5)
        self.full_controls=t
        self.odd=kind in ("y","U")
        self.freq=np.arange(1 if self.odd else 0,mode+1)
        self.shape=(t.shape[1],len(self.freq));self.n=int(np.prod(self.shape))
    def angle(self,a,k):
        p=np.asarray(a)[:,None]*self.freq+k*np.pi/2
        return (np.sin(p) if self.odd else np.cos(p))*self.freq**k
    def tables(self,s,a):
        return ([self.spl(s,nu=j) for j in range(3)],[self.angle(a,k) for k in range(3)])
    def eval(self,c,s,a,j=0,k=0):
        z=c.reshape(self.shape)
        s,a=np.broadcast_arrays(s,a);shape=s.shape
        # The central trajectories generally have distinct radii at one angle.
        if a.size and np.all(a==a.flat[0]):
            return (self.spl(s.ravel(),nu=j)@(z@self.angle([a.flat[0]],k)[0])).reshape(shape)
        return np.einsum("ij,jm,im->i",self.spl(s.ravel(),nu=j),z,self.angle(a.ravel(),k),optimize=True).reshape(shape)

class Bank:
    def __init__(self,spaces,s,theta):
        self.spaces=spaces;self.s=s;self.theta=theta
        self.tables=[sp.tables(s,theta) for sp in spaces]
        count=np.cumsum([0]+[sp.n for sp in spaces])
        self.sl=[slice(a,b) for a,b in zip(count,count[1:])]
        self.n=count[-1]
    def values(self,c,j,k):
        return np.stack([r[j]@c[sl].reshape(sp.shape)@h[k].T
                     for sp,(r,h),sl in zip(self.spaces,self.tables,self.sl)],axis=-1)
    def adj(self,v,j,k):
        return np.concatenate([(r[j].T@v[...,i]@h[k]).ravel()
                               for i,(r,h) in enumerate(self.tables)])
    def scale(self,second):
        ans=[]
        for r,h in self.tables:
            one=np.mean(r[1]**2,axis=0)[:,None]*np.mean(h[0]**2,axis=0)
            one+=np.mean(r[0]**2,axis=0)[:,None]*np.mean(h[1]**2,axis=0)
            one+=second**2*(np.mean(r[2]**2,axis=0)[:,None]*np.mean(h[0]**2,axis=0)
                   +np.mean(r[0]**2,axis=0)[:,None]*np.mean(h[2]**2,axis=0)
                   +2*np.mean(r[1]**2,axis=0)[:,None]*np.mean(h[1]**2,axis=0))
            ans.append(1./np.sqrt(np.maximum(one,1e-8)).ravel())
        return np.concatenate(ans)

class Field:
    def __init__(self,jet,d,extra,spans,modes,s,theta):
        self.jet,self.d,self.extra=jet,d,extra
        self.edges=span_edges(d,jet.base,extra)
        self.s,self.a=np.asarray(s),np.asarray(theta)
        self.frame=np.array([[np.cos(d.gamma),0.,-np.sin(d.gamma)],[0.,1.,0.],
                             [np.sin(d.gamma),0.,np.cos(d.gamma)]])
        self.base=original(jet,d,extra,self.s[:,None],self.a[None,:])@self.frame
        self.F=Bank([Space(self.edges,spans,modes,k) for k in ("x","y","z")],self.s,self.a)
        self.X=Bank([Space(self.edges,spans,modes,k) for k in ("U","W")],self.s,self.a)
    def fields(self,cf):
        return [self.base[...,i,:]+self.F.values(cf,j,k) for i,(j,k) in enumerate(PAIRS)]
    def field_at(self,cf,s,theta):
        z=original(self.jet,self.d,self.extra,s,theta)@self.frame
        for i,(j,k) in enumerate(PAIRS[:3]):
            for c,(sp,sl) in enumerate(zip(self.F.spaces,self.F.sl)):
                z[...,i,c]+=sp.eval(cf[sl],s,theta,j,k)
        return z[...,:3,:]
    def vect(self,c):
        vals=[self.X.values(c,j,k) for j,k in PAIRS[:3]]
        vals[0][...,1]+=1.
        return vals
    def vect_at(self,c,s,a):
        ans=[]
        for j in (0,1):
            u,w=[sp.eval(c[sl],s,a,j,0) for sp,sl in zip(self.X.spaces,self.X.sl)]
            ans.extend([u,w+(j==0)])
        return ans

def geom(f):
    p,u,v,uu,uv,vv=f
    E,F,G=scalar(u,u),scalar(u,v),scalar(v,v)
    n=np.cross(u,v); area=np.linalg.norm(n,axis=-1)
    n=n/row(np.maximum(area,1e-14))
    l,m,h=[scalar(a,n) for a in (uu,uv,vv)]
    H=.5*(G*l-2*F*m+E*h)/np.maximum(area**2,1e-24)
    D=np.sqrt(np.maximum(0.,H*H-(l*h-m*m)/np.maximum(area**2,1e-24)))
    return E,F,G,n,area,np.maximum(abs(H-D),abs(H+D))

def forms(f,x):
    _,u,v,uu,uv,vv=f
    a,ds,dt=x
    ys=row(a[...,0])*uu+row(a[...,1])*uv+row(ds[...,0])*u+row(ds[...,1])*v
    yt=row(a[...,0])*uv+row(a[...,1])*vv+row(dt[...,0])*u+row(dt[...,1])*v
    return np.stack([2*scalar(u,ys),scalar(v,ys)+scalar(u,yt),2*scalar(v,yt)],axis=-1)

def ortho(E,F,G):
    # Gram-Schmidt with the angular direction last. Return a matrix acting
    # on [Kss,Kst,Ktt] and the Frobenius-weighted independent output rows.
    gt=np.maximum(G,1e-14)
    a=F/gt
    e=np.maximum(E-a*F,1e-12)
    mat=np.zeros(E.shape+(3,3))
    mat[...,0,0]=1./e;mat[...,0,1]=-2*a/e;mat[...,0,2]=a*a/e
    mat[...,1,1]=np.sqrt(2./(e*gt));mat[...,1,2]=-a*mat[...,1,1]
    mat[...,2,2]=1./gt
    return mat

def apply(M,b):
    return np.einsum("...ij,...j->...i",M,b)

def pull(M,b):
    return np.einsum("...ij,...i->...j",M,b)

def normop(v):
    a,c,b=v[...,0],v[...,1]/np.sqrt(2),v[...,2]
    return abs((a+b)/2)+np.sqrt(((a-b)/2)**2+c*c)

def xadj(f,v,b):
    _,u,w,uu,uw,ww=f
    # Contractions against dY_s and dY_theta.
    as0=2*row(v[...,0])*u+row(v[...,1])*w
    at=row(v[...,1])*u+2*row(v[...,2])*w
    g=np.stack([scalar(as0,uu)+scalar(at,uw),scalar(as0,uw)+scalar(at,ww)],axis=-1)
    gs=np.stack([scalar(as0,u),scalar(as0,w)],axis=-1)
    gt=np.stack([scalar(at,u),scalar(at,w)],axis=-1)
    return b.adj(g,0,0)+b.adj(gs,1,0)+b.adj(gt,0,1)

def fixed_x(b,cf,reg,iters):
    f=b.fields(cf); E,F,G,*_=geom(f); M=ortho(E,F,G)
    n=b.X.n; z=np.zeros(n)
    mass=np.sqrt(len(b.s)*len(b.a))
    scale=b.X.scale(0);g0=apply(M,forms(f,b.vect(z)))
    def mv(p):
        c=p.ravel()*scale
        x=[b.X.values(c,j,k) for j,k in PAIRS[:3]]
        return np.r_[apply(M,forms(f,x)).ravel()/mass,reg*c]
    def rm(v):
        v=v.ravel()
        gv=pull(M,v[:-n].reshape(g0.shape))/mass
        return scale*(xadj(f,gv,b.X)+reg*v[-n:])
    op=LinearOperator((g0.size+n,n),matvec=mv,rmatvec=rm,dtype=float)
    res=lsmr(op,np.r_[-g0.ravel()/mass,z],atol=2e-9,btol=2e-9,maxiter=iters)
    return res[0]*scale,dict(iterations=int(res[2]),status=int(res[1]),linear_norm=float(res[3]),condition_estimate=float(res[6]))

def positive_field(b,c,margin):
    sp=b.X.spaces[1];full=sp.full_controls@c[b.X.sl[1]].reshape(sp.shape)
    # Treat the constant angular coefficient with its actual sign.
    lower=float(np.min(full[:,0]-np.sum(abs(full[:,1:]),axis=1)))
    alpha=min(1.,(1.-margin)/max(-lower,1.e-15))
    return alpha*c,alpha,1+alpha*lower


class Handles:
    """Independent physical B segment with two long, spatially variable handles.
    The original R742 A surface, cylinder, side, and disk are unchanged.
    The ratio in the projective clock preserves the two material seam jets.
    """
    def __init__(self,jet,right):
        self.jet=jet;self.base=jet.base;self.right=right;self.disk_jet=jet.disk_jet
    def shoulder_jet(self,s,theta,design,normalized):
        if normalized:raise ValueError("two-handle adapter uses physical material input")
        j=self.jet;s,a=np.broadcast_arrays(s,theta)
        out=j.shoulder_jet(s,a,design=design,normalized=False)
        active=(s>self.base.A_LENGTH)&(s<self.base.A_LENGTH+design.join)
        if not active.any():return out
        u=j.J(s[active],s=1.);ang=j.J(a[active],a=1.)
        rb,tb=self.base.rolled_radii(self.base.A_LENGTH,32)
        x0,y,z0,x,cosb,sinb=j.first(rb,tb,ang,design,32)
        left=j.cap_s7((-x-.20)/.55);right=j.cap_s7((x-.65)/.30)
        handle=design.join+design.left_handle*left+self.right*right
        time=j.clock((u-self.base.A_LENGTH)/design.join,handle,design.join)
        S=j.cap_s7(time);v=time.v;sv=self.base.s7(v)
        sv1=140*(v*(1-v))**3;sv2=420*(v*(1-v))**2*(1-2*v)
        G=j.unary(time,v*(1-v)**4*(1+v*(4+v*(10+2.5*v))),1-sv-sv1/2,-sv1-sv2/2)
        xe=self.base.ELL_SCALE*x+design.shift
        xa=(1-S)*x0+S*xe+handle*G*sinb
        za=(1-S)*z0+S*design.end_height+handle*(S-time+G-G*cosb)
        out[active]=j.gather(j.mirror_coordinates(xa,y,za,design,1),len(v))
        return out
