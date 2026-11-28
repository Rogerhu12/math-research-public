"""R775 full-shell material dictionary with hard axial support for every fitted continuous field."""
import numpy as np
import bent_coherent_shear_fields as richer
import r775_nonplanar_compensated_section_two_jets as ref
from r742_tilted_disk_two_jets import J,unary,cap_s7
from r767_preloaded_cap_atlas import root
g=ref.g

def names(level):
    old=richer.names(level);n=level+1
    extra=[("window",k,j,d) for k in range(6) for j in range(n+1) for d in range(2)]
    return old+extra

def grid(ns,nv,order,ind=False):
    ans=richer.grid(ns,nv,order,ind)
    for i,(chart,u,v) in enumerate(ans):
        if chart!="cylinder":continue
        sx=np.unique(np.r_[u,ref.cuts(order)]);ax=np.unique(np.r_[v,
              np.array([0,.012,.024,.036,.048,.06,.10,.20,.265,.37,.5,.63,.735,.80,.90,.94,.952,.964,.976,.988,1])-.5])
        e,x=np.meshgrid(sx,ax,indexing="ij");ans[i]=(chart,e.ravel(),x.ravel())
    return ans

def target(chart,u,v,order):return g.chart_jet(chart,u,v,0.,order)

def base(chart,u,v,t,order,d):return ref.chart_jet(chart,u,v,t,order)

def stack(z,N,K):
    return np.stack([np.broadcast_to(x,(N,K)) for x in z.parts()],axis=1)

def basis(chart,u,v,F,keys,d):
    orig=[q for q in keys if q[0]!="window"];extras=keys[len(orig):]
    B=richer.basis(chart,u,v,F,orig);N=len(u)
    if chart.endswith("+") or (d["heads"]=="both" and chart!="cylinder"):
        return np.zeros((N,6,len(keys)))
    if chart!="cylinder":return np.concatenate((B,np.zeros((N,6,len(extras)))),axis=2)
    x=J(v+.5,a=1.);e=J(u,s=1.);C,H=ref.tangent(e);paid,comp=ref.windows(H)
    if d["heads"]=="both":
        gate=cap_s7(x/.11);jg=J(*(np.broadcast_to(z,(N,))[:,None] for z in gate.parts()))
        B=stack(J(*B.transpose(1,0,2))*jg,N,len(orig))
    h=x*(1-x);bell=64*h*h*h
    left=cap_s7(x/.022)*(1-cap_s7((x-.03)/.055))
    right=cap_s7((1-x)/.022)*(1-cap_s7(((1-x)-.03)/.055))
    ds=[bell*comp,bell*paid,bell*cap_s7((H*H-.68)/.2),left,right,bell]
    degree=max(2,max(q[2] for q in extras));px=richer.cheb(2*x-1,degree)
    X=[]
    for typ,k,j,tr in extras:
        z=ds[k]*px[j]*(C if tr else H)
        X.append(np.stack(np.broadcast_arrays(*z.parts(),u)[:6],axis=1))
    return np.concatenate((B,np.stack(X,axis=2)),axis=2)

def floor(t,order):
    return .5-float(ref.axis_table(float(t),order)[1][-1,0])-ref.end_limits(order)[0]-.008*np.sin(t)

def apply(F,B,Z,yfloor,linear):
    # This routine is valid both for actual material jets and for their
    # fixed-target orthonormal linear transforms at a given material point.
    vals=B@Z;out=F+vals
    s=J(*vals[:,:,1].T);w=J(*F[:,:,1].T)-yfloor
    rad=root(1+s*s)
    positive=s+rad
    # Stable value when s is large negative; rationalized derivatives as well.
    if np.any(s.v<0):
        alt=J(1.)/(rad-s)
        positive=J(*(np.where(s.v<0,a,b) for a,b in zip(alt.parts(),positive.parts())))
    y=J(yfloor)+w*positive
    out[:,:,1]=np.stack(np.broadcast_arrays(*y.parts(),F[:,0,1])[:6],axis=1)
    if not linear:return out,None
    Hprime=positive/rad
    W=w*Hprime;WW=J(*(np.broadcast_to(x,(len(F),))[:,None] for x in W.parts()))
    Y=stack(WW*J(*B.transpose(1,0,2)),len(F),B.shape[2])
    D=np.broadcast_to(B[:,:,:,None],B.shape+(3,)).copy();D[:,:,:,1]=Y
    return out,D

def image(chart,u,v,t,d,order,keys,Z):
    f=base(chart,u,v,t,order,d)
    if not t or chart.endswith("+") or (d["heads"]=="both" and chart!="cylinder"):return f
    B=basis(chart,u,v,target(chart,u,v,order),keys,d)
    return apply(f,B,Z,floor(t,order),False)[0]
